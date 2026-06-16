# S1-A4 — Why Documentation Fails in AI-Assisted Development

**Status:** Not started
**Series position:** 4 of 10

---

## Voice and Tone

- **This is the personal arc article.** Point 4 of the argument flow says so explicitly: the
  author's own trajectory through under-documentation, then overcorrection into unfiltered
  journals, is the through-line. Write it in first person without apology. The credibility
  comes from having made both mistakes.
- **Register:** reflective but precise. Not confessional — the emotional content is in the
  structure of the argument, not in explicit feeling-statements. "The reasoning was in a chat
  session that closed six weeks ago" is the right register.
- **Do not lecture about documentation.** The argument is that most teams are doing the
  wrong kind, not that they are lazy. Respect the effort before redirecting it.
- **The "wrong reader" reframe is the article's core move.** Write toward it early. Everything
  else is consequence.
- **ADRs should be introduced as a discovery**, not as a recommendation. "Here is what
  actually works and why" rather than "you should write ADRs."

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

## Argument Flow

1. **A3 showed the cognitive cost. A4 shows where the damage lives in the codebase.**
   The team has been shipping things nobody fully understands. At some point someone asks
   "why is this designed this way?" and nobody knows. The rationale was in a chat session
   that closed six weeks ago.

2. **Two failure modes, same root cause.** Underdocumentation: reasoning never recorded,
   lost on exit. Overdocumentation: journals, summaries, AI-generated handoffs pile up —
   nobody reads them because reading them costs more than re-deriving. Both produce the
   same outcome: the reasoning is unavailable when needed. Activity without durable
   understanding.

3. **Documentation designed for the wrong reader.** Human-facing docs assume a reader who
   can infer context, scan git history, ask colleagues. Agent-facing context can't do any
   of that — it has a window. What doesn't make it into that window doesn't exist. Most
   documentation was designed for humans. It fails agents not because it's wrong but because
   it wasn't designed for retrieval.

4. **The personal through-line.** Not enough documentation → rationale lost, repeated
   rediscovery. Overcorrection into journals and AI-generated lessons → too much unfiltered
   material buries the reasoning it was meant to preserve. This is the author's own arc.
   It makes the failure modes credible — both are real, and they are sequential.

5. **ADRs as the counter-example.** ADRs work not because they are thorough but because
   they capture the one thing that matters: WHY. Context, decision, consequences. Compact
   enough to retrieve. Specific enough to answer the question. That is the design target
   for agent-facing documentation.

6. **Tease the architecture.** The fix is not better documentation — it is documentation
   designed as memory infrastructure. What gets written, in what format, indexed for what
   retrieval. That is A7 and A8.

## Main Points to Discuss

- A3 showed cognitive cost; A4 shows where it lives in the artifact layer
- Two failure modes with the same root: underdocumentation (rationale lost) and
  overdocumentation (rationale buried) — both produce unavailable reasoning
- Documentation designed for humans fails agents: wrong reader, wrong format, wrong
  retrieval assumptions
- Personal through-line: experienced both failure modes in sequence
- ADRs as the counter-example: WHY captured compactly enough to survive retrieval
- Too little documentation and the reasoning is lost; too much unfiltered documentation
  and it gets buried — the solution is not more notes, it is better memory architecture

## Solution Hints to Seed

- ADRs for significant decisions only — capture WHY, not WHAT
- Distinguish canonical truth (ADRs, specs) from scratch notes (journals, drafts)
- Design documentation for retrieval, not for completeness
- Retrieval over stuffing

---

## Sources

- [Vibe coding in style.md — AGENTS.md as discipline framework (Evil Martians)](https://evilmartians.com/chronicles/vibe-coding-in-style-dot-md)
- [Documentation: diminishing returns — Allan Kelly](https://www.allankelly.net/archives/5516/documentation-another-case-of-rapidly-diminishing-returns/)
- [ADR best practices — AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/master-architecture-decision-records-adrs-best-practices-for-effective-decision-making/)
- [ADR guidance — Microsoft Azure Well-Architected](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record)
- [ADR creation practices — Olaf Zimmermann](https://ozimmer.ch/practices/2023/04/03/ADRCreation.html)
