# S2-A8 — Contract Testing for Constrained LLM Nodes

**Status:** Not started

---

## Voice and Tone

- **Register:** technical and grounded. This is the most "engineering" article in the series.
  The reader is someone who has tried to test an LLM call and found that classical unit testing
  doesn't fit. Lead from that frustration into the reframe.
- **The claim is novel but not overclaimed.** The argument is not "you can test LLMs with TDD."
  It is: "the constraint design decision determines testability, and the test is a contract
  assertion, not an oracle comparison." Be precise about what that does and doesn't give you.
- **First person where you have done this.** The WindowConfigurator AI additions (voice-to-spec,
  vision measurement) are the concrete instance. Use them — they're the only published example
  of this pattern applied to a real system.
- **The practitioner tools are real but not academically validated.** Name PydanticAI
  TestModel/FunctionModel honestly — they exist, they are designed for this, there is no
  peer-reviewed study on their effectiveness. That gap is fine to name.
- **The literature gap is the article's credential.** The field has established that constraints
  reduce variance (LMQL) and that schema checks can be deterministic gates (Automated
  Self-Testing). Nobody has assembled these into a testing methodology. That assembly is this
  article's contribution.

---

## Thesis

Classical TDD breaks on LLM systems because the oracle assumption fails: you cannot write
`assert output == expected` when the output is stochastic. But the oracle is not the only
thing TDD requires. It requires a *failing assertion you can write before implementation*.

For a tightly constrained LLM node — fixed system prompt, schema-bound output, narrow task
scope — that assertion exists: output satisfies the output schema AND satisfies the business
logic invariant. The property is testable before the node is built. The red-green loop is
intact. The test is a contract assertion, not an oracle comparison.

This works because the constraint design decision converts the testable unit from "the output
string" to "the output contract." Schema conformance is deterministic. Business logic
invariants over schema-valid outputs are deterministic. The stochastic part of the LLM call
is inside the contract boundary, not outside it.

---

## The Literature Gap

The field has established:
- Constraints reduce output variance: LMQL (arXiv:2212.06094), grammar-constrained decoding,
  15-25 pp improvement on structured tasks
- Schema validation is a deterministic check: Automated Self-Testing (arXiv:2603.15676),
  schema checks as gates alongside probabilistic evaluators
- Classical TDD is explicitly rejected for agents: AgentAssay (arXiv:2603.02601), stochastic
  test semantics, three-valued verdicts
- Record & replay check functions as trust anchors on constrained workflows: arXiv:2505.17716

What nobody has assembled: these observations into a testing methodology. The gap is the claim
that *the contract is the testable unit*, and that contract can be written as a failing
assertion before the node exists. This article fills that gap.

---

## The Constraint Requirement

This methodology only applies to nodes that meet the constraint definition:

1. **Fixed system prompt** — not dynamically assembled, not pulling from ambient session state.
   The prompt is a constant. It can be read in a test without reconstruction.
2. **Schema-bound output** — the output contract is a named type. Pydantic model, TypedDict,
   JSON Schema. The schema is the output spec.
3. **Narrow task scope** — the node does one thing. It does not branch internally based on
   session context. Its behavior is determined by its inputs, not by global state.
4. **Typed inputs** — the node's inputs are declared. There is no ambient context. What the
   node receives is what the test can provide.

A node that violates any of these is not a candidate for contract testing. The violation is
a design smell (S2-A1): hard to test means poorly bounded.

---

## The Contract Testing Pattern

### Step 1 — Define the output contract

Before writing the node, write the output schema and the invariants that must hold over it.
These are the assertions.

```python
class WindowSpec(BaseModel):
    width_inches: float = Field(gt=0, lt=240)
    height_inches: float = Field(gt=0, lt=240)
    frame_type: Literal["casement", "picture", "awning", "fixed"]
    configuration: list[Literal["left", "right", "center"]]

# Business logic invariant:
# - configuration length must match the number of operable frames
# - picture frames have no configuration entry
```

### Step 2 — Write the failing contract assertion

```python
def test_voice_spec_parser_contract():
    result = parse_window_spec("58 by 35 right casement picture left casement")
    assert isinstance(result, WindowSpec)         # schema conformance
    assert result.width_inches == 58.0            # business logic: dimension maps to first number
    assert result.height_inches == 35.0
    assert result.frame_type_sequence == ["casement", "picture", "casement"]
    assert "picture" not in [c["type"] for c in result.configuration]  # picture frames excluded
```

This test fails before the node exists. It defines what "done" means.

### Step 3 — Build the node to pass the contract

Use PydanticAI TestModel or FunctionModel to run the test without a real LLM call during
development. Wire the real model in once the contract passes.

