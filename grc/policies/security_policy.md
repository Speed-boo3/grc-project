# Information Security Policy

**Version:** 3.0  
**Last updated:** April 2026  
**Owner:** Security Team  
**Review cycle:** Annual or after significant change  

---

## Purpose

This policy sets out the security requirements for protecting information assets, systems and data. It applies to all employees, contractors, third-party suppliers and anyone accessing company systems.

Non-compliance may result in disciplinary action, contract termination or legal liability.

---

## 1. Access Control

All access follows the principle of least privilege — accounts have only the permissions needed for their role, nothing more.

- Admin accounts are separate from standard user accounts
- Multi-factor authentication (MFA) is mandatory for all remote access and privileged accounts
- Shared or generic accounts are prohibited
- Access is reviewed every 90 days; unused accounts are disabled within 7 days
- All access changes are logged and auditable
- Joiners, movers and leavers process must be completed within 24 hours of a role change

---

## 2. Password and Authentication

- Minimum 14 characters, or passphrase of 4+ words
- Password reuse is prohibited (last 12 passwords)
- Passwords are never stored in plaintext, email or shared documents
- Privileged accounts require hardware MFA tokens or FIDO2 keys
- Password manager use is encouraged and supported

---

## 3. Network Security

- All traffic between sites uses encrypted tunnels (VPN or equivalent)
- Production, development and guest networks are segmented
- Firewall rules are reviewed quarterly; no rule permits unrestricted inbound access
- SSH is restricted to known IPs or requires certificate authentication
- Databases are never directly accessible from the internet

---

## 4. Endpoint Security

- Full-disk encryption is mandatory on all laptops and mobile devices
- EDR (Endpoint Detection and Response) is installed and monitored on all endpoints
- OS and critical software patches must be applied within 14 days of release
- Removable media is restricted by policy and technical control
- Remote wipe capability is required on all mobile devices

---

## 5. Data Protection and GDPR

- Personal data is processed only for documented and lawful purposes
- Data minimisation: collect only what is needed
- Data is classified: Public, Internal, Confidential, Restricted
- Confidential and Restricted data must be encrypted in transit and at rest
- Personal data is not transferred outside the EU/EEA without adequate safeguards
- Subject Access Requests (SARs) must be responded to within 30 days
- Data breaches affecting personal data must be reported to the DPA within 72 hours (GDPR Art. 33)

---

## 6. Supply Chain and Third-Party Security

- All suppliers with access to company data or systems must complete a security assessment before onboarding
- Supplier risk is reviewed annually or after a significant security incident at the supplier
- Contracts must include security requirements, data processing agreements and breach notification obligations
- ISO 27001:2022 Annex A 5.19–5.22 controls apply to all critical suppliers

---

## 7. AI and LLM Governance (2026)

- The use of AI tools including large language models (LLMs) for work purposes must be approved by the Security Team
- Confidential, Restricted or personal data must not be submitted to external AI services
- AI-generated outputs in security-relevant contexts (code, reports, policies) must be reviewed by a qualified human
- The organisation maintains an inventory of all AI tools in use
- This policy aligns with ISO/IEC 42001:2023 (AI management systems)

---

## 8. Incident Response

- All suspected security incidents are reported to the Security Team within 1 hour of detection
- The incident response plan (based on NIST SP 800-61) is tested at least annually
- Post-incident reports are completed within 5 business days
- NIS2 obligations: incidents with significant impact must be reported to the relevant authority within 24 hours (early warning) and 72 hours (full notification)

---

## 9. Logging and Monitoring

- Security-relevant events are logged centrally and retained for a minimum of 12 months
- Logs are protected against tampering
- Alerts are reviewed by the SOC daily
- Anomaly detection is in place for privileged account activity

---

## 10. Business Continuity and Resilience

- Critical systems have documented recovery time objectives (RTO) and recovery point objectives (RPO)
- Backups are tested quarterly; recovery is verified, not assumed
- This policy aligns with DORA (Digital Operational Resilience Act) for organisations in scope

---

## 11. Physical Security

- Server rooms and network equipment are locked; access is badge-controlled and logged
- Clean desk policy applies to all staff in open areas
- Visitors to secure areas are escorted at all times

---

## 12. Exceptions

Exceptions to this policy require written approval from the Security Team and Head of IT. Exceptions are time-limited (maximum 90 days) and tracked in the risk register.

---

## Review history

| Version | Date | Change |
|---|---|---|
| 3.0 | April 2026 | Add AI/LLM governance, NIS2/DORA obligations, supply chain controls |
| 2.0 | January 2025 | Add Zero Trust requirements, DORA alignment, expand data protection |
| 1.0 | March 2024 | Initial release |
