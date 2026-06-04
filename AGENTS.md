# AGENTS.md

## Single Entry Point

This file is the single entry point for any agent working in this repository.
It should remain a startup router, not a duplicate policy dump.

Every agent should bootstrap in this order:
1. read this file
2. read [AGENT_BOOTSTRAP_COMPACT.md](AGENT_BOOTSTRAP_COMPACT.md)
3. read only the specific supporting docs needed for the current task

Do not begin by loading every context file in the repo.

Preferred CLI: Use WSL for running repository scripts and the `job_search` runner.

## Bootstrap Rule

The compact bootstrap file is the default machine-facing context layer.
It should stay short, dense, and optimized for quick agent loading.

The human-readable explanation of that bootstrap lives in:
- [docs/agent_bootstrap_human.md](docs/agent_bootstrap_human.md)

Whenever the compact bootstrap changes, update the human-readable document in the same change.

## Source Context Files

The compact bootstrap is derived from these source files:
- [JOB_HUNT_CONTEXT.md](JOB_HUNT_CONTEXT.md)
- [COVER_LETTER_RULES.md](COVER_LETTER_RULES.md)
- [ROLE_EVAL_CHECKLIST.md](ROLE_EVAL_CHECKLIST.md)
- [RECRUITER_RESPONSE_RULES.md](RECRUITER_RESPONSE_RULES.md)
- [RESUME_BULLET_RULES.md](RESUME_BULLET_RULES.md)
- [APPLICATION_WORKFLOW.md](APPLICATION_WORKFLOW.md)

Only read the full source file when the current task actually needs that detail.

## Working Rules For Agents

- Keep employer-facing writing truthful, restrained, and role-specific.
- Keep Dorian-facing analysis honest, structured, and strategically useful.
- Prefer the narrower defensible claim over the broader impressive claim.
- Do not fabricate employers, titles, certifications, years of experience, clearance, or unsupported domain expertise.
- Optimize for coherent direction, not application spam.
- Protect runway, learning time, and long-term systems/C++/simulation positioning.
- Keep machine-managed search bookkeeping in `job_search/ledger/`; do not auto-update `master_tracker.md` from search runs.
- Keep company watchlist updates in `company_watchlist.md`; do not fold watchlist checks into `master_tracker.md`.

## Workflow Requirement

For application work:
1. bootstrap from the compact context
2. record the exact posting URL in the application's `job_description.md`
3. follow the default workflow in [APPLICATION_WORKFLOW.md](APPLICATION_WORKFLOW.md)

Mandatory when status is `Applied`:
- update or create `applications/YYYY-MM_<company>_<role>/job_description.md`
- update or create `applications/YYYY-MM_<company>_<role>/submission_snapshot.md`
- update or create `applications/YYYY-MM_<company>_<role>/notes.md`
- update `master_tracker.md` with the applied row details
- append a `decision_update` event in `job_search/ledger/transactions.jsonl` with:
	- `actor: "chat_update"`
	- `status: "applied"`
	- canonical job URL and company/role context

Before finishing any "Applied" update, run a final verification pass that confirms all five artifacts above exist and are consistent.

For company monitoring:
- record the company, URL, and latest public hiring signal in `company_watchlist.md`
- treat "look for a job now" as including watchlist check-ins when the user has named a company

Do not restate the detailed workflow here unless the startup contract itself changes.

## Canonical Consistency Rule

- `AGENTS.md` is the canonical startup contract.
- `CLAUDE.md` and `.github/copilot-instructions.md` must remain semantically identical to this contract, with only path-prefix differences where required.
- If any startup rule changes here, mirror it in both files in the same change.

## Maintenance Rule

If you change:
- candidate positioning
- role hierarchy
- truth constraints
- writing rules
- workflow expectations

then update all three layers that apply:
- source context file(s)
- [AGENT_BOOTSTRAP_COMPACT.md](AGENT_BOOTSTRAP_COMPACT.md)
- [docs/agent_bootstrap_human.md](docs/agent_bootstrap_human.md)

Keep the compact layer minimal.
Keep the human layer understandable.
