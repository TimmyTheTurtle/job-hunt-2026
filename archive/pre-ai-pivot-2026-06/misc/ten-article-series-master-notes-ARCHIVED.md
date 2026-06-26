# Clean Agent Coding: Ten-Article Series Master Notes

This document captures the current state of the ten-article series, the architecture and repository direction behind it, and the most important ideas that emerged in discussion. It is designed to let work resume later without depending on chat history.

## Core framing

The central thesis is that **vibe coding is the new doomscrolling**: chat-based coding can reproduce the engagement dynamics of social media feeds, with prompt-response-reprompt loops that deliver intermittent rewards, low-friction continuation, and a misleading feeling of progress.[cite:20][cite:11][cite:37][cite:47]

The point is not that AI coding tools are bad. The point is that they can become **engagement systems** unless they are bounded by software-engineering and systems-engineering discipline.[cite:43][cite:29][cite:26]

The long-range answer emerging from this project is not a single tool. It is an architecture that layers:

- disciplined loops and constraints,[cite:30][cite:33][cite:43]
- guardrails and quality gates,[cite:29][cite:26][cite:157]
- durable but selective memory via RAG and contextual retrieval,[cite:131][cite:153][cite:159]
- graph-backed engineering memory via GraphRAG,[cite:158][cite:144][cite:162]
- and eventually behavioral tuning such as LoRA when prompt/retrieval structure reaches diminishing returns.[cite:175][cite:187][cite:184]

---

## Personal through-line

A major part of the series is personal and should remain visible. There is a real history of documentation friction: not keeping enough durable documentation in the past caused loss of rationale, repeated rediscovery, and confusion during later work.[cite:164]

The current overcorrection is highly documentation-oriented: journals, ADRs, handoffs, and AI-generated lessons learned are now part of the workflow, and the user spends time reviewing these so the evolving system remains legible.[cite:164]

That leads to a more advanced systems problem:

- too little documentation and the reasoning is lost,
- too much unfiltered documentation and the reasoning gets buried,
- so the true solution is not simply “more documentation,” but **better memory architecture**.[cite:123][cite:127][cite:131][cite:138]

This should become a recurring signature idea across the series.

Reusable line:

> Too little documentation and the reasoning is lost. Too much unfiltered documentation and the reasoning gets buried. The solution is not more notes, but better memory architecture.

---

## Mission / positioning language

One of the strongest framing lines that emerged is:

> Bringing sanity to agentic development before we’re all buried in magical nonsense.

This works best as a mission statement or occasional article subheading rather than a compact brand slogan.

Related phrasing that fits the repo and series:

- Sanity for agentic development.
- Agentic development without the magical nonsense.
- Serious engineering for agentic AI.

---

## Overall series design principle

A key editorial principle for the series is that **each article should justify the next**. Each introduced technology or idea should appear because the previous layer stops paying off or reveals a new failure mode.[cite:131][cite:158][cite:175]

This progression currently looks like:

1. Identify attention and engagement problems.
2. Show the cognitive and burnout consequences.
3. Show the memory and documentation consequences.
4. Introduce constraints and guardrails.
5. Introduce selective retrieval.
6. Introduce graph-structured memory.
7. Only later, when those gains flatten, consider model adaptation such as LoRA.[cite:131][cite:29][cite:158][cite:175]

This gives the series a natural staircase structure rather than a random list of AI topics.

---

## Article 1 — Vibe Coding Is the New Doomscrolling

### Main thesis

Vibe coding with chat-based AI tools can mirror doomscrolling: infinite continuation, variable rewards, and a persistent “just one more” interaction loop that feels productive but can become compulsive.[cite:20][cite:12][cite:16][cite:11]

### Main points to discuss

- What doomscrolling is and how it works psychologically.[cite:20][cite:12][cite:16]
- What vibe coding is: prompt-driven software generation and iterative steering through conversational interfaces.[cite:11][cite:19][cite:10][cite:15]
- Similarities between Facebook-like engagement loops and Claude-like coding loops.
- Why “productivity feels” can be as sticky as entertainment or outrage.
- Why the issue is not AI itself but the unbounded loop.

### Solution hints to seed

- Better loop design.
- Clear stopping conditions.
- Memory and constraints outside the chat itself.[cite:43][cite:29]

### Useful source links

