"""
fetch-citations.py — Query Semantic Scholar for citations of each seed paper.

Reads the seed arXiv IDs from a hardcoded manifest (matching download-papers.ps1),
calls the Semantic Scholar API, and writes articles/papers/citations.json.

Safe to re-run — cached responses are reused unless --force is passed.

Usage:
    python scripts/fetch-citations.py [--force] [--cache-dir .cache/s2]

Output:
    articles/papers/citations.json   — full manifest (seeds + refs)
    .cache/s2/<arxiv_id>.json        — raw S2 API responses (for reruns)

Requires:
    pip install requests
"""

import argparse
import json
import time
from pathlib import Path

try:
    import requests
except ImportError:
    raise SystemExit("ERROR: pip install requests")

# ---------------------------------------------------------------------------
# Seed manifest — arXiv IDs and which article plans they support
# ---------------------------------------------------------------------------

SEEDS: list[dict] = [
    # Series 1
    {"arxiv_id": "2507.09089", "file": "arxiv-2507.09089-metr-productivity-rct.pdf",                "articles": ["S1-A1", "S1-A3"]},
    {"arxiv_id": "2604.13277", "file": "arxiv-2604.13277-comprehension-debt.pdf",                   "articles": ["S1-A1", "S1-A2", "S1-A3"]},
    {"arxiv_id": "2603.28592", "file": "arxiv-2603.28592-debt-behind-ai-boom.pdf",                  "articles": ["S1-A1", "S1-A2"]},
    {"arxiv_id": "2512.11922", "file": "arxiv-2512.11922-vibe-coding-in-practice.pdf",              "articles": ["S1-A1"]},
    {"arxiv_id": "2604.00436", "file": "arxiv-2604.00436-programming-by-chat.pdf",                  "articles": ["S1-A1", "S1-A2"]},
    {"arxiv_id": "2601.02410", "file": "arxiv-2601.02410-vibe-check-protocol.pdf",                  "articles": ["S1-A1", "S1-A3"]},
    {"arxiv_id": "2604.18538", "file": "arxiv-2604.18538-fast-and-forgettable.pdf",                 "articles": ["S1-A3"]},
    {"arxiv_id": "2602.20206", "file": "arxiv-2602.20206-mitigating-epistemic-debt.pdf",            "articles": ["S1-A3"]},
    {"arxiv_id": "2601.20112", "file": "arxiv-2601.20112-enterprise-ai-coding-assistants.pdf",      "articles": ["S1-A3"]},
    {"arxiv_id": "2606.05391", "file": "arxiv-2606.05391-human-oversight-agentic-systems.pdf",      "articles": ["S1-A3"]},
    {"arxiv_id": "2511.06428", "file": "arxiv-2511.06428-walking-the-tightrope.pdf",                "articles": ["S1-A3"]},
    {"arxiv_id": "2507.03156", "file": "arxiv-2507.03156-llm-assistant-developer-productivity.pdf", "articles": ["S1-A3"]},
    {"arxiv_id": "2503.14281", "file": "arxiv-2503.14281-xoxo-context-poisoning.pdf",               "articles": ["S1-A6"]},
    {"arxiv_id": "2404.17723", "file": "arxiv-2404.17723-rag-knowledge-graphs.pdf",                 "articles": ["S1-A8"]},
    # Series 2
    {"arxiv_id": "2602.20684", "file": "arxiv-2602.20684-agile-v-koch-wellbrock.pdf",               "articles": ["S2-A2", "S1-A10"]},
    {"arxiv_id": "2605.20456", "file": "arxiv-2605.20456-agentic-agile-v-scope-v.pdf",              "articles": ["S2-A2"]},
    {"arxiv_id": "2512.12791", "file": "arxiv-2512.12791-beyond-task-completion.pdf",               "articles": ["S2-A2", "S2-A5"]},
    {"arxiv_id": "2603.02601", "file": "arxiv-2603.02601-agentassay.pdf",                           "articles": ["S2-A2", "S2-A5"]},
    {"arxiv_id": "2308.05381", "file": "arxiv-2308.05381-v-model-ml-software.pdf",                  "articles": ["S2-A2"]},
    {"arxiv_id": "2411.09050", "file": "arxiv-2411.09050-systems-engineering-llms.pdf",             "articles": ["S2-A2"]},
    {"arxiv_id": "2605.17675", "file": "arxiv-2605.17675-transparency-traceability-v-model.pdf",    "articles": ["S2-A2"]},
    {"arxiv_id": "2412.05579", "file": "arxiv-2412.05579-llms-as-judges-survey.pdf",                "articles": ["S2-A1"]},
    {"arxiv_id": "2509.06216", "file": "arxiv-2509.06216-agentic-se-foundational-pillars.pdf",      "articles": ["S2-A3"]},
    {"arxiv_id": "2603.15676", "file": "arxiv-2603.15676-automated-self-testing-quality-gate.pdf",  "articles": ["S2-A4"]},
    {"arxiv_id": "2604.26275", "file": "arxiv-2604.26275-agentic-ai-sdlc.pdf",                      "articles": ["S2-A4"]},
    # Series 4
    {"arxiv_id": "2510.26309", "file": "arxiv-2510.26309-graphcompliance.pdf",                      "articles": ["S4-A5", "S4-A6"]},
    {"arxiv_id": "2110.11984", "file": "arxiv-2110.11984-coupette-law-smells.pdf",                  "articles": ["S4-A1", "S4-A3", "S4-A4", "S4-A5", "S4-A7"]},
    {"arxiv_id": "2206.14879", "file": "arxiv-2206.14879-grimmelmann-programming-languages-law.pdf","articles": ["S4-A1", "S4-A3", "S4-A5"]},
    {"arxiv_id": "2401.01301", "file": "arxiv-2401.01301-dahl-large-legal-fictions.pdf",            "articles": ["S4-A5", "S4-A6"]},
]

