# S1-A4 — Why Documentation Fails in AI-Assisted Development

**Status:** Not started
**Series position:** 4 of 10

---

## Thesis

Missing documentation and vibe coding share a common failure mode: they produce activity without
durable understanding. One loses the reasoning by never recording it; the other loses it by
keeping it transient inside endless chats.

Documentation written for humans assumes a reader who can infer context, ask questions, look at
git history, and build a mental model over time. AI agents have none of that — they have a
context window. Documentation that doesn't make it into the context window doesn't exist from
the agent's perspective.

The failure mode: teams add more documentation, AI ignores most of it, the team concludes
documentation is useless, and stops writing it. The correct diagnosis: documentation isn't
failing because it's incomplete — it's failing because it was designed for the wrong reader.

---

## Key Claims

- Human-facing documentation and agent-facing context are different artifacts with different
  design requirements
- Adding more of the wrong kind of documentation makes the problem worse
- The right response is redesigning what gets written, not writing more of it
- ADRs work because they capture WHY — which is what agents (and new team members) actually need

---

## Main Points to Discuss

- Personal documentation failures: not keeping enough durable documentation caused loss of
  rationale, repeated rediscovery, and confusion during later work
- The overcorrection: journals, ADRs, handoffs, and AI-generated lessons — spending time
  reviewing these so the evolving system remains legible
- Why "more docs" alone does not equal more clarity
- The need to distinguish authoritative memory from exploratory thinking
- Documentation as memory infrastructure, not prose exhaust

## Solution Hints to Seed

- ADRs for significant decisions only
- Distinguish canonical truth from scratch notes
- Retrieval over stuffing

---

## Sources

- [Vibe coding in style.md — AGENTS.md as discipline framework (Evil Martians)](https://evilmartians.com/chronicles/vibe-coding-in-style-dot-md)
- [Documentation: diminishing returns — Allan Kelly](https://www.allankelly.net/archives/5516/documentation-another-case-of-rapidly-diminishing-returns/)
- [ADR best practices — AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/master-architecture-decision-records-adrs-best-practices-for-effective-decision-making/)
- [ADR guidance — Microsoft Azure Well-Architected](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record)
- [ADR creation practices — Olaf Zimmermann](https://ozimmer.ch/practices/2023/04/03/ADRCreation.html)
