# Copilot Instructions

## Single Entry Point

This file is the single entry point for GitHub Copilot when working in this repository.
It mirrors the startup contract in [AGENTS.md](../AGENTS.md).

Bootstrap in this order:
1. read this file
2. read [AGENT_BOOTSTRAP_COMPACT.md](../AGENT_BOOTSTRAP_COMPACT.md)
3. read only the specific supporting docs needed for the current task

Do not begin by loading every context file in the repo.

Preferred CLI: Use WSL for repository scripts, especially the Gmail job-report runner. The old direct job-board/ATS search runners are retired and must not be used for discovery unless the user explicitly asks for legacy diagnostics or a workflow change.

## Environment & Tool Constraints

- Never use visual or GUI tools (such as File Explorer, native application windows, or browser screenshots) if a command-line alternative is available.
- Always prefer executing commands within Windows Subsystem for Linux (WSL) over any other interface.
- If a task cannot be handled within WSL, fall back to standard CLI tools or PowerShell commands.
- Use text-based terminal utilities (e.g., `ls`, `grep`, `find`, `cat`, `Get-ChildItem`) exclusively for navigating file systems and managing project tasks.

## Bootstrap Rule

The compact bootstrap file is the default machine-facing context layer.
It should stay short, dense, and optimized for quick agent loading.

The human-readable explanation of that bootstrap lives in:
- [agent_bootstrap_human.md](../agent_bootstrap_human.md)

Whenever the compact bootstrap changes, update the human-readable document in the same change.

## Source Context Files

The compact bootstrap is derived from these source files:
- [JOB_HUNT_CONTEXT.md](../JOB_HUNT_CONTEXT.md)
- [current_strategy.md](../current_strategy.md)
- [COVER_LETTER_RULES.md](../COVER_LETTER_RULES.md)
- [ROLE_EVAL_CHECKLIST.md](../ROLE_EVAL_CHECKLIST.md)
- [RECRUITER_RESPONSE_RULES.md](../RECRUITER_RESPONSE_RULES.md)
- [RESUME_BULLET_RULES.md](../RESUME_BULLET_RULES.md)
- [APPLICATION_WORKFLOW.md](../APPLICATION_WORKFLOW.md)

Only read the full source file when the current task actually needs that detail.

## Working Rules For Agents

## Repo State (as of 2026-06-26)

This repo was refactored on 2026-06-26 to a single positioning: **Applied AI Systems Engineer**.

- All simulation, HPC, defense, and generic cloud/Java application history is in `archive/pre-ai-pivot-2026-06/`. Do not reference it in new work.
- `master_tracker.md` is clean. Two applications are on record (Ikuto 2026-06-18, CyberCoders portfolio co. 2026-06-25).
- `applications/` contains only AI-relevant applications.
- `cover_letters/` is empty — ready for first AI-era cover letter.
- UI reporting week of 2026-06-23/06-29 has one qualifying application (CyberCoders 2026-06-25). UI submission due week of June 30.

- Keep employer-facing writing truthful, restrained, and role-specific.
- Keep Dorian-facing analysis honest, structured, and strategically useful.
- Prefer the narrower defensible claim over the broader impressive claim.
- Do not fabricate employers, titles, certifications, years of experience, clearance, or unsupported domain expertise.
- Optimize for coherent direction, not application spam.
- Protect runway, learning time, and the Applied AI Systems Engineer positioning.
- Gmail job alerts are the sole active job-discovery channel. Do not perform a separate LinkedIn, Indeed, Google Jobs, ATS, startup, or contracting search unless the user explicitly changes this policy.
- Keep machine-managed search bookkeeping in `job_search/ledger/`; do not auto-update `master_tracker.md` from search runs.
- Keep company watchlist updates in `company_watchlist.md`; do not fold watchlist checks into `master_tracker.md`.
- Do not draw from or reference `archive/` in new applications or materials.

## Workflow Requirement

For application work:
1. bootstrap from the compact context
2. record the exact posting URL in the application's `job_description.md`
3. follow the default workflow in [APPLICATION_WORKFLOW.md](../APPLICATION_WORKFLOW.md)

