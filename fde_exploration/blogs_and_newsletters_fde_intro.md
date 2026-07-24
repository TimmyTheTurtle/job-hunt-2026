# Blogs And Newsletters For FDE Intro

Date: 2026-07-23

## Purpose

This is a curated list of blogs, engineering guides, and newsletters that best support a
forward-deployed AI engineering learning path.

The focus is on sources that help answer:

- when to use agents versus simpler workflows
- how to design tools and boundaries
- how to evaluate and monitor systems
- how to think about governance, reliability, and production delivery

## Recommended Reading Order

1. provider guides for current agent best practices
2. engineering notes on evals, tools, and trust
3. field-oriented architecture patterns
4. recurring newsletters/bloggers who track the space well

## Recommended Sources

### 1. OpenAI Learn / Practical Agent Guides

Links:
- [A practical guide to building AI agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- [OpenAI Learning Hub](https://openai.com/business/learn/)

Why read:
- strongest current source for mainstream agent design guidance
- practical advice on workflow selection, tool design, instructions, orchestration, and guardrails
- clearly production-minded

Maps to learning path:
- workflow discovery and scoping
- tool boundaries
- guardrails
- human intervention design

Best for:
- deciding when AI belongs in a workflow
- learning the baseline vocabulary hiring teams now use

### 2. Anthropic Engineering

Links:
- [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents?src_trk=em67ed76512686f3.435449232057658369)
- [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents?s=08)
- [Trustworthy agents in practice](https://www.anthropic.com/research/trustworthy-agents)

Why read:
- one of the best current collections for understanding simple-vs-complex architectures
- especially strong on evals, tool design, and trust boundaries
- unusually relevant to your "deterministic core, AI at the edges" instinct

Maps to learning path:
- workflow orchestration
- evals and observability
- tool contract design
- governance and human oversight

Best for:
- turning your existing architectural instincts into more standard agent-engineering language

### 3. LangChain Blog

Link:
- [LangChain blog](https://blog.langchain.dev/)

Example surfaced by search:
- [Quickly Start Evaluating LLMs With OpenEvals](https://blog.langchain.dev/evaluating-llms-with-openevals/)

Why read:
- useful for implementation-oriented discussions
- good source for evaluation, tracing, and workflow tooling topics
- worth following even if you do not standardize on LangChain

Maps to learning path:
- evaluation
- workflow implementation
- testing and feedback loops

Best for:
- practical engineering patterns
- implementation ideas for learning projects

### 4. Martin Fowler / Thoughtworks GenAI Articles

Links:
- [Emerging Patterns in Building GenAI Products](https://martinfowler.com/articles/gen-ai-patterns/)
- [Feedback Flywheel](https://martinfowler.com/articles/reduce-friction-ai/feedback-flywheel.html)
- [Agentic Email](https://martinfowler.com/bliki/AgenticEmail.html)

Why read:
- best fit for your systems and engineering-craft sensibility
- emphasizes field-tested patterns instead of hype
- especially good for understanding risk, abstraction, and operational learning loops

Maps to learning path:
- workflow scoping
- review and feedback loops
- governance and risk
- production discipline

Best for:
- architectural framing
- developing a non-hype, engineering-first vocabulary

### 5. Simon Willison's Weblog

Links:
- [Writing about Agentic Engineering Patterns](https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/)
- [Vibe engineering](https://simonwillison.net/2025/Oct/7/vibe-engineering/)
- [parallel-agents tag](https://feeds.simonwillison.net/tags/parallel-agents/)

Why read:
- one of the best ongoing sources for grounded practitioner thinking
- strong on context limits, subagents, tool use, and responsible use of coding agents
- highly compatible with your article-series concerns

Maps to learning path:
- workflow orchestration
- context management
- human accountability
- production coding discipline

Best for:
- staying current
- absorbing practical instincts from someone shipping and observing the space closely

### 6. Decoding AI Magazine

Link:
- [Decoding AI Magazine](https://www.pauliusztin.ai/aimagazine)

Why read:
- directly focused on escaping PoC purgatory and shipping AI products
- unusually aligned with your current transition from concept-heavy work to deployable systems
- good ongoing complement to deeper engineering sources

Maps to learning path:
- full-stack AI delivery
- production mindset
- project and portfolio shaping

Best for:
- recurring tactical guidance
- keeping momentum on shipping-oriented learning

## Best "Start Here" Picks

If you only follow three:

1. OpenAI Learn
2. Anthropic Engineering
3. Simon Willison's Weblog

Why:
- together they cover workflow selection, tool/eval discipline, and practitioner-level pattern
  thinking

## Reading Habit Suggestion

Use a three-layer habit:

- weekly: one practitioner blog or newsletter issue
- every two weeks: one deeper engineering guide
- monthly: one long architecture or pattern article tied to a project you are building

That keeps the reading connected to actual work instead of turning into passive intake.
