# S2-A2 — The V-Model Was Built for This Problem

**Status:** Not started

---

## Thesis

The V-model predates LLMs by decades. It was developed for aerospace and medical devices —
systems where behavior can't be fully specified before implementation, requirements are expressed
in natural language with interpretive ambiguity, and failure modes require human judgment to
evaluate. LLM systems share all three properties. This isn't a coincidence. It's structural.

---

## Key Claims

- Verification (building the system right) is partially automatable for LLM systems
- Validation (building the right system) requires human judgment — always
- Sprint-based TDD workflows don't map onto LLM component development
- The V-model's decomposition-then-integration structure, with explicit V&V gates, does

---

## Attribution Note — IMPORTANT

The term "Agile V" is **not original to this work.** Source:

> *Agile V: A Compliance-Ready Framework for AI-Augmented Engineering* —
> [ArXiv 2602.20684](https://arxiv.org/pdf/2602.20684)

The Sandbox 005 work adopts and extends this framework to address the non-determinism gap.
Before publishing this article:
1. Read the ArXiv paper in full
2. Cite it explicitly with authors, title, and ArXiv ID
3. State clearly where the extension begins and what problem it addresses that the original
   does not

---

## Sources

- [Agile V: A Compliance-Ready Framework (ArXiv 2602.20684)](https://arxiv.org/pdf/2602.20684)
- [Exploratory study of V-Model in ML-enabled software (ArXiv)](https://arxiv.org/html/2308.05381v3)
- [Proposed V-Model for AI verification and validation (IEEE)](https://ieeexplore.ieee.org/document/10207641/)
- [Verification and Validation of AI systems — SEBoK](https://sebokwiki.org/wiki/Verification_and_Validation_of_Systems_in_Which_AI_is_a_Key_Element)
- [Model-Based Testing of Non-Deterministic Systems (PDF)](https://marcfrappierudes.github.io/Papers/Model_Based_Testing_of_Non_Deterministic_Systems.pdf)
- [The Systems Engineering Approach in Times of LLMs (ArXiv)](https://arxiv.org/pdf/2411.09050)
- [AI Systems Engineering: rescuing AI from the valley of death — OpenChain](https://openchainproject.org/news/2026/03/26/ai-systems-engineering-the-new-discipline-to-rescue-ai-from-the-valley-of-death)
- [Model-Based Systems Engineering and Agentic AI — MathWorks](https://blogs.mathworks.com/simulink/2026/04/26/model-based-systems-engineering-and-agentic-ai/)
