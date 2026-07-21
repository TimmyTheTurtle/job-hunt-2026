# The Architecture I'm Building
### Draft 1 - expanded working draft / research packet

---

## Working Note

This is the closing argument, so it cannot read like a bag of components.

It has to feel like the whole series resolving into a system:

- A1 named the problem
- A2 through A4 showed what it damages
- A5 introduced friction and verification
- A6 through A8 introduced memory design
- A9 reframed the discipline
- A10 says: here is the stack that makes all of that operational

This article is also where claims need the most caution.
Do not overstate what exists.

---

## Core Argument

The answer to gamified continuation is not a single tool and not a single prompt pattern.
It is an architecture with:

- explicit phase boundaries
- verification layers
- curated memory
- relational memory where needed
- automation that enforces constraints
- human gates where judgment cannot be safely delegated

This article should feel domain-agnostic in principle, but grounded by one concrete document
intelligence / legal-tech-debt implementation.

Need a sharper opening line for the eventual essay:

> If the problem is a work system that makes continuation cheap and stopping unnatural, then the
> answer is a system that makes boundaries, evidence, and acceptance explicit.

That is what the architecture has to be shown doing, not just containing.

---

## What This Article Has To Do

1. explicitly answer A1
2. credit Agile V clearly and carefully
3. show where the original extension begins
4. describe the layered stack as staged, not fantasy
5. close with a modest outreach paragraph rather than a sales pitch

---

## Research Spine

### 1. Agile V is the governance spine

The paper gives the clean formal frame:

- AI-assisted engineering lacks built-in task-level verification and traceability
- Agile V merges agile iteration with V-model verification
- mandatory human approval gates remain part of the cycle
- audit-ready artifacts are generated as part of work

That is exactly why it belongs at the center of the architecture article.

