# Manufacturing Performance Analysis — 2024

**Author / Contact:** 24f1000999@ds.study.iitm.ac.in

## Overview
This analysis investigates quarterly equipment efficiency rates for 2024 and compares them to the industry benchmark target of **90%**. The observed average efficiency across the year is **76.6%**. This analysis was prepared using Jules (ChatGPT Codex): https://chatgpt.com/codex/tasks

## Quarterly Efficiency Data
- **Q1:** 72.08
- **Q2:** 76.59
- **Q3:** 79.04
- **Q4:** 78.68
- **Average:** **76.6**

## Key Findings
- Efficiency increased from Q1 to Q3 but plateaued below the industry target.
- The 2024 average efficiency is **76.6**, which is **13.4 percentage points** below target 90.
- This gap likely stems from high unplanned downtime and reactive maintenance.

## Business Implications
- Operating below the benchmark can increase per-unit costs and reduce throughput.
- Persistent downtime undermines customer delivery timelines and profitability.

## Recommendations (Actionable)
**Primary solution:** implement a predictive maintenance program.

Steps:
1. Deploy sensors/telemetry (vibration, temperature, run-hours).
2. Build predictive models for time-to-failure and anomaly detection.
3. Prioritize maintenance using risk scores and schedule proactively.
4. Pilot on 2–3 critical production lines; measure MTBF and MTTR improvements.
5. Scale across plant and integrate with CMMS and spare-parts optimization.

## Files included in this PR
- `analysis.py` — Python script reproducing the trend chart
- `equipment_efficiency_trend.png` — visualization of quarterly trend and benchmark
- `README.md` — this data story and recommendations

**Solution statement:** implement predictive maintenance program

# Codex verification update
This update ensures README.md is included in the pull request.

