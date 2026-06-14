# Article Prerequisites and Project Dependency Map

This document answers two questions for every article:
1. What project work must exist before this article can be written?
2. What does the project's SE documentation trail need to look like before it counts?

The schedule and Gantt live in [ROADMAP.md](ROADMAP.md).
This document governs prerequisites only.

---

## SE Management Standard — All Projects

Before any project can be drawn upon as a source for articles, it must be SE-managed.
An SE-managed project has all of the following:

- `BOOTSTRAP.md` or equivalent startup contract (agent-readable project state)
- `AGENTS.md` / `CLAUDE.md` (AI agent instructions and constraints)
- At least one ADR for the first significant architectural decision
- A defined handoff format (session boundary documentation)
- `BACKLOG.md` or equivalent active work tracking

**Current SE management status:**

| Project | SE-Managed? | Notes |
|---|---|---|
| legal-tech-debt | Yes ✓ | BOOTSTRAP, AGENTS, AGENT_OPERATING_MODEL, ADRs, handoffs, backlog all in place |
| job-hunt-2026 | Partial ✓ | CLAUDE.md, AGENTS.md, master_tracker — sufficient for its purpose |
| Watershed | No — pre-Phase A | Exploration done; no formal Phase A docs yet. Needed before deeper articles draw from it. |
| Granny's House Trials (adversarial) | No | Undocumented; needs extraction into own repo with full SE startup docs |
| WindowConfigurator sandboxes | No | Not started; needs sandbox structure and at least one experiment before RAG articles |

---

## Series 1 — The Vibe Coding Problem

| Article | Status | Project Prerequisites | SE Doc Requirements |
|---|---|---|---|
| S1-A1 Vibe Coding Is the New Doomscrolling | Out for editing | None — Watershed positive case inline | None needed for current draft |
| S1-A2 AI Makes Bad Code Worse | Write now | None | — |
| S1-A3 I Shipped More and Felt Worse | Write now | None | — |
| S1-A4 Why Documentation Fails | Write now | Optional: legal-tech-debt HANDOFF pattern as enrichment | legal-tech-debt already SE-managed ✓ |
| S1-A5 Vibe Coding Without Constraints | Write now | legal-tech-debt `CLAUDE_CONSTRAINTS.md` exists as concrete working example | legal-tech-debt already SE-managed ✓ |
| S1-A6 Context Poisoning | Write now | Optional: legal-tech-debt `AGENT_OPERATING_MODEL.md` as positive architecture example | legal-tech-debt already SE-managed ✓ |
| S1-A7 RAG as Engineering Memory | **Blocked** | WindowConfigurator: at least one RAG experiment running and demoable | WindowConfigurator must be SE-managed before drawing from it |
| S1-A8 GraphRAG and Architectural Memory | **Blocked** | WindowConfigurator: GraphRAG experiment running and demoable | WindowConfigurator must be SE-managed |
| S1-A9 There Is No Such Thing as Clean Agentic Code | Write now (theory); enrich later | Optional: accumulated experience across projects | — |
| S1-A10 The Architecture I'm Building | **Blocked** | legal-tech-debt demo deployed with public URL; synthetic dataset built | All source projects SE-managed |

---

## Series 2 — AI Systems Engineering

| Article | Status | Project Prerequisites | SE Doc Requirements |
|---|---|---|---|
| S2-A1 TDD Doesn't Work for Non-Deterministic Systems | Write now | None | — |
| S2-A2 The V-Model Was Built for This Problem | **Blocked (read first)** | Read arXiv:2602.20684 (Agile V paper) — 2 hrs | — |
| S2-A3 Context Architecture Is the New Software Architecture | Write now | Optional enrichment from any SE-managed project | — |
| S2-A4 Separating the SDLC Stack from the Agentic Runtime | Write now | legal-tech-debt ADR-012 is the primary source ✓ | legal-tech-debt already SE-managed ✓ |
| S2-A5 Adversarial Agent Testing | **Blocked** | Granny's House Trials: own repo, SE-managed, Stage 2 complete, evals framework hands-on | Granny's must be SE-managed with documented Stage 1 and Stage 2 before writing |
| S2-A6 LoRA and Behavioral Tuning | **Do not write** | Hands-on LoRA tuning experience required — minimum 6 months out | — |

---

## Series 3 — Product Discovery in the AI Age

All three articles draw from the Watershed exploration phase, which is already complete.
They can be written without waiting for Watershed to reach Phase A.

