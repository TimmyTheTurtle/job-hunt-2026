# How to Run the Manual Job Search

This repo now includes a manual one-shot job-search tool for preferred roles.

It is designed to:
- run only when you ask for it
- generate a shortlist for later review
- include posting URLs for manual follow-up
- avoid auto-applying
- feed the machine-managed search ledger without auto-editing `master_tracker.md`

## What It Does

The search tool:
- runs from WSL
- searches selected job boards through `python-jobspy`
- uses role queries tuned for your preferred C++ / simulation / systems direction
- de-dupes against posting URLs already recorded in this repo
- writes a markdown shortlist and CSV export to `job_search/output/`

Current default emphasis:
- simulation engineer
- modeling and simulation engineer
- systems software engineer
- real-time software engineer
- HPC / scientific computing stretch roles

## Where It Lives

- Runner: [job_search/run_search.sh](job_search/run_search.sh)
- Main script: [job_search/run_search.py](job_search/run_search.py)
- Search profile: [job_search/search_profile.json](job_search/search_profile.json)
- Detailed subsystem notes: [job_search/README.md](job_search/README.md)

## Quick Start

From WSL:

```bash
cd /mnt/d/Repos/job-hunt-2026
./job_search/run_search.sh
```

On first run, it will create a local virtual environment and install Python dependencies.
That first run may take a minute.

## Common Commands

Run the normal full search:

```bash
cd /mnt/d/Repos/job-hunt-2026
./job_search/run_search.sh
```

Run a smaller test pass:

```bash
cd /mnt/d/Repos/job-hunt-2026
./job_search/run_search.sh --max-searches 2 --results-per-query 5
```

Restrict to specific sites:

```bash
cd /mnt/d/Repos/job-hunt-2026
./job_search/run_search.sh --sites linkedin,indeed
```

Search only more recent postings:

```bash
cd /mnt/d/Repos/job-hunt-2026
./job_search/run_search.sh --hours-old 168
```

## Where Results Go

Generated files are written to:

- `job_search/output/*.md`
- `job_search/output/*.csv`

The markdown report is the main review artifact.
It groups results into:
- `Apply First`
- `Review`
- `Low Priority`

Each entry includes:
- company
- role title
- location
- site source
- posting URL
- match notes

## How to Review Results

Recommended workflow:

1. Open the newest markdown file in `job_search/output/`.
2. Skim the `Apply First` section first.
3. Open promising posting URLs in the browser.
4. Record `applied`, `dismissed`, or `saved` decisions in the search ledger.
5. If you decide to pursue one, create the standard application folder and record the exact posting URL in `job_description.md`.
6. Add or update the row in [master_tracker.md](master_tracker.md) only when you intentionally want that manual/UI-facing record updated.

See also:
- [How to use the search ledger](HOW_TO_USE_SEARCH_LEDGER.md)

## How to Record Decisions

From WSL, you can record review decisions directly into the search ledger.

Mark one or more jobs as applied:

```bash
cd /mnt/d/Repos/job-hunt-2026
./job_search/.venv/bin/python job_search/record_decisions.py \
  --applied "https://example.com/job-1" \
  --applied "https://example.com/job-2" \
  --note "applied after review"
```

Mark jobs as dismissed:

```bash
cd /mnt/d/Repos/job-hunt-2026
./job_search/.venv/bin/python job_search/record_decisions.py \
  --dismissed "https://example.com/job-3" \
  --dismissed "https://example.com/job-4" \
  --note "too senior or wrong fit"
```

Mark jobs as saved for later:

```bash
cd /mnt/d/Repos/job-hunt-2026
./job_search/.venv/bin/python job_search/record_decisions.py \
  --saved "https://example.com/job-5" \
  --saved "https://example.com/job-6" \
  --note "interesting, revisit later"
```

Record a mixed batch in one transaction:

```bash
cd /mnt/d/Repos/job-hunt-2026
cat <<'JSON' | ./job_search/.venv/bin/python job_search/record_decisions.py --actor chat_update
{
  "metadata": {
    "source": "manual review session"
  },
  "decisions": [
    {
      "status": "applied",
      "job_url": "https://example.com/job-1",
      "note": "Applied after shortlist review"
    },
    {
      "status": "dismissed",
      "job_url": "https://example.com/job-2",
      "note": "Not aligned enough"
    },
    {
      "status": "saved",
      "job_url": "https://example.com/job-3",
      "note": "Possible later follow-up"
    }
  ]
}
JSON
```

After recording decisions, check:

- [job_search/ledger/summary.md](job_search/ledger/summary.md)
- [job_search/ledger/transactions.jsonl](job_search/ledger/transactions.jsonl)

## How to Do This Through Chat

Yes, you can tell a chat window to record these updates for you.

Good examples:

- `Please mark our current application as applied in the search ledger.`
- `Please mark these as dismissed in the search ledger:` followed by a list of posting URLs
- `Please save these for later in the search ledger:` followed by a list of posting URLs
- `Please mark these three applied and these two dismissed in one ledger update.`

Best practice:
- if you have the posting URLs, provide them
- if you are referring to the current application and the context is unambiguous, saying `current application` is fine
- if there is any ambiguity, include company, role title, or the posting URL

Recommended chat patterns:

Mark the current application as applied:

```text
Please mark our current application as applied in the search ledger.
Do not update master_tracker.md unless I ask separately.
```

Mark a list as dismissed:

```text
Please mark these as dismissed in the search ledger:
- https://example.com/job-1
- https://example.com/job-2
- https://example.com/job-3
```

Mark a list as saved:

```text
Please save these in the search ledger for later review:
- https://example.com/job-4
- https://example.com/job-5
```

Mixed update:

```text
Please record this search-ledger update:
Applied:
- https://example.com/job-1

Dismissed:
- https://example.com/job-2
- https://example.com/job-3

Saved:
- https://example.com/job-4
```

By default, those requests should update the search ledger only.
Ask separately if you also want [master_tracker.md](master_tracker.md) updated.

## Important Notes

- This is a triage tool, not a final decision-maker.
- The ranking is heuristic and will still surface some imperfect results.
- Google Jobs is included in the profile, but in live testing here LinkedIn and Indeed produced more usable results than Google.
- Search systems often handle `C++` badly, so the profile intentionally leans on `c plus plus` phrasing.
- Generated output and the local virtual environment are ignored by git.
- The search ledger is separate from [master_tracker.md](master_tracker.md); the runner should update the ledger, not the manual tracker.

## When You Want to Tune It

Edit [job_search/search_profile.json](job_search/search_profile.json) to change:
- role families
- locations
- default sites
- posting age window
- query wording

If the search starts drifting:
- tighten the search terms
- reduce the number of broad software-engineer queries
- shorten `hours_old`
- restrict sites during a run

## Best First File

If you only want one file to remember, use:

- [job_search/output/](job_search/output/)

That folder is the inbox.
