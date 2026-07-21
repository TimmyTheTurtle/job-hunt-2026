# Vibe Coding Without Constraints Is Just Vibe Coding
### Draft 1 - expanded working draft / research packet

---

## Working Note

This is the turn in the series.

After A1 through A4, the reader has heard enough diagnosis. This is where the article stack has
to start feeling constructive. Not optimistic in a fluffy way. Constructive in the sense of:

here is what the alternative operating model actually looks like.

The new central line:

> Constraints are intentional friction.

That is the clean answer to the gamification frame.

---

## Core Argument

If AI coding tools are continuation-optimized systems with weak stopping cues, then the fix is
not moral willpower. The fix is workflow design that makes specification, verification, and
acceptance criteria more rewarding than another blind continuation step.

Constraints are not a tax on speed.
They are the mechanism by which speed becomes trustworthy.

Need to keep saying "trustworthy delivery" instead of generic "quality."

---

## What This Article Has To Do

1. reframe structure as friction in service of trustworthy delivery
2. show that the same model behaves differently under explicit constraints
3. connect clean-code ideas to context-window realities without becoming dogmatic
4. introduce mini-V discipline as light structure, not bureaucracy
5. mention enforceable hooks as architecture, not aspiration

This piece should read like a practical systems article, not a manifesto.

---

## Research Spine

### 1. Agile V as the formal backbone

The Agile V paper is valuable because it makes explicit what most AI-assisted workflows lack:

- task-level verification
- regulatory traceability
- independent verification
- audit artifacts generated as part of the cycle
- human approval gates

The article does not need to make a compliance-heavy argument, but it does need to borrow the
key idea:

the development loop should have a left side and a right side.

