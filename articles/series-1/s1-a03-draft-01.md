# I Shipped More and Felt Worse
### Draft 1 - expanded working draft / research packet

---

## Working Note

This needs to stay personal without becoming melodramatic.

The key upgrade from the older frame:

Do not make this article mainly about doomscrolling or burnout in the generic sense.
Make it about competence-signal erosion inside a gamified work system.

The phrase to keep returning to:

> reward without mastery

That is the whole article.

The system keeps paying out visible signs of progress:

- tasks completed
- files changed
- tests passing
- diffs landing
- plans advancing

But those rewards are no guarantee that understanding is accumulating at the same rate.
That gap is what starts to feel bad.

---

## What This Article Has To Do

1. distinguish this feeling from ordinary deadline fatigue
2. name the gap between output rate and understanding rate
3. use the empirical papers to show that the feeling is not imagined
4. argue that cognition itself needs protection as an engineering asset
5. introduce the review-artifact idea that later supports A4

This article is probably the emotional center of Series 1.
If A1 is the diagnosis of the system and A2 is the first structural consequence, A3 is where
the reader says "yes, that is what this feels like."

---

## Core Argument

The problem is not that AI assistance reduces effort.
The problem is that it can preserve the feeling of movement even when the competence signal is
decaying.

Engineering normally has a built-in meaning loop:

- I understand the thing
- I change the thing
- the thing behaves differently
- that reinforces my sense of competence

Heavy AI offloading can break that loop:

- I request the change
- the thing changes
- I verify some surface behavior
- but I do not feel ownership of the understanding

That is why the article title works. It is not "I shipped less and felt worse."
The paradox is the point.

Need one stronger formulation here:

Engineering usually contains its own proof-of-work. If I can implement, debug, extend, and
explain the thing, I know I understand it. Heavy AI assistance can counterfeit that proof-of-work
with surface proxies: a merged diff, a closed ticket, a passing run, a successful demo. Those
signals are not meaningless. They are just not the same thing as ownership of understanding.

That may be the best way to frame the hurt in this article:

the loop keeps paying out competence-shaped rewards that are no longer tightly coupled to
competence itself.

Possible line:

> The system can now simulate the feeling of fluency faster than it builds fluency.

---

## The Structural Difference From Ordinary Burnout

Need an explicit section on this, because otherwise the piece risks sounding like a productivity
or wellness article.

Ordinary deadline burnout:

- too much work
- too little recovery
- obvious overload
- often improved by rest, staffing, scope reduction, or deadline relief

This pattern:

- can occur even when the day feels "productive"
- often includes lower friction in the moment, not higher
- creates ambiguity about whether the problem is effort, quality, or understanding
- does not disappear just because the immediate workload was lighter

That distinction matters. The article is not claiming that AI makes work feel harder in every
moment. In many moments it makes work feel easier. The problem is what that easier feeling does
to schema formation, corrective competence, and long-term confidence.

Possible line:

> This is not only exhaustion. It is a mismatch between visible progress and retained ability.

---

## Research Spine

### 1. METR as the perception-reality shock

The Becker/Rush/Barnes/Rein paper is essential because it gives you the perception gap in one
clean result:

- 16 experienced developers
- 246 real tasks
- developers expected about 24% faster before the study
- estimated about 20% faster after using the tools
- actual result: 19% slower

This is the number that lets you say the feedback signal is compromised.

