# Contract Search - 2026-06-16

Source runner dry run: `job_search/output/job_search_2026-06-16_143802.md`  
CSV dry run: `job_search/output/job_search_2026-06-16_143802.csv`

No ledger decisions were recorded. The runner was executed with `--dry-run`.

## Executive Summary

The contract-search workflow is viable, but it needs to stay two-layered:

1. Run the dedicated contract profile for staffing-board and job-board coverage.
2. Follow with manual web/ATS searches for rate-bearing contract roles.

The runner found several plausible contract leads, especially W2 staffing-style AI engineer roles in Michigan and remote AI engineer listings. The manual web sweep was stronger for compensation and scope details.

## What Was Added

- `job_search/search_profile_contracting.json`
- `job_search/run_contract_search.sh`
- `job_search/CONTRACT_SEARCH_WORKFLOW.md`
- runner support for profile-level or search-level `job_type`
- contract markers in scoring
- stronger filters for legal-practice roles, commission/business-development roles, and obvious non-US locations

## Runner Results

- Profile: `applied_ai_systems_contracting_v1`
- Sites: LinkedIn, Indeed, Google
- Search specs run: 20
- Existing application URLs known: 14
- Suppressed by search ledger: 6
- Suppressed by application folders: 0
- Ranked results: 30
- Ledger transaction: dry run, not recorded

## Strong Contract Targets

- CBTS - AI Software Engineer III (Only W2, No Third party) - Detroit, MI  
  https://www.linkedin.com/jobs/view/4415111443  
  W2-only AI software engineering contract signal. Needs link follow-up for rate, duration, stack, and onsite/remote expectations.

- CBTS - AI Software Engineer III (W2 Contract only) - Detroit, MI  
  https://www.linkedin.com/jobs/view/4415121150  
  Similar to the above; likely duplicate or sibling posting. Worth one deep dive because it is local, contract-shaped, and software-engineering-forward.

- Presto Phoenix, Inc. - AI Engineer (Contract)  
  https://www.linkedin.com/jobs/view/4426608544  
  Clean title signal. Needs direct review because LinkedIn did not expose location, rate, or requirements.

- IC Resources - Python / LLM Engineer (Contract or Permanent)  
  https://www.linkedin.com/jobs/view/4426746074  
  Good LLM/contract title signal, but location is unknown from runner output and may be non-US. Review before spending energy.

## Current / Stretch Contract Targets

- Insight Global - AI Engineer search result / contract AI engineer roles  
  https://jobs.insightglobal.com/find_a_job/?miles=False&remote=true&srch=AI+engineer  
  The page exposes multiple relevant contract roles. One remote/Los Angeles listing is a Senior AI Engineer contract at about $59-$74/hr with .NET, Azure, MCP, LLM/RAG, regulated enterprise integration, and governance language. A Boston legal-AI contract/permanent-possible listing shows about $64-$80/hr estimated and later text mentions $75-$85/hr for legal AI application work. These are stretch on years-of-experience, but excellent market signals for Dorian's positioning.

- Azul - Marketing AI Engineer (4 Month Contract) - Remote US - $35/hr  
  https://jobs.lever.co/azul/97327568-3154-4019-99f6-f1df6b520cc2  
  Strong AI workflow/MCP/RAG/agentic-workflow language, but marketing-domain and low rate. Useful as market evidence; probably not a first-choice application unless the scope is unusually portfolio-friendly.

- US Tech Solutions - AI-Powered Python Automation & Document Processing Engineer  
  https://www.linkedin.com/jobs/view/4426178706  
  Strong title language around Python automation and document processing. Runner found Dallas, TX; needs review for remote/contract details.

- HTC Global Services - Senior AI Engineer - Generative AI & Machine Learning - Dearborn, MI  
  https://www.linkedin.com/jobs/view/4427755395  
  Local staffing-style signal, but likely senior/stretch and needs rate/duration details.

- Stefanini North America and APAC - Artificial Intelligence Engineer - Dearborn, MI  
  https://www.linkedin.com/jobs/view/4413765263  
  Local staffing-style AI engineer signal. Needs deep dive.

- Tata Consultancy Services - Senior Engineer - Agentic AI - Troy, MI  
  https://www.linkedin.com/jobs/view/4414780196  
  Local agentic-AI market signal. Likely senior/stretch.

## Business-Development Leads

These may be better outreach/watchlist sources than direct applications:

- GreenLight.ai / GreenLight Workforce Solutions - Full-Stack AI Engineer / Workflow Automation Lead  
  https://jobs.ashbyhq.com/greenlight-workforce-solutions/340a15c0-3a4a-4d1f-b793-b05ceb5f9eac  
  Search result identifies the role as remote and contract-or-full-time. Strong title fit; direct page requires JavaScript, so follow-up needs browser or another source.

