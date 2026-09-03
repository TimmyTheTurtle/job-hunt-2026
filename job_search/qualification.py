from __future__ import annotations

import html
import json
import re
from pathlib import Path
from typing import Any


LEVEL_RANK = {"none": 0, "exposure": 1, "portfolio": 2, "professional": 3, "production": 4}
EDUCATION_RANK = {"none": 0, "associate": 1, "bachelors": 2, "masters": 3, "phd": 4}
DESCRIPTION_MIN_CHARS = 240

REQUIRED_HEADINGS = re.compile(
    r"^(?:minimum |basic |required )?(?:qualifications?|requirements?|what you(?:'|’)ll need|what you need|must haves?)\s*:?$",
    re.I,
)
PREFERRED_HEADINGS = re.compile(r"^(?:preferred qualifications?|preferred|nice to haves?|bonus)\s*:?$", re.I)
OTHER_HEADINGS = re.compile(
    r"^(?:responsibilities|what you(?:'|’)ll do|what you will do|about (?:us|the role)|benefits|compensation|salary|duties)\s*:?$",
    re.I,
)
DIRECT_REQUIRED = re.compile(
    r"\b(?:required|must (?:have|possess|be)|minimum of|at least|proficien(?:t|cy)|demonstrated experience|hands-on experience|years? of experience|expertise in)\b",
    re.I,
)
DIRECT_PREFERRED = re.compile(r"\b(?:preferred|nice to have|bonus|a plus)\b", re.I)
YEAR_WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}
YEAR_PATTERN = re.compile(
    r"(?:(?P<years>\d{1,2})(?:\s*[-–]\s*\d{1,2})?\s*\+?|(?P<word>one|two|three|four|five|six|seven|eight|nine|ten)(?:\s+or\s+more)?)\s*(?:years?|yrs?)",
    re.I,
)
REQUIRED_PREFIX = re.compile(
    r"^(?:experience required|required education and experience|required qualifications?|required skills?|minimum qualifications?|basic qualifications?|requirements?|what you(?:'|’)ll need|what you need|must haves?)\s*:?[ \t]*(.*)$",
    re.I,
)
PREFERRED_PREFIX = re.compile(r"^(?:preferred qualifications?|desired qualifications?|preferred|nice to haves?|bonus)\s*:?[ \t]*(.*)$", re.I)
OTHER_PREFIX = re.compile(
    r"^(?:responsibilities|key responsibilities|what you(?:'|’)ll do|what you will do|about (?:us|the role)|benefits|compensation|salary|duties|how to apply)\s*:?[ \t]*(.*)$",
    re.I,
)
SOFT_REQUIREMENT = re.compile(
    r"\b(?:communication skills?|written and verbal|team player|collaborat(?:e|ion)|work independently|problem[- ]solving|analytical skills?|self[- ]motivated|fast[- ]paced|stakeholder management|manage multiple|attention to detail)\b",
    re.I,
)


