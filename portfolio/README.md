# Portfolio

Status: Active organization layer
Purpose: Keep the public portfolio path aligned to production-ready commercial shape, not throwaway demos.

## Standard

Portfolio work should demonstrate applied AI systems engineering through systems that look like they could become paid work without a rewrite.

The working bar is:

> Deployable app shape, real user boundary, billing or invoicing path, audit trail, observability, safe demo data, and a documented cutover checklist.

This does not mean every project is already production deployed or commercially operating. It means the architecture, documentation, and demo path should be honest about stage while preserving the shape of a real product.

## Folder Map

- [production-readiness-checklist.md](production-readiness-checklist.md) - reusable checklist for every portfolio project.
- [projects/legal-tech-debt.md](projects/legal-tech-debt.md) - applied AI/document intelligence evidence workbench path.
- [projects/deep-research-tool.md](projects/deep-research-tool.md) - research evidence engine path.
- [projects/window-configurator.md](projects/window-configurator.md) - production-minded domain configurator path.
- [projects/articles-and-site.md](projects/articles-and-site.md) - public writing and demo landing surface path.

## Portfolio Anchors

| Project | Role in Portfolio | Current Stage | Production-Aligned Target |
|---|---|---|---|
| Legal Tech Debt | Applied AI/document intelligence proof | Research prototype in separate repo | Commercial-looking evidence workbench over synthetic legal/compliance documents |
| Deep Research Tool | RAG/GraphRAG/evidence pipeline proof | Starter architecture in this repo | Multi-workspace research console with provenance, audit, and exportable evidence bundles |
| WindowConfigurator/RenoNerd | Production-minded domain software proof | External product/CPQ direction | Authenticated configurator with customer/workspace boundary and quote/invoice path |
| Articles + personal site | Public explanation layer | Drafting/research gate | Public case studies and demos that point to working systems |

## Working Rules

- [ ] Every portfolio project has a project brief under `portfolio/projects/`.
- [ ] Every portfolio project uses the reusable readiness checklist or explains why a checklist item does not apply.
- [ ] Public demos use synthetic or demo-safe data unless live-data controls are explicitly in place.
- [ ] Claims distinguish `prototype`, `production-aligned`, `production-ready`, and `production customer` stages.
- [ ] User, tenant, billing, observability, and audit boundaries are designed before public positioning calls a project production-ready.
- [ ] The personal site should point to demos and case studies only after the project brief states what is safe to claim.

## Truth Language

Use:

- "production-aligned"
- "commercial skeleton"
- "deployable demo"
- "auth-ready"
- "billing-path designed"
- "synthetic-data public demo"

Avoid unless true:

- "production customer"
- "live SaaS"
- "SOC 2 ready"
- "compliance certified"
- "revenue-generating"
- "enterprise scale"
