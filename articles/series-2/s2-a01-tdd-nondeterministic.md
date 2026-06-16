# S2-A1 — TDD Doesn't Work for Non-Deterministic Systems (And What Does)

**Status:** Not started

---

## Voice and Tone

- **Register:** technical and direct. Series 2 is a step up in assumed reader sophistication —
  this audience knows TDD. Don't explain it; build on it. The argument is "here is where the
  familiar thing breaks and here is what replaces it."
- **The title makes a bold claim. Earn it without hedging it to death.** "TDD doesn't work"
  is the thesis. The nuance is in why and what does work instead — not in retreating to
  "well, it depends." Make the case.
- **First person only where you have operated evals yourself.** The article can be largely
  in analytical voice. Personal experience earns its place when describing what it actually
  feels like to see an 8-point accuracy drop and have no red test to point at.
- **LLM-as-judge:** treat it with precision, not dismissal. It reduces review volume — that
  is real. It cannot verify — that is also real. Both are true simultaneously.
- **Do not make this a methodology pitch.** The argument is structural. Evals aren't "better"
  than TDD in the sense of being superior engineering discipline — they are the appropriate
  tool for a different class of system. Make that distinction clearly.

---

## Thesis

TDD rests on three assumptions LLM systems violate: determinism (same input always produces
same output), binary correctness (pass or fail), and fast cheap feedback (seconds, free). The
replacement methodology is evals. LLM-as-judge is triage, not verification.

---

## Key Insight — Constraint Architecture Restores TDD (Session note 2026-06-16)

The thesis as written assumes all LLM calls are non-deterministic and therefore TDD-incompatible.
That is too broad. A tightly constrained LLM call — fixed system prompt, schema-bound output,
narrow task scope, deterministic inputs — is effectively a pure function from the test's
perspective. Classical TDD applies cleanly to it.

**The constraint architecture collapses two problems into one solution:**

1. Token frugality (S2-A7): constrained calls are cheap
2. Testability: constrained calls are deterministic enough for classical assertions

This means the article's scope boundary needs to be more precise. The claim is not "TDD doesn't
work for LLM systems." It is:

- **Constrained LLM nodes** (schema-bound, narrow task, fixed prompt): TDD applies. Write
  the failing schema assertion and business logic assertion first, then build the call to
  satisfy it. These are the edge nodes in a well-designed agentic system.
- **Orchestration layer** (sequences constrained calls, routes between them, manages state):
  TDD breaks here. This is where evals, invariants, and terminal conditions replace the
  red-green-refactor loop.

**The architecture does the work.** Pushing non-determinism up to the orchestration layer —
and keeping every node below it constrained and deterministic — is not just a token decision.
It is what makes TDD viable for the parts of the system where TDD is the right tool.

**Three testing layers that follow from this:**

1. **Constrained LLM nodes**: classical TDD, deterministic assertions, cheap, run on every
   execution. Schema validation, output contract checks, business logic assertions.
2. **Orchestration invariants**: things that must be true regardless of trajectory — no
   out-of-scope side effects, schema-valid outputs at every tool boundary, timing and resource
   constraints. Specified before implementation (V-model left side), verified at runtime.
3. **Statistical evals**: aggregate metrics over the orchestration layer's behavior across
   many runs. Human reads the dashboard. Periodic, not continuous.

**Human-in-the-loop is structural, not compensatory.** It belongs at specific V&V gates —
novel failure modes, out-of-distribution cases, high-stakes decisions. The constraint
architecture clarifies where human judgment is irreplaceable rather than using it as a
fallback for weak evals.

**Connection to AgentAssay (arXiv:2603.02601):** Sequential hypothesis testing applies at
layer 3 — reach statistical confidence with the minimum number of eval runs. Token frugality
at the eval layer, not just the system-under-test layer.

**Connection to S2-A7:** The constraint decision is architectural. A system designed with
constrained nodes is simultaneously token-frugal and TDD-compatible. These are not separate
concerns — they are the same design decision observed from two different angles.

**This is an original claim.** The literature treats TDD-incompatibility as a property of
LLM systems in general. The constraint architecture argument — that you can recover TDD
compatibility by design — is not in the existing sources. It should be the article's new
central claim, with the evals methodology as the answer for the orchestration layer that
remains genuinely non-deterministic.

---

## Scope Boundary — Important

This article covers **single-turn LLM evaluation**: evaluating the outputs a language model
produces in response to a prompt. Evals, G-Eval, LLM-as-judge, aggregate statistics.

It does **not** cover **agentic system testing** — verification and validation of a system
that autonomously makes decisions, calls tools, and produces non-deterministic *behavior
trajectories*, not just non-deterministic outputs. That is a structurally different problem
and is the subject of S2-A2.

The boundary: if you can evaluate one model response at a time against a rubric, that's
S2-A1 territory. If the system under test takes sequences of actions across multiple turns
and tool calls, and you need to test the decision path not just the terminal output, that
is S2-A2 territory.

---

## Key Claims

- TDD's red-green-refactor loop requires deterministic outputs — LLM systems are stochastic
- "Correctness" for LLM outputs is a distribution over a rubric, not a boolean
- Evals are the appropriate methodology: aggregate statistics over labeled datasets
- LLM-as-judge reduces human review volume but cannot verify — same non-determinism problem,
  plus correlation bias
- You can automate the running of evals; you cannot automate the interpretation

---

## Main Points to Discuss

- The three TDD assumptions and how each fails for LLM systems
- What evals are: structured evaluation runs against curated datasets with human-labeled
  ground truth, producing aggregate statistics
- A drop from 87% to 79% accuracy is a signal requiring human interpretation — not a failed
  test requiring a code fix
- The G-Eval framework: chain-of-thought evaluation, limit to 3-5 criteria, integer scales
- LLM-as-judge: useful for triage at scale (100k outputs in hours vs. 52 days human review),
  but bounded by correlation bias and hallucination
- The human gate is non-optional — it is not a fallback for uncertainty, it is the only
  mechanism that can validate against real-world requirements

---

## Sources

- [LLM as a Judge: guide and best practices — Agenta](https://agenta.ai/blog/llm-as-a-judge-guide-to-llm-evaluation-best-practices)
- [LLMs-as-Judges: comprehensive survey (ArXiv)](../papers/arxiv-2412.05579-llms-as-judges-survey.pdf)
- [LLM judge cookbook — Hugging Face](https://huggingface.co/learn/cookbook/en/llm_judge)
- [Beyond vibe checks: complete guide to evals — Lenny's Newsletter](https://www.lennysnewsletter.com/p/beyond-vibe-checks-a-pms-complete)
- [A pragmatic guide to LLM evals — Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/evals)
- [LLM testing frameworks and tools — TestOmat](https://testomat.io/blog/llm-test/)
- [Beyond Traditional Testing: Non-Deterministic Software — AWS/dev.to](https://dev.to/aws/beyond-traditional-testing-addressing-the-challenges-of-non-deterministic-software-583a)
- [Testing AI Agents: Validating Non-Deterministic Behavior — SitePoint](https://www.sitepoint.com/testing-ai-agents-deterministic-evaluation-in-a-non-deterministic-world/)
