# S3-A2 — Experimentation IS Requirements Gathering (But Only If You Do It Like a Scientist)

**Status:** Not started
**Series position:** 2 of 3

---

## Voice and Tone

- **Register:** the title already has the voice — direct and slightly sharp. "But Only If You
  Do It Like a Scientist" is the edge that keeps this from being a vibe coding apologia. Carry
  that tone into the article. The distinction between disciplined experimentation and enthusiasm
  without a plan is the article's moral center.
- **The "kid with a chemistry set" line from the thesis is good.** Keep it. It is specific
  enough to be funny without being mean.
- **Jobs to Be Done and the observed-vs-stated distinction** should be introduced as
  practitioner knowledge, not academic citation. Name the framework, move on.
- **First person on the failure mode.** Workshops that produce requirements nobody actually
  uses — this is a universal experience. Own it. "I have sat in those workshops" is the
  sentence that makes the rest of the article land.
- **Do not allow this article to sound like a methodology.** It is an argument about what
  requirements actually are, derived from experience. The scientist framing is the discipline
  check, not a process prescription.

---

## Thesis

The traditional requirements process — elicit, specify, validate, then build — assumes you can
know what a system should do before seeing it. Decades of software delivery evidence says
otherwise: stakeholders don't know what they want until they see what they don't want.

In the AI age, building a throwaway proof of concept may now be cheaper than writing a
thorough requirements specification. The prototype reveals requirements that no amount of
interviews and workshops would have surfaced. "Build it to find out what it should be" has
become economically viable for the first time.

The critical distinction: this is not a defense of vibe coding. The difference between
disciplined experimentation-as-requirements-discovery and vibe coding is the same as the
difference between a scientist and a kid with a chemistry set. One has a hypothesis, capture
criteria, and exit conditions. The other has enthusiasm and no plan.

---

## Key Claims

- Requirements cannot be fully specified before building — they emerge from contact with
  a working system
- Observed behavior reveals requirements better than stated preferences (Jobs to be Done)
- In the AI age, prototyping cost dropped below specification cost for many problem types
- Disciplined experimentation produces structured findings that become formal requirements
- The experiment-requirement-candidate is the artifact that bridges experiment to specification
- This is not vibe coding: the discipline is what makes the difference

---

## The Requirements Discovery Problem

Traditional requirements elicitation has a fundamental epistemological problem: you're asking
stakeholders to specify what they want from a system they've never seen. The gap between
"what people say they want" and "what people actually need when they use the thing" is the
source of most product failures.

Clayton Christensen's Jobs to be Done framework addresses this obliquely: focus on the job
the customer is trying to do, not the features they request. But even JTBD still operates
in the pre-build phase. It makes better requirements, but requirements nonetheless.

Rita McGrath's Discovery-Driven Planning goes further: convert assumptions to knowledge
through structured experiments before committing resources. But it was designed for a world
where experiments were expensive — so you ran a few carefully chosen ones.

## What Experimentation Adds That Specification Cannot

A working prototype, even a bad one, reveals:
- What interactions are confusing that seemed obvious on paper
- What edge cases exist in the domain that no stakeholder mentioned
- What the system is surprisingly good at that wasn't in the spec
- What is unexpectedly hard to build, which changes the cost structure
- What users actually do vs. what they said they'd do

None of these are available before the prototype exists. All of them are requirements.

## The Disciplined Version

The undisciplined version: build things, observe loosely, absorb some vague impressions,
build more things. This is vibe coding applied to product discovery. The impressions don't
accumulate into anything.

The disciplined version:

1. **State the hypothesis before building**: "I believe contractors will describe windows
   in trade-language dimensions + configuration terms, not UI navigation terms"
2. **Define exit criteria**: what observation would confirm or refute the hypothesis?
3. **Build the minimum thing that could answer the question** — not a product, an answer
4. **Record the outcome explicitly**: what happened, what was surprising, what was revealed
5. **Formalize the finding as a requirement** before it disappears into memory

Step 5 is what makes the experiment a requirements artifact rather than a learning that
evaporates. This is the experiment-requirement-candidate pattern from Sandbox 005.

## The Pre-V Phase

The V-model starts with requirements at the top-left. But if experimentation produces the
requirements, you need a phase that precedes the V — a disciplined exploration layer that
feeds into the formal process.

