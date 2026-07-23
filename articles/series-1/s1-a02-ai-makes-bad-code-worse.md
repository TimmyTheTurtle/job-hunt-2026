# S1-A2 — AI Makes Bad Code Worse

**Status:** Not started
**Series position:** 2 of 10

---

## Voice and Tone

- **Register:** cooler and more analytical than A1, but with edge. The exasperation is at the
  mechanism, not at practitioners. The system is doing exactly what it was designed to do —
  that is the problem.
- **First person:** yes, but restrained. "I have seen this" rather than "I feel this." The
  practitioner writing about a structural trap they have diagnosed, not confessed to.
- **The `/compact` line is a keeper.** That's the voice — technically precise, slightly wry,
  earned. Write toward more moments like it.
- **Do not moralize.** The argument is structural, not ethical. Developers are not doing
  something wrong. The pattern is wrong. Keep the blame on the architecture, not the people.
- **Positive case before the floor** — same rule as A1. Name what good looks like before
  laying out the empirical damage.

---

## Thesis

AI accelerates output in proportion to the quality of the context it's given. Give it clean,
well-structured code and it extends that. Give it accumulated technical debt and it extends
that too — faster. The amplification is symmetric. Productive vibes, compounding debt.

The A1 mechanism matters here: continuation-friendly tooling keeps engineers in extension mode
after the phase where extension is safe. Once the loop is rewarding "one more pass" rather than
"stop and specify," the agent keeps extending whatever context exists. In clean code it extends
good patterns. In debt-heavy code it extends the debt.

There is a second mechanism that runs alongside amplification: silent accumulation. Technical
debt generated during vibe coding is invisible until it isn't. There is no review gate that
surfaces it. The code works. It passes the continuation loop's reward checks. The debt
accumulates beneath the surface until the codebase is the problem.

Context windows can be reset. Codebases cannot. When the context gets poisoned you start a
new session. When the codebase gets poisoned you have to live in it. That asymmetry makes
the codebase the more dangerous accumulation site — and the longer vibe coding runs without
a review gate, the more the codebase becomes the contaminated context the agent works in
next time.

---

## Key Claims

- AI amplifies the pattern of surrounding code, not the ideal pattern
- Technical debt zones are exactly where AI does the most damage
- Debt accumulates silently during vibe coding — no review gate surfaces it until it compounds
- Codebases cannot be /compact'd: context windows reset, codebases don't
- The longer vibe coding runs without review, the more the codebase poisons its own future sessions
- The problem is not the AI — it's the absent review mechanism that would surface the debt

---

## Argument Flow

1. **A1 established the loop. A2 shows the first structural consequence.** The reader stayed
   in exploration mode. Now look at what the codebase looks like. The agent has been extending
   whatever it found. If it found clean code, clean code got extended. If it found debt, debt
   got extended — faster.

2. **The amplification mechanism.** AI doesn't editorialize. It continues the pattern it
   sees. This is not a bug — it is how in-context learning works. The agent is doing exactly
   what it was designed to do. The problem is that "continue the pattern" is neutral about
   whether the pattern is good. In debt-heavy zones it is actively dangerous.

3. **The Agile-V process angle.** Agile V starts from the premise that AI-assisted engineering
   without built-in verification and traceability creates machine-speed delivery with no
   reliable gate. Agentic Agile-V sharpens that into verification debt: output volume grows
   faster than verification capacity, so weak tests, broad patches, unvalidated dependencies,
   undocumented behavior, and reviewer burden accumulate. That is the same trap this article
   is naming from the codebase side. When continuation is easy and evidence is optional, the
   system extends debt faster than the team can see it.

4. **Silent accumulation — the second mechanism.** Amplification is what happens in a single
   session with existing debt. Accumulation is what happens over time when the reward loop
   keeps privileging continuation over review. Vibe coding produces no artifacts that would
   surface the debt — no ADR asking "was this the right design?", no review step asking "do
   we understand what this does?". The debt lands and stays.

   Context windows can be reset. When a session gets too long or too confused, you /compact
   or start fresh. Codebases have no equivalent. The debt from yesterday's session is the
   context for today's. It compounds.

5. **The large-scale empirical confirmation.** 304,362 AI-authored commits (arXiv:2603.28592):
   24.2% of AI-introduced defects are never cleaned up. Not "introduced and fixed quickly" —
   introduced and left. The debt is not temporary.

6. **The acceleration-vs-offloading distinction begins here.** In clean code, a skilled
   developer using AI for acceleration (understanding maintained) produces good output faster.
   In debt zones, even a skilled developer tends toward offloading because the context is
   confusing — and offloading in a confusing context produces confident wrong output.

7. **Tease the fix without delivering it.** The fix is not "don't use AI in bad code."
   The fix is managing what the agent sees — context hygiene, code health gates, constraint
   enforcement — and building the review artifacts that surface debt before it compounds.
   That's A4, A5, and A6.

## Main Points to Discuss

- A1 established the loop mechanics; A2 shows what the codebase looks like afterward
- Two mechanisms: amplification (agent extends bad patterns) and accumulation (debt lands
  silently with no review gate to surface it)
- Continuation-friendly tooling keeps the team in extension mode after extension stopped being safe
- Codebases cannot be /compact'd — context windows reset, codebases don't; the debt from
  yesterday is the context for today
- The amplification is statistical, not malicious — the agent mirrors its context
- Agile-V / Agentic Agile-V framing: machine-speed generation without built-in verification
  creates verification debt and reviewer overload — a compounding trap
- Large-scale evidence: 24.2% of AI-introduced defects never cleaned up (arXiv:2603.28592)
- The self-reinforcing loop: vibe coding produces debt → debt contaminates future context →
  contaminated context produces more debt
- The acceleration-vs-offloading distinction: in clean code, acceleration is possible;
  in debt zones, offloading is almost inevitable
- Comprehension debt accumulates in the codebase and in the team simultaneously

## Solution Hints to Seed

- Verification gates and scoped evidence as a prerequisite for AI assistance, not an afterthought
- Context management — what the agent sees determines what it produces
- Risk-adaptive gates before AI assistance in high-risk zones

---

## Sources

- [Agile V: A Compliance-Ready Framework for AI-Augmented Engineering — arXiv:2602.20684](../papers/arxiv-2602.20684-agile-v-koch-wellbrock.pdf) — machine-speed delivery needs built-in verification, traceability, and human approval gates
- [Agentic Agile-V: From Vibe Coding to Verified Engineering — arXiv:2605.20456](../papers/arxiv-2605.20456-agentic-agile-v-scope-v.pdf) — names verification debt, conversation-to-contract gates, and risk-adaptive evidence bundles
- [Debt Behind the AI Boom — arXiv:2603.28592](../papers/arxiv-2603.28592-debt-behind-ai-boom.pdf) — 304,362 AI commits; 24.2% of introduced defects never cleaned up
- [The Vibe-Check Protocol — arXiv:2601.02410](../papers/arxiv-2601.02410-vibe-check-protocol.pdf) — acceleration vs. offloading; context quality determines which mode is even possible
- [Comprehension Debt in GenAI SE — arXiv:2604.13277](../papers/arxiv-2604.13277-comprehension-debt.pdf) — debt accumulates in cognition and codebase simultaneously
