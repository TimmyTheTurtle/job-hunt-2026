# S1-A5 — Vibe Coding Without Constraints Is Just Vibe Coding

**Status:** Not started
**Series position:** 5 of 10 — the pivot article

---

## Voice and Tone

- **The pivot article.** The tone shifts here from diagnostic to constructive. After four
  articles naming problems, this one changes direction. The register should feel like a gear
  change — still composed, but forward-moving. Not cheerful. Purposeful.
- **"Constraint-first" is not a compliance argument.** Do not let this article sound like
  a process document. The argument is pragmatic: constraints change what the agent generates.
  That is an engineering observation, not a methodology pitch.
- **Uncle Bob Martin reference:** engage with the argument, not the authority. The point is
  that function size stopped being a style guideline and became a context management constraint
  — the underlying principle didn't change, the stakes did. Credit the observation, then own
  the extension.
- **First person selectively.** The examples of constraint-first prompts that actually worked
  differently should be in first person if drawn from experience. The theoretical framing
  can be third person.
- **Do not over-promise.** "Mini V per feature" is a lightweight discipline, not a
  transformation. Present it as a practical unit of structure, not a silver bullet.
  The composure of the claim is part of its credibility.

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

## Argument Flow

1. **The pivot article.** A1-A4 diagnosed problems. A5 is where the direction changes.
   Everything before this showed what goes wrong without structure. This article asks:
   what does structure actually look like in practice, without making AI-assisted development
   feel like a compliance exercise?

2. **The wrong objection.** The common pushback against adding structure is that it slows
   things down. This assumes the metric is generation speed. The right metric is rate of
   trustworthy delivery — output you can ship, debug, extend, and explain. By that metric,
   unconstrained generation is slow because it produces things you cannot trust.

3. **Constraints change what the agent generates.** "Make it work" prompts produce sloppy
   code because the agent has no definition of "work." Constraint-first prompts — with
   preconditions, postconditions, and testable invariants — give the agent a target. The
   same model produces materially different output when it has something specific to satisfy.
   This is not about discipline as philosophy. It is about prompt engineering that produces
   verifiable results.

4. **Some clean code principles become hard requirements.** For humans, function size is a
   readability guideline. For agents, a function that doesn't fit in a single tool call can't
   be worked on atomically — it becomes a context management problem. The principle didn't
   change. The reason it matters changed.

5. **The mini V per feature.** You don't need to adopt a full systems engineering process.
   A lightweight version — left-side requirements before generation, right-side verification
   before acceptance — is enough to catch the failure mode where the agent produces confident
   wrong output. This is practical, not theoretical.

6. **Hooks as constraint enforcement infrastructure.** PreToolUse hooks make constraints
   enforceable rather than aspirational. The agent cannot bypass them by generating confident
   output. This is the first concrete architecture element the series introduces.

## Main Points to Discuss

- The pivot: A1-A4 diagnosed, A5 changes direction toward what structure looks like
- The wrong objection: speed of generation is not the metric; rate of trustworthy delivery is
- Constraint-first prompting: preconditions, postconditions, invariants change output quality
- Clean code principles that were guidelines for humans become hard requirements for agents
  (function size, atomicity, single responsibility)
- The mini V per feature: lightweight left-side/right-side discipline without full process overhead
- PreToolUse hooks as enforceable constraint infrastructure — not aspirational, automated
- Agile V: the formal framing (ArXiv 2602.20684) — cite with attribution

## Solution Hints to Seed

- Constraint-first prompting as standard practice
- Mini V per feature: specify before generating, verify before accepting
- ADRs as guardrails the agent operates within
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
