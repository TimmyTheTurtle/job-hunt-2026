# Article Plan

Two series. Different tents.

**Series 1 — The Vibe Coding Problem** is the public-facing funnel: a coherent argument from problem
diagnosis to architecture, aimed at engineering leaders and senior engineers wrestling with AI tooling.
It builds the contractor audience.

**Series 2 — AI Systems Engineering** is the deeper technical series: theory and practice of building
non-deterministic systems with engineering discipline. It builds the thought-leadership floor beneath
Series 1 and justifies the positioning long-term.

They share vocabulary and cross-link, but they are not the same argument and should not be the same
publication sequence.

---

## Series 1: The Vibe Coding Problem

**Audience:** Engineering leaders, senior engineers, CTOs evaluating AI-assisted development.
**Arc:** Diagnose the failure mode → deepen the diagnosis → introduce the solution components → present the architecture.
**Publication cadence:** One article every 10–14 days. Article 1 is the lead; everything else builds on its reach.
**Platform:** LinkedIn primary, personal site canonical.

---

### Article 1 — Vibe Coding Is the New Doomscrolling

**The hook.** This is the article that gets shared. Everything else depends on how well this one lands.

Andrej Karpathy coined "vibe coding" in February 2025 — accepting AI-generated code without
understanding it, surfing on vibes. One year later he renamed it "agentic engineering" and admitted
his own new project was basically hand-written. That pivot is the opening. The argument: vibe coding
exploits the same attention-loop mechanics as doomscrolling. Rapid generation, instant gratification,
no friction, no consolidation. The output feels productive. The system degrades.

**Key claims:**
- Vibe coding is not a productivity strategy, it's a dopamine loop
- The loop is structurally identical to social media attention mechanics
- The cost is deferred, invisible, and compounds

