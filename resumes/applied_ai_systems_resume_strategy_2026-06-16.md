# Applied AI Systems Resume Strategy - 2026-06-16

Purpose: synthesize the current repository evidence, existing resume, application materials, article plans, and job-search deep dive into a concrete plan for the next resume.

This is not the final resume. It is the resume design brief.

## Bottom Line

The new resume should not be the old simulation resume with AI keywords added.

The new resume should present Dorian as:

> Applied AI Systems Engineer focused on document intelligence, workflow automation, and human-reviewable AI systems for regulated or operational domains.

The strongest current story is:

> A systems-oriented software engineer who has built real business and enterprise software, handled messy domain workflows, and is now applying that discipline to AI-assisted document intelligence, evidence pipelines, and compliance-sensitive automation.

The resume needs to make that identity legible in the first third of page one.

## What The Current Resume Says

Source reviewed:
- `resumes/resume_simulation_v1.md`
- `resumes/resume_simulation_v1.docx`
- `resumes/resume_overhaul_notes.md`

Current resume identity:
- Software Engineer
- broad SDLC / full-stack / troubleshooting framing
- simulation/C++ direction implied by repo context, not strongly present in the actual docx

Current strengths in the existing resume:
- Finys: C# enterprise system work, undocumented subsystems, SQL, transactional ledger-style database, derived-state reconstruction, production correctness.
- RenoNerd: .NET MVC, CPQ/configuration, pricing/estimation workflows, IIS/Azure deployment, NopCommerce plugin, OAuth 2.0 / REST API exploration, business ownership.
- Caribou: client support, deployment testing, custom reports, AWS VMs/S3, SQL, troubleshooting, remote integration.
- SED: real mission-operations software for CSA CASSIOPE, classified/controlled information, systems discipline.
- Areva: automated government-facing environmental/radiation reporting, measurable time savings.

Current problems:
- The headline is too generic: "Software Engineer."
- The summary is too broad and HR-flavored.
- The most relevant current evidence, `legal-tech-debt`, is absent.
- WindowConfigurator is partly present as RenoNerd/CPQ work, but should be framed as emerging production-minded .NET product engineering rather than production-adjacent evidence.
- The resume does not show the applied AI direction early enough.
- The old simulation/C++ target does not match the current job-search deep dive.

## What The Job Market Deep Dive Says

Source reviewed:
- `job_search/output/job_search_deep_dive_2026-06-16.md`

Best current targets from the deep dive:
- City of Hope - Intelligent Automation Developer
- Marco Technologies - AI Solutions / Agent Engineer
- Patch My PC - Software Engineer, AI
- Aline - Junior Agentic AI Engineer
- Ford - AI diagnostics / observability role
- micro1 - Software Engineer, Human Data Platforms
- Cotiviti - Senior Software Engineer (AI), pending exact JD
- Chickasaw Nation Industries - AI Engineer, pending exact JD

Repeated role language:
- applied AI implementation
- intelligent automation
- workflow automation
- agentic workflows
- RAG / retrieval / vector search
- document intelligence / OCR / PDF / search
- evals / golden sets / LLM-as-judge, as market language and future growth rather than current hands-on evidence
- human-in-loop review
- traceability / auditability
- governance / guardrails
- APIs / system integration
- C#/.NET, Python, TypeScript/React where truthful
- regulated workflows and sensitive data care

Resume conclusion:
- Lead with applied AI systems and workflow/document evidence.
- Keep C#/.NET product engineering visible because several good roles use it as the bridge.
- Use healthcare/legal/compliance language as workflow context, not as claimed professional authority.

## Evidence Inventory

### Evidence To Lead With

#### legal-tech-debt

Use as the primary applied-AI direction proof.

Defensible claims from repo context:
- built or is building an applied AI/document intelligence prototype
- works with legal, insurance, compliance, or regulatory documents
- uses source provenance, evidence artifacts, schemas, and structured outputs
- includes deterministic detectors and LLM-assisted triage
- emphasizes human-reviewable outputs and audit-ready evidence
- explores RAG/retrieval, graph-backed evidence modeling, and typed defect records

Boundary:
- prototype/research evidence, not production SaaS
- do not claim legal expertise, patent authority, or production-scale LLM platform ownership

