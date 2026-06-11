# S1-A3 — I Shipped More and Felt Worse

**Status:** Not started
**Series position:** 3 of 10

---

## Thesis

AI-assisted development done wrong causes measurable cognitive decline — not fatigue, decline.
The same mechanism as doomscrolling: passive consumption replacing active construction, applied
to the cognitive work of engineering. The burnout is not from overwork. It is from competence
erosion.

The specific pattern: AI-assisted development creates a gap between the rate of output and the
rate of understanding. You ship things you don't understand at a pace that prevents you from
ever catching up. The competence signal degrades. The feedback loop that makes engineering feel
meaningful breaks.

---

## Key Claims

- Vibe coding causes cognitive decline through the same mechanism as doomscrolling
- The competence erosion is gradual and invisible until the capability is needed and isn't there
- This is a different burnout than deadline burnout and won't respond to the same interventions
- The counter-move is deliberate: protect active reasoning as a daily practice
- Lesson-first, build-second is the practical inversion of the vibe coding default
- Morning math/physics/calculus is a legitimate engineering practice, not a hobby

---

## Main Points to Discuss

- Burnout and "brain fry" in heavy AI usage — documented by Evil Martians
- Verification burden and hollow productivity: supervising and verifying agents rather than
  writing code produces a different kind of cognitive strain
- Hypervigilance and decision fatigue from rapid-fire AI outputs
- Why more assistance can paradoxically mean more mental strain
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

## Solution Hints to Seed

- Guardrails that reduce oversight burden
- Process that filters low-quality output before the human has to babysit it
- Deliberate daily practice of active reasoning (math, physics, hard problems without AI)
- Lesson-first workflow: get the conceptual map first, then build yourself
- Structured review artifacts (journals, ADRs, handoffs) that give the wait time a job —
  reading the last run's output instead of switching contexts or staring at a spinner

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
- [arXiv 2606.05391 — Human oversight of agentic systems in practice](https://arxiv.org/abs/2606.05391) — 17 developer interviews; documents cognitive load of monitoring agents; closest academic treatment of what developers do while agents run
- [arXiv 2511.06428 — Walking the Tightrope: LLMs for Software Development](https://arxiv.org/abs/2511.06428) — 22 practitioner interviews; names flow disruption as a cost of LLM tools
- [arXiv 2507.03156 — Impact of LLM-Assistants on Developer Productivity](https://arxiv.org/html/2507.03156v1) — cites 23-minute recovery time after interruption applied to LLM workflows
- [RedMonk — 10 Things Developers Want from Agentic IDEs in 2025](https://redmonk.com/kholterhoff/2025/12/22/10-things-developers-want-from-their-agentic-ides-in-2025/) — "fire and forget" as dominant developer fantasy; attention cost of that pattern unexamined
- [Stack Overflow — Agents on a leash: agentic AI remains mostly monitored](https://stackoverflow.blog/2026/05/27/agents-on-a-leash-agentic-ai-remains-mostly-monitored-at-work/) — most developers keep agents on short leashes; baseline for how common the wait-time problem actually is
