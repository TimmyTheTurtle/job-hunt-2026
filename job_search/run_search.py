#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
from zoneinfo import ZoneInfo

from jobspy import scrape_jobs


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROFILE = ROOT / "job_search" / "search_profile.json"
DEFAULT_OUTPUT_DIR = ROOT / "job_search" / "output"
APPLICATIONS_DIR = ROOT / "applications"
TIMEZONE = ZoneInfo("America/New_York")

TIER_BONUS = {"A": 4, "B": 2, "C": 0}

POSITIVE_TITLE_PATTERNS = [
    (re.compile(r"\bsoftware\b"), 2, "software"),
    (re.compile(r"\bdeveloper\b"), 2, "developer"),
    (re.compile(r"\bprogrammer\b"), 2, "programmer"),
    (re.compile(r"\bsimulation\b"), 4, "simulation"),
    (re.compile(r"\bmodel(?:ing)?\b"), 3, "modeling"),
    (re.compile(r"\bsystems?\b"), 2, "systems"),
    (re.compile(r"\breal[ -]?time\b"), 3, "real-time"),
    (re.compile(r"\bengine\b"), 2, "engine"),
    (re.compile(r"\bgraphics?\b"), 3, "graphics"),
    (re.compile(r"\brender(?:ing)?\b"), 3, "rendering"),
    (re.compile(r"\bphysics\b"), 3, "physics"),
    (re.compile(r"\bhpc\b"), 3, "hpc"),
    (re.compile(r"\bscientific\b"), 2, "scientific"),
    (re.compile(r"\bdistributed\b"), 2, "distributed"),
    (re.compile(r"\bperformance\b"), 2, "performance"),
]

POSITIVE_TEXT_PATTERNS = [
    (re.compile(r"c\+\+|c plus plus|\bcpp\b"), 3, "c++"),
    (re.compile(r"\bsimulation\b"), 2, "simulation"),
    (re.compile(r"\bmodel(?:ing)?\b"), 2, "modeling"),
    (re.compile(r"\bperformance\b"), 2, "performance"),
    (re.compile(r"\bdistributed\b"), 2, "distributed"),
    (re.compile(r"\bmultithread(?:ed|ing)?\b|\bconcurren(?:cy|t)\b"), 2, "concurrency"),
    (re.compile(r"\bgraphics?\b|\brender(?:ing)?\b"), 2, "graphics"),
    (re.compile(r"\bhpc\b|\bhigh performance computing\b"), 2, "hpc"),
]

HARD_REJECT_TITLE_PATTERNS = [
    re.compile(r"\bintern\b"),
    re.compile(r"\brotational\b"),
    re.compile(r"\bmanager\b"),
    re.compile(r"\bdirector\b"),
    re.compile(r"\barchitect\b"),
    re.compile(r"\brecruiter\b"),
    re.compile(r"\bsales\b"),
    re.compile(r"\bmarketing\b"),
    re.compile(r"\bproduct manager\b"),
    re.compile(r"\bdata scientist\b"),
    re.compile(r"\bmachine learning\b"),
    re.compile(r"\bml\b"),
    re.compile(r"\bbusiness intelligence\b"),
    re.compile(r"\bfrontend\b"),
    re.compile(r"\bbackend\b"),
    re.compile(r"\bfull[ -]?stack\b"),
    re.compile(r"\blow[- ]code\b"),
    re.compile(r"\bdesigner\b"),
    re.compile(r"\bverification\b"),
    re.compile(r"\bmanufacturing\b"),
    re.compile(r"\bmechanical\b"),
    re.compile(r"\bthermal\b"),
]

HARD_REJECT_TEXT_PATTERNS = [
    re.compile(r"\baspice\b"),
    re.compile(r"\badas\b"),
    re.compile(r"\bwordpress\b"),
    re.compile(r"\bcrm\b"),
    re.compile(r"\binsurance sales\b"),
]

