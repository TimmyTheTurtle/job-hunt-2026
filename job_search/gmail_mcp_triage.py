#!/usr/bin/env python3
"""Deterministically transform Gmail MCP captures into job-triage reports.

This module never connects to Gmail. A chat agent obtains the message data and
performs approved label changes through the connected Gmail MCP tools. The
script owns only the bounded-window calculation, validation, URL recovery,
qualification scoring, report rendering, and local state.
"""

from __future__ import annotations

import argparse
import base64
import json
import re
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse

try:  # Supports both `python job_search/gmail_mcp_triage.py` and unittest imports.
    from .qualification import evaluate_qualifications, load_candidate_profile, qualification_recommendation, summarize_items
except ImportError:  # pragma: no cover - direct script execution
    from qualification import evaluate_qualifications, load_candidate_profile, qualification_recommendation, summarize_items


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "job_search" / "output"
STATE_FILE = ROOT / "job_search" / "ledger" / "gmail_mcp_triage_state.json"
LEGACY_STATE_FILE = ROOT / "job_search" / "ledger" / "gmail_job_report_state.json"
PROFILE_FILE = ROOT / "job_search" / "candidate_profile.json"
JOB_DOMAINS = {"ashbyhq.com", "greenhouse.io", "jobs.lever.co", "linkedin.com", "myworkdayjobs.com", "taleo.net", "workable.com", "indeed.com", "cts.indeed.com"}
CONTROL_WORDS = {"bad match", "unsubscribe", "pause these emails", "no, i don't want", "yes, i want", "help center", "indeed home", "edit profile"}


def parse_iso(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)


def parse_message_time(value: str | int) -> datetime:
    if isinstance(value, int) or (isinstance(value, str) and value.isdigit()):
        return datetime.fromtimestamp(int(value) / 1000, tz=timezone.utc)
    return parse_iso(str(value))


def lower_bound(last_successful_run: str | None, now: datetime) -> datetime:
    cap = now - timedelta(days=14)
    return max(parse_iso(last_successful_run), cap) if last_successful_run else cap


def gmail_request(start: datetime) -> dict[str, Any]:
    return {
        "label_ids": ["STARRED"],
        "query": f"after:{start.strftime('%Y/%m/%d')} -in:spam -in:trash",
        "exact_lower_bound": start.isoformat(),
    }


def header_value(headers: list[dict[str, Any]], name: str) -> str:
    wanted = name.lower()
    for header in headers:
        if str(header.get("name", "")).lower() == wanted:
            return str(header.get("value", ""))
    return ""


def decode_text(value: str) -> str:
    return base64.urlsafe_b64decode(value + "===").decode("utf-8", errors="replace")


def extract_bodies(payload: dict[str, Any]) -> tuple[str, str]:
    """Read decoded MCP text MIME content, tolerating raw Gmail payload data."""
    plain: list[str] = []
    rich: list[str] = []
    mime_type = str(payload.get("mime_type", payload.get("mimeType", ""))).lower()
    body = payload.get("body") or {}
    content = body.get("content")
    if content is None and body.get("data"):
        content = decode_text(str(body["data"]))
    if content:
        (plain if mime_type == "text/plain" else rich if mime_type == "text/html" else plain).append(str(content))
    for part in payload.get("parts") or []:
        child_plain, child_html = extract_bodies(part)
        plain.append(child_plain)
        rich.append(child_html)
    return "\n".join(item for item in plain if item), "\n".join(item for item in rich if item)


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[dict[str, str]] = []
        self.href = ""
        self.text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "a":
            self.href = dict(attrs).get("href") or ""
            self.text = []

    def handle_data(self, data: str) -> None:
        if self.href:
            self.text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "a" and self.href:
            self.links.append({"label": " ".join("".join(self.text).split()), "url": self.href})
            self.href, self.text = "", []


def canonicalize_url(url: str) -> str:
    parsed = urlparse(url)
    host, query = parsed.netloc.lower(), parse_qs(parsed.query)
    if host.endswith("cts.indeed.com"):
        return url
    if host.endswith("indeed.com") and parsed.path in {"/rc/clk", "/viewjob"} and query.get("jk"):
        return f"https://www.indeed.com/viewjob?jk={query['jk'][0]}"
    return url.split("#", 1)[0] if parsed.scheme in {"http", "https"} else ""


def is_job_link(link: dict[str, str]) -> bool:
    if any(word in link.get("label", "").lower() for word in CONTROL_WORDS):
        return False
    parsed = urlparse(link.get("url", ""))
    host = parsed.netloc.lower()
    return parsed.scheme in {"http", "https"} and any(host == domain or host.endswith("." + domain) for domain in JOB_DOMAINS)


def extract_job_links(plain: str, rich: str) -> list[dict[str, str]]:
    parser = LinkParser()
    parser.feed(rich)
    candidates = parser.links + [{"label": "", "url": match.rstrip(".,)")} for match in re.findall(r"https?://[^\s<>]+", plain)]
    found: list[dict[str, str]] = []
    for link in candidates:
        if not is_job_link(link):
            continue
        canonical = canonicalize_url(link["url"])
        if canonical and canonical not in {item["canonical_url"] for item in found}:
            found.append({"label": link["label"], "source_url": link["url"], "canonical_url": canonical})
    return found


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_state() -> dict[str, Any]:
    """Use the prior report boundary once, then keep MCP workflow state separate."""
    if STATE_FILE.exists():
        return load_json(STATE_FILE)
    if LEGACY_STATE_FILE.exists():
        legacy = load_json(LEGACY_STATE_FILE)
        return {"last_successful_run": legacy.get("last_successful_run")}
    return {}


