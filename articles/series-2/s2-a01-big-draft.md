# TDD Doesn't Work for Non-Deterministic Systems (And What Does)
### Big Draft - expanded working draft

---

## Working Note

This is a deliberately oversized working draft.

It is not trying to sound finished. It is trying to make the whole argument available in one
place so I can later cut it down into something much tighter. That means redundancy on purpose:
multiple framings of the same idea, spare transitions, stronger and softer phrasings of the
thesis, extra bridges to later articles, and more examples than I will probably keep.

This draft has to do several jobs:

- make the title-level claim feel earned rather than clicky
- explain exactly which assumptions classical TDD depends on
- show why those assumptions break for non-deterministic LLM behavior
- preserve the important nuance that constrained nodes can still support contract testing
- distinguish evals, invariants, and human review instead of flattening them into one thing
- set up S2-A2 and S2-A8 without stealing their full territory

The tone should stay technical and calm. The point is not "TDD is obsolete." The point is that
deterministic testing habits do not map cleanly onto stochastic systems, and pretending they do
creates false confidence.

---

TDD is not a moral ritual. It is a fit-for-purpose method.

That is a useful place to start because it makes the whole article less defensive. Too many
arguments about TDD become identity arguments. People hear "TDD doesn't work here" as "the old
discipline was fake," or "the new tools have broken software engineering," or "engineers should
just accept probabilistic mush and stop asking for rigor." None of those are the argument I want.

TDD worked because it matched the shape of the systems it was testing.

You write a failing test. You implement the smallest change that makes it pass. You refactor
under the safety of a test suite that can rapidly tell you whether behavior regressed. The loop
works because the thing under test is expected to behave consistently enough that a pass means
something stable and a fail points toward something actionable.

That method carries a few hidden assumptions:

- same input, same output
- pass/fail is meaningful at the unit boundary
- feedback is fast and cheap enough to run constantly

Those assumptions often hold in conventional software.

They break in interesting ways for LLM systems.

Once they break, the question is no longer "why are the tests awkward?" The question becomes
"what kind of confidence structure replaces them?"

That is the actual article.

---

## The Three Broken Assumptions

There are three assumptions beneath classical TDD that matter here.

### 1. Determinism

The red-green-refactor loop assumes that a failing test can be made to pass in a repeatable way.
The same code, under the same conditions, should produce the same observable result. That does
not mean all software is metaphysically simple. It means the unit being tested is stable enough
that an assertion is a reliable boundary.

LLM systems violate that assumption immediately.

The same prompt can produce materially different outputs across runs. The variance may be small
or large depending on model, temperature, decoding strategy, context, and task shape, but the
variance exists. That matters because a single passing output is not the same thing as a stable
behavioral guarantee. You can get an apparently correct answer once and still have no durable
evidence that the system is now "fixed."

### 2. Binary correctness

Classical TDD also assumes that correctness can be expressed as a boolean often enough to make
the loop work. The function either returns the right value or it does not. The parser either
accepts valid input or rejects invalid input. The query either produces the expected structure
or fails.

LLM outputs often do not fit cleanly into that shape.

Many tasks are rubric-based rather than exact-match. The answer may be more or less faithful,
more or less complete, more or less grounded, more or less safe, more or less aligned with a
business need that is itself not reducible to one string comparison. Sometimes there are many
acceptable outputs. Sometimes there are outputs that are locally plausible but globally wrong.
Sometimes the "correct" answer is actually a distribution of acceptable behavior.

### 3. Fast cheap feedback

TDD also depends on cost structure. The loop is practical because tests are cheap enough to run
constantly. Red. Green. Refactor. Repeat. The cadence matters. You are not waiting for a
committee or a quarterly evaluation cycle. The feedback is fast enough to shape how you write
the code.

LLM evaluations are often slower and more expensive. They may require datasets, multiple runs,
statistical aggregation, human adjudication, or a judge model whose own variance has to be
managed. They are not always suitable for "every keystroke" confidence. Even when the runtime is
acceptable, the interpretation is not always automatic. A drop from 87% to 79% accuracy is not
the same as a failed unit test that points to line 42.