S2_BASE = "https://api.semanticscholar.org/graph/v1"
S2_FIELDS = "title,authors,year,externalIds,openAccessPdf,venue,abstract"
DELAY = 3.0  # seconds between API calls — S2 free tier: ~100 req/5 min without key


def s2_id_from_arxiv(arxiv_id: str) -> str:
    return f"ARXIV:{arxiv_id}"


def _get_with_retry(session: requests.Session, url: str, params: dict, timeout: int) -> requests.Response:
    """GET with exponential backoff on 429. Retries indefinitely up to ~10 min total wait."""
    backoff = 15
    for attempt in range(10):
        resp = session.get(url, params=params, timeout=timeout)
        if resp.status_code == 429:
            wait = min(backoff * (2 ** attempt), 300)  # cap at 5 min
            print(f"\n  429 rate-limited — waiting {wait}s ...", end=" ", flush=True)
            time.sleep(wait)
            continue
        return resp
    # Last attempt
    resp = session.get(url, params=params, timeout=timeout)
    resp.raise_for_status()
    return resp


def fetch_paper(s2_id: str, session: requests.Session, cache_dir: Path, force: bool) -> dict | None:
    cache_file = cache_dir / f"{s2_id.replace(':', '_')}.json"
    if not force and cache_file.exists():
        return json.loads(cache_file.read_text())

    url = f"{S2_BASE}/paper/{s2_id}"
    params = {"fields": S2_FIELDS}
    resp = _get_with_retry(session, url, params, timeout=15)
    if resp.status_code == 404:
        return None
    resp.raise_for_status()
    data = resp.json()
    cache_file.write_text(json.dumps(data, indent=2))
    time.sleep(DELAY)
    return data


def fetch_references(s2_id: str, session: requests.Session, cache_dir: Path, force: bool) -> list[dict]:
    cache_file = cache_dir / f"{s2_id.replace(':', '_')}_refs.json"
    if not force and cache_file.exists():
        return json.loads(cache_file.read_text())

    url = f"{S2_BASE}/paper/{s2_id}/references"
    params = {"fields": S2_FIELDS, "limit": 500}
    resp = _get_with_retry(session, url, params, timeout=30)
    if resp.status_code == 404:
        return []
    resp.raise_for_status()
    refs = resp.json().get("data", [])
    # unwrap — each entry is {"citedPaper": {...}, "contexts": [...]}
    papers = [r["citedPaper"] for r in refs if r.get("citedPaper")]
    cache_file.write_text(json.dumps(papers, indent=2))
    time.sleep(DELAY)
    return papers


def resolve_download_url(paper: dict) -> str | None:
    """Return the best available open-access PDF URL, or None."""
    oa = paper.get("openAccessPdf") or {}
    if oa.get("url"):
        return oa["url"]
    arxiv = (paper.get("externalIds") or {}).get("ArXiv")
    if arxiv:
        return f"https://arxiv.org/pdf/{arxiv}"
    return None


