# Journal - 2026-06-16: Knowledge Graph Pipeline and S2-A8 Contract Testing Article

## Session Summary

Two interlocking threads this session: completing the paper knowledge graph pipeline, and locking in the intellectual contribution of S2-A8.

---

## TDD for Agentic Systems — From Vague Claim to Defensible Thesis

The session opened with the question of whether TDD for agentic systems deserved its own article. The prior session had already been working toward this, but the framing was shaky. The original instinct ("constrained LLM node behaves like a pure function") was too strong — it ignores stochastic variation and doesn't survive scrutiny.

The refined claim is more defensible and more interesting:

> A tightly constrained LLM node (fixed system prompt, schema-bound output, narrow task scope) exposes a testable contract. The red-green loop is not oracle comparison of outputs; it is property-based assertion on schema conformance and business logic invariants.

This matters because:
- It explains why classical TDD fails for unconstrained agents (no oracle)
- It explains why TDD *can* work for constrained nodes (contract replaces oracle)
- It names the gap in the literature (LMQL shows constraints reduce variance; AgentAssay says ditch TDD; nobody connects them into a contract methodology)

The gap is S2-A8's original contribution.

### Literature Used

Papers already in the graph that directly support this:

| Paper | Role |
|-------|------|
| AgentAssay (2603.15676) | Rejects classical TDD; proposes statistical evals |
| LMQL — Prompting is Programming (2212.06094) | Constraints reduce output variance |
| Record & Replay LLM Agents (2505.17716) | Uses "check functions" — closest existing practice to contract assertions |
| Automated Self-Testing LLM Apps (2603.15676) | Additional practitioner evidence |
| SCOPE-V | Schema validation/constraint enforcement in agent outputs |
| PydanticAI TestModel/FunctionModel | Practitioner tools that enable zero-token contract testing |

The literature confirms the gap is real. Nobody has articulated the "constraint architecture restores TDD compatibility" connection cleanly.

---

## Article Changes

### S2-A1 (TDD for Nondeterministic Systems) — Refined

- Replaced "pure function" framing with "property-based contract assertions"
- Added literature context block naming the three-paper landscape
- Named the gap explicitly
- Scope boundary updated to reference S2-A8 for the contract testing methodology
- New sources added: AgentAssay, LMQL, Record & Replay, Automated Self-Testing

### S2-A8 (NEW) — Contract Testing Constrained LLM Nodes

New article plan at `articles/series-2/s2-a08-contract-testing-constrained-nodes.md`.

Thesis: a schema-bound LLM node with a fixed system prompt and narrow scope is a testable unit. The contract is the schema plus business logic invariants. Property assertions replace oracle comparison. The red-green loop survives — at contract level.

Key sections:
- Why classical TDD breaks (nondeterminism, no oracle)
- What a constrained node is (four requirements: fixed prompt, schema-bound output, narrow scope, typed inputs)
- The contract testing pattern (WindowSpec and MeasurementEstimate as worked examples)
- Three testing layers: constrained node → contract assertions; orchestration → invariant spec; system → statistical evals
- Economics: contract tests cost zero tokens via TestModel; statistical evals are periodic and expensive
- Honest framing: proposed framework, not a validated study

WindowConfigurator AI additions (voice-to-spec, vision measurement estimation) are the primary worked examples because they're the clearest concrete cases of constrained node design.

### Roadmap Dashboard Updated

- Added S2-A8 entry
- Updated S2-A1 thesis description
- write-now count: 16 → 17

---

## Knowledge Graph Pipeline — Completed

The full pipeline is now working end-to-end.

### What Was Built

| Script | Purpose |
|--------|---------|
| `scripts/fetch-citations.py` | Fetch Semantic Scholar metadata for 31 seed papers; outputs `citations.json` |
| `scripts/download-refs.py` | Download PDFs for 586 referenced papers |
| `scripts/ingest.py` | Docling PDF parsing → Kuzu graph (nodes: Paper, Section, Author, ArticlePlan; edges: CITES, HAS_SECTION, AUTHORED_BY, REFERENCES) |
| `scripts/query.py` | Query interface: search, explore, hot-refs, for-article, who-cites, citing |

### Current Graph State