Source:
- [Agile V: A Compliance-Ready Framework for AI-Augmented Engineering -- From Concept to Audit-Ready Delivery](https://arxiv.org/abs/2602.20684)

### 2. Retrieval and contextual retrieval are the memory layer

This article does not need to re-explain A7, but it should summarize the layer:

- archive is larger than active context
- retrieval determines what becomes active
- contextual retrieval and reranking improve the chance of surfacing the right evidence

Source:
- [Introducing Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval)

### 3. GraphRAG is the relational memory layer

Needed when the system must reason over dependency, lineage, and cross-document structure rather
than only semantic similarity.

Sources:

- [Project GraphRAG](https://www.microsoft.com/en-us/research/project/graphrag/)
- [From Local to Global: A Graph RAG Approach to Query-Focused Summarization](https://www.microsoft.com/en-us/research/publication/from-local-to-global-a-graph-rag-approach-to-query-focused-summarization/)

### 4. Systems engineering life-cycle support

The FHWA life-cycle overview is useful because it keeps the article from sounding invented out
of thin air. The deeper message is that explicit lifecycle thinking remains relevant even when
the implementation substrate changes.

Source:
- [FHWA systems-engineering life cycle](https://ops.fhwa.dot.gov/seits/sections/section2/2_7.html)

### 5. Why this architecture should be staged, not totalizing

Need a sober paragraph here. Otherwise the article risks reading like architecture maximalism.

The sequence should be defended like this:

- first add phase boundaries and verification
- then fix memory selection
- then add relational memory if the questions demand it
- only later consider behavioral tuning

That sequence is not only pragmatic. It is epistemically cleaner. It makes each new layer answer
an already observed failure mode rather than arriving as speculative complexity.

---

## The Most Important Attribution Boundary

Need to be extremely careful here.

Agile V is not original to this work.
What may be original is the specific extension into:

- non-deterministic LLM runtime behavior
- eval-heavy verification rather than only unit-test confidence
- LLM-as-judge as triage rather than verification oracle
- non-optional human gates for acceptance
- domain application into document intelligence / legal-tech-debt work

This distinction probably needs its own subsection in the final article.

Possible line:

> Agile V provides the governance skeleton. The extension is in how that skeleton is adapted to
> non-deterministic model behavior and evidence-driven review.

Need to be explicit about what not to claim:

- not claiming to have invented Agile V
- not claiming mature production proof for every layer
- not claiming LoRA experience beyond the appropriate future-looking boundary

This article should probably have the strongest truthfulness filter in the whole series.

---

## Architecture Stack Notes

### Layer 1: phase control and task structure

- exploratory work is allowed
- but transition into owned implementation is explicit
- each feature has requirements, constraints, and verification targets

### Layer 2: guardrails and hooks

- pre-generation or pre-tool-use checks
- policy enforcement
- bounded actions

### Layer 3: curated memory

- canonical documents
- retrieval instead of stuffing
- freshness and authority signals

### Layer 4: relational memory

- graph-backed decision, requirement, and component relationships
- absence detection
- lineage and supersession

### Layer 5: human gates

- review of evidence bundles
- decision acceptance
- accountability boundary

### Layer 6: later behavioral tuning

- adapters / LoRA only after prompt, retrieval, and architecture gains flatten

The article should make this look staged and sober, not all-at-once and grandiose.

Need one more sentence under the stack:

Each layer should remove a failure mode introduced earlier in the series:

- A1/A2: phase slippage and debt amplification -> constraints and verification
- A4/A6: buried or poisoned reasoning -> curated retrieval
- A8: relational and gap questions -> graph memory
- persistent model-behavior mismatch after all that -> only then consider tuning

That mapping may be one of the best framing devices in the article.

---

## Concrete Example Thread

Need a simple recurring concrete example:

- ingest synthetic policy or document corpus
- parse
- classify / detect
- retrieve supporting context
- produce typed findings
- route to human review
- generate report / evidence bundle

This is where the legal-tech-debt demo can anchor the abstract system.

Need to articulate what the example proves and what it does not prove.

It proves:

- the stack can be made concrete
- the memory and review layers have a visible job
- evidence-bearing outputs are possible

It does not prove:

- universal domain readiness
- solved legal AI
- production-grade maturity in every organizational setting

That restraint is part of the article's credibility.

---

## Counterarguments To Handle

### "This is too much architecture for most teams"

Answer:

Most teams do not need all layers immediately.
The whole series already justifies the escalation one layer at a time.

### "This sounds domain-specific"

Answer:

Legal/compliance is the first proving ground because the need for evidence, traceability, and
review is obvious there. The architectural logic is broader.

### "Why not just fine-tune the model"

Answer:

Because most teams have not yet exhausted the gains available from workflow design, retrieval,
and verification structure.

### "Why not just use a stronger frontier model"

Because raw model capability does not remove the need for phase boundaries, evidence trails,
retrieval discipline, or acceptance gates. A stronger model inside a weak workflow can still
produce very persuasive drift.

---

## Suggested Structure

1. Open by explicitly answering the gamified-work problem.
2. Summarize the series staircase in two short paragraphs.
3. Introduce Agile V with attribution.
4. Explain why the architecture has to be staged.
5. Walk the layered stack from constraints to memory to graph memory to human gates.
6. Map each layer back to a failure mode from earlier in the series.
7. Ground it in the document-intelligence example and state what that example proves.
8. Clarify where the extension begins.
9. End with a quiet invitation paragraph.

---

## Lines Worth Keeping

- The answer to gamified continuation is architecture.
- What the workflow cannot verify, the system should not treat as complete.
- Memory is a subsystem, not a pile of notes.
- Retrieval chooses what becomes present. Governance chooses what becomes accepted.
- The architecture matters more than the individual model inside it.
- A stronger model inside a weak workflow can still produce very persuasive drift.
- The stack should arrive one solved failure mode at a time.

---

## Source Pack

Primary sources:

- [Agile V: A Compliance-Ready Framework for AI-Augmented Engineering -- From Concept to Audit-Ready Delivery](https://arxiv.org/abs/2602.20684)
  Local target when pulled: `articles/papers/arxiv-2602.20684-agile-v-koch-wellbrock.pdf`
- [Introducing Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval)
- [Project GraphRAG](https://www.microsoft.com/en-us/research/project/graphrag/)
- [From Local to Global: A Graph RAG Approach to Query-Focused Summarization](https://www.microsoft.com/en-us/research/publication/from-local-to-global-a-graph-rag-approach-to-query-focused-summarization/)

Supporting links from the outline:

- [FHWA systems-engineering life cycle](https://ops.fhwa.dot.gov/seits/sections/section2/2_7.html)
- [SwarmForge repo](https://github.com/unclebob/swarm-forge)
- [IBM LoRA overview](https://www.ibm.com/think/topics/lora)
