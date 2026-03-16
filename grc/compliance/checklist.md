# Security Compliance Checklist

Based on common controls from ISO 27001 and NIST CSF. Use this as a starting point for a basic security review.

---

## Access Management
- [ ] All user accounts are documented and reviewed quarterly
- [ ] Admin accounts are separate from regular accounts
- [ ] MFA is enabled for all remote access
- [ ] Shared accounts have been removed or disabled
- [ ] Terminated employee accounts removed within 24 hours
- [ ] Password policy enforced via technical controls

## Network Security
- [ ] Firewall rules are documented and reviewed
- [ ] Unused ports and services are disabled
- [ ] Network is segmented — production separated from dev
- [ ] Remote access uses VPN or equivalent
- [ ] IDS/IPS is in place and generating alerts

## Endpoint Security
- [ ] Antivirus/EDR installed and updated on all endpoints
- [ ] Full disk encryption enabled on laptops
- [ ] Software inventory is maintained
- [ ] Patch levels are tracked and reported monthly

## Logging and Monitoring
- [ ] Centralised log collection is set up
- [ ] Logs retained for at least 90 days
- [ ] SOC team reviews alerts daily
- [ ] Log integrity is protected

## Incident Response
- [ ] Incident response plan exists and is documented
- [ ] IR plan tested in the last 12 months
- [ ] Staff know how to report an incident
- [ ] Escalation contact list is up to date

## Data Protection
- [ ] Sensitive data is identified and classified
- [ ] Encryption used for data at rest and in transit
- [ ] Backups taken regularly and tested
- [ ] Data retention and deletion policy in place

## Physical Security
- [ ] Server rooms are locked and access is logged
- [ ] Clean desk policy is enforced
- [ ] Visitor access is controlled and logged

## Awareness and Training
- [ ] All staff completed security awareness training
- [ ] Phishing simulations run at least once a year
- [ ] New starters receive a security induction

---

## Scoring

Count the checked boxes and divide by the total (32) to get a compliance percentage. This is not a substitute for a formal audit — it gives a rough snapshot of control coverage.
