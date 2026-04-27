# NIST Cybersecurity Framework 2.0 (2024)

## What it is

The NIST CSF was developed by the US National Institute of Standards and Technology. It gives organisations a common language and structure for managing cybersecurity risk. Unlike ISO 27001, it is not a certification standard — it is a flexible framework you adopt at any level of maturity.

Version 2.0 was released in February 2024. The major change was adding a sixth function: **Govern**.

---

## The six core functions

| Function | Focus | Key question |
|---|---|---|
| **Govern** | Strategy, roles, policy, oversight | Are we set up to manage cybersecurity risk? |
| **Identify** | Assets, risks, business context | What do we have and what could go wrong? |
| **Protect** | Safeguards and controls | What have we put in place to prevent incidents? |
| **Detect** | Monitoring and anomaly detection | How quickly do we find out something is wrong? |
| **Respond** | Incident response and communications | What do we do when an incident occurs? |
| **Recover** | Restoration and resilience | How do we get back to normal? |

The order is deliberate. You cannot protect what you have not identified. You cannot respond effectively without a plan. Govern was added because organisations were implementing strong technical controls with no strategic direction.

---

## Why CSF 2.0 matters in 2026

**Govern function** is now the foundation. Boards and executives are expected to have direct accountability for cybersecurity risk. This aligns with NIS2 requirements that came into force in October 2024.

**Supply chain risk** (ID.SC) is expanded significantly. Third-party and software supply chain risk is now treated with the same rigour as internal risk.

**AI and emerging technology** is explicitly referenced. Organisations using AI tools must assess and manage the associated risks within the CSF framework.

---

## Mapping to this project

| GRC project component | CSF function |
|---|---|
| `grc/risk-assessment/risk_matrix.py` | Govern, Identify |
| `grc/network-scan/scanner.py` | Identify, Detect |
| `grc/compliance/checklist.md` | All six functions |
| `grc/policies/security_policy.md` | Govern, Protect |
| `scripts/generate_report.py` | Govern (reporting) |

---

## CSF vs ISO 27001

| | NIST CSF 2.0 | ISO 27001:2022 |
|---|---|---|
| Certification | No | Yes |
| Prescriptiveness | Low — flexible | High — specific controls |
| Primary audience | US-originated, global | Global, strong in Europe |
| Cost to implement | Lower | Higher |
| Used for | Internal maturity | Customer/regulator assurance |
| Audit requirement | No | Yes |

Most mature organisations use both — CSF as the internal management framework, ISO 27001 for external certification.