- Blacksmith Agency - AI Engineer - Contract / Remote  
  https://jobs.ashbyhq.com/blacksmith%20agency/5dfccfc8-a527-44b9-b3ec-eaee25fc3f0f  
  Search result identifies the role as contract and remote. Needs deeper review.

- Infinity - Full Stack AI Engineer / AI Engineer Contract-to-Hire  
  https://jobs.ashbyhq.com/infinity-constellation/30fac65e-bcd7-4ecc-9477-fc7c8c8a9f52  
  Search result showed remote global, contract-to-hire trial, and $75/hr for first 4 weeks. Needs direct validation because the Ashby page requires JavaScript.

## Future / Market Signals

- Protagonist Therapeutics - AI Consultant - Contract - $150-$200/hr, onsite 4 days/week  
  Found via Indeed AI automation consultant search. The rate is excellent and the scope includes MCP, APIs, enterprise connectors, and workflow automation, but onsite Newark, CA likely makes it a dismiss unless travel/on-site constraints are somehow flexible.

- Hare and Turtle AI Solutions - AI Consultant - $70-$90/hr  
  Found via Indeed search. Strong agentic AI, RAG, observability, enterprise governance language. Needs direct review for location and contract terms.

- Frontapp - Operations AI Engineer (Contract) - $125-$150/hr  
  Found in broader search results for hourly AI roles. Very strong rate signal, but likely Bay Area/hybrid or high-experience. Worth knowing as market evidence.

## Dismiss / Noisy

- Riverbed Technology - Performance Consultant  
  Runner scored this highly because of compliance/performance/remote/workflow language, but it does not yet look like an AI engineering contract.

- Reply - Consultant (m/w/d) - Generative AI  
  Likely non-US or not location-compatible.

- Elbit Systems of America - Principal Algorithm/AI Engineer  
  Too senior/principal and probably not the right contract target.

- Legal AI Consultant roles that are attorney/paralegal/legal-research roles  
  The filter was tightened to reject attorney, paralegal, and legal research analyst titles.

- Commission-based AI consultant/business-development roles  
  The filter was tightened to reject business-development and commission markers.

## Rate / Scope Notes

Early observed ranges:

- Low AI workflow contract: about $35/hr for Azul's 4-month marketing AI contract.
- Staffing-style AI engineer contracts: about $59-$85/hr from Insight Global examples.
- Specialist AI consultant postings: about $70-$90/hr in one Indeed result and $150-$200/hr for an onsite-heavy AI consultant result.
- Public salary pages/search pages suggest broad AI engineer hourly ranges around the $40-$80/hr band, but credible specialized contract work can go higher.

For Dorian, the more realistic near-term target band may be:

- minimum acceptable exploratory contract: about $50-$60/hr if portfolio value is high and scope is contained
- healthier W2/staffing target: about $65-$85/hr
- consulting/SOW target once the offer is crisp: about $85-$125/hr+

## Resume / Pitch Notes

Contracting wants a sharper offer than full-time search.

Best phrasing:

> I build AI pipelines for document-heavy workflows: ingestion, extraction, retrieval, triage, evidence trails, and human-reviewable reports.

Useful supporting terms:

- MCP connectors
- RAG pipelines
- document processing
- workflow automation
- enterprise integrations
- governed AI
- regulated environments
- structured/unstructured data
- human-in-the-loop review
- audit/evidence trail
- Python, .NET/C#, Azure, APIs

Avoid leaning too hard on:

- attorney/legal authority
- ML research depth
- production AI platform veteran claims
- generic prompt engineering
- low-code automation as the core identity

## Search System Notes

- The separate contracting profile works and should remain separate from the full-time profile.
- `job_type: contract` is now supported by the runner and passed through to JobSpy.
- Contract search needs manual web/ATS follow-up because many useful rate and contract details do not appear in runner output.
- LinkedIn returns many unknown-location staffing posts. Deep dive is required before classification.
- The filters now reject some obvious false positives, but the profile will still surface noisy consultant listings.

## Recommended Next Actions

1. Deep dive the two CBTS W2 contract postings first.
2. Deep dive Insight Global's AI Engineer contract listings and see whether direct application or recruiter contact is best.
3. Open Presto Phoenix, IC Resources, US Tech Solutions, HTC, Stefanini, and TCS postings to classify location, rate, duration, and seniority.
4. Add targeted manual searches for Dice, Insight Global, Motion Recruitment, Robert Half, Brooksource, Kforce, Apex Systems, TEKsystems, and CyberCoders contract variants.
5. Consider creating a short contractor-facing one-page pitch around document intelligence and compliance workflow automation.
