"""Generate review-only job-alert plans and temporary DevTools overlays.

This program does not access Gmail, a browser, or a job board. Gmail MCP supplies
the minimal inventory capture; a human performs every account change.
"""
from __future__ import annotations

import argparse
import html
import json
import re
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PROFILE_FILE = Path(__file__).with_name("alert_cleanup_profile.json")
OUTPUT_DIR = Path(__file__).with_name("output")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def sender_domain(sender: str) -> str:
    match = re.search(r"@([A-Za-z0-9.-]+)", sender)
    return match.group(1).lower() if match else ""


def platform_for(sender: str, profile: dict[str, Any]) -> str:
    domain = sender_domain(sender)
    for platform, details in profile["platforms"].items():
        if any(domain == item or domain.endswith("." + item) for item in details["sender_domains"]):
            return platform
    return "other"


def classify_subject(subject: str, profile: dict[str, Any]) -> str:
    lower = subject.lower()
    if any(pattern in lower for pattern in profile["legacy_patterns"]):
        return "legacy"
    aligned = ("forward deployed", "applied ai", "agentic ai", "llm", "rag", "ai integration", "ai implementation")
    return "aligned" if any(term in lower for term in aligned) else "unclear"


def build_plan(inventory: dict[str, Any], profile: dict[str, Any]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for message in inventory.get("messages", []):
        platform = platform_for(str(message.get("from", "")), profile)
        if platform != "other":
            grouped[platform].append(message)
    plan = []
    for platform in profile["platforms"]:
        messages = grouped.get(platform, [])
        categories = {classify_subject(str(message.get("subject", "")), profile) for message in messages}
        status = "not_observed" if not messages else "replace_legacy" if "legacy" in categories else "retune" if "aligned" in categories else "review"
        plan.append({"platform": platform, "status": status, "observed_messages": len(messages), "sample_subjects": [str(item.get("subject", "")) for item in messages[:3]]})
    return plan


def target_steps(profile: dict[str, Any]) -> list[str]:
    return [
        f"Upload {profile['resume_path']} if the current resume is not already stored.",
        "Configure remote roles worldwide and onsite roles in Canada or the United States.",
        *[f"Create alert: {item['label']} — query: {item['query']}" for item in profile["target_alerts"]],
        "Review the resulting alert before saving; platform query syntax and filters vary.",
    ]


def render_markdown(run_date: str, plan: list[dict[str, Any]], profile: dict[str, Any]) -> str:
    lines = [f"# Job-Alert Cleanup Plan - {run_date}", "", "Review-only output from a Gmail MCP inventory capture. It does not alter Gmail or job-board accounts.", "", "## Target policy", "", "- Remote: worldwide", "- Onsite: Canada and the United States", f"- Resume: `{profile['resume_path']}`", "", "## Platform actions", ""]
    for item in plan:
        lines.extend([f"### {item['platform'].title()} — {item['status'].replace('_', ' ')}", "", f"- Observed messages: {item['observed_messages']}"])
        if item["sample_subjects"]:
            lines.append("- Samples:")
            lines.extend(f"  - {subject}" for subject in item["sample_subjects"])
        lines.extend(["- Manual steps:", *[f"  - {step}" for step in target_steps(profile)], ""])
    return "\n".join(lines)


def render_overlay(plan: list[dict[str, Any]], profile: dict[str, Any]) -> str:
    cards = "".join(f"<li><strong>{html.escape(item['platform'].title())}</strong>: {html.escape(item['status'].replace('_', ' '))} ({item['observed_messages']} observed)</li>" for item in plan)
    steps = "".join(f"<li>{html.escape(step)}</li>" for step in target_steps(profile))
    return f"""(() => {{
  document.getElementById('dorian-alert-guide')?.remove();
  const guide = document.createElement('aside');
  guide.id = 'dorian-alert-guide';
  guide.innerHTML = `<button aria-label="Close guide" style="float:right;border:0;background:none;font-size:20px;cursor:pointer">×</button><h2>Job-alert cleanup guide</h2><p><strong>Temporary overlay.</strong> Review changes before saving.</p><h3>Current platform plan</h3><ul>{cards}</ul><h3>Next steps</h3><ol>{steps}</ol>`;
  Object.assign(guide.style, {{position:'fixed',top:'16px',right:'16px',zIndex:'2147483647',width:'390px',maxHeight:'calc(100vh - 32px)',overflow:'auto',padding:'18px',background:'#102a43',color:'#f0f7ff',border:'2px solid #38bdf8',borderRadius:'12px',boxShadow:'0 16px 40px rgba(0,0,0,.35)',font:'14px/1.45 system-ui,sans-serif'}});
  guide.querySelector('button').onclick = () => guide.remove();
  document.body.append(guide);
}})();
"""


def command_plan(args: argparse.Namespace) -> None:
    profile = load_json(PROFILE_FILE)
    plan = build_plan(load_json(Path(args.input)), profile)
    run_date = args.run_date or date.today().isoformat()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    markdown = OUTPUT_DIR / f"job_alert_cleanup_plan_{run_date}.md"
    overlay = OUTPUT_DIR / f"job_alert_cleanup_overlay_{run_date}.js"
    markdown.write_text(render_markdown(run_date, plan, profile), encoding="utf-8")
    overlay.write_text(render_overlay(plan, profile), encoding="utf-8")
    print(f"Plan: {markdown}\nOverlay: {overlay}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(required=True)
    plan = commands.add_parser("plan", help="generate artifacts from a Gmail MCP inventory")
    plan.add_argument("--input", required=True, help="minimal inventory JSON following alert_inventory_schema.json")
    plan.add_argument("--run-date", help="YYYY-MM-DD for reproducible output names")
    plan.set_defaults(func=command_plan)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
