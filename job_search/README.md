# Gmail Job-Alert Discovery

The Gmail alert workflow is the only active job-discovery path for this
repository. Job alerts are configured by the user; the repository reads the
starred alert messages, recovers canonical posting links, verifies full
postings, and produces research/application-review artifacts.

## Active entry points

- [Gmail job report and application workflow](GMAIL_JOB_APPLICATION_WORKFLOW.md)
- [Gmail report runner](run_gmail_job_report.sh)
- [Full-posting deep-dive workflow](DEEP_DIVE_WORKFLOW.md)
- [Candidate evidence profile](candidate_profile.json)
- [Search bookkeeping ledger](ledger/README.md)

Run from WSL:

```bash
cd /mnt/d/Repos/job-hunt-2026
./job_search/run_gmail_job_report.sh
```

The report searches starred Gmail messages newer than the later of the last
successful report and 14 days before the run. It uses exact message timestamps
after Gmail’s coarse date prefilter, reads the full MIME body, and records
public canonical job URLs. It does not search job boards directly.

## Active boundaries

- Full-posting verification is required before recommending a role.
- Review labels are visible in Gmail: `Jobs/Reviewed`, `Jobs/Applied`, and
  `Jobs/Rejections`.
- `Jobs/Rejections` covers employer rejection and confirmed closed/expired
  postings; it is a Gmail workflow label, not an application-history record.
- Review-only application folders do not update `master_tracker.md`.
- An application counts only when both the matching application folder and
  `master_tracker.md` row exist.
- Do not record ledger decisions during a deep dive unless the user explicitly
  asks.

## Retired tools

`run_search.py`, `run_search.sh`, `run_contract_search.sh`, the direct-search
profiles, and `ATS_SWEEP_WORKFLOW.md` / `CONTRACT_SEARCH_WORKFLOW.md` are kept
as historical/diagnostic material only. They must not be invoked for new job
discovery unless the user explicitly changes the Gmail-only policy.
