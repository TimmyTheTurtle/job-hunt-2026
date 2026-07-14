# Applied AI Engineering Learning Plan

Purpose: build a grounded, non-proprietary foundation for Applied AI Systems Engineering so the article series is informed by practice, not only systems-engineering instinct.

This plan is intentionally:
- open standards first
- small-project driven
- workflow-oriented rather than buzzword-oriented
- compatible with document intelligence, compliance-sensitive automation, and human-reviewable AI systems

It is not a certification checklist.
It is a six-week build-and-learn sequence meant to produce:
- practical familiarity with common open tooling
- repeated exposure to real AI-system failure modes
- better language for job positioning
- stronger raw material for future articles
- production-aligned portfolio artifacts that show deployability, user boundaries, auditability, and commercial readiness

Pluralsight is the certificate-bearing support layer for this plan.
Use it to document structured study for UI and to accelerate the open-tooling work, but do not let the courses replace the small projects.

---

## Portfolio Build Standard

The small projects should be designed as commercial skeletons, not disposable demos.

Where a project is intended for portfolio use, it should have a credible path to:
- deploy with environment-specific configuration,
- connect real authentication and authorization,
- separate users, tenants, or workspaces when relevant,
- support billing or invoicing without re-architecting,
- protect secrets and customer data,
- preserve audit trails and evidence records,
- expose health, error, and workflow-state observability,
- use synthetic/demo-safe data until live-data controls exist,
- and document the cutover checklist for real use.

This does not mean every learning slice needs full SaaS infrastructure on day one. It means the architecture should avoid choices that would make commercial use a rewrite.

## Core Principle

Do not try to "learn AI engineering" as a giant abstract field.

Instead:
1. learn one small layer
2. build one small project around it
3. observe where the system fails
4. write down the pattern and the failure mode
5. move to the next layer

The goal is to experience the common engineering problems directly:
- schema drift
- bad extraction
- retrieval misses
- hallucinated tool use
- poor workflow state management
- weak observability
- missing eval coverage
- prompt injection and boundary failures

That is the material good articles are made from.

---

## Open Standards And Shared Foundations

These are the main non-proprietary foundations to learn first.

### Data Contracts

- `JSON Schema`
- `Pydantic` as a practical local enforcement layer

Learn:
- required vs optional fields
- enums, patterns, ranges, nested objects
- validation failures
- versioning of structured outputs

Why it matters:
- structured extraction
- typed intermediate artifacts
- machine-checkable boundaries
- safer LLM output handling

### Service Contracts

- `OpenAPI`

Learn:
- operation specs
- request/response schemas
- tool/service discoverability
- idempotent endpoints
- explicit error responses

Why it matters:
- tool-calling workflows
- internal AI services
- contract-first design

### Tool Integration

- `Model Context Protocol (MCP)`

Learn:
- tool exposure model
- resources vs tools
- client/server boundary
- permission surface
- transport and contract thinking

Why it matters:
- open, portable tool integration
- grounding agent workflows in explicit interfaces

### Telemetry

- `OpenTelemetry`

Learn:
- spans
- trace hierarchy
- attributes
- events
- failure tagging
- per-step timing

Why it matters:
- AI systems are hard to debug without traces
- this is one of the few real cross-stack observability standards

### Evaluation

- `promptfoo`

Learn:
- eval fixtures
- assertions
- regression checks
- adversarial test cases
- pass/fail discipline for LLM features

Why it matters:
- this is how you stop talking about quality in the abstract

---

## Recommended Open Tooling

These are tools to learn as practice surfaces, not as ideology.

### Workflow Runtime

- `LangGraph`

Use for:
- stateful workflows
- resumable steps
- human review interrupts
- explicit node/edge orchestration

### Retrieval And Document Work

- `LlamaIndex`

Use for:
- ingestion
- chunking
- indexing
- retrieval
- structured extraction experiments
- evaluation-oriented RAG work

### Validation Layer

- `Pydantic`

Use for:
- typed artifacts
- runtime validation
- schema-backed outputs

### API Layer

- `FastAPI`

Use for:
- small OpenAPI-described tool services
- local workflow endpoints
- clean contracts

### Local Storage Options

- `SQLite` for simple workflow state and artifacts
- `Kuzu` for graph experiments
- filesystem JSON/JSONL for transparent intermediate outputs

Avoid hiding too much too early in framework state.

---

## Design Patterns To Learn On Purpose

These are more important than memorizing framework APIs.

### Pattern 1: Schema-First Extraction

Input:
- messy document

Output:
- validated structured object

Key idea:
- the LLM does not "return text"
- it attempts to populate a typed artifact

### Pattern 2: Deterministic-First, Model-Second

Do:
- regex
- parser
- rules
- exact lookup
- validation

Before:
- model judgment

Key idea:
- reserve LLM work for ambiguity, not for chores