| Article | Status | Project Prerequisites |
|---|---|---|
| S3-A1 The MVP Is a One-Bet Strategy | Write now | Watershed exploration phase (done) |
| S3-A2 Experimentation IS Requirements Gathering | Write now | Watershed exploration phase (done) |
| S3-A3 Derive the Product from the Path of Least Resistance | Write now | Watershed exploration phase (done) |

**Note:** If Watershed reaches a formal Phase A with SE documentation before these articles
publish, the formal documents (first ADR, Phase A concept of operations) can be cited as
evidence. They are not required to write — they would strengthen the argument.

---

## Series 4 — Legal Tech Debt

Building toward a peer-reviewed paper. Articles are excerpts and proof-of-concept
publications, not the primary output.

| Article | Status | Project Prerequisites | SE Doc Requirements |
|---|---|---|---|
| S4-A1 Legal systems accumulate tech debt — the analogy is exact | Write now | legal-tech-debt taxonomy exists ✓; litigation mapping in progress | legal-tech-debt SE-managed ✓ |
| S4-A2 The taxonomy: 87 named smells | **Blocked** | All 87 smells documented with synthetic examples and at least one litigation citation each | legal-tech-debt SE-managed ✓ |
| S4-A3 RAII applied to legal obligations | Write now | RAII defect class framework exists ✓ | legal-tech-debt SE-managed ✓ |
| S4-A4 AI agents reading legal text face context poisoning | **Blocked** | Working AI pipeline reading legal corpus (B5 area) | legal-tech-debt SE-managed ✓ |
| S4-A5 What refactoring looks like in a regulated legal corpus | **Blocked** | Substantially more corpus research + at least one worked remediation example | legal-tech-debt SE-managed ✓ |

**Publication policy for all Series 4 articles:**
- All examples are synthetic
- Real corpus analysis informs the taxonomy; real policy text is never published
- Litigation citations (public record) are the evidentiary backbone
- Primary sources: peer-reviewed academic work, court records, regulatory filings, NAIC data
- Accessible sources (blog posts, Wikipedia) are secondary orientation only

---

## What Can Be Worked on in Parallel Right Now

**Write immediately (no blockers):**
- S1-A2, S1-A3, S1-A4, S1-A5, S1-A6, S1-A9
- S2-A1, S2-A3, S2-A4
- S3-A1, S3-A2, S3-A3
- S4-A1, S4-A3

**Read to unblock (2 hrs each):**
- B1: arXiv:2602.20684 → unblocks S2-A2

**Build to unblock (project work):**
- WindowConfigurator: SE-manage the repo, run first RAG sandbox → unblocks S1-A7
- Granny's House Trials: extract to own repo, SE-manage, document Stage 1 → unblocks S2-A5 ramp
- Watershed: begin Phase A, write BOOTSTRAP.md and first ADR → unblocks deeper S3 citations
- legal-tech-debt: complete synthetic examples for all 87 smells → unblocks S4-A2

**Do not start yet:**
- S1-A7, S1-A8, S1-A10 (build blockers)
- S2-A5 (Granny's Stage 2 blocker)
- S2-A6 (experience blocker — do not write for 6+ months)
- S4-A4, S4-A5 (research and build blockers)

---

## Project SE Documentation — What Needs to Happen

### Watershed
Before drawing on Watershed for anything beyond the S1-A1 positive case already written:
- [ ] Create `BOOTSTRAP.md` with current project state
- [ ] Create `AGENTS.md` with agent startup contract
- [ ] Write ADR-001: Phase A concept of operations (scope, goals, first requirements)
- [ ] Define handoff format for session boundaries
- [ ] Create `BACKLOG.md`

### Granny's House Trials (Adversarial Agent Testing)
Before S2-A5 can be written:
- [ ] Extract into own public repo (separate from Watershed)
- [ ] Create `BOOTSTRAP.md`, `AGENTS.md`, `BACKLOG.md`
- [ ] Document Stage 1 fully (what was tested, what happened, what the evidence bundle contains)
- [ ] Write ADR-001: adversarial testing methodology
- [ ] Complete Stage 2 with evals framework

### WindowConfigurator Sandboxes
Before S1-A7 can be written:
- [ ] SE-manage the sandbox directory (BOOTSTRAP.md at minimum)
- [ ] Run and document at least one RAG experiment end-to-end
- [ ] Write a session handoff describing what the experiment showed
- [ ] The experiment must be demoable — not just "it ran" but "here is what it retrieves"
