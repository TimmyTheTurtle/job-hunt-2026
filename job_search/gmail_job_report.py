#!/usr/bin/env python3
"""Export a bounded, qualification-ready report from starred Gmail job leads.

The exporter is read-only by default.  STARRED is removed only when callers
pass --unflag-reviewed together with explicit message IDs they actually read.
"""

from __future__ import annotations

import argparse
import base64
import html as html_lib
import json
import re
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "job_search" / "output"
STATE_FILE = ROOT / "job_search" / "ledger" / "gmail_job_report_state.json"
CONTROL_WORDS = {
    "bad match",
    "unsubscribe",
    "pause these emails",
    "no, i don't want",
    "yes, i want",
    "help center",
    "indeed home",
    "edit profile",
}
JOB_DOMAINS = {
    "ashbyhq.com",
    "greenhouse.io",
    "jobs.lever.co",
    "linkedin.com",
    "myworkdayjobs.com",
    "taleo.net",
    "workable.com",
    "indeed.com",
    "cts.indeed.com",
}


def decode_part(data: str) -> str:
    return base64.urlsafe_b64decode(data + "===").decode("utf-8", errors="replace")


def header_value(headers: list[dict], name: str) -> str:
    wanted = name.lower()
    for header in headers:
        if header.get("name", "").lower() == wanted:
            return header.get("value", "")
    return ""


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[dict[str, str]] = []
        self._href = ""
        self._text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        values = dict(attrs)
        self._href = values.get("href") or ""
        self._text = []

    def handle_data(self, data: str) -> None:
        if self._href:
            self._text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "a" and self._href:
            self.links.append({"label": " ".join("".join(self._text).split()), "url": self._href})
            self._href = ""
            self._text = []


def extract_bodies(payload: dict) -> tuple[str, str]:
    """Return concatenated plain text and HTML bodies from a MIME payload."""
    plain: list[str] = []
    rich: list[str] = []
    mime_type = payload.get("mimeType", "")
    data = payload.get("body", {}).get("data", "")
    if data and mime_type == "text/plain":
        plain.append(decode_part(data))
    elif data and mime_type == "text/html":
        rich.append(decode_part(data))
    for part in payload.get("parts", []):
        child_plain, child_html = extract_bodies(part)
        plain.append(child_plain)
        rich.append(child_html)
    return "\n".join(item for item in plain if item), "\n".join(item for item in rich if item)


def html_to_text(source: str) -> str:
    without_scripts = re.sub(r"<script\b[^>]*>.*?</script>|<style\b[^>]*>.*?</style>", " ", source, flags=re.I | re.S)
    text = re.sub(r"<[^>]+>", " ", without_scripts)
    return " ".join(html_lib.unescape(text).split())


def canonicalize_url(url: str) -> str:
    """Remove tracking while retaining a public job-detail URL when possible."""
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    query = parse_qs(parsed.query)
    if host.endswith("cts.indeed.com"):
        return url
    if host.endswith("indeed.com") and parsed.path.endswith("/rc/clk") and query.get("jk"):
        return f"https://www.indeed.com/viewjob?jk={query['jk'][0]}"
    if host.endswith("indeed.com") and parsed.path == "/viewjob" and query.get("jk"):
        return f"https://www.indeed.com/viewjob?jk={query['jk'][0]}"
    if parsed.scheme not in {"http", "https"}:
        return ""
    return url.split("#", 1)[0]


def is_job_link(link: dict[str, str]) -> bool:
    label = link.get("label", "").lower()
    url = link.get("url", "")
    if any(word in label for word in CONTROL_WORDS):
        return False
    parsed = urlparse(url)
    host = parsed.netloc.lower()
    return parsed.scheme in {"http", "https"} and any(host == domain or host.endswith("." + domain) for domain in JOB_DOMAINS)


def extract_job_links(plain_body: str, html_body: str) -> list[dict[str, str]]:
    links: list[dict[str, str]] = []
    parser = LinkParser()
    if html_body:
        parser.feed(html_body)
    for link in parser.links:
        if not is_job_link(link):
            continue
        canonical = canonicalize_url(link["url"])
        if not canonical or canonical in {item["canonical_url"] for item in links}:
            continue
        links.append({"label": link["label"], "source_url": link["url"], "canonical_url": canonical})
    for match in re.findall(r"https?://[^\s<>]+", plain_body):
        candidate = match.rstrip(".,)")
        link = {"label": "", "url": candidate}
        if not is_job_link(link):
            continue
        canonical = canonicalize_url(candidate)
        if canonical and canonical not in {item["canonical_url"] for item in links}:
            links.append({"label": "", "source_url": candidate, "canonical_url": canonical})
    return links


def parse_iso(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)


def lower_bound(last_successful_run: str | None, now: datetime) -> datetime:
    cap = now - timedelta(days=14)
    return max(parse_iso(last_successful_run), cap) if last_successful_run else cap


def load_state() -> dict:
    return json.loads(STATE_FILE.read_text()) if STATE_FILE.exists() else {}


def save_state(state: dict) -> None:
    STATE_FILE.write_text(json.dumps(state, indent=2) + "\n")


def search_messages(service, start: datetime) -> list[dict]:
    query = f"after:{start.strftime('%Y/%m/%d')} -in:spam -in:trash"
    results: list[dict] = []
    page_token = None
    while True:
        kwargs = {"userId": "me", "labelIds": ["STARRED"], "q": query, "maxResults": 100}
        if page_token:
            kwargs["pageToken"] = page_token
        response = service.users().messages().list(**kwargs).execute()
        results.extend(response.get("messages", []))
        page_token = response.get("nextPageToken")
        if not page_token:
            return results


