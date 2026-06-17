# Job Search Source Research - 2026-06-16

Question: should the Applied AI Systems Engineer search look anywhere beyond the current runner?

Short answer: yes. Keep LinkedIn, Indeed, Google Jobs, and CyberCoders, but add a manual/secondary source layer focused on direct ATS pages, startup boards, and domain-company watchlists.

## Current Runner Coverage

Current default sites in `job_search/search_profile.json`:
- LinkedIn
- Indeed
- Google
- CyberCoders

Supported but not default through JobSpy:
- ZipRecruiter
- Glassdoor

Assessment:
- LinkedIn and Indeed are still necessary for broad coverage and compensation clues.
- Google is useful for discovery but unstable as a raw source.
- CyberCoders is worth keeping, especially now that the custom scraper is fixed.
- ZipRecruiter and SimplyHired-style sources are noisy; use them for occasional targeted sweeps, not as primary truth.
- The current runner misses many roles posted directly through Ashby, Greenhouse, Lever, and startup-specific boards.

## Best New Source Layer

### 1. Direct ATS Search: Ashby, Greenhouse, Lever

Many high-signal applied-AI roles live on ATS-hosted pages before or instead of appearing cleanly on general boards.

Important: these are not centralized job boards with one reliable search box. "Direct ATS search" means using a search engine to search public job pages hosted under the ATS domain.

For Ashby, search Google or Bing directly with `site:jobs.ashbyhq.com`. Example:

```text
site:jobs.ashbyhq.com "Applied AI Engineer" "Remote"
```

Then open the result that points to the specific company/job page, such as:

```text
https://jobs.ashbyhq.com/<company>/<job-id>
```

Same pattern for Greenhouse and Lever:

```text
site:job-boards.greenhouse.io "AI Solutions Engineer" "Remote"
site:jobs.lever.co "document intelligence" "RAG" "Remote"
```

Observed examples:
- Zapier, WorkOS, GC AI, Centralize, Benchling, Drata, LlamaIndex, and many startups use Ashby.
- Chainguard, Natera, NPR, Checkr, A-TEK, Sharebite, Osano, OpenSesame, and others use Greenhouse.
- Egen, BLEN, Factor Law, airSlate, Filevine, Mistral, and others use Lever.

Use manual search queries like:

```text
site:jobs.ashbyhq.com ("Applied AI Engineer" OR "AI Solutions Engineer" OR "Software Engineer (Applied AI)") ("Remote" OR "United States") (RAG OR "document intelligence" OR workflow)
site:job-boards.greenhouse.io ("AI Engineer" OR "AI Solutions Engineer") ("Remote" OR "United States") (RAG OR "document intelligence" OR "workflow automation")
site:jobs.lever.co ("AI Engineer" OR "Applied AI" OR "AI Solutions") ("Remote" OR "United States") (RAG OR "document intelligence" OR legal OR compliance)
```

Why this matters:
- These searches surfaced multiple roles that match the target language better than broad job-board queries.
- They also expose market language even when the role is too senior.
- They often include compensation and precise remote/location constraints.

Recommendation:
- Add an "ATS sweep" as a manual weekly step.
- Do not try to fully automate this yet unless the query results stay consistently valuable.

### 2. Wellfound

Wellfound is strong for startup AI roles:
- founding AI engineer
- forward-deployed AI engineer
- applied AI engineer
- RAG/LLM engineer
- AI product engineer

Observed signal:
- Many postings are too senior or too "production AI at scale" for current fit.
- Still useful for discovering market language and small companies building document/workflow AI.
- Better for future/stretch and contract/startup networking than immediate high-confidence applications.

Recommendation:
- Use manually once or twice per week.
- Save only roles that are engineering-heavy and do not require already-shipped production AI systems at scale.

### 3. Y Combinator Work At A Startup

YC's Work at a Startup is useful for:
- legal AI
- document automation
- applied AI product engineering
- founding engineer roles
- early-stage companies where direct project evidence matters

Observed examples:
- Legal/product engineer and founding AI roles in AI-native legal startups.
- Some roles include compensation and direct founder access.

Risks:
- Many roles are onsite SF/NY/London.
- Founding roles can expect intensity and senior production proof.
- Legal AI roles may require actual legal credentials; screen carefully.

Recommendation:
- Maintain a YC legal/document/AI watchlist.
- Use it for targeted outreach and market research, not volume applications.

