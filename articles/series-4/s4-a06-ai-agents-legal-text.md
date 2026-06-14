# S4-A6 — AI Agents Reading Legal Text

**Status:** Blocked on working pipeline
**Blocker:** Needs a functional AI pipeline actually running on the legal corpus (B5 in
PREREQUISITES.md). Plan can be written now. Do not publish until pipeline results exist.

---

## Thesis

A language model reading legal text without a defect taxonomy is doing keyword search with
extra steps. It can surface text that matches a query. It cannot tell you whether that text
is structurally sound. The smell taxonomy in S4-A4 is the schema an AI agent needs to
move from retrieval to diagnosis.

This article describes what that pipeline looks like: not a product review, not a benchmark,
but an architecture — and the specific places where the taxonomy changes what the model can
claim to have done.

---

## The Two Regimes

### Regime 1: AI as retrieval (current state)
- RAG over legal corpus: retrieve relevant clauses, summarize, answer questions
- Contract review tools: extract named entities, flag deviation from standard form
- Legal judgment prediction: predict outcome given precedent text

These systems are good at finding text. They are not designed to diagnose it.

**The failure mode:** a RAG system asked "does this policy cover flood damage?" can retrieve
the flood exclusion clause and say "no." It cannot tell you whether the flood exclusion
contains an UnboundedExclusion that would survive a coverage dispute, or a DanglingReference
to a repealed state flood definition, or a TemporalConflict with an endorsement added two
years later. Those are defects. Retrieval doesn't find them.

### Regime 2: AI as diagnostic agent (what this architecture targets)
- Load a legal document
- Run the smell taxonomy as a structured detection pass — not free-form summarization
- Return typed defect records: smell class, severity, failing clause, rule violated
- Flag where a human expert is required vs. where the defect is mechanical and automatable

This regime requires a typed schema. Free-form generation produces unstructured observations,
not defect records. The taxonomy is the schema that makes the output structured and auditable.

---

## Architecture

```
Input: policy form (PDF or structured text)

Stage 1 — Preprocessing
  - Section segmentation (base form, endorsements, schedules)
  - Term extraction and definition binding
  - Authority reference extraction (statutes, bulletins, ISO forms)

Stage 2 — Smell Detection (per-category passes)
  - Run each of the 10 smell categories as a typed detection task
  - Each task: "Does this clause exhibit [smell class]? If yes, return: clause_id,
    smell_class, severity, evidence, remediation_target."
  - Output: structured defect record or null

Stage 3 — RAII Lifecycle Check
  - For each extracted obligation: populate typed schema
  - Validate: authority_refs resolve to current documents
  - Validate: scope predicate is bounded
  - Validate: sunset condition exists or obligation is explicitly permanent
  - Validate: owner is single, not multiply assigned
  - Flag: InvariantViolation if required_actions cannot be satisfied

Stage 4 — Defect Report
  - Prioritized list: severity × exploitability × coverage impact
  - Audit trail: which rule fired, which clause triggered it, what evidence supports the flag
  - Human review queue: smells that require legal judgment vs. mechanical detections

Output: typed defect report, not a summary
```

---

## What Changes When You Have the Taxonomy

Without taxonomy:
- "This clause looks complex and may create coverage uncertainty."

With taxonomy:
- "Clause 14(b)(ii): ShadowDefinition. The term 'property damage' is redefined in
  Endorsement CGL-2207 without a superceding notice in the base form. Severity: High.
  Coverage disputes in three states have turned on this exact pattern. Remediation:
  add explicit override notice or consolidate definitions."

The second output is auditable. It names the defect. It assigns severity. It points to
the failing clause. It suggests a remediation path. That is the difference between a
language model being a search engine and being a diagnostic tool.

---

## What Remains Blocked

This article cannot be published until:

1. A pipeline implementing Stage 1–3 is running on the real (private) corpus.
2. The pipeline produces real typed defect records — not simulated.
3. The article can report what the pipeline actually found, not what it theoretically would find.
4. All examples in the published version are synthetic, but the architecture section should be
   validated by a working system.

Publishing before the pipeline exists would make this a speculative architecture piece, not
a demonstrated result. The field has enough of those.

---

## Sources

**Primary (peer-reviewed)**
- Lewis et al. "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." NeurIPS 2020.
  RAG foundation — the regime this article extends beyond.
- Koreeda & Manning. "ContractNLI." EMNLP 2021. Best legal NLP retrieval baseline.
- Hendrycks et al. "CUAD." NeurIPS 2021.
- Merigoux et al. "Catala." ICFP 2021. The nearest working system — executable law formalism
  without the smell detection layer.

**Architectural references**
- S4-A3 (RAII schema) — the typed obligation record this pipeline populates.
- S4-A4 (Taxonomy) — the 87 smell classes this pipeline detects.
