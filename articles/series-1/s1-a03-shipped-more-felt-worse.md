# S1-A3 — I Shipped More and Felt Worse

**Status:** Not started
**Series position:** 3 of 10

---

## Voice and Tone

- **Most personal article in Series 1.** The morning math, the walk, the cognitive rotation
  model — these are Dorian's actual practices. Write in first person without hedging. "I start
  with vector math before anything else" is more credible than "some engineers find it useful
  to..."
- **The title is a confession, not a complaint.** Own it. The piece works because it admits
  the experience before explaining it. Don't back away from the personal register when the
  empirical section arrives — carry the first person through.
- **Tone:** serious and calm, not wounded. The argument is about a structural pattern that
  causes real harm. Naming it clearly is not melodrama — it is precision.
- **The cognitive rotation model and the walk are earned opinion, not advice.** Present them
  as "what I do and why" not "what you should do." The reader can draw their own conclusion.
- **Do not catastrophize.** The floor is bad enough without amplification. Let the 39-point
  perception gap speak without editorial. The facts are dramatic. The prose should be composed.
- **The wait-time attention section is original.** Nobody has written a clean essay on this
  yet (article plan says so). Write it like you know that — with the quiet confidence of
  someone saying something that should have been said already.

---

## Thesis

AI-assisted development done wrong preserves the feeling of momentum while degrading the
competence signal that makes engineering feel real. The problem is not just fatigue. It is
reward without mastery: output arrives, tasks close, diffs land, but understanding does not
keep pace.

The specific pattern: AI-assisted development creates a gap between the rate of output and the
rate of understanding. You ship things you don't understand at a pace that prevents you from
ever catching up. The competence signal degrades. The feedback loop that makes engineering feel
meaningful breaks.

---

## Key Claims

- Gamified AI workflows can preserve momentum while eroding mastery
- The competence erosion is gradual and invisible until the capability is needed and isn't there
- This is now empirically measured, not just felt: controlled trials show the gap
- This is a different burnout than deadline burnout and won't respond to the same interventions
- The counter-move is deliberate: protect active reasoning as a daily practice
- Lesson-first, build-second is the practical inversion of the vibe coding default
- Morning math/physics/calculus is a legitimate engineering practice, not a hobby

## Empirical Grounding (cite these — do not soften)

- **METR RCT (arXiv:2507.09089):** 16 experienced developers, 246 tasks in their own
  mature repos. AI tools produced a 19% increase in task completion *time*. Developers
  estimated they were 20% *faster*. 39-point perception-reality gap. This is not anecdote.
- **Comprehension debt (arXiv:2604.13277):** Engineers using AI completed tasks in similar
  time but scored 17% lower on comprehension quizzes. Names four accumulation patterns:
  AI-as-black-box acceptance, context-mismatch debt, dependency-induced atrophy,
  verification-bypass. Comprehension debt is distinct from technical debt — it lives in
  team cognition, not the codebase. You cannot fix it by refactoring.
- **Fast and Forgettable (arXiv:2604.18538):** RCT comparing Copilot vs. human pair
  programming. Lower workload during session, trend toward worse one-week retention.
  Participants systematically overestimated their own learning when working with AI.
- **Vibe-Check Protocol (arXiv:2601.02410):** Distinguishes acceleration (AI to go faster,
  understanding maintained) from offloading (delegating understanding itself). These produce
  measurably different outcomes. The article should use this distinction — it is the line
  between healthy and harmful AI-assisted development.

---

## Main Points to Discuss

- Burnout and "brain fry" in heavy AI usage — documented by Evil Martians
- Verification burden and hollow productivity: supervising and verifying agents rather than
  writing code produces a different kind of cognitive strain
- Hypervigilance and decision fatigue from rapid-fire AI outputs
- Why more assistance can paradoxically mean more mental strain
- Reward without mastery: visible progress survives even when comprehension stops accumulating
- The cognitive offloading research: knowing you can look something up reduces encoding depth
  (the "Google effect") — vibe coding is the aggressive version applied to engineering skills
