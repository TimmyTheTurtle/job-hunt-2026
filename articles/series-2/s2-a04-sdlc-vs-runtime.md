# S2-A4 — Separating the SDLC Stack from the Agentic Runtime

**Status:** Not started

---

## Thesis

The development toolchain (CI, linters, test runners, code review) and the agentic product
runtime (LLMs, orchestration, retrieval, inference infrastructure) must be kept separate.
Conflating them produces systems where a deployment pipeline change can affect model behavior
and vice versa.

This is ADR-012 from legal-tech-debt made into a general principle.

---

## Key Claims

- The SDLC stack is deterministic and can be tested with traditional methods
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
