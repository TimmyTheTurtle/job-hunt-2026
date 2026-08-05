# Contract Search Workflow

Use this when the user wants to look for contracting, consulting, fractional, or short-term project work around the Applied AI Systems Engineer identity.

This workflow is a sibling of the full-time job search. It uses the same runner and ledger machinery, but a separate profile:

```bash
./job_search/run_contract_search.sh
```

For test runs that should not mutate the ledger:

```bash
./job_search/run_contract_search.sh --dry-run --max-searches 3 --results-per-query 5
```

## Strategic Target

Target AI engineering contracts in legal, compliance, insurance, regulatory, audit, and document-heavy domains.

Forward-deployed AI engineering is a destination/current-stretch lane, not the only contract target. Also search for attainable applied-AI application, implementation, integration, document-automation, workflow-automation, and systems-integration work that builds the evidence needed for forward-deployed delivery.

Lead with:

> I build AI pipelines that turn unstructured legal and compliance documents into structured findings: automated detection, LLM-assisted triage, and human-readable reports, using systems engineering discipline throughout.

Prefer contract work that strengthens one or more of:

- document intelligence
- RAG / retrieval / evidence pipelines
- workflow automation
- compliance-sensitive AI systems
- human-reviewable outputs
- deterministic boundaries around AI components
- systems integration and implementation
- portfolio-quality artifacts that can be discussed publicly or semi-publicly

## Sources

Run the contract profile first, then add a manual sweep when the user wants serious discovery.

The runner covers:

- LinkedIn
- Indeed
- Google Jobs

Manual sweep targets:

- Ashby, Greenhouse, and Lever via search-engine `site:` queries
- YC Work at a Startup
- Hacker News "Who is hiring?"
- consulting and freelance marketplaces
- direct company career pages for watchlist companies
- recruiter/staffing firms with contract technical roles

## Manual Search Queries

Useful search-engine queries:

```text
"AI engineer" "contract" "remote"
"LLM engineer" "contract" "remote"
"RAG engineer" "contract" "remote"
"AI automation consultant" "remote"
"AI solutions engineer" "contract" "remote"
"document intelligence" "contractor" "AI"
"legal AI" "consultant" "contract"
"compliance automation" "consultant" "AI"
"fractional AI engineer"
"1099" "AI engineer" "RAG"
"corp-to-corp" "AI engineer" "remote"
```

ATS-specific queries:

```text
site:jobs.ashbyhq.com "contract" "AI engineer" "Remote"
site:jobs.ashbyhq.com "consultant" "RAG" "Remote"
site:job-boards.greenhouse.io "contract" "AI engineer" "Remote"
site:job-boards.greenhouse.io "AI solutions engineer" "contract"
site:jobs.lever.co "contract" "RAG" "Remote"
site:jobs.lever.co "consultant" "document intelligence"
```

## Review Fields

For each promising contract lead, capture:

- company/client or staffing firm
- title
- direct posting URL
- source
- remote/location/timezone constraints
- hourly rate or salary range if listed
- contract length
- expected weekly hours
- W2 contract, 1099, C2C, or unclear
- conversion-to-full-time risk
- client-facing load
- core stack and AI scope
- whether the work creates reusable portfolio evidence
- fit bucket

## Fit Buckets

Use these buckets:

- strong contract target
- current/stretch contract target
- business-development lead
- future/stretch market signal
- dismiss/archive
- noisy/unverified

Strong contract targets usually combine:

- concrete implementation work
- document-heavy or workflow-heavy AI use case
- RAG, extraction, triage, automation, or evidence assembly
- reasonable seniority and scope
- explicit remote compatibility
- hourly/rate transparency or a credible path to rate discussion
- enough independence to be useful without requiring mature production-AI credentials

Dismiss or archive when the role is mostly:

- pure AI trainer/content labeling
- unpaid/revenue-share speculation
- low-code-only automation
- sales/customer-success without engineering depth
- principal/staff production-AI ownership beyond current proof
- location/language mismatch
- vague "AI expert" work with no system boundary

## Output

If there are enough results, write a report under `job_search/output/`:

```text
contract_search_YYYY-MM-DD.md
```

Use this shape:

```markdown
# Contract Search - YYYY-MM-DD

## Executive Summary

## Strong Contract Targets

## Current / Stretch Contract Targets

## Business-Development Leads

## Future / Market Signals

## Dismiss / Noisy

## Rate / Scope Notes

## Resume / Pitch Notes

## Recommended Next Actions
```

Do not record ledger decisions unless the user explicitly asks.