- Doomscrolling overview: <https://en.wikipedia.org/wiki/Doomscrolling> [cite:20]
- Doomscrolling and feedback loops: <https://damorementalhealth.com/doomscrolling/> [cite:12]
- Psychology of doomscrolling: <https://rowancenterla.com/psychology-of-doom-scrolling-explained/> [cite:16]
- Vibe coding overview: <https://en.wikipedia.org/wiki/Vibe_coding> [cite:11]
- Replit on vibe coding: <https://replit.com/blog/what-is-vibe-coding> [cite:19]
- Martin Fowler on loops: <https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html> [cite:43]

---

## Article 2 — Inside the Agentic Attention Loop

### Main thesis

The key object to study is not just “AI assistance” but the attention loop itself: prompt, output, micro-win, uncertainty, reprompt, repeat.[cite:47][cite:37][cite:51]

### Main points to discuss

- Anatomy of a chat-based programming loop.[cite:47]
- Why partial success is especially sticky.
- How novelty and uncertainty keep the user engaged.
- Why this can feel different from normal coding, even when output volume rises.
- Why the user’s attention becomes the real scarce resource.

### Solution hints to seed

- Bound the loop.
- Add review gates.
- Use hooks and approval steps for critical transitions.[cite:157][cite:35]

### Useful source links

- Programming by Chat study: <papers/arxiv-2604.00436-programming-by-chat.pdf> [cite:47]
- Axios on agentic-tool addiction/brain effects: <https://www.axios.com/2026/04/04/ai-agents-burnout-addiction-claude-code-openclaw> [cite:37]
- AI fatigue essay: <https://siddhantkhare.com/writing/ai-fatigue-is-real> [cite:51]
- PreToolUse hooks: <https://www.linkedin.com/posts/lanemik_building-guardrails-for-ai-coding-assistants-activity-7418782309803544576-oSVd> [cite:35]
- Hooks article: <https://dev.to/rajeshroyal/hooks-how-to-put-guardrails-on-your-ai-coding-assistant-4gak> [cite:157]

---

## Article 3 — AI-Assisted Engineers Are Burning Out

### Main thesis

AI can improve throughput while simultaneously increasing cognitive exhaustion, because engineers are increasingly supervising, verifying, and second-guessing agents rather than simply writing code directly.[cite:59][cite:37][cite:63][cite:194]

### Main points to discuss

- Burnout and “brain fry” in heavy AI usage.[cite:59][cite:37]
- Verification burden and hollow productivity.[cite:42][cite:51]
- Hypervigilance and decision fatigue from rapid-fire AI outputs.[cite:104][cite:107]
- Why more assistance can paradoxically mean more mental strain.

### Solution hints to seed

- Guardrails that reduce oversight burden.
- Process that filters low-quality output before the human has to babysit it.[cite:29][cite:26]

### Useful source links

- Evil Martians burnout article: <https://evilmartians.com/chronicles/ai-assisted-engineers-are-burning-out-is-this-fine> [cite:59]
- Axios on power-user brain effects: <https://www.axios.com/2026/04/04/ai-agents-burnout-addiction-claude-code-openclaw> [cite:37]
- AI fatigue essay: <https://siddhantkhare.com/writing/ai-fatigue-is-real> [cite:51]
- HBR hidden penalty: <https://hbr.org/2025/08/research-the-hidden-penalty-of-using-ai-at-work> [cite:194]
- CodeScene guardrails: <https://codescene.com/blog/implement-guardrails-for-ai-assisted-coding> [cite:29]
- Snyk guardrails: <https://snyk.io/blog/build-fast-stay-secure-guardrails-for-ai-coding-assistants/> [cite:26]

---

## Article 4 — Bad Documentation and Vibe Coding Have the Same Failure Mode

### Main thesis

Missing documentation and vibe coding share a common failure mode: they produce activity without durable understanding. One loses the reasoning by never recording it; the other loses it by keeping it transient inside endless chats.[cite:164]

### Main points to discuss

- Personal documentation failures in the past and why they mattered.[cite:164]
- The current overcorrection into journals, ADRs, handoffs, and AI-generated lessons.[cite:164]
- Why “more docs” alone does not equal more clarity.[cite:108][cite:119]
- The need to distinguish authoritative memory from exploratory thinking.

### Solution hints to seed

- ADRs for significant decisions only.
- Documentation as memory infrastructure, not prose exhaust.[cite:114][cite:117][cite:120]

### Useful source links

