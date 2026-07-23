# AI Makes Bad Code Worse
### Big Draft - expanded working draft

---

## Working Note

This is intentionally too large.

The point is not to preserve this shape. The point is to make the argument available in more
forms than the final article will need: alternate transitions, extra framing lines, repeated
claims from different angles, more evidence than will survive publication, and a few bridges
to later articles so I can decide later which ones to keep.

This draft has to do a few things clearly:

- inherit A1's phase-boundary / gamification frame rather than sounding like a generic
  "AI creates bugs" article
- distinguish **amplification** from **accumulation**
- explain why the trap is structural rather than moral
- make the `/compact` asymmetry land cleanly
- use Agile-V and Agentic Agile-V as the stronger non-proprietary process frame
- set up A3, A5, and A6 without solving everything early

The emotional register should stay cool. The system is doing exactly what it is optimized to do.
That is the problem.

---

Good code is legible constraint.

Bad code is accumulated ambiguity.

That is a useful place to start because it clarifies what AI coding systems are actually
amplifying. They are not amplifying intention in the abstract. They are not amplifying
architecture in the ideal form it would have if the team stopped, thought clearly, wrote down
its invariants, and reorganized the repository around what it now understands. They are
amplifying what is locally available.

That distinction matters.

If the local code expresses a coherent design, the assistant can extend something coherent. If
the names are stable, the boundaries are sensible, the tests describe behavior, the abstractions
are real, and the surrounding modules reflect deliberate choices, then continuation can be a
form of acceleration. The assistant is not inventing the quality. It is inheriting it.

If the local code expresses drift, contradiction, half-completed refactors, unexplained
wrappers, broad utility functions, ambiguous side effects, and behavior nobody fully trusts,
then the assistant inherits that too. It does not pause and say: this area of the codebase is
confused, perhaps the right thing to do is halt and recover the missing design rationale before
we produce more output.

It extends the pattern.

That sentence probably has to stay in the final piece:

> The agent extends the pattern, not the ideal.

That is the core mechanism. It sounds almost too simple, but the simplicity is exactly what
makes it dangerous. People often want the tool to function like an always-on senior engineer:
seeing through the mess, inferring the architecture that should have existed, quietly refusing
bad local precedent, and producing the cleaner version anyway. Sometimes it appears to do that,
which is part of why the workflow is so seductive. But structurally that is not what we should
assume. Structurally we should assume a system that is highly sensitive to the evidence it is
given.

Evidence is not the same thing as truth.

The repository contains evidence. The current file contains evidence. The names, patterns,
comments, tests, nearby abstractions, and recent diffs all contain evidence. Some of that
evidence may point toward good design. Some of it may point toward historical accidents that
have survived long enough to look legitimate. The assistant does not experience the difference
the way a human maintainer eventually does after enough painful contact with the system.

So the article's first move is not "AI writes bad code." That is too broad, too dull, and too
easy to reject.

The better first move is:

> AI-assisted development accelerates output in proportion to the quality of the context it is
> allowed to extend.

That preserves the positive case. It matters to preserve it. If this article sounds like a
blanket denunciation of AI assistance, it loses both credibility and usefulness. The true
argument is sharper: current tools can be genuinely helpful in healthy, well-bounded contexts
and genuinely dangerous in unhealthy, poorly bounded ones. The same continuation loop that
makes exploration productive can make debt compound.

That is why A2 has to come directly after A1.

A1 says the reward structure of the tool keeps people in motion after the phase of work should
have changed. A2 asks the obvious next question: once the loop keeps running, what exactly gets
installed into the codebase?

Not understanding.
Not architecture.
Not judgment.

Patterns.

Patterns plus local precedent.
Patterns plus partial tests.
Patterns plus whatever ambiguity was already there.

That is the first structural consequence of the gamified continuation loop.

---

## The Two Mechanisms

This article needs a clean distinction that readers can remember after they forget the rest of
the prose.

There are two mechanisms here:

1. **Amplification**
2. **Accumulation**

