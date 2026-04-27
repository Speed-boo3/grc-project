# ISO 27001:2022

## What it is

ISO 27001 is the international standard for managing information security. Published by the International Organization for Standardization, it defines requirements for an Information Security Management System (ISMS). Organisations can become certified by passing a two-stage external audit.

It is the most widely recognised security certification globally. In Europe, it is often a procurement requirement — enterprise customers ask for it before signing contracts.

The 2022 revision replaced the 2013 version. All certifications issued after October 2025 must be against the 2022 standard.

---

## Structure

ISO 27001:2022 consists of two parts:

**Clauses 4–10** define the ISMS requirements — scope, leadership, risk assessment, objectives, controls, performance evaluation, continual improvement. These are mandatory.

**Annex A** lists 93 controls across four themes. Organisations select which apply via the Statement of Applicability (SoA).

---

## The 93 controls — four themes

| Theme | Controls | Examples |
|---|---|---|
| Organisational (5.1–5.37) | 37 | Policies, roles, supplier security, threat intelligence, incident management |
| People (6.1–6.8) | 8 | Screening, training, disciplinary process, offboarding |
| Physical (7.1–7.14) | 14 | Physical access, equipment protection, clean desk, media disposal |
| Technological (8.1–8.34) | 34 | Authentication, malware protection, logging, vulnerability management, encryption |

---

## Key changes in ISO 27001:2022

The 2022 revision reduced controls from 114 to 93 and introduced 11 new controls that reflect the current threat landscape:

| New control | Why it matters |
|---|---|
| 5.7 — Threat intelligence | Organisations must collect and act on threat data |
| 5.23 — Cloud services security | Explicit cloud security requirements |
| 5.30 — ICT readiness for business continuity | Links resilience to DORA and NIS2 |
| 8.9 — Configuration management | Baseline configurations must be defined and enforced |
| 8.10 — Information deletion | Data must be securely deleted when no longer needed |
| 8.11 — Data masking | Sensitive data must be masked in non-production environments |
| 8.12 — Data leakage prevention | DLP controls required |
| 8.16 — Monitoring activities | Anomaly detection and behavioural monitoring |
| 8.23 — Web filtering | Controls on web access |
| 8.28 — Secure coding | Formal secure development requirements |

---

## Certification process

1. **Gap analysis** — compare current controls against Annex A. Identify gaps.
2. **Remediation** — implement missing controls. Document everything.
3. **Stage 1 audit** — external auditor reviews documentation. Not a pass/fail.
4. **Stage 2 audit** — external auditor tests implementation. Issues findings.
5. **Certification** — valid for 3 years with annual surveillance audits.

---

## This project

The compliance checklist in `grc/compliance/checklist.md` maps to ISO 27001:2022 Annex A. The gap analysis template in `templates/gap-analysis-template.md` follows the structure an auditor expects.
