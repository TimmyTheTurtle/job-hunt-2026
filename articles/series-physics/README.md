# Series Physics — V&V as Woo Prevention

**Working title**: *Can You Build Respectable Science With an LLM That Wants to Write Sci-Fi?*

## Series Thesis

Real physics research on time-rate fields and analogue gravity exists. The problem
is that an LLM's training distribution on these topics is ~99.99% speculative
content — pseudoscience, fringe YouTube, Reddit threads. Ask the LLM a question at
the frontier and it gives you language that sounds like physics but skips the
validation ladder.

This series documents what happens when you apply SE discipline to that problem:
concept dependency graph, experiment records, mandatory category labels (Established |
Toy hypothesis | Speculative extension), and a hard rule that says you cannot advance
a concept without a documented comparison to established physics.

The thesis is not about the physics. The thesis is about the validation loop: does
SE discipline work as a woo-prevention mechanism when the primary tools are an LLM
and a graphics sandbox?

## Relationship to Other Series

- **Series 2** (V&V for agentic systems) is the methodological backbone.
  This series is the case study. S2 explains the theory; S-Physics is the experiment.
- **Series 1** establishes the vibe coding problem. The LLM woo attractor on fringe
  topics is a specific, worst-case variant of the vibe coding pattern.

## What the Physics Project Produces as Evidence

| Physics Phase | What It Tests | Article Evidence |
|--------------|--------------|-----------------|
| Phase 0 | Numerical primitives (grid, gradient) | Shows the baseline — boring establishment before any claims |
| Phase 1 | Time-rate field, proper time accumulation | First validation gate: toy hypothesis compared against known GR formula |
| Phase 2 | Gradient steering, Newtonian comparison | Newtonian comparison harness; designed-in failure (non-closing orbits) documented |
| Phase 3 | Poisson solver, matter-field coupling | First established physics primitive (∇²Φ = 4πGρ) validated in simulation |
| Phase 4 | Wave propagation, interference | Known linear wave equation reproduced; speed measured against coupling constant |
| Phase 5 | Metric, geodesics, light bending | Nordström failure mode hits as designed; scalar model limit documented |
| Phase 6 | Directional fields, frame drag analog | Speculative extension clearly labeled; qualitative comparison only |

## Planned Articles

### SP-A1 — The Woo Attractor (no prerequisite)

**Status**: Ready to draft

**Thesis**: LLM training data on frontier physics topics is biased toward
pseudoscience. The bias is not random — it is structural: popular content about
speculative physics vastly outnumbers peer-reviewed sources. When you ask an LLM
about gravitational time dilation or analogue gravity, it pattern-matches to the
dominant training distribution. The result is confident-sounding answers that skip
the concept hierarchy. This article establishes the problem that the series solves.

**Evidence needed**: The 6/14/2026 failure case in `D:\Repos\physics\docs\research\initial-conversations.md`.
That section shows what happens without the validation gate active — the LLM produced
HLSL shader code for metamaterial propulsion without validating the scalar field model first.

**Cross-series reference**: Series 1, vibe coding as doom scrolling.

---

### SP-A2 — The Concept Dependency Graph as a Stopping Rule (no prerequisite)

**Status**: Ready to draft after SP-A1

**Thesis**: Vibe coding has no internal exit condition. The concept dependency graph
imposes one: you cannot build the next level until you have an experiment record for
the current level. This is the SE equivalent of a type system for claims — it prevents
the LLM from skipping levels. The validation gate document is the proof assistant.

**Evidence needed**: The concept dependency graph in `D:\Repos\physics\docs\project\concept-dependency-graph.md`.
The article shows the structure, explains the category labels, and explains why
advancement gates work where code review alone doesn't.

**Cross-series reference**: Series 2, S2-A1 (TDD doesn't work for non-deterministic
systems — this is the analog for non-deterministic knowledge claims).

---

### SP-A3 — Running Experiment 2a: The First Comparison That Matters

**Status**: Blocked on Phase 0 and Phase 1 validated

**Thesis**: The first meaningful gate is the Newtonian comparison harness in Phase 2.
When the Gaussian T field fails to produce closed ellipses, that is the correct result.
Documenting a designed-in failure as data — not as a bug — is the critical discipline.
The article shows the experiment record, the comparison, and what the divergence from
Newtonian gravity tells you about the toy model.

**Evidence needed**: Completed experiment records for Phase 2, especially exp-2b and exp-2d.

---

### SP-A4 — The Nordström Failure as Feature

**Status**: Blocked on Phase 5 validated

**Thesis**: Scalar gravity theories (Nordström, 1913) predict zero light deflection.
GR (Einstein, 1915) predicts twice as much as Newtonian, and was confirmed by the
1919 eclipse measurement. When the Phase 5 simulation fails to bend light by the GR
amount, that failure is the correct behavior of a scalar model. Knowing in advance
that you're going to hit this ceiling, and being able to document it as the expected
output of the model, is what separates honest simulation from wishful thinking.

**Evidence needed**: Phase 5 experiment records, especially exp-5b (light bending test).

---

### SP-A5 — Did the Validation Loop Work? (no prerequisite on experiments)

**Status**: Can be drafted speculatively; needs experiment evidence to finalize

**Thesis**: The retrospective. Did SE discipline prevent woo drift? Where did the
gates hold? Where did the LLM try to skip levels? What evidence can show that the
validation loop changed the output compared to unstructured generation? This is the
closing argument.

**Evidence needed**: At least Phase 2 experiment records; Phase 5 records to close
the arc fully.

---

## Publication Dependency Map

```
SP-A1 — woo attractor problem             (no prereq — write now)
  └─ SP-A2 — concept graph as stopping rule (after SP-A1 — write now)
       └─ SP-A3 — Newtonian comparison       (needs Phase 2 validated)
            └─ SP-A4 — Nordström failure      (needs Phase 5 validated)
                 └─ SP-A5 — retrospective     (after SP-A4; or partial after SP-A2)
```

## Relationship to ROADMAP.md

This series does not appear in the current 26-week ROADMAP Gantt. SP-A1 and SP-A2
have no experiment prerequisites and can be drafted during the current writing window.
SP-A3 through SP-A5 are blocked on experiment work that is planned but not yet run.

Suggested ROADMAP integration:
- Add SP-A1, SP-A2 to the no-prereq block alongside S3 articles.
- Track the physics experiment phases as build work items (similar to B2 Sandbox 005).
- Schedule SP-A3 after Phase 2 experiments run; SP-A4 after Phase 5.

## What This Series Is Not

This series is not about the physics. It is about the engineering discipline.
The physics is the domain that makes the problem hard — not the finding.

Do not write SP-A3 through SP-A5 without running the experiments. Publishing a
comparison to established physics without the experiment records would be exactly
the failure mode the series is arguing against.
