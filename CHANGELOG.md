# Changelog

## [1.1.0] - 2026-03-16
- Added automated weekly report with Mermaid charts
- Added pytest test suite (8 tests)
- Added CONTRIBUTING.md
- Added GitHub Actions for tests and auto-reporting

## [1.0.0] - 2026-03-14
- Initial release
- Risk matrix with likelihood x impact scoring
- Security policy template
- ISO 27001 / NIST CSF compliance checklist

## [1.2.0] - 2026-03-16
- Added network scanner (nmap-based) that converts open ports to GRC risks
- Added 5 new pytest tests for the scanner (13 total, all passing)
- Updated README with 4 new Mermaid diagrams explaining the scan pipeline
- Scanner output feeds directly into risk_matrix.py
