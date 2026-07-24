# S2-A3 — Context Architecture Is the New Software Architecture

**Status:** Not started

---

## Voice and Tone

- **Register:** serious and architectural. This is the article that argues context architecture
  is a real discipline with a real name. The tone should match that ambition — precise,
  grounded, not breathless.
- **"Not metaphorically, but operationally"** is the hinge phrase in the thesis. Write toward
  it. The whole article's credibility rests on making that distinction stick.
- **Draw on information architecture and knowledge management traditions without being
  academic about it.** These are real fields with real vocabulary. Use the vocabulary without
  explaining it at length — this audience can keep up.
- **The tiered memory model (Canonical / Reference / Scratch) should feel discovered,
  not announced.** Build to it through the argument before naming it.
- **First person where the context architecture decisions were made in real systems** —
  legal-tech-debt, Watershed, Granny's House. These are concrete. Use them.
- **The token economics note (cross-ref S2-A7) should land as a consequence**, not a detour.
  "Archive broadly, retrieve narrowly is a cost principle" — one sentence, no expansion needed
  in this article.

---

## Thesis

If the agent is a mirror of its context, then the design of the context is the design of the
system. Context architecture is the new software architecture — not metaphorically, but
operationally. What artifacts exist for the agent to retrieve, how they are structured, where
human gates are placed, how context poisoning is prevented across sessions — these are
first-class engineering decisions.

In the Series 2 frame, this article should also say plainly: context architecture is the
substrate on which evaluation-driven development runs. If the system cannot retrieve the right
contracts, rubrics, ADRs, and evidence artifacts at the right time, the eval loop itself becomes
noisy and untrustworthy.

---

## Key Claims

- Context architecture is a discipline, not a metaphor
- Good eval-driven development depends on retrievable contracts, rubrics, and evidence context
- It draws from information architecture, knowledge management, and safety-critical documentation
- What's new is that these disciplines now have direct operational impact on software quality
- The implicit knowledge senior engineers carry must be materialized as retrievable artifacts

---

## Artifact Types

- Task contracts — explicit scope and boundaries for an agent session
- Experiment requirement candidates — hypotheses before implementation
- Evidence bundles — outputs with provenance
- V&V evidence — verification and validation records
- Risk registers
- Architecture decision records structured for retrieval

## Tiered Memory Model

- **Canonical** — current truth: active architecture, active ADRs, current glossary
- **Reference** — useful but not primary: superseded ADRs, archived handoffs
- **Scratch** — exploratory: journals, half-baked reflections, AI-generated summaries

Rule: archive broadly, retrieve narrowly.

Token economics note (cross-reference S2-A7): the canonical/reference/scratch tiering model
is a frugality architecture as much as a quality architecture. Every token in the context
window costs money on every call. "Archive broadly, retrieve narrowly" is a cost principle.
Name this explicitly in the article — the same discipline solves two problems.

---

## Sources

- [Agentic Software Engineering: Foundational Pillars (ArXiv)](../papers/arxiv-2509.06216-agentic-se-foundational-pillars.pdf)
- [AI-Infused Development Needs More Than Prompts — O'Reilly](https://www.oreilly.com/radar/ai-infused-development-needs-more-than-prompts/)
- [Agentic AI Content Verification — Quality Gates (Pebblous)](https://blog.pebblous.ai/blog/agentic-content-pipeline-verification/en/)
- [Why Your AI Agent Needs a Quality Gate — dev.to](https://dev.to/yurukusa/why-your-ai-agent-needs-a-quality-gate-not-just-tests-42eo)
- [AI Agent Governance — Policy and Compliance 2026](https://www.digitalapplied.com/blog/ai-agent-governance-policy-compliance-2026)