Source:
- [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://arxiv.org/abs/2507.09089)

### 2. Comprehension debt as the vocabulary of the feeling

Ahmad gives you the mechanism names:

- black-box acceptance
- context mismatch
- dependency-induced atrophy
- verification bypass

Most important for this article:

Comprehension debt is not ordinary technical debt because it lives in collective cognition.
That is the exact reason refactoring alone does not fix the feeling.

Source:
- [Comprehension Debt in GenAI-Assisted Software Engineering Projects](https://arxiv.org/abs/2604.13277)

### 3. Vibe-Check as the conceptual divider

The acceleration vs offloading distinction is probably the cleanest conceptual tool for the
entire middle of the series.

Acceleration:

- AI helps me go faster
- I still understand the work

Offloading:

- AI substitutes for understanding itself
- I can still get output
- my corrective competence decays

That distinction belongs here in a very central way.

Source:
- [The Vibe-Check Protocol: Quantifying Cognitive Offloading in AI Programming](https://arxiv.org/abs/2601.02410)

### 4. Fast and Forgettable as the memory/retention warning

Useful because it adds another dimension:

- lower subjective workload in the AI condition
- better short-term performance
- worse downstream retention trend

That is exactly the pattern this article wants.
The system feels easier and may even be easier in the moment. The concern is what remains after.

Source:
- [Fast and Forgettable: A Controlled Study of Novices' Performance, Learning, Workload, and Emotion in AI-Assisted and Human Pair Programming Paradigms](https://arxiv.org/abs/2604.18538)

### 5. Epistemic debt / metacognitive friction

The Sankaranarayanan paper is useful because it gives you a constructive angle:

- unrestricted AI can produce fragile competence
- scaffolded AI with explanation gates preserves more capability

This gives the article permission to end constructively:
the answer is not abstinence. The answer is friction that forces active reasoning back into the
loop.

Source:
- [Mitigating "Epistemic Debt" in Generative AI-Scaffolded Novice Programming using Metacognitive Scripts](https://arxiv.org/abs/2602.20206)

### 6. Oversight work is its own form of strain

Need to use the oversight/enterprise papers more explicitly so the article does not lean only on
student learning studies.

Two helpful ideas from the newer workplace-oriented material:

- oversight itself becomes work: checking, steering, validating, and deciding when to trust
- that work has a different cognitive profile from ordinary implementation

This helps explain why the experience can feel strangely depleting even in sessions where a lot
got done. The engineer is not only building. They are arbitrating a stream of plausible outputs.

Useful supporting sources:

- [Human oversight of agentic systems in practice](https://arxiv.org/abs/2606.05391)
- [Usage, Effects and Requirements for AI Coding Assistants in the Enterprise](https://arxiv.org/abs/2601.20112)

---

## The Wait-Time Attention Problem

This is one of the most original ideas in the article plan and should stay.

The key asymmetry:

- agent wait time is measured in minutes
- attention recovery from context switching is much longer

The risk is that every agent run creates a tiny invitation to do one of two bad things:

1. stare passively at progress
2. context-switch into something else and pay the recovery cost

This section becomes much stronger if it is tied to the rest of the architecture:

review artifacts turn wait time into review time.

That is a huge point.

Without artifacts, wait time is dead time.
With artifacts, wait time becomes the human gate.

That sentence probably belongs near the end:

> The pause is not where productivity stops. The pause is where understanding re-enters.

Need a sharper connection to the rest of the article:

If every agent run creates either passivity or a context switch, then wait-time discipline is
not a tiny productivity hack. It is part of cognitive architecture. The whole system either
protects active reasoning during the pauses or quietly trains the engineer to become a reviewer
of outputs they did not construct.

---

## Personal Material To Lean Into

This article has permission to be more autobiographical than the others.

Keep:

- morning math / vector work / calculus / physics before tools come on
- the idea that active reasoning needs deliberate protection
- the walk
- the rotation model
- lesson-first, build-second

Need to present these not as universal wellness advice, but as engineering countermeasures.

The tone should be:

I noticed something real degrading, so I changed my practice to defend the cognitive layer.

Possible line:

> If AI can cheaply simulate the feeling of progress, then I need at least one daily practice
> that cannot be faked by progress theater.

Need one more concrete articulation of the "lesson-first, build-second" move.

The useful claim is:

- if the model explains a concept and I then rebuild it from scratch, the build is the
  comprehension check
- if the model simply hands me the finished artifact, I can falsely believe I learned because
  I recognized the steps while watching them happen

Recognition is not recall. Recall is not implementation. Implementation under mild adversity is
closer to competence.

---

## Counterarguments To Address

### "This is just resistance to new tools"

No. The article should explicitly say acceleration is real and useful.
The objection is not to assistance. It is to assistance that replaces schema formation.

### "Professionals are different from students"

Yes, but not immune.

Use the student papers for mechanism and the METR paper for experienced-developer calibration.
The combination matters.

### "If the code works, why does this matter?"

Because engineering is not only code emission. It is future change under uncertainty.
The capability that matters shows up later, under maintenance, extension, debugging, and failure.

---

## Suggested Structure

1. Confession in the title and opening paragraph.
2. Name the paradox: more output, less competence signal.
3. Drop METR and the perception gap.
4. Bring in comprehension debt and acceleration vs offloading.
5. Add Fast and Forgettable / epistemic debt.
6. Add the oversight-work explanation so the article covers the professional setting better.
7. Turn to the wait-time attention problem.
8. Offer the personal counter-moves.
9. End by pointing toward review artifacts and the documentation article.

---

## Lines Worth Keeping

- Reward without mastery.
- The output arrived. The understanding did not.
- This is not deadline burnout. It is competence erosion.
- If the assistant keeps closing loops for me, I stop strengthening the part that closes loops.
- The pause is where understanding re-enters.
- The system can simulate the feeling of fluency faster than it builds fluency.

---

## Source Pack

Primary papers from the Series 1 corpus:

- [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://arxiv.org/abs/2507.09089)
  Local target when pulled: `articles/papers/arxiv-2507.09089-metr-productivity-rct.pdf`
- [Comprehension Debt in GenAI-Assisted Software Engineering Projects](https://arxiv.org/abs/2604.13277)
  Local target when pulled: `articles/papers/arxiv-2604.13277-comprehension-debt.pdf`
- [The Vibe-Check Protocol: Quantifying Cognitive Offloading in AI Programming](https://arxiv.org/abs/2601.02410)
  Local target when pulled: `articles/papers/arxiv-2601.02410-vibe-check-protocol.pdf`
- [Fast and Forgettable: A Controlled Study of Novices' Performance, Learning, Workload, and Emotion in AI-Assisted and Human Pair Programming Paradigms](https://arxiv.org/abs/2604.18538)
  Local target when pulled: `articles/papers/arxiv-2604.18538-fast-and-forgettable.pdf`
- [Mitigating "Epistemic Debt" in Generative AI-Scaffolded Novice Programming using Metacognitive Scripts](https://arxiv.org/abs/2602.20206)
  Local target when pulled: `articles/papers/arxiv-2602.20206-mitigating-epistemic-debt.pdf`

Additional series-attached sources:

- [Usage, Effects and Requirements for AI Coding Assistants in the Enterprise: An Empirical Study](https://arxiv.org/abs/2601.20112)
- [Human oversight of agentic systems in practice](https://arxiv.org/abs/2606.05391)
- [Walking the Tightrope of LLMs for Software Development: A Practitioners' Perspective](https://arxiv.org/abs/2511.06428)
