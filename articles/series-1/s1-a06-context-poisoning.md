# S1-A6 — Context Poisoning

**Status:** Not started
**Series position:** 6 of 10

---

## Thesis

At some point, accumulated AI-generated notes, summaries, and memory artifacts stop helping and
start contaminating the active context window — leading to distraction, overflow, stale
reasoning, and compounding degradation. Context poisoning is what happens when the context an
agent operates in has accumulated bad information: outdated architecture, inconsistent naming,
misleading comments, stale tests. The agent mirrors its context. Poison in, poison extended.

There is also a security dimension: XOXO attacks (Cross-Origin Context Poisoning) achieve 75%+
success rates by injecting malicious instructions through documents the agent reads. The organic
version — accumulated debt and drift — is less dramatic but more pervasive.

---

## Key Claims

- Context poisoning is the mechanism, not a metaphor
- It happens organically through debt accumulation and deliberately through adversarial injection
- Cleaning the context is not optional maintenance — it is the primary engineering discipline
  in agentic workflows
- More context is not always better context — the U-shaped accuracy curve is real

---

## Main Points to Discuss

- Context distraction and context overflow
- Why accumulated AI-generated notes become stale: old ADRs, duplicate summaries, historical
  residue steering the model after they should have expired
- The feeling that the system fights your current intent with your own past thoughts
- XOXO attacks as the adversarial extreme of the same phenomenon
- The U-shaped accuracy problem: models perform better on content at the start and end of
  context windows — middle content is systematically deprioritized

## Solution Hints to Seed

- Retrieval over stuffing
- Fresh summaries over raw history
- Explicitly separating canonical, reference, and scratch notes

---

## Sources

- [XOXO: Cross-Origin Context Poisoning attacks on AI coding assistants (ArXiv)](https://arxiv.org/html/2503.14281v1)
- [Context rot is slowing down your AI agent — LogRocket](https://blog.logrocket.com/context-rot-slowing-down-your-ai-agent-how-fix/)
- [Context Rot: Why LLMs degrade as context grows — Morph](https://www.morphllm.com/context-rot)
- [How Long Contexts Fail and How to Fix Them — dbreunig](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html)
- [Context poisoning in LLMs — Elastic](https://www.elastic.co/search-labs/blog/context-poisoning-llm)
- [LLM context window limitations — Atlan](https://atlan.com/know/llm-context-window-limitations/)
- [Contextual Retrieval — Anthropic](https://www.anthropic.com/engineering/contextual-retrieval)
