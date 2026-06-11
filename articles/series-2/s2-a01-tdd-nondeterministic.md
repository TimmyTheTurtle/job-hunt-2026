# S2-A1 — TDD Doesn't Work for Non-Deterministic Systems (And What Does)

**Status:** Not started

---

## Thesis

TDD rests on three assumptions LLM systems violate: determinism (same input always produces
same output), binary correctness (pass or fail), and fast cheap feedback (seconds, free). The
replacement methodology is evals. LLM-as-judge is triage, not verification.

---

## Key Claims

- TDD's red-green-refactor loop requires deterministic outputs — LLM systems are stochastic
- "Correctness" for LLM outputs is a distribution over a rubric, not a boolean
- Evals are the appropriate methodology: aggregate statistics over labeled datasets
- LLM-as-judge reduces human review volume but cannot verify — same non-determinism problem,
  plus correlation bias
- You can automate the running of evals; you cannot automate the interpretation

---

## Main Points to Discuss

- The three TDD assumptions and how each fails for LLM systems
- What evals are: structured evaluation runs against curated datasets with human-labeled
  ground truth, producing aggregate statistics
- A drop from 87% to 79% accuracy is a signal requiring human interpretation — not a failed
  test requiring a code fix
- The G-Eval framework: chain-of-thought evaluation, limit to 3-5 criteria, integer scales
- LLM-as-judge: useful for triage at scale (100k outputs in hours vs. 52 days human review),
  but bounded by correlation bias and hallucination
- The human gate is non-optional — it is not a fallback for uncertainty, it is the only
  mechanism that can validate against real-world requirements

---

## Sources

- [LLM as a Judge: guide and best practices — Agenta](https://agenta.ai/blog/llm-as-a-judge-guide-to-llm-evaluation-best-practices)
- [LLMs-as-Judges: comprehensive survey (ArXiv)](https://arxiv.org/pdf/2412.05579)
- [LLM judge cookbook — Hugging Face](https://huggingface.co/learn/cookbook/en/llm_judge)
- [Beyond vibe checks: complete guide to evals — Lenny's Newsletter](https://www.lennysnewsletter.com/p/beyond-vibe-checks-a-pms-complete)
- [A pragmatic guide to LLM evals — Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/evals)
- [LLM testing frameworks and tools — TestOmat](https://testomat.io/blog/llm-test/)
- [Beyond Traditional Testing: Non-Deterministic Software — AWS/dev.to](https://dev.to/aws/beyond-traditional-testing-addressing-the-challenges-of-non-deterministic-software-583a)
- [Testing AI Agents: Validating Non-Deterministic Behavior — SitePoint](https://www.sitepoint.com/testing-ai-agents-deterministic-evaluation-in-a-non-deterministic-world/)