Amplification is the immediate mechanism. A messy area of code invites help. The assistant sees
the mess and continues it. If the local abstraction is questionable, the generated patch often
extends the questionable abstraction instead of replacing it. If the function is too broad, the
assistant happily adds another branch. If the service object already does four jobs, the patch
makes it do five. If naming is inconsistent, the patch tends to reinforce the inconsistency.

Amplification is what happens inside a single interaction.

Accumulation is slower and more dangerous. It is what happens after the patch lands, survives
review, becomes part of the repository, and turns into context for the next session. Yesterday's
plausible local compromise becomes today's local precedent. A pattern that might once have been
recognized as a temporary shortcut now exists in the codebase as something the next prompt will
read as normal.

That is the recursive part.

The output does not merely affect today's task. It changes the substrate on which future tasks
will be generated.

This is the moment where the `/compact` comparison earns its place.

You can compact a session. You can summarize the conversation, start a fresh context, or decide
that the active chat has become too noisy to be useful. The working memory can be reset.

Codebases do not have that escape hatch.

> Context windows can be reset. Codebases cannot.

That is not just a clever line. It is the operational asymmetry that makes codebase debt more
dangerous than session confusion. A bad chat can be abandoned. A bad patch that has been merged
and later extended has to be unwound. A context window can be pruned. A repository accumulates
history in public, executable form.

This is why the article should keep returning to the word *installed*.

Generated debt is not just written. It is installed into the future.

And because the article sits early in the series, it should probably say explicitly that
technical debt here is not only complexity in the classic sense. It includes:

- poor local abstractions
- unclear boundaries
- duplicated logic
- weak naming
- silent side effects
- tests that bless behavior nobody intended
- undocumented assumptions
- review burden transferred to the future

Some of that will look harmless in the moment. That is the point. Silent accumulation is rarely
dramatic while it is happening. The diff passes. The feature works. The test is green. The
ticket closes.

The problem is not visible at the level of the local reward signal.

---

## The Trap Zone

One of the strongest claims in this article is also one of the simplest:

> The places where developers most want AI help are often the places where AI help is least
> trustworthy.

That is the trap zone.

Humans ask for assistance where the local understanding is thin. This is normal. It is what we
would expect from finite attention. When a codebase is messy, stale, confusing, or historically
layered, the cost of rebuilding a full mental model is high. That is exactly when it becomes
tempting to delegate part of the search and part of the implementation to the assistant.

But those same conditions are precisely what make continuation risky.

The assistant is not looking at some purified representation of the design. It is looking at the
very local evidence that the human already found hard to reason about. The human feels the area
is difficult because the area lacks legible constraints. The assistant reads that same absence as
"continue from what is present."

This is where "AI makes bad code worse" becomes more than a slogan.

It is not just that bad code exists and AI sometimes contributes to it. It is that the workflow
systematically concentrates assistance in confusing regions. The tool is most tempting where the
human comprehension burden is highest. The trouble is not randomly distributed. It clusters.

There is a practical version of this that almost every engineer will recognize. You open a file
that nobody loves. The names are vague. The helper functions are overly broad. The state changes
in more than one place. The tests are either missing or too coupled to implementation details.
There are traces of older designs that were never fully removed. There may be comments that once
explained something and are now mostly decorative. You do not want to spend two hours rebuilding
the entire rationale for why this subsystem looks the way it does. So you ask the assistant for a
targeted change.

The patch comes back plausible.

Not beautiful. Plausible.

It fits the local style because the local style is what it read. It takes the existing shape for
granted because that is what continuation does. It may even feel "respectful" of the codebase in
the sense that it changes only what seems necessary. But if the local pattern was the problem,
then respecting it is not a virtue. It is a multiplier.

This is the part that should feel slightly exasperated in the final essay:

> In debt-heavy zones, "continue the pattern" is not neutral.

That line gets close to the real emotional core. The system is not malicious. It is not trying
to make things worse. It is doing exactly what the interface and context structure reward it for
doing. Which means the burden shifts back to the workflow: when does the workflow force a stop,
a summary, a redesign, a narrower constraint, a test-first boundary, or a refusal to keep
extending the local mess?

Without that stop signal, the continuation loop quietly turns confusion into precedent.

---

