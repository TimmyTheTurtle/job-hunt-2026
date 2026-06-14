# Articles

Two series. Different tents. Same mission.

> Bringing sanity to agentic development before we're all buried in magical nonsense.

---

## Mission

The central thesis: vibe coding reproduces the engagement dynamics of social media feeds —
prompt-response-reprompt loops that deliver intermittent rewards, low-friction continuation,
and a misleading feeling of progress. The point is not that AI coding tools are bad. The point
is that they become engagement systems unless bounded by software and systems engineering discipline.

The long-range answer is not a single tool. It is an architecture that layers:
- disciplined loops and constraints
- guardrails and quality gates
- durable but selective memory via RAG and contextual retrieval
- graph-backed engineering memory via GraphRAG
- eventually behavioral tuning (LoRA) when prompt/retrieval structure reaches diminishing returns

---

## Series 1 and Series 3 Are Connected

Series 1 diagnoses what happens when you never exit the exploratory phase. Series 3 is the
positive case for what disciplined exploratory phases look like when done right. The Bjarnason
prototyping model (PAM, 2023) provides the formal academic vocabulary for this distinction:
exploratory prototypes (pre-requirements, discovery-oriented) are categorically different from
evolutionary prototypes (requirements-locked). Series 3 is the former done correctly. Series 1
is the former done indefinitely.

When writing either series, cross-reference the other. The argument is incomplete without both.

---

## Token Frugality — Series Throughline

Token frugality is not a cost-cutting tip. It is a design discipline, and it runs through
every layer of the architecture this series describes.

Every architectural decision is simultaneously a token frugality decision:
- **Constraints and guardrails** — filter bad output before the human reviews it; don't spend
  attention tokens on noise
- **RAG** — retrieve the three relevant paragraphs instead of stuffing full docs into context
  or hoping the model's training knowledge is correct
- **GraphRAG** — retrieve structured relationships instead of raw text; denser signal per token
- **SLM routing** — send classification tasks to small cheap models; reserve the frontier model
  for judgment that actually requires it
- **Compact bootstraps and summary layers** — every session's context load is a cost; design it
- **Anti-rampancy** — expire stale context aggressively; don't carry what you don't need

The argument: better context selection produces better outputs AND cheaper runs. These are not
separate benefits. Precision is frugality. Frugality enforces precision.

---

## Editorial Principle

**Each article justifies the next.** Each introduced technology or idea appears because the
previous layer stops paying off or reveals a new failure mode. The series has a staircase
structure, not a random list of AI topics:

1. Identify attention and engagement problems
2. Show cognitive and burnout consequences
3. Show memory and documentation consequences
4. Introduce constraints and guardrails
5. Introduce selective retrieval
6. Introduce graph-structured memory
7. Only later, when those gains flatten, consider model adaptation (LoRA)

---

## Personal Through-Line

A recurring signature idea across the series: there is a real history of documentation friction.
Not keeping enough durable documentation caused loss of rationale, repeated rediscovery, and
confusion. The overcorrection into journals, ADRs, handoffs, and AI-generated lessons creates
a new problem — too much unfiltered documentation buries the reasoning it was meant to preserve.

> Too little documentation and the reasoning is lost. Too much unfiltered documentation and the
> reasoning gets buried. The solution is not more notes — it is better memory architecture.

This through-line connects Articles 4, 6, 7, and 8.

---

## Reusable Framing Lines

- Vibe coding can burn hours and leave behind a working system — but only if treated as a tool
  instead of a feed.
- Bad documentation and vibe coding share the same failure mode: activity without durable
  understanding.
- The future is probably not bigger context windows — it is better selection of what deserves
  to be in context at all.
- What is needed is not more generated text, but a memory architecture that knows what to
  surface and what to leave buried.
- Bringing sanity to agentic development before we're all buried in magical nonsense.

---

## Series 1 — The Vibe Coding Problem

**Audience:** Engineering leaders, senior engineers, CTOs evaluating AI-assisted development.
**Platform:** LinkedIn primary, personal site canonical.
**Cadence:** One article every 10–14 days.

| # | File | Title | Status |
|---|------|-------|--------|
| 1 | [s1-a01](series-1/s1-a01-vibe-coding-doomscrolling.md) | Vibe Coding Is the New Doomscrolling | Not started |
| 2 | [s1-a02](series-1/s1-a02-ai-makes-bad-code-worse.md) | AI Makes Bad Code Worse | Not started |
| 3 | [s1-a03](series-1/s1-a03-shipped-more-felt-worse.md) | I Shipped More and Felt Worse | Not started |
| 4 | [s1-a04](series-1/s1-a04-documentation-fails.md) | Why Documentation Fails in AI-Assisted Development | Not started |
| 5 | [s1-a05](series-1/s1-a05-vibe-coding-without-constraints.md) | Vibe Coding Without Constraints Is Just Vibe Coding | Not started |
| 6 | [s1-a06](series-1/s1-a06-context-poisoning.md) | Context Poisoning | Not started |
| 7 | [s1-a07](series-1/s1-a07-rag-engineering-memory.md) | RAG as Engineering Memory | Not started |
| 8 | [s1-a08](series-1/s1-a08-graphrag-architectural-memory.md) | GraphRAG and Architectural Memory | Not started |
| 9 | [s1-a09](series-1/s1-a09-no-such-thing-clean-agentic-code.md) | There Is No Such Thing as Clean Agentic Code | Not started |
| 10 | [s1-a10](series-1/s1-a10-architecture-im-building.md) | The Architecture I'm Building | Not started |

