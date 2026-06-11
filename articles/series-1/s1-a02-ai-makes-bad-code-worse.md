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

## Main Points to Discuss

- The attention loop article introduced the loop mechanics. This article shows the structural
  consequence: bad code gets worse faster
- Adam Tornhill's CodeScene research: code with low health scores (high complexity, high
  coupling) is where bugs concentrate — AI working in those areas increases output velocity
  in the highest-risk zones
- The amplification is not malicious — it is statistical. The agent mirrors what it sees.

## Solution Hints to Seed

- Context management
- Code health as a prerequisite for AI assistance, not an afterthought

---

## Sources

- [CodeScene code biomarkers research](https://codescene.com/blog/code-biomarkers/)
- [Adam Tornhill on psychology of code quality — Tech Lead Journal ep. 241](https://techleadjournal.dev/episodes/241/)
- [CodeScene guardrails for AI-assisted coding](https://codescene.com/blog/implement-guardrails-for-ai-assisted-coding)
