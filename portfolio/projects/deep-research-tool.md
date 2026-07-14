# Deep Research Tool Portfolio Brief

Status: Secondary applied AI portfolio anchor
Source folder: `deep-research-tool-starter/`
Public posture: Production-aligned research evidence engine, not a generic chatbot.

## Role In Portfolio

The Deep Research Tool should prove applied AI engineering around:

- ingestion and normalization,
- retrieval,
- citation/provenance tracking,
- graph-backed relationship modeling,
- semantic suggestions,
- evidence bundles,
- grounded synthesis,
- evaluation,
- and durable research memory.

It should support the article series and also stand alone as a document intelligence portfolio app.

## Commercial Skeleton Target

The target product shape is a research console:

- user/workspace boundary,
- project corpus ingestion,
- source manifest and provenance records,
- exact, lexical, graph, and semantic retrieval,
- evidence bundle generation,
- grounded report draft generation,
- human approval before promotion into durable memory,
- audit trail for source ingestion, retrieval runs, model calls, promotions, and exports,
- billing/invoicing path for a research workspace or evidence-report engagement,
- and a demo-safe public corpus.

## Current Proof Already Present

- [x] Starter repo exists.
- [x] Vision, architecture, roadmap, SDLC, artifact model, and evaluation docs exist.
- [x] Article research corpus exists under `articles/`.
- [x] Knowledge graph pipeline exists in scripts and agent guidance.
- [x] Production-aligned standard is now recorded in starter docs.

## Production-Aligned Gaps

- [ ] App boundary exists beyond docs.
- [ ] User/workspace model exists.
- [ ] Auth provider or auth-ready stub exists.
- [ ] Billing/invoicing path exists.
- [ ] Demo corpus is selected and documented.
- [ ] Source ingestion creates stable persisted records.
- [ ] Retrieval layer is exposed through a usable interface.
- [ ] Audit events are emitted for important actions.
- [ ] Observability exists for parsing, retrieval, model, and validation steps.
- [ ] Evaluation fixtures exist.
- [ ] Cutover checklist exists for real customer research data.

## First Commercially Shaped Milestone

Build a deployable single-user demo with a workspace model already present:

1. User signs in or enters a demo workspace.
2. User selects an article/research corpus.
3. System retrieves supporting evidence for one claim.
4. System shows source provenance and uncertainty.
5. User promotes a finding into a report draft.
6. System records the audit trail.
7. A test/manual invoice path exists for "research evidence report."

## Claim Boundary

Safe claim:

> A production-aligned research evidence engine prototype for turning messy source material into traceable findings and report drafts.

Unsafe until proven:

> Fully automated research assistant, production knowledge management SaaS, or verified research oracle.

