# Gmail Job Report and Application Workflow

Use this workflow when job leads arrive through Gmail and the user wants the
best current leads prepared for review.

## 1. Bounded Gmail report

Run from the repository root through WSL:

```sh
./job_search/run_gmail_job_report.sh
```

The runner searches starred messages with `-in:spam -in:trash`. Its exact
lower bound is the later of the last successful report timestamp and fourteen
days before the run. Gmail's date query is only a coarse prefilter; message
`internalDate` is used for the exact boundary. The first run may use
`--since <ISO-8601 timestamp>` to migrate from the previous report.

The report extracts full MIME bodies and records public canonical job URLs.
Opaque Gmail/Indeed tracking links are not copied into tracked application
files. The generated report is written under `job_search/output/`.

## 2. Full-posting verification and ranking

For every candidate, open the employer or ATS posting and capture the complete
posting context: title, company, location/remote eligibility, compensation,
responsibilities, requirements, seniority, domain constraints, and current
availability. Use `candidate_profile.json`, `ROLE_EVAL_CHECKLIST.md`, and
`current_strategy.md`. Missing or thin postings remain unverified.

Select the top two only from candidates with usable full-posting evidence. If
the bounded window contains fewer than two credible roles, report fewer than
two; do not backfill older messages or invent requirements.

## 3. Review and unflagging

Only messages actually opened and analyzed count as reviewed. After evidence is
captured, remove only the `STARRED` label from those explicit message IDs:

```sh
./job_search/run_gmail_job_report.sh \
  --run-date YYYY-MM-DD \
  --unflag-reviewed \
  --reviewed-id MESSAGE_ID
```

For a previously reviewed message whose ID is not in the current bounded
report, use an exact subject instead of widening the report window:

```sh
./job_search/run_gmail_job_report.sh \
  --run-date YYYY-MM-DD \
  --unflag-reviewed \
  --reviewed-subject "Exact message subject"
```

The command never deletes messages and never removes other labels. Verify the
message IDs no longer have `STARRED` after the operation. The report state is
stored separately from `gmail_last_run.json`, which belongs to inbox triage.

The visible Gmail status-label lifecycle is:

- `Jobs/Reviewed`: the message was opened and the posting was analyzed.
- `Jobs/Applied`: the user confirmed the application was submitted.
- `Jobs/Rejections`: the employer or application process produced a rejection.

Use the existing `Jobs/Applied` and `Jobs/Rejections` labels rather than
creating duplicates. These labels are mutually exclusive outcome states; do
not mark a message applied or rejected before the outcome is known.

## 4. Review-only application folders

For each selected role, create:

```text
applications/YYYY-MM_<company>_<role>/
  job_description.md
  notes.md
  cover_letter.md
  submission_snapshot.md
```

`job_description.md` contains the exact public posting URL, source message/date,
full posting snapshot, and verification status. `notes.md` contains the fit
assessment, truthful positioning, material gaps, and internal drafting rules.
`cover_letter.md` is concise, role-specific, and based only on verified facts.
`submission_snapshot.md` says `Draft / Not submitted` until the user actually
submits the application.

Do not update `master_tracker.md` or append an Applied ledger decision for
preparation-only folders. When the user later confirms submission, follow the
Applied-artifact requirements in `AGENTS.md`.

An application is canonical only when the matching application folder and
`master_tracker.md` row both exist. Gmail labels or email evidence alone never
establish application history; if either side is missing, report the record as
incomplete/unconfirmed and do not count it.

## 5. Cover-letter truth audit

Letters must be calm, specific, technically credible, and 250–400 words by
default. Do not mention unemployment/UI matters, AI-103, AI-500, or unsupported
production AI, legal, healthcare, clearance, or platform-ownership claims.
Keep certification status as an internal drafting constraint only.