- The personal counter-move: starting the day with vector math, calculus, or physics problems
  before AI tools come on — protecting cognitive capability deliberately
- The lesson-first/build-second technique: AI generates the lesson, you build it yourself.
  The build loop is the comprehension check — you can't fake implementing something you
  don't understand. This habit compounds capability in a way generate-and-accept never does.

### The Wait-Time Attention Problem

There is a second, underexamined mechanism of cognitive damage that nobody has written a clean
essay about yet: what happens to your attention while the agent runs.

Multi-tasking during an agent run costs the 23-minute recovery time, which likely exceeds the
value of the task you context-switched to. Passive waiting (staring at the progress bar) is
not rest — it is the same low-engagement idle that doomscrolling produces.

The asymmetry is brutal: agent runs take minutes. Human attention recovery takes 23 minutes.
If you context-switch on every run, the cognitive cost exceeds the productivity gain.

**The solution is already in the workflow — if the workflow was designed correctly.**

When you have structured review artifacts — journals, ADRs, handoffs, evidence bundles — the
wait time is consumed by the review of the previous run's output. You read what the agent did
last time while it does the next thing. The pause is not idle time. It is the human gate
stage that was going to happen anyway.

This is why the documentation system is load-bearing, not optional. Without review artifacts,
agent wait time is dead time that either damages attention (context switch) or trains
passivity (staring). With them, the wait time is the highest-value moment in the cycle:
the moment where understanding is built, the moment that protects cognitive capability.

Workflows with no review artifacts force passivity. Vibe coding has no review artifacts.
That is not a coincidence — it is the same failure mode as the rest of the article.

### The Complete Cognitive Stack

The full counter-model to the burnout and decline pattern this article diagnoses. Nobody
in the AI development space is writing about this — the conversation is all workflow tools,
focus techniques, and prompt strategies. The physical and rotational layers are absent.

1. **Morning active reasoning** — math, physics, calculus before AI tools come on. Protects
   the reasoning faculty deliberately. Non-negotiable.
2. **Cognitive rotation through the day** — six modes: abstract reasoning, structured intake
   (lectures, papers), implementation, play (simulations, experiments), writing, review.
   When one saturates, switch. This is not multi-tasking — it is sequential cycling through
   modes that use different mental muscles. It is how 12-hour days are sustainable.
3. **Review as a first-class mode** — not administrative overhead. The mode that turns
   activity into understanding. Never blocked; there is always something to review.
4. **Documentation as wait-time strategy** — structured review artifacts mean agent pauses
   are consumed by the previous run's review, not by context-switching or passive waiting.
5. **Daily walk (3–5 miles)** — the seventh element, outside the rotation pool entirely.
   Not a cognitive mode — the physical reset that allows the pool to keep running. Walking
   promotes diffuse thinking; stuck problems resolve on the walk in ways they don't at the desk.

This is a complete operating model, not a productivity tip. The vibe coder has one mode
(implementation) and no physical reset. When implementation is blocked or the agent is
running, they are stuck. The engineer with a full rotation pool and a daily walk is never
stuck — they are always in a mode that is productive, and the hard problems solve themselves
on mile three.

**Note for writing:** This section may deserve its own article — the positive version of
this one. S1-A3 is the diagnosis. The treatment article would be its natural companion.
Flag for placement decision when drafting begins.

---

## Solution Hints to Seed

- Guardrails that reduce oversight burden
- Process that filters low-quality output before the human has to babysit it
- Morning active reasoning practice (math, physics) — protect cognitive capability deliberately
- Lesson-first workflow: get the conceptual map first, then build yourself
- Cognitive rotation pool: six modes, switch when saturated, never stuck
- Review as a first-class daily mode — journals, ADRs, agent output, previous builds
- Structured review artifacts that give agent wait time a job
- Daily walk — diffuse mode reset, the physical layer nobody is talking about

---

## Sources

