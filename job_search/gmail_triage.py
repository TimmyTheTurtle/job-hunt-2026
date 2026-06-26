#!/usr/bin/env python3
"""
Gmail inbox triage for job-hunt emails.

Pass 1 (rules, free):
  Detects bulk job-site digests by sender domain + subject pattern.
  Files to Jobs/Digests and marks read.

Pass 2 (GPT-4o-mini, per email):
  Reads full body of surviving emails.
  Classifies into role tier or category label.
  Unknown emails are left in inbox and not marked read.

State is tracked in job_search/ledger/gmail_last_run.json so each run
picks up only new messages. Multi-machine safe: Gmail label application
is idempotent, so a rare duplicate run just re-labels — no harm done.
"""

from __future__ import annotations

import base64
import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

from openai import OpenAI

from gmail_auth import get_gmail_service


ROOT = Path(__file__).resolve().parents[1]
SECRETS = ROOT / "secrets"
LEDGER_FILE = ROOT / "job_search" / "ledger" / "gmail_last_run.json"

LABEL_NAMES = [
    "Jobs/Digests",
    "Jobs/Tier1",
    "Jobs/Tier2",
    "Jobs/Tier3",
    "Jobs/Recruiter-Outreach",
    "Jobs/Applied",
    "Jobs/Rejections",
    "Jobs/Interviews",
]

# Domains that send bulk digest emails (not individual recruiter messages).
# A sender from these domains only triggers Pass 1 when the subject *also*
# matches a digest pattern — so real LinkedIn InMail still reaches Pass 2.
DIGEST_DOMAINS = {
    "linkedin.com",
    "ziprecruiter.com",
    "indeed.com",
    "glassdoor.com",
    "monster.com",
    "dice.com",
    "careerbuilder.com",
    "simplyhired.com",
    "wellfound.com",
    "themuse.com",
    "flexjobs.com",
    "builtin.com",
}

DIGEST_SUBJECT_RE = re.compile(
    r"\d+\s+new\s+jobs?"
    r"|jobs?\s+for\s+you"
    r"|jobs?\s+you\s+might\s+like"
    r"|new\s+jobs?\s+matching"
    r"|job\s+recommendations?"
    r"|job\s+alert"
    r"|jobs?\s+matching\s+your"
    r"|recommended\s+jobs?"
    r"|top\s+jobs?"
    r"|jobs?\s+near\s+you"
    r"|similar\s+jobs?"
    r"|\d+\s+jobs?\s+match"
    r"|your\s+weekly\s+jobs?"
    r"|daily\s+job\s+digest",
    re.IGNORECASE,
)

CLASSIFICATION_SYSTEM_PROMPT = """\
You are a job email classifier for a software engineer's job-hunt inbox.

Given the body of a single email, classify it into exactly one category:

- Tier1: Applied AI systems, AI solutions or automation, LLM/RAG, document
  intelligence, AI workflow automation, evals or quality gates, human-in-loop
  systems, compliance/legal/insurance/regulatory AI engineering, or software
  roles building production-minded AI boundaries.
- Tier2: Strong adjacent software, solutions, implementation, or platform roles,
  especially C#/.NET/SaaS, workflow, integration, compliance, or document-heavy
  systems with meaningful engineering depth.
- Tier3: Broad web, reporting, configuration, business systems, or
  operations-adjacent technical work without meaningful AI, document workflow,
  compliance, or systems-depth value.
- Recruiter-Outreach: A recruiter reaching out but no full job description yet.
- Applied: Application confirmation or acknowledgment from a company or ATS.
- Rejection: Rejection notice or "we've moved forward with other candidates."
- Interview: Interview invitation, scheduling request, or next-step coordination.
- Unknown: Cannot determine the category from this email.

Respond with ONLY the category name — no punctuation, no explanation.\
"""

CATEGORY_TO_LABEL: dict[str, str] = {
    "Tier1": "Jobs/Tier1",
    "Tier2": "Jobs/Tier2",
    "Tier3": "Jobs/Tier3",
    "Recruiter-Outreach": "Jobs/Recruiter-Outreach",
    "Applied": "Jobs/Applied",
    "Rejection": "Jobs/Rejections",
    "Interview": "Jobs/Interviews",
}

