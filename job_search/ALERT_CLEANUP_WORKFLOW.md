# Job-Alert Cleanup Workflow

Use this workflow when Dorian asks to inventory, remove, retune, or replace
future job alerts. It is cross-agent repository guidance: Codex, Copilot, and
other agents should follow it without requiring a product-specific skill.

## Purpose and boundary

This is **alert configuration maintenance**, not job discovery. Gmail remains
the sole discovery channel after the user configures the alerts. Do not use
LinkedIn, Indeed, or other boards to discover and recommend jobs directly.

The deterministic layer is local Python. Gmail MCP performs all Gmail reads,
searches, and label changes. Browser or DevTools tools are only for the
user-approved, human-reviewed account settings work.

Never create an application record, modify `master_tracker.md`, or write a
ledger decision while cleaning alerts.

## Inputs

1. Read `AGENTS.md` and `AGENT_BOOTSTRAP_COMPACT.md`.
2. Use targeted Gmail MCP searches to identify job-alert senders and their
   alert names. Prefer sender and subject reads over full MIME batches.
3. Save only a minimal capture to the ignored `job_search/input/` directory,
   following [alert_inventory_schema.json](alert_inventory_schema.json). Do not
   place email content, tracking URLs, or credentials in tracked files.
4. Use the canonical employer-facing upload file:
   `resumes/resume_fde_applied_ai_systems.docx`.

## Deterministic planning

Run from repository root:

```bash
python job_search/alert_cleanup.py plan \
  --input job_search/input/job_alert_inventory.json \
  --run-date YYYY-MM-DD
```

The tracked [alert_cleanup_profile.json](alert_cleanup_profile.json) is the
source of truth for:

- desired alert titles and portable query text;
- remote-worldwide and Canada/U.S.-onsite scope;
- legacy-alert patterns and platform/sender mapping;
- canonical resume path.

The command creates ignored outputs in `job_search/output/`:

- a Markdown review plan;
- a temporary JavaScript overlay for Chrome DevTools MCP.

Treat platform-specific query syntax, filters, and account state as unverified
until a human sees the platform’s actual settings.

## Human-in-the-loop account work

Before an external save, upload, subscription, or unsubscription, obtain the
user's explicit approval for the specific platform and action. Then, for each
platform:

1. Compare current alerts with the generated plan.
2. Remove only confirmed legacy or unwanted alerts.
3. Upload the canonical resume only if the user approves that destination and
   it does not already hold the current version.
4. Create or retune the desired alerts.
5. Have the user review the final platform configuration before saving.

Temporary overlays may highlight controls and show the planned next actions,
but must not submit forms, upload files, or obscure account warnings. They are
not a persistent browser extension.

## Browser workspace safety

If a durable browser workspace is wanted, Dorian creates and owns the Chrome
tab group. Agent-created browser task tabs can be ephemeral. Do not create or
reorganize a user-owned tab group. Navigate only an explicitly selected tab,
and keep any handoff page open only at the user's request.

## After each platform

Report the observed changes and any unverified settings. Do not claim an alert,
resume upload, or subscription update succeeded without confirming it in the
platform UI. The next Gmail MCP report remains the evidence that the revised
configuration is producing the intended alert stream.
