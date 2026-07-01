# AGENT BOOTSTRAP COMPACT

intent:
- produce honest, tactically strong, strategically coherent job-hunt materials
- support EA/UI compliance, runway preservation, employer outreach, market research, and applied AI systems identity-building

candidate_default:
- Applied AI Systems Engineer
- systems-oriented software engineer moving into applied AI systems
- practical builder
- strong debugger
- business-aware technical problem solver
- growth path toward document intelligence, compliance-sensitive AI workflows, RAG/retrieval, future eval work, and production-minded AI boundaries

positioning_preferred:
- applied AI systems engineer
- AI solutions engineer
- LLM / RAG systems engineer
- document intelligence engineer
- AI workflow / automation engineer
- software engineer, AI systems
- compliance AI engineer when engineering-heavy
- technical solutions / implementation engineer
- systems-minded software engineer

positioning_avoid:
- indie game developer
- vague generalist hacker
- prompt engineer
- AI enthusiast without technical substance
- ML researcher
- lawyer, compliance officer, or regulatory expert
- production LLM platform veteran

contractor_pitch:
  target: AI engineering contracts in legal, compliance, insurance, and document-heavy domains
  one_liner: >
    I build AI pipelines that turn unstructured legal and compliance documents into structured
    findings — automated detection, LLM-assisted triage, and human-readable reports —
    using systems engineering discipline throughout.
  se_discipline_angle: >
    Unlike most AI contractors who wire up APIs and move on, I apply systems engineering
    discipline: requirements traceability, deterministic boundaries, human verification gates,
    and evidence trails. Clients get systems that can be audited, debugged, and extended —
    not black boxes that worked once in a demo.
  full_pitch: see JOB_HUNT_CONTEXT.md contractor_pitch section

core_priorities:
- truthful claims
- coherent career direction
- realistic fit
- learning value
- runway value
- reduced burnout risk
- preserve UI audit recordkeeping
- keep machine search ledger separate from manual tracker updates
- keep company watchlist records separate from application tracking
- treat job-search deep dives as market research plus resume calibration, not only application triage
- never mark `Applied` without updating application folder records, `master_tracker.md`, and ledger `decision_update`

long_term_vector:
- applied AI systems engineering
- document intelligence
- compliance-sensitive workflow automation
- RAG / retrieval / structured extraction
- future eval work and human-review gates
- traceable evidence pipelines
- production-minded AI boundaries
- modern C++
- simulation
- graphics
- real-time systems
- performance-aware engineering
- eventual deeper systems/HPC-caliber rigor as secondary technical depth

usable_background:
- SED Systems: mission ops software for CSA CASSIOPE satellite (2007–2010); secret clearance Canada, lapsed
- Areva Resources: automated compliance reporting for Canadian government regulatory review (2004–2005)
- legal-tech-debt: prototype AI/document intelligence evidence pipeline for insurance/legal/compliance text
- WindowConfigurator/RenoNerd: emerging .NET CPQ/configurator work with production-minded architecture direction; not production-adjacent yet
- RenoNerd ownership and practical delivery
- CPQ/configuration and workflow systems
- web deployment, IIS, Azure, plugin integration
- insurance/compliance-sensitive software thinking
- Google Ads and business-side technical operations

strongest_strengths:
- systems thinking
- debugging
- software engineering fundamentals
- translating messy needs into structure
- turning messy domain documents into structured artifacts
- traceability, validation, schemas, and audit-ready evidence
- independent learning
- ownership
- cross technical/business fluency
- strong written reasoning

identity_voice:
- define the identity through the positive through-line, not defensive negation
- preferred framing: Dorian keeps working in messy domains where documents, workflows, edge cases, old systems, or forgotten decisions need to become structured enough to reason about
- short version: "I build systems that turn messy domain material into structured, reviewable evidence. Right now, AI is becoming part of that system."
- use this for resume summaries, About Me drafts, LinkedIn copy, and portfolio language

growth_areas_safe_language:
- currently building
- actively developing
- focused on strengthening
- recent hands-on work includes

