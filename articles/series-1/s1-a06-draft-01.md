# Context Poisoning
### Draft 1 - expanded working draft / research packet

---

## Working Note

This article is diagnostic again, but now at the memory-layer rather than the workflow-layer.

Need to keep the organic version central.
The security angle is important because it proves the mechanism is real, but the article should
not read like a security scare piece.

Best emotional phrase in the outline:

> the system fighting your intent using your own past thoughts

That line should survive into the finished article.

---

## Core Argument

Once teams start producing lots of AI-generated summaries, scratch notes, handoffs, journals,
and provisional memory artifacts, context itself becomes an attack surface even without an
attacker. Outdated architecture notes, duplicated summaries, stale names, and reversed decisions
can all remain present long after they stopped being true. The agent mirrors what it sees.

This article should make one counterintuitive point feel obvious by the end:

> more context is not always better context

That is the bridge into retrieval architecture.

---

## What This Article Has To Do

1. name organic context poisoning as a normal operational failure mode
2. use XOXO to show that the same mechanism can be weaponized
3. explain why long context can become distracting, conflicting, and unreliable
4. argue for hygiene, expiry, and curation rather than accumulation
5. set up A7 naturally

---

## Research Spine

### 1. XOXO as proof that context itself is a security boundary

The XOXO paper matters because it shows the assistant's automatically gathered context is not
neutral infrastructure. It is part of the prompt, and therefore part of the attack surface.

What I need from it:

- context is gathered from multiple origins
- semantically equivalent adversarial modifications can poison the assistant's outputs
- the attack is hard to spot because the modifications need not look obviously malicious

This is good because it validates the broader article claim:
the agent mirrors its context, including context that should not have been trusted.

Source:
- [XOXO: Stealthy Cross-Origin Context Poisoning Attacks against AI Coding Assistants](https://arxiv.org/abs/2503.14281)

### 2. Long contexts fail in multiple ways

The dbreunig piece is useful because it names more than one failure:

- poisoning
- distraction
- confusion
- clash

That is valuable because it prevents the article from sounding like "one weird trick called
poisoning." The point is broader: long accumulated context can fail in several distinct ways,
all of which argue against brute-force stuffing.

Source:
- [How Long Contexts Fail](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html)

### 3. Retrieval is already the hinted answer

Anthropic's contextual retrieval article is useful here even before A7 because it gives the
positive contrast:

- traditional chunking destroys context
- targeted retrieval and reranking can recover relevance much more effectively

This helps because A6 should end with a need, not with the full solution. But the solution
shape should already be visible.

Source:
- [Introducing Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval)

---

## Organic Poisoning Examples To Use

Need a lot of concrete examples here. The article becomes vivid when the reader recognizes the
failure modes immediately.

Examples:

- ADR says service A is canonical, but service B replaced it three months ago
- architecture note still uses an old subsystem name
- generated summary collapsed two distinct concepts into one
- handoff note preserved a temporary workaround as if it were permanent design
- multiple summaries of the same feature disagree because each was generated at a different time
- tests still encode behavior from a superseded requirement

The general feeling:

the agent is not hallucinating from nowhere.
It is faithfully continuing from stale local truth.

Possible line:

> Poisoning is not always fiction entering the context. Sometimes it is yesterday's truth
> overstaying its authority.

---

## The Janitor Concept

This needs to be presented as a named systems role.

Possible job description:

- detect stale artifacts
- detect duplicate summaries
- detect superseded decisions without links
- detect orphaned notes with no canonical parent
- expire unverified memory
- mark provenance and freshness

This should probably not sound like "clean your docs."
It should sound like a maintenance subsystem for context health.

---

## Counterarguments To Handle

### "Can't we just give the model more context?"

No. This is where the article should be blunt.
More tokens can mean more distraction, more contradiction, and more stale authority.

### "Isn't this just better prompting?"

No. Prompting cannot reliably compensate for a contaminated memory substrate.

### "Security poisoning is rare"

Maybe. But the article's main claim is about organic poisoning anyway.
The security case is there because it shows the mechanism clearly.

---

## Suggested Structure

1. Open with the lived feeling of the system fighting your intent.
2. Define context poisoning in the organic sense.
3. Introduce XOXO as the adversarial mirror.
4. Expand to long-context failure modes more generally.
5. State the "more context is not better context" claim.
6. Introduce the Janitor concept.
7. End by pointing to selective retrieval and curated memory.

---

## Lines Worth Keeping

- Poison in, poison extended.
- Yesterday's truth can become today's contamination.
- The system is fighting your intent using your own past thoughts.
- More context is not always better context.
- Context hygiene is not tidying. It is reliability engineering.

---

## Source Pack

Primary sources:

- [XOXO: Stealthy Cross-Origin Context Poisoning Attacks against AI Coding Assistants](https://arxiv.org/abs/2503.14281)
  Local target when pulled: `articles/papers/arxiv-2503.14281-xoxo-context-poisoning.pdf`
- [How Long Contexts Fail](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html)
- [Introducing Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval)

Supporting links already attached to the outline:

- [Context rot is slowing down your AI agent](https://blog.logrocket.com/context-rot-slowing-down-your-ai-agent-how-fix/)
- [Context poisoning in LLMs](https://www.elastic.co/search-labs/blog/context-poisoning-llm)

