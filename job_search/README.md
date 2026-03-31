# Job Search Runner

Quick start doc: [../HOW_TO_RUN_JOB_SEARCH.md](../HOW_TO_RUN_JOB_SEARCH.md)
Ledger doc: [../HOW_TO_USE_SEARCH_LEDGER.md](../HOW_TO_USE_SEARCH_LEDGER.md)

Manual one-shot search tooling for preferred roles.

## Purpose

This is meant to produce a shortlist you can review later, not to auto-apply.

The runner:
- searches several job boards through `python-jobspy`
- uses search strings tuned for C++ / simulation / systems roles
- prefers `c plus plus` phrasing because many search systems handle `C++` poorly
- de-dupes results against existing application posting URLs already recorded in this repo
- records surfaced jobs into the search ledger
- writes a markdown shortlist and a CSV file to `job_search/output/`

## Why Google Is Included Carefully

Google Jobs tends to return good results in the browser, but it is not a stable raw-`curl` target.
This workflow uses JobSpy's Google support where possible and pairs it with LinkedIn and Indeed for coverage.

Google searches are especially sensitive to query wording.
If results are weak, tune the `google_search_term_template` values in `search_profile.json`.

## Files

- `search_profile.json`
  Search profile, role families, locations, and search-site defaults.
- `run_search.py`
  Main search and ranking script.
- `run_search.sh`
  WSL-friendly wrapper that bootstraps the virtual environment if needed.
- `record_decisions.py`
  Ledger update helper for `applied`, `dismissed`, and `saved` decisions.
- `ledger/`
  Machine-managed search ledger state and summary files.
- `output/`
  Generated markdown and CSV reports. Ignored by git.

## Run

From WSL:

```bash
cd /mnt/d/Repos/job-hunt-2026
./job_search/run_search.sh
```

Optional flags:

```bash
./job_search/run_search.sh --max-searches 2 --results-per-query 5
```

Useful options:
- `--max-searches N`
  Limit how many search specs run. Good for quick tests.
- `--results-per-query N`
  Override the profile default.
- `--hours-old N`
  Override the posting-age window.
- `--sites linkedin,indeed`
  Restrict the job boards used for a run.

## Output

Each run writes:
- a markdown review list
- a CSV export of ranked results

The markdown file groups results into:
- `Apply First`
- `Review`
- `Low Priority`

Each entry includes:
- company
- title
- location
- site(s)
- posting URL
- brief match reasons

## Notes

- Existing applications are de-duped by normalized posting URL from `applications/*/job_description.md`.
- The ranking is heuristic and intentionally conservative.
- This is a search triage tool, not a final decision-maker.