company_watchlist:
- use `company_watchlist.md` for employers Dorian wants to revisit before applying
- record company name, location, website, latest public hiring signal, posting URL if any, last checked date, and next check
- when user says "look for a job now," check the watchlist too
- do not create an application folder unless the user actually applies

role_tiers:
- Tier 1: applied AI systems, LLM/RAG, document intelligence, AI workflow automation, compliance/legal/insurance AI engineering
- Tier 2: pragmatic software, C#/.NET/SaaS, solutions, consulting, internal tools, applied reporting, systems/simulation roles with strong technical depth
- Tier 3: temporary stabilization roles only if needed for runway/UI compliance

cover_letter_rules:
- specific
- concise
- calm
- technically credible
- no desperation
- no fake enthusiasm
- no UI/unemployment discussion

recruiter_response_rules:
- brief
- warm but restrained
- ask for JD, compensation, location, stack when relevant

resume_bullet_rules:
- concrete
- honest
- outcome-oriented
- no invented numbers or scale

truth_never_fabricate:
- employers
- titles
- certifications
- years of experience
- production-scale HPC experience
- game-industry experience
- AI research depth
- security clearance
- unsupported domain expertise

default_workflow:
1. capture exact posting URL in job_description.md
2. read role carefully
3. evaluate fit
4. choose positioning angle
5. select relevant evidence only
6. draft materials
7. truthfulness audit
8. strategy audit

job_search_deep_dive:
- after a search run, use `job_search/DEEP_DIVE_WORKFLOW.md` when asked to follow links, classify surfaced roles, capture compensation, identify current vs future targets, or extract resume implications
- for serious discovery, pair the runner with `job_search/ATS_SWEEP_WORKFLOW.md` to check Ashby, Greenhouse, Lever, YC, HN, and direct company career pages
- for contracting/consulting/fractional searches, use `job_search/CONTRACT_SEARCH_WORKFLOW.md` and the `job_search/search_profile_contracting.json` profile; capture rate, contract length, W2/1099/C2C status, weekly hours, timezone constraints, and portfolio value
- do not treat generated `Apply First` buckets as final recommendations
- do not record ledger decisions during a deep dive unless the user explicitly asks

knowledge_graph_pipeline:
- article research lives in articles/series-*/; graph DB at articles/graph.kuzu (Kuzu, gitignored)
- pipeline: fetch-citations.py → download-refs.py → ingest.py --seeds-only → query.py
- API key in secrets/credentials.txt under SAMANTIC_SCHOLAR_API_KEY (typo — keep as-is)
- inline usage: SEMANTIC_SCHOLAR_API_KEY=$(grep SAMANTIC secrets/credentials.txt | cut -d= -f2) python3 scripts/fetch-citations.py
- query commands: search, explore, hot-refs, for-article, who-cites, citing
- search is case-sensitive substring; use hyphens ("test-driven" not "test driven")
- citations.json is tracked when it contains curated citation truth; PDFs, refs PDFs, and graph DB artifacts are ignored
- do not parse ref PDFs without explicit approval; use --seeds-only
- if ingest crashes: delete articles/graph.kuzu and articles/graph.kuzu.wal before rerunning
- full command reference in AGENTS.md Knowledge Graph Pipeline section

article_citation_integrity:
- citation validity requires source relevance, not just a resolving link
- local PDF citations must point to the exact named paper and should live in articles/papers/
- verify local PDFs by PDF header plus title/first-page text or reliable metadata
- do not substitute adjacent or loosely related papers for missing sources
- DOI-only/web-only sources must be recorded honestly as no-local-file
- when article citations change, update articles/papers/citations.json with title, authors, year, URL/DOI/arXiv ID, local file if present, verification status, and article relevance
- if a paper becomes an article citation, update the citation manifest and relevant script seed lists

applied_status_required_artifacts:
- applications/YYYY-MM_<company>_<role>/job_description.md
- applications/YYYY-MM_<company>_<role>/submission_snapshot.md
- applications/YYYY-MM_<company>_<role>/notes.md
- master_tracker.md row update
- job_search/ledger/transactions.jsonl decision_update with actor chat_update and status applied
