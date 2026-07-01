# Deep Research Tool Canvas

## Purpose

This document is a planning canvas for a new repository that will hold a personal deep research tool project.

It combines:

- the project definition
- the recommended agent bootstrap instructions
- the architecture direction
- the SDLC choice
- the phase plan
- the mapping between project phases and curriculum phases

The goal is to give a future agent or future repo a clean starting contract without forcing a heavyweight process too early.

---

## Project Summary

This project is a:

- personal learning project
- portfolio project
- practical applied AI systems engineering project
- repo-native evidence engine for deep research

It is not meant to be:

- a generic chatbot
- a shallow "chat with PDFs" demo
- a premature SaaS platform
- a black-box answer engine

The tool should help investigate a domain the way a systems engineer, researcher, and careful architect would.

---

## Core Thesis

The project should turn messy source material into:

- structured records
- explicit citation links
- semantic similarity links
- evidence bundles
- grounded findings
- report drafts
- durable memory artifacts

The central design idea is:

**evidence first, answers second**

---

## What The Tool Should Do

The tool should be able to:

- ingest papers, notes, article drafts, PDFs, and saved research
- normalize them into project-owned artifacts
- support exact, lexical, metadata, graph, and semantic retrieval
- connect article drafts to supporting papers
- discover semantically related papers even when no explicit citation exists
- highlight contradictions, weak support, and missing citations
- generate grounded research outputs with uncertainty and provenance
- promote useful findings into durable repo-visible artifacts

---

## What Makes This Project Specific To Dorian

This tool is not generic by default. It reflects recurring patterns across existing repos:

- document-heavy domains
- layered dependencies
- partial understanding
- hidden relationships
- strong interest in traceability
- preference for explicit artifacts over opaque magic
- desire for durable memory rather than context bloat
- human-in-the-loop review instead of blind automation

The project is especially well aligned with:

- article research
- academic paper synthesis
- legal/compliance document reasoning
- evidence pipelines
- context architecture
- GraphRAG / retrieval engineering
- applied AI systems engineering

---

## Recommended Agent Bootstrap For A New Repository

Use the following as the startup contract for a future `AGENTS.md`.

### Purpose

This repository contains a personal deep research tool project.

The project is a learning vehicle, portfolio project, and applied AI systems engineering exercise.

It should help the owner build a system that can:

- ingest papers, articles, notes, and other document-heavy sources
- normalize them into project-owned artifacts
- retrieve evidence deterministically and semantically
- link ideas across documents, papers, and article drafts
- produce grounded research outputs with citations, uncertainty, and open questions
- preserve durable project memory in repo-visible artifacts

### Design Principles

1. Evidence first.
2. Project-owned artifacts over vendor-owned meaning.
3. Hybrid retrieval over vector-only retrieval.
4. Human review is part of the system.
5. Preserve the distinction between explicit links and semantic links.
6. Favor durable memory over context hoarding.
7. Use lightweight but disciplined SDLC.

### Canonical Architectural Shape

- corpus and source manifests
- normalization pipeline
- explicit graph substrate
- vector sidecar for semantic similarity
- retrieval and ranking layer
- synthesis layer
- evaluation layer
- artifact promotion layer

### Working Rules

- prefer small inspectable steps
- do not overbuild infrastructure early
- deterministic layers should remain explicit
- semantic results are suggestions until reviewed
- repo-visible artifacts matter more than assistant private memory
- if uncertain between flashy and sober, choose sober

---

## Recommended SDLC

The correct SDLC for this project is:

**Evidence-Driven Iterative Prototyping**

This is a better fit than full Agile V because the project is:

- solo
- exploratory
- architecture-discovery-heavy
- learning-oriented
- low external-risk
- light on stakeholder complexity

### Phase Gate Questions

Each phase should answer:

1. What are we trying to learn?
2. What is the smallest slice that answers it?
3. What evidence did the slice produce?
4. What decision follows from that evidence?

### Required Discipline

This repo should still keep:

- phase goals
- artifact contracts
- short ADRs when alternatives matter
- experiment records
- journals
- handoffs
- evaluation artifacts

It should not begin with:

- sprint bureaucracy
- heavy release governance
- formal stakeholder ceremony
- full Agile V traceability overhead

Agile V ideas can be borrowed later as a hardening influence, especially for:

