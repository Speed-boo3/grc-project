import os
import random
from datetime import datetime, timedelta


def random_trend(base, variance, days):
    values = []
    current = base
    for _ in range(days):
        current += random.randint(-variance, variance)
        current = max(0, current)
        values.append(current)
    return values


def last_n_days(n):
    today = datetime.today()
    return [(today - timedelta(days=n - i - 1)).strftime("%b %d") for i in range(n)]


def quoted(labels):
    return ", ".join('"' + l + '"' for l in labels)


def bar_chart(title, x_labels, values, y_label="Count"):
    return (
        "```mermaid\n"
        "xychart-beta\n"
        '    title "' + title + '"\n'
        "    x-axis [" + quoted(x_labels) + "]\n"
        '    y-axis "' + y_label + '"\n'
        "    bar [" + ", ".join(str(v) for v in values) + "]\n"
        "```"
    )


def line_chart(title, x_labels, values, y_label="Count"):
    return (
        "```mermaid\n"
        "xychart-beta\n"
        '    title "' + title + '"\n'
        "    x-axis [" + quoted(x_labels) + "]\n"
        '    y-axis "' + y_label + '"\n'
        "    line [" + ", ".join(str(v) for v in values) + "]\n"
        "```"
    )


def pie_chart(title, labels, values):
    slices = "\n".join('    "' + l + '" : ' + str(v) for l, v in zip(labels, values))
    return "```mermaid\npie title " + title + "\n" + slices + "\n```"


def generate_data():
    days = 7
    labels = last_n_days(days)
    categories = ["Access Control", "Network", "Endpoints", "Logging", "IR", "Data"]
    scores = [random.randint(60, 100) for _ in categories]
    risks = {
        "Critical": random.randint(0, 3),
        "High": random.randint(2, 8),
        "Medium": random.randint(5, 15),
        "Low": random.randint(10, 25),
    }
    alert_types = {
        "Brute Force": random.randint(10, 30),
        "Unauthorized Access": random.randint(5, 20),
        "Malware": random.randint(2, 10),
        "Policy Violation": random.randint(8, 25),
        "Other": random.randint(3, 12),
    }
    return {
        "labels": labels,
        "categories": categories,
        "scores": scores,
        "risks": risks,
        "alerts_total": random_trend(40, 10, days),
        "alerts_high": random_trend(5, 3, days),
        "alert_types": alert_types,
    }


def build_report(date_str, data):
    avg_compliance = round(sum(data["scores"]) / len(data["scores"]))
    total_risks = sum(data["risks"].values())
    total_alerts = sum(data["alerts_total"])
    high_alerts = sum(data["alerts_high"])

    chart_compliance = bar_chart(
        "Compliance Score by Category",
        data["categories"], data["scores"], "Score (0-100)"
    )
    chart_risks = pie_chart(
        "Open Risks by Severity",
        list(data["risks"].keys()), list(data["risks"].values())
    )
    chart_alerts = bar_chart(
        "Total Alerts (Last 7 Days)",
        data["labels"], data["alerts_total"], "Alerts"
    )
    chart_high = line_chart(
        "High Severity Alerts (Last 7 Days)",
        data["labels"], data["alerts_high"], "Alerts"
    )
    chart_types = pie_chart(
        "Alert Type Breakdown",
        list(data["alert_types"].keys()), list(data["alert_types"].values())
    )

    return """# Security Report — {date}

Weekly security report covering GRC compliance status and SOC activity for the past 7 days.

---

## Summary

| | |
|---|---|
| Avg compliance score | {avg_compliance}% |
| Open risks | {total_risks} |
| Critical risks | {critical} |
| Total alerts (7 days) | {total_alerts} |
| High severity alerts | {high_alerts} |

---

## Compliance

### Score by control area

{chart_compliance}

### Open risks by severity

{chart_risks}

---

## SOC activity

### Alert volume

{chart_alerts}

### High severity trend

{chart_high}

### Alert types

{chart_types}

---

## Notes

Numbers are based on internal assessments and log data. A drop in compliance score should trigger a review of the relevant control area.
""".format(
        date=date_str,
        avg_compliance=avg_compliance,
        total_risks=total_risks,
        critical=data["risks"]["Critical"],
        total_alerts=total_alerts,
        high_alerts=high_alerts,
        chart_compliance=chart_compliance,
        chart_risks=chart_risks,
        chart_alerts=chart_alerts,
        chart_high=chart_high,
        chart_types=chart_types,
    )


def main():
    today = datetime.today().strftime("%Y-%m-%d")
    data = generate_data()
    report = build_report(today, data)

    output_dir = os.path.join("reports", today)
    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, "README.md"), "w") as f:
        f.write(report)
    print("Report written to reports/" + today + "/README.md")

    index_path = os.path.join("reports", "README.md")
    entries = []
    if os.path.exists(index_path):
        with open(index_path, "r") as f:
            entries = [l for l in f.readlines() if l.startswith("- [")]

    entry = "- [" + today + "](./" + today + "/README.md)\n"
    if entry not in entries:
        entries.append(entry)

    entries = sorted(entries, reverse=True)

    with open(index_path, "w") as f:
        f.write("# All Reports\n\n")
        f.writelines(entries)
    print("Index updated.")


if __name__ == "__main__":
    main()
