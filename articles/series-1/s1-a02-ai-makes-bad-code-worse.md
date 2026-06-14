# S1-A2 — AI Makes Bad Code Worse

**Status:** Not started
**Series position:** 2 of 10

---

## Thesis

AI accelerates output in proportion to the quality of the context it's given. Give it clean,
well-structured code and it extends that. Give it accumulated technical debt and it extends
that too — faster. The amplification is symmetric. Productive vibes, compounding debt.

---

## Key Claims

- AI amplifies the pattern of surrounding code, not the ideal pattern
- Technical debt zones are exactly where AI does the most damage
- The problem is not the AI — it's introducing AI without managing the context it operates in

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

4. **The large-scale empirical confirmation.** 304,362 AI-authored commits (arXiv:2603.28592):
   24.2% of AI-introduced defects are never cleaned up. Not "introduced and fixed quickly" —
   introduced and left. The debt is not temporary.

5. **The acceleration-vs-offloading distinction begins here.** In clean code, a skilled
   developer using AI for acceleration (understanding maintained) produces good output faster.
   In debt zones, even a skilled developer tends toward offloading because the context is
   confusing — and offloading in a confusing context produces confident wrong output.

6. **Tease the fix without delivering it.** The fix is not "don't use AI in bad code."
   The fix is managing what the agent sees — context hygiene, code health gates, constraint
   enforcement. That's A5 and A6.

## Main Points to Discuss

- A1 established the loop mechanics; A2 shows what the codebase looks like afterward
- The amplification is statistical, not malicious — the agent mirrors its context
- CodeScene research: low health code zones are where bugs concentrate AND where AI help
  is most requested — a compounding trap
- Large-scale evidence: 24.2% of AI-introduced defects never cleaned up (arXiv:2603.28592)
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