That is why the replacement cannot simply be "TDD but with more AI."

The shape of the system changed. The confidence method has to change too.

---

## What The Title Really Means

The title says TDD doesn't work for non-deterministic systems. That is intentionally blunt, but
the real claim is slightly more precise:

> Classical red-green-refactor breaks at the orchestration layer of stochastic systems because
> the unit under test is no longer a deterministic function with a binary truth condition.

That is the strong form.

The weaker and probably more readable form is:

> TDD is excellent for deterministic components. It is insufficient as the main confidence
> architecture for systems whose behavior is probabilistic.

Both are saying the same thing. The second version may be easier to publish if the first feels
too headline-shaped, but I want the stronger version in the working draft because the article
needs some spine.

The important thing is not to overgeneralize. Not every part of an AI application is equally
non-deterministic. Plenty of surrounding software is ordinary software:

- data validation
- schemas
- business rules
- orchestration state handling
- retry logic
- tool wrappers
- post-processing
- storage
- authorization
- cache policy

All of that can still be tested conventionally.

The friction point appears where model behavior itself becomes part of the unit under test.

If the system's value depends on a probabilistic generation step, then a single green test is no
longer enough to justify confidence. You need aggregate evidence, distributional thinking, or
explicit behavioral invariants that survive variation.

That is why the article should probably say:

TDD did not fail.
The problem escaped TDD's native geometry.

I like that line because it avoids needless culture war energy. Methods fit shapes. We changed
the shape.

---

## The Important Nuance: Not Every LLM Boundary Is Untestable

This is the nuance that makes the article more useful than a simple "evals replace tests"
piece.

A tightly constrained LLM node is not the same thing as an unconstrained multi-step agent.

If I have a narrow model call with:

- a fixed prompt shape
- a well-defined task
- schema-bound output
- a small behavioral surface
- explicit business invariants

then I may be able to test that node with something much closer to contract testing than to
open-ended evaluation.

This is where the "TDD doesn't work" claim has to be scoped carefully.

It is too broad to say all LLM calls are untestable in a red-green style. That is not true. A
schema-bound node with fixed output structure and explicit invariants can absolutely support
failing assertions before implementation. The assertion just is not "exact string equals X." It
is closer to:

- output conforms to schema
- output satisfies business logic invariants
- forbidden fields are absent
- required constraints are preserved
- downstream tool boundary remains valid

That is not classical pure-function TDD, but it is still test-first work at the contract layer.

This nuance matters for two reasons.

First, it keeps the article honest. We are not arguing that every stochastic boundary is a black
box that can only be observed statistically from a distance.

Second, it creates a clean architecture distinction:

- **constrained nodes** can often be contract-tested
- **orchestration behavior** still needs evals, invariants, and human interpretation

That distinction is probably one of the most valuable ideas in the whole piece because it moves
the conversation from methodology tribalism to system design. If you want more of your system to
be cheaply testable, design more of its edges as constrained nodes.

Now the testing conversation becomes architectural rather than theological.

LMQL helps here because it shows that structured or grammar-constrained decoding can reduce
variance significantly on certain classes of tasks. It does not make the model deterministic in a
strong sense, but it narrows the output space enough that deterministic validation becomes more
meaningful. Record & Replay is also useful because it frames constrained workflows plus check
functions as a way of restoring trust anchors in uncertain systems.

That is the right level of claim:

constraints do not remove uncertainty; they give uncertainty a smaller field in which to move.

And once the field is small enough, contract assertions become useful again.

This probably belongs in the final piece almost verbatim:

> The testable unit is not "the model output string." The testable unit is the contract:
> schema conformance plus business invariant.

---

## The Real Replacement Is Layered

One reason people get confused here is that "evals" gets used as if it names one thing. It does
not. In practice a serious confidence architecture for LLM systems usually needs at least three
layers:

