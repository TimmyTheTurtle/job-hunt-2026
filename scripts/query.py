"""
query.py — Query the paper graph.

Examples:
    # Full-text search across section content
    python scripts/query.py search "sequential hypothesis testing"

    # Which seed papers cite a ref paper by title keyword
    python scripts/query.py who-cites "agentassay"

    # All papers that support a specific article plan
    python scripts/query.py for-article S2-A2

    # Papers cited by multiple seeds (high-value refs)
    python scripts/query.py hot-refs [--min-seeds 3]

    # Everything citing a specific arXiv paper
    python scripts/query.py citing 2603.02601

    # Explore ref papers by topic keyword (title/abstract)
    python scripts/query.py explore "v-model verification"

Requires:
    pip install kuzu
"""

import argparse
import json
from pathlib import Path

try:
    import kuzu
except ImportError:
    raise SystemExit("ERROR: pip install kuzu")

REPO_ROOT  = Path(__file__).parent.parent
DEFAULT_DB = REPO_ROOT / "articles" / "graph.db"


def get_conn(db_path: Path) -> kuzu.Connection:
    if not db_path.exists():
        raise SystemExit(f"Graph DB not found at {db_path} — run ingest.py first")
    db = kuzu.Database(str(db_path))
    return kuzu.Connection(db)


def fmt_paper(row: dict) -> str:
    year  = f" ({row['year']})" if row.get("year") else ""
    tier  = f"[{row['tier']}]" if row.get("tier") else ""
    arxiv = f"  arXiv:{row['arxiv_id']}" if row.get("arxiv_id") else ""
    return f"{tier} {row.get('title','?')}{year}{arxiv}"


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_search(conn: kuzu.Connection, query: str, limit: int) -> None:
    """Full-text search across section text."""
    result = conn.execute(
        """
        MATCH (p:Paper)-[:HAS_SECTION]->(s:Section)
        WHERE s.text CONTAINS $q OR s.title CONTAINS $q
        RETURN p.title, p.tier, p.arxiv_id, p.year, s.title, s.text
        LIMIT $lim
        """,
        {"q": query, "lim": limit},
    )
    print(f"\nSearch: '{query}'\n")
    count = 0
    while result.has_next():
        row = result.get_next()
        paper_title, tier, arxiv_id, year, sec_title, text = row
        print(f"[{tier}] {paper_title} ({year or '?'})")
        if arxiv_id:
            print(f"  arXiv:{arxiv_id}")
        if sec_title:
            print(f"  § {sec_title}")
        snippet = text[:300].replace("\n", " ") if text else ""
        print(f"  {snippet}...")
        print()
        count += 1
    print(f"{count} results")


def cmd_who_cites(conn: kuzu.Connection, title_keyword: str) -> None:
    """Find which seed papers cite a paper matching a title keyword."""
    result = conn.execute(
        """
        MATCH (seed:Paper)-[:CITES]->(ref:Paper)
        WHERE ref.title CONTAINS $kw AND seed.tier = 'seed'
        RETURN seed.title, seed.arxiv_id, ref.title, ref.arxiv_id
        """,
        {"kw": title_keyword},
    )
    print(f"\nSeed papers that cite '{title_keyword}':\n")
    while result.has_next():
        seed_title, seed_arxiv, ref_title, ref_arxiv = result.get_next()
        print(f"  {seed_title}  (arXiv:{seed_arxiv})")
        print(f"    → cites: {ref_title}" + (f"  arXiv:{ref_arxiv}" if ref_arxiv else ""))
        print()


def cmd_for_article(conn: kuzu.Connection, plan_id: str) -> None:
    """List all papers (seeds and refs) that support an article plan."""
    result = conn.execute(
        """
        MATCH (ap:ArticlePlan {id: $plan})-[:REFERENCES]->(p:Paper)
        RETURN p.title, p.tier, p.arxiv_id, p.year, p.venue
        ORDER BY p.tier, p.year DESC
        """,
        {"plan": plan_id},
    )
    print(f"\nPapers for {plan_id}:\n")
    while result.has_next():
        title, tier, arxiv_id, year, venue = result.get_next()
        print(f"  [{tier}] {title} ({year or '?'}) — {venue or ''}")
        if arxiv_id:
            print(f"          arXiv:{arxiv_id}")
    print()

    # Also show refs cited by seeds that support this article
    result2 = conn.execute(
        """
        MATCH (ap:ArticlePlan {id: $plan})-[:REFERENCES]->(seed:Paper)-[:CITES]->(ref:Paper)
        WHERE ref.tier = 'ref'
        RETURN DISTINCT ref.title, ref.arxiv_id, ref.year, count(*) AS cited_by_n
        ORDER BY cited_by_n DESC
        LIMIT 20
        """,
        {"plan": plan_id},
    )
    print(f"Refs cited by seeds supporting {plan_id} (top 20 by frequency):\n")
    while result2.has_next():
        title, arxiv_id, year, n = result2.get_next()
        print(f"  (cited by {n} seeds) {title} ({year or '?'})" +
              (f"  arXiv:{arxiv_id}" if arxiv_id else ""))