VALID_CATEGORIES = set(CATEGORY_TO_LABEL) | {"Unknown"}


# ── Credentials ──────────────────────────────────────────────────────────────

def load_openai_key() -> str:
    """Read OpenAI key from env var or secrets/credentials.txt."""
    if key := os.environ.get("OPENAI_API_KEY"):
        return key
    creds_file = SECRETS / "credentials.txt"
    if creds_file.exists():
        for line in creds_file.read_text().splitlines():
            if line.startswith("openai_api_key:"):
                return line.split(":", 1)[1].strip()
    raise SystemExit(
        "\nOpenAI API key not found.\n"
        "Either set the OPENAI_API_KEY environment variable, or add this line\n"
        "to secrets/credentials.txt:\n\n"
        "  openai_api_key: sk-...\n"
    )


# ── Ledger ────────────────────────────────────────────────────────────────────

def load_ledger() -> dict:
    if LEDGER_FILE.exists():
        return json.loads(LEDGER_FILE.read_text())
    return {}


def save_ledger(data: dict) -> None:
    LEDGER_FILE.write_text(json.dumps(data, indent=2))


# ── Gmail label management ────────────────────────────────────────────────────

def get_or_create_labels(service) -> dict[str, str]:
    """Return {label_name: label_id}, auto-creating any missing labels."""
    existing = {
        lbl["name"]: lbl["id"]
        for lbl in service.users().labels().list(userId="me").execute().get("labels", [])
    }
    label_ids: dict[str, str] = {}
    for name in LABEL_NAMES:
        if name in existing:
            label_ids[name] = existing[name]
        else:
            body = {
                "name": name,
                "labelListVisibility": "labelShow",
                "messageListVisibility": "show",
            }
            created = service.users().labels().create(userId="me", body=body).execute()
            label_ids[name] = created["id"]
            print(f"  Created label: {name}")
    return label_ids


# ── Message helpers ───────────────────────────────────────────────────────────

def header_value(headers: list[dict], name: str) -> str:
    name_lower = name.lower()
    for h in headers:
        if h["name"].lower() == name_lower:
            return h["value"]
    return ""


def sender_base_domain(from_header: str) -> str:
    """Extract the root domain (last two segments) from a From header."""
    match = re.search(r"@([\w.-]+)", from_header or "")
    if not match:
        return ""
    parts = match.group(1).lower().split(".")
    return ".".join(parts[-2:]) if len(parts) >= 2 else parts[0]


def is_digest(from_header: str, subject: str) -> bool:
    """True if this looks like a bulk job-site digest rather than a real contact."""
    domain = sender_base_domain(from_header)
    return domain in DIGEST_DOMAINS and bool(DIGEST_SUBJECT_RE.search(subject or ""))


def get_body_text(payload: dict) -> str:
    """Recursively extract the first plain-text body part from a Gmail payload."""
    mime_type = payload.get("mimeType", "")
    if mime_type == "text/plain":
        data = payload.get("body", {}).get("data", "")
        if data:
            return base64.urlsafe_b64decode(data + "==").decode("utf-8", errors="replace")
    if mime_type.startswith("multipart/"):
        for part in payload.get("parts", []):
            text = get_body_text(part)
            if text:
                return text
    return ""


def apply_label_mark_read(service, msg_id: str, label_id: str) -> None:
    service.users().messages().modify(
        userId="me",
        id=msg_id,
        body={
            "addLabelIds": [label_id],
            "removeLabelIds": ["UNREAD"],
        },
    ).execute()


# ── Inbox fetch ───────────────────────────────────────────────────────────────

def fetch_inbox_messages(service, after_unix: int) -> list[dict]:
    """Page through INBOX messages newer than after_unix (Unix seconds)."""
    query = f"in:inbox after:{after_unix}"
    messages: list[dict] = []
    page_token = None
    while True:
        kwargs: dict = {"userId": "me", "q": query, "maxResults": 100}
        if page_token:
            kwargs["pageToken"] = page_token
        result = service.users().messages().list(**kwargs).execute()
        messages.extend(result.get("messages", []))
        page_token = result.get("nextPageToken")
        if not page_token:
            break
    return messages


