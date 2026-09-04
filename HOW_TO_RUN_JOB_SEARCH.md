# Gmail Job-Alert Workflow

This is the repository’s only active job-discovery workflow. Configure job
alerts in Gmail, star the messages worth reviewing, and use the Gmail report
runner to process only those alerts. Do not run a separate LinkedIn, Indeed,
Google Jobs, ATS, startup, or contracting search unless the user explicitly
changes this policy.

## Canonical flow

```text
Gmail alert
  -> bounded starred-message report
  -> canonical public posting-link recovery
  -> full-posting verification
  -> deep dive and user review
  -> optional review-only application materials
  -> confirmed submission and application/tracker records
```

The report window is the shorter of the two constraints: messages newer than
the last successful Gmail report, with a maximum lookback of 14 days. Do not
backfill older alerts simply to reach a target number.

## Run the report

From WSL at the repository root:

```bash
cd /mnt/d/Repos/job-hunt-2026
./job_search/run_gmail_job_report.sh
```

The runner reads full message bodies, extracts public job links, and writes a
dated report under `job_search/output/`. Gmail OAuth is cached in
`secrets/gmail_token.json` after the initial authorization.

## Review and status handling

For each promising alert:

1. Open the recovered public posting or employer/ATS page.
2. Capture the exact URL, location, compensation, responsibilities, requirements, seniority, domain constraints, and current availability.
3. Use `job_search/DEEP_DIVE_WORKFLOW.md` for qualification and resume implications.
4. Apply `Jobs/Reviewed` after the posting has actually been analyzed.
5. Remove the star only for the explicit message that was reviewed.
6. Apply `Jobs/Rejections` when the employer rejects the candidate or the posting is confirmed closed/expired/no longer accepting applications.
7. Apply `Jobs/Applied` only after the user confirms submission.

`Jobs/Reviewed`, `Jobs/Applied`, and `Jobs/Rejections` are visible Gmail
workflow labels. They do not establish application history. An application is
canonical only when its matching `applications/...` folder and
`master_tracker.md` row both exist.

## Application preparation

When the user selects a role, follow
`job_search/GMAIL_JOB_APPLICATION_WORKFLOW.md` and create review-only
materials with the exact posting URL before drafting. Do not update
`master_tracker.md` or the Applied ledger state until submission is confirmed.

## Retired discovery paths

The former direct JobSpy search, ATS/startup sweep, and contracting search are
not active workflows. Their scripts, profiles, reports, and documentation are
preserved for historical context or explicitly requested diagnostics; agents
must not invoke them for new discovery.
