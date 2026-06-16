# S1-A9 — There Is No Such Thing as Clean Agentic Code

**Status:** Not started
**Series position:** 9 of 10 — the reframe article

---

## Voice and Tone

- **Register:** the reframe article. This one has permission to be a little more intellectually
  playful than the rest of Series 1. The thesis is surprising — "clean code is a category error
  for agents" — and the prose should carry that energy without overselling it.
- **"Probably a category error"** is the right hedge. Don't be more certain than the argument
  earns. The article's strength is the reframe, not the certainty.
- **First person:** yes, selectively. The moments where the argument is drawn from direct
  experience with agents should be first person. The compiler analogy and the category error
  framing can be in the cleaner analytical register.
- **Do not dismiss Uncle Bob or the clean code tradition.** The argument is not that they were
  wrong. It is that their target was human readers, and agents are a categorically different
  reader. Respect the tradition before redirecting it.
- **"Every context window is day one"** — this is the line the article hinges on. Write toward
  it. Everything before it is setup; everything after is consequence.
- **The economic dimension (S2-A7 cross-reference) should feel like a discovery**, not a
  footnote. "A verbose prompt that works is not clean at scale" is the kind of line that lands
  when it arrives without telegraphing.

---

## Thesis

"Clean code for agents" is probably a category error — the same way "clean code for a compiler"
would be. Compilers don't read code for meaning. Neither do agents. They read a context window
that contains code, among other things. The discipline that matters is not code style. It is
context architecture.

What does transfer: consistent vocabulary (agents have no out-of-band knowledge to resolve
naming ambiguity), small files (context window economics, not readability), explicit contracts
(type signatures and docstrings are agent-readable specifications), and externalized
architectural memory (the implicit knowledge senior engineers carry must be written down to
be retrievable).

What doesn't transfer: most aesthetic and structural guidance that assumes a human reader
building a mental model over time. An agent has no prior sessions. Every context window is day one.

---

## Key Claims

- "Clean code for agents" collapses into: normal clean code (indirectly helpful) + context
  architecture (the new discipline)
- The new discipline has different design targets than code style
- Writing for the new team member on day one, not the expert on day 100, is the standard that
  works for both humans and agents
- The agent is a mirror of its context — a corrupted context produces a corrupted continuation

---

## Main Points to Discuss

- How humans, machines (compilers/linters), and agents read code differently
- The context window as the unit of readability — not the file, not the module
- Token cost as a cleanliness dimension: a verbose prompt that works is not clean at scale.
  Small files, concise contracts, compressed tool outputs are frugality decisions that are
  also cleanliness decisions. S2-A7 makes the economic argument; this article notes the
  overlap without centering it.
- Names carry the entire semantic load for agents: naming is specification, not readability
- Consistency is more critical for agents than humans — agents have no out-of-band knowledge
- The implicit architectural memory that experienced engineers carry must be externalized
- ADRs as agent-first artifacts, not human-first documentation hygiene
- What "human-compatible agentic clean code" looks like in practice:
  - Contracts are more important than implementations
  - One concept, one name, everywhere
  - Files as context chunks
  - Externalize the WHY
  - Tests as behavioral contracts
  - Bounded modules with explicit surfaces

## Agent-Favorable Maintainability Features

- Consistent idioms and structure
- Small, locally understandable functions
- Predictable naming and typing
- Explicit tests aligned to code units
- Low surprise density and minimal unnecessary cleverness
- Graph-friendly code relationships navigable at repository scale

---

## Sources

- [Clean AI: Agentic Discipline — Uncle Bob Martin (Clean Coders)](https://cleancoders.com/episode/agentic-discipline-1)
- [Clean Code for AI Agents — AkitaOnRails](https://akitaonrails.com/en/2026/04/20/clean-code-for-ai-agents/)
- [Skills, Not Vibes: Teaching AI agents to write clean code — dev.to](https://dev.to/gde/skills-not-vibes-teaching-ai-agents-to-write-clean-code-3l9e)
- [So your developers use AI now — Evil Martians](https://evilmartians.com/chronicles/so-your-developers-use-ai-now-here-is-what-to-know)
- [Comparing AI code generation tools on maintainability — GoCodeo](https://www.gocodeo.com/post/comparing-ai-code-generation-tools-on-maintainability-and-readability)
- [Clarity over speed: maintainable code in the AI era — AWS Plain English](https://aws.plainenglish.io/why-i-choose-clarity-over-speed-my-battle-for-maintainable-code-in-the-ai-era-3d0b45a36be3)