def cmd_hot_refs(conn: kuzu.Connection, min_seeds: int) -> None:
    """Refs cited by multiple seed papers — high-value candidates to read."""
    result = conn.execute(
        """
        MATCH (seed:Paper {tier: 'seed'})-[:CITES]->(ref:Paper {tier: 'ref'})
        WITH ref, count(DISTINCT seed) AS n
        WHERE n >= $min
        RETURN ref.title, ref.arxiv_id, ref.doi, ref.year, ref.venue, n
        ORDER BY n DESC
        LIMIT 50
        """,
        {"min": min_seeds},
    )
    print(f"\nRefs cited by ≥{min_seeds} seed papers:\n")
    while result.has_next():
        title, arxiv_id, doi, year, venue, n = result.get_next()
        print(f"  [{n} seeds] {title} ({year or '?'})")
        if arxiv_id:
            print(f"    arXiv:{arxiv_id}")
        elif doi:
            print(f"    doi:{doi}")
        print()


def cmd_citing(conn: kuzu.Connection, arxiv_id: str) -> None:
    """Find all papers in the graph that cite a given arXiv paper."""
    result = conn.execute(
        """
        MATCH (a:Paper)-[:CITES]->(b:Paper {arxiv_id: $id})
        RETURN a.title, a.tier, a.arxiv_id, a.year
        ORDER BY a.tier, a.year DESC
        """,
        {"id": arxiv_id},
    )
    print(f"\nPapers citing arXiv:{arxiv_id}:\n")
    while result.has_next():
        title, tier, aid, year = result.get_next()
        print(f"  [{tier}] {title} ({year or '?'})" + (f"  arXiv:{aid}" if aid else ""))


def cmd_explore(conn: kuzu.Connection, keyword: str, limit: int) -> None:
    """Search ref papers by title/abstract keyword."""
    result = conn.execute(
        """
        MATCH (p:Paper)
        WHERE (p.title CONTAINS $kw OR p.abstract CONTAINS $kw)
          AND p.tier = 'ref'
        RETURN p.title, p.arxiv_id, p.doi, p.year, p.venue
        ORDER BY p.year DESC
        LIMIT $lim
        """,
        {"kw": keyword, "lim": limit},
    )
    print(f"\nRef papers matching '{keyword}':\n")
    while result.has_next():
        title, arxiv_id, doi, year, venue = result.get_next()
        print(f"  {title} ({year or '?'}) — {venue or ''}")
        if arxiv_id:
            print(f"    arXiv:{arxiv_id}")
        elif doi:
            print(f"    doi:{doi}")
        print()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Query the paper graph.")
    parser.add_argument("--db", default=str(DEFAULT_DB), help="Kuzu DB directory")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_search = sub.add_parser("search", help="Full-text search across section content")
    p_search.add_argument("query")
    p_search.add_argument("--limit", type=int, default=10)

    p_who = sub.add_parser("who-cites", help="Which seeds cite a paper (by title keyword)")
    p_who.add_argument("title_keyword")

    p_art = sub.add_parser("for-article", help="Papers supporting an article plan")
    p_art.add_argument("plan_id", help="e.g. S2-A2")

    p_hot = sub.add_parser("hot-refs", help="Refs cited by multiple seeds")
    p_hot.add_argument("--min-seeds", type=int, default=2)

    p_cit = sub.add_parser("citing", help="Papers citing a given arXiv ID")
    p_cit.add_argument("arxiv_id")

    p_exp = sub.add_parser("explore", help="Explore refs by title/abstract keyword")
    p_exp.add_argument("keyword")
    p_exp.add_argument("--limit", type=int, default=20)

    args   = parser.parse_args()
    db_path = Path(args.db)
    conn   = get_conn(db_path)

    if args.cmd == "search":
        cmd_search(conn, args.query, args.limit)
    elif args.cmd == "who-cites":
        cmd_who_cites(conn, args.title_keyword)
    elif args.cmd == "for-article":
        cmd_for_article(conn, args.plan_id)
    elif args.cmd == "hot-refs":
        cmd_hot_refs(conn, args.min_seeds)
    elif args.cmd == "citing":
        cmd_citing(conn, args.arxiv_id)
    elif args.cmd == "explore":
        cmd_explore(conn, args.keyword, args.limit)


if __name__ == "__main__":
    main()
