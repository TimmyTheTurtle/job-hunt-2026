# Agent Bootstrap Guide

This document explains the compact agent bootstrap layer and how it should be maintained.

## Purpose

The repository now uses a layered context model for agents:

1. [AGENTS.md](../AGENTS.md) is the single entry point.
2. [AGENT_BOOTSTRAP_COMPACT.md](../AGENT_BOOTSTRAP_COMPACT.md) is the compact machine-facing bootstrap context.
3. The fuller policy and candidate docs remain available as source material.

The goal is to let agents load only the minimum durable context needed at startup while still keeping a human-readable explanation in the repo.

`AGENTS.md` should stay short and route startup behavior.
`AGENT_BOOTSTRAP_COMPACT.md` should carry the actual startup context.
Detailed policy and maintenance explanation belongs here or in the source docs, not duplicated in both startup files.

Company monitoring follows the same layered approach:
- `company_watchlist.md` is for employers Dorian wants to revisit before applying
- `master_tracker.md` is for actual applications
- `job_search/ledger/` is for machine-managed search bookkeeping

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

1. read [AGENTS.md](../AGENTS.md)
2. read [AGENT_BOOTSTRAP_COMPACT.md](../AGENT_BOOTSTRAP_COMPACT.md)
3. read only the specific detailed source docs needed for the active task

Examples:
- For a cover letter, read the compact bootstrap plus [COVER_LETTER_RULES.md](../COVER_LETTER_RULES.md).
- For role triage, read the compact bootstrap plus [ROLE_EVAL_CHECKLIST.md](../ROLE_EVAL_CHECKLIST.md).
- For recruiter replies, read the compact bootstrap plus [RECRUITER_RESPONSE_RULES.md](../RECRUITER_RESPONSE_RULES.md).

As part of the default application workflow, agents should also preserve the exact job posting URL in the application's `job_description.md` before drafting. That URL is part of the UI audit trail.

For search bookkeeping, agents should treat the machine-managed search ledger and the manual application tracker as separate systems:
- `job_search/ledger/` for duplicate suppression and fast decision logging
- `master_tracker.md` for supervised/manual application logging

## Source Of Truth

The compact bootstrap is a distilled mirror of these source files:

- [JOB_HUNT_CONTEXT.md](../JOB_HUNT_CONTEXT.md)
- [COVER_LETTER_RULES.md](../COVER_LETTER_RULES.md)
- [ROLE_EVAL_CHECKLIST.md](../ROLE_EVAL_CHECKLIST.md)
- [RECRUITER_RESPONSE_RULES.md](../RECRUITER_RESPONSE_RULES.md)
- [RESUME_BULLET_RULES.md](../RESUME_BULLET_RULES.md)
- [APPLICATION_WORKFLOW.md](../APPLICATION_WORKFLOW.md)

The compact file should not become the only place where meaning lives. It is a compressed operational summary.

## What Belongs In The Compact File

Keep in the compact file:
- default candidate positioning
- strongest themes and constraints
- role hierarchy summary
- truth constraints
- default workflow
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
- [AGENT_BOOTSTRAP_COMPACT.md](../AGENT_BOOTSTRAP_COMPACT.md)
- this file

This includes changes to:
- candidate positioning
- strategic direction
- truthfulness constraints
- role tier logic
- writing constraints
- default workflow

The compact file should remain optimized for startup.
This file should remain optimized for humans who need to understand the system.

## Recommended Mental Model

- `AGENTS.md` = where agents start
- `AGENT_BOOTSTRAP_COMPACT.md` = what agents load first
- source rule/context docs = what agents read on demand
- this document = why the bootstrap layer exists and how to keep it healthy
