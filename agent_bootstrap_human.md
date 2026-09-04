# Agent Bootstrap Guide

This document explains the compact agent bootstrap layer and how it should be maintained.

## Purpose

The repository now uses a layered context model for agents:

1. [AGENTS.md](AGENTS.md) is the single entry point.
2. [AGENT_BOOTSTRAP_COMPACT.md](AGENT_BOOTSTRAP_COMPACT.md) is the compact machine-facing bootstrap context.
3. The fuller policy and candidate docs remain available as source material.

The goal is to let agents load only the minimum durable context needed at startup while still keeping a human-readable explanation in the repo.

`AGENTS.md` should stay short and route startup behavior.
`AGENT_BOOTSTRAP_COMPACT.md` should carry the actual startup context.
Detailed policy and maintenance explanation belongs here or in the source docs, not duplicated in both startup files.

Company monitoring follows the same layered approach:
- `company_watchlist.md` is for employers Dorian wants to revisit before applying
- `master_tracker.md` is for actual applications
- `job_search/ledger/` is for machine-managed search bookkeeping

## Current Positioning Paradigm

As of 2026-06-16, the primary job-search identity is:

> Applied AI Systems Engineer

This replaces the earlier simulation/C++-first positioning as the default identity. The older systems, C++, simulation, graphics, and real-time systems vector remains useful technical depth, but it is secondary unless a role directly calls for that background.

The new default story is:

> A systems-oriented software engineer moving into applied AI systems for document-heavy, compliance-sensitive workflows, with emphasis on traceability, validation, deterministic boundaries, human review, and audit-ready evidence.

The preferred voice explains this by following the positive pattern rather than defining Dorian by what he is not. A good short version is:

> I build systems that turn messy domain material into structured, reviewable evidence. Right now, AI is becoming part of that system.

Agents should not overclaim. Dorian should not be presented as a finished ML researcher, production LLM platform veteran, lawyer, compliance officer, or legal-domain authority. The honest current stage is a transition/proof-building phase backed by:
- WindowConfigurator/RenoNerd as emerging production-minded .NET configurator evidence, not production-adjacent yet
- legal-tech-debt as applied AI/document intelligence prototype evidence
- Areva as early compliance-sensitive reporting automation evidence
- SED Systems as the origin of mission/system discipline

Forward-deployed AI engineering is the intended destination, not the exclusive present-tense target. Search should keep it as a smaller current/stretch or future/stretch family while prioritizing attainable applied-AI application, implementation, integration, document-intelligence, workflow-automation, and adjacent systems roles that build the proof needed for that destination.

Portfolio projects should be evaluated against a production-aligned commercial skeleton standard. The goal is not a toy demo or notebook. The target shape is: deployable app, environment-based configuration, secure secret handling, authentication/authorization, user or tenant boundaries, billing or invoicing path, audit logs, observability, human-review gates for AI outputs, demo-safe data boundaries, and a documented cutover checklist. Project-specific portfolio proof belongs under [portfolio/](portfolio/). Agents should describe this as production-aligned engineering discipline unless live production customers, revenue, scale, or mature compliance controls are actually present.

## Why This Exists

Without a compact bootstrap layer, agents tend to:
- load too much context up front
- duplicate or drift instructions across files
- treat long human-readable strategy documents as startup material

The compact bootstrap is meant to solve that by keeping the default startup context:
- small
- dense
- stable
- derived from canonical source docs

## Bootstrap Sequence For Agents

Every agent should:

1. read [AGENTS.md](AGENTS.md)
2. read [AGENT_BOOTSTRAP_COMPACT.md](AGENT_BOOTSTRAP_COMPACT.md)
3. read only the specific detailed source docs needed for the active task

Examples:
- For a cover letter, read the compact bootstrap plus [COVER_LETTER_RULES.md](COVER_LETTER_RULES.md).
- For role triage, read the compact bootstrap plus [ROLE_EVAL_CHECKLIST.md](ROLE_EVAL_CHECKLIST.md).
- For recruiter replies, read the compact bootstrap plus [RECRUITER_RESPONSE_RULES.md](RECRUITER_RESPONSE_RULES.md).

As part of the default application workflow, agents should also preserve the exact job posting URL in the application's `job_description.md` before drafting. That URL is part of the UI audit trail.

For search bookkeeping, agents should treat the machine-managed search ledger and the manual application tracker as separate systems:
- `job_search/ledger/` for duplicate suppression and fast decision logging
- `master_tracker.md` for supervised/manual application logging

For search-result analysis, agents should use [job_search/DEEP_DIVE_WORKFLOW.md](job_search/DEEP_DIVE_WORKFLOW.md) when the user asks to follow links, classify surfaced jobs, compare current fit against future/stretch roles, capture compensation, or extract resume implications. This keeps the deep-dive step separate from the raw search runner and from ledger decision updates.

