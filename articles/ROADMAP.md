# Roadmap Checklist

Check items off as they are completed.
Run `/sync-roadmap` after checking items to reconcile with roadmap-dashboard.html.

Current rule:
- begin drafting articles now
- do not release any article until the six-week Applied AI engineering curriculum is complete
- use the curriculum to strengthen the article stack before publication

See:
- [../APPLIED_AI_ENGINEERING_LEARNING_PLAN.md](../APPLIED_AI_ENGINEERING_LEARNING_PLAN.md)

---

## Curriculum - Six-Week Release Gate

- [ ] C1 - `FastAPI Fundamentals`
- [ ] C2 - `Validate Data Classes with Pydantic`
- [ ] C3 - `Observability with OpenTelemetry and Grafana`
- [ ] C4 - `LangChain Development`
- [ ] C5 - `Retrieval Augmented Generation (RAG) for Developers`
- [ ] C6 - `Implementing Vector Search with LlamaIndex`
- [ ] C7 - `Introduction to LangGraph`
- [ ] C8 - `Model Context Protocol in Practice`

Release gate:
- no article publication before C1-C8 are complete
- drafting is allowed in parallel during weeks 1-6
- first release window opens after curriculum completion

---

## Articles - Draft In Parallel

- [ ] S1-A1 - Vibe Coding Is Gamified Work (Draft 4 ready; hold release until curriculum is complete)
- [ ] S1-A2 - AI Makes Bad Code Worse
- [ ] S1-A3 - Shipped More, Felt Worse
- [ ] S1-A4 - Documentation Fails
- [ ] S1-A5 - Vibe Coding Without Constraints
- [ ] S1-A6 - Context Poisoning
- [ ] S1-A9 - There Is No Such Thing as Clean Agentic Code
- [ ] S2-A1 - TDD Doesn't Work for Non-Deterministic Systems (And What Does)
- [ ] S2-A3 - Context Architecture Is the New Software Architecture
- [ ] S2-A4 - The Prompt Is a Contract
- [ ] S2-A7 - Token Frugality Is a Design Discipline
- [ ] S3-A1 - The MVP Is a One-Bet Strategy
- [ ] S3-A2 - Experimentation IS Requirements Gathering
- [ ] S3-A3 - Derive the Product from the Path of Least Resistance
- [ ] S4-A1 - Legal Systems Accumulate Tech Debt - the Analogy Is Exact
- [ ] S4-A2 - The Cost Is Measured
- [ ] S4-A3 - RAII Applied to Legal Obligations
- [ ] S4-A5 - The Gap Nobody Fills

---

## Articles - Release Order After Curriculum

- [ ] S1-A1 - target release wk 7
- [ ] S1-A2 - target release wk 9
- [ ] S1-A3 - target release wk 11
- [ ] S1-A4 - target release wk 13
- [ ] S1-A5 - target release wk 15
- [ ] S1-A6 - target release wk 17
- [ ] S1-A7 - target release wk 19
- [ ] S1-A8 - target release wk 21
- [ ] S1-A9 - target release wk 23
- [ ] S1-A10 - target release wk 25

---

## Articles - Read First

- [ ] S2-A2 - The V-Model Was Built for This Problem
  - B1 must be done first (4 papers, ~3-4 hrs)

---

## Articles - Build-Blocked

- [ ] S1-A7 - RAG as Engineering Memory <- needs B4/B5/B6
- [ ] S1-A8 - GraphRAG as Architectural Memory <- needs B4/B5/B6
- [ ] S1-A10 - The Architecture I'm Building <- needs B4/B5/B6/B7
- [ ] S2-A5 - Three Idiots Walk Into an Agentic System <- needs B8/B9
- [ ] S4-A4 - A Taxonomy of 87 Law Smells <- needs synthetic examples for all 87
- [ ] S4-A6 - How AI Agents Read Legal Text <- needs B4/B5/B6
- [ ] S4-A7 - The Filing That Fixes Itself <- needs B4/B5/B6

---

## Articles - Not Yet (experience-blocked)

- [ ] S2-A6 - LoRA and Behavioral Tuning as Engineering Discipline
  - Do not start. Needs 6+ months hands-on LoRA experience. Earliest: late 2026.

---

## Build Items

- [ ] B1 - Read 4 Agile-V papers (~3-4 hrs) -> unlocks S2-A2
  - Artifact: notes that separate artifact V&V, non-deterministic runtime behavior, and token-efficient regression testing into one synthesis for S2-A2.
  - Output expectation: read `2602.20684`, `2605.20456`, `2512.12791`, and `2603.02601`; capture the three-problem framing for article use.
- [ ] B2 - Sandbox 005 Stage 002 - manual pilot (1-2 weeks)
  - Artifact: documented Stage 2 evidence bundle for adversarial-agent behavior.
  - Output expectation: Stage 1 fully documented, extracted into its own repo, with methodology ADR and publishable notes.
- [ ] B3 - Synthetic demo dataset - design (1 day) -> unlocks B4
  - Artifact: dataset schema and coverage plan.
  - Output expectation: define document type, jurisdiction, date, target smell classes, RAII defect coverage, and ground-truth labels using synthetic-only source material.