### 4. Hacker News "Who Is Hiring?"

HN is useful because small teams often post more candidly than they do on formal job boards.

Observed signal:
- Recent threads include applied AI, RAG, full-stack AI, and founder-led hiring posts.
- Posts often expose process details, salary ranges, and direct email/application paths.

Recommendation:
- Check current and previous month's "Who is hiring?" thread monthly.
- Search within the thread for:
  - `AI engineer`
  - `applied AI`
  - `RAG`
  - `LLM`
  - `document`
  - `workflow`
  - `remote`
  - `legal`
  - `compliance`

### 5. Domain Company Watchlists

The best-fit roles may appear at companies whose names matter more than job-board source.

Maintain direct-careers watchlists for:

Legal/document AI:
- GC AI
- Filevine
- Ironclad
- Harvey
- Factor Law
- Lawhive
- LlamaIndex
- Hyperscience

Compliance/governance/privacy:
- Drata
- Credo AI
- Osano
- Vanta
- A-TEK / BLEN-style federal AI implementers, with citizenship/clearance constraints checked carefully

Document/workflow automation:
- airSlate
- Hyperscience
- OpenSesame-style internal AI workflow teams
- Chainguard-style internal AI solutions roles
- Zapier / n8n / automation-platform companies

Healthcare/document workflows:
- City of Hope
- Aline
- Fabric Health
- Natera
- Citizen Health
- Cotiviti

Recommendation:
- Add companies to `company_watchlist.md` when they produce a credible hiring signal.
- Prefer direct careers pages for named companies.

## Lower Priority Sources

### ZipRecruiter

Use occasionally for targeted searches like:

```text
"Remote Retrieval Augmented Generation"
"Azure AI Document Intelligence"
"AI workflow automation engineer"
```

Risks:
- noisy recruiter posts
- unrealistic requirements
- duplicated jobs
- low-signal contract listings

Recommendation:
- Do not add to default runner yet.
- Run occasional `--sites zip_recruiter` dry runs for targeted sweeps.

### Glassdoor

Useful for salary checking and employer reviews, but less useful as a primary source.

Recommendation:
- Do not prioritize as a search source.
- Use when evaluating a specific company.

### Built In / RemoteRocketship / TrueUp / Agentic Engineering Jobs

Useful as secondary aggregators and market-language sources.

Observed signal:
- RemoteRocketship surfaces remote AI engineer roles with compensation and company tags.
- TrueUp claims broad AI job coverage and can be useful for trend scanning.
- Agentic Engineering Jobs is narrowly aligned with RAG/agent/LLM roles.
- Built In is useful for startup/company discovery and remote AI role lists.

Recommendation:
- Use for discovery and alerts, not as canonical source.
- Follow through to the original company posting before recording or applying.

## Search Terms To Add To Manual Sweeps

The current runner's title strings are good, but manual searches should include more market variants:

```text
"Applied AI Engineer"
"Software Engineer (Applied AI)"
"AI Product Engineer"
"Forward Deployed AI Engineer"
"Forward Deployed AI Solutions Engineer"
"AI Solutions Engineer"
"AI Enablement Engineer"
"Intelligent Automation Developer"
"AI Automation Engineer"
"Agentic AI Engineer"
"Document Intelligence Engineer"
"Document Understanding Engineer"
"Human Data Platforms"
"RAG Engineer"
"LLM Systems Engineer"
"AI Workflow Automation"
"MCP" "RAG" "remote"
"document intelligence" "RAG"
"legal AI" "software engineer"
"compliance AI" "software engineer"
```

## Recommended Weekly Source Mix

1. Run the repo search runner.
2. Do an ATS sweep across Ashby, Greenhouse, and Lever.
3. Check YC Work at a Startup for legal/document/applied-AI startups.
4. Check the current HN "Who is hiring?" thread.
5. Check company watchlist direct careers pages.
6. Use RemoteRocketship / TrueUp / Built In / Agentic Engineering Jobs for discovery.
7. Use ZipRecruiter only as a targeted dry-run source.

## Practical Recommendation

Do not expand the automated runner too aggressively yet.

Better next step:
- keep current runner as the broad recurring scan
- add a documented manual `ATS + startup sweep`
- track promising companies in `company_watchlist.md`
- only automate a source after it repeatedly produces good leads

This keeps the system from becoming noisy while still widening the search beyond Indeed/LinkedIn/Google.
