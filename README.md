Maternal Digital Twin Early-Warning System

Project Overview

This project demonstrates a "Digital Twin" approach to maternal health monitoring, shifting from population-wide averages to N-of-1 personalized baselines. By identifying biological "breaks in rhythm" in blood pressure and heart rate, this model provides a 4–5 day early warning for gestational hypertension before traditional clinical thresholds are breached.


Key Features

• Personalized Baselines: Uses the first 30 days of gestation to establish a "Healthy Self" reference for each patient.

• Z-Score Shift Detection: A custom-built statistical engine that identifies deviations exceeding 2.0 standard deviations from the initial baseline.

• Clinical Triage Logic: Automatically categorizes patients into "Stable" or "Clinical Review Required" based on physiological trajectory.

• iOS Optimized Architecture: Developed entirely in Carnets (Jupyter) on iPad, utilizing a "Pure Python" stack to bypass binary dependency limitations (scikit-learn/adtk) in mobile environments.

The Technical Challenge: "Baseline Drift"
During development, initial "Sliding Window" models failed to detect anomalies because the baseline drifted upward alongside the rising blood pressure. I pivoted to a Fixed Initial Baseline strategy, which successfully isolated the deviation from the patient's healthy 1st-trimester state.


Tech Stack

• Language: Python 3.x

• Libraries: Pandas, NumPy, Matplotlib, SQLite3

• Environment: Carnets (iOS / Mobile Jupyter)

• Domain Logic: Midwifery, Public Health Nursing


Clinical Impact

• Reduced Alarm Fatigue: Filters out daily "noise" (e.g., stress, caffeine) by focusing on 7-day trend shifts.

• Early Intervention: Detects systemic changes at 125–130 mmHg for patients with low baselines, preventing delayed care.


How to "Save" your Project for Sharing:

1. Export to HTML: In Carnets, tap File > Download as > HTML.

2. Upload to GitHub: Upload the .ipynb file and the .html file.

3. The "Live" Link: If you use GitHub Pages, you can host the HTML file so anyone can view your charts and code directly in their browser.


![Maternal Digital Twin Chart]
(maternal_digital_twin_chart.png)
