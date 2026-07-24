# S2-A2 — The V-Model Was Built for This Problem

**Status:** Blocked — read arXiv:2602.20684 and arXiv:2605.20456 before writing (est. 3–4 hrs total)

---

## Thesis

The V-model predates LLMs by decades. It was developed for aerospace and medical devices —
systems where behavior can't be fully specified before implementation, requirements are expressed
in natural language with interpretive ambiguity, and failure modes require human judgment to
evaluate. LLM systems share all three properties. This isn't a coincidence. It's structural.

Series 2 should now make one thing explicit: **evaluation-driven development** is the task-level
development loop for probabilistic behavior, while the V-model / Agile-V is the lifecycle
structure that tells teams where evaluation evidence belongs, how it rolls up, and where human
approval gates sit.

But the V-model needs adaptation at two layers that the existing Agile-V literature does not
fully address: (1) evaluating agent-generated artifacts, where the output can be tested
deterministically even if the generation was not; and (2) evaluating the agentic system itself
as a non-deterministic runtime, where the *system under test* takes different execution paths
on every run. These are structurally different problems and they require different V&V
machinery.

---

## The Three-Problem Distinction — Central to the Article

This is the key structural insight the article must establish clearly. All three problems exist
in real AI systems. They require different testing machinery. Conflating them produces frameworks
that are well-designed for one and useless for the others.

**Problem 1 — V&V of deterministic software** (original V-model domain)
Same input, same output. Classical hierarchy: unit → integration → system. Fully solved.
AI-assisted development still produces deterministic code; this problem doesn't change.

**Problem 2 — V&V of agent-generated artifacts**
An AI agent generates code, documentation, or designs. The *generation* is non-deterministic
but the *artifact* can be deterministic. You can test the generated code the same way you'd
test any code. The Agile-V framework (arXiv:2602.20684, Koch & Wellbrock 2026) addresses
this well: human approval gates, compliance traceability, audit-ready artifacts as a byproduct.
Limitation: a single 500-line feasibility study; generalizability unproven.

**Problem 3 — V&V of the agentic system itself as a non-deterministic runtime**
The *system under test* makes autonomous decisions, calls tools, takes different execution
paths on every run, and produces outputs that are samples from a probability distribution.
Traditional V&V collapses: you cannot write a test that expects a specific output. A 3%
failure rate might be noise or a real regression — you cannot tell from a single run.
This is the hard unsolved problem. The article must name it and propose the adaptation.

---

## Key Claims

- The V-model's *structure* — decomposition, hierarchical testing, explicit V&V gates — is
  exactly right for agentic systems; its *acceptance criteria* are wrong
- Evaluation-driven development supplies the micro-loop; the V-model supplies the macro-lifecycle
- Verification (building the system right) is partially automatable for agentic systems
  via behavioral invariants + statistical sampling
- Validation (building the right system) requires human judgment — always, at every risk level
- Sprint-based TDD workflows don't map onto LLM component development (S2-A1)
- Eval-driven development does map onto LLM component development, but it needs to be placed
  inside a larger lifecycle and governance structure
- The V-model's decomposition-then-integration structure, with explicit V&V gates, does map —
  but only if acceptance criteria shift from expected outputs to behavioral invariants +
  probabilistic confidence bounds
- Empirical proof that outcome testing is insufficient: one evaluation scenario achieved 100%
  task completion and only 33% policy adherence (arXiv:2512.12791)

---

## The Adaptation: What Changes at Each Level

### Replace expected outputs with two-tier acceptance criteria

**Hard invariants** (pass/fail, non-negotiable regardless of non-determinism):
- Schema compliance: output is structurally valid
- Safety properties: no harmful content, no unauthorized state mutations
- Monotonic side-effect rules: idempotent where required
- Response time bounds

**Probabilistic assertions** (statistical, not boolean):
- "This behavioral criterion holds ≥ 95% of the time across the test distribution"
- "Mean task completion rate has not dropped by more than 3pp vs. baseline with p < 0.05"
- Sequential hypothesis testing to determine minimum runs needed (AgentAssay, arXiv:2603.02601)

### Replace naive unit-test thinking with eval-driven evidence at each level

At every level of the V (component, integration, system): run N iterations, produce aggregate
statistics, interpret against the acceptance distribution — not a single pass/fail result.
The number of runs required can be minimized with sequential hypothesis testing.

### Add trajectory evaluation at integration and system levels

The test artifact is the agent's full decision path, not just the terminal output. Behavioral
invariants — diagnostic-before-action, policy consultation patterns, tool sequencing — must
be tested across the trajectory, not inferred from the final result.

### Preserve human gates at the original V-model positions — make them risk-adaptive

The Agentic Agile-V SCOPE-V loop (arXiv:2605.20456) provides the best current treatment
of risk-adaptive gates:
- R0 (exploratory): smoke test or manual run; optional review
- R1 (routine): targeted tests, lint, normal review
- R2 (production): CI, static analysis, regression, mandatory approval
- R3 (high assurance): traceable requirements, independent tests, formal/simulation/HIL
  evidence, explicit sign-off