Resume use:
- place in a "Selected Projects" or "Applied AI Systems Work" section near the top
- make it the first proof that the pivot is real

#### WindowConfigurator / RenoNerd CPQ Work

Use as emerging production-minded .NET/product engineering proof. It is not production-adjacent yet, but it is an important direction and bridge.

Defensible claims from repo context and current resume:
- .NET MVC / C# product engineering
- custom PVC window CPQ/configuration logic
- pricing and estimation workflows
- validation/pricing direction and domain constraints, if supported by WindowConfigurator repo
- API/webhook/integration boundaries
- OAuth 2.0 / REST API exploration for multi-CRM interoperability
- IIS and Azure deployment
- NopCommerce plugin integration
- tests and ADRs, if/when supported by WindowConfigurator repo

Boundary:
- do not overstate as production-adjacent, a public SaaS, or a commercial product unless deployment/commercial status is clear
- separate active WindowConfigurator evidence from broader RenoNerd operations when needed

Resume use:
- make this the strongest professional/work-experience proof beneath the AI project
- use it to qualify for Patch My PC, Marco, City of Hope, and pragmatic .NET/AI bridge roles

#### Finys

Use as enterprise systems and data-reconstruction proof.

Defensible claims from extracted resume:
- implemented custom functionality in complex enterprise C# platform
- integrated with undocumented legacy and third-party subsystems
- reverse engineered black-box behaviors
- designed and optimized SQL against highly transactional ledger-style database
- reconstructed derived state from atomic records where reporting abstractions did not exist
- maintained correctness across service and database boundaries

Why it matters now:
- "ledger-style database" and "derived-state reconstruction" map surprisingly well to evidence pipelines, auditability, provenance, and state reconstruction.
- This should be reframed away from generic enterprise customization and toward structured reasoning over messy operational data.

Resume use:
- keep in experience section with 3-4 strong bullets
- connect to systems integration, data correctness, and auditability

#### Areva

Use as compliance-sensitive automation proof.

Defensible claims:
- automated reporting tools for environmental and radiation protection departments
- reports sent to Canadian government for monthly, quarterly, and annual licensing review
- saved up to 160 hours per year of remote on-site engineer time

Why it matters now:
- This is the clearest historical bridge to compliance-sensitive workflow automation.

Resume use:
- include in prior experience or selected early experience
- keep the measurable result

#### SED Systems

Use as origin story for systems discipline.

Defensible claims:
- Junior Programmer on CSA CASSIOPE mission operations system components
- handled classified/controlled information with Canadian Secret clearance, now lapsed
- developed/maintained mission operations system components
- worked on spectrum analyzer UI and near-earth object tracking UI prototype
- completed hardware configurations for MOS environment

Boundary:
- do not claim active clearance
- do not make aerospace the main resume identity unless targeting Ford/KLA/systems roles

Resume use:
- concise prior experience section
- phrase as "mission operations software" and "systems-discipline origin"

### Supporting Evidence

#### Caribou

Use selectively for:
- customer-facing technical support
- deployment/integration testing
- remote troubleshooting
- AWS VM and S3 backup management
- report porting from VB6 to .NET
- SQL and Boolean/set-logic troubleshooting

Resume use:
- collapse or compress if page length requires it
- keep only if targeting implementation/solutions roles

#### Article Series

Use as public-thinking proof, not resume bulk.

Strong ideas:
- context architecture
- RAG as engineering memory
- GraphRAG and architectural memory
- evals over unit tests for nondeterministic systems, as research direction rather than hands-on experience
- human gates and evidence bundles
- token frugality as system design discipline
- AI systems engineering / V-model adaptation
- legal tech debt taxonomy and diagnostic-agent architecture

Resume use:
- optional "Writing / Research" line or portfolio link once public
- do not overload resume with unpublished article plans

## Recommended Resume Architecture

### Header

Name, location, phone, email, LinkedIn, GitHub.

Use:
- GitHub: `https://github.com/Dorian-Klingenberg`

Target headline:

> Applied AI Systems Engineer

Alternate by role:
- AI Workflow Automation Engineer
- Software Engineer, AI Systems
- Document Intelligence Systems Engineer
- C#/.NET Software Engineer - Applied AI Systems