For Gmail-led job discovery and application preparation, agents should use [job_search/GMAIL_JOB_APPLICATION_WORKFLOW.md](job_search/GMAIL_JOB_APPLICATION_WORKFLOW.md). It bounds starred-message searches to the later of the last successful run or fourteen days, recovers canonical public posting links from full message bodies, requires full-posting verification, unflags only explicitly reviewed messages, uses visible `Jobs/Reviewed`, `Jobs/Applied`, and `Jobs/Rejections` status labels, and keeps preparation-only folders separate from Applied bookkeeping.

Application history is canonical only when the matching application folder and `master_tracker.md` row both exist. Gmail labels, emails, or one incomplete artifact are not enough to count an application; missing one side is reported as incomplete or unconfirmed.

The raw search runner is qualification-aware. It reads the conservative evidence inventory in [job_search/candidate_profile.json](job_search/candidate_profile.json), extracts explicit requirements from each available posting description, and keeps qualification separate from topic relevance. A missing or thin posting is unverified; it cannot become `Apply First`. Hard gaps such as active-clearance requirements, unsupported specific tenure, required credentials, or an incompatible location override an attractive title or long-term learning value. Candidate-profile claims must come from defensible, non-archived resume and project evidence, with professional experience kept distinct from portfolio work and exposure.

The active search is focused on AI-engineering roles: applied AI systems and applications, AI integration/implementation/solutions, LLM/RAG, document intelligence, AI workflow automation, and compliance-sensitive AI. Generic software, data, DevOps, or implementation roles are secondary unless the posting is explicitly AI-enabled.

Full-time and contracting runs maintain separate surfaced-result suppression. A URL surfaced by one profile may still appear in the other profile for an independent evaluation; applied, saved, and dismissed decisions remain global across profiles.

For serious search discovery, agents should pair the normal runner with [job_search/ATS_SWEEP_WORKFLOW.md](job_search/ATS_SWEEP_WORKFLOW.md). That sweep covers Ashby, Greenhouse, Lever, YC Work at a Startup, Hacker News "Who is hiring?", and direct company career pages, which often contain sharper applied-AI roles than the broad job boards.

For contracting, consulting, or fractional work, agents should use [job_search/CONTRACT_SEARCH_WORKFLOW.md](job_search/CONTRACT_SEARCH_WORKFLOW.md) and the dedicated contracting profile at [job_search/search_profile_contracting.json](job_search/search_profile_contracting.json). Contract review should capture rate, duration, W2/1099/C2C status, expected weekly hours, timezone constraints, client-facing load, and whether the work creates useful portfolio evidence.

For article and research work, agents should treat citation integrity as part of the work, not as a cleanup detail. A resolving markdown link is not enough. The source must actually support the article claim, local PDF links must point to the exact named paper, and DOI-only or web-only sources should be marked honestly rather than replaced with a convenient unrelated PDF. When article citations change, the tracked `articles/papers/citations.json` should include the current article-specific truth: title, authors, year, URL/DOI/arXiv ID, local file when present, verification status, and why the source is germane.

## Source Of Truth

The compact bootstrap is a distilled mirror of these source files:

- [JOB_HUNT_CONTEXT.md](JOB_HUNT_CONTEXT.md)
- [current_strategy.md](current_strategy.md)
- [COVER_LETTER_RULES.md](COVER_LETTER_RULES.md)
- [ROLE_EVAL_CHECKLIST.md](ROLE_EVAL_CHECKLIST.md)
- [RECRUITER_RESPONSE_RULES.md](RECRUITER_RESPONSE_RULES.md)
- [RESUME_BULLET_RULES.md](RESUME_BULLET_RULES.md)
- [APPLICATION_WORKFLOW.md](APPLICATION_WORKFLOW.md)

The compact file should not become the only place where meaning lives. It is a compressed operational summary.

## What Belongs In The Compact File

Keep in the compact file:
- default candidate positioning
- strongest themes and constraints
- role hierarchy summary
- truth constraints
- default workflow
- search deep-dive trigger and ledger boundary
- ATS/startup sweep trigger for serious job discovery
- contract-search trigger and contract-specific review fields
- article citation integrity requirements
- critical recordkeeping requirements like preserving the exact posting URL
- company watchlist checks for employers Dorian wants to revisit
- short reminders about tone and strategy

Do not put in the compact file:
- long narrative explanation
- detailed examples unless they are essential
- duplicated prose from every source document
- source-doc inventories that already live in `AGENTS.md`
- maintenance prose that is only useful to humans
- temporary application-specific details

## Maintenance Rule

Whenever any agent changes underlying meaning in the source context, that agent should update:
- the relevant source context file(s)
- [AGENT_BOOTSTRAP_COMPACT.md](AGENT_BOOTSTRAP_COMPACT.md)
- this file

This includes changes to:
- candidate positioning
- strategic direction
- truthfulness constraints
- role tier logic
- writing constraints
- default workflow
- article citation/source integrity workflow

The compact file should remain optimized for startup.
This file should remain optimized for humans who need to understand the system.

## Recommended Mental Model

- `AGENTS.md` = where agents start
- `AGENT_BOOTSTRAP_COMPACT.md` = what agents load first
- source rule/context docs = what agents read on demand
- this document = why the bootstrap layer exists and how to keep it healthy
