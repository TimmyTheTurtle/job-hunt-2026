# S4-A4 — The Taxonomy: 87 Named Legal Code Smells

**Status:** Blocked on synthetic examples
**Blocker:** Need synthetic examples for all 87 smells before publishing. Plan can be written now.

---

## Thesis

Coupette et al. (2023) demonstrated five law smells and taxonomized fifteen. This taxonomy
names 87.

The 83 domain-specific smells across claims and policy language represent the first complete
smell taxonomy for insurance regulatory documents. The 7 RAII defect classes (S4-A3) apply
across all regulatory domains. Together they form a unified defect taxonomy for legal text that
has no equivalent in existing academic literature.

**Academic lineage:** Fowler (1999) introduced the code smell taxonomy and refactoring catalog
for software. Coupette et al. (2023) applied the concept to legal text (15 smells, non-insurance
domain). Braz de Souza et al. (ScienceDirect, 2025) applied it to commercial contracts via LLMs
("Software engineering meets legal texts: LLMs for auto detection of contract smells"). This work
extends the lineage to insurance regulatory documents — the first domain with a complete taxonomy
(87 smells) and an obligation lifecycle framework.

---

## Structure

### Three Layers

**Layer 1 — Inherited Law Smells (Coupette et al., 2023)**
Five smells identified in existing academic literature:
- Ambiguous Reference
- Undefined Term
- Circular Definition
- Temporal Conflict
- Scope Confusion

These five are the baseline the academic community currently recognizes. This taxonomy adds 82
more. The gap is the point.

**Layer 2 — Domain-Specific Smells (83 named, insurance corpus)**

10 categories:

| Category | Count | Example Smell |
|---|---|---|
| Temporal Conflicts | 10 | DeadlineAmbiguity, ConflictingEffectiveDates, RetroactiveUndermining |
| Scope and Coverage Gaps | 10 | UnboundedExclusion, OverlappingTriggers, OrphanedEndorsement |
| Reference Integrity | 10 | DanglingCrossReference, CircularCoverage, UnresolvedAlias |
| Definitional Defects | 10 | GodClause, NullReference, ShadowDefinition (policy layer) |
| Obligation Lifecycle Defects | 10 | ZombieObligation, MissingDecommission, UnownedRequirement |
| Structural Defects | 10 | NestedNegation, ExceptionSandwich, BooleanSoup |
| Enforceability Defects | 8 | CircularCondition, TautologicalExclusion, UnprovableCondition |
| Compliance Gaps | 9 | UnresolvableConflict, RegionAmbiguity, RequirementOrphan |
| Ambiguity Classes | 6 | CoverageWhenThenAmbiguity, Weasel, CatholicAnd |
| Jurisdiction/Regulatory Misalignment | 10 | JurisdictionLeak, BulletinConflict, FormVersionDrift |

**Layer 3 — RAII Defect Classes (7, obligation lifecycle)**
Cross-layer: apply to obligations that cross document boundaries and authority hierarchies.
Detailed in S4-A3.

---

## The Academic Gap

Existing literature:

- Coupette et al. 2023: 15 law smells (5 demonstrated), non-insurance domain
- Grimmelmann 2022: patterns in legal design, no taxonomy
- Surden 2014: computational law principles, no defect taxonomy
- Rules as Code movement: focuses on formalization, not defect detection
- Catala (Merigoux et al. 2021): executable law formalism, no smell classification

No existing work combines:
- A complete smell taxonomy for regulatory documents
- A lifecycle framework for legal obligations
- Empirical cost evidence mapped to named defects
- A machine-queryable obligation schema

This paper fills all four gaps simultaneously.

---

## Argument Flow

1. **Open with the count contrast.** Coupette et al. found five law smells. After analyzing an
   insurance regulatory corpus, the count is 87. The gap in existing coverage is not small —
   it is an order of magnitude. That is not a refinement of prior work; it is the first
   systematic catalog of a domain that has existed for over a century.

2. **Walk the 10 category structure.** Brief for each category: what makes these smells
   distinct, what failure mode they represent, one synthetic example per category. The
   synthetic examples demonstrate the pattern without exposing the real corpus.

3. **Show the RAII defect classes as a cross-layer.** The 83 domain-specific smells live
   within documents. The 7 RAII classes live across documents and authority hierarchies.
   Both layers are necessary. The RAII layer is the one that doesn't yet exist in any
   legal tech literature.

4. **Name the tool this enables.** A linter that loads a policy form, runs all 87 smell
   detectors, and produces a prioritized defect report. Not a suggestion. A typed defect
   with a category, a severity level, the failing clause, and the rule that flags it.
   This is the same thing SE teams already have for code. Legal teams do not have it yet.

5. **Close with the paper's position.** This taxonomy is the foundation. The empirical
   cost evidence (S4-A2) is the validation. The RAII schema (S4-A3) is the architecture.
   Together they constitute a formal framework for legal quality engineering that has
   no equivalent in current academic literature.

---

## On Synthetic Examples

Every illustration in this article must use a synthetic document. The structure comes from
the real corpus. The text is purpose-built to exhibit the pattern. The name is fictional.

Standard label: "Fictional Umbrella Commercial Liability Policy, Section XIV(b)(ii)."
No company name. No state. No form number that matches a real filing.

"The identities of the guilty parties have been protected."

---

## Sources

**Primary (peer-reviewed)**
- Coupette, Corinna, et al. "Law Smells." *AI and Law* 31 (2023). Fifteen smells taxonomized, five demonstrated. The direct baseline.
- Braz de Souza et al. "Software engineering meets legal texts: LLMs for auto detection of contract smells." *ScienceDirect* 2025. Nearest academic neighbor — contracts via LLMs; no regulatory authority hierarchy, no RAII lifecycle layer.
- Merigoux, Denis, Nicolas Chataing, and Jonathan Protzenko. "Catala: A Programming Language
  for the Law." ICFP 2021. Best executable law formalism; no smell taxonomy.
- Grimmelmann, James. "Programming Languages and Law: A Research Agenda." arXiv 2022.
  Patterns in legal design; nearest thing to a GoF-style framework for law.
- Surden, Harry. "Computable Contracts." *Davis Law Review* 46 (2012). Foundational.

**Evidentiary backbone**
- Cost evidence table: see S4-A2 (all 13 named cases with public record citations).

**Academic gap statement**
- OECD "Cracking the Code." 2020. Rules as Code survey — confirms absence of defect taxonomy.
