# ATS And Startup Sweep Workflow

Use this after the normal job-search runner when the user wants the job search to include direct ATS and startup sources.

This workflow covers roles that often do not surface cleanly through LinkedIn, Indeed, Google Jobs, or CyberCoders:
- Ashby-hosted postings
- Greenhouse-hosted postings
- Lever-hosted postings
- YC Work at a Startup
- Hacker News "Who is hiring?"
- startup/domain-company career pages

## When To Run

Run this when the user asks to:
- "do the job search"
- "look for jobs"
- "run the job search routine"
- "look beyond LinkedIn/Indeed"
- "do an ATS sweep"
- "search Ashby/Greenhouse/Lever"

For a quick compliance-oriented search, the normal runner may be enough.
For market research or serious role discovery, run this after the runner.

## Important Boundary

This is a manual/web-search workflow, not part of `job_search/run_search.py`.

Do not add every ATS source to the Python runner until a source repeatedly produces useful results and can be queried reliably. Use this workflow as the controlled second layer.

## Procedure

1. Run the normal search runner first unless the user explicitly asks for only the ATS sweep.
2. Search Ashby, Greenhouse, and Lever using search-engine `site:` queries.
3. Check YC Work at a Startup for legal/document/applied-AI startups.
4. Check the current Hacker News "Who is hiring?" thread.
5. Check direct careers pages for companies on `company_watchlist.md`.
6. For each promising role, capture:
   - company
   - title
   - direct posting URL
   - source
   - location / remote constraints
   - compensation if listed
   - why it is current target, stretch/future signal, or dismiss
7. If there are enough results, write a short sweep report under `job_search/output/`:

   ```text
   ats_sweep_YYYY-MM-DD.md
   ```

8. Do not record ledger decisions unless the user explicitly asks.

## Ashby Search

Ashby does not provide one useful central search box.

Use Google or Bing with `site:jobs.ashbyhq.com`.

Useful queries:

```text
site:jobs.ashbyhq.com "Applied AI Engineer" "Remote"
site:jobs.ashbyhq.com "AI Solutions Engineer" "Remote" "RAG"
site:jobs.ashbyhq.com "Software Engineer" "Applied AI" "United States"
site:jobs.ashbyhq.com "document intelligence" "AI Engineer"
site:jobs.ashbyhq.com "Forward Deployed AI Engineer" "Remote"
site:jobs.ashbyhq.com "AI Enablement Engineer" "Remote"
site:jobs.ashbyhq.com "Agentic AI Engineer" "Remote"
```

Open the specific company/job result, usually shaped like:

```text
https://jobs.ashbyhq.com/<company>/<job-id>
```

## Greenhouse Search

Use:

```text
site:job-boards.greenhouse.io "AI Solutions Engineer" "Remote"
site:job-boards.greenhouse.io "AI Engineer" "RAG" "Remote"
site:job-boards.greenhouse.io "document intelligence" "Remote"
site:job-boards.greenhouse.io "Forward Deployed AI" "United States"
site:job-boards.greenhouse.io "AI workflow" "Remote"
site:job-boards.greenhouse.io "Federal AI Solutions Engineer" "Remote"
```

## Lever Search

Use:

```text
site:jobs.lever.co "AI Engineer" "RAG" "Remote"
site:jobs.lever.co "document intelligence" "RAG" "Remote"
site:jobs.lever.co "AI Solutions" "Remote"
site:jobs.lever.co "legal AI" "engineer" "Remote"
site:jobs.lever.co "workflow automation" "AI Engineer"
site:jobs.lever.co "MCP" "RAG" "Remote"
```

## YC Work At A Startup

Use:

- `https://www.workatastartup.com/`
- `https://www.ycombinator.com/jobs`

Search/filter for:
- AI
- legal AI
- document automation
- applied AI
- founding AI engineer
- product engineer
- remote

Screen carefully for:
- onsite SF/NY/London requirements
- legal-credential expectations
- founding-role intensity
- senior production-AI expectations

## Hacker News Who Is Hiring

Use the current and previous month's "Who is hiring?" threads.

Search within thread for:

```text
AI engineer
applied AI
RAG
LLM
document
workflow
remote
legal
compliance
```

HN posts are useful because they often include founder-written context, salary ranges, process details, and direct email paths.

## Company Watchlist Check

For named companies or companies discovered repeatedly through sweeps, update `company_watchlist.md` rather than burying them in chat.

Good watchlist candidates:
- legal/document AI companies
- compliance/governance/privacy AI companies
- document/workflow automation companies
- healthcare/document workflow companies
- AI implementation consultancies with real engineering work

## Output Format

If writing an ATS sweep report, use:

```markdown
# ATS And Startup Sweep - YYYY-MM-DD

## Current Targets

## Stretch / Future Signals

## Dismiss / Noisy

## Companies To Add To Watchlist

## Resume / Market Language Notes
```

## Decision Rule

The ATS sweep is successful if it finds either:
- 2-5 credible roles worth deeper review, or
- useful market language that improves resume/search targeting.

It does not need to produce applications every time.