---

## Series 2 — AI Systems Engineering

**Audience:** Senior engineers, technical leads, AI practitioners.
**Platform:** Personal site primary, LinkedIn secondary.
**Cadence:** No fixed schedule — write in parallel with Series 1, publish when ready.

| # | File | Title | Status |
|---|------|-------|--------|
| 1 | [s2-a01](series-2/s2-a01-tdd-nondeterministic.md) | TDD Doesn't Work for Non-Deterministic Systems | Not started |
| 2 | [s2-a02](series-2/s2-a02-v-model-built-for-this.md) | The V-Model Was Built for This Problem | Not started |
| 3 | [s2-a03](series-2/s2-a03-context-architecture.md) | Context Architecture Is the New Software Architecture | Not started |
| 4 | [s2-a04](series-2/s2-a04-sdlc-vs-runtime.md) | Separating the SDLC Stack from the Agentic Runtime | Not started |
| 5 | [s2-a05](series-2/s2-a05-adversarial-agent-testing.md) | Adversarial Agent Testing: Three Idiots in the Garden | Not started |
| 6 | [s2-a06](series-2/s2-a06-lora-behavioral-tuning.md) | LoRA and Behavioral Tuning as Engineering Discipline | Not started |

---

## Publication Schedule (Series 1)

```
Week 1:   S1-A1   Vibe Coding Is the New Doomscrolling     ← Lead. Everything depends on this.
Week 3:   S1-A2   AI Makes Bad Code Worse
Week 5:   S1-A3   I Shipped More and Felt Worse
Week 7:   S1-A4   Why Documentation Fails
Week 9:   S1-A5   Vibe Coding Without Constraints
Week 11:  S1-A6   Context Poisoning
Week 14:  S1-A7   RAG as Engineering Memory
Week 17:  S1-A8   GraphRAG and Architectural Memory
Week 20:  S1-A9   There Is No Such Thing as Clean Agentic Code
Week 23:  S1-A10  The Architecture I'm Building
```

---

## Candidate Articles (Not Yet Scheduled)

| Candidate | Thesis | Home |
|---|---|---|
| The Complete Cognitive Stack | The positive version of S1-A3 — full operating model: morning reasoning, six-mode rotation, review as first-class mode, daily walk. Nobody in AI dev is writing about the physical layer. | Could extend S1-A3 or be a standalone S1 article. Decide when drafting S1-A3. |
| Acceleration vs. Offloading | The Vibe-Check Protocol (arXiv:2601.02410) names the key distinction: using AI to go faster while maintaining understanding (acceleration) vs. delegating understanding itself (offloading). These produce measurably different outcomes. This is the line between healthy and harmful AI-assisted development — sharper than "vibe coding bad." | Could be S1-A2 material or a standalone. Connects directly to comprehension debt research. |

---

## What This Is Not

This is not a tutorial series. Not "how to use ChatGPT." Not vendor content.

It is a coherent intellectual argument, published in installments, for engineers who are trying
to figure out what rigorous AI-assisted development actually looks like. Every article assumes
the reader is technically literate and tired of hype. The argument should be useful to a senior
engineer even if they never hire the author for anything.

That is how it builds an audience worth having.

---

## Series 3 — Product Discovery in the AI Age

**Audience:** Product engineers, technical founders, engineering leads tired of the MVP treadmill.
**Arc:** Reframe product discovery as a scientific experiment program, not a single-bet pivot game.
**Platform:** LinkedIn and personal site. Cross-links to Series 1 and 2.

| # | File | Title | Status |
|---|------|-------|--------|
| 1 | [s3-a01](series-3/s3-a01-mvp-one-bet-strategy.md) | The MVP Is a One-Bet Strategy | Not started |
| 2 | [s3-a02](series-3/s3-a02-experimentation-is-requirements.md) | Experimentation IS Requirements Gathering | Not started |
| 3 | [s3-a03](series-3/s3-a03-derive-the-product.md) | Derive the Product from the Path of Least Resistance | Not started |

---

## Supporting Files

- [research.md](research.md) — all source links organized by topic
- [PREREQUISITES.md](PREREQUISITES.md) — per-article project prerequisites, SE management requirements, and parallel work map
