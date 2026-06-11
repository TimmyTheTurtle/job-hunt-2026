# Article + Build Roadmap

## Dependency Rules

**Can write NOW — no prerequisites:**
S1-A1, S1-A2, S1-A3, S1-A4, S1-A5, S1-A6, S1-A9
S2-A1, S2-A3, S2-A4
S3-A1, S3-A2, S3-A3

**Blocked — read first:**
- S2-A2: read ArXiv 2602.20684 (Agile V paper) before writing

**Blocked — build first:**
- S1-A7: RAG implementation running and demoable
- S1-A8: GraphRAG implementation running and demoable
- S1-A10: synthetic demo dataset built + legal-tech-debt deployed with URL
- S2-A5: Granny's House Trials Stage 2 + evals framework hands-on

**Blocked — experience first (6+ months):**
- S2-A6: LoRA — do not write until hands-on tuning experience exists

---

## Build Work Items

| ID | Item | Estimated Effort | Unlocks |
|----|------|-----------------|---------|
| B1 | Read Agile V paper (ArXiv 2602.20684) | 2 hrs | S2-A2 |
| B2 | Sandbox 005 Stage 002 — manual pilot | 1–2 weeks | internal |
| B3 | Synthetic demo dataset — design | 1 day | — |
| B4 | Synthetic demo dataset — build | 1 week | S1-A10 |
| B5 | Add Claude API call to legal-tech-debt | 1–2 days | S1-A10 |
| B6 | Deploy legal-tech-debt demo with URL | 2–3 days | S1-A10 |
| B7 | Legal-tech-debt case study write-up | 1 week | S1-A10 |
| B8 | Learn evals frameworks (DeepEval / Promptfoo) | 2–4 weeks | S2-A5 |
| B9 | Granny's House Trials Stage 2 | 4–6 weeks | S2-A5 |
| B10 | Personal site build | 1–2 weeks | contractor outreach |

---

## Gantt — 26 Weeks

```
WEEK  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SERIES 1 PUBLICATION (every 10–14 days)
A1        ●
A2              ●
A3                    ●
A4                          ●
A5                                ●
A6                                      ●
A7                                               ●
A8                                                     ●
A9                                                           ●
A10                                                                ●

WRITING — Series 1 (write ahead of publication)
A1–A3   [===]
A4–A6         [======]
A7–A8                     [========]  ← blocked on B4/B5/B6
A9                   [==]
A10                                         [====]  ← blocked on B4/B5/B6

WRITING — Series 2 (no fixed cadence)
S2-A1   [==]
S2-A2    [=]  ← blocked on B1 (read Agile V)
S2-A3         [==]
S2-A4         [==]
S2-A5                                               [====]  ← blocked on B8/B9
S2-A6   ░░░░░░░░░░░░░░░░░░░░░░░░░░░  NOT YET — needs LoRA experience

WRITING — Series 3 (no fixed cadence)
S3-A1   [==]
S3-A2   [==]
S3-A3    [==]

BUILD TRACK
B1      [=]    read Agile V paper
B2      [========]    Sandbox 005 Stage 002
B3          [=]    synthetic dataset design
B4            [=====]    synthetic dataset build
B5                  [==]    Claude API to legal-tech-debt
B6                    [===]    deploy legal-tech-debt demo
B7                       [====]    legal-tech-debt case study
B8            [============]    learn evals frameworks
B9                          [======================]    Granny's Stage 2
B10                    [=======]    personal site build

MILESTONES
Wk 1:   ★ S1-A1 published — series launches
Wk 12:  ★ legal-tech-debt demo live with URL
Wk 15:  ★ personal site live
Wk 23:  ★ S1-A10 published — series complete
Wk 23:  ★ contractor outreach begins
Wk 26+: ★ S2-A5 published (evals + three idiots)
```

---

## First Two Weeks — Exact Actions

Week 1:
- [ ] Write S1-A1 (Vibe Coding Is the New Doomscrolling) — publish end of week
- [ ] Write S1-A2 and S1-A3 — in the queue ahead of schedule
- [ ] Read ArXiv 2602.20684 (Agile V paper) — 2 hours, unblocks S2-A2
- [ ] Write S3-A1, S3-A2, S3-A3 — all argument-based, no prereqs, clear the backlog

Week 2:
- [ ] Begin Sandbox 005 Stage 002
- [ ] Design synthetic demo dataset (fictional company, defect taxonomy)
- [ ] Write S1-A4 and S1-A5
- [ ] Write S2-A1, S2-A2 (if Agile V paper read), S2-A3, S2-A4

---

## What "Contractor Outreach Begins" Means

By week 23:
- 10 Series 1 articles published (full argument arc visible)
- Legal-tech-debt demo live and linked from S1-A10
- Personal site live with work, writing, and contact sections
- Series 2 and 3 articles published on personal site

At that point outreach is inbound-first: the articles are the pitch, not a cold email.
