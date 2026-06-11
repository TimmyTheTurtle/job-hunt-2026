# S1-A7 — RAG as Engineering Memory

**Status:** Not started
**Series position:** 7 of 10

---

## Thesis

RAG is not a product feature — it is an engineering memory pattern. Archive broadly, retrieve
narrowly. A large archive of documentation becomes usable engineering memory through selective
retrieval: the agent doesn't get everything, it gets the right things.

Anthropic's contextual retrieval reduced failed retrievals by 49% (67% with reranking) by adding
chunk-specific explanatory context before embedding. This is the engineering discipline behind
RAG that naive implementations miss.

---

## Key Claims

- RAG is not a product feature — it's an engineering memory pattern
- The quality of what you index determines the quality of agent output
- Contextual retrieval (Anthropic's approach) is meaningfully better than naive chunking
- A system should distinguish canonical truth from scratch notes before indexing either

---

## Main Points to Discuss

- Plain RAG basics: why retrieval beats prompt stuffing
- Contextual retrieval and reranking: adding chunk-specific context before embedding
- Why metadata matters: authority, freshness, document type
- Why the system should distinguish canonical truth from scratch notes
- What it means to "gatekeep" documentation behind retrieval
- Connection to grannies-house-trials: the SQLite FTS5 knowledge base is a working instance
  of this pattern (books/lookup.py)

## Solution Hints to Seed

- Metadata-rich chunking
- Retrieval ranking by authority and freshness
- Context assembled from small, relevant, human-vetted packets

---

## Sources

- [Contextual Retrieval — Anthropic official](https://www.anthropic.com/news/contextual-retrieval)
- [Contextual Retrieval implementation guide — DataCamp](https://www.datacamp.com/tutorial/contextual-retrieval-anthropic)
- [Building a contextual retrieval system — Azure AI Foundry blog](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/building-a-contextual-retrieval-system-for-improving-rag-accuracy/)
- [Contextual Retrieval overview — Box](https://blog.box.com/contextual-retrieval-in-retrieval-augmented-generation-rag)
- [Deeper insights into RAG: the role of sufficient context — Google Research](https://research.google/blog/deeper-insights-into-retrieval-augmented-generation-the-role-of-sufficient-context/)
- [10 techniques to improve RAG accuracy — Redis](https://redis.io/blog/10-techniques-to-improve-rag-accuracy/)
- [A pragmatic guide to LLM evals — Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/evals)
