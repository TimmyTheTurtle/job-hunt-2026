# S1-A10 — The Architecture I'm Building

**Status:** Not started
**Series position:** 10 of 10 — the closing argument

---

## Thesis

Everything prior was diagnosis and theory. This article is the system. Agile V (ArXiv 2602.20684)
is the published V-model framework for AI-augmented development this work builds on. Sandbox 005
is the working implementation, extended specifically to handle non-deterministic LLM outputs.
The document intelligence pipeline (Ingest → Model → Detect → Triage → Report → Govern) is a
concrete instance of the architecture running on real data.

The call to action lives here: a quiet paragraph at the end. Not a pitch — a door.

---

## Key Claims

- The architecture described in this series exists and is running
- It is domain-agnostic — legal/compliance is the first experiment, not the definition
- The SE discipline (explicit boundaries, human gates, evidence trails) is the differentiator,
  not the AI components
- Agile V as governance spine, RAG + GraphRAG as memory, guardrails and hooks as enforcement

---

## Full Architecture Stack

- **Agile V** — governance and verification structure (cite: ArXiv 2602.20684)
- **SwarmForge-style orchestration** — multiple specialized agents in disciplined coordination
- **Curated SE/SW engineering knowledge** — reusable context repository
- **RAG** — retrieve only relevant pieces of the memory system
- **GraphRAG** — preserve relations among decisions, components, risks, tests, lessons
- **Guardrails and hooks** — automated constraint enforcement
- **LoRA** — behavioral tuning, later, after retrieval and architecture stop delivering
  sufficient incremental gains

This stack is described as a staged progression, not a fantasy all-at-once implementation.
Each layer is justified by the limits of the previous one.

---

## Attribution Note — IMPORTANT

The term "Agile V" is **not original to this work**. It comes from:

> *Agile V: A Compliance-Ready Framework for AI-Augmented Engineering* —
> [ArXiv 2602.20684](../papers/arxiv-2602.20684-agile-v-koch-wellbrock.pdf)

The Sandbox 005 work adopts and extends this framework to address the non-determinism gap:
the published framework assumes more determinism than LLM systems provide. The extension —
evals over unit tests, LLM-as-judge as triage not verification, human gates as non-optional —
is the original contribution.

Before publishing this article:
1. Read the ArXiv paper in full
2. Cite it explicitly with authors, title, and ArXiv ID
3. State clearly where the extension begins

---

## Call to Action (end of article)

One quiet paragraph. Not a services page. Something like:

> "I'm taking on a small number of engagements where this architecture is relevant to your
> team's situation. If that's you, reach out."

---

## Sources

- [Agile V: A Compliance-Ready Framework for AI-Augmented Engineering (ArXiv 2602.20684)](../papers/arxiv-2602.20684-agile-v-koch-wellbrock.pdf)
- [Agile V hybrid model — ITEA](https://itea.org/journals/volume-47-1/implementing-agile-v-hybrid-model/)
- [FHWA systems-engineering life cycle](https://ops.fhwa.dot.gov/seits/sections/section2/2_7.html)
- [SwarmForge repo — Uncle Bob](https://github.com/unclebob/swarm-forge)
- [Managing a swarm of 20 AI agents — Zach Wills](https://zachwills.net/i-managed-a-swarm-of-20-ai-agents-for-a-week-here-are-the-8-rules-i-learned/)
- [Anthropic Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval)
- [Microsoft GraphRAG docs](https://microsoft.github.io/graphrag/)
- [IBM LoRA overview](https://www.ibm.com/think/topics/lora)
- [Red Hat on LoRA adapters + semantic routing](https://www.redhat.com/en/blog/creating-cost-effective-specialized-ai-solutions-lora-adapters-red-hat-openshift-ai)