def get_message_details(service, msg_id: str) -> dict:
    return service.users().messages().get(userId="me", id=msg_id, format="full").execute()


# ── LLM classification ────────────────────────────────────────────────────────

def classify_email(client: OpenAI, body: str) -> str:
    """Call GPT-4o-mini to classify the email body. Returns a category string."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": CLASSIFICATION_SYSTEM_PROMPT},
            {"role": "user", "content": body[:4000]},  # keep well within token budget
        ],
        max_tokens=10,
        temperature=0,
    )
    result = response.choices[0].message.content.strip()
    return result if result in VALID_CATEGORIES else "Unknown"


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    print("Gmail Triage — starting")

    ledger = load_ledger()
    last_ts: int = ledger.get("last_timestamp", 0)
    if not last_ts:
        last_ts = int((datetime.now(timezone.utc) - timedelta(days=7)).timestamp())
        print("  First run — scanning last 7 days")
    else:
        from_dt = datetime.fromtimestamp(last_ts, tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        print(f"  Scanning since {from_dt}")

    service = get_gmail_service()
    label_ids = get_or_create_labels(service)
    openai_client = OpenAI(api_key=load_openai_key())

    messages = fetch_inbox_messages(service, last_ts)
    if not messages:
        print("  No new inbox messages.")
        save_ledger({**ledger, "last_run": datetime.now(timezone.utc).isoformat()})
        return

    print(f"  Found {len(messages)} message(s) to evaluate\n")

    counts: dict[str, int] = {"digest": 0, "unknown": 0, "error": 0}
    classified: dict[str, int] = {}
    newest_ts = last_ts

    for msg_ref in messages:
        msg_id = msg_ref["id"]
        try:
            msg = get_message_details(service, msg_id)
            headers = msg.get("payload", {}).get("headers", [])
            from_hdr = header_value(headers, "From")
            subject = header_value(headers, "Subject")
            internal_ts = int(msg.get("internalDate", 0)) // 1000  # ms → s
            if internal_ts > newest_ts:
                newest_ts = internal_ts

            # Pass 1: bulk digest detection (free)
            if is_digest(from_hdr, subject):
                apply_label_mark_read(service, msg_id, label_ids["Jobs/Digests"])
                counts["digest"] += 1
                continue

            # Pass 2: full-body LLM classification
            body = get_body_text(msg.get("payload", {}))
            if not body.strip():
                counts["unknown"] += 1
                print(f"  [no body]  {subject[:70]}")
                continue

            category = classify_email(openai_client, body)
            label_name = CATEGORY_TO_LABEL.get(category)
            if label_name:
                apply_label_mark_read(service, msg_id, label_ids[label_name])
                classified[category] = classified.get(category, 0) + 1
                print(f"  [{category:<20}]  {subject[:60]}")
            else:
                # Unknown — leave in inbox, do not mark read
                counts["unknown"] += 1
                print(f"  [Unknown             ]  {subject[:60]}")

        except Exception as exc:
            print(f"  [Error] {msg_id}: {exc}", file=sys.stderr)
            counts["error"] += 1

    # Persist ledger with latest processed timestamp
    save_ledger({
        **ledger,
        "last_timestamp": newest_ts,
        "last_run": datetime.now(timezone.utc).isoformat(),
    })

    # Print summary
    print("\n── Summary ──────────────────────────────────────────")
    print(f"  Digests filed & marked read:  {counts['digest']}")
    for cat in ("Tier1", "Tier2", "Tier3", "Recruiter-Outreach", "Applied", "Rejection", "Interview"):
        if cat in classified:
            print(f"  {cat:<26}  {classified[cat]}")
    print(f"  Left in inbox (Unknown):      {counts['unknown']}")
    if counts["error"]:
        print(f"  Errors:                       {counts['error']}")
    print("─────────────────────────────────────────────────────")


if __name__ == "__main__":
    main()
