# S1-A1 — Vibe Coding Is the New Doomscrolling

**Status:** Not started
**Series position:** 1 of 10 — the lead. Everything depends on how well this one lands.

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
compounds debt invisibly. Andrej Karpathy coined the term in February 2025, renamed it
"agentic engineering" a year later, and admitted his own new project was basically hand-written.
That pivot is the opening — not because vibe coding is bad, but because even its inventor
recognized it needs a phase boundary.

The empirical record is now clear: a METR controlled trial with 16 experienced developers found
AI tools made them 19% slower while they believed they were 20% faster — a 39-point
perception-reality gap. Research on comprehension debt found engineers using AI completed tasks
in similar time but scored 17% lower on comprehension quizzes. These are not vibes. They are
measured outcomes of staying in exploration mode past the point where discipline should have
engaged.

---

## Key Claims

- Vibe coding is a valid exploratory phase tool, not a productivity methodology
- The harm comes from never exiting the exploratory phase, not from the tool itself
- The loop mechanics are structurally identical to social media attention mechanics
- The cost is deferred, invisible, and measured — not just felt
- Karpathy's pivot is the honest signal: even the inventor recognized the phase boundary
- The fix is not discipline instead of vibe coding — it is discipline about when to stop

---

## Argument Flow

1. **Open with the Karpathy pivot.** He coined the term, the term embarrassed people, he
   renamed it. That sequence is the article in miniature — name a real behavior, watch the
   industry flinch, watch it rebrand rather than change. Use it to earn the reader's trust
   early: you are not going to do the same thing.

2. **Define the loop mechanics honestly.** Vibe coding has a legitimate on-ramp function.
   When you have no momentum, no inspiration, no clear starting point — the low-friction
   prompt-response loop gets you into a problem space you might not have entered otherwise.
   The intermittent reward is doing real work here. Name it. The doomscrolling parallel is
   not "both are purely harmful." It is "both are useful ignition mechanisms with no built-in
   exit condition."

3. **Introduce the phase argument.** Exploratory prototyping (pre-requirements, discovery)
   is categorically different from disciplined engineering (requirements-locked). The Bjarnason
   PAM model gives this formal vocabulary. Vibe coding is the right fuel for the exploratory
   engine. The failure mode is running that engine indefinitely.

4. **Drop the empirical floor.** METR: 19% slower, felt 20% faster. Comprehension debt: 17%
   lower quiz scores. 24.2% of AI-introduced defects never cleaned up. These are not
   impressions — they are measurements. The cost of staying in exploration mode past the phase
   boundary is now quantified.

5. **Name what is missing.** Not discipline instead of vibe coding. A phase boundary. An exit
   condition. The question "are we still exploring, or are we building?" asked and answered
   explicitly. Tease that the rest of the series is about how to build the structure that makes
   that question answerable.

## Main Points to Discuss

- What doomscrolling is and how it works psychologically
- What vibe coding is: prompt-driven software generation via conversational interfaces
- The honest case for the engagement loop: it is a valid ignition mechanism, not purely harmful
- The phase argument: exploratory prototyping is categorically different from disciplined
  engineering; the Bjarnason prototyping model (PAM) provides the formal vocabulary
- Similarities between social-media engagement loops and chat-based coding loops when
  the exploratory phase never ends — same failure mode: no exit condition
- Why "productivity feels" can be as sticky as entertainment or outrage
- The empirical record: METR study (19% slower, perceived 20% faster), comprehension
  debt (17% lower quiz scores), 24.2% of AI-introduced defects never cleaned up
- Why the issue is not AI itself but the absent phase boundary

## Solution Hints to Seed (don't solve yet — tease)

- Phase boundaries with explicit exit criteria
- The question "are we still exploring?" asked and answered
- Memory and constraints that engage when the formal phase begins

---

## Concrete Example — Watershed (Granny's House Trials)

The strongest counter to "vibe coding is always harmful" is a worked positive case. Watershed
(D3D12 puzzle game, formerly Granny's House Trials) is pre-phase A exploration done right.

**What happened:** Started with no requirements — a 30-year-imagined world, a rough sense of
puzzle mechanics, no game design document. AI-assisted vibe coding drove a series of bounded
throwaway experiments:
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

- [Andrej Karpathy coins "vibe coding" — Simon Willison](https://simonwillison.net/2025/Mar/19/vibe-coding/)
- [Karpathy admits he hand-coded his new project — Futurism](https://futurism.com/artificial-intelligence/inventor-vibe-coding-doesnt-work)
- [Karpathy renames vibe coding to "agentic engineering" — SD Times](https://sdtimes.com/ai/andrej-karpathy-has-renamed-vibe-coding-heres-what-engineering-leaders-need-to-do-about-it/)
- [Doomscrolling overview — Wikipedia](https://en.wikipedia.org/wiki/Doomscrolling)
- [Doomscrolling and feedback loops — Da More Mental Health](https://damorementalhealth.com/doomscrolling/)
- [Psychology of doomscrolling — Rowan Center LA](https://rowancenterla.com/psychology-of-doom-scrolling-explained/)
- [Vibe coding overview — Wikipedia](https://en.wikipedia.org/wiki/Vibe_coding)
- [Replit on vibe coding](https://replit.com/blog/what-is-vibe-coding)
- [Martin Fowler on humans and agents](https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html)
- [METR productivity RCT — AI made experienced devs 19% slower, they felt 20% faster](https://arxiv.org/abs/2507.09089) — arXiv:2507.09089; 16 developers, 246 tasks, own mature repos
- [Comprehension Debt in GenAI-Assisted SE Projects](https://arxiv.org/abs/2604.13277) — arXiv:2604.13277; 17% lower comprehension quiz scores; comprehension debt distinct from technical debt
- [Debt Behind the AI Boom — large-scale empirical study](https://arxiv.org/abs/2603.28592) — arXiv:2603.28592; 304,362 AI commits, 24.2% of AI-introduced defects never cleaned up
- [Empirically Based Model of Software Prototyping — Bjarnason et al. 2023](https://dl.acm.org/doi/10.1007/s10664-023-10331-w) — formal PAM vocabulary; exploratory vs. evolutionary prototypes are categorically distinct
- [Vibe Coding in Practice: Flow, Technical Debt, and Guidelines](https://arxiv.org/abs/2512.11922) — arXiv:2512.11922; flow-debt trade-off; proposes phase handoff sustainability guidelines
