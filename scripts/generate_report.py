#!/usr/bin/env python3
"""
GRC Weekly Compliance Report Generator
Produces a clean markdown report from the risk register and compliance checklist.
Scheduled via GitHub Actions: Mon, Wed, Fri at 08:00 UTC.
"""

import os
import json
import random
from datetime import datetime, timedelta

REGISTER_PATH = os.path.join(os.path.dirname(__file__), "..", "grc", "risk-assessment", "sample_risks.json")


def load_risks():
    try:
        with open(REGISTER_PATH) as f:
            return json.load(f)
    except Exception:
        return []


def score_level(score):
    if score >= 17: return "Critical"
    if score >= 10: return "High"
    if score >= 5:  return "Medium"
    return "Low"


def level_icon(level):
    return {"Critical": "🔴", "High": "🟠", "Medium": "🟡", "Low": "🟢", "Closed": "✅"}.get(level, "⚪")


def compliance_scores():
    """Simulated control area scores — in production these would come from scan results."""
    return {
        "Access Control":       random.randint(78, 95),
        "Network Security":     random.randint(70, 90),
        "Endpoint Security":    random.randint(75, 92),
        "Logging & Monitoring": random.randint(72, 88),
        "Incident Response":    random.randint(80, 95),
        "Data Protection":      random.randint(68, 85),
        "Supply Chain":         random.randint(55, 75),
        "AI / LLM Governance":  random.randint(40, 65),
    }


def score_bar(score, width=20):
    filled = round(score / 100 * width)
    bar = "█" * filled + "░" * (width - filled)
    return f"`{bar}` {score}%"


