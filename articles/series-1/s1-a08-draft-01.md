# GraphRAG and Architectural Memory
### Draft 1 - expanded working draft / research packet

---

## Working Note

This article should feel like a justified escalation from A7, not like "and now a fancier buzzword."

The cleanest reason GraphRAG exists in the series:

RAG is good when the main problem is finding the right text.
GraphRAG enters when the main problem is finding the right relationship, dependency,
neighborhood, absence, or lineage.

That is the jump.

---

## Core Argument

Software memory is relational by nature.

ADRs, components, interfaces, constraints, tests, risks, superseded decisions, and lessons do
not simply sit next to one another as isolated chunks. They point at one another. Their meaning
often depends on those links.

That is why a pure vector store can help with semantic relevance but still miss what architecture
questions often need:

- what depends on this?
- what superseded this?
- what requirement is not covered?
- what changed because of that decision?

This is the place where "absence detection" becomes a memorable idea.

---

## What This Article Has To Do

1. show the limit case of plain RAG
2. explain why architecture is graph-shaped
3. use Microsoft GraphRAG as the main supporting frame
4. make "global vs local question" very concrete
5. point toward the closing architecture article

---

## Research Spine

### 1. Microsoft's GraphRAG framing

The best summary from Microsoft's publication page:

- traditional RAG fails on global questions over a corpus
- GraphRAG combines graph indexing with community summaries
- it supports both scale and broader, dataset-level reasoning

This is useful because architecture questions are very often corpus-level and relational, not
just snippet-level.

Sources:

- [From Local to Global: A Graph RAG Approach to Query-Focused Summarization](https://www.microsoft.com/en-us/research/publication/from-local-to-global-a-graph-rag-approach-to-query-focused-summarization/)
- [Project GraphRAG](https://www.microsoft.com/en-us/research/project/graphrag/)
- [GraphRAG docs](https://microsoft.github.io/graphrag/)

### 2. Structured, hierarchical retrieval

The GraphRAG docs make a clean claim:

- GraphRAG is structured and hierarchical
- it extracts a knowledge graph
- builds community hierarchy
- generates summaries for those communities
- uses those structures during retrieval

That supports the article's thesis that architectural memory is not a pile of notes.

### 3. KG-backed RAG beyond Microsoft

The Xu et al. paper is not about software architecture, but it is still useful because it makes
the general point that relations and structure help retrieval and answer quality compared with
treating everything as plain text.

Source:
- [Retrieval-Augmented Generation with Knowledge Graphs for Customer Service Question Answering](https://arxiv.org/abs/2404.17723)

---

## The Key Distinction To Push

Local vs global questions.

Local:

- what does this interface do?
- where is this term defined?
- what did we decide about retries?

Global:

- what are the main themes across the architecture decisions?
- which components depend on this interface?
- where do we have similar constraints expressed differently?
- which requirements have evidence but no verification?

GraphRAG becomes more compelling once the article emphasizes that global architectural questions
are not rare edge cases. They are normal senior-engineering questions.

---

## Absence Detection

This is probably the freshest idea in the article.

Vector similarity is good at finding nearby text.
It is not naturally good at proving that something expected is missing.

Possible examples:

- requirement has no linked test
- architectural decision has no superseding record despite known change
- component has no documented ownership
- risk appears in lessons but not in constraints

This is the point where the graph framing becomes more than "a better retrieval system."
It becomes a consistency and gap-detection system.

---

## Candidate Graph Schema To Keep

The outline's schema is already good. Keep it.

Nodes:

- Article
- Claim
- Source
- ADR
- Requirement
- Constraint
- Component
- Pattern
- Risk
- Test
- Lesson
- Handoff
- Journal entry

Edges:

- SUPPORTS
- EVIDENCES
- AFFECTS
- IMPLEMENTS
- SUPERSEDES
- DERIVED_FROM
- RELATES_TO
- VALIDATES
- BLOCKED_BY
- VALID_DURING

This could become a diagram later, but for now it is a very good note block.

---

## Counterarguments To Handle

### "This is overkill"

Sometimes true.
Need to admit that GraphRAG is not the first move for every team.
The series staircase already helps here: plain retrieval first, graph retrieval later.

### "Can't embeddings already capture relationships?"

Some, yes. But not explicit lineage, constraints, absence, or durable structural links in a
reliable way.

### "This sounds like knowledge-management theater"

Then keep the examples anchored in ordinary engineering questions, not enterprise taxonomy talk.

---

## Suggested Structure

1. Start from A7's limit: right text is not always enough.
2. Explain software memory as relational.
3. Use local vs global question distinction.
4. Introduce GraphRAG and community summaries.
5. Make the absence-detection argument.
6. Offer the candidate graph schema.
7. Point toward A10 where this becomes part of the full system.

---

## Lines Worth Keeping

- Software memory is a graph, not a pile of notes.
- Vector search finds nearby text. Graph structure finds meaningful relations.
- Some architectural questions are not retrieval questions at all. They are graph questions.
- The most important thing in the system may be the thing that is missing.
- Graph memory is how rationale, dependency, and lineage survive at scale.

---

## Source Pack

Primary sources:

- [From Local to Global: A Graph RAG Approach to Query-Focused Summarization](https://www.microsoft.com/en-us/research/publication/from-local-to-global-a-graph-rag-approach-to-query-focused-summarization/)
- [Project GraphRAG](https://www.microsoft.com/en-us/research/project/graphrag/)
- [GraphRAG docs](https://microsoft.github.io/graphrag/)
- [Retrieval-Augmented Generation with Knowledge Graphs for Customer Service Question Answering](https://arxiv.org/abs/2404.17723)
  Local target when pulled: `articles/papers/arxiv-2404.17723-rag-knowledge-graphs.pdf`

Supporting links from the existing outline:

- [KG-guided RAG paper](https://aclanthology.org/2025.naacl-long.449/)
- [GraphRAG GitHub repo](https://github.com/microsoft/graphrag)

