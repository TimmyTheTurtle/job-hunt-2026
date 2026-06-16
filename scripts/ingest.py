"""
ingest.py — Parse papers with Docling and load the graph into Kuzu.

Graph schema:

  Nodes:
    Paper     (id, tier, arxiv_id, doi, s2_id, title, year, venue, abstract,
               local_path, articles)
    Section   (id, paper_id, title, level, text, page)
    Author    (name)
    ArticlePlan (id)           — e.g. "S1-A2"

  Edges:
    (:Paper)-[:CITES]->(:Paper)
    (:Paper)-[:HAS_SECTION]->(:Section)
    (:Paper)-[:AUTHORED_BY]->(:Author)
    (:ArticlePlan)-[:REFERENCES]->(:Paper)

Usage:
    python scripts/ingest.py [--db articles/graph.db] [--force] [--no-parse]

    --force      Re-parse and re-ingest everything (default: skip already-ingested papers)
    --no-parse   Skip Docling parsing; only update graph metadata and edges

Requires:
    pip install kuzu docling requests
    Run fetch-citations.py (and optionally download-refs.py) first.
"""

import argparse
import hashlib
import json
from pathlib import Path

try:
    import kuzu
except ImportError:
    raise SystemExit("ERROR: pip install kuzu")

try:
    from docling.document_converter import DocumentConverter
    from docling.chunking import HybridChunker
except ImportError:
    raise SystemExit("ERROR: pip install docling")

REPO_ROOT   = Path(__file__).parent.parent
PAPERS_DIR  = REPO_ROOT / "articles" / "papers"
REFS_DIR    = REPO_ROOT / "articles" / "refs"
CITATIONS   = PAPERS_DIR / "citations.json"
DEFAULT_DB  = REPO_ROOT / "articles" / "graph.db"


# ---------------------------------------------------------------------------
# Schema
# ---------------------------------------------------------------------------

SCHEMA = """
CREATE NODE TABLE IF NOT EXISTS Paper(
    id        STRING,
    tier      STRING,
    arxiv_id  STRING,
    doi       STRING,
    s2_id     STRING,
    title     STRING,
    year      INT64,
    venue     STRING,
    abstract  STRING,
    local_path STRING,
    articles  STRING,
    PRIMARY KEY (id)
);

CREATE NODE TABLE IF NOT EXISTS Section(
    id        STRING,
    paper_id  STRING,
    title     STRING,
    level     INT64,
    text      STRING,
    page      INT64,
    PRIMARY KEY (id)
);

CREATE NODE TABLE IF NOT EXISTS Author(
    name STRING,
    PRIMARY KEY (name)
);

CREATE NODE TABLE IF NOT EXISTS ArticlePlan(
    id STRING,
    PRIMARY KEY (id)
);

CREATE REL TABLE IF NOT EXISTS CITES(FROM Paper TO Paper);
CREATE REL TABLE IF NOT EXISTS HAS_SECTION(FROM Paper TO Section);
CREATE REL TABLE IF NOT EXISTS AUTHORED_BY(FROM Paper TO Author);
CREATE REL TABLE IF NOT EXISTS REFERENCES(FROM ArticlePlan TO Paper);
"""


def open_db(db_path: Path) -> kuzu.Database:
    db_path.mkdir(parents=True, exist_ok=True)
    db = kuzu.Database(str(db_path))
    conn = kuzu.Connection(db)
    for stmt in SCHEMA.strip().split(";"):
        stmt = stmt.strip()
        if stmt:
            conn.execute(stmt + ";")
    return db


def paper_id(arxiv_id: str | None, s2_id: str | None, title: str) -> str:
    """Stable unique ID for a paper node."""
    if arxiv_id:
        return f"arxiv:{arxiv_id}"
    if s2_id:
        return f"s2:{s2_id}"
    return "title:" + hashlib.sha256(title.encode()).hexdigest()[:16]


def section_id(pid: str, idx: int) -> str:
    return f"{pid}:sec:{idx}"


# ---------------------------------------------------------------------------
# Graph helpers
# ---------------------------------------------------------------------------

