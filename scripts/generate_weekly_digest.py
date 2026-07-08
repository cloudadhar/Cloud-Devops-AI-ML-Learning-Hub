#!/usr/bin/env python3
"""Generate a weekly learner-focused technology digest from public feeds.

The script uses only Python standard-library modules so it can run reliably in
GitHub Actions without dependency installation.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import ssl
import sys
import textwrap
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "data" / "weekly-update-sources.json"
OUT_DIR = ROOT / "docs" / "weekly-updates"

FOCUS_RULES = [
    ("AWS", ["aws", "amazon", "ec2", "s3", "lambda", "eks", "ecs", "rds", "dynamodb", "sagemaker", "bedrock"]),
    ("Azure", ["azure", "aks", "entra", "fabric", "defender", "sentinel", "app service", "cosmos", "azure devops"]),
    ("Google Cloud", ["google cloud", "gcp", "gke", "cloud run", "bigquery", "vertex", "gemini", "artifact registry"]),
    ("GitHub and DevOps", ["github", "actions", "copilot", "pull request", "workflow", "devops", "ci/cd", "runner"]),
    ("Containers and Kubernetes", ["kubernetes", "docker", "container", "helm", "pod", "cluster", "ingress", "gateway api"]),
    ("IaC and Automation", ["terraform", "opentofu", "ansible", "infrastructure as code", "iac", "automation", "provider"]),
    ("Observability", ["grafana", "prometheus", "opentelemetry", "logging", "metrics", "tracing", "alert", "dashboard"]),
    ("Security", ["security", "vulnerability", "cve", "identity", "iam", "secret", "zero trust", "policy", "sast", "supply chain"]),
    ("AI / ML / MLOps", ["ai", "machine learning", "ml", "model", "llm", "agent", "rag", "embedding", "sagemaker", "vertex", "copilot"]),
]

LEARNER_ACTIONS = {
    "AWS": "Review IAM, cost impact, region availability, and how the service fits EC2/EKS/Lambda/S3 projects.",
    "Azure": "Map the update to subscriptions, RBAC, AKS/App Service, Azure Monitor, and cost controls.",
    "Google Cloud": "Connect the update to projects, IAM, Cloud Run/GKE, Artifact Registry, and Cloud Operations.",
    "GitHub and DevOps": "Check whether workflows, branch protection, pull requests, runners, or release automation should be improved.",
    "Containers and Kubernetes": "Practice the change with Docker, kubectl, Helm, ingress, probes, and rollback thinking.",
    "IaC and Automation": "Think in Terraform/OpenTofu modules, state, plan review, drift, and safe rollback.",
    "Observability": "Ask what metrics, logs, traces, dashboards, and alerts would prove the system is healthy.",
    "Security": "Check secrets, identity, least privilege, dependency risk, image risk, and audit logs.",
    "AI / ML / MLOps": "Focus on model/API quality, evaluation, observability, cost, data safety, and responsible usage.",
    "Cloud Native": "Connect the update to Kubernetes, platform engineering, CNCF projects, reliability, and production operations.",
    "Azure and DevOps": "Map the update to Azure DevOps, Git workflows, enterprise authentication, and release safety.",
    "General": "Read the release note, identify the affected tool, and write one small lab or interview answer from it.",
}

@dataclass
class Item:
    title: str
    link: str
    published: datetime | None
    summary: str
    source: str
    source_area: str
    focus: str


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def parse_date(value: str | None) -> datetime | None:
    if not value:
        return None
    value = value.strip()
    try:
        dt = parsedate_to_datetime(value)
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except Exception:
        pass
    for candidate in (value, value.replace("Z", "+00:00")):
        try:
            dt = datetime.fromisoformat(candidate)
            return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
        except Exception:
            continue
    return None


def fetch_url(url: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "CloudAdhar-Weekly-Learner-Digest/1.0 (+https://github.com/cloudadhar/Cloud-Devops-AI-ML-Learning-Hub)",
            "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            return response.read()
    except urllib.error.URLError as exc:
        # Some local Python/macOS installs do not have a working CA bundle.
        # GitHub-hosted runners normally do, but this fallback keeps manual
        # generation usable for public feeds without adding dependencies.
        if "CERTIFICATE_VERIFY_FAILED" not in str(exc):
            raise
        context = ssl._create_unverified_context()
        with urllib.request.urlopen(request, timeout=25, context=context) as response:
            return response.read()


def ns_tag(element: ET.Element, local: str) -> str:
    if element.tag.startswith("{"):
        ns = element.tag.split("}")[0][1:]
        return f"{{{ns}}}{local}"
    return local


def first_text(parent: ET.Element, names: Iterable[str]) -> str:
    for name in names:
        found = parent.find(name)
        if found is not None and found.text:
            return found.text
    return ""


def parse_feed(xml_bytes: bytes, source: dict) -> list[Item]:
    root = ET.fromstring(xml_bytes)
    items: list[Item] = []
    source_name = source["name"]
    source_area = source["area"]

    if root.tag.endswith("rss") or root.find("channel") is not None:
        channel = root.find("channel")
        if channel is None:
            return []
        for node in channel.findall("item"):
            title = clean_text(first_text(node, ["title"]))
            link = clean_text(first_text(node, ["link", "guid"]))
            published = parse_date(first_text(node, ["pubDate", "date", "updated"]))
            summary = clean_text(first_text(node, ["description", "summary", "content:encoded"]))
            items.append(Item(title, link, published, summary, source_name, source_area, "General"))
        return items

    entry_tag = ns_tag(root, "entry")
    title_tag = ns_tag(root, "title")
    updated_tag = ns_tag(root, "updated")
    published_tag = ns_tag(root, "published")
    summary_tag = ns_tag(root, "summary")
    content_tag = ns_tag(root, "content")
    link_tag = ns_tag(root, "link")
    for node in root.findall(entry_tag):
        title = clean_text(first_text(node, [title_tag, "title"]))
        link = ""
        for link_node in node.findall(link_tag):
            if link_node.attrib.get("href"):
                link = link_node.attrib["href"]
                break
        if not link:
            link = clean_text(first_text(node, ["link"]))
        published = parse_date(first_text(node, [published_tag, updated_tag, "published", "updated"]))
        summary = clean_text(first_text(node, [summary_tag, content_tag, "summary", "content"]))
        items.append(Item(title, link, published, summary, source_name, source_area, "General"))
    return items


def classify(item: Item) -> str:
    source_priority = {
        "AWS",
        "Azure",
        "Google Cloud",
        "GitHub and DevOps",
        "Azure and DevOps",
        "Containers and Kubernetes",
        "IaC and Automation",
        "Observability",
    }
    if item.source_area in source_priority:
        return item.source_area

    text = f"{item.source_area} {item.source} {item.title} {item.summary}".lower()
    for focus, keywords in FOCUS_RULES:
        if any(keyword in text for keyword in keywords):
            return focus
    return item.source_area if item.source_area else "General"


def learner_task(item: Item) -> str:
    focus = item.focus or "General"
    if focus == "AWS":
        return "Create a mini note covering affected AWS service, IAM impact, cost impact, region impact, and one cleanup step."
    if focus == "Azure":
        return "Map this to Azure identity, resource groups, monitoring, pricing, and one hands-on Azure lab idea."
    if focus == "Google Cloud":
        return "Map this to GCP projects, service accounts, networking, deployment option, and one Cloud Run or GKE lab idea."
    if focus in {"GitHub and DevOps", "Azure and DevOps"}:
        return "Write where this fits in a CI/CD workflow and one interview question about release safety or collaboration."
    if focus == "Containers and Kubernetes":
        return "Turn this into a kubectl, Docker, Helm, ingress, rollback, or troubleshooting practice task."
    if focus == "IaC and Automation":
        return "Write the Terraform/OpenTofu state, plan, module, drift, and rollback angle for this update."
    if focus == "Observability":
        return "Define one metric, one log, one trace, and one alert that would prove this is working."
    if focus == "Security":
        return "Identify the risk, the control, where it belongs in CI/CD, and one validation command or checklist item."
    if focus == "AI / ML / MLOps":
        return "Connect this to AI API quality, evaluation, observability, data safety, latency, and cost."
    if focus == "Cloud Native":
        return "Connect this to CNCF tools, platform engineering, reliability, Kubernetes operations, and one lab idea."
    return "Read the source note, identify what changed, and create one learner note plus one interview question."


def render_digest(items: list[Item], errors: list[str], generated_at: datetime, window_days: int) -> str:
    date_slug = generated_at.strftime("%Y-%m-%d")
    lines: list[str] = []
    lines.append(f"# Weekly Learner Tech Digest - {date_slug}")
    lines.append("")
    lines.append(f"Generated on {generated_at.strftime('%Y-%m-%d %H:%M UTC')} from official or maintained public feeds.")
    lines.append("")
    lines.append(f"Lookback window: last {window_days} days.")
    lines.append("")
    lines.append("## How Learners Should Use This")
    lines.append("")
    lines.append("1. Pick one focus area for the week.")
    lines.append("2. Read 2-3 linked updates from that area.")
    lines.append("3. Write a short note: what changed, why it matters, and one command/lab to practice.")
    lines.append("4. Add one interview question from the update.")
    lines.append("5. Update your GitHub project or learning log.")
    lines.append("")

    grouped: dict[str, list[Item]] = {}
    for item in items:
        grouped.setdefault(item.focus, []).append(item)

    lines.append("## This Week Focus Plan")
    lines.append("")
    if grouped:
        for focus in sorted(grouped):
            count = len(grouped[focus])
            lines.append(f"- **{focus}** ({count} updates): {LEARNER_ACTIONS.get(focus, LEARNER_ACTIONS['General'])}")
    else:
        lines.append("- No recent feed entries were collected. Use the evergreen focus plan in `docs/weekly-practice-plan.md`.")
    lines.append("")

    lines.append("## Updates by Focus Area")
    lines.append("")
    if not grouped:
        lines.append("No update items were collected this run.")
        lines.append("")
    for focus in sorted(grouped):
        lines.append(f"### {focus}")
        lines.append("")
        for item in sorted(grouped[focus], key=lambda x: x.published or datetime.min.replace(tzinfo=timezone.utc), reverse=True):
            date = item.published.strftime("%Y-%m-%d") if item.published else "date unknown"
            title = item.title or "Untitled update"
            link = item.link or "#"
            lines.append(f"- [{title}]({link})")
            lines.append(f"  - Source: {item.source} | Published: {date}")
            lines.append(f"  - What to learn: {LEARNER_ACTIONS.get(item.focus, LEARNER_ACTIONS['General'])}")
            lines.append(f"  - Learner task: {learner_task(item)}")
        lines.append("")

    lines.append("## Suggested Interview Practice")
    lines.append("")
    lines.append("- Pick one cloud update and explain its impact on cost, IAM, networking, and operations.")
    lines.append("- Pick one DevOps update and explain where it fits in a CI/CD pipeline.")
    lines.append("- Pick one Kubernetes or container update and explain how you would test it safely.")
    lines.append("- Pick one security update and explain the risk it reduces.")
    lines.append("- Pick one AI/MLOps update and explain how you would monitor quality, latency, and cost.")
    lines.append("")

    if errors:
        lines.append("## Feed Warnings")
        lines.append("")
        lines.append("These feeds failed during this run. The workflow skips failures so the weekly digest can still be generated.")
        lines.append("")
        for error in errors:
            lines.append(f"- {error}")
        lines.append("")

    lines.append("## Source Feeds")
    lines.append("")
    lines.append("Source feed configuration lives in `data/weekly-update-sources.json`.")
    lines.append("")
    return "\n".join(lines)


def update_index(generated_at: datetime) -> None:
    files = sorted(OUT_DIR.glob("20*.md"), reverse=True)
    lines = [
        "# Weekly Learner Tech Updates",
        "",
        "This folder is generated by `.github/workflows/weekly-learner-digest.yml`.",
        "",
        "- [Latest Digest](latest.md)",
        "",
        "## Archive",
        "",
    ]
    for path in files[:30]:
        lines.append(f"- [{path.stem}]({path.name})")
    lines.append("")
    (OUT_DIR / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=str(CONFIG_PATH))
    parser.add_argument("--days", type=int, default=None)
    parser.add_argument("--max-items", type=int, default=None)
    args = parser.parse_args()

    config = json.loads(Path(args.config).read_text(encoding="utf-8"))
    window_days = args.days or int(config.get("window_days", 10))
    max_items_per_source = int(config.get("max_items_per_source", 8))
    max_items_total = args.max_items or int(config.get("max_items_total", 80))
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=window_days)

    all_items: list[Item] = []
    errors: list[str] = []
    seen: set[str] = set()

    for source in config["sources"]:
        try:
            parsed = parse_feed(fetch_url(source["url"]), source)
        except (urllib.error.URLError, TimeoutError, ET.ParseError, ValueError) as exc:
            errors.append(f"{source['name']}: {exc}")
            continue
        kept = 0
        for item in parsed:
            if item.published and item.published < cutoff:
                continue
            key = (item.link or item.title).strip().lower()
            if not key or key in seen:
                continue
            seen.add(key)
            item.focus = classify(item)
            all_items.append(item)
            kept += 1
            if kept >= max_items_per_source:
                break

    all_items.sort(key=lambda x: x.published or datetime.min.replace(tzinfo=timezone.utc), reverse=True)
    all_items = all_items[:max_items_total]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    digest = render_digest(all_items, errors, now, window_days)
    dated = OUT_DIR / f"{now.strftime('%Y-%m-%d')}.md"
    latest = OUT_DIR / "latest.md"
    dated.write_text(digest, encoding="utf-8")
    latest.write_text(digest, encoding="utf-8")
    update_index(now)

    print(f"Generated {dated.relative_to(ROOT)} with {len(all_items)} items and {len(errors)} feed warnings.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
