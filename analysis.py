"""
Manufacturing Equipment Efficiency Analysis
Generates trend plot comparing quarterly efficiency to industry target.

Author/Contact: 24f1000999@ds.study.iitm.ac.in
"""
# updated for PR req

import matplotlib.pyplot as plt

quarters = ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']
values = [72.08, 76.59, 79.04, 78.68]
average = 76.6
target = 90

plt.figure(figsize=(8,8), dpi=64)
plt.plot(quarters, values, marker='o', linewidth=2)
plt.axhline(average, color='orange', linestyle='--', linewidth=1.5, label=f'Average ({average})')
plt.axhline(target, color='red', linestyle='-.', linewidth=1.5, label=f'Industry Target ({target})')
plt.ylim(60, 95)
plt.title("Equipment Efficiency Rate — 2024 Quarterly Trend")
plt.ylabel("Efficiency Rate (%)")
plt.xlabel("Quarter")
plt.grid(alpha=0.3)
plt.legend()
plt.savefig("equipment_efficiency_trend.png", dpi=64)
plt.close()
