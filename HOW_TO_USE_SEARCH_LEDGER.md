# How to Use the Search Ledger

The search ledger is the machine-managed bookkeeping system for search results and review decisions.

It exists so that:
- repeated search runs do not keep surfacing the same jobs
- you can record `applied`, `dismissed`, or `saved` decisions separately from `master_tracker.md`
- `master_tracker.md` stays a supervised/manual artifact for UI submissions

## Important Boundary

Use the search ledger for:
- machine-managed search results
- duplicate suppression
- quick review decisions

Use [master_tracker.md](master_tracker.md) for:
- supervised application logging
- UI-facing submission history
- the record you want to curate manually

The search system should not auto-edit `master_tracker.md`.

## Where It Lives

- Source of truth: [job_search/ledger/transactions.jsonl](job_search/ledger/transactions.jsonl)
- Current state view: [job_search/ledger/state.json](job_search/ledger/state.json)
- Human-readable summary: [job_search/ledger/summary.md](job_search/ledger/summary.md)
- Notes: [job_search/ledger/README.md](job_search/ledger/README.md)

## How It Works

When you run the search:
- new shortlist items are recorded as `surfaced`
- those URLs are then blocked from showing up again on the next run

When you review results later:
- you can mark jobs as `applied`
- you can mark jobs as `dismissed`
- you can mark jobs as `saved`

Those decisions are also recorded transactionally in the ledger.

## Common Statuses

- `surfaced`
  The search found it and recorded it for review.
- `saved`
  Keep it in the ledger without resurfacing it in every run.
- `dismissed`
  Intentionally tossed out.
- `applied`
  Applied already.

## Recording Decisions

You can record decisions with:

- [job_search/record_decisions.py](job_search/record_decisions.py)

Examples from WSL:

```bash
cd /mnt/d/Repos/job-hunt-2026
./job_search/.venv/bin/python job_search/record_decisions.py \
  --applied "https://example.com/job-1" \
  --dismissed "https://example.com/job-2" \
  --note "reviewed after shortlist pass"
```

Or by JSON payload:

```bash
cd /mnt/d/Repos/job-hunt-2026
cat <<'JSON' | ./job_search/.venv/bin/python job_search/record_decisions.py --actor chat_update
{
  "metadata": {
    "source": "chat review"
  },
  "decisions": [
    {
      "status": "applied",
      "job_url": "https://example.com/job-1",
      "note": "Applied after review"
    },
    {
      "status": "dismissed",
      "job_url": "https://example.com/job-2",
      "note": "Too senior"
    }
  ]
}
JSON
```

## Using Chat Instead of CLI

You can also have a chat session record ledger updates for you.

Examples:

- `Please mark our current application as applied in the search ledger.`
- `Please mark these as dismissed in the search ledger:` followed by posting URLs
- `Please save these for later in the search ledger:` followed by posting URLs
- `Please record this mixed ledger update:` followed by `Applied`, `Dismissed`, and `Saved` lists

Best practice:
- provide posting URLs when you have them
- if you say `current application`, make sure the active application is clear from the chat context
- if there might be ambiguity, include the company, role title, or exact posting URL

Important:
- chat-ledger updates should affect the search ledger
- they should not automatically update [master_tracker.md](master_tracker.md) unless you ask for that separately

## Recommended Human Workflow

1. Run the search tool.
2. Review the newest markdown report in `job_search/output/`.
3. Record `applied`, `dismissed`, or `saved` decisions into the ledger.
4. Only update [master_tracker.md](master_tracker.md) when you intentionally want to log an actual application for UI/manual tracking.

## Best Files To Watch

If you only want the most useful ledger files:

- [job_search/ledger/summary.md](job_search/ledger/summary.md)
- [job_search/ledger/transactions.jsonl](job_search/ledger/transactions.jsonl)