- evidence bundles
- verification discipline
- evaluation thinking
- quality gates

---

## Architecture Direction

### Canonical Truth

Canonical truth should live in repo-visible artifacts such as:

- Markdown
- JSON / JSONL
- CSV where useful
- lightweight local stores when justified

### Explicit Relationship Layer

Use a graph substrate for explicit relationships such as:

- cites
- references
- belongs to article
- derived from source
- supports section

Kuzu is a reasonable starting candidate.

### Semantic Relationship Layer

Use a vector sidecar for semantic similarity and suggestion generation.

Preferred initial candidate:

- Qdrant

Alternative candidate:

- pgvector

The vector layer should not become the canonical truth source.

### Recommended Artifact Model

The model can evolve, but the project should likely normalize toward:

- `Source`
- `Document`
- `Block`
- `Chunk`
- `Claim`
- `Citation`
- `Reference`
- `Edge`
- `RetrievalBundle`
- `Report`
- `SemanticLink`

### Semantic Link Types

Suggested initial semantic links:

- `RELATED_PAPER`
- `SUPPORTS_ARTICLE`
- `MISSING_CITATION_CANDIDATE`
- `OVERLAPPING_ARTICLE`
- `SIMILAR_ARGUMENT`

These should be suggestion records with review state, not automatic truth.

---

## Retrieval Strategy

### Start With Deterministic Retrieval

The first useful retrieval modes should be:

- exact phrase search
- lexical search
- metadata filters
- document / article scoping
- citation traversal
- graph expansion

### Add Semantic Retrieval Afterward

The first embeddings should likely target:

1. paper abstracts
2. article thesis summaries
3. paper sections
4. article sections

Avoid full-document embeddings as the first move.

### Hybrid Ranking

Ranking should combine:

- lexical score
- semantic similarity
- graph / citation proximity
- metadata relevance
- article relevance
- optional recency weighting

Do not rely on nearest-neighbor similarity alone.

---

## Synthesis Strategy

LLMs are appropriate for:

- query expansion
- claim extraction
- contradiction detection
- gap finding
- grounded synthesis
- report drafting

Deterministic code should own:

- ingestion
- normalization
- schema validation
- provenance
- ID stability
- retrieval orchestration
- artifact generation
- evaluation harnesses

---

## Evaluation Philosophy

This project should not stop at "looks useful."

It should gradually build an evaluation layer that measures:

- retrieval quality
- support quality
- citation grounding
- contradiction handling
- semantic-link precision
- report usefulness

Likely eval artifacts:

- gold queries
- expected support passages
- regression checks
- groundedness checks
- semantic-link review sets
- error analysis notes

---

## Project Phases

### Phase 0: Corpus Discipline

Goal:
Establish repo-native source truth.

Deliverables:

- corpus layout
- source manifests
- acquisition rules
- stable raw-source organization
- reproducible ingest commands

Success signal:
The corpus can be reloaded and reasoned about without hidden manual context.

### Phase 1: Normalization

Goal:
Convert raw material into project-owned records.

Deliverables:

- parser adapters
- normalized `Source`, `Document`, and `Chunk` records
- stable IDs
- provenance fields
- warnings and parser uncertainty records

Success signal:
The project can trace any normalized chunk back to a source.

### Phase 2: Deterministic Retrieval

Goal:
Make the corpus usefully searchable without vectors.

Deliverables:

- exact phrase search
- lexical search
- metadata filters
- citation traversal
- article / document scoping

Success signal:
Useful evidence can be found deterministically for known questions.

### Phase 3: Semantic Retrieval

Goal:
Add embeddings as a second evidence layer.

Deliverables:

- embeddings for abstracts and thesis summaries first
- vector store integration
- semantic nearest-neighbor search
- metadata-constrained semantic search

Success signal:
The system finds useful related materials that explicit citation links miss.

### Phase 4: Hybrid Linking

Goal:
Combine explicit and semantic relationships.

Deliverables:

- semantic-link generation
- hybrid ranking
- suggested missing-citation candidates
- article-to-paper support suggestions

Success signal:
The system can suggest plausible support or relatedness links worth human review.

### Phase 5: Grounded Synthesis

Goal:
Generate structured research outputs.

Deliverables:

