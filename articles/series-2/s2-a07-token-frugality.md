# S2-A7 — Token Frugality Is a Design Discipline

**Status:** Not started

---

## Thesis

Token spend is the new cloud compute bill. It accumulates invisibly, scales with every
architectural mistake, and by the time it shows up on the dashboard it is baked into the
system. The answer is not prompt optimization as a post-hoc activity. Token frugality is a
design discipline: it must be designed in from the first architectural decision, not
retrofitted after the bill arrives.

The five levers — prompt caching, model routing, context discipline, tool call minimization,
and output compression — are not independent optimizations. They are a coherent design stance
that, taken together, determines whether a system is economically viable at production scale.
Each one has to be a first-class concern at architecture time. None of them can be meaningfully
bolted on later.

---

## Key Claims

- Token waste is an architecture problem, not a prompt engineering problem
- The cost structure of LLM APIs rewards specific design decisions and penalizes their absence
- Retrofitting frugality after launch fails because context bloat and verbose patterns compound
- A system without a model router is paying Opus prices for Haiku-class tasks — constantly
- Output tokens cost more than input tokens; asking a machine for prose when you need data
  is the most common and least noticed waste pattern
- Token frugality and context quality are the same discipline from different angles — S1-A6,
  S2-A3, and S2-A4 all arrive at frugality as a consequence; this article names it directly

---

## The Five Levers

### 1 — Prompt Caching

The cost structure: cache writes cost slightly more than base input tokens. Cache reads cost
roughly 10% of base input token price (model-dependent; check current pricing). The 5-minute
TTL means a prompt that is called frequently enough will pay the write cost once and the read
cost on every subsequent call.

What this requires at design time:
- **Stable prefix / volatile suffix structure.** The system prompt, persona, tools definitions,
  and static context must be at the top. The dynamic content (user query, session state, current
  task) must be at the bottom. This is not a convention — it is the structural requirement for
  cache hits. A prompt designed with dynamic content in the middle has no stable prefix and will
  never get a cache hit regardless of call frequency.
- **Explicit cache breakpoints.** On APIs that support manual cache control, mark the end of the
  stable prefix. On APIs that auto-cache, understand where the boundary falls and design to it.
- **Call frequency planning.** Cache-friendly design only pays off if the prompt is called
  frequently enough to amortize the write cost. Know your call patterns before committing to
  a caching strategy.

The failure mode: a system prompt that embeds the current date, session ID, or any dynamic
field near the top. Every call is a cache miss. The caching infrastructure exists and is never
used.

### 2 — Model Routing

The cost differential between model tiers is roughly 10-50x depending on provider and tier.
Using the most capable model for every call is the most expensive architectural decision a team
can make — and the most common default.

What token-frugal routing looks like:
- **Task classifier at the front of every workflow.** Before any task reaches a capable model,
  a lightweight classifier (cheapest available model, few-shot prompt) decides: is this a
  classification task, a retrieval task, a reasoning task, or a generation task? Route
  accordingly.
- **Capability thresholds, not model preferences.** Define the minimum capability required for
  each task class. Use the cheapest model that meets the threshold. Reserve the most capable
  model for tasks that require deep reasoning, synthesis across long context, or high-stakes
  judgment.
- **Fallback escalation, not default escalation.** Start cheap, escalate on failure or low
  confidence — not the reverse.

The failure mode: a single `model: "opus"` (or equivalent) hardcoded in the agent config. Every
classification, every retrieval confirmation, every formatting task runs at the highest tier.
The difference between this and a routed system is not marginal at scale.

### 3 — Context Discipline

Every token in the context window costs money on every call. A context window that grows
unchecked is not a feature — it is a cost multiplier applied to every subsequent interaction.

The connection to S1-A6 and S2-A3: context poisoning is a quality problem and a billing
problem simultaneously. A poisoned context does not just produce worse outputs — it produces
more expensive worse outputs. Context discipline (archive broadly, retrieve narrowly) is the
structural answer to both.

Design requirements:
- **Canonical / Reference / Scratch tiering** (S2-A3). Only canonical context goes into the
  window by default. Reference and scratch are retrieved on demand.
- **Context budget as a named constraint.** Each agent session has a maximum context size.
  It is documented. It is enforced. It is not "as much as fits."
- **Summarization over accumulation.** Long conversation history is compressed before being
  passed forward. Raw history is archived, not stuffed.

The compounding failure mode: a verbose system prompt → verbose agent responses → those
responses become context for the next call → the next call starts from a larger base → repeat.
Context bloat is self-reinforcing. The intervention must happen at design time.

### 4 — Tool Call Minimization

Each tool call is input tokens (the tool definition + call parameters) plus output tokens (the
tool result). An agent that makes 12 tool calls where 3 would do is not just slow — it is
paying for 9 unnecessary round trips on every execution of that workflow.

