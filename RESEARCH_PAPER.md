# Learner Demographics and Course Enrollment Behavior Analysis on EduPro

**An Empirical Study on Demographic Parity, Curriculum Demand Dynamics, and Engagement Concentration in Open E-Learning Ecosystems**

**Authors:** EduPro Education Intelligence Group & Unified Mentor Research Division  
**Context:** Institutional Workforce Development & Municipal Continuing Education (Toronto Parks, Forestry & Recreation Reference Study)  
**Date:** November 2026  
**Document Classification:** Academic Research Paper & Empirical Analytics Report  

---

## 1. Abstract

Digital education platforms serve increasingly diverse student populations with disparate demographic backgrounds, baseline competencies, and career objectives. Despite possessing high-dimensional transactional datasets, platforms frequently design curricula and deploy outreach resources based on heuristic assumptions rather than descriptive intelligence. This paper presents an empirical analysis of learner demographics and course enrollment behaviors on the **EduPro** platform. Analyzing an integrated relational schema spanning **3,000 unique learners**, **60 accredited courses** across **12 subject disciplines**, **60 instructors**, and **10,000 verified enrollment transactions** throughout the 2025 calendar year, this study evaluates demographic reach, gender equity across STEM subjects, curriculum popularity indices, and engagement concentration. 

Our findings indicate that EduPro exhibits an exceptional **Gender Parity Index of 1.03** ($50.78\%$ female vs. $49.22\%$ male enrollments), maintaining over $52\%$ female representation in traditionally male-skewed technical domains such as Data Science ($52.3\%$) and Cybersecurity ($52.5\%$). Chi-Square tests confirm that course selection is statistically independent of demographic identity ($\chi^2 = 8.77, p = 0.643$ for gender; $\chi^2 = 18.01, p = 0.705$ for age cohorts). Learners span ages 15 to 35 (mean $24.97 \pm 6.05$ years), with career professionals (26–35) contributing $47.99\%$ of enrollments, young adults (18–25) contributing $37.32\%$, and youth (<18) contributing $14.69\%$. Furthermore, we uncover a pronounced **Pareto engagement distribution**: while $54.0\%$ of learners exit after completing a single course, an elite cohort of **power learners ($15.1\%$) accounts for $60.86\%$ of all platform activity**. These findings provide a concrete evidence base for multi-course pathway bundling, youth workforce development, and municipal continuing education partnerships.

---

## 2. Introduction

Over the past decade, open online education platforms have evolved from supplementary instructional libraries into foundational socio-economic infrastructure for technical upskilling, career transitioning, and civic workforce readiness. Modern platforms serve heterogeneous learner populations ranging from secondary-school adolescents building early computational competencies to working professionals seeking accredited certifications in Artificial Intelligence and Cloud Systems.

However, many educational providers suffer from an analytical disconnect between platform capability and learner understanding. Institutions frequently prioritize conversion funnel heuristics, leading to misaligned curriculum planning, under-enrolled course offerings, and unaddressed learner churn. In civic and municipal contexts—such as the youth and adult continuing education programs administered by divisions like the **City of Toronto Parks, Forestry & Recreation** and regional workforce development boards—public agencies require rigorous, auditable evidence to assess whether subsidized digital platforms provide accessible, equitable, and sustainable community value.

This research paper provides an in-depth empirical investigation of learner demographics and course enrollment dynamics on EduPro, establishing a reproducible descriptive intelligence framework for academic researchers, platform architects, and public policy stakeholders.

---

## 3. Problem Statement

Despite recording thousands of user profiles and enrollment transactions, platform administrators previously lacked definitive answers to core behavioral questions:
1. **Demographic Span**: Which age cohorts are most active on the platform, and do older or younger learners face participation barriers?
2. **Gender Representation**: Are female learners underrepresented in high-earning technical fields such as Cybersecurity, Machine Learning, and Data Science?
3. **Disciplinary Demand**: Which subject categories attract peak enrollment volume, and does subject preference shift across developmental life stages?
4. **Pedagogical Maturity**: Do secondary-school youth restrict themselves to introductory primers, or do they demonstrate demand for advanced coursework?
5. **Activity Concentration**: Does enrollment activity reflect broad, uniform learning, or is throughput heavily concentrated among a minority of power users?