## What Agile-V Adds

This is where the Agile-V material matters because it gives a non-proprietary vocabulary for the
same structural problem.

Agile V starts from a straightforward observation: machine-speed AI-assisted development can
generate code and supporting artifacts faster than ordinary workflows can verify them. If the
delivery loop does not build verification and traceability into each cycle, speed outruns
control. Agentic Agile-V extends that observation into the broader claim that current agentic
systems create a process problem, not just a prompting problem.

That matters here because A2 is not really an article about style. It is an article about what
happens when continuation outruns verification.

Agile-V's strength is that it makes the missing gate visible. The problem is not merely that
developers are extending poor local patterns. The deeper problem is that there is no structural
requirement to turn conversational exploration into explicit constraints before more code is
allowed to survive. Agentic Agile-V calls this out through ideas like the conversation-to-
contract gate, scoped execution, evidence bundles, and human approval boundaries. Those are all
different ways of saying the same thing:

speed without a phase change becomes debt.

There is a phrase from Agentic Agile-V that should do a lot of work in this article:

**verification debt**.

That term is useful because it is broader than "bugs" and more procedural than "technical debt"
used in the abstract. Verification debt is what accumulates when output volume grows faster than
the team's ability to validate meaningfully. Weak tests, broad patches, hidden regressions,
unvalidated assumptions, and reviewer overload all belong to it. A2 can borrow that concept and
then translate it into codebase terms:

- the assistant extends local patterns
- the team accepts plausible output under time pressure
- the repository stores the result
- future sessions inherit that repository as context
- the cost is deferred, not avoided

That is the whole loop.

Agile-V is especially useful because it avoids the trap of making this article sound like a
personal preference about code cleanliness. It relocates the critique into process control.
Maybe the patch compiles. Maybe the feature works. Maybe the generated diff even looks smaller
and tidier than what a tired engineer would have produced manually. None of that proves the work
was correctly bounded, independently verified, or made legible enough to survive future change.

The process question is always larger than the diff.

This is also a good place to keep the article from drifting into "the AI should have saved us."
The stronger claim is:

> Without an explicit verification gate, continuation treats plausibility as success.

That is not just an AI problem. But AI makes it cheaper, faster, and more frequent.

---

## Debt In The Wild

The large-scale empirical result from Liu et al. has to anchor the article somewhere in the
middle. It gives the essay weight without forcing it to become purely academic.

The numbers matter because they relocate the discussion from anecdotes to lifecycle evidence:

- 302.6K verified AI-authored commits
- 6,299 repositories
- 484,366 distinct issues
- more than 15% of commits from every assistant introduce at least one issue
- 22.7% of tracked AI-introduced issues survive to the latest repository revision

The power of this result is not that AI sometimes makes mistakes. Everybody already knows that.
The power is that a meaningful fraction of introduced issues are not cleaned up by the normal
course of later development.

The debt persists.

That is exactly what the article needs. A2 is not trying to prove that generated code can be
bad in the moment. It is trying to prove that unverified continuation installs lasting costs
into the future codebase. The survival rate matters because it shows the problem is not merely
"temporary mess that gets polished later." Some of it never gets polished later.

It becomes normal.

This is also why the article should resist sensational language. The study is already strong.
There is no need to write as if every AI-assisted workflow is a disaster. The evidence is more
interesting than that. The evidence says the local convenience is real and the downstream cost is
also real. That is a much more durable argument.

It might be useful to say it this way:

> The question is not whether AI-authored code can be cleaned up. The question is whether the
> workflow reliably creates the conditions under which it will be.

Without gates, the answer often seems to be no.

That claim becomes even stronger when paired with the behavioral research on conversational
coding. Progressive specification is real. Developers genuinely do discover requirements while
working with these tools. That is part of their value. But if the session remains purely
progressive - always refining, rarely consolidating - then the codebase becomes the place where
half-made decisions harden.

That is the move from amplification to accumulation in one paragraph:

The assistant copies local precedent. The user accepts the patch because the patch is plausible.
The repository stores the compromise. The next prompt treats the compromise as evidence. Debt no
longer has to be chosen intentionally. It only has to be extended repeatedly.

