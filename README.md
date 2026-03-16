# GRC Project

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![Reports](https://img.shields.io/badge/Reports-Weekly-orange?style=flat-square)

A Governance, Risk and Compliance project built as part of a master's in cybersecurity. It covers risk assessment, security policy, compliance checking and weekly reporting.

---

## What this project does

```mermaid
flowchart LR
    A[Risk register JSON] --> B[Risk Matrix]
    B --> C[Scored + ranked risks]
    D[Compliance checklist] --> E[Control review]
    C --> F[Weekly report]
    E --> F
    F --> G[reports/ folder]
    G --> H[GitHub Pages / README]
```

---

## Project structure

```
grc-project/
├── grc/
│   ├── risk-assessment/
│   │   ├── risk_matrix.py       # Scores and ranks risks
│   │   └── sample_risks.json    # Example risk register
│   ├── policies/
│   │   └── security_policy.md  # Sample security policy
│   └── compliance/
│       └── checklist.md        # ISO 27001 / NIST CSF checklist
├── scripts/
│   └── generate_report.py      # Generates weekly reports
├── reports/
│   └── README.md               # Index of all generated reports
├── tests/
│   └── test_risk_matrix.py
├── .github/workflows/
│   └── weekly-report.yml       # Runs Mon, Wed, Fri at 08:00
├── requirements.txt
├── CONTRIBUTING.md
└── CHANGELOG.md
```

---

## How it works

### Risk assessment

```bash
python grc/risk-assessment/risk_matrix.py --file grc/risk-assessment/sample_risks.json
```

Risks are scored using a standard **likelihood × impact** matrix. Each risk gets a score from 1 to 25 and is rated Low, Medium, High or Critical.

### Risk matrix

```mermaid
quadrantChart
    title Risk Matrix — Likelihood vs Impact
    x-axis Low Impact --> High Impact
    y-axis Low Likelihood --> High Likelihood
    quadrant-1 Critical
    quadrant-2 High
    quadrant-3 Low
    quadrant-4 Medium
    Unpatched Systems: [0.9, 0.75]
    Phishing Attack: [0.75, 0.9]
    Insider Threat: [0.9, 0.35]
    DDoS Attack: [0.55, 0.55]
    SQL Injection: [0.9, 0.55]
    Lost Laptop: [0.35, 0.55]
```

### Sample risk output

```
Risk Assessment Report
======================================================================
ID        Risk                           Score   Level      Owner
----------------------------------------------------------------------
RISK-002  Phishing attack                20      Critical   Security Team
RISK-001  Unpatched systems              20      Critical   IT Operations
RISK-005  Data breach via SQL injection  15      High       Dev Team
RISK-003  Insider threat                 10      High       HR / Security
RISK-004  DDoS attack                    9       Medium     Network Team
RISK-006  Lost or stolen laptop          6       Medium     IT Operations
```

---

## Compliance coverage

The checklist maps to two frameworks:

```mermaid
mindmap
  root((Compliance))
    ISO 27001
      Access Control
      Asset Management
      Incident Management
      Cryptography
    NIST CSF
      Identify
      Protect
      Detect
      Respond
      Recover
```

---

## Reports

I put together a weekly report that tracks compliance scores and risk levels over time. It covers the same control areas as the checklist and gives a quick snapshot of where things stand.

The reports live in the [`reports/`](./reports/README.md) folder, one subfolder per date. Each report includes charts for compliance score by area, open risks by severity, and alert trends from the SOC side.

```mermaid
flowchart LR
    A[Risk register] --> B[Score risks]
    B --> C[Check compliance]
    C --> D[Write report]
    D --> E[reports/YYYY-MM-DD/]
```

---

## Setup

```bash
git clone https://github.com/Speed-boo3/grc-project.git
cd grc-project
pip install -r requirements.txt
```

---

## Running the tests

```bash
pytest tests/
```

---

## Related project

The SOC side of this work is in a separate repo: [soc-project](https://github.com/Speed-boo3/soc-project)

GRC defines the controls and policies. The SOC monitors whether those controls are working. They feed each other.

---

## Network Scanning

One of the most important parts of GRC work is checking whether the controls you have on paper actually match reality. The network scanner does exactly that — it scans a host, finds open ports, and turns them into risks that feed directly into the risk register.

> **Important:** Only scan hosts you own or have explicit permission to scan. This tool is intended for use on `localhost` or a private lab network.

---

### How the scan pipeline works

```mermaid
flowchart TD
    A[Run scanner.py] --> B[nmap scans the target]
    B --> C[Open ports found]
    C --> D{Is the port risky?}
    D -- Known risky port --> E[Risk level: High]
    D -- Unexpected port --> F[Risk level: Medium]
    D -- Expected port 80 443 22 --> G[No risk added]
    E --> H[Risk JSON output]
    F --> H
    H --> I[risk_matrix.py scores and ranks]
    I --> J[GRC risk register]
```

---

### What counts as a risky port

```mermaid
mindmap
  root((Risky Ports))
    Plaintext protocols
      21 FTP
      23 Telnet
    Remote access
      3389 RDP
      22 SSH on unexpected host
    Databases exposed
      3306 MySQL
      5432 PostgreSQL
      27017 MongoDB
      6379 Redis
    Other
      445 SMB
      25 SMTP open relay
      8080 HTTP without TLS
```

---

### Running the scanner

```bash
python grc/network-scan/scanner.py --target localhost --output network_risks.json
```

Then feed the output straight into the risk matrix:

```bash
python grc/risk-assessment/risk_matrix.py --file network_risks.json
```

---

### Example output

When the scanner finds a risky port, it looks like this:

```
Network Scan Report
Target  : localhost
Date    : 2026-03-16 08:00
============================================================

Open ports found: 4
  22     ssh
  80     http
  443    https
  3306   mysql (8.0.32)

Risks identified: 1

  ID           Risk                                Level
  ------------------------------------------------------------
  NET-3306     MySQL exposed on port 3306          High

Details:

  NET-3306 -- MySQL exposed on port 3306
    Port     : 3306 (mysql)
    Reason   : Database should not be exposed outside the local network.
    Score    : 16 -> High
    Treatment: Close the port if not needed, or restrict with firewall rules.
```

---

### How it connects to the rest of the project

```mermaid
flowchart LR
    A[Network scanner] -->|Finds open ports| B[Risk JSON]
    B -->|Fed into| C[Risk matrix]
    C -->|Scored risks| D[GRC report]
    D -->|Low compliance score| E[Policy updated]
    E -->|New control added| F[SOC monitors for violations]
    F -->|Alert fires| A
```

This closes the loop between SOC and GRC. The scanner finds a weakness, GRC registers it as a risk, the policy is updated to address it, and the SOC monitors for violations going forward.
