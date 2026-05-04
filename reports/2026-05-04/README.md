# GRC Compliance Report — 2026-05-04
**Reporting period:** 28 Apr – 04 May 2026  
**Generated:** 2026-05-04 by GitHub Actions  
**Frameworks:** ISO 27001:2022 · NIST CSF 2.0 · GDPR · NIS2 · DORA

---

## Executive summary

| Metric | Value | Status |
|---|---|---|
| Overall compliance score | 77% | ✅ Acceptable |
| ISO 27001 mapping | 71% | ✅ |
| Open risks | 6 | 🔴 Action required |
| Critical risks | 2 | 🔴 Immediate action |
| Closed this period | 2 | ✅ |
| Frameworks assessed | 5 | ISO 27001 · NIST CSF · GDPR · NIS2 · DORA |

---

## Compliance by control area

| Control area | Score | Trend |
|---|---|---|
| Access Control | `██████████████████░░` 91% | ↑ |
| Network Security | `████████████████░░░░` 81% | ↑ |
| Endpoint Security | `█████████████████░░░` 86% | ↑ |
| Logging & Monitoring | `████████████████░░░░` 78% | → |
| Incident Response | `█████████████████░░░` 83% | ↑ |
| Data Protection | `█████████████████░░░` 85% | ↑ |
| Supply Chain | `████████████░░░░░░░░` 61% | ↓ |
| AI / LLM Governance | `███████████░░░░░░░░░` 53% | ↓ |

> **Average: 77%** — target is 85% across all control areas

---

## Risk register — open risks

| ID | Risk | Score | Level | Owner | Deadline |
|---|---|---|---|---|---|
| RISK-001 | Unpatched systems | 20 | 🔴 Critical | IT Operations | **Immediate** |
| RISK-002 | Phishing attack | 20 | 🔴 Critical | Security Team | **Immediate** |
| RISK-005 | SQL injection data breach | 15 | 🟠 High | Dev Team | 30 days |
| RISK-007 | Third-party supplier breach | 12 | 🟠 High | Procurement / Security | 30 days |
| RISK-003 | Insider threat | 10 | 🟠 High | HR / Security | 30 days |
| RISK-004 | DDoS attack | 9 | 🟡 Medium | Network Team | 90 days |

### Closed risks

| ID | Risk | Closed note |
|---|---|---|
| RISK-006 | ~~Lost or stolen laptop~~ | Full-disk encryption enforced via MDM policy. Risk accepted at residual level. |
| RISK-008 | ~~Cloud storage misconfiguration~~ | Block Public Access enabled on all buckets. CloudTrail alerts added for policy changes. |

---

## 2026 focus areas

| Area | Requirement | Status |
|---|---|---|
| **NIS2 Directive** | EU member states enforcing since Oct 2024. Incident reporting within 24h required. | ⚠️ Review needed |
| **DORA** | Digital Operational Resilience Act in force Jan 2025. Applies to financial sector. | ⚠️ Assess applicability |
| **AI / LLM Governance** | ISO/IEC 42001 (AI management) published 2023. Use of AI tools requires policy. | 🔴 Gap identified |
| **Zero Trust Architecture** | NIST SP 800-207 — never trust, always verify. Replace perimeter-only model. | → In progress |
| **Supply Chain Security** | ISO 27001:2022 Annex A 5.19-5.22. Vendor risk assessments mandatory. | ⚠️ Partially covered |

---

## Recommended actions

- 🔴 **[IMMEDIATE]** Remediate RISK-001 — Unpatched systems (owner: IT Operations)
- 🔴 **[IMMEDIATE]** Remediate RISK-002 — Phishing attack (owner: Security Team)
- 🟠 **[30 days]** Address RISK-003 — Insider threat
- 🟠 **[30 days]** Address RISK-005 — SQL injection data breach
- 🟠 **[30 days]** Address RISK-007 — Third-party supplier breach
- ⚠️ **[This quarter]** Conduct AI/LLM usage audit and draft governance policy
- ⚠️ **[This quarter]** Complete NIS2 gap assessment if operating in EU
- → **[Ongoing]** Progress Zero Trust Architecture implementation

---

*Report generated automatically by `scripts/generate_report.py`.*  
*Risk data sourced from `grc/risk-assessment/sample_risks.json`.*  
*Next report: 2026-05-06*