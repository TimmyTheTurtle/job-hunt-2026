# S2-A5 — Adversarial Agent Testing: Three Idiots in the Garden

**Status:** Not started — requires hands-on experimentation first

**Prerequisite:** Granny's House Trials Stage 2 + initial evals framework work

---

## Thesis

Static evals run fixed datasets against an LLM and measure aggregate statistics. That catches
known failure modes. It doesn't find the failure modes you didn't know to look for.

The complement is adversarial agent testing: agents with distinct behavioral personalities set
loose in a system with hidden infrastructure and constrained interventions, with the goal of
finding what breaks. Chaos engineering applied to AI systems — not killing servers to find
resilience gaps, but running behaviorally distinct agents to find semantic and behavioral gaps.

---

## Key Claims

- Static evals and adversarial agent testing are complementary, not competing methodologies
- Behavioral diversity in test agents surfaces failure modes that dataset-based evals miss
- The human-host/system-records-facts structure maps directly to human gate / evidence bundle
- Chaos engineering for AI systems requires agents, not just bad inputs

---

## The Three Idiots Format (Granny's House Trials)

Three agents with different behavioral personalities — the naive one who tries the obvious
solution badly, the aggressive one who pushes every boundary, the cautious one who finds edge
cases through excessive care — set loose in a domestic scenario (yard drainage, hidden hydraulic
infrastructure) with deterministic outcomes and hidden state.

The "three idiots in the garden" framing is presentation. The real payload:
- Hidden infrastructure the agents must discover
- Constrained interventions
- Deterministic outcomes (system records facts)
- Evidence left behind for review
- The host judges meaning; the system records facts

The host/judge separation is the human gate / evidence bundle pattern instantiated as a playable
format.

---

## Connection to Eval Frameworks

- Tools like DeepEval and Promptfoo handle the assertion layer (known failure modes)
- The three-idiots format handles the adversarial exploration layer (unknown failure modes)
- Together they constitute a complete non-deterministic system test methodology

---

## Sources

- [Beyond Traditional Testing: Non-Deterministic Software — AWS/dev.to](https://dev.to/aws/beyond-traditional-testing-addressing-the-challenges-of-non-deterministic-software-583a)
- [Testing AI Agents: Validating Non-Deterministic Behavior — SitePoint](https://www.sitepoint.com/testing-ai-agents-deterministic-evaluation-in-a-non-deterministic-world/)
- [Agentic AI Content Verification — Quality Gates (Pebblous)](https://blog.pebblous.ai/blog/agentic-content-pipeline-verification/en/)
- Granny's House Trials repo (internal):
  `C:\Users\DorianKlingenberg\OneDrive - RenoNerd Inc\2026-projects\grannies-house-trials`
