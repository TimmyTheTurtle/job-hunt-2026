# S1-A8 — GraphRAG and Architectural Memory

**Status:** Not started
**Series position:** 8 of 10

---

## Thesis

Software and architecture knowledge is inherently relational. Vector similarity finds relevant
content; graph traversal finds relevant relationships. GraphRAG over ADRs and component
interfaces enables an agent to retrieve not just the relevant document but the relevant
architectural relationship — including what's *missing*, which pure vector similarity cannot do.

Microsoft's GraphRAG extracts knowledge graphs from text, builds community hierarchies, and
enables global reasoning over a document corpus — answering "what are all the components that
depend on this interface?" rather than "what does this interface do?"

---

## Key Claims

- Vector similarity finds relevant content; graph traversal finds relevant relationships
- Absence detection (finding what's missing) requires graph structure, not embeddings
- GraphRAG is the mechanism for giving agents persistent architectural memory across sessions
- Software memory is a graph, not a pile of notes

---

## Main Points to Discuss

- Why software memory is a graph: ADRs, constraints, components, tests, risks, lessons — all
  have relationships that matter as much as their content
- What GraphRAG is: knowledge graph extraction, community summarization, global reasoning
- Knowledge-graph-guided retrieval vs. naive top-k chunk retrieval
- Connection to legal-tech-debt: ADR-010 uses graph-based gap detection over vector embeddings
  specifically for absence detection — the graph finds what's missing
- A possible future graph model for the architecture:
  - Nodes: Article, Claim, Source, ADR, Requirement, Constraint, Component, Pattern, Risk,
    Test, Lesson, Handoff, Journal entry
  - Edges: SUPPORTS, EVIDENCES, AFFECTS, IMPLEMENTS, SUPERSEDES, DERIVED_FROM, RELATES_TO,
    VALIDATES, BLOCKED_BY, VALID_DURING

## Solution Hints to Seed

- Hybrid retrieval: semantic seeds + graph expansion
- Subgraph retrieval instead of naive top-k chunks

---

## Sources

- [GraphRAG on GitHub — Microsoft Research announcement](https://www.microsoft.com/en-us/research/blog/graphrag-new-tool-for-complex-data-discovery-now-on-github/)
- [GraphRAG project page — Microsoft Research](https://www.microsoft.com/en-us/research/project/graphrag/)
- [From Local to Global: A Graph RAG Approach — Microsoft Research paper](https://www.microsoft.com/en-us/research/publication/from-local-to-global-a-graph-rag-approach-to-query-focused-summarization/)
- [Microsoft GraphRAG docs](https://microsoft.github.io/graphrag/)
- [GraphRAG GitHub repo](https://github.com/microsoft/graphrag)
- [How Microsoft GraphRAG works step-by-step — Bertelsmann](https://tech.bertelsmann.com/en/blog/articles/how-microsoft-graphrag-works-step-by-step-part-12)
- [KG-guided RAG paper — ACL Anthology](https://aclanthology.org/2025.naacl-long.449/)
- [RAG + knowledge graphs paper — ArXiv](../papers/arxiv-2404.17723-rag-knowledge-graphs.pdf)
- [Memgraph GraphRAG overview](https://memgraph.com/docs/ai-ecosystem/graph-rag)
- [GraphRAG for developers coding assistant — Memgraph](https://memgraph.com/blog/graphrag-for-devs-coding-assistant)
