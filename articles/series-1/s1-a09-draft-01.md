# There Is No Such Thing as Clean Agentic Code
### Draft 1 - expanded working draft / research packet

---

## Working Note

This article should feel like an earned reframe, not a cheap contrarian take.

Need to respect the clean-code tradition before redirecting it.
The thesis is not "clean code is dumb now."
The thesis is "the target reader changed, so some of the discipline has to be reinterpreted."

The best hinge line remains:

> Every context window is day one.

That line can carry the whole piece.

---

## Core Argument

"Clean code for agents" is probably a category error in the same way "clean code for a compiler"
would be. A compiler does not appreciate tasteful decomposition. It obeys formal structure.
An agent is not identical to a compiler, but it also does not read code the way an experienced
human teammate does. It reads a context window assembled from partial evidence.

So:

- some classic clean-code ideas still help
- but they help for new reasons
- and some of the truly important properties are now properties of context architecture,
  not only code style

---

## What This Article Has To Do

1. compare human, compiler/linter, and agent readers
2. reclassify which clean-code ideas transfer and why
3. make naming, contracts, and boundedness central
4. connect token cost to cleanliness without turning the article into a cost piece
5. end by showing that context architecture is the new discipline

---

## Research Spine

### 1. Evil Martians / AGENTS.md as style externalization

The Evil Martians article is useful again here because it shows something important:

when a human expert's style has to become legible to an assistant, it gets externalized as:

- context
- use-case framing
- rules
- patterns
- preferred naming

That is already halfway to the thesis of this article.

Source:
- [Vibe coding in style.md](https://evilmartians.com/chronicles/vibe-coding-in-style-dot-md)

### 2. Akita and "clean code for AI agents"

This source is useful mainly because it proves the conversation is happening in the engineering
community already. The article can then push the argument further:

clean code still matters, but agent-facing maintainability is not exhausted by classic style
guidance.

Source:
- [Clean Code for AI Agents](https://akitaonrails.com/en/2026/04/20/clean-code-for-ai-agents/)

### 3. Context architecture as the true successor concept

This article should lightly borrow from the series as a whole:

- A4: rationale must be externalized
- A6: context can rot
- A7: retrieval governs what becomes active context
- A8: relations matter

By the time A9 arrives, the reader should be ready for:

the unit of readability for an agent is not the file alone. It is the assembled working context.

---

## What Transfers From Classic Clean Code

Need a nice explicit list here.

Transfers:

- consistent vocabulary
- one concept, one name
- predictable typing and explicit contracts
- small bounded modules
- explicit tests aligned to behavior
- low surprise density

But the reason changes:

- names are not just for readability; they are semantic anchors
- small files are not just ergonomic; they are context-economical
- contracts are not just documentation; they are agent-readable specifications
- tests are not just regression safety; they are behavioral boundaries

---

## What Does Not Transfer Cleanly

Anything that assumes:

- long-term accumulation of tacit context in a human mind
- broad shared background among experienced teammates
- generous time to infer intent from style alone

This is where the article should stay respectful.
Do not mock aesthetic concerns. Just say they are no longer sufficient.

Possible line:

> What made code elegant for a senior human reader is not always what makes it recoverable for
> a context-window-bound assistant.

---

## Token Frugality As Cleanliness

This should be a discovery, not the center.

Possible argument:

A verbose prompt that works is not necessarily clean if it must be repeated across thousands of
calls or across many teammates. Concision, boundedness, and crisp contracts become cleanliness
properties because they reduce the amount of contextual cargo the system has to carry.

This article should only hint at this and point to S2-A7 later.

---

## Counterarguments To Handle

### "So code style no longer matters?"

No. It still matters indirectly and often materially.
The article should say: clean code helps, but context architecture is the missing layer.

### "Agents should just get better"

Maybe, but the whole series argues that systems should be designed for the actual reader they
currently have, not the one people hope for later.

### "This is all just documentation again"

No. Documentation is one part of context architecture.
Naming, file boundaries, contracts, tests, retrieval, and graph structure also belong here.

---

## Suggested Structure

1. Open with the category-error claim.
2. Compare compilers, humans, and agents as readers.
3. Introduce the "every context window is day one" line.
4. Separate what transfers from what does not.
5. Bring in naming, contracts, boundedness, and token frugality.
6. End by saying context architecture, not code style alone, is the new discipline.

---

## Lines Worth Keeping

- Every context window is day one.
- Names are carrying more semantic load than ever.
- Clean code is still helpful; it is just no longer the whole problem.
- The unit of readability for an agent is the assembled context.
- Elegant code is not automatically recoverable code.

---

## Source Pack

Primary practical sources:

- [Vibe coding in style.md](https://evilmartians.com/chronicles/vibe-coding-in-style-dot-md)
- [Clean Code for AI Agents](https://akitaonrails.com/en/2026/04/20/clean-code-for-ai-agents/)
- [Clean AI: Agentic Discipline](https://cleancoders.com/episode/agentic-discipline-1)

Supporting links from the outline:

- [Skills, Not Vibes: Teaching AI agents to write clean code](https://dev.to/gde/skills-not-vibes-teaching-ai-agents-to-write-clean-code-3l9e)
- [So your developers use AI now](https://evilmartians.com/chronicles/so-your-developers-use-ai-now-here-is-what-to-know)

