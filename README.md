# job-hunt-2026

This repository is the canonical record for job-search strategy, applications, resume versions, cover letters, and gaps.

## Start Here

- [How to add a new application](HOW_TO_ADD_A_FOLDER.md)
- [How to run the manual job search](HOW_TO_RUN_JOB_SEARCH.md)
- [Current strategy](docs/current_strategy.md)
- [UI compliance notes](docs/ui_compliance.md)
- [Agent entry point](AGENTS.md)
- [Agent bootstrap guide](docs/agent_bootstrap_human.md)
- [Master tracker](master_tracker.md)
- [Skills gap ledger](gaps.md)

## Repository Structure

- `applications/`
  One folder per application with job description, notes, submission snapshot, and interview prep.
- `cover_letters/`
  Reusable templates and role-specific letters.
- `resumes/`
  Resume versions and notes about positioning changes.
- `docs/`
  Canonical reference docs for strategy and administrative guidance.
- `job_search/`
  Manual one-shot search tooling plus generated review lists under `job_search/output/`.
- `master_tracker.md`
  Main application ledger.
- `gaps.md`
  Running list of exposed skill gaps and study plans.

## Working Model

- The repo is the source of truth for durable information.
- GitHub issues should be active tasks, not long-form document storage.
- The GitHub Project board should be an execution view over those issues.

## Current Priorities

- Keep job-search administration lightweight and consistent.
- Preserve training time for C++, simulation, and systems growth.
- Apply to roles that compound toward simulation, performance, and real-time systems work.

## Notes

- Historical planning notes still exist in [job-search-tips.md](job-search-tips.md), but the canonical strategy now lives in [docs/current_strategy.md](docs/current_strategy.md).
- Application-specific rationale should stay inside the relevant folder under `applications/`.
