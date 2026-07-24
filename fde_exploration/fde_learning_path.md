# FDE Learning Path

Date: 2026-07-23

## Purpose

This learning path covers the parts of forward-deployed AI engineering that do not appear to be
fully covered by the current repo learning direction.

It is meant to complement, not replace:

- [../APPLIED_AI_ENGINEERING_LEARNING_PLAN.md](../APPLIED_AI_ENGINEERING_LEARNING_PLAN.md)
- the main Applied AI Systems Engineer positioning
- the article and portfolio work already underway

The central idea:

> Dorian already has strong systems, workflow, debugging, document, and integration instincts.
> The main gap is the middle layer between an intelligent prototype and a customer-operable
> deployed workflow.

## What You Already Have

Based on the current repo, the strongest existing foundations are:

- software engineering fundamentals
- debugging and ambiguity tolerance
- enterprise and workflow software experience
- deployment and integration exposure
- data reconstruction and auditability instincts
- document intelligence and evidence-pipeline thinking
- human-review and deterministic-boundary instincts
- systems writing and architectural reasoning

## What You Are Already Learning

The current applied-AI learning plan already covers:

- structured outputs and validation
- retrieval and RAG failure modes
- workflow orchestration
- human review as a workflow boundary
- OpenAPI and MCP tool contracts
- observability
- evals

That means this document focuses on the adjacent FDE skills not yet covered clearly enough.

## Missing FDE-Relevant Learning Areas

### 1. Workflow Discovery And Solution Scoping

This is the pre-build layer:

- process mapping
- stakeholder discovery
- identifying pain points and exception paths
- deciding where AI belongs and where it should not
- defining success and rollback before implementation

Why it matters:

- forward-deployed work often begins before the system design is obvious
- the wrong workflow choice destroys value before model quality matters

### 2. Enterprise Integration Delivery

This is the glue layer between an idea and a deployable system:

- OAuth and service-account patterns
- webhooks
- background jobs
- queues
- retries
- idempotency
- sync vs async workflow boundaries
- unreliable upstream/downstream system handling

Why it matters:

- customer environments are messy
- many FDE problems are integration problems with AI inside them

### 3. Auth, Permissions, And Tenant Boundaries

This is only partly implied in the current repo.
It should become an explicit learning track:

- user/workspace/tenant models
- RBAC basics
- approval roles
- per-tenant configuration
- audit visibility rules
- secrets/config separation

Why it matters:

- production-shaped AI workflow systems need access boundaries before they need polish

### 4. Human Review UX And Queue Design

The repo already treats human review correctly as a system boundary.
The missing piece is product design for review:

- what evidence a reviewer actually needs
- review queues
- approval/reject/escalate states
- reviewer notes
- artifact history
- exception routing

Why it matters:

- bad review UX kills adoption even when the model is good enough

### 5. Production Operations For AI Workflows

Observability is already in the main plan.
This layer goes further:

- prompt and config versioning
- release comparison
- rollback strategy
- incident triage
- bad-output capture
- runbooks
- latency/cost/failure budgeting
- operational dashboards tied to workflow stages

Why it matters:

- FDE value often depends on operating the workflow safely after launch

### 6. Business Value Framing

This is not fluff.
It is part of implementation engineering:

- define the operator
- define the pain reduced
- define the measurable value
- define what manual work remains
- define why this should be a workflow, not a one-off demo

Why it matters:

- strong FDEs can explain why the system matters, not only how it works

### 7. Handoff, Enablement, And Change Management

This is a classic forward-deployed gap area:

- rollout checklists
- operator guides
- admin guides
- training artifacts
- known-failure-mode docs
- escalation paths
- support boundaries

Why it matters:

- the work is not done when the prototype works once
- the work is done when the customer can operate it without constant rescue

### 8. Security And Governance For Real Deployments

The repo has good instincts here, but the learning should be more explicit:

- secrets handling
- least privilege
- PII boundaries
- redaction strategy
- data retention and deletion rules
- approval gates for risky actions
- audit-log completeness

Why it matters:

- many attractive FDE opportunities live in sensitive workflow domains

## Recommended Learning Sequence

This sequence assumes the main six-week applied-AI curriculum stays intact.

## Phase 1: Workflow Discovery And Scoping

Goal:
- learn how to choose and shape the right workflow before building

Practice:

