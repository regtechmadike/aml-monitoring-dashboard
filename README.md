# AML Monitoring Dashboard Prototype

**Automated transaction monitoring & risk scoring for AML compliance**  
By Magdalene Madike – AML/CFT Specialist (6.5+ years) | RegTech Automator | ISO 27001 Lead Auditor (97%) | Python & Power BI Expert

### What this project does
A lightweight, open-source Python prototype that:
- Screens **100 sample transactions** for money laundering red flags
- Detects **58 configurable red flags** automatically (structuring, velocity, sanctions, geographic risk, etc.)
- Assigns each transaction a **risk score 0–100**
- Flags high-risk items for review / STR filing
- Outputs a summary report (console + future dashboard export)

**Real-world tie-in** — inspired by my work building Power BI AML dashboards that detected 3 potential fraud cases in the first month and reduced manual processing time by 60%.

### Why this matters for banks & FinTechs
Manual transaction monitoring is slow and error-prone.  
This prototype shows how to **automate** large parts of AML compliance while keeping humans in the loop for final decisions — exactly what regulated institutions need in 2026.

### Features
- 58 red-flag rules across 8 categories (structuring, velocity, sanctions, PEP, geography, device, amount patterns, beneficiary risk)
- Basic statistical anomaly detection (outlier amounts, unusual frequency)
- Risk scoring engine (weighted rules + anomaly bonus)
- Color-coded console output + CSV export for review
- Easy to extend: add new rules, connect to real data feeds, integrate Power BI

### Quick Start

```bash
# Clone & run
git clone https://github.com/Nobody3120/aml-monitoring-dashboard.git
cd aml-monitoring-dashboard
pip install pandas numpy
python aml_monitor.py
