# S4-A7 — What Refactoring Looks Like

**Status:** Blocked on more research
**Blocker:** Needs more completed smell taxonomy + real remediation examples from corpus work.
  Plan can be written. Do not publish without empirical remediation examples.

---

## Thesis

Fowler's refactoring catalog maps each code smell to a named refactoring: Extract Method,
Replace Magic Number, Introduce Parameter Object. The legal equivalent exists. It is not
documented anywhere. This article documents it for the smells where the remediation pattern
is clear, and names the open problems where it is not.

This is the "so what do we actually do about it" article. Every series that names a problem
eventually needs this piece. Series 4 earns the right to write it only after the taxonomy
(S4-A4) and the cost evidence (S4-A2) have been published.

---

## Refactoring Catalog Structure

For each named smell: the defect, the canonical refactoring, the precondition for applying it,
and the risk of misapplication. Same structure as Fowler's original catalog.

### Selected Refactoring Entries (to expand with full taxonomy before publishing)

**GodClause → Extract Definition + Introduce Scope Predicate**
- Smell: a single clause governs all coverage, all exclusions, all conditions, and all
  definitions simultaneously. No structure. Maximum coupling.
- Refactoring: extract each logical component into a named section with a bounded scope.
  Introduce explicit scope predicates (applies to: commercial auto, not personal lines).
- Precondition: the extracted sections must be individually filed and approved in all
  jurisdictions where the form is active. Refactoring a God Clause without refiling is
  itself a regulatory violation.
- Risk: inadvertent coverage expansion or restriction if extraction changes the effective
  scope of any component. Requires legal review before filing.

**DanglingReference → Update Authority Reference or Insert Supersession Notice**
- Smell: clause references a statute, bulletin, or form that has been repealed or superseded.
- Refactoring (path A): update the reference to the current authority.
- Refactoring (path B): if the original authority's requirements are still operationally
  correct, insert a supersession notice: "As governed under [current authority], which
  superseded [original reference] effective [date]."
- Precondition: confirm that the current authority contains equivalent or more specific
  requirements. Do not substitute a new authority that changes substantive requirements
  without filing review.
- Risk: path B can create a TemporalConflict if the new authority has different effective
  dates. Verify authority timelines before applying.

**ZombiePolicy → Explicit Decommission or Statutory Replacement**
- Smell: active obligation; the authority that created it was repealed. The obligation
  continues with no valid basis.
- Refactoring (path A): decommission the obligation with a dated retirement record that
  documents the authority change.
- Refactoring (path B): identify the replacement statutory basis and re-anchor the
  obligation under the new authority.
- Precondition: confirm that the obligation is not implicitly required by a separate,
  still-active authority that was not identified in the original obligation record.
  Decommissioning a zombie that is actually required under a different authority creates
  a compliance gap.
- Risk: high. Requires legal sign-off on the authority chain before any decommission.

**MissingDestructor → Introduce Sunset Condition + Decommission Protocol**
- Smell: obligation has no defined end state. Accumulates indefinitely. Compliance stack
  grows without bound.
- Refactoring: add explicit sunset condition to the typed obligation record. Define the
  decommissioning protocol: who reviews, what triggers review, what the end-state looks like.
- Precondition: the obligation's authorizing statute must not itself be perpetual without
  review cycles. Check the authority's own renewal or sunset provisions.
- Risk: low if done correctly. The principal risk is setting an overly short sunset that
  decommissions an obligation before the underlying requirement actually expires.

**InvariantViolation → Resolve Conflict or Accept Partial Coverage Statement**
- Smell: no claims procedure satisfies all current obligations simultaneously. The invariant
  is provably unsatisfied.
- Refactoring (path A): identify and eliminate the conflicting obligation. One of them is
  wrong. Determine which.
- Refactoring (path B): issue a conflict acknowledgment: "In [jurisdiction X], the 14-day
  notice requirement (Endorsement CGL-2207) governs. In all other jurisdictions, the 30-day
  notice requirement (base form Section 8.2) governs."
- Precondition: path B is only acceptable when the conflict is jurisdictional. A within-
  jurisdiction conflict cannot be resolved by acknowledgment — it must be resolved by
  eliminating one of the conflicting obligations.
- Risk: path B without proper jurisdictional scoping can create a ScopeLeak that makes
  the conflict worse.

---

## What This Catalog Lacks (Open Problems)

**Smells that resist mechanical remediation:**
- BooleanSoup: complex nested boolean logic in coverage conditions. The "correct" refactoring
  depends on intent, which may not be recoverable from the text alone.
- CoverageWhenThenAmbiguity: "when X occurs" vs. "if X has occurred" — temporal ambiguity
  that requires legal interpretation to resolve, not structural refactoring.
- Weasel: "reasonable," "substantial," "material" — intentionally vague terms that resist
  definition without changing the practical scope of the obligation.

**These are the cases that require a human expert.** The linter can flag them. The audit
report can prioritize them. The remediation requires legal judgment. The framework names
the limit of automation honestly.

---

## Argument Flow

1. **Establish the analogy to Fowler's catalog.** Refactoring is not rewriting. It is a
   named transformation that preserves behavior while improving structure. The legal
   equivalent: a named transformation that preserves the substantive obligation while
   eliminating the structural defect. Same discipline, domain-specific vocabulary.

2. **Walk five refactoring entries in full detail.** Smell → canonical refactoring →
   preconditions → risks. Each entry should be concrete enough that a compliance team
   could use it as a checklist.

3. **Name the open problems.** The smells that resist mechanical remediation are not
   failures of the framework. They are the framework being honest. "This requires a
   human expert and here is why" is a stronger claim than pretending everything is
   automatable.

4. **Close with the tooling implication.** A linter that detects GodClauses and outputs
   "Apply: Extract Definition + Introduce Scope Predicate" is a useful tool. A compliance
   team that receives a typed defect report with a named remediation and a precondition
   checklist is not starting from scratch. That is what the framework enables.

---

## Sources

**Primary (peer-reviewed)**
- Fowler, Martin. *Refactoring: Improving the Design of Existing Code.* Addison-Wesley, 1999.
  The structural foundation. The catalog format is Fowler's.
- Coupette et al. "Law Smells." *AI and Law* 2023. Comparison baseline.
- Grimmelmann 2022. "IDE for lawyers" vision — this article is the nearest thing to making
  that vision concrete.

**Internal cross-references**
- S4-A3: RAII defect classes → refactoring entries for DanglingReference, ZombiePolicy,
  MissingDestructor, InvariantViolation
- S4-A4: full taxonomy → the remaining 82 smells need refactoring entries before this
  article is complete
- S4-A2: cost evidence → each refactoring entry should cite the cost case where this
  defect class materialized
