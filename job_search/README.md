# Gmail Job-Alert Discovery

The Gmail alert workflow is the only active job-discovery path for this
repository. Job alerts are configured by the user; the repository reads the
starred alert messages, recovers canonical posting links, verifies full
postings, and produces research/application-review artifacts.

## Active entry points

- [Gmail job report and application workflow](GMAIL_JOB_APPLICATION_WORKFLOW.md)
- [Deterministic Gmail MCP report script](gmail_mcp_triage.py)
- [MCP capture contract](gmail_mcp_capture_schema.json)
- [Full-posting deep-dive workflow](DEEP_DIVE_WORKFLOW.md)
- [Candidate evidence profile](candidate_profile.json)
- [Search bookkeeping ledger](ledger/README.md)
- [Deterministic job-alert cleanup planner](alert_cleanup.py)
- [Cross-agent job-alert cleanup workflow](ALERT_CLEANUP_WORKFLOW.md)
- [Cross-agent deterministic component map](DETERMINISTIC_JOB_SEARCH_COMPONENTS.md)

Run the deterministic Python steps from the repository root:

```bash
python job_search/gmail_mcp_triage.py window
# use the returned request with connected Gmail MCP search/read tools
python job_search/gmail_mcp_triage.py report --input job_search/input/gmail_mcp_capture.json
```

Gmail MCP performs all Gmail search, read, and label actions. The Python script
performs no Gmail authentication or network I/O; it validates the MCP capture,
applies the exact report window, recovers public posting URLs, scores supplied
full postings, and writes the report. Capture files are intentionally ignored
because they contain email content.

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

## Alert cleanup and temporary browser guidance

`alert_cleanup.py` turns a minimal, ignored inventory capture from Gmail MCP
searches into a review-only platform plan and a temporary JavaScript overlay.
It does not access Gmail, browser accounts, or job boards. A Chrome DevTools
MCP session may inject the generated overlay to show the agreed next steps while
the user manually reviews each platform's settings.

```bash
python job_search/alert_cleanup.py plan \
  --input job_search/input/job_alert_inventory.json \
  --run-date 2026-09-10
```

The committed alert profile keeps remote roles worldwide and onsite roles in
Canada or the United States. It names the FDE/applied-AI target alerts and the
canonical resume path; platform-specific query syntax must still be reviewed
before any external save action.

## Retired tools

`gmail_auth.py`, `gmail_job_report.py`, `gmail_triage.py`,
`run_gmail_job_report.sh`, `run_gmail_triage.sh`, `run_search.py`,
`run_search.sh`, `run_contract_search.sh`, the direct-search
profiles, and `ATS_SWEEP_WORKFLOW.md` / `CONTRACT_SEARCH_WORKFLOW.md` are kept
as historical/diagnostic material only. They must not be invoked for new job
discovery unless the user explicitly changes the Gmail-only policy.
