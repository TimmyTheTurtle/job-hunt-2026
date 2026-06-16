# Vibe Coding Is the New Doomscrolling
### Draft 3

---

Every tool has a right phase. Vibe coding — AI-assisted development where code arrives faster
than comprehension — is exactly right for exploration: when you have no requirements, no settled
architecture, no clear starting point, and the point is to find out what you're building rather
than to build it. In that phase, the low-friction prompt-response loop is the right engine.
Generation without full comprehension is a feature, not a defect.

The phase ends. The tool doesn't know that.

When you have no obvious starting point, the loop gets you inside the problem — the model
generates something wrong, or pointed sideways, but now you are looking at a concrete artifact,
and your brain starts doing the real work of evaluating it. That is the value. The problem is
structural: there is no exit condition built in. The same mechanics that make the loop useful
for exploration make it easy to continue past the point where exploration should have stopped.

Andrej Karpathy demonstrated the distinction before he had fully articulated it. In October
2025, when asked how much of nanochat he had written himself, he said it was basically entirely
by hand — Claude and Codex agents had been net unhelpful there. That was a phase boundary
decision: the work required comprehension the agents were not providing. By April 2026, at
Sequoia Ascent, he named the distinction directly. Vibe coding raises the floor. Agentic
engineering raises the ceiling. Same technology, two different relationships to it, and the
phase is what determines which you're in.

---

### The doomscrolling parallel

Both are useful ignition mechanisms with no built-in exit condition. The parallel is
structural, not punitive.

Doomscrolling research identifies the mechanism: variable rewards, always-available next
content, sessions that elongate past the point the user intended to stop. The same mechanics
run in a vibe coding session. Each prompt returns something. Each something suggests another
prompt. The next turn might be the one that finally snaps the problem into focus. And because
sometimes it is, the loop is stickier than entertainment. Oh good, we built a slot machine
with merge permissions.

With vibe coding, something real does get built. The productivity signal is genuine — which
is exactly what makes the loop run longer than it should.

---

### The phase argument

The distinction that matters is between phases of work.

Bjarnason et al.'s empirically-derived model of software prototyping separates two
categorically different types: exploratory prototypes — explicitly throwaway, built to answer
a question and discarded when the question is answered — and evolutionary prototypes, expected
to become the final system. The engineering practices for each are opposite. An exploratory
prototype should be fast and cheap; maintainability is irrelevant. An evolutionary prototype
must be built on a foundation that can grow.

Karpathy's 2026 distinction maps directly onto that frame. Vibe coding is floor-raising
exploratory work. Agentic engineering is what starts when the software is expected to survive
correctness checks, maintenance, security review, and other human beings. The failure mode is
quietly letting a throwaway loop become a shipping process.

---

### The positive case

I know what the exit looks like because I have seen one.

<!-- TODO: decide whether to use the project name or "a D3D12 puzzle game I have been building" -->
A D3D12 puzzle game I have been building started exactly where vibe coding should start: no
settled requirements, no finished design, just a set of questions worth answering.
grass-field-001 through grass-field-004 were probes — four column raycast renderer prototypes,
each named as a disposable stage, each one answering a specific visual and technical question
before being set aside. The RAII extraction work that followed was bounded, completable, and
local. And the Wave Function Collapse notes, the scalar field simulation, the formal
solvability model — those are the tell. Once those existed, exploration had crystallized into
a system design. Vibe coding had done its job and, crucially, gotten out of the way.

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
the story in the right way: with late-2025 tools, they saw signs of modest speedups, but also
enough task-selection and participation bias that they no longer trusted the experiment design
as a clean measure. That does not weaken the case here. It strengthens it. Productivity is
situational, moving fast, and astonishingly easy to misperceive.

Speed is one bill. Comprehension is another. Anthropic's January 2026 study found that
developers learning a new Python library scored 17% lower on a follow-up mastery quiz when
using AI assistance, despite only slight and statistically insignificant time savings. Ahmad's
April 2026 Comprehension Debt paper names the mechanism: black-box acceptance, context
mismatch, dependency-induced atrophy, verification bypass. Liu et al.'s March 2026 large-scale
study shows what happens when those habits reach production. Across 304,362 verified
AI-authored commits in 6,275 repositories, they identified 484,606 introduced issues — code
smells, runtime bugs, security vulnerabilities — and 24.2% of those issues still survived at
the latest revision. Not feelings. Issues that stayed.

The 39-point perception gap is the most consequential number in that set. Developers in the
wrong phase don't just produce worse outcomes — they believe they are producing better ones.
The feedback signal that would normally indicate "this isn't working" has been suppressed. The
loop continues with confidence it hasn't earned.

---

### What is missing

The solution is discipline about when to stop.

Typing every character when a well-specified agent could generate it is theater. AI-generated
code is exactly as good as the spec and coded behaviors the agent was given. With those in
place, generation is correct and fast. Without them, it is fast and unreliable. The phase
boundary produces the spec. That is what is missing.

Karpathy's version of the human role is judgment, taste, oversight, and the spec. Fowler and
Thoughtworks make the same move in more formal language: humans shift from inspecting every
generated line to designing the loop the agent runs inside. Willison's version is the same
idea expressed plainly: the practices that agents reward are the same old unfashionable ones —
planning, testing, documentation, version control. Use vibe coding to discover what the thing
is. Then stop. Then engineer. Everything after that is just doomscrolling with a CI pipeline.

---

*Systems Engineering Applied to Agentic Systems is a series about making that stop signal
explicit — and understanding why, without it, the loop doesn't end on its own.*