SENIORITY_PENALTIES = [
    (re.compile(r"\bprincipal\b"), -5, "principal"),
    (re.compile(r"\bstaff\b"), -4, "staff"),
    (re.compile(r"\blead\b"), -3, "lead"),
    (re.compile(r"\bsenior\b"), -2, "senior"),
]


@dataclass
class SearchSpec:
    tier: str
    label: str
    search_term: str
    google_search_term: str
    location_label: str
    location: str
    google_location_phrase: str
    is_remote: bool


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run one-shot preferred-role job search.")
    parser.add_argument("--profile", default=str(DEFAULT_PROFILE))
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--hours-old", type=int)
    parser.add_argument("--results-per-query", type=int)
    parser.add_argument("--max-searches", type=int)
    parser.add_argument("--sites", help="Comma-separated override, e.g. google,indeed")
    return parser.parse_args()


def load_profile(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_url(url: str) -> str:
    if not url:
        return ""
    split = urlsplit(url.strip())
    query = [(k, v) for k, v in parse_qsl(split.query, keep_blank_values=True) if not k.lower().startswith("utm_")]
    normalized_path = split.path.rstrip("/") or "/"
    return urlunsplit((split.scheme.lower(), split.netloc.lower(), normalized_path, urlencode(query), ""))


def existing_application_urls() -> set[str]:
    urls: set[str] = set()
    for path in APPLICATIONS_DIR.glob("*/job_description.md"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in re.findall(r"https?://\S+", text):
            urls.add(normalize_url(match.rstrip(")]>")))
    return urls


def build_search_specs(profile: dict[str, Any]) -> list[SearchSpec]:
    specs: list[SearchSpec] = []
    for location in profile["locations"]:
        for search in profile["searches"]:
            specs.append(
                SearchSpec(
                    tier=search["tier"],
                    label=search["label"],
                    search_term=search["search_term"],
                    google_search_term=search["google_search_term_template"].format(
                        google_location_phrase=location["google_location_phrase"]
                    ),
                    location_label=location["label"],
                    location=location["location"],
                    google_location_phrase=location["google_location_phrase"],
                    is_remote=bool(location.get("is_remote", False)),
                )
            )
    return specs


def safe_str(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def build_location(row: dict[str, Any]) -> str:
    pieces = [
        safe_str(row.get("location")),
        safe_str(row.get("city")),
        safe_str(row.get("state")),
        safe_str(row.get("country")),
    ]
    cleaned = []
    for piece in pieces:
        if piece and piece not in cleaned:
            cleaned.append(piece)
    return ", ".join(cleaned[:3])


def row_to_text(row: dict[str, Any]) -> tuple[str, str]:
    title = safe_str(row.get("title"))
    description = safe_str(row.get("description"))
    company = safe_str(row.get("company"))
    location = build_location(row)
    return title.lower(), f"{title}\n{company}\n{location}\n{description}".lower()


def classify(row: dict[str, Any], spec: SearchSpec) -> tuple[int, list[str], bool]:
    title_text, full_text = row_to_text(row)
    reasons: list[str] = []
    score = TIER_BONUS.get(spec.tier, 0)
    rejected = False
    title_hits: set[str] = set()

    for pattern in HARD_REJECT_TITLE_PATTERNS:
        if pattern.search(title_text):
            rejected = True
            reasons.append(f"reject:{pattern.pattern}")
            break

    if not rejected:
        for pattern in HARD_REJECT_TEXT_PATTERNS:
            if pattern.search(full_text):
                rejected = True
                reasons.append(f"reject:{pattern.pattern}")
                break

    for pattern, delta, label in SENIORITY_PENALTIES:
        if pattern.search(title_text):
            score += delta
            reasons.append(label)

    for pattern, delta, label in POSITIVE_TITLE_PATTERNS:
        if pattern.search(title_text):
            score += delta
            reasons.append(label)
            title_hits.add(label)

    for pattern, delta, label in POSITIVE_TEXT_PATTERNS:
        if pattern.search(full_text):
            score += delta
            if label not in reasons:
                reasons.append(label)

    if spec.location_label == "remote" and safe_str(row.get("is_remote")).lower() in {"true", "1"}:
        score += 2
        reasons.append("remote")
    elif "michigan" in build_location(row).lower():
        score += 2
        reasons.append("michigan")

    if safe_str(row.get("site")) == "google":
        score += 1
        reasons.append("google")

    if not title_hits:
        score = min(score, 6)
        reasons.append("weak_title_match")

    return score, sorted(set(reasons)), rejected


def recommendation(score: int, rejected: bool) -> str:
    if rejected:
        return "skip"
    if score >= 12:
        return "apply_first"
    if score >= 8:
        return "review"
    return "low_priority"


def date_to_str(value: Any) -> str:
    text = safe_str(value)
    if not text:
        return ""
    return text.replace("T", " ")


def is_allowed_location(row: dict[str, Any]) -> bool:
    country = safe_str(row.get("country")).lower()
    if country and country not in {"us", "usa", "united states", "united states of america"}:
        return False

    location_text = f"{build_location(row)} {safe_str(row.get('title'))}".lower()
    blocked_markers = [
        "brazil",
        "india",
        "indonesia",
        "germany",
        "poland",
        "spain",
        "portugal",
        "malaysia",
        "canada",
        "singapore",
        "sao paulo",
        "pune",
    ]
    return not any(marker in location_text for marker in blocked_markers)


def scrape_spec(spec: SearchSpec, profile: dict[str, Any], sites: list[str], hours_old: int, results_per_query: int) -> list[dict[str, Any]]:
    effective_sites = list(sites)
    kwargs: dict[str, Any] = {
        "site_name": effective_sites,
        "search_term": spec.search_term,
        "google_search_term": spec.google_search_term,
        "location": spec.location,
        "results_wanted": results_per_query,
        "hours_old": hours_old,
        "country_indeed": profile["country_indeed"],
        "verbose": 0,
    }
    if spec.is_remote:
        kwargs["is_remote"] = True

    jobs = scrape_jobs(**kwargs)
    if jobs is None or len(jobs) == 0:
        return []
    return jobs.to_dict(orient="records")


def key_for_candidate(row: dict[str, Any]) -> str:
    url = normalize_url(safe_str(row.get("job_url")))
    if url:
        return url
    title = safe_str(row.get("title")).lower()
    company = safe_str(row.get("company")).lower()
    location = build_location(row).lower()
    return f"{company}|{title}|{location}"


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    fieldnames = [
        "recommendation",
        "score",
        "tier",
        "company",
        "title",
        "location",
        "sites",
        "posted",
        "job_url",
        "query_labels",
        "reasons",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({name: row.get(name, "") for name in fieldnames})


def write_markdown(
    path: Path,
    rows: list[dict[str, Any]],
    profile_name: str,
    sites: list[str],
    search_count: int,
    existing_url_count: int,
) -> None:
    generated = datetime.now(TIMEZONE).strftime("%Y-%m-%d %H:%M %Z")
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[row["recommendation"]].append(row)

    sections = [
        ("apply_first", "Apply First"),
        ("review", "Review"),
        ("low_priority", "Low Priority"),
    ]

    lines = [
        "# Job Search Inbox",
        "",
        f"- Generated: {generated}",
        f"- Profile: `{profile_name}`",
        f"- Sites: `{', '.join(sites)}`",
        f"- Search specs run: {search_count}",
        f"- Existing application URLs known: {existing_url_count}",
        f"- Ranked results: {len(rows)}",
        "",
    ]

    for key, title in sections:
        bucket = grouped.get(key, [])
        if not bucket:
            continue
        lines.append(f"## {title}")
        lines.append("")
        for idx, row in enumerate(bucket, start=1):
            company = row["company"] or "Unknown company"
            title_text = row["title"] or "Unknown title"
            lines.append(f"### {idx}. {company} - {title_text}")
            lines.append(f"- Score: {row['score']}")
            lines.append(f"- Tier: {row['tier']}")
            lines.append(f"- Location: {row['location'] or 'Unknown'}")
            lines.append(f"- Site(s): {row['sites']}")
            if row["posted"]:
                lines.append(f"- Posted: {row['posted']}")
            lines.append(f"- Query labels: {row['query_labels']}")
            lines.append(f"- Match notes: {row['reasons']}")
            lines.append(f"- Posting URL: {row['job_url']}")
            lines.append("")

    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    profile_path = Path(args.profile)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    profile = load_profile(profile_path)
    sites = [item.strip() for item in (args.sites.split(",") if args.sites else profile["default_sites"]) if item.strip()]
    hours_old = args.hours_old if args.hours_old is not None else int(profile["hours_old"])
    results_per_query = args.results_per_query if args.results_per_query is not None else int(profile["results_wanted_per_query"])

    specs = build_search_specs(profile)
    if args.max_searches is not None:
        specs = specs[: args.max_searches]

    known_urls = existing_application_urls()
    aggregated: dict[str, dict[str, Any]] = {}

    for spec in specs:
        try:
            rows = scrape_spec(spec, profile, sites, hours_old, results_per_query)
        except Exception as exc:
            print(f"[warn] search failed for {spec.label} / {spec.location_label}: {exc}")
            continue

        for row in rows:
            if not is_allowed_location(row):
                continue

            score, reasons, rejected = classify(row, spec)
            job_url = normalize_url(safe_str(row.get("job_url")))
            if job_url and job_url in known_urls:
                continue

            key = key_for_candidate(row)
            candidate = {
                "recommendation": recommendation(score, rejected),
                "score": score,
                "tier": spec.tier,
                "company": safe_str(row.get("company")),
                "title": safe_str(row.get("title")),
                "location": build_location(row),
                "sites": safe_str(row.get("site")),
                "posted": date_to_str(row.get("date_posted")),
                "job_url": job_url or safe_str(row.get("job_url")),
                "query_labels": spec.label,
                "reasons": ", ".join(reasons),
            }

            if key not in aggregated:
                aggregated[key] = candidate
                continue

            existing = aggregated[key]
            if score > existing["score"]:
                aggregated[key] = {**candidate, "sites": existing["sites"], "query_labels": existing["query_labels"]}
                existing = aggregated[key]

            merged_sites = {item.strip() for item in (existing["sites"] + ", " + candidate["sites"]).split(",") if item.strip()}
            merged_labels = {item.strip() for item in (existing["query_labels"] + ", " + spec.label).split(",") if item.strip()}
            merged_reasons = {item.strip() for item in (existing["reasons"] + ", " + ", ".join(reasons)).split(",") if item.strip()}
            existing["sites"] = ", ".join(sorted(merged_sites))
            existing["query_labels"] = ", ".join(sorted(merged_labels))
            existing["reasons"] = ", ".join(sorted(merged_reasons))
            existing["score"] = max(existing["score"], score)
            existing["recommendation"] = recommendation(existing["score"], rejected)

    ranked = sorted(
        aggregated.values(),
        key=lambda row: (
            {"apply_first": 0, "review": 1, "low_priority": 2, "skip": 3}[row["recommendation"]],
            -row["score"],
            row["company"].lower(),
            row["title"].lower(),
        ),
    )

    ranked = [row for row in ranked if row["recommendation"] != "skip"]
    ranked = ranked[: int(profile["max_report_items"])]

    timestamp = datetime.now(TIMEZONE).strftime("%Y-%m-%d_%H%M%S")
    base = output_dir / f"job_search_{timestamp}"
    markdown_path = base.with_suffix(".md")
    csv_path = base.with_suffix(".csv")

    write_markdown(markdown_path, ranked, profile["profile_name"], sites, len(specs), len(known_urls))
    write_csv(csv_path, ranked)

    print(f"Markdown report: {markdown_path}")
    print(f"CSV export: {csv_path}")
    print(f"Ranked results: {len(ranked)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