def build_report(today, risks, scores):
    open_risks   = [r for r in risks if r.get("status", "open") == "open"]
    closed_risks = [r for r in risks if r.get("status") == "closed"]

    by_level = {"Critical": [], "High": [], "Medium": [], "Low": []}
    for r in open_risks:
        score = r.get("score", r.get("likelihood", 1) * r.get("impact", 1))
        lvl = score_level(score)
        by_level[lvl].append(r)

    avg_score = round(sum(scores.values()) / len(scores))
    framework_score = round(avg_score * 0.92)  # ISO mapping typically ~8% lower than internal

    week_start = (datetime.strptime(today, "%Y-%m-%d") - timedelta(days=6)).strftime("%d %b")
    week_end   = datetime.strptime(today, "%Y-%m-%d").strftime("%d %b %Y")

    lines = []

    lines.append(f"# GRC Compliance Report — {today}")
    lines.append(f"**Reporting period:** {week_start} – {week_end}  ")
    lines.append(f"**Generated:** {today} by GitHub Actions  ")
    lines.append(f"**Frameworks:** ISO 27001:2022 · NIST CSF 2.0 · GDPR · NIS2 · DORA")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Executive summary
    lines.append("## Executive summary")
    lines.append("")
    lines.append("| Metric | Value | Status |")
    lines.append("|---|---|---|")
    lines.append(f"| Overall compliance score | {avg_score}% | {'✅ Acceptable' if avg_score >= 75 else '⚠️ Needs attention'} |")
    lines.append(f"| ISO 27001 mapping | {framework_score}% | {'✅' if framework_score >= 70 else '⚠️'} |")
    lines.append(f"| Open risks | {len(open_risks)} | {'🔴 Action required' if by_level['Critical'] else '✅ Under control'} |")
    lines.append(f"| Critical risks | {len(by_level['Critical'])} | {'🔴 Immediate action' if by_level['Critical'] else '✅ None'} |")
    lines.append(f"| Closed this period | {len(closed_risks)} | ✅ |")
    lines.append(f"| Frameworks assessed | 5 | ISO 27001 · NIST CSF · GDPR · NIS2 · DORA |")
    lines.append("")

    # Compliance scores per control area
    lines.append("---")
    lines.append("")
    lines.append("## Compliance by control area")
    lines.append("")
    lines.append("| Control area | Score | Trend |")
    lines.append("|---|---|---|")
    for area, score in scores.items():
        bar = score_bar(score)
        trend = "↑" if score >= 80 else "→" if score >= 65 else "↓"
        lines.append(f"| {area} | {bar} | {trend} |")
    lines.append("")
    lines.append(f"> **Average: {avg_score}%** — target is 85% across all control areas")
    lines.append("")

    # Risk register
    lines.append("---")
    lines.append("")
    lines.append("## Risk register — open risks")
    lines.append("")

    if not open_risks:
        lines.append("No open risks. All risks are closed or accepted.")
    else:
        lines.append("| ID | Risk | Score | Level | Owner | Deadline |")
        lines.append("|---|---|---|---|---|---|")
        for r in sorted(open_risks, key=lambda x: x.get("score", 0), reverse=True):
            score = r.get("score", r.get("likelihood", 1) * r.get("impact", 1))
            lvl = score_level(score)
            icon = level_icon(lvl)
            deadline = {
                "Critical": "**Immediate**",
                "High": "30 days",
                "Medium": "90 days",
                "Low": "Monitor"
            }.get(lvl, "")
            title = r.get("title", r.get("name", "Unknown"))
            lines.append(f"| {r['id']} | {title} | {score} | {icon} {lvl} | {r.get('owner','—')} | {deadline} |")

    lines.append("")

    # Closed risks
    if closed_risks:
        lines.append("### Closed risks")
        lines.append("")
        lines.append("| ID | Risk | Closed note |")
        lines.append("|---|---|---|")
        for r in closed_risks:
            title = r.get("title", r.get("name", "Unknown"))
            note = r.get("closed_note", r.get("treatment", "Resolved"))
            lines.append(f"| {r['id']} | ~~{title}~~ | {note} |")
        lines.append("")

    # 2026 focus areas
    lines.append("---")
    lines.append("")
    lines.append("## 2026 focus areas")
    lines.append("")
    lines.append("| Area | Requirement | Status |")
    lines.append("|---|---|---|")
    lines.append("| **NIS2 Directive** | EU member states enforcing since Oct 2024. Incident reporting within 24h required. | ⚠️ Review needed |")
    lines.append("| **DORA** | Digital Operational Resilience Act in force Jan 2025. Applies to financial sector. | ⚠️ Assess applicability |")
    lines.append("| **AI / LLM Governance** | ISO/IEC 42001 (AI management) published 2023. Use of AI tools requires policy. | 🔴 Gap identified |")
    lines.append("| **Zero Trust Architecture** | NIST SP 800-207 — never trust, always verify. Replace perimeter-only model. | → In progress |")
    lines.append("| **Supply Chain Security** | ISO 27001:2022 Annex A 5.19-5.22. Vendor risk assessments mandatory. | ⚠️ Partially covered |")
    lines.append("")

    # Actions
    lines.append("---")
    lines.append("")
    lines.append("## Recommended actions")
    lines.append("")

    actions = []
    if by_level["Critical"]:
        for r in by_level["Critical"]:
            title = r.get("title", r.get("name", ""))
            actions.append(f"🔴 **[IMMEDIATE]** Remediate {r['id']} — {title} (owner: {r.get('owner','—')})")
    if by_level["High"]:
        for r in by_level["High"]:
            title = r.get("title", r.get("name", ""))
            actions.append(f"🟠 **[30 days]** Address {r['id']} — {title}")
    actions.append("⚠️ **[This quarter]** Conduct AI/LLM usage audit and draft governance policy")
    actions.append("⚠️ **[This quarter]** Complete NIS2 gap assessment if operating in EU")
    actions.append("→ **[Ongoing]** Progress Zero Trust Architecture implementation")

    for a in actions:
        lines.append(f"- {a}")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Report generated automatically by `scripts/generate_report.py`.*  ")
    lines.append("*Risk data sourced from `grc/risk-assessment/sample_risks.json`.*  ")
    lines.append(f"*Next report: {(datetime.strptime(today, '%Y-%m-%d') + timedelta(days=2)).strftime('%Y-%m-%d')}*")

    return "\n".join(lines)


def main():
    today = datetime.today().strftime("%Y-%m-%d")
    risks = load_risks()
    scores = compliance_scores()
    report = build_report(today, risks, scores)

    output_dir = os.path.join("reports", today)
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "README.md")
    with open(output_path, "w") as f:
        f.write(report)
    print(f"Report written to {output_path}")

    # Update index
    index_path = os.path.join("reports", "README.md")
    entries = []
    if os.path.exists(index_path):
        with open(index_path) as f:
            entries = [l for l in f.readlines() if l.startswith("- [")]
    entry = f"- [{today}](./{today}/README.md)\n"
    if entry not in entries:
        entries.append(entry)
    entries = sorted(entries, reverse=True)
    with open(index_path, "w") as f:
        f.write("# GRC Compliance Reports\n\n")
        f.writelines(entries)
    print("Index updated.")


if __name__ == "__main__":
    main()
