# Roadmap

## Cross-Cutting Commercial Readiness

These concerns should be designed from the beginning and implemented when the project moves beyond local proof:

- environment-based deployment configuration
- secure secret handling
- authentication and authorization
- user or tenant/workspace separation
- billing or invoicing integration path
- audit logs for important user, source, AI, and evidence-promotion actions
- observability for parsing, retrieval, model calls, validation failures, and workflow state
- synthetic/demo-safe public dataset
- production cutover checklist

Do not let these concerns force premature infrastructure into Phase 0. Do keep interfaces and data models from assuming a single-user toy forever.

## Phase 0: Corpus Discipline

Goal:
Establish repo-native source truth.

Deliverables:

- corpus layout
- source manifests
- acquisition rules
- stable raw-source organization
- reproducible ingest commands

## Phase 1: Normalization

Goal:
Convert raw material into project-owned records.

Deliverables:

- parser adapters
- normalized `Source`, `Document`, and `Chunk` records
- stable IDs
- provenance fields
- warnings and parser uncertainty records

## Phase 2: Deterministic Retrieval

Goal:
Make the corpus usefully searchable without vectors.

Deliverables:

- exact phrase search
- lexical search
- metadata filters
- citation traversal
- article / document scoping

## Phase 3: Semantic Retrieval

Goal:
Add embeddings as a second evidence layer.

Deliverables:

- embeddings for abstracts and thesis summaries first
- vector store integration
- semantic nearest-neighbor search
- metadata-constrained semantic search

## Phase 4: Hybrid Linking

Goal:
Combine explicit and semantic relationships.

Deliverables:

- semantic-link generation
- hybrid ranking
- suggested missing-citation candidates
- article-to-paper support suggestions

## Phase 5: Grounded Synthesis

Goal:
Generate structured research outputs.

Deliverables:

- claim extraction
- evidence bundles
- contradiction capture
- open-question capture
- report skeletons and grounded summaries

## Phase 6: Evaluation

Goal:
Measure actual usefulness and reliability.

Deliverables:

- gold query sets
- semantic-link review sets
- groundedness checks
- retrieval quality scoring
- error analysis artifacts

## Phase 7: Workflow Promotion

Goal:
Turn useful outputs into durable project memory.

Deliverables:

- promote finding to note
- promote finding to article support bundle
- promote finding to ADR candidate
- promote finding to backlog/risk item
- run and evidence history

## Phase 8: Optional Agentic Layer

Goal:
Add orchestration only if it earns its keep.

Deliverables:

- subquestion planning
- bounded research loops
- researcher/synthesizer role separation
- review checkpoints