---

## The Cognitive Companion Problem

This article is mainly about the artifact layer, but it should borrow just enough from the
comprehension-debt work to set up A3.

The code is not the only thing that gets worse.

When a team accepts generated output in a confusing part of the system, the debt lands twice:

1. in the repository
2. in the team's mental model of the repository

That distinction matters because otherwise people will think the answer is just refactoring. If
the problem were purely local complexity, then in theory a future cleanup pass could restore the
system. But comprehension debt means the people carrying the code forward may understand less
about it than they think they do. The patch works, the task closes, the feature ships, and the
understanding gap remains mostly invisible until some later change demands genuine explanation.

This is where Ahmad's vocabulary helps:

- black-box acceptance
- context mismatch
- dependency-induced atrophy
- verification bypass

Those ideas belong mostly to A3, but A2 can use them lightly to show why artifact debt does not
stay outside the human system. The codebase does not become harder in isolation. It becomes
harder *for people* who now have to maintain code whose local legitimacy was created by the loop
rather than by explicit understanding.

Possible line:

> The codebase is not just storing bad decisions. It is storing decisions whose rationale was
> never fully recovered from the moment of generation.

That sets up A3 nicely because A3 can then ask what that feels like from inside the engineer's
head: shipping more, feeling worse, and gradually losing the competence signal that used to make
the work feel real.

But A2 should stay disciplined. It should not become the burnout article early. It only needs
enough of this to show that code debt and cognitive debt reinforce each other.

Code nobody fully understands is easier to offload again.

That sentence probably deserves to stay.

---

## Why The Problem Is Structural

It is important that the article not accidentally shame the user.

The weak version of this piece would sound like:

"Developers are careless, lazy, too trusting, or too addicted to the convenience of AI."

That version is both morally tedious and analytically weak.

The stronger version says:

"Developers are responding rationally to a workflow that makes continuation cheap, review
optional, and local progress highly visible."

That is very different.

A continuation-friendly interface teaches people to continue. A system that offers immediate
plausible diffs trains users to trust plausibility under uncertainty. A tool that makes the next
step obvious and the stopping point vague will tend to produce overshoot.

None of that requires a weak engineer.

In fact, this may be one of the most interesting things about the problem: experienced engineers
often know they are in a bad zone and still use the assistant there because the local economics
are persuasive. They can see the ambiguity. They also know the cost of recovering the entire
design by hand. So they take the plausible patch, planning to revisit it later. Sometimes later
never comes. Sometimes later comes only after the patch has already been extended three more
times.

That does not make the engineer unserious. It makes the workflow underconstrained.

This is a useful place to restate the anti-moralizing principle from A1 in a new way:

> The failure is not that people enjoy the acceleration. The failure is that the system offers
> acceleration without forcing the conditions under which acceleration remains safe.

That is what makes the argument structural.

It also explains why the article should not pretend that all assistance in messy code is bad.
Sometimes a strong engineer really can use the tool to map an ugly area, extract a better
abstraction, or draft a cleanup faster than they could alone. But in those cases the tool is not
operating autonomously as a truth engine. It is operating inside strong human judgment plus a
clear intention to refactor, redesign, or narrow the boundary. The improvement does not happen by
continuation alone. It happens because someone imposes a better target on the continuation loop.

Which is another way of saying: constraints matter.

That is A5's territory later. Here it is enough to say the absence of constraints is what turns
plausibility into technical debt.

---

## A Small Concrete Story

The article probably wants one grounded example, even if it stays compact.

The shape of it is simple:

I open a file I already half distrust. The abstractions are muddy. The names suggest one design
but the behavior suggests another. There are traces of previous intentions that were never fully
removed. I need one more feature or one more fix in this area. I do not want to reconstruct the
entire subsystem from first principles just to make a small change, so I ask the assistant for a
patch.

The patch comes back plausible.

It respects the existing file structure. It calls the same helpers the human would probably have
called under time pressure. It preserves the local naming, even when the naming is part of the
confusion. It adds one more branch, one more wrapper, or one more coupling point. Maybe it even
adds tests that faithfully protect the questionable local behavior.

