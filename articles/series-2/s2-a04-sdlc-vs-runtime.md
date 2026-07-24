# S2-A4 — Separating the SDLC Stack from the Agentic Runtime

**Status:** Not started

---

## Voice and Tone

- **Register:** ADR voice. This article argues for a separation that the author has already
  implemented (ADR-012 in legal-tech-debt). Write with the authority of someone who made this
  decision in a real system, not someone proposing it theoretically.
- **Name ADR-012 early as the source of the principle.** Then generalize. The direction
  is concrete-to-general, not principle-to-example.
- **First person throughout.** "I separated these stacks because..." is more credible than
  "teams should separate these stacks because..."
- **The SDLC/runtime distinction is not obvious.** Many readers will have conflated them
  without realizing it. Write to that reader — not condescendingly, but as someone who also
  conflated them before the problem made the distinction visible.
- **Token budget as a production constraint** (cross-ref S2-A7): one paragraph, written like
  the practical consequence it is. Not a detour — the SDLC/runtime argument is incomplete
  without naming who owns the token budget decision. Land it and move on.
- **Do not oversell the separation.** It is not a silver bullet. It is the minimum viable
  discipline for a system where the two stacks change at different cadences and fail in
  different ways.

---

## Thesis

The development toolchain (CI, linters, test runners, code review) and the agentic product
runtime (LLMs, orchestration, retrieval, inference infrastructure) must be kept separate.
Conflating them produces systems where a deployment pipeline change can affect model behavior
and vice versa.

This separation becomes sharper in the eval-driven-development frame: the SDLC stack owns the
definition, execution, and gating of evaluation evidence, while the runtime stack is the thing
being measured, monitored, and bounded.

This is ADR-012 from legal-tech-debt made into a general principle.

---

## Key Claims

- The SDLC stack is deterministic and can be tested with traditional methods
- The SDLC stack is where eval-driven development is operationalized: datasets, rubrics, CI gates,
  regression thresholds, and approval rules
- The agentic runtime is non-deterministic and requires evals and human gates
- Mixing them means applying the wrong discipline to each
- The failure modes are different, the change cadences are different, the verification
  approaches are different

---

## Token Cost as a Runtime Production Concern (cross-reference S2-A7)

The agentic runtime is where token spend happens. The SDLC does not currently have a "token
budget" gate analogous to a performance budget or a bundle size limit — but it should. Add
this to the article's argument:

- Runtime token costs must be planned at SDLC time, not discovered at billing time
- A token budget per workflow is a first-class production constraint: documented, monitored,
  alerted on — the same way response latency is
- The SDLC/runtime separation argument is incomplete without naming who owns the token
  budget decision. It is not the prompt engineer. It is the systems architect, at design time.

Forward-reference S2-A7 for the full economic argument.

---

## Sources

- ADR-012 from legal-tech-debt (internal reference)
- [Automated Self-Testing as a Quality Gate for LLM Applications (ArXiv)](../papers/arxiv-2603.15676-automated-self-testing-quality-gate.pdf)
- [LLM Observability: The Ultimate 2026 Guide — FutureAGI](https://futureagi.com/blog/what-is-llm-observability-ultimate-guide-2026/)
