# Job Search Deep-Dive Workflow

Use this after a Gmail alert report when the user wants to understand the
surfaced jobs, not merely list them.

This workflow turns a bounded Gmail alert report into:
- current-fit targets
- stretch or future-market-signal roles
- dismiss/archive candidates
- compensation notes
- resume-positioning guidance

## Skill Decision

The active discovery functionality is the repository’s Gmail alert workflow,
not a separate web-search routine or Codex skill.

That is the right default for now because the job search depends on repo-local state:
- `job_search/GMAIL_JOB_APPLICATION_WORKFLOW.md`
- `job_search/gmail_job_report.py`
- `job_search/ledger/`
- ignored generated reports under `job_search/output/`
- candidate context and truth constraints in this repository
- application folders and `master_tracker.md`

A future Codex skill may be useful as a thin launcher or checklist, but the source of truth should remain here unless the same workflow needs to run across multiple repositories.

## When To Run

Run a deep dive after a Gmail report when the user asks for:
- "deep dive"
- "follow the links"
- "which jobs am I qualified for?"
- "which ones are future roles?"
- "what does this teach us about the resume?"
- "job market research" after a Gmail alert report

Treat Gmail alerts as leads, not recommendations. Verify the recovered link
against the live employer/ATS posting. `Unverified` roles must not be
recommended until the full requirements are obtained.

## Inputs

Use the newest relevant Gmail report in `job_search/output/`:
- `gmail_job_report_YYYY-MM-DD.md`

If the user names specific Gmail messages or roles, use those explicit message
IDs/subjects and do not widen the search window merely to find more roles.

If the latest run is ambiguous, identify the most recent files by timestamp and state which one you used.

## Procedure

1. Bootstrap from `AGENTS.md` and `AGENT_BOOTSTRAP_COMPACT.md`.
2. Read `ROLE_EVAL_CHECKLIST.md` and `current_strategy.md` if classification or resume implications are part of the request.
3. Load the latest Gmail job report and its explicit message/link evidence.
4. For each surfaced job, open the recovered posting URL or a reliable company/careers page.
5. Capture:
   - current working URL
   - title and company
   - location and remote eligibility
   - salary/hourly range if listed
   - seniority requirements
   - hard domain requirements
   - stack and tool requirements
   - AI/workflow/document/eval/retrieval language
   - disqualifying mismatch, if any
   - whether the automated requirement extraction classified each must-have correctly
6. Classify each role as one of:
   - strong current target
   - current/stretch target
   - future/stretch market signal
   - dismiss/archive
   - noisy/unverified
7. Extract resume implications across the set:
   - repeated keywords to include when truthful
   - strongest evidence to foreground
   - claims to avoid
   - gaps to build next
8. Write a report under `job_search/output/` named:

   ```text
   job_search_deep_dive_YYYY-MM-DD.md
   ```

9. Summarize the top findings to the user and link the report.

## Report Shape

Use this structure:

```markdown
# Job Search Deep Dive - YYYY-MM-DD

Source report: `job_search/output/gmail_job_report_YYYY-MM-DD.md`

## Executive Summary

## Fit Buckets

### Current Qualified / Worth Deep Application
### Future / Stretch / Resume Direction Signal
### Dismiss / Archive / Noisy

## Role-by-Role Notes

## Resume Strategy From This Deep Dive

## Search System Notes

## Recommended Next Actions
```

## Classification Guidance

Strong current targets usually combine several of:
- applied AI implementation
- workflow automation
- document intelligence
- RAG/retrieval
- evals, guardrails, traceability, or human-in-loop review
- APIs and systems integration
- C#/.NET, Python, or other defensible stack overlap
- regulated, compliance-sensitive, legal, insurance, healthcare, or operational workflows
- plausible seniority

Future/stretch roles are useful market signals when they show the target direction but require too much current proof, such as:
- principal/staff ownership
- 7-8+ years in production AI systems
- production agentic systems at scale
- deep ML research credentials
- heavy architecture ownership beyond current evidence

Dismiss/archive roles usually include:
- patent/IP attorney or legal authority requirements
- direct healthcare domain expertise requirements Dorian cannot honestly claim
- security red-team specialization
- pure prompt/content/labeling roles
- sales/customer-success-heavy roles with little engineering
- location/language mismatch
- unverified/noisy aggregator results

## Ledger Boundary

Do not record `applied`, `dismissed`, or `saved` decisions during the deep dive unless the user explicitly asks.

The deep-dive report can recommend a decision batch. Actual ledger updates should be a separate confirmed step through `job_search/record_decisions.py`.