### Pattern 3: Retrieve, Then Reason

Do not ask the model to answer from memory when the answer should come from:
- documentation
- source text
- a policy clause
- a filing rule

Key idea:
- context selection is architecture

### Pattern 4: Human Gate On Ambiguous Steps

Use human review when:
- confidence is weak
- evidence conflicts
- business consequence is real
- output crosses from draft into decision

Key idea:
- human-in-loop is a system boundary, not a patch for bad prompts

### Pattern 5: Explicit Workflow State

Track:
- current stage
- artifact version
- evidence source
- validation status
- human review status
- retry count

Key idea:
- AI systems fail messily when state is implicit

### Pattern 6: Trace Every Important Step

Record:
- input type
- output artifact
- model/tool used
- duration
- token/cost if available
- validation result
- retry/failure cause

Key idea:
- if you cannot inspect the path, you cannot improve it

### Pattern 7: Eval Fixture Before Generalization

Before saying a feature "works":
- write examples
- write expected constraints
- test easy cases
- test adversarial cases
- test missing-context cases

Key idea:
- working once is not a feature

---

## Six-Week Plan

Each week has:
- concepts
- tools
- one small project
- concrete output
- article angles unlocked
- Pluralsight support where it usefully reinforces the week

### Week 1: Structured Outputs And Validation

Focus:
- JSON Schema
- Pydantic
- schema-backed extraction

Pluralsight support:
- `FastAPI Fundamentals`
- `Validate Data Classes with Pydantic`

Small project:
- Build a tiny extractor that reads one messy source document and produces a typed JSON artifact.

Suggested document types:
- job posting
- policy excerpt
- contract clause
- technical ADR

Artifact examples:
- `RoleSummary`
- `ObligationRecord`
- `ClaimRule`
- `RequirementItem`

Deliverables:
- schema file
- Pydantic model
- sample input docs
- extraction script
- saved valid and invalid outputs
- short note on failure modes

What to learn by building:
- which fields are easy to extract
- where ambiguity destroys clean structure
- what validation catches immediately
- what still requires judgment

Article hooks:
- structured outputs are boundary tools, not formatting tricks
- why schema-first extraction changes workflow design

### Week 2: Retrieval Basics And RAG Failure Modes

Focus:
- chunking
- indexing
- retrieval
- source citation
- answer grounding

Tools:
- LlamaIndex

Pluralsight support:
- `Retrieval Augmented Generation (RAG) for Developers`
- `Implementing Vector Search with LlamaIndex`

Small project:
- Build a tiny RAG system over 5 to 15 documents from one narrow domain.

Good domains:
- your article drafts
- public insurance/legal guidance
- product documentation
- small technical standards set

Deliverables:
- ingest pipeline
- chunking strategy note
- retrieval query script
- answer-with-citations flow
- 15 to 20 question eval set
- log of retrieval misses

What to learn by building:
- why naive chunking fails
- when retrieval returns plausible but wrong context
- how much answer quality depends on retrieval quality
- the difference between search and usable evidence retrieval

Article hooks:
- retrieval is not memory, it is selection architecture
- chunking is an engineering decision, not preprocessing trivia

### Week 3: Workflow Orchestration And Human Review

Focus:
- explicit workflow state
- node-based orchestration
- human interrupt/resume
- retries and failure handling

Tools:
- LangGraph

Pluralsight support:
- `LangChain Development`
- `Introduction to LangGraph`

Small project:
- Build a five-step workflow:
  1. ingest
  2. classify
  3. retrieve
  4. extract
  5. human review

Deliverables:
- graph definition
- typed workflow state
- persisted checkpoints
- simple review step
- examples of paused and resumed runs

What to learn by building:
- where state becomes awkward
- where retries are safe vs unsafe
- what steps should be deterministic
- what human review actually needs to see

Article hooks:
- most "agent" systems are really workflow-state problems
- human-in-loop only works when the state model is clean

### Week 4: Tool Contracts, APIs, And MCP Thinking

Focus:
- OpenAPI
- MCP
- tool boundaries
- idempotent service design

Tools:
- FastAPI
- MCP SDK in the language/runtime that feels most practical

Pluralsight support:
- `Getting Started with Swagger 2 Tools`
- `Using OpenAPI/Swagger for Testing and Code Generation in ASP.NET Core`
- `Model Context Protocol in Practice`

Small project:
- Expose 2 or 3 local capabilities behind explicit contracts.

Good capability examples:
- document search
- schema validation
- rule lookup
- artifact persistence

Deliverables:
- one small FastAPI service with OpenAPI
- one small MCP server exposing a useful local capability
- short comparison note: API tool vs MCP tool
- permission and boundary notes

What to learn by building:
- what belongs behind a tool boundary
- why vague tool descriptions create bad behavior
- how interface shape changes workflow quality
- why tool design matters as much as prompts

