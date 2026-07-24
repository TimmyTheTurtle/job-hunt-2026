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
replacement methodology is **evaluation-driven development**: deterministic contract checks where
the boundary permits them, eval suites where behavior is probabilistic, and human interpretation
where meaning and acceptance cannot be reduced to a score. LLM-as-judge is triage, not
verification.

## Eval-Driven Development Frame

The article should name this directly. What replaces classical TDD for non-deterministic LLM
behavior is not "just evals" in the abstract, but **evaluation-driven development (EDD)**:
define what good looks like, encode it as runnable checks, and use those checks to drive system
changes instead of shipping on vibes.

But the article should also sharpen the term:

- **EDD is the dominant methodology for probabilistic behavior**
- **Contract testing remains valid for constrained nodes**
- **Human gates remain necessary for acceptance, governance, and business meaning**

That gives the series a cleaner stack:
- S2-A1: EDD as the replacement for naive TDD at stochastic boundaries
- S2-A2: V-model / Agile-V as the lifecycle structure around EDD
- S2-A8: contract testing as the deterministic inner layer inside EDD

---

## Key Insight — Constraint Architecture and Contract Testing (Session note 2026-06-16)

The thesis as written assumes all LLM calls are non-deterministic and therefore TDD-incompatible.
That is too broad. A tightly constrained LLM call — fixed system prompt, schema-bound output,
narrow task scope — admits *property-based contract testing*, and the red-green-refactor loop
is intact at the contract level.

**What the literature establishes:**

AgentAssay (arXiv:2603.02601) explicitly rejects classical TDD for agents and proposes
stochastic test semantics with confidence intervals. LMQL (arXiv:2212.06094) demonstrates
that grammar-constrained decoding reduces output variance substantially — 15-25 pp improvement
on structured tasks — without eliminating it. Record & Replay (arXiv:2505.17716) frames
constrained workflow + check functions as addressing "inherent uncertainty," with a validation
layer still required. None of these papers claim full determinism from constraints.

**The gap the literature has not filled:**

The field knows that schema constraints reduce variance. It knows that schema validation is a
deterministic check. It has not connected these observations and said: the *testable unit* is
the contract — schema conformance + business logic invariant — and that contract can be written
as a failing assertion before the node is built. That is the red-green loop, applied to the
contract rather than to the output string.

**The precise claim (not "pure function", not classical TDD):**

A schema-bound LLM node with fixed prompt and narrow scope is testable via *property-based
contract assertions*. The property is: "output satisfies schema AND satisfies business logic
invariant." That is weaker than "same input, same output," but it is enough to run
red-green-refactor. Write the failing contract assertion first, build the node to satisfy it.

This is the correct scope boundary:

- **Constrained LLM nodes** (schema-bound, narrow task, fixed prompt): property-based contract
  testing applies. The assertion is the schema + invariant. PydanticAI TestModel and
  FunctionModel are the practical tools. These are the edge nodes in a well-designed agentic
  system. See S2-A8 for the full treatment.
- **Orchestration layer** (sequences constrained calls, routes between them, manages state):
  classical TDD breaks here. This is where evals, invariants, and terminal conditions replace
  the red-green-refactor loop.

**Three testing layers that follow from this:**

1. **Constrained LLM nodes**: property-based contract testing. Assertion = schema + invariant.
   Cheap, fast, run on every commit. Tools: PydanticAI TestModel/FunctionModel, Pydantic
   schema validation, pytest assertions against output contracts.
2. **Orchestration invariants**: things that must be true regardless of trajectory — no
   out-of-scope side effects, schema-valid outputs at every tool boundary, timing and resource
   constraints. Specified before implementation (V-model left side), verified at runtime.
3. **Statistical evals**: aggregate metrics over the orchestration layer's behavior across
   many runs. Human reads the dashboard. Periodic, not continuous.

**Connection to AgentAssay (arXiv:2603.02601):** Sequential hypothesis testing applies at
layer 3 — reach statistical confidence with the minimum number of eval runs.

**Connection to S2-A7:** The constraint decision is architectural. A system designed with
constrained nodes is simultaneously token-frugal and contract-testable. Same design decision,
two angles.

**Connection to S2-A8:** This article names the three layers and sets the scope boundary.
S2-A8 develops the contract testing methodology for constrained nodes fully.

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
- Evaluation-driven development is the appropriate methodology: deterministic contracts where
  possible, aggregate evals where behavior is stochastic
- LLM-as-judge reduces human review volume but cannot verify — same non-determinism problem,
  plus correlation bias
- You can automate the running of evals; you cannot automate the interpretation

---

## Main Points to Discuss

- The three TDD assumptions and how each fails for LLM systems
- Eval-driven development as the replacement frame: check first, build against the check,
  measure regressions before shipping
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
- [What is eval-driven development? — Braintrust](https://www.braintrust.dev/articles/eval-driven-development)
- [Should I practice eval-driven development? — Hamel Husain / Shreya Shankar](https://hamel.dev/blog/posts/evals-faq/should-i-practice-eval-driven-development.html)
- [LLM testing frameworks and tools — TestOmat](https://testomat.io/blog/llm-test/)
- [Beyond Traditional Testing: Non-Deterministic Software — AWS/dev.to](https://dev.to/aws/beyond-traditional-testing-addressing-the-challenges-of-non-deterministic-software-583a)
- [Testing AI Agents: Validating Non-Deterministic Behavior — SitePoint](https://www.sitepoint.com/testing-ai-agents-deterministic-evaluation-in-a-non-deterministic-world/)
- [AgentAssay: Token-Efficient Regression Testing (arXiv:2603.02601)](../papers/arxiv-2603.02601-agentassay.pdf) — establishes stochastic test semantics; basis for layer 3
- [LMQL: Prompting Is Programming (arXiv:2212.06094)](../papers/arxiv-2212.06094-lmql-prompting-is-programming.pdf) — grammar-constrained decoding reduces output variance; evidence for constraint value
- [Record & Replay for LLM Agents (arXiv:2505.17716)](../papers/arxiv-2505.17716-record-replay-llm-agents.pdf) — check functions as trust anchors on constrained workflows
- [Automated Self-Testing as Quality Gate (arXiv:2603.15676)](../papers/arxiv-2603.15676-automated-self-testing-quality-gate.pdf) — schema checks as deterministic gates alongside probabilistic evaluators
