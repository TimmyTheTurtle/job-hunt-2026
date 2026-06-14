# S4-A5 — The Gap Nobody Fills

**Status:** Write now
**Note:** Competitive landscape is derived from public academic literature — no proprietary sources needed.

---

## Thesis

Legal NLP, contract analysis AI, and the Rules as Code movement are three adjacent fields
that have all been working near this problem for years. None of them have solved it. The gap
is not invisible — it is structurally unavoidable given each field's starting assumptions.
This series fills it from a software engineering direction that none of them came from.

---

## The Three Adjacent Fields

### 1. Legal NLP (academic)

**What it does:** Named entity recognition, semantic similarity, clause classification,
legal judgment prediction, statute summarization.

**What it does not do:** Defect detection. A legal NLP model can classify a clause as
an exclusion. It cannot tell you whether that exclusion is a TautologicalExclusion
(logical tautology with zero coverage effect) or an UnboundedExclusion (scope so broad
it voids coverage in practice).

**Representative work:**
- Koreeda & Manning. "ContractNLI: A Dataset for Document-Level Natural Language Inference
  for Contracts." EMNLP 2021. Entity inference, not defect detection.
- Chalkidis et al. "LEGAL-BERT: The Muppets Straight Out of Law School." Findings of EMNLP
  2020. Domain adaptation; no smell taxonomy.
- Hendrycks et al. "CUAD: An Expert-Annotated NLP Dataset for Legal Contract Review."
  NeurIPS 2021. Contract review; no regulatory document coverage, no defect categories.

**The gap:** classification ≠ diagnosis. None of this literature names a defect class,
assigns a severity, or produces an actionable remediation target.

### 2. Contract Analysis AI (commercial tools)

**What it does:** Clause extraction, risk flagging, missing-clause detection for standard
commercial contracts. Products: Kira Systems, Luminance, Evisort, Ironclad, others.

**What it does not do:** Regulatory compliance verification. Insurance policy forms are
not commercial contracts — they are regulatory filings subject to form approval, bureau
versioning, state-specific endorsements, and statutory authority hierarchies. The commercial
tools are not designed for this environment.

**The gap:** commercial tools optimize for contract review speed, not regulatory defect
detection. They don't know what a ZombiePolicy is, because they don't model authority
hierarchies.

### 3. Rules as Code (government movement)

**What it does:** Formalizes statutes and regulations into machine-executable rule sets
so that compliance checking can be automated. Active in: New Zealand, Australia, Canada,
UK, Singapore, OECD-supported pilots.

**What it does not do:** Quality engineering. Rules as Code formalizes the rule. It does
not audit the rule for internal consistency, scope leaks, dangling references to repealed
authority, or RAII lifecycle violations. The movement's assumption is that the rule is
well-formed before formalization.

**Representative work:**
- OECD "Cracking the Code." 2020. Survey of pathfinder jurisdictions.
- Merigoux et al. "Catala." ICFP 2021. Found a bug in French law by formalizing it —
  exactly the kind of InvariantViolation this framework would detect, but Catala has no
  obligation lifecycle layer and no smell taxonomy.

**The gap:** formalization without prior defect detection encodes the smells into the
machine-readable form. The defects survive and become executable.

---

## Why SE Is the Right Starting Point

Software engineering solved this class of problem for code in the 1990s and 2000s:
- Fowler (1999): smell taxonomy + refactoring catalog
- PMD, SpotBugs, SonarQube: automated linting with named rules
- RAII: deterministic resource lifecycle management

Legal texts are programs. The domain-specific failure modes differ, but the engineering
framework — named defects, typed rules, automated detection, prioritized remediation — is
the same. The SE community built these tools because unnamed problems cannot be systematically
fixed. The legal domain is thirty years behind on this curve.

The closest existing bridge:
- Grimmelmann 2022: "IDE for lawyers" framing, GoF-style pattern language vision
- Catala 2021: executable law formalism — the tool that found a bug in the French government's
  own implementation. The RAII framework is the layer Catala doesn't have.

---

## Argument Flow

1. **Name the three fields.** Brief, respectful survey of what each one has achieved.
   Legal NLP is real progress. Commercial contract AI is a genuine product. Rules as Code
   is a serious government initiative. None of them are wrong. They are aiming at adjacent
   targets.

2. **Characterize each gap precisely.** For each field, one paragraph: what it does, what
   it doesn't do, what the gap is, and why that gap is structural (not fixable by doing
   more of the same thing).

3. **Explain the SE approach.** Fowler's smell taxonomy was the foundation. Automated
   linting was the infrastructure. RAII was the lifecycle framework. This series is applying
   all three to legal text. That is not a metaphor — it is the same problem class with a
   domain-specific vocabulary.

4. **Locate the paper in this landscape.** The academic gap statement: no existing work
   combines formal legal defect taxonomy + RAII obligation lifecycle + empirical cost
   evidence + machine-queryable obligation schema. This is not filling a small niche.
   It is the first complete framework for legal quality engineering.

5. **End with the invitation.** The tools implied by this framework (linter, audit query,
   compliance invariant prover) don't exist yet. Building them is an open engineering
   problem. The series names the architecture. The paper names the formal foundation.
   The work is open.

---

## Sources

**Primary (peer-reviewed)**
- Coupette et al. "Law Smells." *AI and Law* 2023.
- Koreeda & Manning. "ContractNLI." EMNLP 2021.
- Chalkidis et al. "LEGAL-BERT." Findings of EMNLP 2020.
- Hendrycks et al. "CUAD." NeurIPS 2021.
- Merigoux et al. "Catala." ICFP 2021.
- Grimmelmann. "Programming Languages and Law." arXiv 2022.
- Fowler, Martin. *Refactoring: Improving the Design of Existing Code.* Addison-Wesley, 1999.
  (Primary SE source for smell taxonomy origin.)

**Survey / government documents**
- OECD "Cracking the Code." 2020. (Government document, treated as authoritative for
  Rules as Code movement scope.)
