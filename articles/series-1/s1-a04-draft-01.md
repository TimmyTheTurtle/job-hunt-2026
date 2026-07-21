# Why Documentation Fails in AI-Assisted Development
### Draft 1 - expanded working draft / research packet

---

## Working Note

This article should sound like someone who has made both documentation mistakes:

- not enough durable reasoning captured
- far too much unfiltered reasoning captured

The key phrase is already strong and should stay central:

> activity without durable understanding

The new addition from the pivot:

The continuation loop optimizes for output, not promotion of rationale into durable memory.
That is why so much reasoning either never gets written down or gets dumped into the wrong form.

---

## Core Argument

Documentation is not failing because teams are lazy or because documentation is inherently
useless. It is failing because the dominant artifacts were designed for the wrong reader and
the wrong retrieval model.

Human reader assumptions:

- can ask a teammate
- can infer context
- can scan git history
- can live with some ambiguity
- can slowly build a mental model

Agent reader assumptions:

- has only the current context window
- cannot infer missing rationale unless surfaced
- cannot know which of ten notes is canonical unless told
- treats present context as if it were relevant unless filtered

This is why "just write more docs" can make the problem worse.

---

## What The Article Must Prove

1. underdocumentation and overdocumentation are opposite forms of the same failure
2. endless chats and AI-generated handoffs can bury reasoning as effectively as missing docs
3. ADRs work because they capture context, rationale, and consequences compactly
4. the real target is memory architecture, not documentation volume

This article is where the personal through-line of the whole series becomes load-bearing.

---

## Research Spine

### 1. Evil Martians / AGENTS.md as a practical memory artifact

The Evil Martians piece is excellent not because it is academic, but because it shows a real
pattern:

- large style or refactoring knowledge gets compressed into a smaller operational artifact
- the smaller artifact encodes context, use case, rules, and patterns
- the output becomes something a model can actually use

That maps perfectly to this article's claim that the problem is not "write more" but
"write retrievable, operative artifacts."

Source:
- [Vibe coding in style.md](https://evilmartians.com/chronicles/vibe-coding-in-style-dot-md)

### 2. ADRs as the counterexample

AWS gives a practical reason ADRs work:

- they capture context
- they capture alternatives
- they capture rationale

Azure sharpens this further:

- architecture is the accumulation of decisions
- the ADR records how and why the system reached its current shape
- accepted records should not be retro-edited away; superseding records preserve the history

This is excellent material for the article because it supports two points:

1. the "why" matters more than the implementation summary
2. drift history matters, because changed decisions without preserved lineage create confusion

Sources:
- [AWS ADR best practices](https://aws.amazon.com/blogs/architecture/master-architecture-decision-records-adrs-best-practices-for-effective-decision-making/)
- [Microsoft ADR guidance](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record)

### 3. Diminishing returns and the buried-rationale problem

Allan Kelly is useful as a sanity check against documentation maximalism.
The article does not need to become an essay about that blog post, but it helps support the
idea that beyond a point, more documentation can produce less usable understanding.

Source:
- [Documentation: diminishing returns](https://www.allankelly.net/archives/5516/documentation-another-case-of-rapidly-diminishing-returns/)

---

## Personal Through-Line To Use

This is probably the article where first person matters most.

Possible structure:

1. not enough documentation
2. rationale lost
3. repeated rediscovery
4. overcorrection into journals, notes, AI handoffs, lessons
5. now the reasoning exists but cannot be found, trusted, or cheaply re-entered

This is the key sentence:

> I have experienced both failures in sequence, which is why I no longer believe the answer is
> "more documentation."

That makes the article feel earned.

---

## Distinctions To Make Explicit

### Human-facing docs vs agent-facing context

Need a very clean distinction here.

Human-facing:

- tutorials
- broader design prose
- onboarding narrative
- explanatory docs with some redundancy

Agent-facing:

- compact context
- canonical decisions
- stable naming and contracts
- current constraints
- retrieval-friendly artifacts

Important not to oversimplify into "docs for humans bad, docs for agents good."
The real point is that they are different jobs.

### Canonical vs scratch

This probably deserves its own subsection.

Canonical:

- ADRs
- accepted specs
- current architecture notes
- constraints and invariants

Scratch:

- journals
- provisional notes
- brainstorms
- intermediate summaries
- handoff dumps

A lot of AI-assisted development blurs these categories, and that is a big part of the failure.

---

## Counterarguments To Handle

### "We just need better documentation discipline"

Partly true but too vague.
The article should insist that format, audience, and retrievability matter as much as discipline.

### "LLMs can summarize everything, so overdocumentation is fine"

No. Summaries generated from poor or conflicting memory stores can preserve confusion more
efficiently, not eliminate it.

### "ADRs are overhead"

Sometimes. But the point is not to ADR every trivial change.
The point is that meaningful decisions need a durable rationale artifact.

---

## Suggested Structure

1. Open with the missing-rationale pain.
2. Show underdocumentation and overdocumentation as sibling failures.
3. Explain the wrong-reader problem.
4. Use personal sequence to make it credible.
5. Introduce ADRs as the counterexample.
6. Point toward retrieval and memory architecture.

---

## Lines Worth Keeping

- The reasoning was in a chat session that closed six weeks ago.
- What doesn't make it into the context window doesn't exist from the agent's perspective.
- Too little documentation loses the reasoning. Too much unfiltered documentation buries it.
- The problem is not incomplete memory. It is unusable memory.
- Documentation volume is not memory architecture.

---

## Source Pack

Primary practical sources:

- [Vibe coding in style.md](https://evilmartians.com/chronicles/vibe-coding-in-style-dot-md)
- [AWS ADR best practices](https://aws.amazon.com/blogs/architecture/master-architecture-decision-records-adrs-best-practices-for-effective-decision-making/)
- [Microsoft ADR guidance](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record)
- [Documentation: diminishing returns](https://www.allankelly.net/archives/5516/documentation-another-case-of-rapidly-diminishing-returns/)
- [ADR creation practices](https://ozimmer.ch/practices/2023/04/03/ADRCreation.html)