Article hooks:
- open tool contracts are a missing part of AI engineering conversations
- MCP matters less as hype and more as interface discipline

### Week 5: Observability And Debuggable AI Systems

Focus:
- traces
- spans
- events
- artifact-linked observability
- failure analysis

Tools:
- OpenTelemetry

Pluralsight support:
- `Observability with OpenTelemetry and Grafana`

Small project:
- Add tracing to the Week 3 or Week 4 workflow.

Track:
- retrieval start/end
- model invocation
- validation pass/fail
- human review handoff
- tool call latency
- workflow completion/failure

Deliverables:
- instrumented workflow
- trace screenshots or exported logs
- failure taxonomy from real runs
- note on what was invisible before tracing

What to learn by building:
- how much time is spent where
- where retries cluster
- which step is actually unstable
- how little intuition alone tells you

Article hooks:
- observability is not optional in AI systems
- tracing reveals workflow truth that prompts cannot

### Week 6: Evals, Adversarial Inputs, And Regression Discipline

Focus:
- eval fixtures
- regression testing
- adversarial inputs
- confidence boundaries

Tools:
- promptfoo

Pluralsight support:
- finish any incomplete RAG / LangGraph / MCP coursework
- promptfoo remains official-docs-first rather than Pluralsight-first

---

## Strongest Pluralsight Sequence

These are the strongest Pluralsight items for Applied AI engineering coverage inside this plan.

### Primary Sequence

1. `FastAPI Fundamentals`
2. `Validate Data Classes with Pydantic`
3. `Observability with OpenTelemetry and Grafana`
4. `LangChain Development`
5. `Retrieval Augmented Generation (RAG) for Developers`
6. `Implementing Vector Search with LlamaIndex`
7. `Introduction to LangGraph`
8. `Model Context Protocol in Practice`

### Secondary Support

- `Getting Started with Swagger 2 Tools`
- `Using OpenAPI/Swagger for Testing and Code Generation in ASP.NET Core`
- `Generating OpenAPI Contracts in ASP.NET Core 10`

Use the primary sequence as the core curriculum.
Use the secondary support items to deepen API-contract thinking where useful.

Small project:
- Write an eval harness around one of the earlier projects.

Include:
- normal cases
- edge cases
- malformed documents
- contradictory evidence
- retrieval failure cases
- prompt injection attempts

Deliverables:
- eval config
- test corpus
- pass/fail assertions
- regression baseline
- summary of weak spots

What to learn by building:
- the system fails in patterns
- "good demos" hide brittleness
- small eval suites change design decisions quickly

Article hooks:
- evals are the bridge from intuition to engineering
- adversarial testing starts much earlier than red teaming

---

## Suggested Repo Structure For This Work

If you want this work to stay coherent, create a separate build repo or a dedicated workspace folder with a simple structure like:

```text
applied-ai-lab/
  AGENTS.md
  BOOTSTRAP.md
  BACKLOG.md
  journal/
  projects/
    01-schema-extractor/
    02-mini-rag/
    03-review-workflow/
    04-tool-contracts/
    05-observability/
    06-evals/
  shared/
    schemas/
    sample-docs/
    eval-fixtures/
    notes/
```

Keep each project small.
The purpose is repeated contact with core patterns, not a giant platform.

---

## Suggested Weekly Writing Habit

At the end of each week, write one short note with:
- what I thought would work
- what actually failed
- what became clearer
- what pattern now feels real instead of theoretical
- what article idea this unlocked

Keep it short and technical.

These weekly notes are likely to become better article seeds than trying to force polished essays too early.

---

## Reading And Reference Priority

Read for the build you are about to do, not for the whole field.

Priority order:
1. official standard/spec docs
2. official framework docs
3. source code examples
4. good practitioner writeups
5. papers when they directly inform the next build

Do not start with giant survey reading.

---

## What This Plan Should Produce By The End

By the end of six weeks, the goal is not mastery.
The goal is that you can truthfully say:

- I have built schema-first extraction workflows.
- I have built and evaluated a small retrieval system.
- I have implemented a stateful human-review workflow.
- I have exposed capabilities behind explicit tool contracts.
- I have instrumented an AI workflow with traces.
- I have run adversarial and regression-style evals against small systems.

That foundation is strong enough to:
- write more credible articles
- sharpen job positioning
- identify which deeper areas deserve sustained focus
- stop relying on instinct alone for the field's shared patterns

---

## Next Step After The Six Weeks

After this plan, choose one deeper lane for a 6 to 12 week follow-on:

- document intelligence and extraction
- workflow orchestration and human review systems
- evals and adversarial testing
- graph-backed retrieval and evidence systems
- standards-driven tool integration and protocol design

Do not deepen all lanes at once.
Pick the one where the small projects felt most alive and most strategically useful.
