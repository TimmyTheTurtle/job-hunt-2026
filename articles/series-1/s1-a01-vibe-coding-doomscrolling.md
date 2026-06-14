# S1-A1 — Vibe Coding Is the New Doomscrolling

**Status:** Out for editing
**Series position:** 1 of 10 — the lead. Everything depends on how well this one lands.

---

## Voice and Tone

- **Karpathy and all practitioners are treated with full respect.** Never raise the hypocrisy
  reading. Never imply the rename was a cover-up or embarrassment-management. His distinction
  between vibe coding (raises the floor) and agentic engineering (raises the ceiling) is a
  genuine contribution — a useful clarification made more precise over time. nanochat being
  hand-written was a phase-boundary decision, not an anti-AI statement.
- **Voice register:** 10% Rodney McKay — brief exasperated undercuts, not sustained; stat ->
  short judgment sentence. Positive case before empirical floor.

---

## Thesis

Vibe coding is a valid tool applied to the wrong phase, indefinitely. That is what makes it
harmful — not the tool itself.

In the right context — pre-requirements exploration, hypothesis generation, rapid prototyping
before you know what you're building — high-velocity, low-judgment AI-assisted coding is
exactly correct. You are not supposed to understand what you're building yet. The point is to
find out. Applying engineering discipline at that stage is premature.

The problem is when you never exit that phase. Vibe coding that continues through design, build,
and deployment reproduces the engagement mechanics of doomscrolling: infinite continuation,
variable rewards, a persistent "just one more" interaction loop that feels productive and
compounds debt invisibly. Andrej Karpathy coined the term in February 2025 to describe a real
behavior — generating software by feel, through conversation, without reading the output closely
enough to understand it. A year later he sharpened the vocabulary: vibe coding raises the floor
(anyone can build something); agentic engineering raises the ceiling (experienced practitioners
using AI rigorously). That distinction is the article in miniature — the same technology, two
different relationships to it, and the phase boundary is what separates them.

The evidence is accumulating: a METR controlled trial with 16 experienced developers found AI
tools made them 19% slower while they believed they were 20–24% faster — a 39-point
perception-reality gap. Anthropic's January 2026 comprehension study (Shen & Tamkin) found
developers using AI assistance scored 17% lower on comprehension quizzes about code they'd just
written. These are not vibes. They are measured outcomes of staying in exploration mode past the
point where discipline should have engaged.

---

## Key Claims

- Vibe coding is a valid exploratory phase tool, not a productivity methodology
- The harm comes from never exiting the exploratory phase, not from the tool itself
- The loop mechanics are structurally identical to social media attention mechanics
- The cost is deferred, invisible, and measured — not just felt
- Karpathy's floor/ceiling distinction is the honest vocabulary: same tool, different
  relationship to it, and the phase boundary is what determines which you're in
- The fix is not discipline instead of vibe coding — it is discipline about when to stop
- Handwriting code when a well-spec'd agent could generate it is waste, not virtue
- The quality of AI-generated code is a function of the spec and coded behaviors given to
  the agent — not of whether a human typed the characters

---

## Argument Flow

