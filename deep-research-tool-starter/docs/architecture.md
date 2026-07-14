# Architecture

## High-Level Shape

The intended architecture is:

- corpus and source manifests
- normalization pipeline
- explicit graph substrate
- vector sidecar for semantic similarity
- retrieval and ranking layer
- synthesis layer
- evaluation layer
- artifact promotion layer

The architecture should stay local-first early, but production-aligned. Avoid decisions that make it impossible to add:

- real authentication and authorization,
- user or tenant/workspace isolation,
- billing or invoicing integration,
- secure secret handling,
- audit trails for important actions,
- deployment-specific configuration,
- and operational observability.

## Canonical Truth

Canonical truth should live in repo-visible artifacts such as:

- Markdown
- JSON / JSONL
- CSV where useful
- lightweight local stores when justified

Dashboards, UIs, notebooks, and assistants may summarize the system, but they must not become canonical truth by accident.

## Explicit Relationship Layer

Use a graph substrate for explicit relationships such as:

- cites
- references
- belongs to article
- derived from source
- supports section

Kuzu is a reasonable early candidate.

## Semantic Relationship Layer

Use a vector sidecar for semantic similarity and suggestion generation.

Preferred initial candidate:

- Qdrant

Alternative candidate:

- pgvector

The vector layer is not the canonical truth source.

## Retrieval Strategy

### Deterministic Retrieval First

Start with:

- exact phrase search
- lexical search
- metadata filters
- document / article scoping
- citation traversal
- graph expansion

### Semantic Retrieval Second

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
