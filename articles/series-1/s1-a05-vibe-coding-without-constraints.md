# S1-A5 — Vibe Coding Without Constraints Is Just Vibe Coding

**Status:** Not started
**Series position:** 5 of 10 — the pivot article

---

## Thesis

LLM-assisted development becomes more accurate and more maintainable when constrained by
explicit requirements, invariants, tests, and design conditions rather than vague intent.

The common objection to adding structure to AI workflows is that it slows things down. That
objection treats speed of generation as the metric. The right metric is rate of trustworthy
delivery.

Uncle Bob Martin's "Clean AI: Agentic Discipline" series makes this argument from a
craftsmanship angle: clean code principles don't disappear with AI — they become more important.
Some of them become technical requirements rather than guidelines. Function size, for example,
isn't just a readability concern anymore: a function that doesn't fit in a single tool call
can't be worked on atomically by an agent.

---

## Key Claims

- The case against constraints assumes the wrong success metric
- Constraints are not friction — they are the mechanism by which AI output becomes trustworthy
- Some clean code principles that were guidelines for humans become hard requirements for agents
- A mini V-model per feature (left-side requirements → right-side verification) is a practical
  unit of discipline that doesn't require changing your entire workflow

---

## Main Points to Discuss

- Why generic "make it better" prompts produce sloppy code
- Constraint-first generation: preconditions, postconditions, testable invariants
- Why constraints are not anti-creativity — they channel creativity into safety and predictability
- Agile V: combining agile iteration with V-model verification discipline
- Hooks and approval steps for critical transitions as lightweight constraint enforcement

## Solution Hints to Seed

- Treat tests and ADRs as guardrails
- Use a left-side/right-side life-cycle mentality — mini V per feature
- PreToolUse hooks as automated constraint enforcement

---

## Sources

- [Clean AI: Agentic Discipline — Uncle Bob Martin (Clean Coders)](https://cleancoders.com/episode/agentic-discipline-1)
- [Clean Code for AI Agents — AkitaOnRails](https://akitaonrails.com/en/2026/04/20/clean-code-for-ai-agents/)
- [AI Agents for Clean Code — Uncle Bob at O'Reilly](https://www.oreilly.com/live-events/ai-agents-for-clean-code-with-uncle-bob-martin/0642572376765/0642572376758/)
- [Agile V hybrid model — ITEA](https://itea.org/journals/volume-47-1/implementing-agile-v-hybrid-model/)
- [Systems engineering life-cycle overview — FHWA](https://ops.fhwa.dot.gov/seits/sections/section2/2_7.html)
- [Design-constraint research — IEEE](https://ieeexplore.ieee.org/document/11218044)
- [Building guardrails for AI coding assistants — LinkedIn/PreToolUse hooks](https://www.linkedin.com/posts/lanemik_building-guardrails-for-ai-coding-assistants-activity-7418782309803544576-oSVd)
- [Hooks: guardrails for your AI coding assistant — dev.to](https://dev.to/rajeshroyal/hooks-how-to-put-guardrails-on-your-ai-coding-assistant-4gak)
