<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,40:0a1a2e,100:0055ff&height=200&section=header&text=GRC%20Project&fontSize=60&fontColor=4488ff&animation=fadeIn&fontAlignY=42&desc=Governance%20%7C%20Risk%20%7C%20Compliance&descAlignY=66&descColor=888888&descSize=16"/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=16&duration=2800&pause=900&color=4488FF&center=true&vCenter=true&width=600&lines=Risk+scoring+with+likelihood+%C3%97+impact;Network+exposure+scanning+with+nmap;ISO+27001+%26+NIST+CSF+compliance+checking;Automated+weekly+reports"/>

<br/>

![Python](https://img.shields.io/badge/Python-3.8+-0d1117?style=flat-square&logo=python&logoColor=00ff41)
![Tests](https://img.shields.io/badge/tests-13%20passing-0d1117?style=flat-square&logo=pytest&logoColor=00ff41)
![License](https://img.shields.io/badge/license-MIT-0d1117?style=flat-square)

</div>

---

## What this is

GRC stands for Governance, Risk and Compliance. It is the part of security work that most students do not learn about until they are in a real job — and then suddenly it is everywhere.

While a SOC analyst is responding to live incidents, a GRC analyst is asking harder questions: do we actually know what our risks are? Does our network match what our policy says it should? Are the controls we think are in place actually working?

This project builds those tools from scratch. Risk scoring, network scanning, compliance checking and automated reporting — all in Python, all with tests.

---

## What is GRC

The three parts fit together like this:

```mermaid
flowchart LR
    subgraph GOV[Governance]
        P[Policies]
        PR[Procedures]
        AC[Accountability]
    end
    subgraph RISK[Risk]
        ID[Identify]
        SC[Score]
        TR[Treat]
    end
    subgraph COMP[Compliance]
        FR[Frameworks]
        AU[Audits]
        CH[Checklists]
    end
    GOV --> ORG[Secure Organisation]
    RISK --> ORG
    COMP --> ORG

    style GOV fill:#1a2a5a,stroke:#4488ff,color:#ffffff
    style RISK fill:#5a1a1a,stroke:#ff4444,color:#ffffff
    style COMP fill:#1a5a2a,stroke:#00ff41,color:#ffffff
    style ORG fill:#2a2a2a,stroke:#888888,color:#ffffff
```

**Governance** is about setting the rules — who is responsible, what the policies say, and making sure people follow them.

**Risk** is about knowing what could go wrong. You identify threats, score them by likelihood and impact, then decide what to do about each one.

**Compliance** is about proving your controls actually exist and work. Not just having a policy that says "we encrypt sensitive data" — but being able to show that you do.

---

## Risk scoring

The scoring model is simple: `likelihood × impact`. Both run from 1 to 5. The result sits between 1 and 25.

```mermaid
flowchart TD
    A[Identify the risk] --> B[Score likelihood 1 to 5]
    B --> C[Score impact 1 to 5]
    C --> D[Multiply them]
    D --> E{What is the score?}
    E -->|1 to 4| F[Low — accept or monitor]
    E -->|5 to 9| G[Medium — fix within 90 days]
    E -->|10 to 16| H[High — fix within 30 days]
    E -->|17 to 25| I[Critical — fix immediately]

    style F fill:#007722,stroke:#00ff41,color:#ffffff
    style G fill:#bb7700,stroke:#ffaa00,color:#ffffff
    style H fill:#cc4400,stroke:#ff6600,color:#ffffff
    style I fill:#cc2200,stroke:#ff0000,color:#ffffff
    style A fill:#1a3a8a,stroke:#4488ff,color:#ffffff
```

Running it against the sample register:

```
Risk Assessment Report
======================================================================
ID         Risk                            Score   Level      Owner
----------------------------------------------------------------------
RISK-002   Phishing attack                  20     Critical   Security Team
RISK-001   Unpatched systems                20     Critical   IT Operations
RISK-005   SQL injection data breach        15     High       Dev Team
RISK-003   Insider threat                   10     High       HR / Security
RISK-004   DDoS attack                       9     Medium     Network Team
RISK-006   Lost or stolen laptop             6     Medium     IT Operations
```

---

## Network scanning

One of the most useful things a GRC analyst does is check whether the network actually matches what the security policy says it should. The scanner handles this — it runs nmap against a target, finds open ports and converts each risky one into a risk register entry automatically.

> Only scan hosts you own or have written permission to test.

```mermaid
flowchart TD
    A[scanner.py] --> B[nmap scans the target]
    B --> C[Open ports found]
    C --> D{Is this port risky?}
    D -->|Known dangerous port| E[High risk entry]
    D -->|Unexpected port| F[Medium risk entry]
    D -->|Expected: 22, 80, 443| G[No risk added]
    E & F --> H[Risk JSON]
    H --> I[risk_matrix.py scores it]
    I --> J[Added to risk register]

    style E fill:#cc2200,stroke:#ff0000,color:#ffffff
    style F fill:#bb7700,stroke:#ffaa00,color:#ffffff
    style G fill:#007722,stroke:#00ff41,color:#ffffff
    style A fill:#1a3a8a,stroke:#4488ff,color:#ffffff
    style J fill:#1a5a2a,stroke:#00ff41,color:#ffffff
```

Ports that trigger a High risk entry automatically:

```
21    FTP         sends credentials in plaintext
23    Telnet      everything unencrypted
25    SMTP        open relay risk
445   SMB         WannaCry and most ransomware used this
3389  RDP         constant brute force target
3306  MySQL       databases should never be public
5432  PostgreSQL  same as MySQL
6379  Redis       often runs with no authentication
27017 MongoDB     countless breaches from exposed instances
8080  HTTP Alt    dev servers without TLS
```

Example output when a risky port is found:

```
Network Scan Report
Target  : localhost
============================================================
Open ports: 22 (ssh), 80 (http), 443 (https), 3306 (mysql 8.0.32)

Risks identified: 1

  NET-3306 — MySQL exposed on port 3306
    Reason   : Database should not be publicly accessible
    Score    : 16 → High
    Treatment: Restrict with firewall rules or close the port
```

---

## Compliance

The checklist maps to ISO 27001 and NIST CSF. These are the two frameworks you will see most often in real GRC roles.

**ISO 27001** is the international standard for information security management. Getting certified means an external auditor verified your controls are real and working.

**NIST CSF** organises security into five functions: Identify, Protect, Detect, Respond, Recover. It is widely used in the US and increasingly everywhere else.

```mermaid
flowchart LR
    subgraph ISO[ISO 27001]
        A[Access Control]
        B[Asset Management]
        C[Incident Management]
        D[Cryptography]
        E[Physical Security]
    end
    subgraph NIST[NIST CSF]
        F[Identify]
        G[Protect]
        H[Detect]
        I[Respond]
        J[Recover]
    end
    A --> G
    B --> F
    C --> H
    C --> I
    C --> J
    D --> G
    E --> G

    style ISO fill:#1a2a5a,stroke:#4488ff,color:#ffffff
    style NIST fill:#1a5a2a,stroke:#00ff41,color:#ffffff
```

---

## How GRC and SOC connect

These two do not work in isolation. The SOC responds to threats in real time. GRC makes sure the controls that should prevent those threats actually exist.

```mermaid
flowchart LR
    A[Scanner finds\nexposed port] -->|Creates risk entry| B[Risk register]
    B -->|High score| C[Report flags it]
    C -->|Review triggered| D[Policy updated]
    D -->|New rule added| E[SOC monitors it]
    E -->|Alert fires| F[Incident investigated]
    F -->|Lessons learned| B

    style A fill:#cc2200,stroke:#ff0000,color:#ffffff
    style B fill:#1a3a8a,stroke:#4488ff,color:#ffffff
    style C fill:#bb7700,stroke:#ffaa00,color:#ffffff
    style D fill:#1a5a2a,stroke:#00ff41,color:#ffffff
    style E fill:#5a1a5a,stroke:#aa44ff,color:#ffffff
    style F fill:#1a3a8a,stroke:#4488ff,color:#ffffff
```

When the scanner finds a database exposed to the internet, it goes into the risk register. That triggers a policy review. The SOC gets a new detection rule. When that rule fires, the findings feed back into the risk register. One loop.

---

## Weekly reports

A report is generated automatically every Monday, Wednesday and Friday. It saves to `reports/YYYY-MM-DD/README.md` and includes charts for compliance score per area and open risks by severity.

All previous reports are in [`reports/`](./reports/README.md).

---

## Project structure

```
grc-project/
├── grc/
│   ├── risk-assessment/
│   │   ├── risk_matrix.py       ← likelihood × impact scoring
│   │   └── sample_risks.json    ← example risk register
│   ├── network-scan/
│   │   └── scanner.py           ← nmap wrapper with risk output
│   ├── policies/
│   │   └── security_policy.md  ← policy template
│   └── compliance/
│       └── checklist.md        ← ISO 27001 / NIST CSF checklist
├── scripts/
│   └── generate_report.py      ← weekly report generator
├── reports/
├── tests/
│   ├── test_risk_matrix.py     ← 8 tests
│   └── test_scanner.py         ← 5 tests
└── .github/workflows/
    ├── tests.yml
    └── weekly-report.yml
```

---

## Quickstart

```bash
git clone https://github.com/Speed-boo3/grc-project.git
cd grc-project
pip install -r requirements.txt
```

Score risks from the sample register:
```bash
python grc/risk-assessment/risk_matrix.py --file grc/risk-assessment/sample_risks.json
```

Scan for network exposure:
```bash
python grc/network-scan/scanner.py --target localhost --output network_risks.json
python grc/risk-assessment/risk_matrix.py --file network_risks.json
```

Generate a report:
```bash
python scripts/generate_report.py
```

Run the tests:
```bash
pytest tests/ -v
```

---

## Test your knowledge

20 questions covering GRC fundamentals. Built for students learning this from scratch.

<div align="center">

[![TAKE THE GRC QUIZ](https://img.shields.io/badge/Take%20the%20GRC%20Quiz-→-4488ff?style=for-the-badge&labelColor=0d1117)](https://speed-boo3.github.io/grc-project/quiz/)

</div>

---

## Learn more

- [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html) — the international security management standard
- [NIST CSF](https://www.nist.gov/cyberframework) — the five-function security lifecycle
- [NIST SP 800-30](https://csrc.nist.gov/publications/detail/sp/800-30/rev-1/final) — risk assessment guide
- [CIS Controls](https://www.cisecurity.org/controls) — prioritised security best practices

---

The SOC side of this project is in [soc-project](https://github.com/Speed-boo3/soc-project).

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0055ff,50:0a1a2e,100:0d1117&height=100&section=footer&text=Govern.%20Assess.%20Comply.&fontSize=18&fontColor=4488ff&animation=twinkling"/>
</div>