def address_text(enrichment: dict[str, Any] | None) -> list[str]:
    address = (enrichment or {}).get("employer_address") or {}
    if address.get("status") != "verified":
        return ["- Employer physical address: Not verified"]
    required = ("address", "address_type", "source_url", "verified_at")
    if any(not address.get(key) for key in required):
        return ["- Employer physical address: Invalid verified-address record"]
    return [
        f"- Employer physical address ({address['address_type']}): {address['address']}",
        f"- Address source: {address['source_url']} (verified {address['verified_at']})",
    ]


def message_record(message: dict[str, Any], start: datetime) -> dict[str, Any] | None:
    received = parse_message_time(message["internal_date"])
    if received <= start:
        return None
    payload = message.get("payload") or {}
    plain, rich = extract_bodies(payload)
    headers = payload.get("headers") or []
    return {
        "message_id": message["id"],
        "thread_id": message.get("thread_id", ""),
        "received_at": received.isoformat(),
        "from": header_value(headers, "From"),
        "subject": header_value(headers, "Subject"),
        "preview": (plain or re.sub(r"<[^>]+>", " ", rich)).strip()[:500],
        "job_links": extract_job_links(plain, rich),
    }


def render_report(report_date: str, start: datetime, records: list[dict[str, Any]], enrichments: dict[str, dict[str, Any]]) -> str:
    lines = [f"# Gmail MCP Job Report - {report_date}", "", "Gmail data was retrieved through the connected Gmail MCP tools. This deterministic report contains no Gmail credentials or network calls.", "", f"Search lower bound: `{start.isoformat()}`", f"Messages after exact timestamp filter: **{len(records)}**", "", "## Ranked Verified Postings", ""]
    profile = load_candidate_profile(PROFILE_FILE)
    ranked: list[tuple[int, str, dict[str, Any], dict[str, Any]]] = []
    for url, posting in enrichments.items():
        qualification = evaluate_qualifications(posting, profile)
        recommendation = qualification_recommendation(int(posting.get("relevance_score", 0)), bool(posting.get("rejected", False)), qualification, str(posting.get("role_focus", "explicit")))
        ranked.append((qualification["qualification_score"], url, posting, {**qualification, "recommendation": recommendation}))
    if not ranked:
        lines.append("No full-posting enrichments supplied. Gmail leads remain unverified until a human captures the employer/ATS posting.")
    for score, url, posting, qualification in sorted(ranked, reverse=True):
        lines.extend([f"### {posting.get('title', 'Untitled role')} — {posting.get('company', 'Unknown company')}", "", f"- Canonical posting: {url}", f"- Verification source: {posting.get('source_url', 'Not provided')}", f"- Qualification: {qualification['recommendation']} ({score}/100)", f"- Requirements status: {qualification['description_status']}", f"- Material gaps: {summarize_items(qualification['gaps'])}"])
        lines.extend(address_text(posting))
        lines.append("")
    lines.extend(["## Candidate Messages", ""])
    if not records:
        lines.append("No starred messages matched the bounded window.")
    for index, record in enumerate(records, 1):
        lines.extend([f"### {index}. {record['subject'] or '(no subject)'}", "", f"- Message ID: `{record['message_id']}`", f"- Received: {record['received_at']}", f"- From: {record['from']}", f"- Preview: {record['preview']}", "- Recovered public job links:"])
        if record["job_links"]:
            for link in record["job_links"]:
                lines.append(f"  - [{link['canonical_url']}]({link['canonical_url']})")
                lines.extend(f"    {item}" for item in address_text(enrichments.get(link["canonical_url"])))
        else:
            lines.append("  - None recovered")
        lines.append("")
    return "\n".join(lines) + "\n"


def command_window(args: argparse.Namespace) -> None:
    now = parse_iso(args.now) if args.now else datetime.now(timezone.utc)
    state = load_state()
    start = lower_bound(state.get("last_successful_run"), now)
    print(json.dumps(gmail_request(start), indent=2))


def command_report(args: argparse.Namespace) -> None:
    capture = load_json(Path(args.input))
    now = parse_iso(args.now) if args.now else datetime.now(timezone.utc)
    state = load_state()
    start = lower_bound(state.get("last_successful_run"), now)
    records = [record for message in capture.get("messages", []) if (record := message_record(message, start))]
    records.sort(key=lambda item: item["received_at"], reverse=True)
    enrichments = {item["canonical_url"]: item for item in capture.get("posting_enrichments", []) if item.get("canonical_url")}
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    report_date = args.run_date or now.date().isoformat()
    path = OUTPUT_DIR / f"gmail_mcp_job_report_{report_date}.md"
    path.write_text(render_report(report_date, start, records, enrichments), encoding="utf-8")
    if not args.no_update_state:
        STATE_FILE.write_text(json.dumps({"last_successful_run": now.isoformat(), "last_report": str(path.relative_to(ROOT))}, indent=2) + "\n", encoding="utf-8")
    print(f"Report: {path}")
    print(f"Messages: {len(records)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(required=True)
    window = subparsers.add_parser("window", help="emit the exact Gmail MCP search request")
    window.add_argument("--now", help="ISO-8601 timestamp for reproducible runs")
    window.set_defaults(func=command_window)
    report = subparsers.add_parser("report", help="render a report from a Gmail MCP capture JSON file")
    report.add_argument("--input", required=True, help="path to a capture following gmail_mcp_capture_schema.json")
    report.add_argument("--run-date")
    report.add_argument("--now", help="ISO-8601 timestamp for reproducible runs")
    report.add_argument("--no-update-state", action="store_true")
    report.set_defaults(func=command_report)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
