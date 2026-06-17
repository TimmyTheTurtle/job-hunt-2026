# Knowledge Graph Pipeline — Architecture

## Purpose

A research pipeline that builds a queryable citation graph from academic papers supporting the article series in `articles/series-*/`. The graph connects article plans to seed papers, seed papers to their cited references, and exposes full-text search over parsed paper content.

The intended use is article research: finding which papers support a claim, discovering high-value references worth reading, and performing keyword search across section-level content.

---

## System Overview

```
Semantic Scholar API
        │
        ▼
fetch-citations.py  ──►  citations.json  ──►  download-refs.py  ──►  articles/refs/*.pdf
        │                                                                      │
        │                   articles/papers/*.pdf (seeds, manual)              │
        │                             │                                        │
        └──────────────────────►  ingest.py  ◄───────────────────────────────┘
                                      │
                                      ▼
                               articles/graph.kuzu  (Kuzu embedded graph DB)
                                      │
                                      ▼
                                  query.py
                                      │
                          ┌───────────┼───────────┐
                        search    hot-refs    for-article  …
```

---

## Components

### `scripts/fetch-citations.py`

**Role:** fetch metadata from Semantic Scholar and build the citation manifest.

**Inputs:**
- Hardcoded `SEEDS` list in the script (31 arXiv IDs mapped to article plans)
- `SEMANTIC_SCHOLAR_API_KEY` env var (optional, enables 1 req/sec vs 3+ sec without)

**Outputs:**
- `articles/papers/citations.json` — full manifest: seeds, refs, edges
- `.cache/s2/<arxiv_id>.json` — raw API response cache (gitignored)

**Behaviour:**
- For each seed, calls `/paper/{ARXIV:id}` and `/paper/{ARXIV:id}/references`
- Deduplicates refs across seeds; tracks `cited_by_seeds` per ref
- Caches raw responses; re-run is safe without `--force`
- Handles 429 rate limits with exponential backoff (15s → 300s cap)
- Resolves best open-access PDF URL per paper (openAccessPdf field → arXiv fallback)

**Idempotency:** safe to re-run; uses cache unless `--force`.

---

### `scripts/download-refs.py`

**Role:** download PDF files for all ref nodes that have a resolvable open-access URL.

**Inputs:**
- `articles/papers/citations.json` (written by fetch-citations.py)

**Outputs:**
- `articles/refs/*.pdf` — downloaded PDFs (gitignored)
- `articles/refs/not-downloadable.json` — log of refs with no accessible PDF
- Updates `citations.json` in-place: adds `local_file` field to each ref node that was downloaded

**Behaviour:**
- Skips files that already exist (idempotent)
- Validates `content-type` header to reject HTML landing pages
- `--limit N` caps downloads per run
- `--dry-run` prints what would be downloaded

**Why `local_file` is written back to citations.json:** `ingest.py` reads this field to know where each ref's PDF lives. The two scripts must be run in order.

**Idempotency:** safe to re-run; skips existing files.

---

### `scripts/ingest.py`

**Role:** parse PDFs with Docling and write nodes and edges into the Kuzu graph database.

**Inputs:**
- `articles/papers/citations.json` (manifest with `local_file` fields populated)
- `articles/papers/*.pdf` (seed PDFs)
- `articles/refs/*.pdf` (ref PDFs, only if not `--seeds-only`)

**Outputs:**
- `articles/graph.kuzu` — Kuzu database (single file on NTFS/WSL; gitignored)

**Key flags:**
- `--seeds-only` — parse seed PDFs with Docling; register refs as metadata-only nodes (no section content). Use this until ref parsing has been explicitly approved.
- `--no-parse` — skip Docling entirely; only update graph structure and edges
- `--force` — re-parse and re-ingest everything (ignores already-ingested check)
- `--db <path>` — override default DB path

**Ingest phases (in order):**

1. **Seeds** — for each seed: upsert Paper node, upsert Authors, link AUTHORED_BY edges, upsert ArticlePlan nodes, link REFERENCES edges, parse PDF with Docling HybridChunker, insert Section nodes, link HAS_SECTION edges.

