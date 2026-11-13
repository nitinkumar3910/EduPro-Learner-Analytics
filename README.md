# Learner Demographics and Course Enrollment Behavior Analysis on EduPro

An institutional-grade descriptive intelligence system, empirical research study, and interactive Streamlit web dashboard analyzing learner demographics, subject demand, and enrollment patterns across the **EduPro** online learning platform.

Developed in collaboration with **Unified Mentor** and contextualized for municipal workforce development partners including the **Toronto Government Parks, Forestry & Recreation** division.

---

## 🌟 Executive Highlights & Key Findings

- **Demographic Balance**: Exceptional **Gender Parity Index of 1.03** ($50.78\%$ Female vs. $49.22\%$ Male enrollments), with women comprising $\ge 52\%$ of enrollments in technical fields like Data Science and Cybersecurity.
- **Demographic Reach**: Learner age spans **15 to 35 years** (mean: $24.97 \pm 6.05$ years), serving youth ($14.7\%$), post-secondary young adults ($37.3\%$), and working-age career professionals ($48.0\%$).
- **Top Subject Disciplines**: **Data Science** leads platform demand with 916 enrollments, followed by **Finance** (864), **Web Development** (844), **Business** (833), and **Project Management** (829).
- **Youth Demand Focus**: Secondary-school age youth (<18) prioritize **Finance ($9.26\%$)** and **Web Development ($8.99\%$)**, with $36.4\%$ enrolling in Advanced-level coursework.
- **Bimodal Activity Concentration**: $54.0\%$ of learners enroll in a single gateway course, while an elite core of **power learners ($15.1\%$) drives $60.86\%$ of all platform enrollments**.
- **Financial Dynamics**: $64.03\%$ of enrollments are Free access, while $35.97\%$ Paid enrollments generated **\$911,323.47** in gross platform value, led by Artificial Intelligence (\$202.8k) and Business (\$181.5k).
- **Statistical Independence**: Chi-Square tests ($\chi^2 = 8.77, p = 0.643$ for gender; $\chi^2 = 18.01, p = 0.705$ for age cohorts) confirm the complete absence of systemic demographic segregation or bias across course disciplines.

---

## 📂 Repository Structure

```
edupro_learner_analytics/
├── .streamlit/
│   └── config.toml               # Streamlit theme & performance configuration
├── .venv/                        # Dedicated virtual environment
├── data/
│   ├── EduPro_Learning_Data.xlsx # Original 4-sheet master Excel workbook
│   ├── users.csv                 # 3,000 learner demographic records
│   ├── teachers.csv              # 60 instructor profiles & ratings
│   ├── courses.csv               # 60 course offerings across 12 disciplines
│   ├── transactions.csv          # 10,000 verified enrollment transactions
│   ├── merged_edupro_data.csv    # Enriched analytical dataset (33 features)
│   └── eda_results.json          # Formatted statistical KPIs & Chi-Square test outputs
├── src/
│   ├── __init__.py
│   ├── data_loader.py            # Caching, ingestion, and feature engineering
│   └── visualizations.py         # Reusable interactive Plotly chart generators
├── app.py                        # Multi-module Streamlit interactive dashboard
├── RESEARCH_PAPER.md             # Complete academic research paper & empirical report
├── EXECUTIVE_SUMMARY_GOV.md      # Strategic briefing for government stakeholders
├── requirements.txt              # Production dependency specifications
└── README.md                     # Project documentation
```

---

## 🚀 Setup & Execution Guide

### 1. Prerequisites
- Python 3.10+ (tested on Python 3.12.4)
- Git (optional)

### 2. Activate Virtual Environment
The virtual environment is already provisioned in `.venv`:
```powershell
# On Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

### 3. Launch the Streamlit Analytics Dashboard
To start the live interactive dashboard:
```powershell
python -m streamlit run app.py
```
Open your browser to: **`http://localhost:8501`**

### 4. Interactive Dashboard Modules
The web application includes 6 core interactive modules:
1. **Overview & Demographics**: Platform KPIs, age histogram with KDE overlay, and gender participation ratio donut.
2. **Age Cohort Analysis**: Age vs. Course Category heatmap and Skill Maturity (Course Level) stacked breakdowns.
3. **Gender Inclusivity & Parity**: Multi-discipline STEM participation comparisons and level preferences.
4. **Catalog Demand & Levels**: Horizontal ranked popularity charts, Free vs. Paid splits, and Top 10 courses.
5. **Behavioral Engagement Tiers**: Pareto activity tiers, cumulative enrollment concentration curves, monthly timelines, and payment methods.
6. **Data Explorer & Queries**: Live keyword search, multi-filter query builder, and one-click filtered CSV exporter.

---

## 📊 Core Performance Indicators (KPIs)

| KPI Name | Value | Strategic Interpretation |
| :--- | :--- | :--- |
| **Total Enrollments** | 10,000 | Baseline scale of engagement across 2025 |
| **Unique Active Learners** | 3,000 | 100% active conversion from registered pool |
| **Gender Parity Index (GPI)** | 1.0317 | Balanced participation (50.8% Female / 49.2% Male) |
| **Primary Age Cohort** | 26–35 ($48.0\%$) | Early-to-mid career upskilling dominant |
| **Average Course Velocity** | 3.33 courses/user | Long-tail: median 1.0, max 16.0 |
| **Top 20% Concentration** | 66.52% | Super-learner cohort driving majority of throughput |
| **Free Access Ratio** | 64.03% | Broad accessible entry point for public learners |

---

## 🏛️ Public Policy Relevance
This research provides an empirical reference framework for municipal agencies such as the **City of Toronto Parks, Forestry & Recreation** division:
- **Youth Empowerment**: Subsidizing Finance and Web Development tracks for teens aged 15–17 in community recreation centers.
- **STEM Diversity**: Leveraging EduPro's proven gender equity model in local civic coding bootcamps.
- **Lifelong Learning**: Identifying the need to expand digital programming beyond age 35 to support mature and senior residents.

---

## 📜 Deliverables
- **Research Paper**: See [RESEARCH_PAPER.md](file:///C:/Users/DELL/.gemini/antigravity/scratch/edupro_learner_analytics/RESEARCH_PAPER.md)
- **Government Executive Summary**: See [EXECUTIVE_SUMMARY_GOV.md](file:///C:/Users/DELL/.gemini/antigravity/scratch/edupro_learner_analytics/EXECUTIVE_SUMMARY_GOV.md)
- **Streamlit Web Application**: See [app.py](file:///C:/Users/DELL/.gemini/antigravity/scratch/edupro_learner_analytics/app.py)
