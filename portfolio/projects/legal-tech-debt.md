# Legal Tech Debt Portfolio Brief

Status: Primary applied AI portfolio anchor
Source repo: `D:\Repos\legal-tech-debt`
Public posture: Production-aligned demo target, not a live legal/compliance SaaS.

## Role In Portfolio

Legal Tech Debt is the strongest proof for applied AI document intelligence:

- source/corpus ingestion,
- structured evidence artifacts,
- deterministic smell detectors,
- graph-style provenance,
- LLM-assisted triage,
- human-reviewable reports,
- legal/compliance domain constraints,
- and market/feasibility discipline.

## Commercial Skeleton Target

The portfolio version should become a small evidence workbench:

- synthetic legal or insurance document package as public demo data,
- authenticated user/workspace boundary,
- upload or select demo corpus,
- run deterministic detectors and optional model triage,
- show source-traceable findings,
- allow human review states,
- generate an exportable report,
- record audit events for ingestion, detection, triage, review, and report export,
- expose enough observability to show failures and latency,
- and include an invoice-ready service path, likely manual invoice first and payment integration later.

## Current Proof Already Present

- [x] Real prototype evidence exists in `D:\Repos\legal-tech-debt`.
- [x] Kentucky homeowners proof work produced structured artifacts and findings.
- [x] Feasibility studies exist and avoid overclaiming.
- [x] Interactive workbench direction exists in Sandbox 006.
- [x] Synthetic demo dataset strategy exists.
- [x] Public examples should avoid real carrier text.

## Production-Aligned Gaps

- [ ] Public synthetic corpus exists and is runnable end to end.
- [ ] Public demo app boundary exists.
- [ ] User/workspace model exists.
- [ ] Auth provider or auth-ready stub exists.
- [ ] Billing/invoicing path exists.
- [ ] Audit log captures important workflow events.
- [ ] Observability captures parse, retrieval, model, validation, and report steps.
- [ ] Report export is demo-safe.
- [ ] Cutover checklist distinguishes demo, paid pilot, and real customer data.

## First Commercially Shaped Milestone

Build a deployable demo over synthetic documents:

1. User signs in or uses a clearly labeled demo workspace.
2. User selects the synthetic corpus.
3. System runs the evidence pipeline.
4. User reviews findings in a workbench.
5. User exports a report.
6. System records audit events.
7. A test-mode/manual invoice path exists for "request paid review."

## Claim Boundary

Safe claim:

> A production-aligned applied AI evidence workbench demo for legal/compliance document review, using synthetic data and source-traceable outputs.

Unsafe until proven:

> Production legal advice platform, live compliance SaaS, or certified regulatory review system.

