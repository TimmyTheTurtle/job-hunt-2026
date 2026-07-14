# AI Engineering Enablement Portfolio Prospects

Status: Prospect list for future portfolio builds
Purpose: Capture portfolio project ideas that align with AI engineering enablement roles such as AI Senior Engineer, developer productivity, internal AI tooling, and applied AI workflow architecture.

## Why These Prospects Exist

These are not generic AI demos. They are candidate portfolio builds meant to prove:

- practical AI adoption judgment,
- measurable engineering productivity thinking,
- code quality and workflow discipline,
- human-review and safety boundaries,
- cost-awareness,
- and the ability to integrate AI into real engineering systems instead of treating it as a novelty layer.

They are especially useful for roles that ask for:

- AI tooling rollout,
- developer enablement,
- coding/test/documentation workflow improvement,
- KPI and ROI measurement,
- and technical guidance for customer-facing AI integration.

## Selection Rules

Each prospect should aim for:

- a deployable demo surface,
- GitHub-centric or repo-centric workflow integration,
- typed outputs instead of pure freeform prose,
- evidence or provenance where relevant,
- an explicit evaluation path,
- and a clear story for how a team would trust or adopt it.

Each should also provide space to exercise one of two process/architecture disciplines:

- `Agile-V` when the project benefits from explicit verification layers, evidence bundles, staged rollout, and risk-based controls
- `SwarmForge` when the project benefits from multiple bounded agents with clearly separated responsibilities

## Priority Prospect List

### 1. AI Pull Request Review Gate

**Core idea**

Build a GitHub-integrated assistant that analyzes pull requests for risk, test gaps, architecture drift, and documentation impact, then produces a structured review report.

**Why it aligns**

- Direct fit for "improve code quality"
- Strong internal AI adoption and developer workflow story
- Easy to explain in terms of team use and measurable benefit

**Good demo shape**

- ingest PR diff plus selected repository context
- run review passes for risk, tests, docs, and architectural concerns
- emit typed findings with severity, evidence, and suggested next action
- allow human accept/reject/acknowledge review states
- show audit trail for what the assistant flagged and what the reviewer decided

**Agile-V angle**

- define review contracts per repository type
- verify findings on seeded PR cases
- track false positive and false negative rates
- produce evidence bundles for rollout decisions

**SwarmForge angle**

- one agent for code-risk review
- one agent for test impact
- one agent for documentation and ADR impact
- one synthesis agent for final structured recommendation

**Best signal**

Demonstrates that AI can be inserted into a real engineering checkpoint with bounded outputs and measurable value.

### 2. Engineering Knowledge Retrieval Copilot

**Core idea**

Build a RAG-based engineering memory tool over ADRs, runbooks, architecture notes, repo docs, handoffs, and incident notes, optimized for source-backed answers.

**Why it aligns**

- Directly supports engineering productivity and onboarding
- Connects strongly to the articles and context-architecture work
- Shows practical AI use beyond code generation

**Good demo shape**

- index ADRs, docs, runbooks, and selected repo artifacts
- answer engineering questions with citations and provenance
- expose stale/conflicting-source warnings
- allow document freshness checks and source scoring
- show the exact supporting snippets behind each answer

**Agile-V angle**

- verify retrieval grounding and citation accuracy
- define "answer must cite source" as a gate
- evaluate stale-context failure modes

**SwarmForge angle**

- retrieval agent
- citation validation agent
- freshness/conflict agent
- answer composition agent

**Best signal**

Demonstrates AI-assisted documentation and engineering memory with discipline, not hallucinated convenience.

### 3. AI Experimentation and ROI Dashboard

**Core idea**

Build an internal platform for evaluating AI tooling experiments across coding, testing, documentation, and support workflows with KPI tracking and cost analysis.

**Why it aligns**

- Closest direct match to AI enablement roles
- Shows practical rollout, measurement, and cost governance
- Creates a credible "trusted internal AI guide" story