def upsert_paper(conn: kuzu.Connection, node: dict, local_path: str | None) -> str:
    pid = paper_id(node.get("arxiv_id"), node.get("s2_id"), node.get("title", ""))

    conn.execute(
        """
        MERGE (p:Paper {id: $id})
        ON CREATE SET
            p.tier       = $tier,
            p.arxiv_id   = $arxiv_id,
            p.doi        = $doi,
            p.s2_id      = $s2_id,
            p.title      = $title,
            p.year       = $year,
            p.venue      = $venue,
            p.abstract   = $abstract,
            p.local_path = $local_path,
            p.articles   = $articles
        ON MATCH SET
            p.tier       = $tier,
            p.local_path = $local_path,
            p.articles   = $articles
        """,
        {
            "id":         pid,
            "tier":       node.get("tier", "ref"),
            "arxiv_id":   node.get("arxiv_id") or "",
            "doi":        node.get("doi") or "",
            "s2_id":      node.get("s2_id") or "",
            "title":      node.get("title") or "",
            "year":       node.get("year") or 0,
            "venue":      node.get("venue") or "",
            "abstract":   node.get("abstract") or "",
            "local_path": local_path or "",
            "articles":   json.dumps(node.get("articles") or []),
        },
    )
    return pid


def upsert_author(conn: kuzu.Connection, name: str) -> None:
    conn.execute("MERGE (:Author {name: $name})", {"name": name})


def upsert_article_plan(conn: kuzu.Connection, plan_id: str) -> None:
    conn.execute("MERGE (:ArticlePlan {id: $id})", {"id": plan_id})


def link_cites(conn: kuzu.Connection, from_pid: str, to_pid: str) -> None:
    conn.execute(
        """
        MATCH (a:Paper {id: $a}), (b:Paper {id: $b})
        MERGE (a)-[:CITES]->(b)
        """,
        {"a": from_pid, "b": to_pid},
    )


def link_authored_by(conn: kuzu.Connection, paper_pid: str, author: str) -> None:
    conn.execute(
        """
        MATCH (p:Paper {id: $pid}), (a:Author {name: $name})
        MERGE (p)-[:AUTHORED_BY]->(a)
        """,
        {"pid": paper_pid, "name": author},
    )


def link_references(conn: kuzu.Connection, plan_id: str, paper_pid: str) -> None:
    conn.execute(
        """
        MATCH (ap:ArticlePlan {id: $plan}), (p:Paper {id: $pid})
        MERGE (ap)-[:REFERENCES]->(p)
        """,
        {"plan": plan_id, "pid": paper_pid},
    )


def insert_section(conn: kuzu.Connection, paper_pid: str, sec_id: str,
                   title: str, level: int, text: str, page: int) -> None:
    conn.execute(
        """
        MERGE (s:Section {id: $id})
        ON CREATE SET
            s.paper_id = $paper_id,
            s.title    = $title,
            s.level    = $level,
            s.text     = $text,
            s.page     = $page
        """,
        {"id": sec_id, "paper_id": paper_pid, "title": title,
         "level": level, "text": text, "page": page},
    )
    conn.execute(
        """
        MATCH (p:Paper {id: $pid}), (s:Section {id: $sid})
        MERGE (p)-[:HAS_SECTION]->(s)
        """,
        {"pid": paper_pid, "sid": sec_id},
    )


# ---------------------------------------------------------------------------
# Docling parsing
# ---------------------------------------------------------------------------

