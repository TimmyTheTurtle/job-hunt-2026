# Journal - 2026-06-16: Applied AI Identity, Job Search Deep Dive, And Resume Pivot

## Session Summary

This session moved the job search from "find plausible AI jobs" into a clearer identity and resume system.

The working identity is now:

> Applied AI Systems Engineer

But the more personal through-line is better:

> I build systems that turn messy domain material into structured, reviewable evidence. Right now, AI is becoming part of that system.

That sentence is important. It explains the shift without sounding defensive or artificial. It connects the old work and the new work:
- mission operations and systems discipline
- compliance reporting
- insurance/ledger data and derived-state reconstruction
- CPQ/configuration workflows
- legal/compliance document intelligence
- retrieval, provenance, structured evidence, and human review

The identity is not "AI as a label." It is the long-running pattern of turning messy domains into structured systems, with AI now becoming one more part of that system.

## Journal Process Note

This repo already treats journals as review artifacts.

The article notes frame journals, ADRs, handoffs, and summaries as the antidote to both missing context and unfiltered context overload. The useful purpose of an end-of-session journal is:
- preserve what changed
- capture why it changed
- name the decisions and boundaries
- leave a next-session entry point
- prevent future agents from reconstructing the same reasoning from scratch

This should become a normal end-of-session habit.

## Job Search Deep Dive

Created a deep-dive report from the 2026-06-16 job search run:

- `job_search/output/job_search_deep_dive_2026-06-16.md`

The main finding:

The strongest current roles are applied automation, document intelligence, workflow orchestration, and pragmatic AI implementation roles. The best current targets are not the most senior frontier-AI roles.

Best current or near-current targets from that pass:
- City of Hope - Intelligent Automation Developer
- Marco Technologies - AI Solutions / Agent Engineer
- Patch My PC - Software Engineer, AI
- Aline - Junior Agentic AI Engineer
- Ford - AI diagnostics / observability role
- micro1 - Software Engineer, Human Data Platforms
- Cotiviti and Chickasaw pending exact posting review

Future/stretch roles were useful as market language:
- Deloitte - Agentic AI Engineer, Healthcare AI
- Instacart - Senior Software Engineer II, AI Labs and Foundations
- Fabric Health - Staff Software Engineer, AI
- Newpage - AI Solution Engineer
- Ally - Principal Software Engineer
- Risepoint - Principal AI Engineer
- Stylitics - Senior AI Software Engineer, Labs

The search system was updated conceptually: the raw runner is not the decision-maker. Deep-dive review is now a named workflow:

- `job_search/DEEP_DIVE_WORKFLOW.md`

## Resume Review

Reviewed the existing resume material:

- `resumes/resume_simulation_v1.md`
- `resumes/resume_simulation_v1.docx`
- `resumes/resume_overhaul_notes.md`
- application notes and cover letters
- article-series notes
- job-search deep dive

The `.docx` was the real current resume. The markdown file was only a stub.

Main observation:

The old resume has stronger raw material than the old positioning suggests. The issue is not lack of evidence; it is that the top third says "generic software engineer" while the current market needs a sharper applied-AI/document/workflow story.

Strongest evidence identified:
- Finys: C# enterprise systems, undocumented subsystems, transactional ledger-style database, derived-state reconstruction, production correctness.
- RenoNerd / WindowConfigurator: .NET MVC, CPQ/configuration, pricing and estimation workflows, deployment, CRM/e-commerce integration planning.
- Areva: government-facing environmental/radiation compliance reporting automation with a real time-saving result.
- SED Systems: CSA CASSIOPE mission operations software and the origin of systems discipline.
- legal-tech-debt: current applied-AI/document-intelligence proof around structured evidence, provenance, deterministic detection concepts, LLM-assisted triage patterns, and human-reviewable outputs.

Created a resume strategy brief:

- `resumes/applied_ai_systems_resume_strategy_2026-06-16.md`

