# S4-A3 — RAII Applied to Legal Obligations

**Status:** Write now
**Series position:** 3 of 7 — the most original piece

---

## Thesis

Resource Acquisition Is Initialization (RAII) is a C++ pattern for ensuring resources are
acquired and released deterministically, with no leaks and no dangling references. Applied to
legal obligations, it becomes a governance framework: every obligation has a defined lifecycle,
an owner, a scope, and an explicit decommissioning process. When those properties are absent,
predictable failures follow — failures that have direct software engineering analogs and
direct legal consequences.

This framework is not in any existing legal tech literature. It is original.

---

## Key Claims

- RAII semantics map directly onto legal obligation lifecycle management
- The seven RAII defect classes are directly detectable in regulatory and policy corpora
- A DanglingReference (clause pointing to repealed authority) is a use-after-free bug in governance
- A ZombiePolicy (active obligation, repealed authority) is a use-after-free that never faults
- A MissingDestructor (no decommissioning process) is a memory leak in the compliance stack
- An InvariantViolation (obligation that can't be satisfied) is a proof failure
- This framework produces auditable, machine-queryable obligation records

---

## Additional RAII Concepts (for the article's conceptual framing)

Beyond the seven defect classes, three more RAII concepts from the origin framework
belong in the introductory framing of the article — they explain why the analogy runs
deeper than just "resource lifecycle":

**Exception Safety → Regulatory Churn Handling.** In C++, exception-safe code guarantees
that a partially completed operation either succeeds completely or leaves the system in
a valid prior state (rollback). In legal systems: when an authority update partially applies
(e.g., a bulletin amends three of five endorsement clauses), the obligation graph must
remain coherent — no partial-update corruption. The compliance stack must be exception-safe.

**Deadlock / Mutex Discipline → Compliance Deadlocks.** Mutual deadlock in concurrent
systems: two threads each hold a lock the other needs. Legal analog: Legal won't approve
a product change until Actuarial reprices it; Actuarial won't reprice until Product signs
off; Product won't sign off until Legal approves. The approval chain deadlocks. Mutex
discipline — naming all locks and establishing strict acquisition order — translates to
named approval dependencies and explicit resolution paths.

**Borrowing vs. Owning → Citation vs. Interpretation.** Rust's borrow checker enforces
that a reference to a value cannot outlive the value itself. Legal analog: a clause that
cites an external authority (a statute, a bulletin, an ISO form) is borrowing from it.
When the authority is amended, the borrow is invalidated unless the clause is revalidated.
Clauses that re-interpret an authority (rather than citing it) are making their own copy
of the semantics — they own the interpretation, but that copy can drift from the source.
The distinction matters for audit: citations are DanglingReference risks; interpretations
are Calculation Rule Drift risks.

---

## The Seven RAII Defect Classes

| Defect Class | Description | Software Analog | Legal Consequence |
|---|---|---|---|
| DanglingReference | Clause points to authority, form, or section that no longer exists | Null pointer dereference | Audit failure; unenforceable obligation |
| ZombiePolicy | Rule or obligation still active; authorizing statute repealed | Use-after-free | Silent noncompliance or unintended enforcement |
| ScopeLeak | Obligation's applicability predicate undefined or unbounded | Memory scope leak | Compliance obligation leaks across products/jurisdictions |
| DoubleOwnership | Same obligation claimed by two teams or systems | Double free | Nobody actually owns it; falls through the cracks |
| ShadowDefinition | Term redefined in endorsement, silently overriding base policy | Variable shadowing | Adjuster applies wrong definition; coverage dispute |
| MissingDestructor | No decommissioning process; obligations accumulate indefinitely | Memory leak | Compliance stack grows unbounded; zombie obligations persist |
| InvariantViolation | A provable compliance invariant is not satisfied by any current rule | Assertion failure | Regulatory violation; unauditable compliance position |

---

## The Typed Obligation Schema

A machine-queryable obligation record:

```
Obligation {
  id:               string           // canonical identifier
  authority_refs:   []AuthorityRef   // statutes, bulletins, ISO forms — versioned
  scope:            ScopePredicate   // jurisdiction, product, channel, effective dates
  triggers:         []TriggerRule    // conditions under which obligation activates
  required_actions: []Action         // what must happen
  evidence:         []EvidenceType   // what proves compliance
  owner:            Team             // who is accountable
  sunset:           Date | null      // expiration condition
}
```

When authority_refs contains a repealed statute: DanglingReference.
When sunset is null and the authorizing statute was repealed: ZombiePolicy.
When scope is undefined or unbounded: ScopeLeak.
When owner contains two teams: DoubleOwnership.
When no current rule satisfies required_actions: InvariantViolation.

This schema makes defects machine-detectable. That is the architectural claim.

---

## Argument Flow

1. **Explain RAII briefly.** C++ pattern: resources acquired in constructor, released in
   destructor, guaranteed by the type system. No leaks. No dangling. Predictable lifecycle.
   The insight: legal obligations are resources. They are acquired (statute passed, policy
   filed, obligation created). They must be released (statute repealed, policy retired,
   obligation decommissioned). When the release path is missing or broken, the same class
   of failures follows.

2. **Walk through each defect class with a synthetic example.** One concrete fictional clause
   per defect type. Show the failure. Name the analog. State the legal consequence.

3. **Introduce the typed obligation schema.** This is what a correctly managed obligation
   looks like as a data record. Show how the schema exposes defects mechanically.

4. **Connect to the InvariantViolation class.** Compliance is a set of invariants that
   must be provable, not just intended. "We intend to comply" is not an audit position.
   "Here is the evidence artifact that proves compliance for obligation ID-0042" is.
   This reframes compliance from an aspiration into a proof obligation.

5. **Connect to Catala.** The Catala programming language (INRIA/Microsoft Research, ICFP 2021)
   found a bug in the official French government implementation of family benefits by
   formalizing the statute. The RAII framework is the obligation lifecycle layer that Catala
   does not yet have — and that the Rules as Code movement is missing entirely.

6. **Tease what this enables.** A linter that flags DanglingReferences when bureaus retire forms.
   An audit query that surfaces ZombiePolicies across a product portfolio. A validation pass
   that proves or disproves InvariantViolation for each jurisdiction before filing. That is
   the tool this framework describes.

---

## Sources

- Merigoux, Chataing, Protzenko. "Catala: A Programming Language for the Law." ICFP 2021.
  Found a bug in French government's family benefits implementation. Microsoft Research /
  INRIA collaboration.
- Grimmelmann, James. "Programming Languages and Law: A Research Agenda." arXiv 2022.
  "IDE for lawyers" vision; legal design patterns as analogs to GoF patterns.
- Coupette et al. "Law Smells." *AI and Law* 2023. Reference for the academic gap.
- OECD "Cracking the Code: Insights and Good Practices from Pathfinder Jurisdictions." 2020.
  Rules as Code framework — no lifecycle management, no RAII analog.
- The RAII pattern itself: Stroustrup, Bjarne. *The C++ Programming Language*. For grounding
  the concept before applying it to legal systems.

---

## Synthetic Examples (to write before publishing)

1. **DanglingReference:** A fictional homeowners policy clause citing "per DOI Bulletin 2019-04"
   where that bulletin was superseded in 2022 — annotation shows the null reference.
2. **ZombiePolicy:** A fictional commercial auto endorsement requiring "arbitration before the
   State Commercial Arbitration Board" — that board was dissolved in 2020. The obligation is
   active; the path to satisfying it does not exist.
3. **InvariantViolation:** A fictional policy that requires "notice within 30 days" in the
   base form and "notice within 14 days" in an attached endorsement — no claims procedure
   satisfies both simultaneously.
