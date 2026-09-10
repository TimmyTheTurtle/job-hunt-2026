# Deterministic Job-Search Components

This reference is for every agent working in this repository, including Codex
and Copilot. It separates deterministic local work from connected-service work
so that a different agent can resume the workflow without rediscovering its
boundaries.

| Component | Deterministic local responsibility | Connected-service handoff | Output / state |
| --- | --- | --- | --- |
| `gmail_mcp_triage.py window` | Calculates the bounded Gmail query and exact timestamp cutoff. | Gmail MCP searches with the emitted request. | JSON request printed to terminal. |
| `gmail_mcp_triage.py report` | Filters the MCP capture, extracts canonical links, evaluates supplied full postings, renders addresses, and advances report state. | Gmail MCP provides the minimal capture; a human verifies full postings and addresses. | Ignored report in `output/`; tracked `ledger/gmail_mcp_triage_state.json`. |
| `qualification.py` + `candidate_profile.json` | Applies the conservative requirements-to-evidence screen. | None. It must receive complete posting text from human/MCP/browser review. | Qualification object embedded in the report. |
| `alert_cleanup.py plan` + `alert_cleanup_profile.json` | Classifies alert inventory, writes review steps, and emits a temporary DevTools overlay. | Gmail MCP supplies inventory; the human configures job-board accounts. | Ignored Markdown plan and overlay JavaScript in `output/`. |
| `record_decisions.py` | Records an explicit user decision into the search ledger. | The user must explicitly state the decision; application updates also require the canonical artifacts. | `ledger/transactions.jsonl` and derived ledger state. |

## Rules shared by every component

- Python scripts have no Gmail credentials and make no Gmail or job-board
  network calls.
- Gmail MCP is the only Gmail transport; it performs every Gmail read, search,
  and label mutation.
- A browser or DevTools MCP session may assist a human through an external
  platform's settings, but it is not job discovery and must not silently submit
  an upload, subscription, unsubscription, or application.
- Treat untracked `job_search/input/` captures and `job_search/output/` reports
  as potentially sensitive. Keep tracking URLs and email bodies out of the
  repository.
- Run Python directly from the repository root; WSL startup is required only
  before a `.sh` runner, not for these cross-platform Python commands.

## Choosing the workflow

- New starred Gmail leads or a report: read
  [GMAIL_JOB_APPLICATION_WORKFLOW.md](GMAIL_JOB_APPLICATION_WORKFLOW.md).
- Future-alert cleanup or temporary browser guidance: read
  [ALERT_CLEANUP_WORKFLOW.md](ALERT_CLEANUP_WORKFLOW.md).
- Full-posting review after a report: read
  [DEEP_DIVE_WORKFLOW.md](DEEP_DIVE_WORKFLOW.md).
- Explicit save, dismiss, or applied decision: read
  [GMAIL_JOB_APPLICATION_WORKFLOW.md](GMAIL_JOB_APPLICATION_WORKFLOW.md) and
  use `record_decisions.py` only after the user decides.