- Allan Kelly on documentation diminishing returns: <https://www.allankelly.net/archives/5516/documentation-another-case-of-rapidly-diminishing-returns/> [cite:108]
- AWS ADR best practices: <https://aws.amazon.com/blogs/architecture/master-architecture-decision-records-adrs-best-practices-for-effective-decision-making/> [cite:114]
- Microsoft ADR guidance: <https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record> [cite:117]
- ADR creation practices: <https://ozimmer.ch/practices/2023/04/03/ADRCreation.html> [cite:120]

---

## Article 5 — From Vibes to Constraints

### Main thesis

LLM-assisted development becomes more accurate and more maintainable when it is constrained by explicit requirements, invariants, tests, and design conditions rather than vague intent.[cite:30][cite:33]

### Main points to discuss

- Why generic “make it better” prompts produce sloppy code.
- Constraint-first generation.
- Preconditions, postconditions, and testable invariants.[cite:30][cite:33]
- Why constraints are not anti-creativity; they are how engineering channels creativity into safety and predictability.

### Solution hints to seed

- Treat tests and ADRs as guardrails.
- Use a left-side/right-side life-cycle mentality like Agile-V or a mini-V per feature.[cite:84][cite:92]

### Useful source links

- Design-constraint research abstracts: <https://ieeexplore.ieee.org/document/11218044> [cite:33]
- PDF/source listing: <https://ieeexplore.ieee.org/iel8/6287639/10820123/11218044.pdf> [cite:30]
- Martin Fowler on loop placement: <https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html> [cite:43]
- Agile-V model overview: <https://itea.org/journals/volume-47-1/implementing-agile-v-hybrid-model/> [cite:84]
- Systems engineering life-cycle overview: <https://ops.fhwa.dot.gov/seits/sections/section2/2_7.html> [cite:92]

---

## Article 6 — When Documentation Becomes Context Poison

### Main thesis

At some point, accumulated AI-generated notes, summaries, and memory artifacts stop helping and start contaminating the active context window, leading to distraction, overflow, stale reasoning, and context poisoning.[cite:123][cite:127][cite:136]

### Main points to discuss

- Context distraction and context overflow.[cite:123][cite:127]
- Why more context is not always better context.[cite:124][cite:133][cite:153]
- Stale ADRs, duplicate summaries, and historical residue that keep steering the model after they should have expired.[cite:127][cite:136]
- The feeling that the system is now fighting your current intent with your own past thoughts.

### Solution hints to seed

- Retrieval over stuffing.
- Fresh summaries over raw history.
- Explicitly separating canonical, reference, and scratch notes.[cite:131][cite:161]

### Useful source links

- How Long Contexts Fail: <https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html> [cite:123]
- Elastic on context poisoning: <https://www.elastic.co/search-labs/blog/context-poisoning-llm> [cite:127]
- Context-window limitations: <https://atlan.com/know/llm-context-window-limitations/> [cite:136]
- Contextual Retrieval (Anthropic): <https://www.anthropic.com/engineering/contextual-retrieval> [cite:131]
- Redis on RAG accuracy: <https://redis.io/blog/10-techniques-to-improve-rag-accuracy/> [cite:161]

---

## Article 7 — RAG as a Gatekeeper for Engineering Memory

### Main thesis

RAG is how a large archive of documentation becomes usable engineering memory: archive broadly, retrieve narrowly.[cite:131][cite:153][cite:159]

### Main points to discuss

- Plain RAG basics and why retrieval beats prompt stuffing.[cite:156][cite:133]
- Contextual retrieval and reranking.[cite:131][cite:159][cite:196]
- Why metadata matters.
- Why a system should distinguish canonical truth from scratch notes.
- What it means to “gatekeep” documentation behind retrieval.

### Solution hints to seed

- Metadata-rich chunking.
- Retrieval ranking by authority and freshness.
- Context assembled from small, relevant, human-vetted packets.[cite:131][cite:153][cite:159]

### Useful source links

- Anthropic Contextual Retrieval: <https://www.anthropic.com/engineering/contextual-retrieval> [cite:131]
- Google on sufficient context: <https://research.google/blog/deeper-insights-into-retrieval-augmented-generation-the-role-of-sufficient-context/> [cite:153]
- Azure contextual retrieval blog: <https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/building-a-contextual-retrieval-system-for-improving-rag-accuracy/> [cite:159]
- Datacamp contextual retrieval guide: <https://www.datacamp.com/tutorial/contextual-retrieval-anthropic> [cite:196]
- Box contextual retrieval overview: <https://blog.box.com/contextual-retrieval-in-retrieval-augmented-generation-rag> [cite:193]
- General RAG accuracy techniques: <https://redis.io/blog/10-techniques-to-improve-rag-accuracy/> [cite:161]

