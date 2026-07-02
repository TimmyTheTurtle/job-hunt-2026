# Curriculum Mapping

The project should be built in parallel with the learning curriculum.

The curriculum is not separate from the project.
The project is the integration spine that gives each learned topic a real home.

## Working Rhythm

1. learn a concept
2. implement a narrow slice
3. validate it
4. preserve the artifact
5. move to the next layer

Avoid waiting to finish the curriculum before building.

## Primary Pluralsight Sequence

The current primary sequence from `APPLIED_AI_ENGINEERING_LEARNING_PLAN.md` is:

1. `FastAPI Fundamentals`
2. `Validate Data Classes with Pydantic`
3. `Observability with OpenTelemetry and Grafana`
4. `LangChain Development`
5. `Retrieval Augmented Generation (RAG) for Developers`
6. `Implementing Vector Search with LlamaIndex`
7. `Introduction to LangGraph`
8. `Model Context Protocol in Practice`

## Deep Research Tool Stage Mapping

The deep research tool phases are:

0. Corpus Discipline
1. Normalization
2. Deterministic Retrieval
3. Semantic Retrieval
4. Hybrid Linking
5. Grounded Synthesis
6. Evaluation
7. Workflow Promotion
8. Optional Agentic Layer

## Course-To-Stage Mapping

| Sequence | Pluralsight Course | Best Deep Research Tool Stage | Why It Fits | Expected Project Deliverable |
|---|---|---|---|---|
| 1 | `FastAPI Fundamentals` | Stage 7: Workflow Promotion | FastAPI is less about core retrieval logic here and more about exposing stable local capabilities and artifact services behind explicit contracts. | a small local service for artifact persistence, query submission, or report retrieval |
| 2 | `Validate Data Classes with Pydantic` | Stage 1: Normalization | Pydantic fits the project at the boundary where messy sources become typed project-owned records. | typed `Source`, `Document`, `Chunk`, or `Claim` models plus validation failures |
| 3 | `Observability with OpenTelemetry and Grafana` | Stage 6: Evaluation | Observability becomes most useful once workflows and retrieval paths exist and need inspection and failure analysis. | traces for retrieval, extraction, synthesis, review, and failure points |
| 4 | `LangChain Development` | Stage 5: Grounded Synthesis | LangChain is most useful after artifacts and retrieval exist, when building extraction and synthesis flows over grounded evidence. | claim extraction, citation-aware summary generation, contradiction detection |
| 5 | `Retrieval Augmented Generation (RAG) for Developers` | Stage 2: Deterministic Retrieval | This is the first retrieval architecture layer: chunking, indexing, retrieval, citation grounding, and visible failure modes. | ingest pipeline, chunking note, retrieval script, answer-with-citations flow |
| 6 | `Implementing Vector Search with LlamaIndex` | Stage 3: Semantic Retrieval | This is the semantic-linking stage: embeddings, vector search, metadata-constrained retrieval, and similarity-based discovery. | abstract and thesis-summary embeddings, vector store integration, semantic search results |
| 7 | `Introduction to LangGraph` | Stage 8: Optional Agentic Layer | LangGraph maps best after the core retrieval and synthesis pipeline exists and needs explicit workflow state and interrupt/resume behavior. | ingest-classify-retrieve-extract-review graph with persisted checkpoints |
| 8 | `Model Context Protocol in Practice` | Stage 7: Workflow Promotion | MCP fits the tool boundary layer where project capabilities become reusable tools with explicit interface discipline. | MCP server exposing search, validation, rule lookup, or artifact-save capabilities |

## Week-Level Mapping

The learning plan also groups the work by week. Mapped to the deep research tool, that becomes:

| Learning Plan Week | Primary Focus | Deep Research Tool Stage Emphasis |
|---|---|---|
| Week 1 | structured outputs and validation | Stage 1: Normalization |
| Week 2 | retrieval basics and RAG failure modes | Stage 2 and early Stage 3 |
| Week 3 | workflow orchestration and human review | Stage 8, but only after Stages 1-5 have a useful core |
| Week 4 | tool contracts, APIs, and MCP thinking | Stage 7 |
| Week 5 | observability and debuggable AI systems | Stage 6 |
| Week 6 | evals, adversarial inputs, and regression discipline | Stage 6 with spillover into Stage 5 and Stage 8 hardening |

## Important Sequencing Note

The strongest conceptual order for the deep research tool is not exactly the same as the listed Pluralsight order.

For this project, the most natural build order is:

1. Stage 0: Corpus Discipline
2. Stage 1: Normalization
3. Stage 2: Deterministic Retrieval
4. Stage 3: Semantic Retrieval
5. Stage 4: Hybrid Linking
6. Stage 5: Grounded Synthesis
7. Stage 6: Evaluation
8. Stage 7: Workflow Promotion
9. Stage 8: Optional Agentic Layer

That means some courses should be studied before or during a later implementation stage rather than immediately forcing that stage.

Example:

- `Observability with OpenTelemetry and Grafana` appears early in the sequence, but is most valuable once the tool has enough moving parts to observe.
- `FastAPI Fundamentals` appears early in the sequence, but the project should not start by becoming an API product.
- `Introduction to LangGraph` is valuable learning earlier, but should not cause premature orchestration before retrieval and synthesis are real.

## Practical Build Guidance

The safest early implementation order is:

1. define the artifact model
2. build corpus and manifest discipline
3. implement Pydantic-backed normalization
4. build deterministic retrieval
5. add semantic retrieval with vectors
6. add hybrid-link suggestions
7. add grounded synthesis
8. add eval and observability
9. expose mature capabilities through FastAPI or MCP
10. only then add LangGraph orchestration if it earns its keep

This is the first point where the project becomes genuinely useful without overbuilding.
