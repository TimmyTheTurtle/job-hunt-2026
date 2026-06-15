# Article + Build Roadmap

## Dependency Rules

**Can write NOW — no prerequisites:**
S1-A1, S1-A2, S1-A3, S1-A4, S1-A5, S1-A6, S1-A9
S2-A1, S2-A3, S2-A4
S3-A1, S3-A2, S3-A3

**Blocked — read first (~3–4 hrs total):**
- S2-A2: read arXiv:2602.20684 (Agile V, Koch & Wellbrock) + arXiv:2605.20456 (Agentic Agile-V, SCOPE-V loop) before writing.
  Also read: arXiv:2512.12791 (Beyond Task Completion) + arXiv:2603.02601 (AgentAssay) — these are the missing sources for Problem 3.

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

## Two Tracks, One Schedule

**Track A — Contract Sprint (weeks 1–8):** minimum viable credibility stack for a first contract.
Goal: one paying client by week 8. Low hours, enough to live on, keep learning.

**Track B — Long Game (weeks 1–26):** articles, deep build work, full contractor pitch.
Goal: inbound-first outreach at week 23 with full credibility stack in place.

Week 2 is a planned light week (family visit). No pressure, no catch-up required.

---

## Gantt — 26 Weeks

```
WEEK  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CONTRACT SPRINT (Track A) — 8 week hard target
Demo live                [=========]  ← target: end of wk 4
Personal site (1-pager)          [====]  ← target: end of wk 4
S1-A1 published          ●
Outreach begins                              ●  ← wk 6
First contract conversations                      [====]

SERIES 1 PUBLICATION (Track B — audience pacing, every 10–14 days)
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

WRITING — Series 1 (write well ahead — full days available)
A1      [=]   ← wk 1, publish immediately
A2–A3   [==]
A4–A6      [======]
A7–A8                  [========]  ← blocked on B4/B5/B6
A9               [==]
A10                                      [====]  ← blocked on B4/B5/B6

WRITING — Series 2 (no fixed cadence)
S2-A1   [==]
S2-A2    [=]  ← blocked on B1 (read Agile V)
S2-A3      [==]
S2-A4      [==]
S2-A5                                            [====]  ← blocked on B8/B9
S2-A6   ░░░░░░░░░░░░░░░░░░░░░░░░░░░  NOT YET — needs LoRA experience

WRITING — Series 3 (no fixed cadence)
S3-A1   [==]
S3-A2   [==]
S3-A3    [==]

BUILD TRACK
B1      [=]    read Agile V paper
B2      [========]    Sandbox 005 Stage 002
B3      [=]    synthetic dataset design  ← moved to wk 1
B4       [====]    synthetic dataset build  ← moved to wk 2–3
B5           [==]    Claude API to legal-tech-debt  ← moved to wk 3
B6             [=]    deploy legal-tech-debt demo  ← moved to wk 4 (★)
B7               [====]    legal-tech-debt case study
B8         [============]    learn evals frameworks
B9                      [======================]    Granny's Stage 2
B10      [====]    personal site — 1-pager first  ← moved to wk 1–4 (★)

MILESTONES
Wk 1:   ★ S1-A1 published — series launches
Wk 1:   ★ S3-A1, S3-A2, S3-A3 written (argument-only, no blockers)
Wk 2:   ~ light week (family visit)
Wk 4:   ★ legal-tech-debt demo live with URL  ← MOVED FROM WK 12
Wk 4:   ★ personal site (1-pager) live  ← MOVED FROM WK 15
Wk 6:   ★ first contract outreach (5–10 targets)
Wk 8:   ★ first contract conversations in progress
Wk 23:  ★ S1-A10 published — series complete
Wk 23:  ★ full contractor outreach (inbound-first, articles are the pitch)
Wk 26+: ★ S2-A5 published (evals + three idiots)
```

---

## Week-by-Week — First Eight Weeks

**Week 1 (full capacity):**
- [ ] Write and publish S1-A1
- [ ] Write S1-A2, S1-A3, S3-A1, S3-A2, S3-A3 — clear the no-prereq backlog
- [ ] Design synthetic demo dataset (B3) — 1 day
- [ ] Start personal site skeleton (B10)
- [ ] Read Agile V paper (B1) — 2 hrs, unblocks S2-A2

**Week 2 (light — family visit):**
- Study, reading, no build pressure
- Write S2-A1 if energy is there

**Week 3:**
- [ ] Build synthetic dataset (B4)
- [ ] Wire Claude API into legal-tech-debt pipeline (B5)
- [ ] Write S1-A4, S1-A5, S2-A2, S2-A3, S2-A4

**Week 4:**
- [ ] Deploy legal-tech-debt demo with public URL (B6) ← hard target
- [ ] Personal site 1-pager live with demo link (B10) ← hard target
- [ ] Begin legal-tech-debt case study write-up (B7)

**Week 5:**
- [ ] S1-A2 publishes
- [ ] Begin Sandbox 005 Stage 002 (B2)
- [ ] Write S1-A6, S1-A9

**Week 6:**
- [ ] First contract outreach — 5–10 targets, cold but specific
- [ ] S1-A3 publishes
- [ ] Learn evals frameworks begins (B8) — background track

**Weeks 7–8:**
- [ ] Follow up outreach, first conversations
- [ ] S1-A4 publishes (wk 7)
- [ ] Continue Series 2 writing, evals learning

---

## What "First Contract Outreach" Means at Week 6

Minimum viable pitch at that point:
- S1-A1 published (shows thinking)
- Legal-tech-debt demo live (shows capability)
- Personal site with demo link and contact (shows seriousness)

Outreach is targeted, not spray: legal, compliance, insurance, document-heavy domains.
5–10 specific targets, direct message or email, one paragraph, link to demo.
Not a cold resume blast — a specific "I built this, you have this problem" message.

---

## What "Full Contractor Outreach" Means at Week 23

By week 23:
- 10 Series 1 articles published (full argument arc visible to anyone who searches)
- Legal-tech-debt demo live and linked from S1-A10
- Personal site with work, writing, and contact sections fully built out
- Series 2 and 3 articles published on personal site

At that point outreach is inbound-first: the articles are the pitch, not a cold email.