Now the dangerous part:

because the patch works, it inherits legitimacy.

Next week, the same file is no longer just historically messy. It is newly messy in a way that
looks current. The ambiguous abstraction now has one more successful use. The next prompt will
see not only the old accident but also the freshly installed precedent. The line between
"historical scar tissue" and "current design" gets blurrier.

That is accumulation in miniature.

The assistant did not sabotage the codebase. It ratified a local compromise and made it easier
for the compromise to survive.

That example is probably enough. The point is not to dramatize. The point is to make the loop
feel ordinary. Because ordinary is exactly what makes it dangerous. If the failure mode were
catastrophic every time, teams would notice sooner. Instead, it often arrives as one more small
success.

---

## What The Article Is Really Against

This article is not really against AI-generated code.

It is against **unreviewed continuation in ambiguous contexts**.

That may seem like hair-splitting, but it matters for tone and for truth. Plenty of generated
code is fine. Plenty of manually written code is terrible. The decisive factor is not the source
of the characters. It is whether the workflow can distinguish:

- exploratory output from committed design
- plausible behavior from verified behavior
- local precedent from trustworthy precedent
- acceleration from offloading

If the workflow cannot tell those apart, then speed becomes a liability.

This is also where the article should avoid sounding nostalgic. Handwritten code is not a moral
achievement. Manual effort is not automatically higher quality. The point is not to restore a
pre-AI priesthood of suffering. The point is to recover the engineering boundary between
"something happened" and "this is now part of the system we own."

If an agent can correctly implement a tightly bounded change against strong tests and clear
constraints, great. That is acceleration.

If an agent is being used to keep moving through a confusing area because stopping to recover the
design feels too expensive, that is usually offloading.

That distinction is what the Vibe-Check Protocol gives this article. It keeps A2 from being
merely a repository-health essay. The real issue is not only code quality in the abstract. It is
how teams use the tool differently when the local understanding is strong versus weak.

In clean zones, acceleration is possible.
In debt zones, offloading is tempting.

That sentence may deserve to survive almost unchanged.

---

## What Has To Interrupt The Loop

Because this article is early in the series, the answer should be teased rather than fully
developed. But it still needs to name the category of solution.

The fix is not "do not use AI in bad code."

That would be unserious. Bad code is where organizations most need help. The real question is:
what has to interrupt the continuation loop before more debt is installed?

Several candidates belong here, even if they are only gestured at:

- explicit acceptance criteria
- tests that encode intended behavior rather than current accident
- review artifacts that force a human-readable rationale
- narrower scopes for AI-generated changes
- context selection rather than raw context dumping
- risk-adaptive gates in higher-risk areas
- a willingness to stop and redesign instead of extend

Agile-V and Agentic Agile-V help because they make the interruption concrete. They say: do not
let the system move from conversation to implementation without a reviewed brief and evidence
requirements. That is the process version.

The later series articles will say:

- A4: the memory artifacts have to be designed, not merely accumulated
- A5: constraints are not bureaucracy; they are how the agent gets a real target
- A6: poisoned context makes continuation unreliable even when the local intent is good

A2 only needs enough of that horizon to show that the problem is answerable, not inevitable.

Maybe the cleanest teaser is this:

> The answer is not less assistance. The answer is stronger boundaries around what assistance is
> allowed to extend.

That feels right for the place this article occupies in the sequence.

---

## A Possible Final Spine

If this draft gets cut down hard, the final article probably only needs this core sequence:

1. A1 showed that current tools keep rewarding continuation after the phase should have changed.
2. A2 shows what continuation installs into the codebase: not ideal design, but local pattern.
3. In healthy code, that can be acceleration.
4. In debt-heavy code, that becomes amplification.
5. Once merged, the amplified compromise becomes future context.
6. That is accumulation.
7. Codebases cannot be `/compact`'d.
8. The large-scale evidence shows AI-introduced issues often survive.
9. Agile-V gives the right process vocabulary: verification debt, gates, evidence, reviewed
   briefs, human approval.
10. The answer is not anti-AI. The answer is explicit interruption of the continuation loop.

