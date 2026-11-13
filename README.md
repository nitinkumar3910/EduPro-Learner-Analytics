# EduPro – Learner Demographics and Course Enrollment Behavior Analysis

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://edupro-learner-analytics-4n2rdzrqpez3svywaqh9y6.streamlit.app/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Code Style: PEP 8](https://img.shields.io/badge/code%20style-PEP%208-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

**An enterprise-grade descriptive intelligence system, empirical research study, and interactive Streamlit web dashboard analyzing learner demographics, curriculum demand, and enrollment behaviors across the EduPro online education ecosystem.**

- **GitHub Repository**: [https://github.com/nitinkumar3910/EduPro-Learner-Analytics](https://github.com/nitinkumar3910/EduPro-Learner-Analytics)
- **Live Streamlit Web Application**: [https://edupro-learner-analytics-4n2rdzrqpez3svywaqh9y6.streamlit.app/](https://edupro-learner-analytics-4n2rdzrqpez3svywaqh9y6.streamlit.app/)
- **Institutional Context**: Developed with **Unified Mentor** reference architecture and contextualized for municipal workforce development partners including the **City of Toronto Parks, Forestry & Recreation** division.

---

## 📑 Table of Contents
1. [Project Overview & Business Understanding](#-project-overview--business-understanding)
2. [Problem Statement & Research Objectives](#-problem-statement--research-objectives)
3. [Dataset Architecture & Data Dictionary](#-dataset-architecture--data-dictionary)
4. [Technology Stack & System Architecture](#-technology-stack--system-architecture)
5. [Data Cleaning & Quality Governance Pipeline](#-data-cleaning--quality-governance-pipeline)
6. [Key Performance Indicators (KPIs)](#-key-performance-indicators-kpis)
7. [Core Empirical Findings & Statistical Insights](#-core-empirical-findings--statistical-insights)
8. [Dashboard Sections & Features](#-dashboard-sections--features)
9. [Experimental Time-Series Forecasting](#-experimental-time-series-forecasting)
10. [Local Installation & Execution Guide](#-local-installation--execution-guide)
11. [Streamlit Cloud Deployment Guide](#-streamlit-cloud-deployment-guide)
12. [Automated Testing Suite](#-automated-testing-suite)
13. [Limitations & Future Scope](#-limitations--future-scope)
14. [Deliverables & Viva Preparation](#-deliverables--viva-preparation)

---

## 🌟 Project Overview & Business Understanding

Online learning platforms accumulate millions of transactional records, yet educational leaders, course creators, and civic stakeholders frequently operate in an analytical vacuum. Decisions regarding course commissioning, prerequisite structures, pricing models, and public outreach are often driven by intuition rather than empirical learner intelligence.

**EduPro Analytics** provides a rigorous, transparent data analytics solution to decode:
- **Demographic Reach**: The actual age architecture and gender balance across curriculum categories.
- **STEM Inclusivity**: Real-world participation parity in high-earning technical fields like Data Science, AI, and Cybersecurity.
- **Subject Demand Dynamics**: Organic learner demand unskewed by catalog size differences.
- **Engagement Concentration**: How platform volume is distributed between single-course trialists and multi-course power users.

---

## 🎯 Problem Statement & Research Objectives

### Problem Statement
EduPro possessed 10,000 verified enrollment transactions across 3,000 learners and 60 courses, but lacked systematic visibility into:
1. Which age groups drive active platform throughput?
2. Does gender disparity exist in high-demand technical courses?
3. Which subject categories generate peak enrollment volume versus revenue?
4. Do secondary-school youth pursue advanced content or only beginner primers?
5. What proportion of learners transition beyond a single course?

### Research Objectives
- **Integrate & Validate**: Merge Users, Courses, Teachers, and Transactions entities with verified 100% referential integrity and 0 null values.
- **Audit Demographic Parity**: Measure the Gender Parity Index (GPI) and age cohort distributions.
- **Test Independence**: Conduct Chi-Square contingency tests ($\chi^2$) and Cramér's $V$ effect size tests to confirm demographic neutrality.
- **Model Engagement Concentration**: Segment users into activity tiers using Pareto and Lorenz curves.
- **Forecast Growth**: Implement experimental Double Exponential Smoothing on chronological weekly time-series to predict near-term capacity demand.

---

## 🗄️ Dataset Architecture & Data Dictionary

The platform database comprises four normalized relational tables exported for the complete 2025 calendar year:

```
+----------------------------------------------------------------------------------------------------+
|                                    EDUPRO RELATIONAL SCHEMA                                        |
+----------------------------------------------------------------------------------------------------+
|   USERS (3,000 Rows)                  TRANSACTIONS (10,000 Rows)                                   |
|   • UserID (PK, string)               • TransactionID (PK, string)                                 |
|   • UserName (string)                 • UserID (FK -> Users)                                       |
|   • Age (integer, 15-35)              • CourseID (FK -> Courses)                                   |
|   • Gender (string, Female/Male)      • TeacherID (FK -> Teachers)                                 |
|   • Email (string, RFC-compliant)     • TransactionDate (date, 2025-01-01 to 2025-12-30)            |
|                                       • Amount (float, $0.00 to $490.90)                           |
|                                       • PaymentMethod (string, PayPal/Credit Card/Bank Transfer)   |
+----------------------------------------------------------------------------------------------------+
                                                        |
                                                        v
+----------------------------------------------------------------------------------------------------+
|   COURSES (60 Rows)                   TEACHERS (60 Rows)                                           |
|   • CourseID (PK, string)             • TeacherID (PK, string)                                     |
|   • CourseName (string)               • TeacherName (string)                                       |
|   • CourseCategory (12 disciplines)   • Age (integer, 27-50)                                       |
|   • CourseType (Free/Paid)            • Gender (string, Female/Male)                               |
|   • CourseLevel (Beg/Int/Adv)         • Expertise (12 disciplines)                                 |
|   • CoursePrice (float, $0 - $490.90) • YearsOfExperience (integer, 1-24)                          |
|   • CourseDuration (float, hrs)       • TeacherRating (float, 1.05-4.97)                           |
|   • CourseRating (float, 1.13-4.94)   +------------------------------------------------------------+
+----------------------------------------------------------------------------------------------------+
```

### Data Dictionary

| Table | Column Name | Data Type | Constraint / Domain | Description |
| :--- | :--- | :---: | :---: | :--- |
| **Users** | `UserID` | String | PK, Format `U#####` | Unique learner identifier |
| Users | `UserName` | String | Unique string | Alphanumeric account username |
| Users | `Age` | Integer | $15 \le \text{Age} \le 35$ | Learner chronological age in years |
| Users | `Gender` | String | `Female`, `Male` | Standardized binary gender identity |
| Users | `Email` | String | Standard RFC Regex | Registered contact email address |
| **Courses**| `CourseID` | String | PK, Format `CR#####`| Unique accredited course code |
| Courses | `CourseName` | String | 60 Titles | Formal course curriculum title |
| Courses | `CourseCategory`| String | 12 Disciplines | Subject area (Data Science, Finance, AI, etc.) |
| Courses | `CourseType` | String | `Free`, `Paid` | Commercial access model |
| Courses | `CourseLevel`| String | `Beginner`, `Intermediate`, `Advanced` | Pedagogical prerequisite skill level |
| Courses | `CoursePrice`| Float | $\$0.00 \le \text{Price} \le \$490.90$ | Official catalog list price in USD |
| Courses | `CourseDuration`| Float | $1.20 \le \text{Duration} \le 49.73$ | Total instructional course duration in hours |
| Courses | `CourseRating` | Float | $1.13 \le \text{Rating} \le 4.94$ | Student satisfaction rating (scale 1.0–5.0) |
| **Teachers**| `TeacherID` | String | PK, Format `TC#####`| Unique instructor identifier |
| Teachers | `TeacherName` | String | Full Name | Lead course instructor name |
| Teachers | `Expertise` | String | 12 Disciplines | Subject matter qualification domain |
| Teachers | `YearsOfExperience`| Integer| $1 \le \text{Exp} \le 24$ | Professional and academic experience (years)|
| Teachers | `TeacherRating`| Float | $1.05 \le \text{Rating} \le 4.97$ | Aggregate instructor feedback rating |
| **Transactions**| `TransactionID`| String | PK, Format `TT#####`| Unique enrollment transaction identifier |
| Transactions | `UserID` | String | FK -> Users | Enrolled learner foreign key |
| Transactions | `CourseID` | String | FK -> Courses | Selected course foreign key |
| Transactions | `TeacherID`| String | FK -> Teachers | Assigned instructor foreign key |
| Transactions | `TransactionDate`| Date | 2025-01-01 to 2025-12-30 | Verified enrollment timestamp |
| Transactions | `Amount` | Float | $\$0.00 \le \text{Amount} \le \$490.90$ | Transaction price paid by learner |
| Transactions | `PaymentMethod`| String | `PayPal`, `Credit Card`, `Bank Transfer` | Payment processing gateway |

---

## 🛠️ Technology Stack & System Architecture

```
+----------------------------------------------------------------------------------------------------+
|                                  EDUPRO SYSTEM ARCHITECTURE                                        |
+----------------------------------------------------------------------------------------------------+
|  [ PRESENTATION LAYER ]                                                                            |
|  Streamlit 1.67 • Custom Executive CSS • Multi-View Navigation • Plotly Express & Graph Objects    |
+----------------------------------------------------------------------------------------------------+
                                                ^
                                                |
+----------------------------------------------------------------------------------------------------+
|  [ ANALYTICAL & BUSINESS INTELLIGENCE LAYER ]                                                      |
|  • Dynamic KPI Engine (calculate_kpis)           • Chi-Square & ANOVA Inference (run_statistical)  |
|  • AI-Powered Automated Insights Engine          • Holt's Trend Time-Series Forecasting            |
+----------------------------------------------------------------------------------------------------+
                                                ^
                                                |
+----------------------------------------------------------------------------------------------------+
|  [ PREPROCESSING & QUALITY GOVERNANCE LAYER ]                                                      |
|  • Data Quality Audit Protocol                   • Referential Integrity Scanner                   |
|  • Vectorized Type Coercion & Standardization    • Interquartile Range (IQR) Outlier Detector     |
+----------------------------------------------------------------------------------------------------+
                                                ^
                                                |
+----------------------------------------------------------------------------------------------------+
|  [ STORAGE & REPOSITORY LAYER ]                                                                    |
|  Master Excel (.xlsx) • Clean Partitioned CSVs • In-Memory BytesIO Exporters (CSV & OpenPyXL Excel)|
+----------------------------------------------------------------------------------------------------+
```

- **Core Analytics**: Python 3.10+, Pandas, NumPy, SciPy (Statistical Inference & Optimization)
- **Visualization**: Plotly Express, Plotly Graph Objects
- **Dashboard Framework**: Streamlit
- **Quality Assurance**: Python `unittest` Automated Testing Suite
- **Exporting**: OpenPyXL, Python `io.BytesIO`

---

## 🛡️ Data Cleaning & Quality Governance Pipeline

The preprocessing pipeline (`src/data_loader.py`) implements automated quality checks:
1. **Zero Nulls Confirmed**: Complete dataset contains $0$ missing cells across $13,120$ total records ($100\%$ completeness score).
2. **Key Uniqueness Verified**: Zero duplicate primary keys detected in Users, Courses, Teachers, or Transactions.
3. **100% Referential Integrity**: Foreign keys in `Transactions` match dimension primary keys bijectively with **0 orphan records**.
4. **Domain Rule Validation**:
   - $100\%$ of Free courses transacted at $\$0.00$.
   - $100\%$ of Paid courses transacted at positive list prices ($>\$0.00$).
   - Learner age verified within valid bounds $[15, 35]$.
   - Course ratings verified within $[1.0, 5.0]$.
5. **Standardized Age Banding**:
   - **Youth (<18)**: 15–17 years (Secondary education)
   - **Young Adult (18–25)**: 18–25 years (Post-secondary & workforce entry)
   - **Career Professional (26–35)**: 26–35 years (Upskilling & career transition)

---

## 📈 Key Performance Indicators (KPIs)

All KPIs are calculated dynamically from the active filtered transaction slice:

| KPI Number | KPI Name | Mathematical Formula | Dataset Benchmark | Strategic Interpretation |
| :---: | :--- | :--- | :---: | :--- |
| **1** | **Total Learners** | $\text{CountDistinct}(\text{UserID})$ | **3,000** | Unique individuals registered and enrolled |
| **2** | **Total Enrollments**| $N_{\text{transactions}}$ | **10,000** | Total course seats filled across 2025 |
| **3** | **Total Courses** | $\text{CountDistinct}(\text{CourseID})$ | **60** | Active catalog course breadth |
| **4** | **Total Categories**| $\text{CountDistinct}(\text{CourseCategory})$ | **12** | Distinct educational disciplines |
| **5** | **Avg Courses/User** | $\frac{\text{Total Enrollments}}{\text{Total Learners}}$ | **3.33** | Mean engagement intensity per learner |
| **6** | **Gender Parity** | $\text{GPR} = \frac{N_{\text{Female}}}{N_{\text{Male}}}$ | **1.0317** | Balanced inclusivity (50.8% F / 49.2% M) |
| **7** | **Top Category** | $\text{Mode}(\text{CourseCategory})$ | **Data Science** | 916 enrollments (9.16% platform share) |
| **8** | **Preferred Level**| $\text{Mode}(\text{CourseLevel})$ | **Beginner** | 3,573 enrollments (35.73% platform share) |
| **9** | **MoM Velocity** | $\frac{E_t - E_{t-1}}{E_{t-1}} \times 100$ | **-5.87%** | Month-over-Month enrollment growth delta |
| **10**| **Gross Value** | $\sum \text{Amount}$ | **\$911,323.47** | Total financial volume (35.97% Paid share) |

---

## 🔬 Core Empirical Findings & Statistical Insights

### 1. Gender Inclusivity & STEM Parity
Unlike traditional technical education platforms where male learners often comprise 65–75% of enrollments, EduPro demonstrates near-perfect gender parity:
- **Data Science**: 479 Female ($52.3\%$) vs. 437 Male ($47.7\%$)
- **Cybersecurity**: 430 Female ($52.5\%$) vs. 389 Male ($47.5\%$)
- **Programming**: 420 Female ($52.1\%$) vs. 386 Male ($47.9\%$)
- **Statistical Independence**: Chi-Square test confirms no association between gender and course choice ($\chi^2 = 8.774, df = 11, p = 0.6427, \text{Cramér's } V = 0.0296$).

### 2. Disciplinary Demand Hierarchy
1. **Data Science**: 916 enrollments ($9.16\%$)
2. **Finance**: 864 enrollments ($8.64\%$)
3. **Web Development**: 844 enrollments ($8.44\%$)
4. **Business**: 833 enrollments ($8.33\%$)
5. **Project Management** & **Artificial Intelligence**: 829 enrollments each ($8.29\%$)
6. **Design**: 827 enrollments ($8.27\%$)
7. **Cybersecurity** & **Machine Learning**: 819 enrollments each ($8.19\%$)
8. **Digital Marketing**: 808 enrollments ($8.08\%$)
9. **Marketing** & **Programming**: 806 enrollments each ($8.06\%$)

### 3. Life-Stage Preferences
- **Youth (<18)**: Show highest relative affinity for **Finance ($9.26\%$)** and **Web Development ($8.99\%$)**. Crucially, $36.35\%$ of youth enrollments are in **Advanced courses**, demonstrating an appetite for practical, career-relevant skills.
- **Career Adults (26–35)**: Lead platform volume ($47.99\%$), concentrating on **Data Science ($9.56\%$)**, **Finance ($8.98\%$)**, and **Project Management ($8.71\%$)**.

### 4. Pareto / Bimodal Activity Concentration
- **Casual Trialists ($54.0\%$)**: 1,620 users take exactly 1 course.
- **Explorers ($20.4\%$)**: 612 users take 2 courses.
- **Engaged ($10.5\%$)**: 314 users take 3–4 courses.
- **Power Learners ($15.1\%$)**: 454 users take 9 to 16 courses, driving **$60.86\%$ of all platform enrollments**.
- **Top 20% Concentration**: The top $20\%$ of users account for **$66.52\%$ of total throughput**.

---

## 🖥️ Dashboard Sections & Features

The redesigned dashboard (`app.py`) is organized into 7 structured views:

1. **1. Overview Dashboard**: Executive scorecards, 10 dynamic KPI cards, category demand ranking, gender donut, and monthly velocity timeline.
2. **2. Learner Demographics**: Histogram + boxplot spread, age cohort breakdowns, skill level stacked distributions, and activity tier shares.
3. **3. Course Enrollment Analysis**: Category popularity index, Free vs. Paid comparative bars, Top/Bottom course rankings, and full course catalog ledger.
4. **4. Advanced Analytics & Models**:
   - Cross-tabulation heatmaps (Age × Category, Gender × Category).
   - Pareto Lorenz concentration curve with 80-20 reference marker.
   - Chi-Square hypothesis testing tables with $\chi^2$, degrees of freedom, p-values, and Cramér's V.
   - Experimental Double Exponential Smoothing enrollment forecasting.
5. **5. AI-Powered Learner Insights**: Rule-based dynamic insights generated in real time from active filters, highlighting curriculum leaders, demographic drivers, bottom 10% course alerts, and strategic recommendations.
6. **6. Data Quality & Preprocessing**: Table-by-table audit scorecard, completeness gauges, domain validation checks, and data cleaning decision log.
7. **7. Methodology & Project Info**: Project architecture, data processing flow, pedagogical rationale, and institutional reference context.

---

## 🔮 Experimental Time-Series Forecasting

To evaluate near-term enrollment capacity demand without conflating it with individual learner retention:
- **Model**: Double Exponential Smoothing (Holt's Linear Trend) with residual variance prediction intervals.
- **Chronological Split**: Fitted on training weeks (first 43 weeks), validated on a held-out test horizon (last 10 weeks).
- **Evaluation**:
  - **MAE**: $55.89$ enrollments/week
  - **RMSE**: $59.69$ enrollments/week
  - **MAPE**: $55.89\%$
  - **Optimal Parameters**: $\alpha = 0.55, \beta = 0.465$
- **Future Horizon**: Projects 8 weeks forward with 95% confidence prediction bands.

---

## 💻 Local Installation & Execution Guide

### Step 1: Clone Repository
```bash
git clone https://github.com/nitinkumar3910/EduPro-Learner-Analytics.git
cd EduPro-Learner-Analytics
```

### Step 2: Set Up Python Virtual Environment
```bash
# Windows
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Production Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Application
```bash
python -m streamlit run app.py
```
Open **`http://localhost:8501`** in your browser.

---

## ☁️ Streamlit Cloud Deployment Guide

The repository is configured for Streamlit Community Cloud:
1. Fork or push changes to your GitHub repository: `https://github.com/nitinkumar3910/EduPro-Learner-Analytics`.
2. Navigate to [share.streamlit.io](https://share.streamlit.io/).
3. Connect your GitHub account and select:
   - **Repository**: `nitinkumar3910/EduPro-Learner-Analytics`
   - **Branch**: `main`
   - **Main file path**: `app.py`
4. Click **Deploy**. Streamlit Cloud will install dependencies from `requirements.txt` and launch the application.

---

## 🧪 Automated Testing Suite

To verify data integrity, KPI formulas, statistical routines, and chart rendering:
```bash
python -m unittest discover -s tests
```
**Test Results**: `Ran 9 tests in 4.777s — OK (0 failures, 0 errors, 0 warnings)`.

---

## ⚠️ Limitations & Future Scope

### Limitations
1. **Absence of Module Progression Logs**: Transaction records confirm enrollments and payments, but do not capture video watch percentage, quiz scores, or course completion drop-off.
2. **Single Calendar Year (2025)**: Prevents multi-year seasonal decomposition.
3. **Upper Age Truncation (Age 35)**: Reflects a younger demographic base, leaving mature/senior continuing education unobserved.

### Future Scope
- Ingest LMS activity event streams to track student drop-off rates and completion timelines.
- Integrate multi-year institutional enrollment records to model macroeconomic seasonality.
- Co-design digital literacy curricula tailored for older adults (36+) in partnership with municipal community centers.

---

## 📚 Deliverables & Viva Preparation

| Document | File Link | Focus Area |
| :--- | :--- | :--- |
| **Comprehensive Research Paper** | [RESEARCH_PAPER.md](RESEARCH_PAPER.md) | Full 13-section academic paper with complete statistical tables and literature references |
| **Government Executive Summary** | [EXECUTIVE_SUMMARY_GOV.md](EXECUTIVE_SUMMARY_GOV.md) | Policy brief tailored for municipal partners (Toronto Parks & Rec) |
| **Viva & Technical Interview Guide** | [VIVA_PREPARATION.md](VIVA_PREPARATION.md) | 30 technical questions & model answers covering architecture, KPIs, and data cleaning |
| **Streamlit Web Application** | [app.py](app.py) | Enterprise 7-view interactive analytics platform |
| **Data Ingestion & Quality Pipeline** | [src/data_loader.py](src/data_loader.py) | Verified preprocessing and data quality audit engine |
| **Analytics & Forecasting Engine** | [src/analytics.py](src/analytics.py) | Dynamic KPIs, Chi-Square inference, AI insights & Holt's forecasting |
| **Visualization Engine** | [src/visualizations.py](src/visualizations.py) | Plotly chart library with corporate theme |
| **Automated Testing Suite** | [tests/test_analytics.py](tests/test_analytics.py) | 9 automated unit tests verifying pipeline stability |

---

*Authored by the EduPro Analytics Taskforce • Unified Mentor Reference Architecture.*