2. **Refs** — for each ref: upsert Paper node, upsert Authors, link AUTHORED_BY edges. If `--seeds-only` is NOT set and PDF exists: parse PDF and insert Sections.

3. **Citation edges** — for each edge in the manifest: MATCH from/to Paper nodes, MERGE CITES edge.

**Docling parsing:** uses `DocumentConverter` + `HybridChunker`. Each chunk becomes a Section node with `title` (last heading in the chunk's heading stack), `level` (depth of heading stack), `text` (chunk content), and `page` (best-effort from provenance metadata).

**Idempotency:** upserts via Kuzu `MERGE` semantics. Re-running without `--force` skips already-ingested papers (those with a non-empty `local_path` in the graph).

**Crash recovery:** if ingest crashes mid-run (Kuzu raises `unordered_map::at`), the database is corrupted. Delete `articles/graph.kuzu` and `articles/graph.kuzu.wal` before rerunning.

---

### `scripts/query.py`

**Role:** query interface over the graph database.

**Commands:**

| Command | Description |
|---------|-------------|
| `search <query>` | Case-sensitive substring match over `Section.text` and `Section.title`. Returns paper + section + snippet. Use hyphens: `"test-driven"` not `"test driven"`. |
| `explore <keyword>` | Keyword search over `Paper.title` and `Paper.abstract` for `tier=ref` papers. Good for discovering refs without their full text parsed. |
| `hot-refs [--min-seeds N]` | Refs cited by ≥N seed papers (default 2). Ranked by citation count. Best starting point for deciding which refs to parse. |
| `for-article <plan_id>` | Papers directly linked to an article plan (via REFERENCES edges) plus refs transitively cited by those seeds. |
| `who-cites <title_keyword>` | Which seed papers cite a paper matching a title keyword. |
| `citing <arxiv_id>` | Papers in the graph that cite a specific arXiv paper. |

---

## Graph Schema

### Node tables

| Table | Primary Key | Key fields |
|-------|-------------|------------|
| `Paper` | `id` | `tier` (seed/ref), `arxiv_id`, `s2_id`, `doi`, `title`, `year`, `venue`, `abstract`, `local_path`, `articles` |
| `Section` | `id` | `paper_id`, `title`, `level`, `text`, `page` |
| `Author` | `name` | — |
| `ArticlePlan` | `id` | — (e.g. `"S2-A8"`) |

**Paper.id** format:
- `arxiv:<id>` if arXiv ID is known
- `s2:<paperId>` if only S2 ID is known
- `title:<sha256[:16]>` as fallback

**Section.id** format: `<paper_id>:sec:<chunk_index>`

**Paper.articles** is stored as a JSON-encoded list of article plan IDs (e.g. `'["S2-A1", "S2-A8"]'`). This is a denormalized field; the canonical link is the REFERENCES edge.

### Edge tables

| Edge | From → To | Populated by |
|------|-----------|-------------|
| `CITES` | Paper → Paper | ingest.py phase 3 |
| `HAS_SECTION` | Paper → Section | ingest.py phase 1/2 |
| `AUTHORED_BY` | Paper → Author | ingest.py phases 1/2 |
| `REFERENCES` | ArticlePlan → Paper | ingest.py phase 1 |

---

## File Layout

```
articles/
  papers/
    citations.json          ← generated manifest (gitignored)
    *.pdf                   ← seed PDFs (gitignored)
  refs/
    *.pdf                   ← ref PDFs (gitignored)
    not-downloadable.json   ← log of refs with no accessible PDF
  graph.kuzu                ← Kuzu DB (single file on NTFS/WSL; gitignored)
  graph.kuzu.wal            ← Kuzu WAL file (gitignored; delete if DB is corrupted)
  series-1/                 ← article plans for Series 1
  series-2/                 ← article plans for Series 2
  …

.cache/
  s2/
    *.json                  ← raw Semantic Scholar API response cache (gitignored)

scripts/
  fetch-citations.py
  download-refs.py
  ingest.py
  query.py

secrets/
  credentials.txt           ← API keys (gitignored; NEVER commit)
```

---

## Data Flow

```
1. fetch-citations.py
   SEEDS (hardcoded) → S2 API → citations.json
   articles: seed arXiv IDs, article plan mappings
   refs: S2 metadata for all first-level references
   edges: (from_arxiv, to_s2_id) pairs

2. download-refs.py
   citations.json → HTTP download → articles/refs/*.pdf
   updates citations.json in-place: adds local_file field per ref

3. ingest.py --seeds-only
   citations.json + articles/papers/*.pdf → Kuzu
   seeds: full parse (Docling → Section nodes)
   refs: metadata-only nodes (no Section content yet)
   edges: CITES, HAS_SECTION, AUTHORED_BY, REFERENCES

4. query.py
   Kuzu → stdout
```

---

## Dependencies

```
pip install kuzu docling requests
```

| Package | Role |
|---------|------|
| `requests` | Semantic Scholar API calls and PDF downloads |
| `docling` | PDF parsing (`DocumentConverter`, `HybridChunker`) |
| `kuzu` | Embedded graph database; Cypher query language |

Python 3.12+ required (uses `str | None` union syntax).

---

## Environment

| Variable | Required | Description |
|----------|----------|-------------|
| `SEMANTIC_SCHOLAR_API_KEY` | Recommended | Enables 1 req/sec vs 3+ sec unauthenticated. Stored in `secrets/credentials.txt` under key `SAMANTIC_SCHOLAR_API_KEY` (note typo). |

Retrieve inline:
```sh
SEMANTIC_SCHOLAR_API_KEY=$(grep SAMANTIC secrets/credentials.txt | cut -d= -f2) \
  python3 scripts/fetch-citations.py
```

---

## Kuzu on Windows/WSL (NTFS)

When Kuzu opens a database path on an NTFS mount via WSL, it creates a **single file** at the path rather than a directory. This is expected behaviour on NTFS — the internal page file lives inside the single file rather than as a directory of files.

**Do not** call `mkdir` on the database path before opening it. `ingest.py` calls `db_path.parent.mkdir()` (creates the containing directory only). If the database path itself is pre-created as a directory, Kuzu raises:

```
Database path cannot be a directory
```

---

## Seed Management

The `SEEDS` list in `fetch-citations.py` is the single source of truth for which papers are in the corpus. To add a new seed:

1. Add an entry to `SEEDS` with `arxiv_id`, `file`, and `articles` fields.
2. Download the PDF manually to `articles/papers/` with the matching filename.
3. Re-run `fetch-citations.py` (cache means only the new seed makes API calls).
4. Re-run `ingest.py --seeds-only` (MERGE semantics mean existing nodes are updated, not duplicated).

---

## Current Corpus State (as of 2026-06-16)

| Metric | Count |
|--------|-------|
| Seed papers | 31 |
| Ref papers (metadata only) | 1,194 |
| CITES edges | 1,301 |
| Section nodes (seeds only) | 3,748 |
| Article plans tracked | varies by series |

Refs are registered as metadata-only nodes. Ref PDFs exist in `articles/refs/` but have not been parsed with Docling — parsing 586 PDFs takes ~8 hours and requires human review of which refs are worth the cost. Run `query.py hot-refs` to prioritize.

---

## Future Work: On-Demand Ref Parsing

Currently, refs are either all parsed or all skipped. The right model is on-demand: parse a ref when it has earned it — cited by multiple seeds, surfaced by a query, or needed for a specific article draft.

Desired behaviour: given a paper ID or arXiv ID, parse just that paper and integrate its sections into the graph without a full re-ingest.

This would probably look like:
- `ingest.py --paper <arxiv_id>` — parse a single ref PDF and upsert its sections
- or a small `parse-paper.py` script that takes a path or arXiv ID and integrates it

`query.py hot-refs` is already the right tool for identifying candidates. The missing piece is the targeted ingest path.