- map one messy workflow end to end
- identify actors, systems, documents, approvals, and exceptions
- write a one-page solution brief

Deliverables:

- workflow map
- exception map
- AI boundary note
- success metric note
- rollback note

Suggested exercise:

- use a legal-tech-debt flow, article research flow, or RenoNerd quote/intake flow

## Phase 2: Integration Mechanics

Goal:
- get comfortable with the ugly but real delivery layer

Practice:

- connect 2 or 3 systems with explicit boundaries
- add retries and idempotency
- model sync vs async steps

Deliverables:

- integration diagram
- boundary notes
- retry strategy
- failure-mode log

Suggested exercise:

- document upload -> parser -> artifact store -> review queue

## Phase 3: Auth, Roles, And Tenant Models

Goal:
- make the portfolio's "production-aligned" standard more real

Practice:

- add a simple user/workspace model to one small project
- define admin, reviewer, and operator roles
- document permission boundaries

Deliverables:

- role matrix
- tenant/workspace model note
- audit visibility rules

Suggested exercise:

- add user/workspace boundaries to the legal-tech-debt workbench concept

## Phase 4: Review UX And Human-In-The-Loop Product Design

Goal:
- make review operational instead of theoretical

Practice:

- design or build a simple review console
- show evidence, extracted artifact, validation flags, and decision state

Deliverables:

- reviewer screen mock or working page
- review-state model
- escalation rules

Suggested exercise:

- "approve / reject / needs escalation" workflow for one extracted artifact type

## Phase 5: Production Ops And Safety

Goal:
- learn to run AI workflows safely after deployment

Practice:

- version prompts/config
- compare runs across revisions
- add rollback notes and incident-response scenarios

Deliverables:

- release checklist
- incident playbook
- rollback notes
- operational dashboard sketch

Suggested exercise:

- define what happens when retrieval degrades, extraction fails, or model output format drifts

## Phase 6: Business Value And Adoption Framing

Goal:
- learn to explain and measure value the way an FDE must

Practice:

- define user, pain, metric, and expected gain for each project
- define what manual work remains

Deliverables:

- one-page business case
- operator pain note
- adoption and training note

Suggested exercise:

- compare "interesting prototype" versus "workflow worth deploying"

## Phase 7: Handoff And Enablement

Goal:
- leave behind something usable by other people

Practice:

- write operator docs
- write admin docs
- define escalation/support boundaries

Deliverables:

- operator guide
- admin guide
- handoff checklist

Suggested exercise:

- prepare a handoff pack as if giving the workflow to a small customer operations team

## Phase 8: Security And Governance Hardening

Goal:
- make the sensitive-workflow story more credible

Practice:

- define data classes
- define redaction rules
- define action-approval points
- document secrets handling

Deliverables:

- data classification note
- least-privilege note
- approval-gate note
- retention/deletion policy sketch

Suggested exercise:

- classify each artifact in a legal-tech-debt-style workflow as public, demo-safe, sensitive, or restricted

## Suggested 12-Week Combined Path

Weeks 1-6:
- complete the existing applied-AI curriculum

Week 7:
- workflow discovery and scoping

Week 8:
- auth, roles, and tenant boundaries

Week 9:
- enterprise integrations, queues, retries, idempotency

Week 10:
- reviewer UX, ops console thinking, and handoff

Week 11:
- production safety, rollback, and incident handling

Week 12:
- business metrics, adoption, enablement, and security hardening

## What Not To Prioritize Yet

Do not make these the center of gravity right now:

- deep model training or fine-tuning
- advanced MLOps platform specialization
- large-scale distributed infra for its own sake
- complex multi-agent systems before simple workflows are solid
- frontier-model research depth as a near-term hiring strategy

Reason:

- the current gap is not "more AI magic"
- the current gap is "make the system survivable in a real environment"

## Best Project Shapes For This Path

The strongest project shapes for this learning path are:

- document intake -> extraction -> validation -> review -> export
- research evidence workflow with retrieval, reviewer approval, and durable memory
- rules-plus-AI workflow where deterministic checks hold authority
- integration-heavy internal tool with explicit audit trail and approval states

## End State

The target outcome is not:

> I know more AI buzzwords.

The target outcome is:

> I can walk into a messy workflow, scope the right problem, build the right boundaries, connect
> the necessary systems, make the review process usable, operate it safely, and leave behind a
> workflow a customer can actually run.