- claim extraction
- evidence bundles
- contradiction capture
- open-question capture
- report skeletons and grounded summaries

Success signal:
Outputs are citation-backed and visibly uncertain where appropriate.

### Phase 6: Evaluation

Goal:
Measure actual usefulness and reliability.

Deliverables:

- gold query sets
- semantic-link review sets
- groundedness checks
- retrieval quality scoring
- error analysis artifacts

Success signal:
The project can explain where it works and where it fails.

### Phase 7: Workflow Promotion

Goal:
Turn useful outputs into durable project memory.

Deliverables:

- promote finding to note
- promote finding to article support bundle
- promote finding to ADR candidate
- promote finding to backlog/risk item
- run and evidence history

Success signal:
The tool improves future work instead of only producing one-off answers.

### Phase 8: Optional Agentic Layer

Goal:
Add orchestration only if it earns its keep.

Deliverables:

- subquestion planning
- bounded research loops
- researcher/synthesizer role separation
- review checkpoints

Success signal:
The agentic layer reduces effort without reducing trust.

---

## Curriculum Mapping

The project should be built in parallel with the curriculum.

The curriculum is not separate from the project.
The project is the integration spine that gives each learned topic a real home.

### Mapping Table

| Curriculum Phase | What Is Being Learned | Project Phase(s) It Unlocks | Practical Deliverable |
|---|---|---|---|
| Phase A | Python scripting, CLI habits, file discipline | Phase 0 | corpus manifests, ingest commands, file-backed workflows |
| Phase B | Data modeling, JSON, schemas, structured artifacts | Phase 1 | normalized document records, stable IDs, provenance |
| Phase C | Search basics, filtering, ranking, retrieval concepts | Phase 2 | lexical/exact retrieval, metadata filters, citation queries |
| Phase D | Embeddings, semantic search, vector DB basics | Phase 3 | abstract embeddings, thesis-summary embeddings, vector sidecar |
| Phase E | Retrieval architecture, hybrid search, GraphRAG ideas | Phase 4 | semantic-link generation, hybrid ranking, graph + vector fusion |
| Phase F | Prompting, LLM app design, structured outputs | Phase 5 | grounded summaries, claim extraction, contradiction capture |
| Phase G | Evaluation, verification, test discipline for AI systems | Phase 6 | gold query sets, groundedness checks, semantic-link review harness |
| Phase H | Workflow engineering, knowledge capture, artifact lifecycle | Phase 7 | promotion flows to notes, ADRs, support bundles, run history |
| Phase I | Agent workflows, bounded orchestration, control surfaces | Phase 8 | optional planner/researcher/synthesizer loops |

### Curriculum Guidance

The right working rhythm is:

1. learn a concept
2. implement a narrow slice
3. validate it
4. preserve the artifact
5. move to the next layer

Avoid waiting to "finish the curriculum" before building.

Also avoid trying to build the whole project in one leap.

---

## Best Initial Build Order

To keep the project from turning into a hole, the recommended early order is:

1. define the artifact model
2. build corpus and manifest discipline
3. normalize article markdown and paper metadata
4. add deterministic retrieval
5. add embeddings for paper abstracts and article thesis summaries
6. add semantic-link suggestions

This is the first point where the project becomes genuinely useful without overbuilding.

---

## What A Future Repo Should Probably Contain

Suggested starting structure:

- `AGENTS.md`
- `README.md`
- `docs/vision.md`
- `docs/architecture.md`
- `docs/artifact-model.md`
- `docs/roadmap.md`
- `docs/sdlc.md`
- `docs/evaluation.md`
- `docs/adr/`
- `journal/`
- `handoffs/`
- `experiments/`
- `corpus/`
- `sources/`

Agents should read:

1. `AGENTS.md`
2. `README.md`
3. the smallest relevant subset of docs for the current task

They should not front-load the entire repo unless the task genuinely requires it.

---

## Success Criteria

The project is succeeding when it becomes possible to say:

- the corpus can be ingested reproducibly
- normalized artifacts are explicit and traceable
- deterministic retrieval is useful on its own
- semantic retrieval adds real discovery value
- semantic links are reviewable rather than magical
- outputs are grounded and citation-backed
- uncertainty is visible
- useful findings become durable project memory
- the architecture demonstrates real applied AI systems engineering maturity

