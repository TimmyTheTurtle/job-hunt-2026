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

## Main Points to Discuss

- What doomscrolling is and how it works psychologically
- What vibe coding is: prompt-driven software generation via conversational interfaces
- The phase argument: exploratory prototyping is categorically different from disciplined
  engineering; the Bjarnason prototyping model (PAM) provides the formal vocabulary
- Similarities between social-media engagement loops and chat-based coding loops when
  the exploratory phase never ends
- Why "productivity feels" can be as sticky as entertainment or outrage
- The empirical record: METR study (19% slower, perceived 20% faster), comprehension
  debt (17% lower quiz scores), 24.2% of AI-introduced defects never cleaned up
- Why the issue is not AI itself but the absent phase boundary

## Solution Hints to Seed (don't solve yet — tease)

- Phase boundaries with explicit exit criteria
- Clear stopping conditions for exploration
- Memory and constraints that engage when the formal phase begins

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
