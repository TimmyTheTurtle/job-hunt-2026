# S2-A6 — LoRA and Behavioral Tuning as Engineering Discipline

**Status:** Not started — flag for 6+ months out

**Prerequisite:** Direct hands-on experience with LoRA tuning. Do not write until that exists.

---

## Thesis

LoRA belongs late in the architecture story — after loops, constraints, retrieval, and graph
structure stop delivering sufficient incremental gains. Fine-tuning the model's behavior is the
last lever, not the first, because it is expensive, hard to reverse, and easy to get wrong.

When it does become appropriate, LoRA (Low-Rank Adaptation) enables targeted behavioral tuning
without full retraining. The engineering discipline question: when do you tune vs.
prompt-engineer vs. constrain via architecture?

---

## Why LoRA Comes Last

The progression:
1. Improve loops (constraints, stopping conditions)
2. Improve retrieval (RAG, contextual retrieval)
3. Improve graph structure (GraphRAG, architectural memory)
4. Only then: adapt the model's behavior when earlier techniques show diminishing returns

---

## Potential LoRA Applications

- Clean-code-for-agents behavioral tuning
- Documentation discipline
- Article voice / authorial style
- Domain-specific task tuning without retraining a foundation model

---

## Sources

- [IBM LoRA overview](https://www.ibm.com/think/topics/lora)
- [IBM LoRA docs — watsonx](https://www.ibm.com/docs/en/watsonx/w-and-w/2.1.0?topic=tuning-lora-fine)
- [Efficient fine-tuning with LoRA — Databricks](https://www.databricks.com/blog/efficient-fine-tuning-lora-guide-llms)
- [LoRA adapters — MAX serve docs](https://docs.modular.com/max/serve/lora-adapters/)
- [LoRA adapters for embedding models — Superlinked](https://superlinked.com/docs/engine/lora)
- [LoRA adapters + semantic routing — Red Hat](https://www.redhat.com/en/blog/creating-cost-effective-specialized-ai-solutions-lora-adapters-red-hat-openshift-ai)
- [LoRA/QLoRA recommendations — Google Cloud](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/lora-qlora)
