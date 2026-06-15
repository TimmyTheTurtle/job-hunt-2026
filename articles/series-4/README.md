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
| `previous-chats/raii-and-legal-tech-debt.md` | Origin document: first development of the RAII framework, defect class names, typed obligation schema, extended RAII analogs (exception safety, deadlock, borrowing/owning) |
| `previous-chats/legal-tech-debt-impact.md` | Origin: legal code smells concept (12-smell precursor list), legal refactorings table (12 entries), legal design patterns, CMMI for law, market valuation framing |
| `lessons/LESSON-2026-06-05-detector-negation-patterns.md` | Empirical pipeline finding: negation-form phrases fire on filing instructions, not policy provisions; node type classification must precede smell detection |
| `lessons/LESSON-2026-06-05-doi-enforcement-accessibility.md` | Accuracy corrections: State Farm $15.6M = Arkansas auto (not homeowners); Louisiana fines = $764,750; KY/TN/OH/WV behind FOIA walls |
| `feasibility-studies/client-pivot-synthesis-2026-06-06.md` | Strategic synthesis: incumbent landscape, best first-customer positioning, generic LLM threat framing |
| `feasibility-studies/external-reports/bull-case-due-diligence-graph-policy-smell-detector.md` | Rich sourcing: GraphCompliance (arXiv:2510.26309), Magesh/Dahl hallucination studies, Insuraviews detail, Harvey AI, SERFF transaction volume |
| `sandboxes/002-claims-regulatory-automation/002-ROI-CASES-FIVE-SMELLS.md` | Detailed ROI per smell category; service pricing structure; corrected dollar figures |

---

## Academic Context

| Work | Relevance |
|---|---|
| Coupette et al., "Law Smells," *AI and Law*, 2023 | Only peer-reviewed law smell taxonomy — taxonomizes 15, demonstrates 5. This work covers 87. |
| Grimmelmann, "Programming Languages and Law," arXiv 2022 | "IDE for lawyers" vision; legal design patterns; directly corroborates the approach |
| Merigoux et al., Catala (ICFP 2021) | Policy compiler — closest thing to a formal executable specification for law |
| OECD "Cracking the Code," 2020 | Rules as Code government framework — covers 0 smells, no lifecycle management |
| Stanford CodeX | Global epicenter for computational law — 20 years of adjacent work, same gap |
| Braz de Souza et al., ScienceDirect 2025 | "Software engineering meets legal texts: LLMs for auto detection of contract smells" — nearest academic neighbor; commercial contracts via LLMs; no regulatory authority hierarchy, no RAII lifecycle |
| GraphCompliance, arXiv:2510.26309, 2025 | Graph-based compliance reasoning: +12–20pt F2 over RAG on regulatory multi-hop tasks — technical validation for S4-A6 architecture direction |
| Magesh et al., JELS 2025 (Stanford RegLab) | Purpose-built legal AI tools hallucinate 17–33%; Lexis+ AI 65% accurate, Westlaw AI 42% — quantified failure rate of current tools |
| Dahl et al., JLA 2024 | General-purpose LLMs hallucinate 58–88% on specific legal questions — baseline for why retrieval alone fails |
| Milliman, "Rate Filing Average Days to Approval — Q2 2025" | CA homeowners: 293 days avg; CO personal auto: 367 days — quantified regulatory friction cost |

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
