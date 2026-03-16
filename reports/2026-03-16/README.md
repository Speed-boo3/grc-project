# Security Report — 2026-03-16

Weekly security report covering GRC compliance status and SOC activity for the past 7 days.

---

## Summary

| | |
|---|---|
| Avg compliance score | 72% |
| Open risks | 42 |
| Critical risks | 0 |
| Total alerts (7 days) | 279 |
| High severity alerts | 66 |

---

## Compliance

### Score by control area

```mermaid
xychart-beta
    title "Compliance Score by Category"
    x-axis ["Access Control", "Network", "Endpoints", "Logging", "IR", "Data"]
    y-axis "Score (0-100)"
    bar [64, 70, 73, 65, 94, 63]
```

### Open risks by severity

```mermaid
pie title Open Risks by Severity
    "Critical" : 0
    "High" : 3
    "Medium" : 14
    "Low" : 25
```

---

## SOC activity

### Alert volume

```mermaid
xychart-beta
    title "Total Alerts (Last 7 Days)"
    x-axis ["Mar 10", "Mar 11", "Mar 12", "Mar 13", "Mar 14", "Mar 15", "Mar 16"]
    y-axis "Alerts"
    bar [43, 33, 35, 35, 39, 46, 48]
```

### High severity trend

```mermaid
xychart-beta
    title "High Severity Alerts (Last 7 Days)"
    x-axis ["Mar 10", "Mar 11", "Mar 12", "Mar 13", "Mar 14", "Mar 15", "Mar 16"]
    y-axis "Alerts"
    line [8, 7, 8, 9, 12, 10, 12]
```

### Alert types

```mermaid
pie title Alert Type Breakdown
    "Brute Force" : 15
    "Unauthorized Access" : 6
    "Malware" : 7
    "Policy Violation" : 22
    "Other" : 9
```

---

## Notes

Numbers are based on internal assessments and log data. A drop in compliance score should trigger a review of the relevant control area.
