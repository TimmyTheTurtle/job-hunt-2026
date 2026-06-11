# Journal — 2026-06-11: Token Frugality Patterns and the Wait-Time Attention Problem

## Session Summary

Two related topics explored in depth. Both fed directly into S1-A3.

---

## Token Frugality — Patterns Extracted from Existing Projects

Scanned agent-orchestration, legal-tech-debt, agentic-sdlc-project-manager, and the
job-hunt-2026 bootstrap files. The following patterns are already present across projects
and form a coherent system — they just hadn't been named together.

### Identified Patterns

**Semantic chunking to token budgets**
Defined in legal-tech-debt RAG spec. Split documents on semantic unit boundaries (clause,
section, provision), not character counts. Each unit type has explicit soft and hard token
budgets (clauses: 150–400 tokens; sections: 400–1200). Arbitrary chunking destroys retrieval
precision; semantic chunking preserves the unit the LLM needs to reason about.

**SLM-first, frontier-model-last routing**
Core to Clean Claws doctrine. Bounded, classification-type tasks (ADR-013 `language_context`
annotation — ~500 tokens, few-shot prompt) route to small cheap models. The frontier model is
reserved for judgment-heavy, non-deterministic, or high-stakes work. The cost hypothesis:
up to two orders of magnitude reduction. The architectural principle: this is model selection
by task type, not by preference.

**Compact bootstrap as session cost control**
The AGENT_BOOTSTRAP_COMPACT.md and UNIVERSAL-AGENT-BOOTSTRAP.md are explicitly designed for
"low token overhead." Every session's context load is treated as a cost. The bootstrap is the
contract for what the agent must know at startup vs. what it retrieves on demand from the repo.

**Dense summary layer (AGENT_CONTEXT.json) vs. full truth**
AGENT_CONTEXT.json is described as "compact current focus, active lanes, latest handoff and
journal pointers — Read-only summary, not full truth." Full truth lives in the repo. The
summary layer is what the agent carries across sessions. Pattern: maintain a dense authoritative
summary that serves as the context load; do not pull full source files unless needed.

**Anti-rampancy / context expiry (Workstream 4)**
Named "rampancy" — context poisoning via unfiltered accumulation of external noise. Guardrails:
provenance fields, TTLs for unverified knowledge, no direct writes from browsing into core
instructions, a Janitor process for entropy detection. The negative-space version of token
frugality: not just "load less" but "expire aggressively and audit what persists."

**Deterministic filter before model judgment (Clean Claws principle 6)**
Cheap deterministic rules first, LLM judgment only when rules fail. ADR-013 documents this
explicitly: tried deterministic language_context classification, failed on messy carrier
formats, escalated to LLM. Principle: don't spend model tokens where a regex will do.

### Framing Note

Token frugality is not a cost-cutting measure — it is a system design discipline. A fast SLM
call that keeps the developer in flow is architecturally different from a slow frontier model
call that pushes them to check email. The cost argument is table stakes. The context integrity
argument is the interesting one.

---

## The Wait-Time Attention Problem

### Research Findings

The conversation is fragmented. Nobody has written the clean essay on this yet.

Closest existing voices:
- Simon Willison calls parallel agent workflows "a thermonuclear ADHD amplifier"
- Armin Ronacher (Pragmatic Engineer): "it's only so much my mind can review"
- arXiv 2606.05391: empirical study of what developers do during agent runs — framed as
  safety/oversight problem, not cognitive cost problem
- arXiv 2507.03156: applies 23-minute attention recovery time to LLM workflows — but frames
  the LLM as the interrupter, not the thing you wait for

What nobody has written: the asymmetry (agent runs: minutes; attention recovery: 23 minutes),
the active choice between idle focus and context-switching, any application of deep work
frameworks to LLM latency as a recurring workflow event.

### The Solution Already in the Workflow

Dorian's insight: the solution is documentation and journaling. While the agent runs the
current task, you read the journal and artifacts from the previous run. The wait time is
not idle time — it is the human gate stage that was going to happen anyway.

This reframes the entire problem. The attention damage is not caused by the wait. It is
caused by workflows that have no review artifacts — vibe coding workflows, where there is
nothing structured to read between runs. The agent ships, you wait, you either context-switch
(pay the 23-minute recovery cost) or stare at the screen (passivity training). Both damage
the project.

With review artifacts, the pause is the highest-value moment in the cycle: the moment where
understanding is built and cognitive capability is protected.

Workflows without review artifacts force passivity. Vibe coding has no review artifacts. That
is the same failure mode as the rest of the article.

### Where This Landed

Integrated into S1-A3 as a new "Wait-Time Attention Problem" subsection under Main Points.
Added to solution hints. Added 8 new source links to S1-A3 sources and to research.md.

---

## Files Changed This Session

- `articles/series-1/s1-a03-shipped-more-felt-worse.md` — added wait-time attention section,
  8 new sources
- `articles/research.md` — new section: Token Frugality / Context Economics, 7 source links
- `articles/ROADMAP.md` — created (committed earlier this session, see prior commit)
- `journal/2026-06-11-token-frugality-and-attention.md` — this file

---

## Open Threads

- Token frugality as architecture could be its own article (S2-A3 candidate or standalone)
- The wait-time essay remains unwritten by anyone; could be a standalone piece or A3 anchor
- S1-A3 is the right home for the wait-time argument; the token frugality patterns are
  more naturally S2 material