---

## Article 8 — GraphRAG for Software Memory

### Main thesis

Software and architecture knowledge is inherently relational, so graph-backed retrieval is a better fit than isolated chunk retrieval for ADRs, code modules, constraints, tests, risks, and lessons learned.[cite:158][cite:144][cite:162]

### Main points to discuss

- Why software memory is a graph, not a pile of notes.[cite:147][cite:210]
- What GraphRAG is.[cite:158][cite:160]
- Knowledge-graph-guided retrieval and community summarization.[cite:144][cite:162][cite:158]
- The relation to legal-tech-debt work already involving metadata and structured relationships.
- A possible future graph model: ADRs, constraints, components, tests, sources, claims, lessons, risks.

### Solution hints to seed

- Hybrid retrieval: semantic seeds + graph expansion.
- Subgraph retrieval instead of naive top-k chunks.[cite:144][cite:158][cite:151]

### Useful source links

- Microsoft GraphRAG docs: <https://microsoft.github.io/graphrag/> [cite:158]
- Microsoft Research GraphRAG page: <https://www.microsoft.com/en-us/research/project/graphrag/> [cite:160]
- GraphRAG GitHub repo: <https://github.com/microsoft/graphrag> [cite:197]
- How GraphRAG works step-by-step: <https://tech.bertelsmann.com/en/blog/articles/how-microsoft-graphrag-works-step-by-step-part-12> [cite:195]
- KG-guided RAG paper: <https://aclanthology.org/2025.naacl-long.449/> [cite:144]
- RAG + knowledge graphs paper: <papers/arxiv-2404.17723-rag-knowledge-graphs.pdf> [cite:162]
- Memgraph GraphRAG overview: <https://memgraph.com/docs/ai-ecosystem/graph-rag> [cite:138]

---

## Article 9 — Clean Code for Agents

### Main thesis

Agentic coding should inherit software craftsmanship practices rather than bypass them. Clean code for agents is not identical to clean code for humans, but the overlap is strong: predictable structure, clear boundaries, test alignment, and maintainable patterns.[cite:72][cite:69][cite:78][cite:29]

### Main points to discuss

- What clean maintainable code looks like from a human perspective versus an agent perspective.[cite:201][cite:200][cite:203]
- Why agents prefer consistent patterns, local clarity, and explicit tests.[cite:29][cite:205][cite:147]
- Code quality, code familiarity, and strong test coverage as AI guardrails.[cite:29]
- Hooks, no-unsafe-command policies, and secure pipelines.[cite:26][cite:157][cite:35]
- A future “clean agent coding” checklist and ruleset.

### Solution hints to seed

- Guardrail files, prompt templates, tests, hooks.
- Repository structure that optimizes for both human and agent maintainability.
- Foreshadow eventual model adaptation only after loops and memory have matured.[cite:175][cite:187]

### Useful source links

- Uncle Bob course: <https://www.oreilly.com/live-events/ai-agents-for-clean-code-with-uncle-bob-martin/0642572376765/0642572376758/> [cite:72]
- Clean Code for AI Agents: <https://www.akitaonrails.com/en/2026/04/20/clean-code-for-ai-agents/> [cite:69]
- Skills, Not Vibes: <https://dev.to/gde/skills-not-vibes-teaching-ai-agents-to-write-clean-code-3l9e> [cite:78]
- CodeScene guardrails: <https://codescene.com/blog/implement-guardrails-for-ai-assisted-coding> [cite:29]
- Snyk guardrails: <https://snyk.io/blog/build-fast-stay-secure-guardrails-for-ai-coding-assistants/> [cite:26]
- Hooks article: <https://dev.to/rajeshroyal/hooks-how-to-put-guardrails-on-your-ai-coding-assistant-4gak> [cite:157]
- Maintainability/readability comparison: <https://www.gocodeo.com/post/comparing-ai-code-generation-tools-on-maintainability-and-readability> [cite:201]
- Maintainable code in the AI era: <https://aws.plainenglish.io/why-i-choose-clarity-over-speed-my-battle-for-maintainable-code-in-the-ai-era-3d0b45a36be3> [cite:200]
- GraphRAG for devs: <https://memgraph.com/blog/graphrag-for-devs-coding-assistant> [cite:147]

---

## Article 10 — The Architecture Being Built for Clean Agent Coding

### Main thesis