**Good demo shape**

- define an experiment with workflow, model/tool choice, and success criteria
- track cycle time, defect rate proxies, review latency, usage, and token spend
- compare baseline workflow vs AI-assisted workflow
- generate a go/no-go or expand/pause recommendation
- preserve decision history and evidence snapshots

**Agile-V angle**

- ideal for stage gates, evidence bundles, and risk-tiered adoption
- treat each pilot as a controlled engineering change
- document validation criteria before rollout

**SwarmForge angle**

- experiment-design agent
- KPI-analysis agent
- cost-analysis agent
- recommendation agent

**Best signal**

Demonstrates the exact combination of AI adoption, ROI discipline, and engineering judgment many internal AI roles want.

### 4. Contract Testing Harness for Constrained LLM Nodes

**Core idea**

Build a reusable framework for schema-bound LLM components with contract tests, replay fixtures, adversarial cases, and periodic eval runs.

**Why it aligns**

- Shows serious AI systems engineering rather than prompt tinkering
- Maps directly to quality gates and safe product integration
- Reinforces the testing and constrained-node ideas already present in article work

**Good demo shape**

- support extraction, classification, summarization, and routing nodes
- define schemas and business invariants
- run deterministic contract tests in CI
- run periodic statistical evals separately
- report regressions by node, prompt, and schema revision

**Agile-V angle**

- extremely natural fit for specify/constrain/prove/verify discipline
- clear separation between deterministic checks and probabilistic evals

**SwarmForge angle**

- test-case generation agent
- adversarial-case agent
- replay-analysis agent
- eval-summary agent

**Best signal**

Demonstrates production-minded AI quality discipline that most "AI tool users" do not have.

### 5. AI Runbook Assistant for Production Operations

**Core idea**

Build an operations assistant that reads runbooks, deployment notes, logs, and incident procedures, then recommends next steps through guarded, approval-based flows.

**Why it aligns**

- Shows AI in real engineering operations
- Demonstrates trust, safety, and human-in-the-loop workflow design
- Connects well to practical enablement rather than novelty demos

**Good demo shape**

- ingest incident context, runbooks, and deployment notes
- assemble a proposed response path with citations
- distinguish read-only guidance from action-taking suggestions
- require explicit approval for sensitive steps
- record audit events for recommendations, approvals, and outcomes

**Agile-V angle**

- define safe vs unsafe action classes
- verify escalation and refusal behavior
- require evidence for operational recommendations

**SwarmForge angle**

- incident-context agent
- runbook retrieval agent
- safety-policy agent
- operator-summary agent

**Best signal**

Demonstrates AI assistance that respects operational boundaries and earns trust under pressure.

## Recommended Build Order

If only two should be built first:

1. `AI Experimentation and ROI Dashboard`
2. `AI Pull Request Review Gate`

Why:

- together they most clearly support an AI engineering enablement narrative
- they create a strong story around adoption, measurement, quality, and team workflow improvement
- they are easier to tie directly to the target role than broader research-heavy builds

Second wave:

3. `Engineering Knowledge Retrieval Copilot`
4. `Contract Testing Harness for Constrained LLM Nodes`
5. `AI Runbook Assistant for Production Operations`

## Shared Production-Aligned Requirements

All five should try to include:

- deployable demo path
- synthetic or demo-safe data by default
- clear user or workspace boundary where applicable
- structured outputs and audit trail
- observability for latency, failures, and cost
- human review or approval gates where the workflow is high impact
- before/after or baseline/AI-assisted measurement
- ADRs explaining architecture and process choices

## Positioning Value

As a group, these prospects would help position Dorian as:

> A systems-oriented software engineer who can help engineering teams adopt AI responsibly, measure what works, and build workflow boundaries that improve quality instead of just increasing activity.

That is more credible for internal AI enablement roles than a portfolio made mostly of chatbots, wrappers, or generic consumer AI demos.