- [AI-assisted engineers are burning out — Evil Martians](https://evilmartians.com/chronicles/ai-assisted-engineers-are-burning-out-is-this-fine)
- [So your developers use AI now — Evil Martians](https://evilmartians.com/chronicles/so-your-developers-use-ai-now-here-is-what-to-know)
- [AI agents, burnout and addiction — Axios](https://www.axios.com/2026/04/04/ai-agents-burnout-addiction-claude-code-openclaw)
- [AI fatigue essay — Siddhant Khare](https://siddhantkhare.com/writing/ai-fatigue-is-real)
- [The hidden penalty of using AI at work — HBR](https://hbr.org/2025/08/research-the-hidden-penalty-of-using-ai-at-work)
- [CodeScene guardrails](https://codescene.com/blog/implement-guardrails-for-ai-assisted-coding)
- [Snyk guardrails for AI coding assistants](https://snyk.io/blog/build-fast-stay-secure-guardrails-for-ai-coding-assistants/)
- [Simon Willison — Embracing the parallel coding agent lifestyle](https://simonw.substack.com/p/embracing-the-parallel-coding-agent) — calls parallel agents "a thermonuclear ADHD amplifier"; notes he can only usefully review one output at a time
- [Pragmatic Engineer — Programming by kicking off parallel AI agents](https://blog.pragmaticengineer.com/new-trend-programming-by-kicking-off-parallel-ai-agents/) — Armin Ronacher: "it's only so much my mind can review"; attention ceiling named but not analyzed
- [arXiv 2606.05391 — Human oversight of agentic systems in practice](../papers/arxiv-2606.05391-human-oversight-agentic-systems.pdf) — 17 developer interviews; documents cognitive load of monitoring agents; closest academic treatment of what developers do while agents run
- [arXiv 2511.06428 — Walking the Tightrope: LLMs for Software Development](../papers/arxiv-2511.06428-walking-the-tightrope.pdf) — 22 practitioner interviews; names flow disruption as a cost of LLM tools
- [arXiv 2507.03156 — Impact of LLM-Assistants on Developer Productivity](../papers/arxiv-2507.03156-llm-assistant-developer-productivity.pdf) — cites 23-minute recovery time after interruption applied to LLM workflows
- [RedMonk — 10 Things Developers Want from Agentic IDEs in 2025](https://redmonk.com/kholterhoff/2025/12/22/10-things-developers-want-from-their-agentic-ides-in-2025/) — "fire and forget" as dominant developer fantasy; attention cost of that pattern unexamined
- [Stack Overflow — Agents on a leash: agentic AI remains mostly monitored](https://stackoverflow.blog/2026/05/27/agents-on-a-leash-agentic-ai-remains-mostly-monitored-at-work/) — most developers keep agents on short leashes; baseline for how common the wait-time problem actually is
- [METR productivity RCT — arXiv:2507.09089](../papers/arxiv-2507.09089-metr-productivity-rct.pdf) — 19% slower, perceived 20% faster; 39-point gap; 16 experienced devs, own repos
- [Comprehension Debt in GenAI-Assisted SE — arXiv:2604.13277](../papers/arxiv-2604.13277-comprehension-debt.pdf) — 17% comprehension drop; four debt patterns; debt in cognition not codebase
- [Fast and Forgettable — arXiv:2604.18538](../papers/arxiv-2604.18538-fast-and-forgettable.pdf) — Copilot vs. pair programming RCT; worse retention; overestimated learning
- [The Vibe-Check Protocol — arXiv:2601.02410](../papers/arxiv-2601.02410-vibe-check-protocol.pdf) — acceleration vs. offloading distinction; measurably different outcomes
- [Mitigating Epistemic Debt — arXiv:2602.20206](../papers/arxiv-2602.20206-mitigating-epistemic-debt.pdf) — Explanation Gate intervention; restored metacognitive engagement
- [Enterprise AI Coding Assistants — arXiv:2601.20112](../papers/arxiv-2601.20112-enterprise-ai-coding-assistants.pdf) — devs spend ~9% of time reviewing AI output; produce more code but delete more too