### Summary

Use 3 compact lines, not a paragraph.

Draft:

> Applied AI Systems Engineer with a C#/.NET software engineering background and hands-on work in document intelligence, workflow automation, and compliance-sensitive systems. Builds structured, human-reviewable AI workflows using retrieval, deterministic checks, evidence artifacts, and clear integration boundaries. Strong fit for applied AI implementation roles involving APIs, document workflows, human review, and operational traceability.

Notes:
- This is confident without claiming senior AI platform ownership.
- It foregrounds the bridge: software engineering + document/workflow AI.

### Core Skills

Group by story, not by generic keyword dump.

Suggested structure:

```text
Applied AI Systems: document intelligence, RAG/retrieval, LLM-assisted triage, evidence pipelines, human-in-loop review, traceable AI workflow boundaries
Software Engineering: C#, .NET, ASP.NET MVC/Core, REST APIs, SQL, Entity Framework, JavaScript, HTML/CSS
Workflow & Integration: CPQ/configuration logic, pricing/validation systems, webhooks, OAuth 2.0, CRM integration, deployment workflows
Data & Operations: SQL Server, transactional data modeling, derived-state reconstruction, reporting automation, auditability, provenance
Cloud & Platforms: Azure Web Apps, IIS/Windows Server, AWS VMs/S3, Linux
```

Only include Python, TypeScript, React, vector databases, LangChain, LangGraph, CrewAI, MCP, Docker, or Kubernetes if the underlying hands-on evidence is current and defensible.

### Selected Applied AI / Systems Projects

This section should appear before professional experience for AI-targeted resumes.

Possible entries:

#### Legal-Tech-Debt - Document Intelligence / Evidence Pipeline

Draft bullets:
- Built a prototype document-intelligence pipeline for legal/compliance text, organizing unstructured source material into structured evidence artifacts with provenance and human-reviewable outputs.
- Designed a legal/compliance defect taxonomy and schema-driven detection approach combining deterministic checks with LLM-assisted triage.
- Explored retrieval and graph-backed evidence modeling to support auditability, absence detection, and structured review over document-heavy workflows.

Truth audit:
- Use "prototype" and "explored" unless/until the pipeline is productionized or publicly demoed.
- Do not say "legal expert" or "compliance expert."

#### WindowConfigurator - .NET CPQ / Workflow System

Draft bullets:
- Designed and implemented .NET-based CPQ/configuration workflows for custom PVC windows, translating measurement, pricing, and product constraints into structured validation logic.
- Built integration-oriented architecture for CRM/e-commerce workflows, including REST/OAuth exploration and plugin-based extension paths.
- Maintained deployment and product-delivery workflows across IIS/Azure-hosted web systems and business operations.

Truth audit:
- Strengthen with exact test count, webhook/API details, or server-authoritative validation only after checking `D:\Repos\renonerd`.

### Professional Experience

#### Finys Inc. - Software Engineer

Draft emphasis:
- enterprise C#/.NET
- SQL/data correctness
- reverse engineering and undocumented systems
- state reconstruction
- integration boundaries

Draft bullets:
- Implemented custom functionality in a layered enterprise C# platform, integrating with undocumented legacy components and third-party subsystems.
- Reverse engineered black-box behavior across application and database layers to extend platform capabilities beyond previously supported use cases.
- Designed SQL logic against a highly transactional ledger-style database, reconstructing derived state from atomic records where reporting abstractions did not exist.
- Maintained correctness and data consistency across service and database boundaries in production feature work.

#### RenoNerd Inc. - Software Engineer / Deployment Specialist / Owner-Operator

Draft emphasis:
- .NET MVC
- CPQ/workflow software
- deployments
- business operations
- customer-facing systems

Draft bullets:
- Built and deployed client-facing .NET MVC tools for custom window configuration, estimating, quoting, and pricing workflows.
- Translated ambiguous product and installation constraints into domain-specific software used in operational quoting and planning.
- Integrated CPQ and estimation workflows into web/e-commerce experiments, including NopCommerce plugin work and CRM/API feasibility studies.
- Managed technical operations across website hosting, IIS/Azure deployment, business systems, and customer-facing delivery.

#### Caribou Software - Software Support Technician / IT Generalist