```python
# Development: FunctionModel returns fixture
# CI: real model, assertion still holds (or doesn't — that's the regression signal)
```

### Step 4 — Interpret failures correctly

A contract failure means one of:
- The node returned a schema-invalid output (implementation bug or model regression)
- The node returned schema-valid output that violates a business invariant (specification bug)
- The invariant was wrong and needs to be updated (specification evolution)

What a contract failure is NOT: a random fluctuation requiring a rerun. If the schema assertion
fails, something is broken. That is the property that makes this TDD-compatible.

---

## What This Does Not Give You

- **Output quality**: a node can satisfy the contract and still give wrong answers. Contract
  testing does not evaluate semantic quality. That requires evals (S2-A1).
- **Regression detection on quality**: a contract that passes says the node is schema-valid
  and invariant-conformant. It does not say it got better or worse. Quality regressions need
  the statistical layer.
- **Coverage of edge cases**: the contract is written over the declared schema. Edge cases
  outside the schema's constraint domain still require exploratory testing or evals.

---

## The Testing Economics Argument

Contract tests for constrained nodes are:
- **Fast**: no real LLM call in development (TestModel/FunctionModel)
- **Cheap**: no token spend during CI on the contract layer
- **Deterministic**: schema assertion either passes or fails, no probabilistic threshold
- **Actionable**: a failure points to a specific contract violation, not a statistical signal

Statistical evals are:
- **Slow**: require many real LLM calls for confidence
- **Expensive**: real token spend on every run
- **Probabilistic**: a drop in aggregate score requires interpretation
- **Broad**: detect behavioral regressions across the full output distribution

The pyramid follows from this. Run contract tests on every commit. Run evals periodically, or
on commits that change the node's prompt or schema. AgentAssay's sequential hypothesis testing
(arXiv:2603.02601) minimizes eval run count for statistical confidence — that is the right tool
for the eval layer, not for the contract layer.

---

## The WindowConfigurator Instance

The proposed AI additions to WindowConfigurator (voice-to-spec, vision measurement estimation)
are the concrete case for this methodology.

**Voice-to-spec node:**
- Input: raw utterance string ("58 by 35 right casement picture left casement")
- Output schema: `WindowSpec` with validated dimensions, frame sequence, configuration
- Business logic invariant: picture frames excluded from operable configuration list
- Test: written before the node; passes once the node satisfies the contract

**Vision measurement node:**
- Input: image bytes + unit preference
- Output schema: `MeasurementEstimate(value: float, unit: Literal["inches","mm"], confidence: float)`
- Business logic invariant: confidence in [0.0, 1.0]; value > 0
- Test: written before the node; contract failure = implementation bug, not model noise

The orchestration layer — combining voice spec and vision measurement into a validated window
order — is where non-determinism lives and where invariant specification (not contract TDD)
applies.

---

## Connection to Other Articles

- **S2-A1 (TDD Doesn't Work):** sets up the three-layer model; this article develops layer 1 fully
- **S2-A2 (V-Model):** contract testing for constrained nodes is the unit-test layer of the
  V-model adaptation; orchestration invariants are the integration layer
- **S2-A7 (Token Frugality):** contract testing with TestModel/FunctionModel costs zero tokens
  during development; the constraint decision is both a frugality decision and a testability
  decision

---

## Sources

- [AgentAssay: Token-Efficient Regression Testing (arXiv:2603.02601)](../papers/arxiv-2603.02601-agentassay.pdf) — explicit rejection of classical TDD; stochastic semantics for layer 3
- [LMQL: Prompting Is Programming (arXiv:2212.06094)](../papers/arxiv-2212.06094-lmql-prompting-is-programming.pdf) — grammar-constrained decoding reduces variance; evidence that constraints do work
- [Record & Replay for LLM Agents (arXiv:2505.17716)](../papers/arxiv-2505.17716-record-replay-llm-agents.pdf) — check functions as trust anchors; constrained replay as uncertainty reduction
- [Automated Self-Testing as Quality Gate (arXiv:2603.15676)](../papers/arxiv-2603.15676-automated-self-testing-quality-gate.pdf) — schema checks as deterministic gates alongside probabilistic evaluators
- [Agentic Agile-V / SCOPE-V (arXiv:2605.20456)](../papers/arxiv-2605.20456-agentic-agile-v-scope-v.pdf) — constraints as governance layer; Constrain step in SCOPE-V loop
- [Agentic SE: Foundational Pillars (arXiv:2509.06216)](../papers/arxiv-2509.06216-agentic-se-foundational-pillars.pdf) — structured constraints as core engineering discipline
- [PydanticAI TestModel/FunctionModel documentation](https://ai.pydantic.dev/testing-evals/) — practitioner tools for contract testing without real LLM calls (not peer-reviewed)