1. **Open with the Karpathy arc.** He coined the term February 6, 2025, described a real
   behavior, and by April 2026 (Sequoia Ascent) had refined the vocabulary: vibe coding raises
   the floor; agentic engineering raises the ceiling. His nanochat project being hand-written
   (October 2025, "basically entirely by hand, because Claude/Codex agents had been net
   unhelpful there") is a phase-boundary decision, not an anti-AI statement. Not avoiding AI.
   Knowing which mode the work requires.

2. **Define the loop mechanics honestly.** Vibe coding has a legitimate on-ramp function.
   When you have no momentum, no inspiration, no clear starting point — the low-friction
   prompt-response loop gets you into a problem space you might not have entered otherwise.
   Include Willison's precision: vibe coding is the specific mode where code arrives faster than
   comprehension. The variable ratio schedule is real. The intermittent reward is doing work.
   The doomscrolling parallel is not "both are purely harmful" — it is "both are useful ignition
   mechanisms with no built-in exit condition."

3. **Introduce the phase argument.** Exploratory prototyping (pre-requirements, discovery)
   is categorically different from disciplined engineering (requirements-locked). The Bjarnason
   PAM model gives this formal vocabulary. Vibe coding is the right fuel for the exploratory
   engine. The failure mode is not using vibe coding — it is quietly letting a throwaway loop
   become a shipping process.

4. **Positive case before the floor.** Watershed is a concrete example of the exploratory
   phase done right — and needs a brief intro sentence for readers who don't know the project.
   Frame it as a personal project: a D3D12 puzzle game, started with no requirements, no design
   doc, just a world and a set of questions. The staged naming (grass-field-001 through -004),
   the bounded experiments, the WFC solvability notes that crystallized at the end — these are
   what the phase boundary looks like when it's implicit but real. Use it to disarm the "AI is
   always harmful" reading before the numbers arrive.

5. **Drop the empirical floor.** METR: 19% slower, felt 20–24% faster; Feb 2026 update says
   productivity triumphalism is no longer defensible, not that AI universally slows developers.
   Shen & Tamkin (Anthropic Jan 2026): 17% lower comprehension scores. Liu et al.: 484,606
   AI-introduced issues across 304,362 commits; 24.2% survived to latest revision.

6. **Name what is missing — and what is not the problem.** Not manual typing. The phase
   boundary produces the spec. The spec is what makes AI generation correct and fast. Without
   it, generation is fast and unreliable. Forcing a human to type every character when a
   well-spec'd agent could generate it is not craftsmanship. It is theater. The human role
   is judgment, taste, oversight, and the spec. Everything after that is just doomscrolling
   with a CI pipeline.

## Main Points to Discuss

- What doomscrolling is and how it works (peer-reviewed: variable rewards, infinite scroll,
  anxiety/pessimism links — not Wikipedia or counseling centers)
- What vibe coding is: Willison's precision — the mode where code arrives faster than comprehension
- The honest case for the engagement loop: valid ignition mechanism, not purely harmful
- The phase argument: Bjarnason PAM; exploratory vs. evolutionary; failure mode is the
  quiet slide from throwaway to shipping
- Karpathy's floor/ceiling distinction as the article's opening arc
- Watershed positive case — needs brief intro (D3D12 puzzle game, personal project,
  pre-requirements exploration) before the staged-naming evidence lands
- Empirical record: METR, Shen & Tamkin, Liu et al.
- What's missing: not keystrokes, but the phase boundary that produces the spec

## Solution Hints to Seed (don't solve yet — tease)

- Phase boundaries with explicit exit criteria
- The question "are we still exploring?" asked and answered
- Memory and constraints that engage when the formal phase begins

---

## Concrete Example — Watershed

**Reader context needed:** Watershed is a personal project — a D3D12 puzzle game built on a
30-year-imagined world. Introduce it as such before the evidence. The reader knows nothing
about it. One sentence of context before any named artifacts.

**What happened:** Started with no requirements — no game design document, no settled
mechanics. AI-assisted vibe coding drove a series of bounded throwaway experiments:
- grass-field-001 through grass-field-004: four column raycast renderer prototypes, each
  named as a disposable stage, each answering a specific visual/technical question
- RAII module extraction (renderer phases 1-3): bounded, completable, not open-ended
- WFC encounter design: Wave Function Collapse + scalar field simulation + formal solvability
  model — the destination the exploration was navigating toward, not the starting point

**The phase discipline was implicit but real:** The staged naming convention is itself evidence.
When grass-field-002 answered its question, a new number started. The WFC notes in
`future-wfc-encounter-notes.md` are a requirements document for the puzzle system. They could
not have been written without the exploration. They are what the exploratory phase crystallized
into when it was done.

**The point for A1:** Watershed is the positive case the article needs. Exploration that
produced a coherent system design (WFC + scalar fields + solvability gate) and a running demo.
The exploratory phase ended. Something definite emerged. The argument isn't "vibe coding always
works" — it's "vibe coding with an implicit exit condition works, and here is evidence."

**Caution when writing:** Don't lean on the game being a passion project. The structural
argument is what matters: bounded experiments, named throwaway stages, crystallized requirements
document at the end. The subject being a game is interesting color, not the point.

---

## Sources

- [Andrej Karpathy coins "vibe coding" Feb 6 2025 — Simon Willison (precise definition: code arrives faster than comprehension)](https://simonwillison.net/2025/Mar/19/vibe-coding/)
- [Karpathy distinguishes vibe coding from agentic engineering, April 2026 Sequoia Ascent — SD Times](https://sdtimes.com/ai/andrej-karpathy-has-renamed-vibe-coding-heres-what-engineering-leaders-need-to-do-about-it/)
- [Karpathy's nanochat "basically entirely hand-written, Claude/Codex agents net unhelpful" Oct 2025 — Futurism](https://futurism.com/artificial-intelligence/inventor-vibe-coding-doesnt-work) — frame as phase-boundary decision, not anti-AI
- [Vibe coding overview — Wikipedia](https://en.wikipedia.org/wiki/Vibe_coding)
- [Replit on vibe coding](https://replit.com/blog/what-is-vibe-coding)
- [Martin Fowler / Thoughtworks 2026: humans working on the loop, not just in it](https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html)
- [Doomscrolling overview — Wikipedia](https://en.wikipedia.org/wiki/Doomscrolling)
- Rixen et al. 2023 — peer-reviewed field study on infinite scroll; users "caught in a loop," sessions "regretfully elongating"; use instead of counseling-center sources
- Variable reward / social media engagement review literature (2025) — ties engagement to variable rewards, personalized feeds, endless continuation
- Doomscrolling + anxiety/pessimism/work-engagement literature (2024) — peer-reviewed associations
- [METR productivity RCT](https://arxiv.org/abs/2507.09089) — arXiv:2507.09089; 16 developers, 246 tasks, own mature repos; 19% slower, felt 20–24% faster; Feb 2026 update: late-2025 tools may show modest speedups; honest claim = "kills productivity triumphalism"
- Shen & Tamkin, Anthropic January 2026 — 17% lower mastery quiz scores using AI assistance; correct source for this stat (NOT Ahmad et al.)
- [Comprehension Debt — Ahmad et al., April 2026](https://arxiv.org/abs/2604.13277) — arXiv:2604.13277; names mechanisms: black-box acceptance, context mismatch, dependency-induced atrophy, verification bypass
- [Debt Behind the AI Boom — Liu et al., March 2026](https://arxiv.org/abs/2603.28592) — arXiv:2603.28592; 304,362 AI commits; 484,606 issues identified; 24.2% surviving to latest revision (code smells, bugs, security — not strictly "defects")
- [Empirically Based Model of Software Prototyping — Bjarnason et al. 2023](https://dl.acm.org/doi/10.1007/s10664-023-10331-w) — PAM; exploratory vs. evolutionary prototypes categorically distinct
- [Vibe Coding in Practice: Flow, Technical Debt, and Guidelines — Waseem et al. Dec 2025](https://arxiv.org/abs/2512.11922) — arXiv:2512.11922; flow-debt trade-off; powerful for MVPs/prototypes, increasingly risky without lifecycle safeguards
- June 2026 interview study (17 experienced developers using software agents) — oversight breaks into a priori control, co-planning, real-time monitoring, post hoc review

---

## Draft

# Vibe Coding Is the New Doomscrolling

Andrej Karpathy coined "vibe coding" on February 6, 2025: a mode of building software where
you give in to the vibes, accept the code, and stop pretending you are reading every diff. By
April 2026, at Sequoia Ascent, he was drawing a sharper line. Vibe coding, he said, raises the
floor. Agentic engineering raises the ceiling. In October 2025, when asked how much of nanochat
he had written himself, he answered that it was basically entirely by hand, because Claude and
Codex agents had been net unhelpful there. That sequence matters. It is a phase boundary showing
up in public before most of the industry had language for it.

Vibe coding is not a fraud. It is not laziness. In the right phase, it is exactly the right
tool. When you do not yet know the real requirements, the architecture, or even the right
question, the low-friction prompt-response loop gets you moving. Simon Willison's distinction
is useful here: vibe coding is not the same thing as all AI-assisted programming. It is the
specific mode where code arrives faster than comprehension. For throwaway exploration, that can
be a feature, not a bug. When you have no momentum — no obvious starting point, no confident
sense of what the architecture should look like — the loop gets you inside the problem. You
describe what you're trying to build, loosely. The model generates something. The something is
wrong, or incomplete, or pointed in a direction you didn't intend. But now you are inside it,
looking at a concrete artifact, and your brain starts doing the real work of evaluating it.
You are not specifying the cathedral yet. You are walking the land, tripping over the rocks,
and finding out where the ground is actually load-bearing.

The problem is not vibe coding. The problem is the phase.

---

### Why the doomscrolling parallel is not an insult

The structural similarity between vibe coding and doomscrolling is not that both are harmful.
It is that both are useful ignition mechanisms with no built-in exit condition.

Infinite-scrolling research describes users feeling caught in a loop, with sessions regretfully
elongated by always-available next content. Reviews of social-media engagement point to variable
rewards, personalized feeds, and endless continuation. Doomscrolling studies link the behavior
with anxiety, pessimism, and lower work engagement. Vibe coding has the same continuation
mechanic with better branding. Each prompt returns something. Each something suggests another
prompt. The next turn might be the one that finally snaps the problem into focus. And because
sometimes it is, the loop is even stickier than entertainment. Oh good, we built a slot machine
with merge permissions.

The difference is that with vibe coding, something real does get built. The productivity
feeling is not entirely false. That's what makes it stickier still — the variable reward
actually delivers sometimes, so the loop runs longer, the exit feels less necessary, and costs
accumulate invisibly until they don't.

---

### The phase argument

The missing distinction is not between AI and discipline. It is between phases of work.

Bjarnason et al.'s empirically-derived model of software prototyping draws a categorical
distinction between two types: exploratory prototypes, which are explicitly throwaway — built
to answer a question, discarded when the question is answered — and evolutionary prototypes,
which are expected to become the final system. The engineering practices for each are opposite.
An exploratory prototype should be fast and cheap; maintainability is irrelevant. An
evolutionary prototype must be built on a foundation that can grow.

Karpathy's 2026 distinction maps almost embarrassingly well onto that frame. Vibe coding is
floor-raising exploratory work. Agentic engineering is what starts when the software is expected
to survive correctness checks, maintenance, security review, and other human beings. The failure
mode is not using vibe coding. The failure mode is quietly letting a throwaway loop become a
shipping process.

---

### The positive case

I know what the exit looks like because I have seen one.

Watershed is a D3D12 puzzle game I have been building — a world that existed in my head for
thirty years before a line of code was written. It started exactly where vibe coding should
start: no settled requirements, no finished design, just a set of questions worth answering.
grass-field-001 through grass-field-004 were not a roadmap. They were probes — four column
raycast renderer prototypes, each one named as a disposable stage, each one answering a
specific visual and technical question before being set aside. The RAII extraction work that
followed was bounded, completable, and local. And the Wave Function Collapse notes, the scalar
field simulation, the formal solvability model — those are the tell. Once those existed,
exploration had crystallized into a system design. That is not vibe coding gone wrong. That
is vibe coding doing its job and then, crucially, getting out of the way.

The staged naming convention is itself evidence. When grass-field-002 answered its question,
a new number started. The WFC notes are a requirements document. They could not have been
written without the exploration that preceded them. They are what the exploratory phase
crystallized into when it was done.

---

### The measurements

The research floor is now sturdy enough that this argument does not need to rely on vibes
about vibes.

METR's early-2025 randomized trial put sixteen experienced open-source developers on 246 real
tasks in mature repositories they knew well and found that AI tools made them 19% slower, even
while they believed they were roughly 20–24% faster. METR's February 2026 update complicates
the story in the right way: with late-2025 tools, the organization saw signs of modest speedups,
but also enough task-selection and participation bias that it no longer trusted the experiment
design as a clean measure. That does not weaken the case here. It strengthens it. The honest
claim is not that AI never speeds developers up. It is that productivity is situational, moving
fast, and astonishingly easy to misperceive.

And speed is not the only bill. Anthropic's January 2026 study found that developers learning
a new Python library scored 17% lower on a follow-up mastery quiz when using AI assistance,
despite only slight and statistically insignificant time savings. Ahmad's April 2026
Comprehension Debt paper gives that cost a name and a mechanism: black-box acceptance, context
mismatch, dependency-induced atrophy, and verification bypass. Liu et al.'s March 2026
large-scale study shows what happens when those habits reach production. Across 304,362 verified
AI-authored commits in 6,275 repositories, they identified 484,606 introduced issues — code
smells, runtime bugs, security vulnerabilities — and 24.2% of those issues still survived at
the latest revision. Not feelings. Not aesthetics. Issues that stayed.

The 39-point perception gap is the most consequential number in that set. Developers in the
wrong phase don't just produce worse outcomes — they believe they are producing better ones.
The feedback signal that would normally indicate "this isn't working" has been suppressed. The
loop continues with confidence it hasn't earned.

---

### What is missing

The solution is not discipline instead of vibe coding. It is discipline about when to stop.

When an agent can implement a well-specified behavior inside a harness of tests, documentation,
rules, and evaluations, forcing a human to type every character is not craftsmanship. It is
theater. The point is not to return to manual implementation. AI-generated code is exactly as
good as the spec and coded behaviors the agent was given. With those in place, generation is
correct and fast. Without them, it is fast and unreliable. The phase boundary is what produces
the spec. That is what is missing — not human keystrokes.

Karpathy's version of the human role is judgment, taste, oversight, and the spec. Fowler and
Thoughtworks make the same move in more formal language: humans shift from inspecting every
generated line to designing the loop the agent runs inside — through specifications, guidance,
and quality checks. Willison's version is similar: the practices that agents reward are the
same old unfashionable ones — planning, testing, documentation, version control. Use vibe
coding to discover what the thing is. Then stop. Then engineer. Everything after that is just
doomscrolling with a CI pipeline.

---

*Systems Engineering Applied to Agentic Systems is a series about making that stop signal
explicit before the whole team ends up wandering the hallway insisting everything feels
productive while the walls quietly catch fire.*