**Links:**
- [Andrej Karpathy coins "vibe coding" (Simon Willison)](https://simonwillison.net/2025/Mar/19/vibe-coding/)
- [Karpathy admits he hand-coded his new project (Futurism)](https://futurism.com/artificial-intelligence/inventor-vibe-coding-doesnt-work)
- [Karpathy renames vibe coding to "agentic engineering" (SD Times)](https://sdtimes.com/ai/andrej-karpathy-has-renamed-vibe-coding-heres-what-engineering-leaders-need-to-do-about-it/)

---

### Article 2 — AI Makes Bad Code Worse

Productive vibes, compounding debt. AI accelerates output in proportion to the quality of the context
it's given. Give it clean, well-structured code and it extends that. Give it accumulated technical debt
and it extends that too — faster. The amplification is symmetric.

Adam Tornhill's CodeScene research on code health provides the empirical grounding: code with low
health scores (high complexity, high coupling) is where bugs concentrate. AI working in those areas
doesn't reduce the concentration — it increases output velocity in the highest-risk zones.

**Key claims:**
- AI amplifies the pattern of surrounding code, not the ideal pattern
- Technical debt zones are exactly where AI does the most damage
- The problem is not the AI — it's introducing AI without managing the context it operates in

**Links:**
- [CodeScene code biomarkers research](https://codescene.com/blog/code-biomarkers/)
- [Adam Tornhill on psychology of code quality (Tech Lead Journal ep. 241)](https://techleadjournal.dev/episodes/241/)

---

### Article 3 — I Shipped More and Felt Worse

**The burnout article — reframed around cognitive decline.** The generic "AI burnout" angle is
crowded and mostly about workload. The stronger claim: AI-assisted development done wrong causes
measurable cognitive decline. Not fatigue. Decline. The same mechanism as doomscrolling — passive
consumption replacing active construction — applied to the cognitive work of engineering.

Social media is engineered to replace active engagement (forming an opinion, sitting with
discomfort) with passive reception (scroll, react, move on). Vibe coding does the same to
engineering cognition: replace active problem-solving (hold the problem, try approaches, feel
where they break) with passive acceptance (generate, skim, approve, move on). The research
supports this — cognitive offloading reduces retention and reasoning depth over time. The
"Google effect" (knowing you can look something up reduces encoding depth) is the mild version.
Vibe coding is the aggressive version applied to the skills that make you an engineer.

The personal counter-move: starting the day with vector math, calculus, or physics problems
before the AI tools come on. Not because the problems are professionally necessary, but because
the *capacity* to do them is what's being protected. Active problem-solving as a daily practice
in the age of AI assistance — protecting cognitive capability deliberately, not by accident.

The practical technique: have the AI create a lesson on what you're about to build, then build
it yourself. Lesson-first, build-second inverts the vibe coding default. The AI teaches; you
construct. The build loop is the comprehension check — you can't fake your way through
implementing something you don't understand. This habit compounds capability over time in a
way that generate-and-accept never does.

**Key claims:**
- Vibe coding causes cognitive decline through the same mechanism as doomscrolling — passive
reception replacing active construction
- The competence erosion is gradual and invisible until the capability is needed and isn't there
- The counter-move is deliberate: protect active reasoning as a daily practice
- Lesson-first, build-second is the practical inversion of the vibe coding default
- Morning math/physics/calculus is a legitimate engineering practice, not a hobby

**Links:**
- [AI-assisted engineers are burning out (Evil Martians)](https://evilmartians.com/chronicles/ai-assisted-engineers-are-burning-out-is-this-fine)
- [So your developers use AI now (Evil Martians)](https://evilmartians.com/chronicles/so-your-developers-use-ai-now-here-is-what-to-know)

---

### Article 4 — Why Documentation Fails in AI-Assisted Development

Documentation written for humans assumes a human reader who can infer context, ask questions, look at
git history, and build a mental model over time. AI agents have none of that. They have a context
window. Documentation that doesn't make it into the context window doesn't exist from the agent's
perspective. The failure mode: teams add more documentation, AI ignores most of it, the team concludes
documentation is useless, and stops writing it.

The correct diagnosis: documentation isn't failing because it's incomplete. It's failing because it
was designed for the wrong reader.

**Key claims:**
- Human-facing documentation and agent-facing context are different artifacts with different design requirements
- Adding more of the wrong kind of documentation makes the problem worse
- The right response is redesigning what gets written, not writing more of it

**Links:**
- [Vibe coding in style.md — AGENTS.md as discipline framework (Evil Martians)](https://evilmartians.com/chronicles/vibe-coding-in-style-dot-md)

---

### Article 5 — Vibe Coding Without Constraints Is Just Vibe Coding

**The pivot article.** The problem is diagnosed. Now: why constraints are the solution, not the
problem. The common objection to adding structure to AI workflows is that it slows things down. That
objection treats speed of generation as the metric. The right metric is rate of trustworthy delivery.

Uncle Bob Martin's "Clean AI: Agentic Discipline" series makes this argument from a craftsmanship
angle: clean code principles don't disappear with AI, they become more important — and some of them
become technical requirements rather than guidelines. Function size, for example, isn't just a
readability concern anymore. A function that doesn't fit in a single tool call can't be worked on
atomically by an agent.

**Key claims:**
- The case against constraints assumes the wrong success metric
- Constraints are not friction — they are the mechanism by which AI output becomes trustworthy
- Some clean code principles that were guidelines for humans become hard requirements for agents

**Links:**
- [Clean AI: Agentic Discipline — Uncle Bob Martin (Clean Coders)](https://cleancoders.com/episode/agentic-discipline-1)
- [Clean Code for AI Agents (AkitaOnRails)](https://akitaonrails.com/en/2026/04/20/clean-code-for-ai-agents/)
- [AI Agents for Clean Code — Uncle Bob at O'Reilly](https://www.oreilly.com/live-events/ai-agents-for-clean-code-with-uncle-bob-martin/0642572376765/0642572376758/)

---

### Article 6 — Context Poisoning

The mechanism behind Articles 2 and 3, made explicit. Context poisoning is what happens when the
context an agent operates in has accumulated bad information — outdated architecture, inconsistent
naming, misleading comments, stale tests. The agent is a mirror of its context. It generates
continuations that are statistically consistent with what it was handed. Poison in, poison extended.

There is also a security dimension: XOXO (Cross-Origin Context Poisoning) attacks achieve a 75%
success rate on major models by injecting malicious instructions into the context through documents
the agent reads. The organic version — accumulated debt and drift — is less dramatic but more
pervasive.

**Key claims:**
- Context poisoning is the mechanism, not a metaphor
- It happens organically through debt accumulation and deliberately through adversarial injection
- Cleaning the context is not optional maintenance — it's the primary engineering discipline in
agentic workflows

**Links:**
- [XOXO: Cross-Origin Context Poisoning attacks (ArXiv)](https://arxiv.org/html/2503.14281v1)
- [Context rot is slowing down your AI agent (LogRocket)](https://blog.logrocket.com/context-rot-slowing-down-your-ai-agent-how-fix/)
- [Context Rot: Why LLMs degrade as context grows (Morph)](https://www.morphllm.com/context-rot)

---

### Article 7 — RAG as Engineering Memory

The first solution component. Retrieval-Augmented Generation as a mechanism for giving agents access
to architectural context they couldn't hold in a single context window. The practical application:
indexing ADRs, test cases, domain glossaries, and module contracts so the agent retrieves relevant
context at the moment of generation rather than operating blind.

Anthropic's contextual retrieval reduced failed retrievals by 49% (67% with reranking) by adding
chunk-specific explanatory context before embedding. This is the engineering discipline behind RAG
that naive implementations miss.

**Key claims:**
- RAG is not a product feature — it's an engineering memory pattern
- The quality of what you index determines the quality of agent output
- Contextual retrieval (Anthropic's approach) is meaningfully better than naive chunking

**Links:**
- [Contextual Retrieval — Anthropic official](https://www.anthropic.com/news/contextual-retrieval)
- [Contextual Retrieval implementation guide (DataCamp)](https://www.datacamp.com/tutorial/contextual-retrieval-anthropic)
- [A pragmatic guide to LLM evals (Pragmatic Engineer)](https://newsletter.pragmaticengineer.com/p/evals)

---

### Article 8 — GraphRAG and Architectural Memory

Beyond chunk retrieval: graph-based retrieval for reasoning about relationships between components.
Microsoft's GraphRAG extracts knowledge graphs from text, builds community hierarchies, and enables
global reasoning over a document corpus — the kind of reasoning that answers "what are all the
components that depend on this interface?" rather than "what does this interface do?"

Applied to codebases: GraphRAG over ADRs and component interfaces enables an agent to retrieve not
just the relevant document but the relevant architectural relationship. This is the approach in
legal-tech-debt (ADR-010: graph-based gap detection over vector embeddings for absence detection —
the graph can find what's *missing*, which pure vector similarity cannot).

**Key claims:**
- Vector similarity finds relevant content; graph traversal finds relevant relationships
- Absence detection (finding what's missing) requires graph structure, not embeddings
- GraphRAG is the mechanism for giving agents persistent architectural memory across sessions

**Links:**
- [GraphRAG on GitHub — Microsoft Research](https://www.microsoft.com/en-us/research/blog/graphrag-new-tool-for-complex-data-discovery-now-on-github/)
- [GraphRAG project page — Microsoft Research](https://www.microsoft.com/en-us/research/project/graphrag/)
- [From Local to Global: A Graph RAG Approach (Microsoft Research paper)](https://www.microsoft.com/en-us/research/publication/from-local-to-global-a-graph-rag-approach-to-query-focused-summarization/)

---

### Article 9 — There Is No Such Thing as Clean Agentic Code

**The reframe article.** "Clean code for agents" is probably a category error. Compilers don't read
code for meaning. Neither do agents — not really. They read a context window that contains code,
among other things. The discipline that matters is not code style. It is context architecture.

What does transfer from clean code to agentic development: consistent vocabulary (agents have no
out-of-band knowledge to resolve naming ambiguity), small files (context window economics, not
readability), explicit contracts (type signatures and docstrings are agent-readable specifications),
and externalized architectural memory (the implicit knowledge senior engineers carry in their heads
must be written down to be retrievable).

What doesn't transfer: most of the aesthetic and structural guidance that assumes a human reader who
builds a mental model over time. An agent has no prior sessions. Every context window is day one.

**Key claims:**
- "Clean code for agents" collapses into: normal clean code (indirectly helpful) + context
architecture (the new discipline)
- The new discipline has different design targets than code style
- Writing for the new team member on day one, not the expert on day 100, is the standard that
works for both humans and agents

**Links:**
- [Clean AI: Agentic Discipline (Clean Coders)](https://cleancoders.com/episode/agentic-discipline-1)
- [So your developers use AI now (Evil Martians)](https://evilmartians.com/chronicles/so-your-developers-use-ai-now-here-is-what-to-know)

---

### Article 10 — The Architecture I'm Building

**The closing argument.** Everything prior was diagnosis and theory. This article is the system.
Agile V (ArXiv 2602.20684) is the published V-model framework for AI-augmented development this
work builds on. Sandbox005 is the working implementation of that framework extended to handle
non-deterministic LLM outputs.
The document intelligence pipeline (Ingest → Model → Detect → Triage → Report → Govern) as a
concrete instance of the architecture in production on real data.

The call to action lives here: a quiet paragraph at the end. Not a pitch — a door.

**Key claims:**
- The architecture described in this series exists and is running
- It is domain-agnostic — legal/compliance is the first experiment, not the definition
- The SE discipline (explicit boundaries, human gates, evidence trails) is the differentiator,
not the AI components

**Links:**
- All prior articles in the series (cross-link the full arc)

---

## Series 2: AI Systems Engineering

**Audience:** Senior engineers, technical leads, AI practitioners who want the theoretical grounding
behind Series 1's claims.
**Arc:** Foundational arguments about what makes LLM systems different from deterministic software,
and what engineering discipline looks like in response.
**Publication cadence:** Less frequent, more technical. These take longer to write and have a smaller
but more valuable audience.
**Platform:** Personal site primary, LinkedIn secondary with summary posts.

These articles do not need to be written in sequence before seeking clients. They build the long-term
intellectual floor. Prioritize Series 1 for the next 10 weeks.

---

### S2-A1 — TDD Doesn't Work for Non-Deterministic Systems (And What Does)

**The core argument.** TDD rests on three assumptions LLM systems violate: determinism (same input
always produces same output), binary correctness (pass or fail), and fast cheap feedback (seconds,
free). LLM systems are stochastic, produce outputs on a correctness distribution rather than a
boolean, and are slow and costly to run at scale.

The replacement methodology is **evals**: structured evaluation runs against curated datasets with
human-labeled ground truth, producing aggregate statistics. A drop from 87% to 79% accuracy is a
signal requiring human interpretation — not a failed test requiring a code fix. You can automate
the running of evals; you cannot automate the interpretation.

LLM-as-judge is triage, not verification. A second LLM evaluating the output of the first can
reduce human review volume by flagging likely errors. It cannot verify — it has the same
non-determinism problem, and correlation bias means both models fail in the same directions.

**Links:**
- [LLM as a Judge: guide and best practices (Agenta)](https://agenta.ai/blog/llm-as-a-judge-guide-to-llm-evaluation-best-practices)
- [LLMs-as-Judges: comprehensive survey (ArXiv)](https://arxiv.org/pdf/2412.05579)
- [LLM judge cookbook (Hugging Face)](https://huggingface.co/learn/cookbook/en/llm_judge)
- [Beyond vibe checks: complete guide to evals (Lenny's Newsletter)](https://www.lennysnewsletter.com/p/beyond-vibe-checks-a-pms-complete)

---

### S2-A2 — The V-Model Was Built for This Problem

The V-model predates LLMs by decades. It was developed for aerospace and medical devices — systems
where behavior can't be fully specified before implementation, requirements are expressed in natural
language with interpretive ambiguity, and failure modes require human judgment to evaluate. LLM
systems share all three properties. This isn't a coincidence. It's structural.

**Verification** (are we building the system right?) is partially automatable for LLM systems:
structural checks, schema validation, deterministic component tests. **Validation** (are we building
the right system?) requires human judgment. Always. The specification for an LLM component is
typically a rubric or a set of examples. A human has to decide whether the output is consistent
with that rubric.

The implication for Agile teams: sprint-based TDD workflows don't map onto LLM component development.
The V-model's decomposition-then-integration structure, with explicit verification and validation
gates, does.

**Attribution note — IMPORTANT:** The term "Agile V" as used in legal-tech-debt and Sandbox 005 is
**not original to this work**. It comes from a published framework discovered while researching
V-model application to AI development:

> *Agile V: A Compliance-Ready Framework for AI-Augmented Engineering — From Concept to Audit-Ready
> Delivery* — [ArXiv 2602.20684](https://arxiv.org/pdf/2602.20684)

The Sandbox 005 work adopts and extends this framework, specifically to address the non-determinism
gap: the published framework assumes more determinism than LLM systems provide. The extension —
evals over unit tests, LLM-as-judge as triage not verification, human gates as non-optional — is
the original contribution.

Before publishing any Series 2 article that references "Agile V":
1. Read the ArXiv paper in full
2. Cite it explicitly with authors, title, and ArXiv ID
3. State clearly where the extension begins and what problem it addresses that the original does not
4. Do not use the term "Agile V" as if it were invented here

**Links:**
- [Exploratory study of V-Model in ML-enabled software (ArXiv)](https://arxiv.org/html/2308.05381v3)
- [Proposed V-Model for AI verification and validation (IEEE)](https://ieeexplore.ieee.org/document/10207641/)
- [Verification and Validation of AI systems (SEBoK)](https://sebokwiki.org/wiki/Verification_and_Validation_of_Systems_in_Which_AI_is_a_Key_Element)

---

### S2-A3 — Context Architecture Is the New Software Architecture

The discipline that Series 1 gestures at, made precise. If the agent is a mirror of its context, then
the design of the context is the design of the system. Context architecture includes: what artifacts
exist for the agent to retrieve, how they are structured for retrieval, where human gates are placed,
how context poisoning is prevented across sessions, and how agent outputs become part of the
retrievable record.

This is not a new idea in disguise — it draws from information architecture, knowledge management,
and safety-critical documentation practices. What's new is that these disciplines now have direct
operational impact on software quality.

The artifact types: task contracts (explicit scope and boundaries for an agent session), experiment
requirement candidates (hypotheses before implementation), evidence bundles (outputs with provenance),
V&V evidence (verification and validation records), risk registers, and architecture decision records
structured for retrieval.

---

### S2-A4 — Separating the SDLC Stack from the Agentic Runtime

A practical architecture article. The development toolchain (CI, linters, test runners, code review)
and the agentic product runtime (the LLMs, orchestration, retrieval, and inference infrastructure)
must be kept separate. Conflating them produces systems where a deployment pipeline change can affect
model behavior and vice versa. The failure modes are different, the change cadences are different,
the verification approaches are different.

This is ADR-012 from the legal-tech-debt project made into a general principle. The SDLC stack is
deterministic and can be tested with traditional methods. The agentic runtime is non-deterministic
and requires evals and human gates. Mixing them means applying the wrong discipline to each.

---

### S2-A5 — Adversarial Agent Testing: Three Idiots in the Garden

Static evals run fixed datasets against an LLM and measure aggregate statistics. That catches known
failure modes — inputs you thought to include in your dataset. It doesn't find the failure modes you
didn't know to look for.

The complement is adversarial agent testing: agents with distinct behavioral personalities set loose
in a system with hidden infrastructure and constrained interventions, with the goal of finding what
breaks. This is chaos engineering applied to AI systems — not killing servers to find resilience
gaps, but running behaviorally distinct agents to find semantic and behavioral gaps.

The "three idiots" format from Granny's House Trials is the experimental vehicle for this concept:
a domestic scenario (yard drainage, hidden hydraulic dependencies) where bad interventions cause
visible collateral damage. Three agents with different personalities — the naive one who tries the
obvious solution badly, the aggressive one who pushes every boundary, the cautious one who finds
edge cases through excessive care — each surface different failure modes. The host judges meaning;
the system records facts. That separation is the human gate / evidence bundle pattern instantiated
as a playable format.

The theoretical connection: static evals measure known failure modes against a fixed rubric.
Adversarial agents explore the unknown failure space through behavioral diversity. Both are
necessary. A system that passes all your evals but breaks under a naive agent with no malicious
intent has a real problem that the evals didn't surface.

The eval framework connection: tools like DeepEval and Promptfoo handle the assertion layer.
The three-idiots format handles the adversarial exploration layer. Together they constitute a
complete non-deterministic system test methodology.

**Key claims:**
- Static evals and adversarial agent testing are complementary, not competing methodologies
- Behavioral diversity in test agents surfaces failure modes that dataset-based evals miss
- The human-host/system-records-facts structure maps directly to the human gate / evidence bundle
pattern in the V-model framework
- Chaos engineering for AI systems requires agents, not just bad inputs

**Note:** This article requires hands-on experimentation with the three-idiots format and evals
frameworks before it can be written with credibility. Flag for after Granny's House Trials Stage 2
and initial evals framework work are complete.

**Links:**
- [Beyond Traditional Testing: Non-Deterministic Software (AWS/dev.to)](https://dev.to/aws/beyond-traditional-testing-addressing-the-challenges-of-non-deterministic-software-583a)
- [Testing AI Agents: Validating Non-Deterministic Behavior (SitePoint)](https://www.sitepoint.com/testing-ai-agents-deterministic-evaluation-in-a-non-deterministic-world/)
- [Agentic AI Content Verification — Quality Gates (Pebblous)](https://blog.pebblous.ai/blog/agentic-content-pipeline-verification/en/)

---

### S2-A6 — LoRA and Behavioral Tuning as Engineering Discipline

**Not yet written — flag for 6+ months out.** Fine-tuning and behavioral adaptation of models is
reaching the point where it belongs in the practitioner's toolkit rather than the research lab.
LoRA (Low-Rank Adaptation) allows targeted behavioral tuning without full retraining. The
engineering discipline question: when do you tune vs. prompt-engineer vs. constrain via architecture?

This article should not be written until there is direct hands-on experience with LoRA tuning to
draw on. It is listed here to mark the roadmap, not as a near-term commitment.

---

## Publication Order

```
Week 1:   S1-A1  Vibe Coding Is the New Doomscrolling          ← Lead. Everything depends on this.
Week 3:   S1-A2  AI Makes Bad Code Worse
Week 5:   S1-A3  I Shipped More and Felt Worse
Week 7:   S1-A4  Why Documentation Fails
Week 9:   S1-A5  Vibe Coding Without Constraints Is Just Vibe Coding
Week 11:  S1-A6  Context Poisoning
Week 14:  S1-A7  RAG as Engineering Memory
Week 17:  S1-A8  GraphRAG and Architectural Memory
Week 20:  S1-A9  There Is No Such Thing as Clean Agentic Code
Week 23:  S1-A10 The Architecture I'm Building

(Series 2 articles: write in parallel with Series 1, publish on personal site,
cross-link from Series 1 articles where relevant. No fixed cadence.)
```

---

## What This Is Not

This is not a tutorial series. It is not a "how to use ChatGPT" series. It is not vendor content.

It is a coherent intellectual argument, published in installments, written for engineers who are
trying to figure out what rigorous AI-assisted development actually looks like. Every article
assumes the reader is technically literate and tired of hype. The argument should be useful to
a senior engineer even if they never hire Dorian for anything.

That is how it builds an audience worth having.
