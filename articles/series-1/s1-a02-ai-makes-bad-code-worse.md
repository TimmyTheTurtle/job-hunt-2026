# S1-A2 — AI Makes Bad Code Worse

**Status:** Not started
**Series position:** 2 of 10

---

## Thesis

AI accelerates output in proportion to the quality of the context it's given. Give it clean,
well-structured code and it extends that. Give it accumulated technical debt and it extends
that too — faster. The amplification is symmetric. Productive vibes, compounding debt.

There is a second mechanism that runs alongside amplification: silent accumulation. Technical
debt generated during vibe coding is invisible until it isn't. There is no review gate that
surfaces it. The code works. It passes the vibe check. The debt accumulates beneath the
surface until the codebase is the problem.

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

3. **The CodeScene empirical angle.** Code health scores predict bug concentration. Low health
   zones are where most defects live. They are also the zones where developers are most likely
   to reach for AI help — because they are the hardest, most confusing code. So AI assistance
   concentrates in exactly the zones where amplification does the most damage.

4. **Silent accumulation — the second mechanism.** Amplification is what happens in a single
   session with existing debt. Accumulation is what happens over time when there is no review
   gate. Vibe coding produces no artifacts that would surface the debt — no ADR asking "was
   this the right design?", no review step asking "do we understand what this does?". The
   debt lands and stays.

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
- Codebases cannot be /compact'd — context windows reset, codebases don't; the debt from
  yesterday is the context for today
- The amplification is statistical, not malicious — the agent mirrors its context
- CodeScene research: low health code zones are where bugs concentrate AND where AI help
  is most requested — a compounding trap
- Large-scale evidence: 24.2% of AI-introduced defects never cleaned up (arXiv:2603.28592)
- The self-reinforcing loop: vibe coding produces debt → debt contaminates future context →
  contaminated context produces more debt
- The acceleration-vs-offloading distinction: in clean code, acceleration is possible;
  in debt zones, offloading is almost inevitable
- Comprehension debt accumulates in the codebase and in the team simultaneously

## Solution Hints to Seed

- Code health as a prerequisite for AI assistance, not an afterthought
- Context management — what the agent sees determines what it produces
- Health gates before AI assistance in high-risk zones

---

## Sources

- [CodeScene code biomarkers research](https://codescene.com/blog/code-biomarkers/)
- [Adam Tornhill on psychology of code quality — Tech Lead Journal ep. 241](https://techleadjournal.dev/episodes/241/)
- [CodeScene guardrails for AI-assisted coding](https://codescene.com/blog/implement-guardrails-for-ai-assisted-coding)
- [Debt Behind the AI Boom — arXiv:2603.28592](https://arxiv.org/abs/2603.28592) — 304,362 AI commits; 24.2% of introduced defects never cleaned up
- [The Vibe-Check Protocol — arXiv:2601.02410](https://arxiv.org/abs/2601.02410) — acceleration vs. offloading; context quality determines which mode is even possible
- [Comprehension Debt in GenAI SE — arXiv:2604.13277](https://arxiv.org/abs/2604.13277) — debt accumulates in cognition and codebase simultaneously