def parse_paper(pdf_path: Path, paper_pid: str, conn: kuzu.Connection) -> int:
    """Parse a PDF with Docling and insert its sections into the graph."""
    converter = DocumentConverter()
    chunker   = HybridChunker()

    result = converter.convert(str(pdf_path))
    doc    = result.document
    chunks = list(chunker.chunk(doc))

    for idx, chunk in enumerate(chunks):
        meta  = chunk.meta if hasattr(chunk, "meta") else {}
        title = ""
        level = 0
        page  = 0

        # Extract heading context from chunk metadata
        headings = getattr(meta, "headings", None) or []
        if headings:
            title = headings[-1]
            level = len(headings)

        # Page number (best-effort)
        if hasattr(meta, "doc_items"):
            for item in meta.doc_items:
                prov = getattr(item, "prov", [])
                if prov:
                    page = getattr(prov[0], "page_no", 0)
                    break

        text = chunk.text if hasattr(chunk, "text") else str(chunk)

        sid = section_id(paper_pid, idx)
        insert_section(conn, paper_pid, sid, title, level, text, page)

    return len(chunks)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest papers into the Kuzu graph.")
    parser.add_argument("--db",       default=str(DEFAULT_DB), help="Kuzu DB directory")
    parser.add_argument("--force",    action="store_true",     help="Re-ingest already-processed papers")
    parser.add_argument("--no-parse", action="store_true",     help="Skip Docling; only update graph structure")
    args = parser.parse_args()

    db_path = Path(args.db)

    if not CITATIONS.exists():
        raise SystemExit("citations.json not found — run fetch-citations.py first")

    manifest = json.loads(CITATIONS.read_text())
    db   = open_db(db_path)
    conn = kuzu.Connection(db)

    print(f"DB: {db_path}")

    # --- Track which paper IDs are already fully ingested ---
    ingested: set[str] = set()
    if not args.force:
        try:
            result = conn.execute("MATCH (p:Paper) WHERE p.local_path <> '' RETURN p.id")
            while result.has_next():
                row = result.get_next()
                ingested.add(row[0])
        except Exception:
            pass

    # --- Seeds ---
    seed_pid: dict[str, str] = {}  # arxiv_id → paper node id

    print(f"\n--- Seeds ({len(manifest['seeds'])}) ---")
    for node in manifest["seeds"]:
        arxiv_id   = node.get("arxiv_id", "")
        local_file = node.get("file", "")
        local_path = str(PAPERS_DIR / local_file) if local_file else ""

        pid = upsert_paper(conn, node, local_path)
        seed_pid[arxiv_id] = pid

        for author in node.get("authors") or []:
            upsert_author(conn, author)
            link_authored_by(conn, pid, author)

        for plan_id in node.get("articles") or []:
            upsert_article_plan(conn, plan_id)
            link_references(conn, plan_id, pid)

        if not args.no_parse and local_path and Path(local_path).exists():
            if pid not in ingested or args.force:
                print(f"  parse  {local_file} ...", end=" ", flush=True)
                n = parse_paper(Path(local_path), pid, conn)
                print(f"{n} chunks")
            else:
                print(f"  skip   {local_file}  (already ingested)")
        else:
            if not Path(local_path).exists():
                print(f"  MISSING {local_file}")

    # --- Refs ---
    ref_pid: dict[str, str] = {}  # s2_id → paper node id

    print(f"\n--- Refs ({len(manifest['refs'])}) ---")
    for node in manifest["refs"]:
        arxiv_id   = node.get("arxiv_id")
        s2_id      = node.get("s2_id", "")
        local_file = node.get("local_file", "")
        local_path = str(REFS_DIR / local_file) if local_file else ""

        pid = upsert_paper(conn, node, local_path)
        ref_pid[s2_id] = pid

        for author in node.get("authors") or []:
            upsert_author(conn, author)
            link_authored_by(conn, pid, author)

        if not args.no_parse and local_path and Path(local_path).exists():
            if pid not in ingested or args.force:
                print(f"  parse  {local_file} ...", end=" ", flush=True)
                n = parse_paper(Path(local_path), pid, conn)
                print(f"{n} chunks")

    # --- Citation edges ---
    print("\n--- Citation edges ---")
    edge_count = 0
    for edge in manifest.get("edges", []):
        from_arxiv = edge["from_arxiv"]
        to_s2_id   = edge["to_s2_id"]
        from_pid   = seed_pid.get(from_arxiv)
        to_pid     = ref_pid.get(to_s2_id)
        if from_pid and to_pid:
            link_cites(conn, from_pid, to_pid)
            edge_count += 1

    print(f"  {edge_count} CITES edges written")
    print(f"\nDone. Graph at {db_path}")


if __name__ == "__main__":
    main()
