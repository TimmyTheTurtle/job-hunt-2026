#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from ledger import record_transaction


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Record job-search decisions into the search ledger.")
    parser.add_argument("--actor", default="manual_review")
    parser.add_argument("--note", default="")
    parser.add_argument("--file", help="Path to a JSON payload file. If omitted, stdin is used when available.")
    parser.add_argument("--applied", action="append", default=[], help="Posting URL marked as applied.")
    parser.add_argument("--dismissed", action="append", default=[], help="Posting URL marked as dismissed.")
    parser.add_argument("--saved", action="append", default=[], help="Posting URL marked as saved.")
    return parser.parse_args()


def decisions_from_payload(payload: dict[str, Any], default_note: str) -> list[dict[str, Any]]:
    decisions = []
    for item in payload.get("decisions", []):
        decisions.append(
            {
                "status": item["status"],
                "job_url": item["job_url"],
                "company": item.get("company", ""),
                "title": item.get("title", ""),
                "location": item.get("location", ""),
                "note": item.get("note", default_note),
            }
        )
    return decisions


def main() -> int:
    args = parse_args()
    decisions: list[dict[str, Any]] = []
    metadata: dict[str, Any] = {}

    if args.file:
        payload = json.loads(Path(args.file).read_text(encoding="utf-8"))
        decisions.extend(decisions_from_payload(payload, args.note))
        metadata = payload.get("metadata", {})
    elif not sys.stdin.isatty():
        raw = sys.stdin.read().strip()
        if raw:
            payload = json.loads(raw)
            decisions.extend(decisions_from_payload(payload, args.note))
            metadata = payload.get("metadata", {})

    for url in args.applied:
        decisions.append({"status": "applied", "job_url": url, "note": args.note})
    for url in args.dismissed:
        decisions.append({"status": "dismissed", "job_url": url, "note": args.note})
    for url in args.saved:
        decisions.append({"status": "saved", "job_url": url, "note": args.note})

    if not decisions:
        raise SystemExit("No decisions provided.")

    result = record_transaction(actor=args.actor, kind="decision_update", events=decisions, metadata=metadata)
    print(f"Transaction: {result['transaction_id']}")
    print(f"Events recorded: {result['event_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
