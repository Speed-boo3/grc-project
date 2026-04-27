# Security Compliance Checklist — 2026

Based on ISO 27001:2022, NIST CSF 2.0, GDPR, NIS2 and emerging 2026 requirements.
Use this for internal gap analysis before an audit or security review.

Scoring: ✅ In place · ⚠️ Partial · ❌ Not in place · N/A Not applicable

---

## 1. Governance and Organisation

| # | Control | ISO 27001 | NIST CSF | Status |
|---|---|---|---|---|
| 1.1 | Information security policy exists and is reviewed annually | 5.1 | GV.PO | |
| 1.2 | Security roles and responsibilities are documented | 5.2 | GV.RR | |
| 1.3 | Security is integrated into project and change management | 5.8 | GV.OC | |
| 1.4 | Board-level accountability for information security exists | 5.4 | GV.RR | |
| 1.5 | Security exceptions are tracked and time-limited | 5.1 | GV.PO | |
| 1.6 | AI/LLM usage policy exists and is enforced | 5.1 | GV.PO | |

---

## 2. Risk Management

| # | Control | ISO 27001 | NIST CSF | Status |
|---|---|---|---|---|
| 2.1 | Formal risk assessment process is documented | 6.1 | ID.RA | |
| 2.2 | Risk register is maintained and reviewed quarterly | 6.1 | GV.RM | |
| 2.3 | Risk treatment plans are documented with owners and deadlines | 6.2 | GV.RM | |
| 2.4 | Residual risk is reviewed and accepted by management | 6.1 | GV.RM | |
| 2.5 | Supply chain risks are assessed and tracked | 5.21 | ID.RA | |
| 2.6 | AI and third-party model risks are included in the register | 5.21 | ID.RA | |

---

## 3. Access Control

| # | Control | ISO 27001 | NIST CSF | Status |
|---|---|---|---|---|
| 3.1 | Least privilege enforced on all accounts | 8.2 | PR.AA | |
| 3.2 | MFA enabled for all privileged and remote access | 8.5 | PR.AA | |
| 3.3 | Joiners, movers, leavers process documented and tested | 8.2 | PR.AA | |
| 3.4 | Access reviews completed quarterly | 8.2 | ID.AM | |
| 3.5 | Service accounts and API keys are inventoried and rotated | 8.2 | PR.AA | |
| 3.6 | Zero Trust principles applied to network access | 8.20 | PR.AA | |

---

## 4. Network and Infrastructure Security

| # | Control | ISO 27001 | NIST CSF | Status |
|---|---|---|---|---|
| 4.1 | Network is segmented (production / dev / guest) | 8.20 | PR.IR | |
| 4.2 | Firewall rules are documented and reviewed quarterly | 8.20 | PR.IR | |
| 4.3 | No management ports (SSH/RDP) open to the internet | 8.20 | PR.IR | |
| 4.4 | All remote access uses encrypted tunnels (VPN/Zero Trust) | 8.20 | PR.AA | |
| 4.5 | Vulnerability scanning runs at least monthly | 8.8 | ID.RA | |
| 4.6 | IDS/IPS is deployed and generating alerts | 8.16 | DE.CM | |

---

## 5. Endpoint Security

| # | Control | ISO 27001 | NIST CSF | Status |
|---|---|---|---|---|
| 5.1 | Full-disk encryption on all laptops and mobile devices | 8.1 | PR.DS | |
| 5.2 | EDR deployed on all endpoints | 8.7 | DE.CM | |
| 5.3 | Patch management: critical patches within 14 days | 8.8 | PR.PS | |
| 5.4 | Software inventory is maintained and reviewed | 8.9 | ID.AM | |
| 5.5 | Removable media is controlled by technical policy | 8.12 | PR.DS | |
| 5.6 | Remote wipe capability on all mobile devices | 8.1 | PR.PS | |

---

## 6. Data Protection and GDPR

| # | Control | ISO 27001 | GDPR Article | Status |
|---|---|---|---|---|
| 6.1 | Data classification policy exists and is applied | 5.12 | Art. 5 | |
| 6.2 | Personal data inventory (ROPA) is maintained | 5.12 | Art. 30 | |
| 6.3 | Lawful basis for all personal data processing is documented | 5.12 | Art. 6 | |
| 6.4 | Data is not transferred outside EU/EEA without safeguards | 8.10 | Art. 46 | |
| 6.5 | SAR process: response within 30 days | 5.34 | Art. 15 | |
| 6.6 | Breach notification: DPA within 72 hours | 5.24 | Art. 33 | |
| 6.7 | Privacy notices are accurate and accessible | 5.34 | Art. 13 | |

---

## 7. Logging and Monitoring

| # | Control | ISO 27001 | NIST CSF | Status |
|---|---|---|---|---|
| 7.1 | Security-relevant logs are collected centrally | 8.15 | DE.CM | |
| 7.2 | Logs retained for minimum 12 months | 8.15 | DE.CM | |
| 7.3 | Logs are protected against tampering | 8.15 | PR.DS | |
| 7.4 | Alerts are reviewed daily by security team | 8.16 | DE.AE | |
| 7.5 | Privileged account activity is monitored and alerted | 8.16 | DE.CM | |
| 7.6 | Cloud activity logs (CloudTrail/equivalent) are enabled | 8.15 | DE.CM | |

---

## 8. Incident Response

| # | Control | ISO 27001 | NIST CSF | Status |
|---|---|---|---|---|
| 8.1 | Incident response plan is documented and tested annually | 5.24 | RS.MA | |
| 8.2 | Incident classification criteria are defined | 5.25 | RS.AN | |
| 8.3 | Post-incident reports completed within 5 business days | 5.27 | RS.MI | |
| 8.4 | NIS2: 24h early warning, 72h notification for significant incidents | 5.24 | RS.CO | |
| 8.5 | Contact list for incident escalation is maintained and current | 5.24 | RS.CO | |

---

## 9. Supply Chain Security

| # | Control | ISO 27001 | NIST CSF | Status |
|---|---|---|---|---|
| 9.1 | Supplier security assessment before onboarding | 5.19 | ID.SC | |
| 9.2 | Supplier contracts include security and DPA requirements | 5.20 | GV.SC | |
| 9.3 | Critical supplier security posture reviewed annually | 5.22 | ID.SC | |
| 9.4 | Software bill of materials (SBOM) for critical software | 8.30 | ID.SC | |
| 9.5 | Open source components are tracked and vulnerability-checked | 8.30 | ID.SC | |

---

## 10. Emerging Requirements (2026)

| # | Area | Requirement | Status |
|---|---|---|---|
| 10.1 | **AI/LLM Governance** | ISO/IEC 42001:2023 alignment. AI usage policy. Data protection in AI tools. | |
| 10.2 | **NIS2 Directive** | In force Oct 2024. Supply chain, incident reporting, board accountability. | |
| 10.3 | **DORA** | In force Jan 2025. Digital resilience for financial sector. ICT risk management. | |
| 10.4 | **Zero Trust** | NIST SP 800-207. Eliminate implicit trust, verify every request. | |
| 10.5 | **Post-Quantum Cryptography** | NIST PQC standards finalised 2024. Migration planning required. | |

---

## Gap analysis summary

After completing this checklist, document all ❌ and ⚠️ items in the risk register with:

- Owner
- Remediation deadline
- Treatment: mitigate / accept / transfer / avoid

Items in sections 1–3 are typically highest priority for an ISO 27001 audit.
Items in section 10 are increasingly expected by enterprise customers and regulators.