def paper_to_node(paper: dict, tier: str, cited_by: list[str] | None = None) -> dict:
    ids = paper.get("externalIds") or {}
    return {
        "tier": tier,
        "s2_id": paper.get("paperId", ""),
        "arxiv_id": ids.get("ArXiv"),
        "doi": ids.get("DOI"),
        "title": paper.get("title", ""),
        "authors": [a.get("name", "") for a in (paper.get("authors") or [])],
        "year": paper.get("year"),
        "venue": paper.get("venue", ""),
        "abstract": paper.get("abstract", ""),
        "download_url": resolve_download_url(paper),
        "cited_by_seeds": cited_by or [],  # list of seed arXiv IDs that cite this
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch citations for seed papers from Semantic Scholar.")
    parser.add_argument("--force",     action="store_true", help="Ignore cached API responses")
    parser.add_argument("--cache-dir", default=".cache/s2",  help="Directory for cached S2 responses")
    args = parser.parse_args()

    repo_root  = Path(__file__).parent.parent
    cache_dir  = repo_root / args.cache_dir
    out_file   = repo_root / "articles" / "papers" / "citations.json"
    cache_dir.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers["User-Agent"] = "job-hunt-2026-research/1.0 (personal research corpus)"

    seed_nodes: list[dict] = []
    ref_nodes:  dict[str, dict] = {}  # s2_id → node (deduped)
    edges:      list[dict] = []       # {from_arxiv, to_s2_id}

    for seed in SEEDS:
        arxiv_id = seed["arxiv_id"]
        s2_id    = s2_id_from_arxiv(arxiv_id)
        print(f"  seed  {arxiv_id} ...", end=" ", flush=True)

        paper = fetch_paper(s2_id, session, cache_dir, args.force)
        if paper is None:
            print("NOT FOUND on S2")
            seed_nodes.append({
                "tier": "seed",
                "arxiv_id": arxiv_id,
                "file": seed["file"],
                "articles": seed["articles"],
                "s2_id": None,
                "title": f"(S2 not found) {arxiv_id}",
                "authors": [], "year": None, "venue": "",
                "abstract": "", "download_url": f"https://arxiv.org/pdf/{arxiv_id}",
                "cited_by_seeds": [],
            })
            continue

        node = paper_to_node(paper, "seed")
        node["file"]     = seed["file"]
        node["articles"] = seed["articles"]
        seed_nodes.append(node)
        print(f"ok — '{paper.get('title', '')[:60]}'")

        refs = fetch_references(s2_id, session, cache_dir, args.force)
        print(f"         {len(refs)} references found")

        for ref in refs:
            if not ref.get("paperId"):
                continue
            ref_s2_id = ref["paperId"]
            edges.append({"from_arxiv": arxiv_id, "to_s2_id": ref_s2_id})

            if ref_s2_id not in ref_nodes:
                ref_nodes[ref_s2_id] = paper_to_node(ref, "ref", cited_by=[arxiv_id])
            else:
                # already seen — add this seed to cited_by
                if arxiv_id not in ref_nodes[ref_s2_id]["cited_by_seeds"]:
                    ref_nodes[ref_s2_id]["cited_by_seeds"].append(arxiv_id)

    # Promote any ref that is also a seed to tier=seed
    seed_arxiv_ids = {s["arxiv_id"] for s in SEEDS}
    for node in ref_nodes.values():
        if node.get("arxiv_id") in seed_arxiv_ids:
            node["tier"] = "seed"

    manifest = {
        "generated": __import__("datetime").datetime.utcnow().isoformat() + "Z",
        "seed_count": len(seed_nodes),
        "ref_count":  len(ref_nodes),
        "edge_count": len(edges),
        "seeds": seed_nodes,
        "refs":  list(ref_nodes.values()),
        "edges": edges,
    }

    out_file.write_text(json.dumps(manifest, indent=2))
    print(f"\nManifest written → {out_file}")
    print(f"  Seeds : {len(seed_nodes)}")
    print(f"  Refs  : {len(ref_nodes)}")
    print(f"  Edges : {len(edges)}")

    # Summary: how many refs are downloadable
    downloadable = sum(1 for n in ref_nodes.values() if n.get("download_url"))
    print(f"  Refs with download URL : {downloadable} / {len(ref_nodes)}")


if __name__ == "__main__":
    main()
