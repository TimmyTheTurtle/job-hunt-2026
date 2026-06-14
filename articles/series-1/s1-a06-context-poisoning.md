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

## Argument Flow

1. **A5 introduced constraints as the answer to unconstrained generation. A6 introduces
   the next problem:** even with constraints, the context the agent operates in degrades
   over time. Constraints help. But what if the context itself is contaminated?

2. **Two forms of poisoning — organic and adversarial.** Organic: accumulated debt, stale
   ADRs, outdated architecture notes, duplicate summaries. The agent was given good
   documentation once. It has since been steered by the residue of decisions that were
   reversed, names that were changed, designs that were replaced. The context fights the
   engineer's current intent using their own past thoughts.
   Adversarial: XOXO attacks achieve 75%+ success rates by injecting malicious instructions
   through documents the agent reads. The organic and adversarial cases are the same
   mechanism — the agent mirrors its context, including context it should not trust.

3. **The U-shaped accuracy problem.** Models perform better on content at the start and end
   of context windows. Middle content is systematically deprioritized. This means a long
   context is not just expensive — it is actively unreliable. The critical information you
   carefully placed in the middle may not be influencing the output at all.

4. **More context is not always better context.** This is the counterintuitive claim the
   article earns. The instinct when AI output degrades is to add more information. The correct
   diagnosis is often the opposite: the context has too much, and the wrong things are in it.
   Context poisoning is a signal to clean and curate, not to add.

5. **The Janitor concept.** A process that periodically scans context stores for entropy —
   stale notes, duplicate summaries, expired decisions. Not a human review task. An automated
   hygiene pass. This is what makes context management scalable.

6. **Tease the solution architecture.** Retrieval over stuffing. Fresh summaries over raw
   history. Canonical vs. scratch distinction enforced structurally. That is what A7 builds
   on — selective retrieval as the answer to context that cannot be trusted at scale.

## Main Points to Discuss

- A5 introduced constraints; A6 introduces the next layer: context itself degrades
- Organic poisoning: stale ADRs, duplicate summaries, reversed decisions still in context
- The feeling of the system fighting your intent using your own past thoughts
- Adversarial poisoning: XOXO attacks (75%+ success rate) — same mechanism, deliberate
- The U-shaped accuracy problem: middle context is systematically deprioritized by models
- More context is not better context — poisoning is a signal to curate, not accumulate
- The Janitor concept: automated entropy scanning, not manual review overhead
- Connection to token frugality: context hygiene and cost efficiency are the same discipline

## Solution Hints to Seed

- Retrieval over stuffing — selective, not comprehensive
- Fresh summaries over raw accumulated history
- Canonical vs. scratch separation enforced structurally, not by convention
- Automated Janitor process for entropy detection and expiry
- TTLs on unverified knowledge

---

## Sources

- [XOXO: Cross-Origin Context Poisoning attacks on AI coding assistants (ArXiv)](https://arxiv.org/html/2503.14281v1)
- [Context rot is slowing down your AI agent — LogRocket](https://blog.logrocket.com/context-rot-slowing-down-your-ai-agent-how-fix/)
- [Context Rot: Why LLMs degrade as context grows — Morph](https://www.morphllm.com/context-rot)
- [How Long Contexts Fail and How to Fix Them — dbreunig](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html)
- [Context poisoning in LLMs — Elastic](https://www.elastic.co/search-labs/blog/context-poisoning-llm)
- [LLM context window limitations — Atlan](https://atlan.com/know/llm-context-window-limitations/)
- [Contextual Retrieval — Anthropic](https://www.anthropic.com/engineering/contextual-retrieval)