Possible short thesis paragraph:

AI coding tools do not extend the architecture you wish you had. They extend the patterns they
can see. In clean code that can be acceleration. In debt-heavy code it becomes amplification.
And once those plausible local compromises are merged, they stop being just mistakes in a
session and become context for future sessions. Context windows can be reset. Codebases cannot.

Possible sharper one-liner:

The assistant is easiest to trust exactly where it is hardest to verify.

Possible closing:

Generated debt is dangerous for the same reason generated speed is appealing: it arrives as
visible progress. By the time the codebase starts fighting back, the local compromises have
already hardened into precedent. The question is not whether AI can help in bad code. The
question is what boundary stops "one more plausible patch" from becoming the architecture.

---

## Alternate Angles To Mine Later

This draft probably contains several smaller essays inside it.

One possible version is the **artifact essay**. That version focuses almost entirely on the
repository as memory. It would say that AI changes codebases not just by adding lines but by
changing what counts as precedent. The key concept would be that merged code is active context.
Every accepted compromise becomes evidence. This version would lean hard on the `/compact`
asymmetry and maybe gesture less toward cognition.

Another version is the **process-control essay**. That one would foreground Agile-V earlier and
more explicitly. It would say the problem with AI-assisted debt is not merely bad style or too
many bugs. It is the absence of a phase boundary between conversational discovery and
verification-bearing implementation. That version would be useful if the goal is to set up
Series 2 more directly.

A third version is the **maintenance essay**. That one would emphasize debt survival and the
handoff problem: the code that "worked fine when generated" has to be modified by someone later.
That later engineer does not inherit the original conversational reasoning. They inherit the
artifact. This version would probably use more of the comprehension-debt material and could
bridge very naturally into A3.

A fourth version is the **trap-zone essay**. That one would center the most memorable claim:
teams seek AI help where human understanding is already thinnest. It would build the whole piece
around that irony. The assistant feels most valuable in legacy tangles, vague abstractions, and
high-friction modules. But those are also the places where local continuation is least reliable.
This version might be the most readable in a short form because the claim is easy to remember.

The series version, which is probably the one to publish, should borrow from all four without
becoming too academic. It needs:

- one memorable mechanism
- one memorable asymmetry
- one serious empirical anchor
- one process-control frame
- one bridge to the next article

The memorable mechanism is amplification plus accumulation.
The memorable asymmetry is `/compact` for sessions but not repositories.
The empirical anchor is the Liu study.
The process-control frame is Agile-V / Agentic Agile-V.
The bridge is comprehension debt and later constraints.

That is enough.

---

## References

- [Agile V: A Compliance-Ready Framework for AI-Augmented Engineering (arXiv:2602.20684)](../papers/arxiv-2602.20684-agile-v-koch-wellbrock.pdf)
- [Agentic Agile-V: From Vibe Coding to Verified Engineering (arXiv:2605.20456)](../papers/arxiv-2605.20456-agentic-agile-v-scope-v.pdf)
- [Debt Behind the AI Boom: A Large-Scale Empirical Study of AI-Generated Code in the Wild (arXiv:2603.28592)](../papers/arxiv-2603.28592-debt-behind-ai-boom.pdf)
- [Programming by Chat: A Large-Scale Behavioral Analysis of 11,579 Real-World AI-Assisted IDE Sessions (arXiv:2604.00436)](../papers/arxiv-2604.00436-programming-by-chat.pdf)
- [Comprehension Debt in GenAI-Assisted Software Engineering Projects (arXiv:2604.13277)](../papers/arxiv-2604.13277-comprehension-debt.pdf)
- [The Vibe-Check Protocol: Quantifying Cognitive Offloading in AI Programming (arXiv:2601.02410)](../papers/arxiv-2601.02410-vibe-check-protocol.pdf)
- [Vibe Coding in Practice: Flow, Technical Debt, and Guidelines for Sustainable Use (arXiv:2512.11922)](../papers/arxiv-2512.11922-vibe-coding-in-practice.pdf)
- [Adam Tornhill on psychology of code quality — Tech Lead Journal](https://techleadjournal.dev/episodes/241/)