This is not a weakness of the V-model. It's a recognition that for novel problems, you
cannot specify requirements without first running experiments. The exploration phase ends
when the experiment history has produced enough confirmed hypotheses to populate the left
side of the V with confidence. Then the formal process begins.

---

## Concrete Example — Watershed WFC Encounter Design

Watershed (D3D12 puzzle game) is the article's worked example for the disciplined version of
experimentation-as-requirements-discovery.

**The experiments:** Four named throwaway renderers (grass-field-001 through 004) answered a
specific question: can the column raycast approach produce the visual feel a water-control
puzzle needs? Each was bounded. Each was disposable. Each produced a finding. They are not
in-progress work — they are closed experiments with outcomes.

**The crystallized requirements output:** `experiments/scalar-field-flooding/future-wfc-encounter-notes.md`
is the direct artifact. A formal design for the WFC encounter generation pipeline:
- WFC layer for spatial coherence (tile placements obey adjacency rules)
- Scalar field layer for per-move simulation (water flow, pressure, drainage)
- Discrete solvability model (Physical state / Puzzle state / Safety state) as a hard reject gate
- Encounter generation pipeline: WFC → anchor placement → scalar field init → abstract
  puzzle state → branch simulation → reject dead seeds → score survivors

This document could not have been written before the experiments. The WFC + scalar field
combination was not chosen because it sounded good. It was chosen because the grass-field
experiments revealed what the physics model needed to do, and WFC was the spatial coherence
mechanism that survived contact with those constraints.

**The experiment-requirement-candidate pattern in practice:**
- Hypothesis: WFC can produce spatially coherent layouts that scalar field simulation can
  resolve into meaningful puzzle states without human review of each result
- Exit criteria: solvability model rejects dead seeds automatically
- Finding: yes — anchor placement is the required bridge between the spatial and simulation layers
- Formalized requirement: the encounter generation pipeline as specified in the notes

**Why this works for S3-A2:** The article's core claim is that disciplined exploration looks
different from vibe coding — you can audit the difference. Watershed is the worked case: the
grass-field experiments (bounded hypothesis tests) and the WFC notes (formal requirements
output) are both in the repo. The experiment history is readable. The requirement that came
out of it is specific and falsifiable.

---

## Sources

- [Discovery-Driven Planning — McGrath & MacMillan, HBR 1995](https://hbr.org/1995/07/discovery-driven-planning)
- [A Refresher on Discovery-Driven Planning — HBR 2017](https://hbr.org/2017/02/a-refresher-on-discovery-driven-planning)
- [Jobs to Be Done — Christensen Institute](https://www.christenseninstitute.org/theory/jobs-to-be-done/)
- [Clay Christensen's Jobs to Be Done Framework — FullStory](https://www.fullstory.com/blog/clayton-christensen-jobs-to-be-done-framework-product-development/)
- [Hypothesis-Driven Development — Barry O'Reilly](https://barryoreilly.com/explore/blog/how-to-implement-hypothesis-driven-development/)
- [Hypothesis-Driven Development — Statsig](https://www.statsig.com/perspectives/hypothesisdrivendevelopment)
- [Hypothesis-driven development: building with experimentation — Harness](https://www.harness.io/harness-devops-academy/hypothesis-driven-development)
- [Amazon Working Backwards PR/FAQ Process](https://workingbackwards.com/concepts/working-backwards-pr-faq-process/)
- [Amazon Working Backwards — Product Frameworks](https://www.product-frameworks.com/Amazon-Working-Backwards.html)
- [Pre-Mortem: Preventing Product Failure — Scrum.org](https://www.scrum.org/resources/blog/pre-mortem-preventing-product-failure-it-strikes)
- [Pre-Mortem: Working Backwards in Software Design — PayPal Tech](https://medium.com/paypal-tech/pre-mortem-technically-working-backwards-1724eafbba02)
- [Software Prototyping — Wikipedia](https://en.wikipedia.org/wiki/Software_prototyping)
- [Throwaway vs Evolutionary Prototyping — Medium](https://medium.com/@pavithrajayasinghe9529/throwaway-prototyping-vs-evolutionary-prototyping-8302be3baf33)
