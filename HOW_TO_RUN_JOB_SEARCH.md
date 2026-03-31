# How to Run the Manual Job Search

This repo now includes a manual one-shot job-search tool for preferred roles.

It is designed to:
- run only when you ask for it
- generate a shortlist for later review
- include posting URLs for manual follow-up
- avoid auto-applying

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
4. If you decide to pursue one, create the standard application folder and record the exact posting URL in `job_description.md`.
5. Add or update the row in [master_tracker.md](master_tracker.md).

## Important Notes

- This is a triage tool, not a final decision-maker.
- The ranking is heuristic and will still surface some imperfect results.
- Google Jobs is included in the profile, but in live testing here LinkedIn and Indeed produced more usable results than Google.
- Search systems often handle `C++` badly, so the profile intentionally leans on `c plus plus` phrasing.
- Generated output and the local virtual environment are ignored by git.

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
