# Series 4 — Legal Tech Debt

**Audience:** Insurance carriers, legal tech practitioners, RegTech engineers, compliance teams,
computational law researchers.
**Platform:** Personal site canonical; LinkedIn for lead articles; academic paper as end target.
**Cadence:** No fixed schedule — write when research is ready. Paper precedes publication of later articles.

---

## Mission

Legal systems accumulate technical debt in exactly the same way software codebases do.
The analogy is not metaphorical — it is structural. The mechanisms are identical, the failure
modes are identical, and the cost is measurable in billions of dollars of litigation, regulatory
fines, and claims leakage.

This series names the patterns, maps the costs, and proposes a framework borrowed from software
engineering that legal and compliance teams can actually use.

---

## Publication Policy

- **All examples are synthetic.** Real corpus analysis informs the taxonomy; real policy text
  is never published. The identities of the guilty parties have been protected.
- **Primary sources:** peer-reviewed academic work, court records, regulatory filings, NAIC
  data, state insurance department decisions, published litigation outcomes.
- **Accessible sources** (blog posts, Wikipedia) are secondary orientation only — never
  the evidentiary backbone of a claim.
- **Building toward a paper.** Articles are proof-of-concept publications and excerpts.
  The taxonomy paper (full 87 smells + RAII framework + empirical cost evidence) is the
  primary academic output. Articles do not substitute for the paper.

---

## Source Material (legal-tech-debt repo — private)

All source documents live in `D:\Repos\legal-tech-debt`. Do not publish raw content
from that repo. Extract insights, write synthetic examples, cite public litigation data.

| File | Content |
|---|---|
| `legal_tech_debt_report.md` | 9-part deep research report — problem definition, academic landscape, pain quantification, competitive landscape, unique contribution, tech stack |
| `legal_code_smell_taxonomy.md` | 87 named smells across 10 categories + 7 RAII defect classes |
| `insurance_policy_smells.md` | 42 policy-specific smells (form & wording, rating rules, regulatory mapping, spec-to-configurator) |
| `insurance_claims_smells.md` | 41 claims-specific smells (coverage determination, valuation, notice, adjuster workflow, subrogation, bad faith) |
| `Real-World Cost Events Mapped to Insurance Legal Code Smells.md` | Named cases, dollar figures, regulatory fines mapped to each smell category |

---

## Academic Context

| Work | Relevance |
|---|---|
| Coupette et al., "Law Smells," *AI and Law*, 2023 | Only peer-reviewed law smell taxonomy — covers 5 smells. This work covers 87+. |
| Grimmelmann, "Programming Languages and Law," arXiv 2022 | "IDE for lawyers" vision; legal design patterns; directly corroborates the approach |
| Merigoux et al., Catala (ICFP 2021) | Policy compiler — closest thing to a formal executable specification for law |
| OECD "Cracking the Code," 2020 | Rules as Code government framework — covers 0 smells, no lifecycle management |
| Stanford CodeX | Global epicenter for computational law — 20 years of adjacent work, same gap |

**The gap nobody is filling:** No existing work combines (a) a formal legal defect taxonomy
rooted in SE, (b) RAII-style obligation lifecycle management, (c) legislative drift detection,
and (d) compliance invariant proof obligations — specifically for the insurance regulatory stack.

---

## Series Articles

| # | File | Title | Status |
|---|------|-------|--------|
| 1 | [s4-a01](s4-a01-analogy-is-exact.md) | Legal Systems Accumulate Tech Debt — the Analogy Is Exact | Write now |
| 2 | [s4-a02](s4-a02-cost-is-measured.md) | The Cost Is Measured | Write now |
| 3 | [s4-a03](s4-a03-raii-legal-obligations.md) | RAII Applied to Legal Obligations | Write now |
| 4 | [s4-a04](s4-a04-taxonomy.md) | The Taxonomy: 87 Named Smells | Blocked — needs synthetic examples |
| 5 | [s4-a05](s4-a05-gap-nobody-fills.md) | The Gap Nobody Is Filling | Write now |
| 6 | [s4-a06](s4-a06-ai-agents-legal-text.md) | AI Agents Reading Legal Text | Blocked — needs working pipeline |
| 7 | [s4-a07](s4-a07-what-refactoring-looks-like.md) | What Refactoring Looks Like in a Regulated Corpus | Blocked — needs more research + worked example |
