# Canonical Gmail Job-Alert and Application Workflow

This is the repository’s only active job-discovery workflow. The user creates
job alerts in Gmail; agents process the starred alert messages, verify the
actual postings, and prepare only the roles the user chooses to review or
apply to. Do not run a separate LinkedIn, Indeed, Google Jobs, ATS, startup,
or contracting search unless the user explicitly changes this policy.

## 1. Bounded Gmail report

From the repository root, have the deterministic Python script emit the exact
Gmail MCP search request:

```sh
python job_search/gmail_mcp_triage.py window
```

Use the returned `label_ids` and `query` with Gmail MCP search, then use Gmail
MCP batch/full reads to collect the matching MIME payloads. Save the result as
an untracked JSON file under `job_search/input/` following
`gmail_mcp_capture_schema.json`. The Python script has no Gmail credentials and
never makes a network call:

```sh
python job_search/gmail_mcp_triage.py report --input job_search/input/gmail_mcp_capture.json
```

The exact lower bound is the later of the last successful report timestamp and
fourteen days before the run. Gmail's date query is only a coarse prefilter;
the script applies the exact `internal_date` filter. It extracts full MIME
bodies, records public canonical job URLs, and writes a report under
`job_search/output/`. Opaque Gmail/Indeed tracking links are not copied into
tracked application files.

## 2. Full-posting verification and ranking

For every candidate, open the employer or ATS posting and capture the complete
posting context: title, company, location/remote eligibility, compensation,
responsibilities, requirements, seniority, domain constraints, current
availability, and (for FDE-shaped roles) the split between hands-on engineering
and customer-success/pre-sales work. Use `candidate_profile.json`,
`ROLE_EVAL_CHECKLIST.md`, and `current_strategy.md`. Missing or thin postings
remain unverified.

Capture verified posting data in `posting_enrichments` in the same MCP capture
JSON. The report script uses `qualification.py` deterministically to rank only
the supplied full postings. An employer physical address is rendered only when
its address type, source URL, and verification date are recorded; otherwise it
is `Not verified`.

Select the top two only from candidates with usable full-posting evidence. If
the bounded window contains fewer than two credible roles, report fewer than
two; do not backfill older messages or invent requirements.

## 3. Review and unflagging

Only messages actually opened and analyzed count as reviewed. After evidence is
captured, use Gmail MCP to remove only the `STARRED` label from those explicit
message IDs, then read/search those IDs again to verify the change. For a
previously reviewed message outside the current window, use Gmail MCP exact
subject search; do not widen the deterministic report window. Gmail mutations
never occur through a local script. The report state is stored separately from
the retired `gmail_last_run.json` inbox-triage state.

The visible Gmail status-label lifecycle is:

- `Jobs/Reviewed`: the message was opened and the posting was analyzed.
- `Jobs/Applied`: the user confirmed the application was submitted.
- `Jobs/Rejections`: the employer rejected the candidate, or the posting was
  confirmed closed, expired, or no longer accepting applications.

Use the existing visible labels rather than creating duplicates. `Jobs/Reviewed`
is the research state; `Jobs/Applied` and `Jobs/Rejections` are outcome states.
When a posting is confirmed closed, apply `Jobs/Rejections` and remove
`Jobs/Reviewed` and `STARRED` from that explicit message if present. Do not
infer closure from an old email alone; verify the current employer/ATS page or
an explicit expired/no-longer-accepting signal first.

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