1. deterministic checks
2. orchestration invariants
3. statistical evals

And then, above all three:

4. human interpretation

### Layer 1: deterministic checks

These are the parts that still feel closest to classical testing:

- schema validation
- output parsing
- contract checks
- business-rule assertions
- tool-call shape validation
- safety filters
- policy checks expressible as code

If your model output is structured and narrow enough, a surprising amount can still live here.
This is where property-based contract testing for constrained nodes belongs.

### Layer 2: orchestration invariants

This is where the system starts behaving more like an agentic workflow and less like a single
function. Some things must remain true regardless of the specific path:

- no forbidden side effects
- no out-of-scope tool usage
- state transitions remain valid
- schemas remain valid at every boundary
- retry counts stay within policy
- resource limits are respected
- terminal conditions are well defined

These are not "accuracy" metrics in the soft sense. They are behavioral boundaries. They are
closer to system safety rails.

### Layer 3: statistical evals

Now we are in evaluation proper: curated datasets, repeated runs, rubric-based scoring, accuracy
or pass-rate distributions, confidence intervals, regressions across versions, judge-model
assessments, human-labeled comparisons, and so on.

This layer exists because the thing you care about cannot be fully collapsed into one
deterministic assertion. You are measuring behavior across samples, not proving a single run.

### Layer 4: human interpretation

This is the layer people keep wanting to automate away, and it is the one the article needs to
defend most clearly.

A metric shift is a signal, not a verdict.

If accuracy drops from 87% to 79%, that does not automatically tell you what changed, whether the
change is acceptable for the product context, whether the dataset is representative, whether the
failure cluster matters commercially, or whether a narrower model should still be deployed
because latency, cost, or policy constraints dominate the decision.

Someone has to interpret the meaning of the number.

That is why I want the article to say:

> You can automate the running of evals. You cannot automate the interpretation.

That feels like a sentence worth keeping.

---

## Why LLM-As-Judge Helps And Still Doesn't Solve It

LLM-as-judge is the perfect example of something that is real, useful, and still frequently
misunderstood.

It absolutely does help.

If you have 100,000 outputs to triage, a judge model can collapse the initial review burden from
weeks of human reading to something operationally manageable. It can rank, filter, cluster, and
surface likely failures. It can apply a rubric more consistently than a sleepy intern at 2 AM. It
can make large-scale iteration economically possible in the first place.

That is a real gain.

The mistake is treating that gain as if it were equivalent to verification.

Judge models inherit the same family of issues as the systems they are judging:

- variance
- prompt sensitivity
- rubric ambiguity
- correlation bias with the model under evaluation
- hallucinated rationale
- weak grounding in real product consequence

If a judge says the answer is "good enough," what exactly has been proven? Usually not as much
as people want to think. A judge is another model applying a rubric. That can be useful. It is
not the same as ground truth.

This is where the article should probably be very direct:

LLM-as-judge is triage.
It is not truth.

That is not a dismissal. It is a boundary.

Good judge workflows can:

- reduce human reading load
- make trend shifts visible
- surface likely failures
- provide directional signals for experimentation
- support ranking and comparison across variants

They cannot:

- make stochastic outputs deterministic
- substitute for real-world acceptance criteria
- settle ambiguous business tradeoffs by themselves
- prove correctness in the classical TDD sense

The more clearly the article says both sides at once, the more credible it will feel.

One phrasing to keep:

> Judge models are valuable because they make evaluation scalable. They are dangerous when their
> scalability is mistaken for authority.

That sounds right.

---

## The AgentAssay Lesson

AgentAssay is helpful because it pushes the conversation away from naive deterministic thinking
and toward statistical confidence with bounded cost.

The paper's real contribution for this article is not a specific tooling recommendation so much
as a shift in semantics. It says, effectively: if behavior is probabilistic, then regression
testing should reason in probabilistic terms. Sequential hypothesis testing is useful because it
lets teams reach confidence using fewer runs than brute-force repetition, which matters when evals
are expensive.