- [ ] B4 - Synthetic demo dataset - build (~1 week) -> unlocks S1-A10, B5
  - Artifact: the actual synthetic document set the legal-tech-debt pipeline can run on.
  - Output expectation: enough believable synthetic policy material to demonstrate major smell categories without using real corpus text.
- [ ] B5 - Wire Claude API into legal-tech-debt pipeline (1-2 days) -> unlocks B6
  - Artifact: working classification step in the pipeline.
  - Output expectation: produce smell class, confidence, evidence quote, and RAII defect type where applicable.
- [ ] B6 - Deploy legal-tech-debt demo with public URL (2-3 days) -> hard target wk 4
  - Artifact: stable public demo URL.
  - Output expectation: accept a synthetic policy document and return typed defect findings with evidence; this is the concrete outreach artifact.
- [ ] B7 - Legal-tech-debt case study writeup (~1 week)
  - Artifact: case-study narrative tied to the demo.
  - Output expectation: explain what the pipeline detects, why the taxonomy matters, and what the worked example shows.
- [ ] B8 - Learn evals frameworks: DeepEval / Promptfoo (2-4 weeks) -> unlocks B9
  - Artifact: hands-on eval harness familiarity.
  - Output expectation: be able to define behavioral invariants, run repeated trials, and produce aggregate results rather than anecdotal observations.
- [ ] B9 - Granny's House Trials - Stage 2 (4-6 weeks) -> unlocks S2-A5
  - Artifact: publishable adversarial testing results section.
  - Output expectation: structured eval runs, hypothesis-testing posture, evidence bundles, and agent-profile comparisons.
- [ ] B10 - Personal site - 1-pager minimum (1-2 weeks) -> hard target wk 4
  - Artifact: live landing page for outreach.
  - Output expectation: demo link, writing link, and contact path; polish can come later.

---

## Build Artifact Detail

### B1 - Read 4 Agile-V papers

- Purpose: unblock S2-A2 with a stronger non-proprietary systems-engineering frame.
- Sources:
  - `2602.20684` - compliance-ready Agile-V framing
  - `2605.20456` - SCOPE-V loop and risk-adaptive evidence bundles
  - `2512.12791` - task completion is not correctness
  - `2603.02601` - token-efficient regression testing for non-deterministic workflows
- Article effect: gives S2-A2 the full three-layer argument instead of a single-paper summary.

### B2 - Sandbox 005 Stage 002 - manual pilot

- Purpose: continue internal adversarial-agent research without forcing premature publication.
- Needed first:
  - Stage 1 fully documented
  - own repo / clean project boundary
  - methodology ADR
- Output artifact: evidence bundle that can later support Stage 2 publication-grade claims.

### B3 - Synthetic demo dataset - design

- Purpose: define the legal-tech-debt demo before implementation drifts.
- Required schema:
  - document type
  - jurisdiction
  - date
  - intended smell class or classes
  - RAII defect coverage
  - ground-truth labels
- Constraint: synthetic examples only, never real policy text.

### B4 - Synthetic demo dataset - build

- Purpose: create the actual documents the pipeline can process.
- Quality bar:
  - covers major smell categories
  - supports the RAII defect classes
  - believable enough that a domain reader would not dismiss it instantly as fake
- Unlock effect: makes S1-A10 and the legal-tech-debt article track demonstrable rather than purely conceptual.

### B5 - Wire Claude API into legal-tech-debt pipeline

- Purpose: move from taxonomy-only work to a working AI-assisted diagnosis pipeline.
- Expected output fields:
  - smell class
  - confidence
  - evidence quote
  - RAII defect type when present
- Unlock effect: turns B6 into a real demo instead of a static mock.

### B6 - Deploy legal-tech-debt demo with public URL

- Purpose: create the outward-facing artifact that proves the concept exists.
- Minimum behavior:
  - takes synthetic policy text as input
  - returns typed findings with evidence
- Strategic effect:
  - unlocks S1-A10
  - gives the personal site and future outreach something real to point at

### B7 - Legal-tech-debt case study writeup

- Purpose: explain what the demo proves and what was learned.
- Should cover:
  - what the pipeline detects
  - what the 87-smell taxonomy means
  - why RAII defect classes matter
  - what the demo does and does not claim
- Strategic effect: strengthens S1-A10 and the Series 4 public argument.

### B8 - Learn evals frameworks: DeepEval / Promptfoo

- Purpose: build shared AI-engineering measurement discipline before stronger eval claims.
- Minimum capability:
  - define behavioral invariants
  - run N repeated evaluations
  - summarize aggregate outcomes against a rubric
- Strategic effect: gives S2-A5 a defensible measurement layer.

### B9 - Granny's House Trials - Stage 2

- Purpose: produce the empirical adversarial-testing article foundation.
- Needs:
  - B8 complete enough to use an eval harness
  - Stage 1 documented
  - evidence bundles and explicit constraints
- Output artifact: publishable results section for S2-A5.

### B10 - Personal site - 1-pager minimum

- Purpose: create the minimum live surface for demos, writing, and contact.
- Minimum content:
  - link to the legal-tech-debt demo
  - link to published writing
  - contact method
- Constraint: it does not need to be polished yet; it needs to be live.