- 31 seed papers: fully parsed by Docling HybridChunker
- 1194 ref papers: registered as metadata-only nodes (no section content yet)
- 1301 CITES edges
- 3748 Section nodes
- DB file: `articles/graph.kuzu` (single file on NTFS/WSL — expected Kuzu behaviour)

### Key Fixes Made This Session

1. **Kuzu "Database path cannot be a directory"** — `open_db` was calling `db_path.mkdir()` before `kuzu.Database()`, creating a directory that Kuzu then rejected. Fixed by changing to `db_path.parent.mkdir()`.

2. **Git recreating empty `graph.db` directory** — `.gitignore` had `articles/graph.db/` with trailing slash, causing git to track and recreate the directory. Fixed by renaming the DB to `graph.kuzu` and updating `.gitignore`.

3. **`unordered_map::at` Kuzu crash** — Corrupted partial database from a killed run. Fix: delete `articles/graph.kuzu` and `articles/graph.kuzu.wal` before rerunning.

4. **Ref parsing skipped** — 586 PDFs × ~45s Docling runtime ≈ 8 hours. Too long without human review of which refs are worth parsing. Added `--seeds-only` flag to `ingest.py`. Refs registered as metadata nodes only.

5. **Smoke test confusion** — `query.py search 'test driven development'` returned 0 results. The search is case-sensitive substring matching; real paper content uses "test-driven" with a hyphen. The graph is fine.

### API Key

Semantic Scholar API key is active and wired. Stored in `secrets/credentials.txt` under `SAMANTIC_SCHOLAR_API_KEY` (typo — 'A' not 'E'; the grep accounts for it). Run authenticated at 1 req/sec.

---

## Commits This Session

- `97991da` — article plan changes (S2-A1 refinement, S2-A8 new plan, roadmap dashboard)
- `fde5efb` — graph pipeline fixes (API key wiring, `--seeds-only`, Kuzu db path fix, `.gitignore`)

---

## Agent Instruction Files Updated

Added `## Knowledge Graph Pipeline` section to all three canonical agent instruction files:
- `AGENTS.md` (canonical)
- `CLAUDE.md` (mirror)
- `.github/copilot-instructions.md` (mirror)

Added compact pointer to `AGENT_BOOTSTRAP_COMPACT.md`.

Future agents starting cold will know the pipeline exists, how to run it, and the key gotchas.

---

## Open Threads

1. **Ref parsing (human-in-the-loop)** — 586 PDFs in `articles/refs/` need review. Running `ingest.py` without `--seeds-only` will parse them when approved. The hot-refs query (`query.py hot-refs`) is the right starting point for deciding which to prioritize.

2. **S2-A1 and S2-A8 writing** — Both article plans are locked. S2-A8 in particular has a strong original contribution. Ready to draft.

3. **`secrets/credentials.txt` typo** — `SAMANTIC_SCHOLAR_API_KEY` should be `SEMANTIC_SCHOLAR_API_KEY`. The grep workaround is in the agent docs. Fix when convenient; chip was spawned for this (task_453d6e44).

4. **Voice and Tone sections** — S3 and S4 article plans still missing these sections (S3-A1 through S3-A3, S4-A1, S4-A2, S4-A3, S4-A5).

5. **WindowConfigurator AI additions** — The voice-to-spec and vision measurement features are the primary worked examples for S2-A8. Implementation in `D:\Repos\renonerd\WindowConfigurator` is the next concrete build task before writing that article.

---

## Next Session Entry Points

For article writing:
- `articles/series-2/s2-a08-contract-testing-constrained-nodes.md` — ready to draft
- `articles/series-2/s2-a01-tdd-nondeterministic.md` — refined and ready

For graph queries:
```sh
# Most-cited refs across all seeds — good prioritization for ref parsing
SEMANTIC_SCHOLAR_API_KEY=$(grep SAMANTIC secrets/credentials.txt | cut -d= -f2) \
  python3 scripts/query.py hot-refs --min-seeds 3

# Papers supporting S2-A8
python3 scripts/query.py for-article S2-A8
```

For WindowConfigurator AI:
- Start in `D:\Repos\renonerd\WindowConfigurator`
- Goal: implement constrained PydanticAI nodes for voice-to-spec parsing and vision measurement estimation
- These become the concrete worked examples in S2-A8