Draft emphasis:
- implementation/solutions support
- deployment testing
- customer-facing technical troubleshooting
- AWS and report migration

Draft bullets:
- Led integration and deployment testing for production releases and custom software components across forestry, oilfield, and construction clients.
- Supported SQL/reporting, estimation, invoicing, work-ticket, and maintenance-scheduling systems in remote multi-user environments.
- Managed AWS virtual machines and S3 backups while supporting customer data, remote hosting, and hardware/software integration.
- Ported and tested VB6 reports into .NET Framework workflows.

#### SED Systems - Junior Programmer

Draft emphasis:
- mission operations
- systems discipline
- controlled information
- UI/prototype work

Draft bullets:
- Developed and maintained mission operations system components for the Canadian Space Agency's CASSIOPE science satellite mission.
- Worked with classified/controlled information under Canadian Secret clearance, now lapsed.
- Supported MOS hardware configuration and built UI components for spectrum-analysis and near-earth-object tracking tools.

#### Areva Resources - Intern Programmer

Draft emphasis:
- compliance automation
- government reporting

Draft bullet:
- Automated environmental and radiation-protection reporting tools submitted for Canadian government licensing review, saving up to 160 hours per year of remote on-site engineer time.

## What To Remove Or Demote

Remove/demote:
- generic "industrious professional" summary language
- broad SDLC paragraph that could belong to anyone
- simulation-first headline for the default AI resume
- long lists of support responsibilities that do not support applied AI, workflow automation, or systems integration
- repeated bullets in the current Finys section
- unsupported C++/HPC/simulation emphasis unless targeting those roles

Keep but compress:
- older SED and Areva experience
- Caribou customer-support details
- business operations from RenoNerd

## Resume Variants Needed

### Variant A - Applied AI Systems Engineer

Default for:
- City of Hope
- Marco
- Aline
- micro1 Human Data Platforms
- Cotiviti
- Chickasaw
- Deloitte/Newpage future stretch roles

Lead with:
- legal-tech-debt
- document intelligence
- workflow automation
- retrieval/evidence/human review; evals only after hands-on work begins
- C#/.NET systems as supporting proof

### Variant B - C#/.NET + Applied AI Product Engineer

Default for:
- Patch My PC
- GM-style .NET roles with AI adjacency
- practical product engineering roles

Lead with:
- C#/.NET
- WindowConfigurator
- Finys
- APIs/integration
- AI work as active direction and project proof

### Variant C - Systems AI / Diagnostics / Observability

Default for:
- Ford
- KLA-like systems roles
- simulation/diagnostics/observability roles with AI adjacency

Lead with:
- SED
- Finys state reconstruction
- legal-tech-debt evidence/retrieval
- structured debugging
- traceability, logs, requirements, observability

## Open Questions Before Final Resume

Need confirm from `D:\Repos\legal-tech-debt`:
- exact implemented pipeline stages
- whether LLM-assisted triage is running or planned
- whether RAG/retrieval is implemented, experimental, or only designed
- names of artifacts that can be cited: ADRs, schemas, JSONL outputs, reports, detectors
- whether any public/synthetic demo exists

Need confirm from `D:\Repos\renonerd`:
- exact WindowConfigurator architecture
- current test count
- API/webhook details
- deployment status
- whether "server-authoritative validation/pricing" is already implemented
- whether voice input exists and should be mentioned

Need decide:
- whether the resume should include a "Selected Projects" section above professional experience
- whether to keep one page or accept two pages for AI/solutions roles
- whether to include article/writing work before anything is published

## Proposed Page-One Order

1. Header
2. Headline: Applied AI Systems Engineer
3. Three-line summary
4. Core skills grouped by applied AI / software / workflow / data
5. Selected Applied AI and Systems Projects
   - legal-tech-debt
   - WindowConfigurator
6. Professional Experience
   - Finys
   - RenoNerd
   - Caribou, compressed if space permits
7. Prior Experience
   - SED
   - Areva
8. Education

## Strongest New Resume Thesis

The resume should make one claim:

> Dorian is not a generic AI applicant. He is a software engineer with real experience turning messy operational domains into structured systems, now applying that discipline to document intelligence, workflow automation, and human-reviewable AI.

Everything in the resume should support that one claim.
