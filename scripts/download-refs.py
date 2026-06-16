"""
download-refs.py — Download first-level reference PDFs to articles/refs/.

Reads articles/papers/citations.json (produced by fetch-citations.py) and
downloads every ref node that has a download_url and does not already exist.

Safe to re-run — skips files that already exist.

Usage:
    python scripts/download-refs.py [--limit N] [--dry-run]

Requires:
    pip install requests
    Run fetch-citations.py first.
"""

import argparse
import json
import re
import time
from pathlib import Path

try:
    import requests
except ImportError:
    raise SystemExit("ERROR: pip install requests")

DELAY = 0.8  # seconds between downloads


def safe_filename(title: str, arxiv_id: str | None, s2_id: str) -> str:
    """Build a filesystem-safe filename for a ref paper."""
    if arxiv_id:
        slug = re.sub(r"[^\w\-]", "-", title.lower())[:60].strip("-")
        return f"arxiv-{arxiv_id}-{slug}.pdf"
    slug = re.sub(r"[^\w\-]", "-", title.lower())[:60].strip("-")
    short_id = s2_id[:12] if s2_id else "unknown"
    return f"ref-{short_id}-{slug}.pdf"


def main() -> None:
    parser = argparse.ArgumentParser(description="Download first-level reference PDFs.")
    parser.add_argument("--limit",   type=int, default=0, help="Max downloads this run (0 = no limit)")
    parser.add_argument("--dry-run", action="store_true",  help="Print what would be downloaded without fetching")
    args = parser.parse_args()

    repo_root    = Path(__file__).parent.parent
    citations    = repo_root / "articles" / "papers" / "citations.json"
    refs_dir     = repo_root / "articles" / "refs"
    not_found_log = refs_dir / "not-downloadable.json"

    if not citations.exists():
        raise SystemExit("citations.json not found — run fetch-citations.py first")

    refs_dir.mkdir(parents=True, exist_ok=True)
    manifest = json.loads(citations.read_text())
    refs = manifest.get("refs", [])

    session = requests.Session()
    session.headers["User-Agent"] = "job-hunt-2026-research/1.0 (personal research corpus)"

    downloaded = 0
    skipped    = 0
    no_url     = 0
    failed: list[dict] = []
    not_downloadable: list[dict] = []

    for ref in refs:
        url   = ref.get("download_url")
        title = ref.get("title", "untitled")

        if not url:
            no_url += 1
            not_downloadable.append({
                "s2_id":    ref.get("s2_id"),
                "arxiv_id": ref.get("arxiv_id"),
                "title":    title,
                "reason":   "no open-access URL found",
                "cited_by": ref.get("cited_by_seeds", []),
            })
            continue

        filename = safe_filename(title, ref.get("arxiv_id"), ref.get("s2_id", ""))
        dest = refs_dir / filename

        # Store the resolved filename back so ingest.py can find it
        ref["local_file"] = filename

        if dest.exists():
            skipped += 1
            continue

        if args.limit and downloaded >= args.limit:
            print(f"Limit of {args.limit} reached — stopping.")
            break

        if args.dry_run:
            print(f"WOULD DOWNLOAD  {filename}")
            print(f"  from: {url}")
            downloaded += 1
            continue

        try:
            resp = session.get(url, timeout=30, stream=True)
            resp.raise_for_status()
            content_type = resp.headers.get("content-type", "")
            if "pdf" not in content_type and "octet-stream" not in content_type:
                # Some URLs redirect to a landing page rather than the PDF
                not_downloadable.append({
                    "s2_id":    ref.get("s2_id"),
                    "arxiv_id": ref.get("arxiv_id"),
                    "title":    title,
                    "reason":   f"non-PDF content-type: {content_type}",
                    "url":      url,
                    "cited_by": ref.get("cited_by_seeds", []),
                })
                no_url += 1
                continue

            with open(dest, "wb") as fh:
                for chunk in resp.iter_content(chunk_size=65536):
                    fh.write(chunk)

            size_kb = dest.stat().st_size // 1024
            print(f"OK    {filename}  ({size_kb} KB)")
            downloaded += 1

        except Exception as exc:
            print(f"FAIL  {filename} — {exc}")
            failed.append({"file": filename, "url": url, "error": str(exc)})
            if dest.exists():
                dest.unlink()

        time.sleep(DELAY)

    # Persist the updated manifest (with local_file fields)
    citations.write_text(json.dumps(manifest, indent=2))

    # Log papers we couldn't download for manual follow-up
    not_found_log.write_text(json.dumps(not_downloadable, indent=2))

    print(f"\nDownloaded : {downloaded}")
    print(f"Skipped    : {skipped}  (already exist)")
    print(f"No URL     : {no_url}   (logged to {not_found_log.name})")
    print(f"Failed     : {len(failed)}")
    if failed:
        for f in failed:
            print(f"  {f['file']} — {f['error']}")


if __name__ == "__main__":
    main()