Source:
- [Agile V: A Compliance-Ready Framework for AI-Augmented Engineering -- From Concept to Audit-Ready Delivery](https://arxiv.org/abs/2602.20684)

### 2. Clean AI / clean code for agents

The point is not to submit to authority. The point is to note that some principles have changed
status:

- function size is no longer only a readability preference
- boundedness and atomicity now affect whether the agent can work locally and reliably
- naming consistency becomes a context-management requirement

AkitaOnRails is useful because it is closer to the actual developer argument than a pure theory
piece. Uncle Bob is useful because he articulates the "discipline didn't disappear" point.

Sources:
- [Clean Code for AI Agents](https://akitaonrails.com/en/2026/04/20/clean-code-for-ai-agents/)
- [Clean AI: Agentic Discipline](https://cleancoders.com/episode/agentic-discipline-1)

### 3. Guardrails and hooks

This is the first place where automation should become concrete.
The real claim is not "people should remember constraints."
The claim is "the workflow should enforce them where possible."

That makes hooks important because they shift discipline from preference to infrastructure.

Supporting links:

- [Building guardrails for AI coding assistants](https://www.linkedin.com/posts/lanemik_building-guardrails-for-ai-coding-assistants-activity-7418782309803544576-oSVd)
- [Hooks: how to put guardrails on your AI coding assistant](https://dev.to/rajeshroyal/hooks-how-to-put-guardrails-on-your-ai-coding-assistant-4gak)

---

## The Article's Main Conceptual Move

Need a clean distinction between:

- generation speed
- trustworthy delivery rate

That is probably the most reusable line in the piece.

Possible paragraph:

Unconstrained generation looks fast because it optimizes for local output. But the metric that
actually matters is how quickly a team can produce something it can ship, explain, debug,
maintain, and safely extend. Once that is the metric, constraints stop looking like delay and
start looking like acceleration of the right kind.

Need a second distinction alongside that one:

- exploration constraints
- ownership constraints

Exploration constraints should be minimal enough not to kill discovery.
Ownership constraints should be explicit enough that the team knows when the artifact is allowed
to survive.

That may be the cleanest callback to A1:

the phase changed, so the acceptable friction changed.

---

## Mini V Per Feature

This needs to be concrete enough that the article does not sound abstract.

Possible simple structure:

Left side:

- behavior to implement
- invariants to preserve
- constraints not to violate
- tests or evals to satisfy

Right side:

- generated implementation
- verification
- review artifact
- acceptance decision

This can be sold as lightweight because it is local.
The reader does not have to buy a full methodology religion.

Need an even more concrete example because otherwise "mini V" can still sound airy.

Possible example skeleton:

Prompting an agent with only:

- "add retry support to this service"

versus prompting with:

- retry only idempotent operations
- maximum three attempts
- preserve existing timeout budget
- never retry authorization failures
- add tests for transient 5xx and timeout paths
- update the decision note if the retry contract changes externally visible behavior

The point is not that the second prompt is verbose. The point is that it gives the model a
verifiable target and gives the human a basis for acceptance.

Possible line:

> A vague prompt asks for code. A constrained prompt asks for behavior inside a boundary.

---

## Where Enforcement Has To Become Infrastructure

This section likely needs to be stronger than it is now.

Human teams are bad at repeatedly remembering soft rules inside fast feedback loops.
That is exactly why gameful systems are powerful: they keep cueing the next move.

Therefore the practical lesson is:

- what matters enough to insist on should be enforceable where possible
- what is only written as preference will lose to the continuation loop surprisingly often

This is where hooks, repo policies, protected paths, required tests, or pre-tool-use checks stop
being fancy extras. They become the way the team makes the desired workflow more automatic than
the undesired one.

Possible line:

> In a continuation-friendly system, unenforced discipline is usually just a wish.

---

## Important Tone Guardrail

Do not let this become anti-exploration.

The message is not:

"Never vibe code."

The message is:

"Once the phase changes, the workflow has to change too."

Possible line:

> Exploration needs low friction. Ownership needs the right friction.

Need to maybe add:

> The point is not to make exploration feel like compliance. The point is to stop shipping
> exploratory behavior by accident.

---

## Counterarguments To Handle

### "Constraints kill the magic"

Answer:

They kill the wrong kind of magic: accidental plausibility mistaken for trustworthy delivery.

### "This sounds like heavyweight process"

Answer:

The article is explicitly advocating local structure, not corporate ceremony.

### "Great developers can do this informally"

Answer:

Sometimes, but the whole point of the series is that AI systems amplify whatever is implicit.
What is not externalized does not reliably survive delegation.

### "The best models already infer constraints"

Sometimes they infer them. That is not the same as being bound by them.
Inferred constraints are probabilistic. Declared constraints are testable. Enforced constraints
are operational.

---

## Suggested Structure

1. Open by naming the wrong objection.
2. Define trustworthy delivery as the metric.
3. Explain constraints as intentional friction.
4. Show how prompts change under explicit requirements and invariants.
5. Introduce mini V per feature with one concrete before/after example.
6. Introduce hooks and enforcement infrastructure.
7. Distinguish inferred constraints from declared and enforced ones.
8. Point to A6: even good constraints fail if context itself rots.

---

## Lines Worth Keeping

- Constraints are intentional friction.
- The problem is not that structure slows generation. The problem is that unstructured generation
  slows trustworthy delivery.
- Exploration needs low friction. Ownership needs the right friction.
- Some practices that were once style preferences become reliability requirements under delegation.
- What the workflow does not enforce, the continuation loop will usually bypass.
- A vague prompt asks for code. A constrained prompt asks for behavior inside a boundary.
- In a continuation-friendly system, unenforced discipline is usually just a wish.

---

## Source Pack

Primary sources:

- [Agile V: A Compliance-Ready Framework for AI-Augmented Engineering -- From Concept to Audit-Ready Delivery](https://arxiv.org/abs/2602.20684)
  Local target when pulled: `articles/papers/arxiv-2602.20684-agile-v-koch-wellbrock.pdf`
- [Clean Code for AI Agents](https://akitaonrails.com/en/2026/04/20/clean-code-for-ai-agents/)
- [Clean AI: Agentic Discipline](https://cleancoders.com/episode/agentic-discipline-1)

Supporting sources:

- [Systems engineering life-cycle overview](https://ops.fhwa.dot.gov/seits/sections/section2/2_7.html)
- [Building guardrails for AI coding assistants](https://www.linkedin.com/posts/lanemik_building-guardrails-for-ai-coding-assistants-activity-7418782309803544576-oSVd)
- [Hooks: how to put guardrails on your AI coding assistant](https://dev.to/rajeshroyal/hooks-how-to-put-guardrails-on-your-ai-coding-assistant-4gak)
