# Job Search Runner

Quick start doc: [../HOW_TO_RUN_JOB_SEARCH.md](../HOW_TO_RUN_JOB_SEARCH.md)
Ledger doc: [../HOW_TO_USE_SEARCH_LEDGER.md](../HOW_TO_USE_SEARCH_LEDGER.md)
Deep-dive workflow: [DEEP_DIVE_WORKFLOW.md](DEEP_DIVE_WORKFLOW.md)
ATS/startup sweep workflow: [ATS_SWEEP_WORKFLOW.md](ATS_SWEEP_WORKFLOW.md)
Contract search workflow: [CONTRACT_SEARCH_WORKFLOW.md](CONTRACT_SEARCH_WORKFLOW.md)

Manual one-shot search tooling for preferred roles.

## Purpose

This is meant to produce a shortlist you can review later, not to auto-apply.

The runner:
- searches several job boards through `python-jobspy`
- uses search strings tuned for Applied AI Systems Engineer roles
- searches overlapping AI title variants because the market has not settled on one canonical job title
- supports a separate contracting profile for contract, consulting, and fractional AI engineering searches
- de-dupes results against existing application posting URLs already recorded in this repo
- records surfaced jobs into the search ledger
- writes a markdown shortlist and a CSV file to `job_search/output/`

The runner does not make final fit decisions. Use the deep-dive workflow after a run to follow posting links, capture compensation, classify current fit versus future roles, and extract resume implications.

For serious discovery, follow the runner with the ATS/startup sweep. Many sharper applied-AI roles live directly on Ashby, Greenhouse, Lever, YC Work at a Startup, HN "Who is hiring?", or company careers pages.

## Why Google Is Included Carefully

Google Jobs tends to return good results in the browser, but it is not a stable raw-`curl` target.
This workflow uses JobSpy's Google support where possible and pairs it with LinkedIn and Indeed for coverage.

Google searches are especially sensitive to query wording.
If results are weak, tune the `google_search_term_template` values in `search_profile.json`.

## Files

- `search_profile.json`
  Search profile, role families, locations, and search-site defaults.
- `search_profile_contracting.json`
  Contracting profile for AI engineering contract, consulting, and fractional searches.
- `run_search.py`
  Main search and ranking script.
- `run_search.sh`
  WSL-friendly wrapper that bootstraps the virtual environment if needed.
- `run_contract_search.sh`
  WSL-friendly wrapper for the contracting profile.
- `record_decisions.py`
  Ledger update helper for `applied`, `dismissed`, and `saved` decisions.
- `DEEP_DIVE_WORKFLOW.md`
  Manual review workflow for turning a raw shortlist into fit buckets, compensation notes, and resume-positioning guidance.
- `ATS_SWEEP_WORKFLOW.md`
  Manual/web-search workflow for Ashby, Greenhouse, Lever, YC, HN, and startup/company career sources that the runner does not reliably cover.
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

Run the contracting profile:

```bash
cd /mnt/d/Repos/job-hunt-2026
./job_search/run_contract_search.sh
```

Optional flags:

```bash
./job_search/run_search.sh --max-searches 2 --results-per-query 5
./job_search/run_search.sh --dry-run --max-searches 2 --results-per-query 5
./job_search/run_contract_search.sh --dry-run --max-searches 3 --results-per-query 5
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
- `--dry-run` / `--no-ledger`
  Write markdown and CSV reports without recording surfaced jobs in the search ledger.

## Output

Each run writes:
- a markdown review list
- a CSV export of ranked results

Normal runs also record surfaced jobs into `ledger/` for duplicate suppression.
Dry runs do not mutate the ledger.

The markdown file groups results into:
- `Apply First`
- `Review`
- `Low Priority`

These buckets are heuristic only. For strategic review, run the deep-dive workflow and classify roles as:
- strong current target
- current/stretch target
- future/stretch market signal
- dismiss/archive
- noisy/unverified

Each entry includes:
- company
- title
- location
- site(s)
- salary/hourly range when available from the source
- posting URL
- brief match reasons

## Notes

- Existing applications are de-duped by normalized posting URL from `applications/*/job_description.md`.
- The ranking is heuristic and intentionally conservative.
- This is a search triage tool, not a final decision-maker.
- If compensation is `Not listed`, open the posting or company careers page during review and capture any salary/hourly range found there.
- Do not record ledger decisions during a deep dive unless the user explicitly asks.