### Add a continuous monitoring layer below deployment

The original V-model ends at deployment. Agentic systems require a post-deployment monitoring
layer as a first-class V&V layer — not an operational concern but a verification concern.
Statistical drift in behavioral metrics is the signal; it requires the same interpretation
infrastructure as pre-deployment evals.

---

## The SCOPE-V Loop (Agentic Agile-V, arXiv:2605.20456)

At the task level inside a sprint, SCOPE-V structures each agentic work unit:

| Stage | Purpose |
|---|---|
| **Specify** | Convert intent to structured task brief: objectives, scope, non-goals, affected modules, acceptance criteria |
| **Constrain** | Establish boundaries: which files can change, which dependencies are allowed, what must be preserved |
| **Orchestrate** | Define agent workflow: inspect first, design summary, plan, implement incrementally, verify locally, document risk |
| **Prove** | Collect evidence appropriate to risk level (R0–R3) |
| **Evolve** | Feed validated learning back into baselines; remove obsolete guidance |
| **Verify** | Recurring: pre-implementation, during, pre-merge CI, post-deployment monitoring |

Core principle: *"Agent output is not accepted because it is plausible; it is accepted because
it satisfies evidence appropriate to its risk level."*

---

## Connection to Granny's House Trials (S2-A5)

The Granny's House Trials adversarial testing experiment is the empirical demonstration of
this entire framework. Three agents with different behavioral profiles run in the same
environment. The evidence bundles are the test artifacts. The behavioral invariants
(what Granny's system should never allow regardless of agent personality) are the hard
constraints. The agent-specific behavioral variation is the probabilistic layer.

When writing S2-A2, note explicitly that S2-A5 is the worked example. The V-model adaptation
proposed here is the theory; Granny's is the experiment that validates or falsifies it.

---

## Attribution — IMPORTANT

**"Agile V"** is not original to this work. Source: Koch & Wellbrock,
*Agile V: A Compliance-Ready Framework for AI-Augmented Engineering*, arXiv:2602.20684, 2026.

**"Agentic Agile-V"** and **SCOPE-V** are not original to this work. Source:
arXiv:2605.20456, 2026.

**The three-problem distinction** and the **layered V-model adaptation** (behavioral
invariants + statistical sampling + trajectory evaluation + continuous monitoring) are
the original contributions of this article, synthesizing from those papers plus
arXiv:2512.12791 and arXiv:2603.02601.

Before publishing: read both Agile-V papers in full. State clearly where the synthesis begins
and what problem each source does and does not address.

---

## Sources

**Primary — the Agile-V lineage:**
- Koch & Wellbrock. "Agile V: A Compliance-Ready Framework for AI-Augmented Engineering."
  arXiv:2602.20684, Feb 2026. *The source framework. Addresses Problem 2 well. Does not
  address Problem 3.*
- arXiv:2605.20456, May 2026. "Agentic Agile-V: From Vibe Coding to Verified Engineering
  in Software and Hardware Development." *SCOPE-V loop; risk-adaptive evidence bundles;
  addresses Problem 3 at the task/process level but not the statistical testing level.*

**Primary — agentic system evaluation:**
- arXiv:2512.12791. "Beyond Task Completion: An Assessment Framework for Evaluating Agentic
  AI Systems." 2025. *Four-pillar model (LLMs, Memory, Tools, Environment). Empirical proof
  that 100% task completion ≠ correct behavior (33% policy adherence in same scenario).
  Behavioral invariant testing.*
- arXiv:2603.02601. "AgentAssay: Token-Efficient Regression Testing for Non-Deterministic
  AI Agent Workflows." 2026. *Sequential hypothesis testing for probabilistic behavioral
  guarantees. Hard invariants vs. probabilistic assertions. Minimum-runs methodology.*

**V-model foundations and adaptations:**
- arXiv:2308.05381. "Exploratory Study of V-Model in ML-Enabled Software." 2023.
  *Empirical study of V-model application to ML; identifies offline/online testing gap.*
- IEEE 10207641. "Proposed V-Model for AI Verification and Validation." 2023.
- SEBoK. "Verification and Validation of Systems in Which AI is a Key Element."
  https://sebokwiki.org/wiki/Verification_and_Validation_of_Systems_in_Which_AI_is_a_Key_Element
- arXiv:2411.09050. "The Systems Engineering Approach in Times of LLMs." 2024.

**Practice-side context:**
- [Model-Based Testing of Non-Deterministic Systems (PDF)](https://marcfrappierudes.github.io/Papers/Model_Based_Testing_of_Non_Deterministic_Systems.pdf)
- [AI Systems Engineering: rescuing AI from the valley of death — OpenChain](https://openchainproject.org/news/2026/03/26/ai-systems-engineering-the-new-discipline-to-rescue-ai-from-the-valley-of-death)
- [Model-Based Systems Engineering and Agentic AI — MathWorks](https://blogs.mathworks.com/simulink/2026/04/26/model-based-systems-engineering-and-agentic-ai/)