Created the first Applied AI Systems resume draft:

- `resumes/resume_applied_ai_systems_draft_v1.md`

Added GitHub to the resume header:

- `https://github.com/Dorian-Klingenberg`

## Truth Boundaries Corrected

Two important corrections were made after review:

1. Evals have not started yet.

Do not present evals as current hands-on experience. They are market language and a future growth area. Current wording should say:
- future eval work
- active growth area
- once hands-on work begins

2. RenoNerd / WindowConfigurator is not production-adjacent yet.

It can be described as:
- emerging production-minded .NET configurator work
- CPQ/workflow-system direction
- domain-constrained configuration and pricing logic
- business workflow and integration planning

Do not present it yet as:
- production-adjacent
- public SaaS
- commercial product evidence
- fully production-style B2B SaaS

This matters because the new identity only works if the claims stay narrow and defensible.

## Voice Note

The identity should not be explained primarily through negation.

Better voice:

> There are messy domains where important information is buried in documents, workflows, edge cases, old systems, or decisions nobody quite remembers. The work is to turn that into something structured enough to reason about.

Then connect to AI:

> AI can now touch parts of that problem that used to be too unstructured to automate cleanly. The useful work is the surrounding system: retrieval, constraints, evidence trails, human review points, and the practical pieces that make the result usable.

This was added to:
- `JOB_HUNT_CONTEXT.md`
- `AGENT_BOOTSTRAP_COMPACT.md`
- `agent_bootstrap_human.md`

## Resume Direction

The draft resume now leads with:

> Applied AI Systems Engineer

and the first-line summary:

> I build systems that turn messy domain material into structured, reviewable evidence.

The next resume pass should preserve that spine.

Recommended resume variants:
- Applied AI Systems Engineer - default for City of Hope, Marco, Aline, micro1, Cotiviti, Chickasaw
- C#/.NET + Applied AI Product Engineer - default for Patch My PC and .NET/AI bridge roles
- Systems AI / Diagnostics / Observability - default for Ford and systems/diagnostics roles

## Files Created This Session

- `job_search/DEEP_DIVE_WORKFLOW.md`
- `resumes/applied_ai_systems_resume_strategy_2026-06-16.md`
- `resumes/resume_applied_ai_systems_draft_v1.md`
- `journal/2026-06-16-applied-ai-identity-and-resume.md`

Generated but ignored output:
- `job_search/output/job_search_deep_dive_2026-06-16.md`

## Files Updated This Session

Key updated docs:
- `AGENT_BOOTSTRAP_COMPACT.md`
- `JOB_HUNT_CONTEXT.md`
- `agent_bootstrap_human.md`
- `current_strategy.md`
- `job-search-tips.md`
- `README.md`
- `HOW_TO_RUN_JOB_SEARCH.md`
- `job_search/README.md`

Resume docs:
- `resumes/resume_applied_ai_systems_draft_v1.md`
- `resumes/applied_ai_systems_resume_strategy_2026-06-16.md`

## Open Threads

Next useful steps:

1. Tighten `resume_applied_ai_systems_draft_v1.md` into an employer-facing version.
2. Build role-specific variants for the strongest current targets.
3. Verify exact legal-tech-debt implementation status before making project claims stronger.
4. Verify exact WindowConfigurator implementation status before strengthening .NET/product claims.
5. Begin evals work before adding evals to the active skills section.
6. Make end-of-session journals a recurring practice.

## Next Session Entry Point

Start from:

- `resumes/resume_applied_ai_systems_draft_v1.md`
- `resumes/applied_ai_systems_resume_strategy_2026-06-16.md`
- `job_search/output/job_search_deep_dive_2026-06-16.md`

The next concrete task is probably one of:
- compress the resume draft
- tailor it to Patch My PC
- tailor it to City of Hope
- verify legal-tech-debt and WindowConfigurator claims against their repos