The capstone article presents the full architecture being proposed as an alternative to magical, unstructured agentic development: Agile-V governance, SwarmForge-style orchestration, curated software/systems engineering knowledge, contextual retrieval, GraphRAG, guardrails, and eventually LoRA adapters when earlier techniques begin to show diminishing returns.[cite:84][cite:79][cite:131][cite:158][cite:175]

### Main points to discuss

- Why governance comes first: Agile-V as the discipline spine.[cite:84][cite:92]
- Why orchestration comes next: SwarmForge as a model for role-specialized agent collaboration.[cite:79][cite:80]
- Why memory must be selective: RAG and contextual retrieval.[cite:131][cite:153][cite:159]
- Why structure matters: GraphRAG for engineering memory.[cite:158][cite:144][cite:162]
- Why safety matters: hooks and guardrails.[cite:29][cite:26][cite:157]
- Why LoRA comes late: adapt the model only after loops, memory, and graph structure stop buying enough performance or behavioral alignment.[cite:175][cite:187][cite:184][cite:185]

### Useful source links

- Agile-V hybrid model: <https://itea.org/journals/volume-47-1/implementing-agile-v-hybrid-model/> [cite:84]
- FHWA systems-engineering life cycle: <https://ops.fhwa.dot.gov/seits/sections/section2/2_7.html> [cite:92]
- SwarmForge repo: <https://github.com/unclebob/swarm-forge> [cite:79]
- Swarm playbook article: <https://zachwills.net/i-managed-a-swarm-of-20-ai-agents-for-a-week-here-are-the-8-rules-i-learned/> [cite:80]
- Anthropic Contextual Retrieval: <https://www.anthropic.com/engineering/contextual-retrieval> [cite:131]
- Microsoft GraphRAG docs: <https://microsoft.github.io/graphrag/> [cite:158]
- IBM LoRA overview: <https://www.ibm.com/think/topics/lora> [cite:187]
- IBM LoRA docs: <https://www.ibm.com/docs/en/watsonx/w-and-w/2.1.0?topic=tuning-lora-fine> [cite:175]
- Red Hat on LoRA adapters + semantic routing: <https://www.redhat.com/en/blog/creating-cost-effective-specialized-ai-solutions-lora-adapters-red-hat-openshift-ai> [cite:184]
- Google LoRA/QLoRA recommendations: <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/lora-qlora> [cite:185]

---

## Architecture direction beyond the articles

The architecture being contemplated is roughly:

- **Agile-V** as governance and verification structure.[cite:84][cite:92]
- **SwarmForge or SwarmForge-like orchestration** for multiple specialized agents working in disciplined coordination.[cite:79][cite:80]
- **A well-curated repository of software and systems engineering best practices** as reusable context.[cite:165][cite:72][cite:43]
- **RAG** to retrieve only the relevant pieces of the memory system.[cite:131][cite:153]
- **GraphRAG** to preserve relations among decisions, components, risks, tests, and lessons.[cite:158][cite:144][cite:151]
- **LoRA** later as behavioral tuning for specialized workflows, once retrieval and architecture stop delivering sufficient incremental gains.[cite:175][cite:187][cite:184]

This stack should be described not as a fantasy all-at-once implementation, but as a staged progression where each layer is justified by the limits of the previous one.

---

## Repository and documentation direction

The repository should support both writing and eventual prototyping. A useful structure already discussed was:

```text
clean-agent-coding/
  README.md
  AGENTS.md
  PROJECT_BRIEF.md
  /articles
  /research
    /sources
    /reading-notes
    /summaries
    /bibliography
  /memory-system
    /adrs
    /handoffs
    /journals
    /lessons
    /canonical
    /scratch
  /architecture
    /concepts
    /diagrams
    /agile-v
    /swarmforge
    /rag
    /graphrag
    /lora
  /prompts
  /templates
```

Important documentation principle: not all notes are equally authoritative.

A tiered model is preferred:

- **Canonical**: current truth, active architecture, active ADRs, current glossary, current article map.
- **Reference**: useful but not primary truth, including superseded ADRs and archived handoffs.
- **Scratch**: exploratory journals, half-baked reflections, AI-generated intermediate summaries.

Rule: **archive broadly, retrieve narrowly**.[cite:131][cite:153][cite:158]

---

## Metadata and future graph model

A future retrieval system should attach metadata to notes and chunks, likely including:

- `id`
- `title`
- `doc_type`
- `project`
- `article_number`
- `theme`
- `status`
- `created_at`
- `updated_at`
- `valid_from`
- `valid_to`
- `source_of_truth_rank`
- `confidence`
- `related_entities`
- `supersedes`
- `superseded_by`
- `tags`

