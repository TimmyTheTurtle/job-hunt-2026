# S2-A3 — Context Architecture Is the New Software Architecture

**Status:** Not started

---

## Thesis

If the agent is a mirror of its context, then the design of the context is the design of the
system. Context architecture is the new software architecture — not metaphorically, but
operationally. What artifacts exist for the agent to retrieve, how they are structured, where
human gates are placed, how context poisoning is prevented across sessions — these are
first-class engineering decisions.

---

## Key Claims

- Context architecture is a discipline, not a metaphor
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

---

## Sources

- [Agentic Software Engineering: Foundational Pillars (ArXiv)](https://arxiv.org/pdf/2509.06216)
- [AI-Infused Development Needs More Than Prompts — O'Reilly](https://www.oreilly.com/radar/ai-infused-development-needs-more-than-prompts/)
- [Agentic AI Content Verification — Quality Gates (Pebblous)](https://blog.pebblous.ai/blog/agentic-content-pipeline-verification/en/)
- [Why Your AI Agent Needs a Quality Gate — dev.to](https://dev.to/yurukusa/why-your-ai-agent-needs-a-quality-gate-not-just-tests-42eo)
- [AI Agent Governance — Policy and Compliance 2026](https://www.digitalapplied.com/blog/ai-agent-governance-policy-compliance-2026)