Design requirements:
- **Batch reads.** An agent that reads 5 files one at a time costs 5x the tool overhead of an
  agent that reads all 5 in a single batched call. Batch where the API allows it.
- **Don't sub-agent for trivial tasks.** Spinning up a sub-agent (with its own system prompt,
  tool definitions, and context initialization) for a task that could be a single tool call is
  the most expensive pattern in agentic systems. Reserve sub-agents for tasks with genuinely
  independent scope.
- **Read before deciding, not speculatively.** An agent that reads a file "just in case" on
  every run is paying for that read whether the information was needed or not. Design workflows
  where reads are triggered by actual need signals, not defensive reflexes.
- **Tool result compression before return.** A tool that returns 4,000 tokens of raw file
  content when the agent needs 200 tokens of specific facts should compress before returning to
  context. This is the most under-used frugality lever in practice.

AgentAssay (arXiv:2603.02601) is named for this problem: token-efficient regression testing.
Its sequential hypothesis testing methodology is the testing-layer answer to tool call waste —
run the minimum number of trials needed to reach statistical confidence, not a fixed N.

### 5 — Output Compression

Output tokens cost more than input tokens on most models (roughly 3-5x depending on tier and
provider). Asking for prose when the downstream consumer is a machine is the most common and
least noticed waste pattern in production systems.

Design requirements:
- **Output schema in the task contract.** If downstream is a machine (another agent, a database
  write, a structured log), specify the output format in the task contract. JSON over narrative.
  Field names over explanatory prose. Numbers over rounded descriptions.
- **Length constraints explicit, not implicit.** "Be concise" is not a constraint. "Maximum 3
  sentences" or "return only the JSON object, no explanation" is a constraint.
- **Separate reasoning from output.** If chain-of-thought is needed for quality, use extended
  thinking or a separate reasoning step. Don't include reasoning tokens in the final output
  that gets passed downstream.

---

## Why Retrofitting Fails

These five levers are not independent post-hoc optimizations. They interact:

- **Prompt structure determines cache hit rate** — you cannot retrofit a stable prefix into a
  prompt designed without one without rewriting the prompt from scratch.
- **Model routing requires a classifier** — the classifier is an architectural component. Adding
  it after a system is deployed means rearchitecting the entry point of every workflow.
- **Context bloat compounds** — a system that has been running verbose for six months has
  accumulated verbose patterns throughout its response history. Compressing that requires
  touching every layer that ingests prior outputs.
- **Tool call patterns are hardcoded in agent logic** — batching and compression must be
  designed into the tool definitions and agent workflow, not added as wrappers later.

The right time to make all five decisions is before the first prompt is written. The right
person to make them is the systems architect, not the prompt engineer.

---

## The Organizational Blind Spot

Development teams burn tokens freely. Experimentation accounts, expense cards, or free-tier
access create no feedback loop between API billing and development decisions. The patterns that
emerge in development — verbose prompts, single-model defaults, unbounded context, speculative
reads — get carried into production architectures unchanged.

By the time the production bill is visible, the patterns are baked in. The team has three
options: refactor the architecture (expensive), cap token usage (degrades quality), or pay
the bill (expensive indefinitely). None of these are good options. The fourth option — design
for frugality from the start — is only available before the system is built.

---

## Connection to Other Articles

- **S1-A6 (Context Poisoning):** Context hygiene and cost efficiency converge. A bloated,
  poisoned context is expensive and unreliable simultaneously. The Janitor concept is both a
  quality intervention and a cost intervention.
- **S2-A3 (Context Architecture):** The canonical/reference/scratch tiering model is a
  frugality architecture. Archive broadly, retrieve narrowly is a cost principle as much as a
  quality principle.
- **S2-A4 (SDLC vs Runtime):** The agentic runtime is where token spend happens. Treating
  runtime token costs as a production concern — with a budget, a monitor, and an alert — is
  the operational completion of the SDLC/runtime separation argument.
- **S1-A9 (Clean Agentic Code):** "Clean" for agents has an economic dimension that human-code
  cleanliness does not. A verbose prompt that works is not clean at scale. Small files, concise
  contracts, and compressed tool outputs are frugality decisions that also happen to be
  cleanliness decisions.

---

## Sources

- [Anthropic prompt caching documentation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)
- [Anthropic model pricing](https://www.anthropic.com/pricing)
- [AgentAssay: Token-Efficient Regression Testing (arXiv:2603.02601)](../papers/arxiv-2603.02601-agentassay.pdf)
- [Agentic AI in the SDLC (arXiv:2604.26275)](../papers/arxiv-2604.26275-agentic-ai-sdlc.pdf)
- [Agentic Software Engineering: Foundational Pillars (arXiv:2509.06216)](../papers/arxiv-2509.06216-agentic-se-foundational-pillars.pdf)