This belongs in the article because it shows what a serious replacement looks like. The answer to
stochastic behavior is not despair. It is a different testing language.

Not:

- "the test passed once"

But:

- "the system meets this behavioral threshold with this confidence under this evaluation set"

That is a different epistemology.

It is also a different user experience. TDD gives immediate red or green at the unit boundary.
Agent-style or LLM-style regression often gives you a probability-shaped statement plus the need
to decide what threshold matters for the product. That is not worse. It is just a different kind
of engineering work.

The article might say:

> Classical TDD asks whether the behavior is correct. Agentic regression asks how confident we
> are that a distribution of behaviors remains within acceptable bounds.

That is clean. Maybe a little formal, but probably worth keeping in some version.

---

## Where The Human Gate Actually Lives

One of the recurring mistakes in AI engineering discourse is treating human review as a fallback:
something we use only because the technology is not quite good enough yet.

That is backwards.

For stochastic systems, the human gate is not a temporary embarrassment. It is part of the
confidence architecture.

The reason is simple: product requirements, policy boundaries, user harm, reputational risk, and
commercial acceptability do not all collapse into a single numeric score. Even when the metrics
are excellent, someone still has to decide whether the measured behavior is acceptable for the
system's real use.

This is where evals differ sharply from ordinary unit tests.

If a deterministic unit test fails, the response is usually obvious: fix the code. If an eval
metric degrades, the response is interpretive. Maybe the regression matters. Maybe it clusters in
a low-value edge case. Maybe the model improved on the business-critical slice and regressed on a
stylistic dimension the team barely cares about. Maybe the dataset has drifted. Maybe the judge
prompt changed. Maybe a stricter schema increased latency but materially reduced downstream risk.

None of that is discoverable from the number alone.

So when the article says "what does work?" the answer cannot just be "evals." The fuller answer
is:

- deterministic checks where possible
- invariants at system boundaries
- statistical evals for probabilistic behavior
- human gates for meaning

That last phrase is useful:

human gates for meaning

Because that is what people are actually doing. They are not just rubber-stamping uncertainty.
They are deciding what counts as acceptable behavior in context.

This is also the point where the article can gently resist hype about automated AI QA. Yes, large
parts of the pipeline can and should be automated. No, that does not collapse governance into a
dashboard. A dashboard is not judgment.

---

## Why This Is Not An Anti-TDD Article

It is probably worth having a whole section on this in the working draft even if it gets cut.

TDD still matters.

It matters for the deterministic parts of the system.
It matters for the contract edges.
It matters for the orchestration logic that is ordinary software.
It matters for policy boundaries and integration layers.
It matters for the habit of specifying expected behavior before implementation.

What breaks is not the discipline of specifying before building. What breaks is the assumption
that all important behavior in an LLM system can be reduced to deterministic pass/fail assertions.

That is a more interesting claim than "TDD is dead."

In fact, one way to frame the whole article is:

The spirit of TDD survives. The unit semantics change.

That line may be too cute for the final version, but I like what it points to. Good engineering
still wants:

- explicit expectations
- fast feedback where possible
- incremental confidence
- refactoring under safety

The difference is that "safety" now includes metrics, distributions, judges, datasets,
thresholds, and interpretation, not just unit-level booleans.

This is also where the constrained-node nuance becomes strategically important. If you want more
TDD-like confidence in an AI system, design more of the system to admit deterministic checks.
Use schemas. Use structured outputs. Narrow task scopes. Make tool boundaries explicit. Separate
stochastic generation from deterministic validation. Keep the model call small enough that its
output contract can actually be reasoned about.

Now the article becomes implicitly architectural:

systems designed for constrained boundaries are easier to test.

That is not an anti-TDD claim at all. It is a systems-design claim.

---

## The Better Replacement Word Might Be "Evals" But The Better Replacement Idea Is "Confidence Architecture"