For all active job discovery and application preparation, follow [job_search/GMAIL_JOB_APPLICATION_WORKFLOW.md](../job_search/GMAIL_JOB_APPLICATION_WORKFLOW.md). The canonical flow is: user-configured Gmail alerts -> bounded starred-message report -> canonical posting-link recovery -> full-posting verification -> deep dive and user review -> optional review-only application materials -> tracker/application updates only after confirmed submission.

The Gmail report window is the shorter of the two constraints: messages newer than the last successful report, with a maximum lookback of 14 days. Do not backfill older alerts merely to reach a target count. The report is the discovery run; the old direct-search runner, ATS sweep, and contract-search runner are retired.

Canonical application record rule:
- Count an application as real only when a matching `applications/...` folder and `master_tracker.md` row both exist.
- Gmail labels, emails, or a single incomplete artifact do not establish application history.
- If either side is missing, report the record as incomplete/unconfirmed and do not count it as an application.

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

## Knowledge Graph Pipeline

The repo has a research pipeline that supports the article series at `articles/series-*/`.
It fetches citation metadata from Semantic Scholar, downloads PDFs, parses them with Docling, and builds a queryable Kuzu graph database.

Run all scripts from repo root via WSL:

```sh
# 1. Fetch citation metadata for seed papers
SEMANTIC_SCHOLAR_API_KEY=$(grep SAMANTIC secrets/credentials.txt | cut -d= -f2) \
  python3 scripts/fetch-citations.py
# → writes articles/papers/citations.json

# 2. Download ref PDFs (optional; requires human review before parsing)
python3 scripts/download-refs.py

# 3. Ingest: parse seed PDFs fully; register refs as metadata-only nodes
python3 scripts/ingest.py --seeds-only
# → writes articles/graph.kuzu

# 4. Query the graph
python3 scripts/query.py hot-refs                    # refs cited by multiple seeds
python3 scripts/query.py search "test-driven"        # full-text across parsed sections
python3 scripts/query.py explore "retrieval"         # keyword search on ref titles/abstracts
python3 scripts/query.py for-article S2-A8           # papers supporting a specific article plan
python3 scripts/query.py who-cites "agentassay"      # which seeds cite a paper (title keyword)
python3 scripts/query.py citing 2603.02601           # papers citing a given arXiv ID
```

Key facts:
- API key is in `secrets/credentials.txt` under key name `SAMANTIC_SCHOLAR_API_KEY` (typo — 'A' not 'E'; do not fix the grep, just use as-is)
- `articles/graph.kuzu` is a **single file** on NTFS/WSL (not a directory) — this is expected Kuzu behaviour
- `articles/papers/citations.json` is tracked when it contains curated citation truth; `articles/papers/*.pdf`, `articles/refs/*.pdf`, and `articles/graph.kuzu` are gitignored
- Do not run `ingest.py` without `--seeds-only` unless ref parsing has been approved — 586 PDFs, ~8 hours of Docling runtime
- `search` is case-sensitive substring matching — use hyphens: `"test-driven"` not `"test driven"`
- If ingest crashes mid-run (Kuzu `unordered_map::at` error): delete `articles/graph.kuzu` and `articles/graph.kuzu.wal` before rerunning

## Article Citation Integrity

For article work under `articles/series-*/`, do not treat a citation as valid merely because a link resolves.

- Every cited source must be germane to the article claim it supports.
- Every local PDF link in an article must point to the exact paper named in the citation, and referenced local PDFs should live in `articles/papers/`.
- Verify local PDFs by checking the PDF header plus title/first-page text or reliable metadata before declaring links fixed.
- Do not substitute adjacent, loosely related, or convenient papers for missing sources.
- For DOI-only or web-only sources, record them honestly as having no local file instead of inventing or mislabeling a PDF.
- When citation sources change, update `articles/papers/citations.json` so the article-specific citation record reflects the current truth: title, authors, year, URL/DOI/arXiv ID, local file when present, verification status, and article relevance.
- If a paper is promoted from supporting background to an article citation, add it to the citation manifest and relevant script seed lists so future graph runs do not erase the source relationship.

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
- [AGENT_BOOTSTRAP_COMPACT.md](../AGENT_BOOTSTRAP_COMPACT.md)
- [agent_bootstrap_human.md](../agent_bootstrap_human.md)

Keep the compact layer minimal.
Keep the human layer understandable.