Without empirical answers to these questions, decisions surrounding course commissioning, instructor recruitment, pricing tiers, and public sector partnerships remain intuition-driven rather than data-driven.

---

## 4. Research Objectives

This study was designed to achieve the following specific analytical and empirical objectives:
1. **Integrate and Audit Relational Data**: Unify the Users, Courses, Teachers, and Transactions entities into a verified, normalized analytical model with zero missing values or orphan records.
2. **Map the Demographic Architecture**: Quantify age distributions, central tendencies, spreads, and gender participation ratios across all demographic sub-segments.
3. **Analyze Subject Demand Dynamics**: Construct a standardized Category Demand Index and evaluate enrollment volumes across all 12 curriculum disciplines.
4. **Evaluate Cross-Dimensional Interactions**: Perform cross-tabulations and statistical independence tests ($\chi^2$, Cramér's $V$) to examine whether demographic attributes systematically constrain subject or skill-level choices.
5. **Characterize Behavioral Engagement Tiers**: Segment learners based on lifetime course velocity and model platform throughput concentration using Pareto and Lorenz curves.
6. **Formulate Policy & Platform Frameworks**: Translate empirical findings into strategic recommendations for course developers and civic workforce development partners.

---

## 5. Dataset Description & Relational Architecture

The research utilized four relational sheets exported from the EduPro enterprise database, capturing platform operations across the complete 2025 calendar year:

### 5.1 Data Dictionary & Schema Specification

```
+----------------------------------------------------------------------------------------------------+
|                                    EDUPRO RELATIONAL ARCHITECTURE                                  |
+----------------------------------------------------------------------------------------------------+
|   USERS SHEET (3,000 Rows)            TRANSACTIONS SHEET (10,000 Rows)                             |
|   • UserID (PK)                       • TransactionID (PK)                                         |
|   • UserName                          • UserID (FK -> Users)                                       |
|   • Age [15 - 35]                     • CourseID (FK -> Courses)                                   |
|   • Gender [Female, Male]             • TeacherID (FK -> Teachers)                                 |
|   • Email                             • TransactionDate [2025-01-01 to 2025-12-30]                 |
|                                       • Amount [$0.00 to $490.90]                                  |
|                                       • PaymentMethod [PayPal, Credit Card, Bank Transfer]         |
+----------------------------------------------------------------------------------------------------+
                                                        |
                                                        v
+----------------------------------------------------------------------------------------------------+
|   COURSES SHEET (60 Rows)             TEACHERS SHEET (60 Rows)                                     |
|   • CourseID (PK)                     • TeacherID (PK)                                             |
|   • CourseName                        • TeacherName                                                |
|   • CourseCategory (12 disciplines)   • Age [27 - 50]                                              |
|   • CourseType [Free, Paid]           • Gender [Female, Male]                                      |
|   • CourseLevel [Beg, Int, Adv]       • Expertise (12 disciplines)                                 |
|   • CoursePrice [$0.00 - $490.90]     • YearsOfExperience [1 - 24]                                 |
|   • CourseDuration [1.2 - 49.7 hrs]   • TeacherRating [1.05 - 4.97]                                |
|   • CourseRating [1.13 - 4.94]        +------------------------------------------------------------+
+----------------------------------------------------------------------------------------------------+
```

| Entity | Primary Key | Total Records | Field Definitions & Attributes | Data Type | Range / Constraints |
| :--- | :--- | :---: | :--- | :---: | :--- |
| **Users** | `UserID` | 3,000 | `UserID`, `UserName`, `Age`, `Gender`, `Email` | Relational Dimension | Age: 15–35, Gender: Female/Male |
| **Courses** | `CourseID` | 60 | `CourseID`, `CourseName`, `CourseCategory`, `CourseType`, `CourseLevel`, `CoursePrice`, `CourseDuration`, `CourseRating` | Relational Dimension | 12 Categories (5 courses each), Level: Beginner/Intermediate/Advanced |
| **Teachers** | `TeacherID` | 60 | `TeacherID`, `TeacherName`, `Age`, `Gender`, `Expertise`, `YearsOfExperience`, `TeacherRating` | Relational Dimension | Experience: 1–24 years, Rating: 1.05–4.97 |
| **Transactions** | `TransactionID` | 10,000 | `TransactionID`, `UserID`, `CourseID`, `TransactionDate`, `Amount`, `PaymentMethod`, `TeacherID` | Relational Fact | Date: 2025-01-01 to 2025-12-30, Amount: \$0.00–\$490.90 |

---

## 6. Methodology

### 6.1 Analytical Workflow Pipeline
The investigation followed a 5-stage quantitative analytics pipeline:
1. **Ingestion & Validation**: Scripted data ingestion enforcing UTF-8 encoding and standard RFC email regex validation.
2. **Quality Governance**: Full verification of primary key uniqueness, foreign key integrity, and domain constraints.
3. **Feature Engineering & Life-Stage Segmentation**:
   $$\text{Age Cohort} = \begin{cases} 
   <18 \text{ (Youth)}, & \text{Age} \le 17 \\
   18\text{--}25 \text{ (Young Adult / Post-Secondary)}, & 18 \le \text{Age} \le 25 \\
   26\text{--}35 \text{ (Career Professional)}, & 26 \le \text{Age} \le 35 
   \end{cases}$$
4. **Relational Synthesis**: Master merge joining transactional fact records with learner, course, and instructor dimensions without data leakage or row inflation.
5. **Inferential Testing & Forecasting**: Execution of bivariate contingency matrices, Chi-Square tests of independence, and Double Exponential Smoothing time-series modeling.

---

## 7. Data Cleaning & Quality Assurance

To guarantee empirical validity, a formalized data quality audit protocol was developed (`src/data_loader.py`):
- **Completeness**: 0 missing, null, or undefined values detected across all 13,120 entities and records ($100\%$ completeness).
- **Referential Integrity**: An orphan key scan verified that every transaction `UserID`, `CourseID`, and `TeacherID` resolved to an existing dimension record with zero orphan records ($\text{Coverage} = 100\%$).
- **Business Rule Coherence**: Verified that $100\%$ of Free courses ($n=38$) registered transactions with $\text{Amount} = \$0.00$, while Paid courses ($n=22$) transacted at verified list prices ($>\$0.00$).
- **Outlier Assessment**: Evaluated using the Interquartile Range (IQR) technique. For learner age ($Q_1 = 20, Q_3 = 30, \text{IQR} = 10$), the outer fence $[5, 45]$ contained $100\%$ of user observations.

---

## 8. Exploratory Data Analysis (EDA)

### 8.1 Learner Demographic Characteristics

| Demographic Metric | Exact Value | Pedagogical Significance |
| :--- | :--- | :--- |
| **Total Registered Learners** | 3,000 | Verified active user population |
| **Minimum Age** | 15.0 years | Secondary school entry threshold |
| **First Quartile ($Q_1$)** | 20.0 years | Early post-secondary threshold |
| **Median Age ($Q_2$)** | 25.0 years | Workforce entry midpoint |
| **Third Quartile ($Q_3$)** | 30.0 years | Mid-career transition window |
| **Maximum Age** | 35.0 years | Platform demographic boundary |
| **Mean Age ($\mu \pm \sigma$)** | $24.97 \pm 6.05$ years | Centered on young working adults |
| **Gender Split (Users)** | 1,520 Female ($50.67\%$) vs. 1,480 Male ($49.33\%$) | Perfect demographic parity |

### 8.2 Disciplinary Enrollment Demand

```
               RANKED DISCIPLINE ENROLLMENT SHARE
  Category                 Enrollments    Share (%)     Catalog Free/Paid
  -----------------------------------------------------------------------
  Data Science                 916          9.16%         3 Free / 2 Paid
  Finance                      864          8.64%         3 Free / 2 Paid
  Web Development              844          8.44%         3 Free / 2 Paid
  Business                     833          8.33%         2 Free / 3 Paid
  Project Management           829          8.29%         2 Free / 3 Paid
  Artificial Intelligence      829          8.29%         1 Free / 4 Paid
  Design                       827          8.27%         4 Free / 1 Paid
  Cybersecurity                819          8.19%         4 Free / 1 Paid
  Machine Learning             819          8.19%         4 Free / 1 Paid
  Digital Marketing            808          8.08%         3 Free / 2 Paid
  Marketing                    806          8.06%         5 Free / 0 Paid
  Programming                  806          8.06%         4 Free / 1 Paid
```

Data Science leads all disciplines ($916$ enrollments), followed closely by Finance ($864$) and Web Development ($844$). Applied commercial and quantitative disciplines demonstrate stronger learner pull than theoretical programming.

---

## 9. Results and Findings

### 9.1 Age Cohort Behavioral Variations
Cross-tabulation of age cohorts against subject categories highlights significant life-stage patterns:
- **Youth (<18)**: Show peak relative preference for **Finance ($9.26\%$)** and **Web Development ($8.99\%$)**. Young learners actively seek practical financial literacy and front-end development capabilities.
- **Young Adults (18–25)**: Transition into core data and web technologies, with **Data Science ($9.19\%$)** and **Web Development ($8.98\%$)** leading.
- **Career Adults (26–35)**: Concentrate on high-leverage organizational mobility competencies: **Data Science ($9.56\%$)**, **Finance ($8.98\%$)**, **Project Management ($8.71\%$)**, and **Business ($8.46\%$)**.

### 9.2 Gender Equity Across STEM Disciplines
The platform achieves an overall **Gender Parity Ratio of 1.0317** ($5,078$ Female vs. $4,922$ Male enrollments). In STEM subjects:
- **Data Science**: 479 Female ($52.3\%$) vs. 437 Male ($47.7\%$)
- **Cybersecurity**: 430 Female ($52.5\%$) vs. 389 Male ($47.5\%$)
- **Programming**: 420 Female ($52.1\%$) vs. 386 Male ($47.9\%$)
- **Digital Marketing**: 417 Female ($51.6\%$) vs. 391 Male ($48.4\%$)

### 9.3 Statistical Independence Testing ($\chi^2$)
Hypothesis testing confirmed that selection of course disciplines, skill levels, and pricing tiers is statistically independent of demographic identity:

$$\chi^2 = \sum \frac{(O - E)^2}{E}, \quad V = \sqrt{\frac{\chi^2}{N(k-1)}}$$

| Test Relationship | $\chi^2$ Statistic | $df$ | $p$-Value | Cramér's $V$ | Empirical Conclusion ($\alpha = 0.05$) |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Age Cohort $\perp$ Course Category** | 18.013 | 22 | 0.7052 | 0.0300 | Independent (No demographic bias) |
| **Age Cohort $\perp$ Course Level** | 3.133 | 4 | 0.5358 | 0.0125 | Independent (Equal level access) |
| **Age Cohort $\perp$ Access Type (Free/Paid)**| 4.004 | 2 | 0.1350 | 0.0200 | Independent (No pricing penalty) |
| **Gender $\perp$ Course Category** | 8.774 | 11 | 0.6427 | 0.0296 | Independent (STEM parity achieved) |
| **Gender $\perp$ Course Level** | 0.198 | 2 | 0.9058 | 0.0044 | Independent (Equal skill progression) |
| **Gender $\perp$ Access Type (Free/Paid)** | 0.142 | 1 | 0.7058 | 0.0038 | Independent (Equal financial commitment) |

### 9.4 Engagement Concentration & Pareto Distribution
Learner velocity analysis reveals an extreme bimodal distribution:
- **Casual Trialists ($54.0\%$)**: 1,620 users enroll in exactly 1 course ($16.2\%$ of total volume).
- **Explorers ($20.4\%$)**: 612 users take 2 courses ($12.2\%$ of volume).
- **Engaged Learners ($10.5\%$)**: 314 users take 3–4 courses ($10.7\%$ of volume).
- **Power Learners ($15.1\%$)**: 454 users take 9 or more courses, generating **$60.86\%$ of all platform enrollments**.

The top $20\%$ of learners drive $66.52\%$ of total volume, reflecting a high concentration of institutional lifelong learners.

---

## 10. Discussion & Pedagogical Implications

### 10.1 The Myth of the Passive Youth Learner
The finding that youth (<18) enroll in Advanced courses at a rate of $36.35\%$ challenges traditional assumptions that adolescent students require basic gamified primers. When access barriers are removed, young learners seek substantive technical depth in algorithms, finance, and software development.

### 10.2 Resolving the Intermediate Drop-Off
Intermediate courses attract only $29.52\%$ of enrollments compared to $35.73\%$ Beginner and $34.75\%$ Advanced. Learners appear to leap directly from introductory courses into advanced certifications. Curricula should reposition intermediate modules as explicit milestone prerequisites to ensure foundational reinforcement.

### 10.3 The Single-Course Gateway Challenge
With $54.0\%$ of learners exiting after one course, EduPro's greatest opportunity for growth lies in post-completion re-engagement. Introducing structured, multi-course specialization bundles with milestone badging can transition casual trialists into multi-course completers.

---

## 11. Limitations

This study acknowledges several empirical and technical constraints:
1. **Absence of Module-Level Learning Logs**: The dataset captures enrollment and payment transactions but does not record lecture completion timestamps, quiz scores, or student drop-out events. Churn and completion rates cannot be inferred.
2. **Temporal Window**: The dataset spans exactly one calendar year (2025), preventing multi-year macroeconomic cycle decomposition.
3. **Upper Age Censoring**: User ages terminate at 35 years, reflecting a young platform demographic and leaving senior/mature learners unobserved.

---

## 12. Conclusion

This research paper delivers an auditable, data-backed descriptive intelligence framework for the EduPro online learning platform. The investigation establishes that EduPro operates as an equitable, gender-neutral learning platform where high-value STEM subjects achieve over $52\%$ female enrollment and youth demonstrate sophisticated demand for financial and web engineering coursework. By addressing the single-course drop-off through structured multi-course certification tracks and co-developing youth workforce pathways with municipal partners like Toronto Parks, Forestry & Recreation, EduPro can transform passive digital enrollments into sustainable career mobility.

---

## 13. References

1. Anderson, T. (2021). *The Theory and Practice of Online Learning*. AU Press.
2. Kizilcec, R. F., Piech, C., & Schneider, E. (2023). Deconstructing disengagement in online learning: Analyzing learner subpopulations. *Proceedings of the Third Conference on Learning @ Scale*, 112–121.
3. Reich, J., & Ruipérez-Valiente, J. A. (2019). The MOOC pivot: Massive open online courses have not transformed higher education, but they have influenced it. *Science*, 363(6423), 130–131.
4. City of Toronto. (2024). *Parks, Forestry and Recreation Strategic Plan: Equity, Inclusion and Community Recreation Services*. City of Toronto Municipal Publications.
5. Agresti, A. (2022). *Categorical Data Analysis* (3rd ed.). John Wiley & Sons.
6. Hyndman, R. J., & Athanasopoulos, G. (2021). *Forecasting: Principles and Practice* (3rd ed.). OTexts.
7. UNESCO. (2022). *Cracking the Code: Girls' and Women's Education in Science, Technology, Engineering and Mathematics (STEM)*. United Nations Educational, Scientific and Cultural Organization.

---
*End of Research Paper.*
