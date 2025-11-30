# Equipment Efficiency Analysis — 2024

**Author / Contact:** 24f1000999@ds.study.iitm.ac.in

## Dataset
Quarterly equipment efficiency rates (2024):
- Q1: 72.08
- Q2: 76.59
- Q3: 79.04
- Q4: 78.68

**Calculated average:** **76.6**

**Industry target:** 90

## Key Findings
- The equipment efficiency rate improved from **72.08** in Q1 to a peak of **79.04** in Q3, then slightly declined to **78.68** in Q4.
- The 2024 average efficiency is **76.6**, which is **13.4 percentage points below** the industry target of 90.
- The quarterly trend shows improvement mid-year but plateaus below target, indicating systemic issues that short-term fixes may not resolve.

## Business Implications
- Persistent gap vs. industry target implies increased downtime and higher maintenance costs are likely continuing.
- Operating below benchmark reduces throughput and may increase per-unit production costs, impacting margins.
- Strategic investment is required to avoid compounding cost increases and loss of competitive advantage.

## Recommendations (Actionable)
**Primary solution:** Implement a predictive maintenance program.
Steps:
1. **Data collection & monitoring:** Deploy sensors and centralized telemetry to capture equipment vitals (vibration, temperature, run-hours).
2. **Analytics & models:** Build predictive models (time-to-failure, anomaly detection) using historical maintenance and sensor data.
3. **Prioritized interventions:** Use risk scoring to schedule maintenance for high-risk equipment proactively.
4. **Pilot program:** Start with 2–3 critical production lines; measure MTBF (mean time between failures) and MTTR (mean time to repair).
5. **Scale & integrate:** After pilot success, roll out across plant, integrate with CMMS and spare-parts optimization.

## Expected Impact
- Predictive maintenance can reduce unplanned downtime, improve availability, and progressively raise equipment efficiency toward the 90 target.
- Early adopters typically see 10–40% reduction in downtime; combined with process improvements, the efficiency gap can be narrowed.

## Files in this PR
- `analysis.py` — Python code to reproduce the chart (`equipment_efficiency_trend.png`)
- `equipment_efficiency_trend.png` — Visualization of quarterly trend vs. benchmark
- `README.md` — This data story and recommendations (includes email and correct average = 76.6)

## How to reproduce
1. Clone repository.
2. Run `python analysis.py` (requires matplotlib).
3. Open `equipment_efficiency_trend.png`.

---

**Solution statement:** implement predictive maintenance program