This supports hybrid retrieval, authority ranking, temporal validity, and eventual graph construction.[cite:146][cite:138][cite:151]

Potential graph nodes:

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

Potential graph edges:

- `SUPPORTS`
- `EVIDENCES`
- `AFFECTS`
- `IMPLEMENTS`
- `SUPERSEDES`
- `DERIVED_FROM`
- `RELATES_TO`
- `VALIDATES`
- `BLOCKED_BY`
- `VALID_DURING`

This should allow retrieval of relevant subgraphs instead of isolated chunks.[cite:144][cite:138][cite:151]

---

## LoRA notes

LoRA belongs later in the series and later in the architecture story unless reading strongly suggests otherwise. The current logic is:

- first improve loops,
- then improve constraints,
- then improve retrieval,
- then improve graph structure,
- and only then adapt the model’s behavior with lightweight adapters when diminishing returns from earlier techniques become visible.[cite:175][cite:176][cite:185]

LoRA is still important because it creates the possibility of specialized adapters for:

- clean-code-for-agents behavior,
- documentation discipline,
- article voice / authorial style,
- and domain-specific task tuning without retraining an entire foundation model.[cite:175][cite:181][cite:186][cite:187]

Useful links:

- IBM LoRA docs: <https://www.ibm.com/docs/en/watsonx/w-and-w/2.1.0?topic=tuning-lora-fine> [cite:175]
- IBM overview: <https://www.ibm.com/think/topics/lora> [cite:187]
- Databricks guide: <https://www.databricks.com/blog/efficient-fine-tuning-lora-guide-llms> [cite:176]
- MAX serve adapters: <https://docs.modular.com/max/serve/lora-adapters/> [cite:181]
- Superlinked on embedding-model LoRA adapters: <https://superlinked.com/docs/engine/lora> [cite:186]
- Red Hat on LoRA adapters with routing: <https://www.redhat.com/en/blog/creating-cost-effective-specialized-ai-solutions-lora-adapters-red-hat-openshift-ai> [cite:184]

---

## Clean maintainable code from an agent’s perspective

An important late-stage concept for article 9 and the architecture article is that “clean maintainable code” is not identical from a human and agent perspective, though the overlap is large.[cite:201][cite:200][cite:203]

Agent-favorable maintainability features include:

- consistent idioms and structure,[cite:201][cite:200]
- small, locally understandable functions,[cite:29][cite:205]
- predictable naming and typing,[cite:201][cite:207]
- explicit tests aligned to code units,[cite:29][cite:205]
- low surprise density and minimal unnecessary cleverness,[cite:203][cite:202]
- graph-friendly code relationships that can be navigated at repository scale.[cite:147][cite:210]

This should likely become a reusable checklist and a future repo artifact.

---

## Additional framing lines worth preserving

- Vibe coding can burn hours and leave behind a working system, but only if it is treated as a tool instead of a feed.[cite:12][cite:16][cite:11][cite:19]
- Bad documentation and vibe coding share the same failure mode: activity without durable understanding.
- The future probably is not bigger context windows; it is better selection of what deserves to be in context at all.[cite:131][cite:153]
- What is needed is not more generated text, but a memory architecture that knows what to surface and what to leave buried.[cite:123][cite:131][cite:158]
- Bringing sanity to agentic development before we’re all buried in magical nonsense.

---

## Suggested immediate next steps

1. Read through the linked source material for each article.
2. Create a repo-level `article-map.md` based on the ten sections above.
3. Create a `sources-index.md` mapping sources to article numbers, roles (problem/mechanism/solution), and reliability.
4. Create ten empty article draft files, each with thesis + section stubs.
5. Create templates for ADRs, reading notes, and handoffs.
6. Begin classifying existing notes into canonical, reference, and scratch.
7. After reading, revisit whether LoRA remains late-stage or whether any part of it deserves to move earlier.

---

## Closing synthesis

This project is becoming more than a set of article ideas. It is evolving into a coherent research, writing, and architecture program centered on the question of how to bring engineering discipline to agentic development before hype, context pollution, burnout, and magical thinking harden into the default way people work.[cite:59][cite:43][cite:131][cite:158][cite:175]

The writing series, the repository, and the future prototype all support the same mission: turn documentation into memory, turn memory into retrieval, turn retrieval into structure, and turn structure into cleaner, saner agentic development.[cite:164][cite:131][cite:138][cite:158]