"Evals" is the common vocabulary, and the article probably has to use it. But in the working
draft I want the stronger phrase because it broadens the picture:

confidence architecture.

That phrase is useful because evals alone are not enough. Schema validation is not an eval in the
usual sense. Permission boundaries are not evals. Invariants are not evals. Cost limits are not
evals. Human signoff is not an eval. Yet all of these contribute to whether the team can trust
the system.

So maybe the final article says:

Evals replace TDD as the dominant methodology for non-deterministic behavior.

But underneath that sentence, what I really mean is:

A layered confidence architecture replaces the fantasy that one green deterministic test can
settle probabilistic behavior.

That feels closer to the truth.

The architecture might include:

- golden examples
- curated regression sets
- judge prompts
- rubric definitions
- schema checks
- business invariants
- run-to-run stability checks
- human spot review
- deployment thresholds
- rollback rules

Once the article frames things that way, the reader can see why the old loop is insufficient
without feeling like rigor itself has been abandoned.

Rigor moved up a level.

That is a nice sentence. Keep it somewhere.

---

## A Concrete Example Shape

The article might benefit from one concrete illustrative contrast.

Imagine a deterministic parser library.

You write a failing test: given this input, return this structure. The test fails. You fix the
code. The test passes. You refactor. The passing test suite gives real confidence because the
behavior under test is stable.

Now imagine a support-answering LLM system.

You ask it to answer customer questions based on internal docs. There is no one exact output for
many prompts. Some answers are clearer than others. Some are complete but overly verbose. Some
are terse but omit a caveat. Some sound confident while being subtly wrong. A single successful
answer to one prompt says almost nothing about overall behavior.

So what do you do?

You build a dataset.
You define evaluation criteria.
You run repeated assessments.
You compare versions.
You inspect clusters of failure.
You maybe use a judge model for triage.
You maybe apply schema constraints if output structure matters.
You maybe add policy checks for prohibited claims.
Then a human decides whether the measured change is acceptable.

That is not red-green-refactor. It is a different loop.

Maybe the article needs one sentence like this:

> TDD gives you confidence one example at a time. Evals give you confidence one distribution at a
> time.

That seems likely to survive.

---

## What This Means For Design

This is where the article becomes more interesting than a testing-methodology complaint.

If the system architecture determines which confidence methods are available, then testing is not
only a downstream QA concern. It is an upstream design concern.

A system built as one giant unconstrained agent with fuzzy responsibilities is hard to test
cheaply, hard to reason about, hard to evaluate, and hard to govern. A system built as narrower
nodes with explicit schemas, crisp tool boundaries, and limited responsibilities admits more
deterministic checks and more interpretable failures.

That means architectural choices are also testability choices.

In other words:

if you design for constraint, you design for confidence.

That connects this article forward to S2-A8, where constrained nodes and contract testing can be
treated directly, and to S2-A2, where the harder orchestration/runtime problem takes over.

S2-A1 should probably only name that future, not fully develop it. But it ought to hint that the
testing story and the system-design story are inseparable.

The more non-deterministic behavior you leave unconstrained, the more your confidence has to be
statistical, interpretive, and expensive.

The more structure you impose at the edge, the more you can pull confidence back down into cheap
deterministic checks.

That is a useful design tradeoff to make visible.

---

## A Possible Final Spine

If this draft gets cut hard, the final essay probably needs only this argument:

1. TDD is a fit-for-purpose method for deterministic systems.
2. It relies on determinism, binary correctness, and fast cheap feedback.
3. LLM systems violate those assumptions at the model-behavior layer.
4. Therefore classical red-green-refactor cannot be the dominant confidence method there.
5. Constrained nodes can still be contract-tested.
6. Orchestration behavior requires invariants plus statistical evals.
7. LLM-as-judge helps with triage, not verification.
8. Human review is part of the architecture, not an embarrassing fallback.
9. The better replacement idea is a layered confidence architecture.

Possible short thesis paragraph:

TDD works because deterministic software makes pass/fail meaningful. Non-deterministic LLM
systems break that assumption. The same prompt can produce different outputs, correctness often
depends on rubric rather than exact match, and the feedback that matters is frequently aggregate
and statistical rather than immediate and binary. The replacement is not "no rigor." It is a
layered confidence architecture: contract checks where outputs are constrained, invariants at
system boundaries, evals for probabilistic behavior, and human interpretation for what the
numbers mean.

Possible sharper hook:

The problem is not that LLM systems are hard to test. The problem is that we keep trying to use a
deterministic testing language on probabilistic behavior.

Possible closing:

You can still write failing assertions before you build. You can still demand fast feedback where
the system permits it. You can still care about refactoring under safety. But once behavior
becomes stochastic, one green test stops meaning what it used to mean. The future of rigorous AI
engineering is not abandoning testing. It is designing systems and workflows whose confidence
matches the shape of the behavior they produce.

---

## Alternate Angles To Mine Later

There are several smaller essays hiding inside this draft.

One is the **methodology essay**. That version is mostly about TDD itself: what assumptions it
requires, why those assumptions fail, and what statistical evaluation changes about engineering
practice. It would be the cleanest for a technical audience already comfortable with testing.

Another is the **architecture essay**. That version would focus less on evals in the abstract and
more on the constrained-node distinction. It would argue that testability is a design property,
not only a QA property. The stronger your boundaries, the more conventional confidence you can
recover. That version would probably bridge most directly into S2-A8.

A third is the **governance essay**. That one would emphasize the human gate and the difference
between automated triage and real acceptance. It would argue that the hard problem is not just
running judge models or benchmark suites; it is deciding what constitutes acceptable behavior in
the real product context. That version could connect naturally to later governance and quality-
gate articles.

A fourth is the **anti-hype essay**. That version would start from the mistake everyone keeps
making: treating one good demo run as proof of system quality. It would use the probabilistic
behavior argument to attack the "it worked once, ship it" mindset. That could be punchy, but it
would risk being too reactive unless balanced carefully.

The best series version probably borrows from all four but keeps the spine simple:

- why classical TDD breaks
- where contract testing still survives
- why evals matter
- why human interpretation remains load-bearing

That is enough for S2-A1.

---

## References

- [LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods (arXiv:2412.05579)](../papers/arxiv-2412.05579-llms-as-judges-survey.pdf)
- [LLM as a Judge: guide and best practices — Agenta](https://agenta.ai/blog/llm-as-a-judge-guide-to-llm-evaluation-best-practices)
- [LLM judge cookbook — Hugging Face](https://huggingface.co/learn/cookbook/en/llm_judge)
- [Beyond vibe checks: a complete guide to evals — Lenny's Newsletter](https://www.lennysnewsletter.com/p/beyond-vibe-checks-a-pms-complete)
- [A pragmatic guide to LLM evals — Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/evals)
- [AgentAssay: Token-Efficient Regression Testing for Non-Deterministic AI Agent Workflows (arXiv:2603.02601)](../papers/arxiv-2603.02601-agentassay.pdf)
- [LMQL: Prompting Is Programming (arXiv:2212.06094)](../papers/arxiv-2212.06094-lmql-prompting-is-programming.pdf)
- [Record & Replay: Automated Testing for LLM Agents (arXiv:2505.17716)](../papers/arxiv-2505.17716-record-replay-llm-agents.pdf)
- [Automated Self-Testing as a Quality Gate for LLM Applications (arXiv:2603.15676)](../papers/arxiv-2603.15676-automated-self-testing-quality-gate.pdf)
- [Beyond Traditional Testing: Non-Deterministic Software — AWS/dev.to](https://dev.to/aws/beyond-traditional-testing-addressing-the-challenges-of-non-deterministic-software-583a)
- [Testing AI Agents: Validating Non-Deterministic Behavior — SitePoint](https://www.sitepoint.com/testing-ai-agents-deterministic-evaluation-in-a-non-deterministic-world/)
