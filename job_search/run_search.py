#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import json
import re
import urllib.parse
import urllib.request
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

from jobspy import scrape_jobs
from ledger import BLOCKING_STATUSES, existing_application_urls, normalize_url, record_transaction, state_map


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROFILE = ROOT / "job_search" / "search_profile.json"
DEFAULT_OUTPUT_DIR = ROOT / "job_search" / "output"
TIMEZONE = ZoneInfo("America/New_York")

TIER_BONUS = {"A": 4, "B": 2, "C": 0}

JOBSPY_SITES = {
    "linkedin",
    "indeed",
    "zip_recruiter",
    "glassdoor",
    "google",
    "bayt",
    "naukri",
    "bdjobs",
}
CUSTOM_SITES = {"cybercoders"}
CYBERCODERS_SEARCH_URL = "https://www.cybercoders.com/ccv5-jobs/search"
CYBERCODERS_JOB_BASE_URL = "https://www.cybercoders.com/job/"
CYBERCODERS_BUSINESS_UNIT = "1"

POSITIVE_TITLE_PATTERNS = [
    (re.compile(r"\bai\b|\bartificial intelligence\b"), 4, "ai"),
    (re.compile(r"\bllm\b|\blarge language model"), 4, "llm"),
    (re.compile(r"\brag\b|\bretrieval[ -]?augmented\b"), 4, "rag"),
    (re.compile(r"\bdocument intelligence\b"), 4, "document intelligence"),
    (re.compile(r"\bcontract(?:or)?\b|\bcontract[ -]?to[ -]?hire\b|\b1099\b|\bc2c\b|\bw2\b"), 2, "contract"),
    (re.compile(r"\bautomation\b|\bworkflow\b"), 3, "workflow automation"),
    (re.compile(r"\bsolutions?\b"), 2, "solutions"),
    (re.compile(r"\bsoftware\b"), 2, "software"),
    (re.compile(r"\bdeveloper\b"), 2, "developer"),
    (re.compile(r"\bprogrammer\b"), 2, "programmer"),
    (re.compile(r"\bcompliance\b|\blegal\b|\bregulatory\b|\binsurance\b"), 3, "compliance domain"),
    (re.compile(r"\bsystems?\b"), 3, "systems"),
    (re.compile(r"\bsimulation\b"), 4, "simulation"),
    (re.compile(r"\bmodel(?:ing)?\b"), 3, "modeling"),
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
    (re.compile(r"\bllm\b|\blarge language model|\bgenerative ai\b|\bgenai\b"), 3, "llm"),
    (re.compile(r"\brag\b|\bretrieval[ -]?augmented\b|\bvector search\b|\bsemantic search\b"), 3, "rag"),
    (re.compile(r"\bdocument intelligence\b|\bdocument automation\b|\bdocument processing\b"), 3, "document intelligence"),
    (re.compile(r"\bcontract(?:or)?\b|\bcontract[ -]?to[ -]?hire\b|\b1099\b|\bc2c\b|\bw2\b"), 2, "contract"),
    (re.compile(r"\bevals?\b|\bevaluation\b|\bquality gate\b|\bhuman[ -]in[ -]the[ -]loop\b"), 3, "evals"),
    (re.compile(r"\btraceability\b|\baudit trail\b|\bevidence\b|\bgovernance\b"), 2, "traceability"),
    (re.compile(r"\bworkflow automation\b|\bautomation\b|\bagentic\b|\bagents?\b"), 2, "workflow automation"),
    (re.compile(r"\bcompliance\b|\blegal\b|\bregulatory\b|\binsurance\b"), 2, "compliance domain"),
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
    re.compile(r"\bbusiness development\b"),
    re.compile(r"\bcommission\b"),
    re.compile(r"\bmarketing\b"),
    re.compile(r"\bproduct manager\b"),
    re.compile(r"\bdata scientist\b"),
    re.compile(r"\battorney\b"),
    re.compile(r"\bparalegal\b"),
    re.compile(r"\blegal research analyst\b"),
    re.compile(r"\bprompt engineer\b"),
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
    re.compile(r"\bcommission based\b"),
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
    job_type: str
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
    parser.add_argument(
        "--dry-run",
        "--no-ledger",
        dest="dry_run",
        action="store_true",
        help="Write reports without recording surfaced jobs in the search ledger.",
    )
    return parser.parse_args()


def load_profile(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_search_specs(profile: dict[str, Any]) -> list[SearchSpec]:
    specs: list[SearchSpec] = []
    default_job_type = safe_str(profile.get("job_type"))
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
                    job_type=safe_str(search.get("job_type")) or default_job_type,
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


def is_missing(value: Any) -> bool:
    if value is None:
        return True
    try:
        if value != value:  # NaN
            return True
    except TypeError:
        pass
    return safe_str(value).lower() in {"", "nan", "none", "null"}


def compensation_interval(value: Any) -> str:
    text = safe_str(value).lower()
    if not text:
        return ""
    if "hour" in text:
        return "hourly"
    if "year" in text or "annual" in text:
        return "yearly"
    if "month" in text:
        return "monthly"
    if "week" in text:
        return "weekly"
    if "day" in text:
        return "daily"
    return text


def format_amount(value: Any, currency: str) -> str:
    if is_missing(value):
        return ""
    try:
        number = float(value)
    except (TypeError, ValueError):
        return safe_str(value)

    symbol = "$" if currency.upper() in {"", "USD"} else f"{currency.upper()} "
    if number.is_integer():
        return f"{symbol}{int(number):,}"
    return f"{symbol}{number:,.2f}"


def format_compensation(row: dict[str, Any]) -> str:
    min_amount = row.get("min_amount")
    max_amount = row.get("max_amount")
    if is_missing(min_amount) and is_missing(max_amount):
        return ""

    currency = safe_str(row.get("currency")) or "USD"
    interval = compensation_interval(row.get("interval"))
    source = safe_str(row.get("salary_source"))
    low = format_amount(min_amount, currency)
    high = format_amount(max_amount, currency)
    if low and high and low != high:
        amount = f"{low} - {high}"
    else:
        amount = low or high

    pieces = [amount]
    if interval:
        pieces.append(interval)
    if source:
        pieces.append(f"source: {source}")
    return " ".join(pieces)


def joined_items(value: Any) -> str:
    if not isinstance(value, list):
        return safe_str(value)

    items = []
    for item in value:
        text = safe_str(item)
        if text and text not in items:
            items.append(text)
    return "; ".join(items)


def cybercoders_days_posted(hours_old: int) -> str:
    if hours_old <= 0:
        return "0"
    if hours_old <= 24:
        return "1"
    if hours_old <= 72:
        return "3"
    if hours_old <= 168:
        return "7"
    if hours_old <= 336:
        return "14"
    return "0"


def cybercoders_job_url(job: dict[str, Any]) -> str:
    slug = safe_str(job.get("JobURL"))
    if not slug:
        return ""
    if slug.startswith(("http://", "https://")):
        return slug
    return urllib.parse.urljoin(CYBERCODERS_JOB_BASE_URL, slug.lstrip("/"))


def cybercoders_is_remote(job: dict[str, Any]) -> bool:
    return (
        safe_str(job.get("WorkLocationTypeId")) == "3"
        or safe_str(job.get("Telecommute")).lower() in {"true", "1", "yes"}
    )


def cybercoders_description(job: dict[str, Any]) -> str:
    parts = [safe_str(job.get("ShortDescription"))]
    tags = joined_items(job.get("tags"))
    if tags:
        parts.append(f"Tags: {tags}")
    salary_min = safe_str(job.get("SalaryMin"))
    salary_max = safe_str(job.get("SalaryMax"))
    salary_type = safe_str(job.get("SalaryType"))
    if salary_min or salary_max:
        salary = " - ".join(item for item in [salary_min, salary_max] if item)
        parts.append(f"Salary: {salary} {salary_type}".strip())
    return "\n".join(part for part in parts if part)


def cybercoders_row(job: dict[str, Any]) -> dict[str, Any]:
    remote = cybercoders_is_remote(job)
    salary_type = safe_str(job.get("SalaryType"))
    return {
        "site": "cybercoders",
        "title": safe_str(job.get("JobTitleThirdParty")) or safe_str(job.get("jobTitle")),
        "company": safe_str(job.get("CompanyName")) or "CyberCoders",
        "location": "Remote" if remote else "",
        "city": "" if remote else joined_items(job.get("City")),
        "state": "" if remote else joined_items(job.get("StateCode")),
        "country": "US",
        "description": cybercoders_description(job),
        "job_url": cybercoders_job_url(job),
        "date_posted": safe_str(job.get("DatePost")),
        "is_remote": remote,
        "interval": compensation_interval(salary_type),
        "min_amount": safe_str(job.get("SalaryMin")),
        "max_amount": safe_str(job.get("SalaryMax")),
        "currency": "USD",
        "salary_source": "cybercoders_direct",
    }


def scrape_cybercoders(spec: SearchSpec, hours_old: int, results_per_query: int) -> list[dict[str, Any]]:
    params = {
        "keyword": spec.search_term,
        "rows": str(results_per_query),
        "page": "1",
        "termOption": "PERM",
        "sortType": "relevance",
        "daysPosted": cybercoders_days_posted(hours_old),
        "buid": CYBERCODERS_BUSINESS_UNIT,
    }
    if spec.is_remote:
        params["workLocationTypeId"] = "3"
    elif spec.location:
        params["locationKeyword"] = spec.location

    url = f"{CYBERCODERS_SEARCH_URL}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (compatible; job-hunt-2026/1.0)",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        data = json.loads(response.read().decode("utf-8"))

    jobs = data.get("jobs")
    if not isinstance(jobs, list):
        return []
    return [cybercoders_row(job) for job in jobs if isinstance(job, dict)]


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
        "mexico",
        "mexico city",
        "united kingdom",
        " uk",
        "london",
        "england",
        "northern ireland",
        "belfast",
        "france",
        "paris",
        "qatar",
        "doha",
        "netherlands",
        "eindhoven",
        "singapore",
        "sao paulo",
        "pune",
    ]
    return not any(marker in location_text for marker in blocked_markers)


def scrape_spec(spec: SearchSpec, profile: dict[str, Any], sites: list[str], hours_old: int, results_per_query: int) -> list[dict[str, Any]]:
    requested_sites = [safe_str(site).lower() for site in sites if safe_str(site)]
    jobspy_sites = [site for site in requested_sites if site in JOBSPY_SITES]
    unsupported_sites = sorted(
        {site for site in requested_sites if site not in JOBSPY_SITES and site not in CUSTOM_SITES}
    )
    rows: list[dict[str, Any]] = []

    for site in unsupported_sites:
        print(f"[warn] unsupported site skipped for {spec.label} / {spec.location_label}: {site}")

    if jobspy_sites:
        kwargs: dict[str, Any] = {
            "site_name": jobspy_sites,
            "search_term": spec.search_term,
            "google_search_term": spec.google_search_term,
            "location": spec.location,
            "results_wanted": results_per_query,
            "hours_old": hours_old,
            "country_indeed": profile["country_indeed"],
            "verbose": 0,
        }
        if spec.job_type:
            kwargs["job_type"] = spec.job_type
        if spec.is_remote:
            kwargs["is_remote"] = True

        try:
            jobs = scrape_jobs(**kwargs)
            if jobs is not None and len(jobs) > 0:
                rows.extend(jobs.to_dict(orient="records"))
        except Exception as exc:
            print(f"[warn] jobspy search failed for {spec.label} / {spec.location_label}: {exc}")

    if "cybercoders" in requested_sites:
        try:
            rows.extend(scrape_cybercoders(spec, hours_old, results_per_query))
        except Exception as exc:
            print(f"[warn] cybercoders search failed for {spec.label} / {spec.location_label}: {exc}")

    return rows


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
        "compensation",
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
    ledger_info: dict[str, Any],
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
        f"- Suppressed by search ledger: {ledger_info['suppressed_by_ledger']}",
        f"- Suppressed by application folders: {ledger_info['suppressed_by_applications']}",
        "- Ledger transaction: dry run (not recorded)"
        if ledger_info.get("dry_run")
        else f"- Ledger transaction: `{ledger_info['transaction_id']}`"
        if ledger_info["transaction_id"]
        else "- Ledger transaction: none",
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
            lines.append(f"- Compensation: {row['compensation'] or 'Not listed'}")
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

    known_application_urls = existing_application_urls()
    ledger_jobs = state_map()
    blocked_ledger_urls = {url for url, job in ledger_jobs.items() if job.get("status") in BLOCKING_STATUSES}
    aggregated: dict[str, dict[str, Any]] = {}
    suppressed_by_ledger = 0
    suppressed_by_applications = 0

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
            if job_url and job_url in known_application_urls:
                suppressed_by_applications += 1
                continue
            if job_url and job_url in blocked_ledger_urls:
                suppressed_by_ledger += 1
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
                "compensation": format_compensation(row),
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

    ledger_events = [
        {
            "status": "surfaced",
            "job_url": row["job_url"],
            "company": row["company"],
            "title": row["title"],
            "location": row["location"],
            "sites": [item.strip() for item in row["sites"].split(",") if item.strip()],
            "query_labels": [item.strip() for item in row["query_labels"].split(",") if item.strip()],
            "score": row["score"],
            "recommendation": row["recommendation"],
            "compensation": row["compensation"],
        }
        for row in ranked
        if row["job_url"]
    ]
    if args.dry_run:
        ledger_result = {"transaction_id": "", "event_count": 0, "dry_run": True}
    elif ledger_events:
        ledger_result = record_transaction(
            actor="job_search_runner",
            kind="search_run",
            events=ledger_events,
            metadata={
                "profile_name": profile["profile_name"],
                "sites": sites,
                "search_specs_run": len(specs),
            },
        )
    else:
        ledger_result = {"transaction_id": "", "event_count": 0, "dry_run": False}

    timestamp = datetime.now(TIMEZONE).strftime("%Y-%m-%d_%H%M%S")
    base = output_dir / f"job_search_{timestamp}"
    markdown_path = base.with_suffix(".md")
    csv_path = base.with_suffix(".csv")

    write_markdown(
        markdown_path,
        ranked,
        profile["profile_name"],
        sites,
        len(specs),
        len(known_application_urls),
        {
            "suppressed_by_ledger": suppressed_by_ledger,
            "suppressed_by_applications": suppressed_by_applications,
            "transaction_id": ledger_result["transaction_id"],
            "dry_run": bool(ledger_result.get("dry_run")),
        },
    )
    write_csv(csv_path, ranked)

    print(f"Markdown report: {markdown_path}")
    print(f"CSV export: {csv_path}")
    if args.dry_run:
        print("Ledger transaction: dry run (not recorded)")
    elif ledger_result["transaction_id"]:
        print(f"Ledger transaction: {ledger_result['transaction_id']}")
    print(f"Ranked results: {len(ranked)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