def collect_message(service, message_id: str, start: datetime) -> dict | None:
    message = service.users().messages().get(userId="me", id=message_id, format="full").execute()
    received = datetime.fromtimestamp(int(message.get("internalDate", "0")) / 1000, tz=timezone.utc)
    if received <= start:
        return None
    payload = message.get("payload", {})
    plain, rich = extract_bodies(payload)
    visible_text = plain.strip() or html_to_text(rich)
    headers = payload.get("headers", [])
    return {
        "message_id": message_id,
        "thread_id": message.get("threadId", ""),
        "received_at": received.isoformat(),
        "from": header_value(headers, "From"),
        "subject": header_value(headers, "Subject"),
        "preview": visible_text[:500],
        "job_links": extract_job_links(plain, rich),
    }


def write_report(report_date: str, start: datetime, messages: list[dict]) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / f"gmail_job_report_{report_date}.md"
    lines = [
        f"# Gmail Job Report - {report_date}",
        "",
        "This report is generated from starred Gmail messages newer than the last successful report and no older than 14 days.",
        "",
        f"Search lower bound: `{start.isoformat()}`",
        f"Messages with exact timestamps after the bound: **{len(messages)}**",
        "",
        "## Candidate Messages",
        "",
    ]
    if not messages:
        lines.append("No starred messages matched the bounded window.")
    for index, message in enumerate(messages, 1):
        lines.extend([
            f"### {index}. {message['subject'] or '(no subject)'}",
            "",
            f"- Message ID: `{message['message_id']}`",
            f"- Received: {message['received_at']}",
            f"- From: {message['from']}",
            f"- Preview: {message['preview']}",
            "- Recovered public job links:",
        ])
        if message["job_links"]:
            lines.extend(f"  - [{item['canonical_url']}]({item['canonical_url']})" for item in message["job_links"])
        else:
            lines.append("  - None recovered")
        lines.append("")
    path.write_text("\n".join(lines) + "\n")
    return path


def unflag_reviewed(service, message_ids: list[str]) -> None:
    for message_id in message_ids:
        service.users().messages().modify(
            userId="me", id=message_id, body={"removeLabelIds": ["STARRED"]}
        ).execute()


def find_starred_subjects(service, subjects: list[str]) -> list[tuple[str, str]]:
    """Find exact starred messages for an explicit cleanup request."""
    if not subjects:
        return []
    query = 'is:starred -in:spam -in:trash {' + " ".join(
        f'subject:"{subject}"' for subject in subjects
    ) + "}"
    refs = service.users().messages().list(userId="me", q=query, maxResults=100).execute().get("messages", [])
    wanted = set(subjects)
    matches: list[tuple[str, str]] = []
    for reference in refs:
        message = service.users().messages().get(
            userId="me",
            id=reference["id"],
            format="metadata",
            metadataHeaders=["Subject"],
        ).execute()
        subject = header_value(message.get("payload", {}).get("headers", []), "Subject")
        if subject in wanted:
            matches.append((reference["id"], subject))
    return matches


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-date", default=datetime.now().date().isoformat())
    parser.add_argument("--since", help="Explicit initial lower bound, ISO-8601 with timezone")
    parser.add_argument("--reviewed-id", action="append", default=[])
    parser.add_argument("--reviewed-subject", action="append", default=[])
    parser.add_argument("--unflag-reviewed", action="store_true")
    return parser


def main() -> None:
    try:
        from .gmail_auth import get_gmail_service
    except ImportError:  # pragma: no cover - supports direct execution by the runner
        from gmail_auth import get_gmail_service

    args = build_parser().parse_args()
    if args.unflag_reviewed and not (args.reviewed_id or args.reviewed_subject):
        raise SystemExit("--unflag-reviewed requires --reviewed-id or --reviewed-subject")
    now = datetime.now(timezone.utc)
    state = load_state()
    start = parse_iso(args.since) if args.since else lower_bound(state.get("last_successful_run"), now)
    service = get_gmail_service()
    messages: list[dict] = []
    for reference in search_messages(service, start):
        message = collect_message(service, reference["id"], start)
        if message:
            messages.append(message)
    messages.sort(key=lambda item: item["received_at"], reverse=True)
    report_path = write_report(args.run_date, start, messages)
    state.update({"last_successful_run": now.isoformat(), "last_report": str(report_path.relative_to(ROOT))})
    if args.unflag_reviewed:
        known_ids = {message["message_id"] for message in messages}
        unknown_ids = set(args.reviewed_id) - known_ids
        if unknown_ids:
            raise SystemExit(f"Reviewed IDs were not in this report: {', '.join(sorted(unknown_ids))}")
        subject_matches = find_starred_subjects(service, args.reviewed_subject)
        subject_ids = [message_id for message_id, _ in subject_matches]
        unflag_reviewed(service, args.reviewed_id + subject_ids)
        all_reviewed_ids = args.reviewed_id + subject_ids
        state["reviewed_message_ids"] = sorted(set(state.get("reviewed_message_ids", [])) | set(all_reviewed_ids))
        state["last_unflagged_at"] = now.isoformat()
    save_state(state)
    print(f"Report: {report_path}")
    print(f"Messages: {len(messages)}")
    if args.unflag_reviewed:
        print(f"Unflagged reviewed messages: {len(args.reviewed_id) + len(subject_matches)}")


if __name__ == "__main__":
    main()