def load_candidate_profile(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _safe_text(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).strip()
    return "" if text.lower() in {"nan", "none", "null"} else text


def clean_description(value: Any) -> str:
    text = _safe_text(value)
    if not text:
        return ""
    text = re.sub(r"(?i)<(?:br|/p|/li|/ul|/ol|/h\d)>\s*", "\n", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = re.sub(r"\\([+()\-#])", r"\1", text)
    text = text.replace("•", "\n").replace("·", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n", text)
    return text.strip()


def description_status(description: str) -> str:
    if not description:
        return "missing"
    if len(description) < DESCRIPTION_MIN_CHARS:
        return "thin"
    return "usable"


def _description_lines(description: str) -> list[str]:
    raw_lines = [part.strip(" -:\t") for part in description.splitlines() if part.strip(" -:\t")]
    lines: list[str] = []
    for raw in raw_lines:
        if len(raw) > 260:
            pieces = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", raw)
            lines.extend(piece.strip() for piece in pieces if piece.strip())
        else:
            lines.append(raw)
    return lines


def requirement_lines(description: str) -> list[tuple[str, str]]:
    state = "other"
    results: list[tuple[str, str]] = []
    for line in _description_lines(description):
        heading = re.sub(r"[*_#`]", "", line).strip()
        prefix = REQUIRED_PREFIX.match(heading)
        if prefix:
            state = "required"
            remainder = prefix.group(1).strip(" -*:")
            if remainder:
                results.append(("required", remainder))
            continue
        prefix = PREFERRED_PREFIX.match(heading)
        if prefix:
            state = "preferred"
            remainder = prefix.group(1).strip(" -*:")
            if remainder:
                results.append(("preferred", remainder))
            continue
        prefix = OTHER_PREFIX.match(heading)
        if prefix:
            state = "other"
            continue
        if len(heading) <= 90 and REQUIRED_HEADINGS.match(heading):
            state = "required"
            continue
        if len(heading) <= 90 and PREFERRED_HEADINGS.match(heading):
            state = "preferred"
            continue
        if len(heading) <= 90 and OTHER_HEADINGS.match(heading):
            state = "other"
            continue

        if DIRECT_PREFERRED.search(line):
            kind = "preferred"
        elif DIRECT_REQUIRED.search(line):
            kind = "required"
        else:
            kind = state
        if kind in {"required", "preferred"}:
            results.append((kind, line))
    return results


def _alias_pattern(alias: str) -> re.Pattern[str]:
    return re.compile(rf"(?<![A-Za-z0-9]){re.escape(alias)}(?![A-Za-z0-9])", re.I)


def _has_alias(text: str, aliases: list[str]) -> bool:
    return any(_alias_pattern(alias).search(text) for alias in aliases)


def _scope_for_year_match(line: str, year_match: re.Match[str], skills: dict[str, Any]) -> str:
    priority = [
        "llm_rag",
        "agentic_ai",
        "ai_ml",
        "data_engineering",
        "python",
        "csharp_dotnet",
        "sql",
        "cloud_platforms",
        "customer_implementation",
        "workflow_automation",
        "software_engineering",
    ]
    candidates: list[tuple[int, int, str]] = []
    for priority_index, key in enumerate(priority):
        skill = skills.get(key, {})
        for alias in skill.get("aliases", []):
            for alias_match in _alias_pattern(alias).finditer(line):
                if alias_match.end() < year_match.start():
                    distance = year_match.start() - alias_match.end()
                elif year_match.end() < alias_match.start():
                    distance = alias_match.start() - year_match.end()
                else:
                    distance = 0
                candidates.append((distance, priority_index, key))
    if candidates:
        distance, _, key = min(candidates)
        if distance <= 100:
            return key
    return "software_engineering"


def _result_item(
    key: str,
    label: str,
    status: str,
    detail: str,
    evidence: str = "",
    hard: bool = False,
    kind: str = "required",
) -> dict[str, Any]:
    return {
        "key": key,
        "label": label,
        "status": status,
        "detail": detail,
        "evidence": evidence,
        "hard": hard,
        "kind": kind,
    }


def _evaluate_year_requirements(lines: list[tuple[str, str]], profile: dict[str, Any]) -> tuple[list[dict[str, Any]], set[str]]:
    skills = profile.get("skills", {})
    results: list[dict[str, Any]] = []
    scoped: set[str] = set()
    seen: set[tuple[str, int, str]] = set()
    for kind, line in lines:
        for match in YEAR_PATTERN.finditer(line):
            minimum = int(match.group("years")) if match.group("years") else YEAR_WORDS[match.group("word").lower()]
            scope = _scope_for_year_match(line, match, skills)
            signature = (scope, minimum, kind)
            if signature in seen:
                continue
            seen.add(signature)
            scoped.add(scope)
            skill = skills.get(scope, {})
            candidate_years = float(skill.get("years", 0) or 0)
            label = skill.get("label", scope.replace("_", " "))
            evidence = skill.get("evidence", "")
            if candidate_years >= minimum:
                status = "match"
                hard = False
            elif candidate_years > 0 and candidate_years >= minimum * 0.6:
                status = "partial"
                hard = False
            else:
                status = "gap"
                hard = kind == "required" and (minimum >= 5 or scope in {"ai_ml", "llm_rag", "agentic_ai", "data_engineering", "python"})
            results.append(
                _result_item(
                    f"years:{scope}:{minimum}",
                    f"{minimum}+ years {label}",
                    status,
                    f"Posting asks for {minimum}+ years; conservative candidate record has {candidate_years:g}.",
                    evidence,
                    hard,
                    kind,
                )
            )
    return results, scoped


def _evaluate_skill_requirements(
    lines: list[tuple[str, str]], profile: dict[str, Any], year_scopes: set[str]
) -> list[dict[str, Any]]:
    skills = profile.get("skills", {})
    detected: dict[str, tuple[str, int, str]] = {}
    for kind, line in lines:
        lower = line.lower()
        for key, skill in skills.items():
            if key in year_scopes or not _has_alias(line, skill.get("aliases", [])):
                continue
            target = 2 if kind == "preferred" else 3
            if re.search(r"\b(?:production|expert|advanced|deep expertise|strong proficiency)\b", lower):
                target = 4
            elif re.search(r"\b(?:familiarity|exposure|basic knowledge)\b", lower):
                target = 1
            existing = detected.get(key)
            if existing is None or (kind == "required", target) > (existing[0] == "required", existing[1]):
                detected[key] = (kind, target, line)

    results: list[dict[str, Any]] = []
    for key, (kind, target, line) in detected.items():
        skill = skills[key]
        level = skill.get("level", "none")
        rank = LEVEL_RANK.get(level, 0)
        if rank >= target:
            status = "match"
        elif rank + 1 >= target:
            status = "partial"
        else:
            status = "gap"
        hard = kind == "required" and target >= 4 and rank < LEVEL_RANK["professional"]
        results.append(
            _result_item(
                f"skill:{key}",
                skill.get("label", key.replace("_", " ")),
                status,
                f"Posting requirement detected; candidate evidence level is {level}.",
                skill.get("evidence", ""),
                hard,
                kind,
            )
        )
    return results


def _evaluate_degree(lines: list[tuple[str, str]], profile: dict[str, Any]) -> list[dict[str, Any]]:
    education = profile.get("education", {})
    candidate_level = education.get("level", "none")
    candidate_rank = EDUCATION_RANK.get(candidate_level, 0)
    results: list[dict[str, Any]] = []
    degrees = [("phd", r"\b(?:ph\.?d\.?|doctorate|doctoral)\b"), ("masters", r"\bmaster'?s\b"), ("bachelors", r"\bbachelor'?s\b")]
    for kind, line in lines:
        for level, pattern in degrees:
            if not re.search(pattern, line, re.I):
                continue
            required_rank = EDUCATION_RANK[level]
            equivalent = bool(re.search(r"equivalent (?:experience|combination)", line, re.I))
            if candidate_rank >= required_rank or (equivalent and candidate_rank >= EDUCATION_RANK["bachelors"]):
                status = "match"
                hard = False
            else:
                status = "gap"
                hard = kind == "required" and not equivalent
            results.append(
                _result_item(
                    f"degree:{level}",
                    f"{level.title()} degree",
                    status,
                    f"Candidate record: {candidate_level} in {education.get('field', 'an unspecified field')}.",
                    education.get("evidence", ""),
                    hard,
                    kind,
                )
            )
            return results
    return results


def _evaluate_clearance_and_authorization(lines: list[tuple[str, str]], profile: dict[str, Any]) -> tuple[list[dict[str, Any]], list[str]]:
    results: list[dict[str, Any]] = []
    verification: list[str] = []
    for kind, line in lines:
        if kind != "required":
            continue
        if re.search(r"\b(?:active|current|must possess|requires?)\b.{0,40}\b(?:secret|top secret|ts/sci|security clearance)\b", line, re.I) or re.search(
            r"\b(?:secret|top secret|ts/sci) clearance\b.{0,30}\b(?:required|must)\b", line, re.I
        ):
            results.append(
                _result_item(
                    "clearance:active",
                    "active security clearance",
                    "gap",
                    "Posting requires an active clearance; candidate has only a lapsed Canadian Secret clearance and no US clearance.",
                    profile.get("clearance", {}).get("note", ""),
                    True,
                )
            )
        elif re.search(r"\b(?:ability|eligible|eligibility) to obtain\b.{0,40}\bclearance\b", line, re.I):
            verification.append("Clearance eligibility must be verified; the record does not establish US eligibility.")

        if re.search(r"\b(?:u\.?s\.? citizen|united states citizen|citizenship required)\b", line, re.I):
            verification.append("US citizenship requirement cannot be verified from the candidate record.")
        if re.search(r"\b(?:no sponsorship|unable to sponsor|without sponsorship)\b", line, re.I):
            verification.append("US work-authorization/sponsorship status is intentionally unknown in the candidate profile.")
    return results, sorted(set(verification))


def _evaluate_location(row: dict[str, Any], description: str, profile: dict[str, Any]) -> list[dict[str, Any]]:
    location_profile = profile.get("location", {})
    location = " ".join(
        _safe_text(row.get(key)) for key in ("location", "city", "state", "country") if _safe_text(row.get(key))
    )
    remote = _safe_text(row.get("is_remote")).lower() in {"true", "1", "yes"}
    remote = remote or bool(re.search(r"\b(?:fully remote|100% remote|remote within|remote position|remote role)\b", description[:1600], re.I))
    if remote and location_profile.get("remote_us", False):
        return [_result_item("location", "location", "match", "Remote US work is within the configured search boundary.")]

    allowed = any(_alias_pattern(marker).search(location) for marker in location_profile.get("onsite_states", []))
    if allowed:
        return [_result_item("location", "location", "match", f"{location or 'Michigan'} is within the configured onsite area.")]
    if location:
        return [
            _result_item(
                "location",
                "location",
                "gap",
                f"Posting location is {location}; candidate profile allows remote US or onsite work in Michigan and does not assume relocation.",
                "",
                True,
            )
        ]
    return [_result_item("location", "location", "partial", "Posting location/remote eligibility is not clear enough to verify.")]


def _unparsed_required_lines(lines: list[tuple[str, str]], profile: dict[str, Any]) -> list[str]:
    skills = profile.get("skills", {})
    unparsed: list[str] = []
    for kind, line in lines:
        if kind != "required" or len(line) < 16 or SOFT_REQUIREMENT.search(line):
            continue
        recognized = bool(
            YEAR_PATTERN.search(line)
            or re.search(r"\b(?:bachelor'?s|master'?s|ph\.?d\.?|doctorate|clearance|citizen|sponsorship)\b", line, re.I)
            or any(_has_alias(line, skill.get("aliases", [])) for skill in skills.values())
        )
        if not recognized:
            cleaned = re.sub(r"\s+", " ", line).strip(" -*")
            unparsed.append(f"Unparsed required item needs manual review: {cleaned[:180]}")
    return unparsed[:4]


def evaluate_qualifications(row: dict[str, Any], profile: dict[str, Any]) -> dict[str, Any]:
    description = clean_description(row.get("description"))
    status = description_status(description)
    lines = requirement_lines(description) if description else []
    if status == "thin" and len(lines) >= 3:
        status = "usable"
    location_results = _evaluate_location(row, description, profile)
    if status != "usable":
        matched = [item for item in location_results if item["status"] == "match"]
        partial = [item for item in location_results if item["status"] == "partial"]
        gaps = [item for item in location_results if item["status"] == "gap"]
        return {
            "description_status": status,
            "qualification_score": 0,
            "required_count": len(location_results),
            "substantive_required_count": 0,
            "matched": matched,
            "partial": partial,
            "gaps": gaps,
            "preferred_matches": [],
            "preferred_gaps": [],
            "hard_blockers": [f"{item['label']}: {item['detail']}" for item in gaps if item["hard"]],
            "verification_blockers": ["Full posting requirements were not available; qualification cannot be assessed."],
        }

    year_results, year_scopes = _evaluate_year_requirements(lines, profile)
    results = year_results
    results.extend(_evaluate_skill_requirements(lines, profile, year_scopes))
    results.extend(_evaluate_degree(lines, profile))
    clearance_results, verification = _evaluate_clearance_and_authorization(lines, profile)
    verification.extend(_unparsed_required_lines(lines, profile))
    results.extend(clearance_results)
    results.extend(location_results)

    unique: dict[str, dict[str, Any]] = {}
    status_rank = {"match": 0, "partial": 1, "gap": 2}
    for item in results:
        existing = unique.get(item["key"])
        if existing is None or (item["hard"], status_rank[item["status"]]) > (existing["hard"], status_rank[existing["status"]]):
            unique[item["key"]] = item
    results = list(unique.values())

    required = [item for item in results if item["kind"] == "required"]
    scored_required = [item for item in required if item["key"] != "location"]
    preferred = [item for item in results if item["kind"] == "preferred"]
    matched = [item for item in required if item["status"] == "match"]
    partial = [item for item in required if item["status"] == "partial"]
    gaps = [item for item in required if item["status"] == "gap"]
    preferred_matches = [item for item in preferred if item["status"] in {"match", "partial"}]
    preferred_gaps = [item for item in preferred if item["status"] == "gap"]
    hard_blockers = [f"{item['label']}: {item['detail']}" for item in gaps if item["hard"]]
    required_count = len(required)
    substantive_required_count = len(scored_required)
    scored_matched = [item for item in scored_required if item["status"] == "match"]
    scored_partial = [item for item in scored_required if item["status"] == "partial"]
    score = round(100 * (len(scored_matched) + 0.5 * len(scored_partial)) / substantive_required_count) if substantive_required_count else 0
    if substantive_required_count < 2:
        verification.append("Too few explicit requirements were extracted to support a qualification decision.")
        score = 0
    elif verification:
        score = min(score, 70)

    return {
        "description_status": status,
        "qualification_score": score,
        "required_count": required_count,
        "substantive_required_count": substantive_required_count,
        "matched": matched,
        "partial": partial,
        "gaps": gaps,
        "preferred_matches": preferred_matches,
        "preferred_gaps": preferred_gaps,
        "hard_blockers": sorted(set(hard_blockers)),
        "verification_blockers": sorted(set(verification)),
    }


def qualification_recommendation(
    relevance_score: int, rejected: bool, result: dict[str, Any], role_focus: str = "explicit"
) -> str:
    if rejected or result["hard_blockers"]:
        return "skip"
    if result["description_status"] != "usable" or result.get("substantive_required_count", 0) < 2 or result["verification_blockers"]:
        return "unverified"
    score = result["qualification_score"]
    if role_focus != "explicit" and score >= 75:
        return "review"
    if score >= 75 and relevance_score >= 5:
        return "apply_first"
    if score >= 55:
        return "review"
    return "stretch"


def summarize_items(items: list[dict[str, Any]], limit: int = 4) -> str:
    if not items:
        return "None"
    values = []
    for item in items[:limit]:
        value = item["label"]
        if item.get("status") != "match":
            value = f"{value}: {item['detail']}"
        values.append(value)
    if len(items) > limit:
        values.append(f"+{len(items) - limit} more")
    return "; ".join(values)
