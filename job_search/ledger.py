#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
APPLICATIONS_DIR = ROOT / "applications"
LEDGER_DIR = ROOT / "job_search" / "ledger"
TRANSACTIONS_PATH = LEDGER_DIR / "transactions.jsonl"
STATE_PATH = LEDGER_DIR / "state.json"
SUMMARY_PATH = LEDGER_DIR / "summary.md"
TIMEZONE = ZoneInfo("America/New_York")

KNOWN_STATUSES = {"surfaced", "saved", "dismissed", "applied"}
BLOCKING_STATUSES = {"surfaced", "saved", "dismissed", "applied"}


def now_iso() -> str:
    return datetime.now(TIMEZONE).isoformat()


def ensure_ledger_dir() -> None:
    LEDGER_DIR.mkdir(parents=True, exist_ok=True)


def write_text_atomic(path: Path, content: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(content, encoding="utf-8")
    tmp.replace(path)


def write_json_atomic(path: Path, payload: dict[str, Any]) -> None:
    write_text_atomic(path, json.dumps(payload, indent=2, sort_keys=True) + "\n")


def normalize_url(url: str) -> str:
    if not url:
        return ""
    split = urlsplit(url.strip())
    query = [(k, v) for k, v in parse_qsl(split.query, keep_blank_values=True) if not k.lower().startswith("utm_")]
    normalized_path = split.path.rstrip("/") or "/"
    return urlunsplit((split.scheme.lower(), split.netloc.lower(), normalized_path, urlencode(query), ""))


def safe_str(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def existing_application_urls() -> set[str]:
    urls: set[str] = set()
    for path in APPLICATIONS_DIR.glob("*/job_description.md"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in re.findall(r"https?://\S+", text):
            urls.add(normalize_url(match.rstrip(")]>")))
    return urls


def load_transactions() -> list[dict[str, Any]]:
    ensure_ledger_dir()
    if not TRANSACTIONS_PATH.exists():
        return []

    transactions: list[dict[str, Any]] = []
    for line in TRANSACTIONS_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        transactions.append(json.loads(line))
    return transactions


def materialize_state(transactions: list[dict[str, Any]]) -> dict[str, Any]:
    jobs: dict[str, dict[str, Any]] = {}
    recent_transactions: list[dict[str, Any]] = []

    for transaction in transactions:
        tx_id = transaction.get("transaction_id", "")
        timestamp = transaction.get("timestamp", "")
        actor = transaction.get("actor", "")
        kind = transaction.get("kind", "")
        events = transaction.get("events", [])

        recent_transactions.append(
            {
                "transaction_id": tx_id,
                "timestamp": timestamp,
                "actor": actor,
                "kind": kind,
                "event_count": len(events),
            }
        )

        for event in events:
            normalized_url = event.get("normalized_url") or normalize_url(safe_str(event.get("job_url")))
            if not normalized_url:
                continue

            status = safe_str(event.get("status")) or "surfaced"
            if status not in KNOWN_STATUSES:
                status = "surfaced"

            job = jobs.setdefault(
                normalized_url,
                {
                    "normalized_url": normalized_url,
                    "job_url": safe_str(event.get("job_url")),
                    "company": "",
                    "title": "",
                    "location": "",
                    "status": "surfaced",
                    "first_seen_at": timestamp,
                    "last_seen_at": "",
                    "last_decision_at": "",
                    "seen_count": 0,
                    "sites": [],
                    "query_labels": [],
                    "score": None,
                    "recommendation": "",
                    "note": "",
                    "last_actor": actor,
                    "last_transaction_id": tx_id,
                },
            )

            for field in ("job_url", "company", "title", "location", "recommendation"):
                value = safe_str(event.get(field))
                if value:
                    job[field] = value

            score = event.get("score")
            if score is not None:
                job["score"] = score

            note = safe_str(event.get("note"))
            if note:
                job["note"] = note

            sites = event.get("sites", [])
            if sites:
                merged_sites = set(job["sites"])
                merged_sites.update(str(item).strip() for item in sites if str(item).strip())
                job["sites"] = sorted(merged_sites)

            query_labels = event.get("query_labels", [])
            if query_labels:
                merged_labels = set(job["query_labels"])
                merged_labels.update(str(item).strip() for item in query_labels if str(item).strip())
                job["query_labels"] = sorted(merged_labels)

            if status == "surfaced":
                job["seen_count"] += 1
                job["last_seen_at"] = timestamp
                if job["status"] not in {"applied", "dismissed", "saved"}:
                    job["status"] = "surfaced"
            else:
                job["status"] = status
                job["last_decision_at"] = timestamp

            job["last_actor"] = actor
            job["last_transaction_id"] = tx_id

    ordered_jobs = sorted(
        jobs.values(),
        key=lambda item: (
            {"surfaced": 0, "saved": 1, "applied": 2, "dismissed": 3}.get(item["status"], 9),
            item.get("company", "").lower(),
            item.get("title", "").lower(),
        ),
    )

    status_counts = {status: 0 for status in KNOWN_STATUSES}
    for job in ordered_jobs:
        status_counts[job["status"]] = status_counts.get(job["status"], 0) + 1

    return {
        "generated_at": now_iso(),
        "job_count": len(ordered_jobs),
        "status_counts": status_counts,
        "jobs": ordered_jobs,
        "recent_transactions": recent_transactions[-20:],
    }


def write_summary(state: dict[str, Any]) -> None:
    lines = [
        "# Search Ledger Summary",
        "",
        f"- Generated: {state['generated_at']}",
        f"- Total tracked jobs: {state['job_count']}",
        f"- Surfaced: {state['status_counts'].get('surfaced', 0)}",
        f"- Saved: {state['status_counts'].get('saved', 0)}",
        f"- Applied: {state['status_counts'].get('applied', 0)}",
        f"- Dismissed: {state['status_counts'].get('dismissed', 0)}",
        "",
        "Source of truth: `transactions.jsonl`",
        "",
    ]

    sections = [
        ("surfaced", "Open Surfaced Jobs"),
        ("saved", "Saved Jobs"),
        ("applied", "Applied Jobs"),
        ("dismissed", "Dismissed Jobs"),
    ]

    for status, title in sections:
        items = [job for job in state["jobs"] if job["status"] == status]
        if not items:
            continue
        lines.append(f"## {title}")
        lines.append("")
        for job in items[:40]:
            lines.append(f"### {job.get('company') or 'Unknown company'} - {job.get('title') or 'Unknown title'}")
            if job.get("location"):
                lines.append(f"- Location: {job['location']}")
            if job.get("recommendation"):
                lines.append(f"- Last recommendation: {job['recommendation']}")
            if job.get("score") is not None:
                lines.append(f"- Last score: {job['score']}")
            if job.get("sites"):
                lines.append(f"- Sites: {', '.join(job['sites'])}")
            if job.get("query_labels"):
                lines.append(f"- Query labels: {', '.join(job['query_labels'])}")
            if job.get("note"):
                lines.append(f"- Note: {job['note']}")
            if job.get("first_seen_at"):
                lines.append(f"- First seen: {job['first_seen_at']}")
            if job.get("last_seen_at"):
                lines.append(f"- Last seen: {job['last_seen_at']}")
            if job.get("last_decision_at"):
                lines.append(f"- Last decision: {job['last_decision_at']}")
            lines.append(f"- Posting URL: {job['job_url'] or job['normalized_url']}")
            lines.append("")

    if state["recent_transactions"]:
        lines.append("## Recent Transactions")
        lines.append("")
        for tx in reversed(state["recent_transactions"][-10:]):
            lines.append(
                f"- `{tx['timestamp']}` `{tx['kind']}` by `{tx['actor']}`: {tx['event_count']} event(s) [{tx['transaction_id']}]"
            )

    write_text_atomic(SUMMARY_PATH, "\n".join(lines).rstrip() + "\n")


def rebuild_views() -> dict[str, Any]:
    state = materialize_state(load_transactions())
    write_json_atomic(STATE_PATH, state)
    write_summary(state)
    return state


def state_map() -> dict[str, dict[str, Any]]:
    return {job["normalized_url"]: job for job in materialize_state(load_transactions())["jobs"]}


def record_transaction(
    *,
    actor: str,
    kind: str,
    events: list[dict[str, Any]],
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    ensure_ledger_dir()
    timestamp = now_iso()
    transaction_id = f"tx_{datetime.now(TIMEZONE).strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"

    normalized_events: list[dict[str, Any]] = []
    for event in events:
        job_url = safe_str(event.get("job_url"))
        normalized_url = event.get("normalized_url") or normalize_url(job_url)
        if not normalized_url:
            continue
        status = safe_str(event.get("status")) or "surfaced"
        if status not in KNOWN_STATUSES:
            raise ValueError(f"Unsupported status: {status}")

        normalized_events.append(
            {
                "normalized_url": normalized_url,
                "job_url": job_url or normalized_url,
                "company": safe_str(event.get("company")),
                "title": safe_str(event.get("title")),
                "location": safe_str(event.get("location")),
                "sites": list(event.get("sites", [])),
                "query_labels": list(event.get("query_labels", [])),
                "score": event.get("score"),
                "recommendation": safe_str(event.get("recommendation")),
                "status": status,
                "note": safe_str(event.get("note")),
            }
        )

    transaction = {
        "transaction_id": transaction_id,
        "timestamp": timestamp,
        "actor": actor,
        "kind": kind,
        "metadata": metadata or {},
        "events": normalized_events,
    }

    with TRANSACTIONS_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(transaction, sort_keys=True) + "\n")

    state = rebuild_views()
    return {
        "transaction_id": transaction_id,
        "timestamp": timestamp,
        "event_count": len(normalized_events),
        "state": state,
    }

