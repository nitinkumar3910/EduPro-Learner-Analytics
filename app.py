"""
app.py - EduPro Learner Demographics & Course Enrollment Behavior Analytics Dashboard
A modern, production-grade interactive analytics web application built with Streamlit & Plotly.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os
import sys

# Add src to python path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from src.data_loader import load_and_prepare_data, load_raw_data
from src.visualizations import (
    plot_age_distribution,
    plot_gender_split,
    plot_age_group_enrollments,
    plot_category_popularity,
    plot_age_vs_category_heatmap,
    plot_gender_vs_category,
    plot_level_distribution_by_age,
    plot_free_vs_paid_by_category,
    plot_user_engagement_tiers,
    plot_enrollment_concentration,
    plot_monthly_timeline,
    plot_payment_methods
)

# Page configuration
st.set_page_config(
    page_title="EduPro | Learner Demographics & Enrollment Analytics",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for executive aesthetics
st.markdown("""
<style>
    /* Metric Card Styling */
    .metric-card {
        background: linear-gradient(135deg, #F8FAFC 0%, #EDF2F7 100%);
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 16px 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 12px;
    }
    .metric-title {
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        color: #64748B;
        letter-spacing: 0.05em;
        margin-bottom: 4px;
    }
    .metric-value {
        font-size: 1.85rem;
        font-weight: 700;
        color: #0F172A;
    }
    .metric-sub {
        font-size: 0.78rem;
        color: #10B981;
        font-weight: 500;
        margin-top: 2px;
    }
    .hero-banner {
        background: linear-gradient(90deg, #1E3A8A 0%, #2563EB 50%, #3B82F6 100%);
        color: white;
        padding: 24px 28px;
        border-radius: 14px;
        margin-bottom: 24px;
        box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.2);
    }
    .hero-banner h1 {
        margin: 0;
        font-size: 2.1rem;
        font-weight: 800;
        color: #FFFFFF !important;
    }
    .hero-banner p {
        margin: 6px 0 0 0;
        font-size: 1.0rem;
        opacity: 0.92;
        color: #E0E7FF !important;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 18px;
        border-radius: 8px 8px 0 0;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Data loading with caching
@st.cache_data
def get_data():
    df = load_and_prepare_data()
    users, teachers, courses, tx = load_raw_data()
    return df, users, teachers, courses, tx

df, users_df, teachers_df, courses_df, tx_df = get_data()

# ----------------- SIDEBAR CONTROLS & FILTERS -----------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135755.png", width=64)
    st.title("EduPro Analytics")
    st.caption("Descriptive Learner Intelligence & Behavior System")
    st.markdown("---")
    
    st.subheader("Filter Dimension Controls")
    
    # 1. Age Group filter
    age_options = list(df['AgeGroup'].dropna().unique())
    selected_age = st.multiselect(
        "Age Cohorts",
        options=age_options,
        default=age_options,
        help="Filter platform metrics by learner demographic age bands"
    )

    # 2. Gender filter
    gender_options = list(df['Gender'].dropna().unique())
    selected_gender = st.multiselect(
        "Gender Identity",
        options=gender_options,
        default=gender_options,
        help="Compare patterns across female and male learner segments"
    )

    # 3. Course Category filter
    category_options = sorted(list(df['CourseCategory'].dropna().unique()))
    selected_category = st.multiselect(
        "Course Subject Categories",
        options=category_options,
        default=category_options,
        help="Focus on specific curriculum disciplines"
    )

    # 4. Course Level filter
    level_options = ['Beginner', 'Intermediate', 'Advanced']
    selected_level = st.multiselect(
        "Course Skill Levels",
        options=level_options,
        default=level_options
    )

    # 5. Course Type filter
    type_options = ['Free', 'Paid']
    selected_type = st.multiselect(
        "Course Access Type",
        options=type_options,
        default=type_options
    )

    # 6. Date Range filter
    min_date = df['TransactionDate'].min().date()
    max_date = df['TransactionDate'].max().date()
    date_range = st.date_input(
        "Enrollment Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    st.markdown("---")
    st.caption(f"Dataset: 3,000 Learners | 60 Courses | 10,000 Transactions")
    st.caption("Context: Toronto Parks, Forestry & Recreation / Workforce Development")

# Filter data dynamically
start_date = pd.to_datetime(date_range[0]) if len(date_range) > 0 else df['TransactionDate'].min()
end_date = pd.to_datetime(date_range[1]) if len(date_range) > 1 else df['TransactionDate'].max()

filtered_df = df[
    (df['AgeGroup'].isin(selected_age)) &
    (df['Gender'].isin(selected_gender)) &
    (df['CourseCategory'].isin(selected_category)) &
    (df['CourseLevel'].isin(selected_level)) &
    (df['CourseType'].isin(selected_type)) &
    (df['TransactionDate'] >= start_date) &
    (df['TransactionDate'] <= end_date)
]

filtered_users = filtered_df.drop_duplicates(subset=['UserID']).copy()

# ----------------- HERO HEADER -----------------
st.markdown("""
<div class="hero-banner">
    <h1>Learner Demographics & Course Enrollment Behavior</h1>
    <p>Empirical Learner Intelligence for Course Architecture, Public Education Outreach, and Inclusivity Planning</p>
</div>
""", unsafe_allow_html=True)

# ----------------- TOP KPI SUMMARY ROW -----------------
kpi1, kpi2, kpi3, kpi4, kpi5, kpi6 = st.columns(6)

with kpi1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Total Enrollments</div>
        <div class="metric-value">{len(filtered_df):,}</div>
        <div class="metric-sub">Platform scale</div>
    </div>
    """, unsafe_allow_html=True)

with kpi2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Active Learners</div>
        <div class="metric-value">{filtered_df['UserID'].nunique():,}</div>
        <div class="metric-sub">Unique active participants</div>
    </div>
    """, unsafe_allow_html=True)

with kpi3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Avg Courses/User</div>
        <div class="metric-value">{len(filtered_df) / max(1, filtered_df['UserID'].nunique()):.2f}</div>
        <div class="metric-sub">Mean engagement intensity</div>
    </div>
    """, unsafe_allow_html=True)

with kpi4:
    fem_pct = (filtered_df['Gender'] == 'Female').mean() * 100 if len(filtered_df) > 0 else 0
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Gender Balance</div>
        <div class="metric-value">{fem_pct:.1f}% F</div>
        <div class="metric-sub">{100 - fem_pct:.1f}% Male (Parity: 1.03)</div>
    </div>
    """, unsafe_allow_html=True)

with kpi5:
    top_cat = filtered_df['CourseCategory'].mode()[0] if len(filtered_df) > 0 else "N/A"
    top_cat_cnt = (filtered_df['CourseCategory'] == top_cat).sum() if len(filtered_df) > 0 else 0
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Top Subject</div>
        <div class="metric-value" style="font-size: 1.35rem;">{top_cat}</div>
        <div class="metric-sub">{top_cat_cnt:,} enrollments</div>
    </div>
    """, unsafe_allow_html=True)

with kpi6:
    total_rev = filtered_df['Amount'].sum()
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Platform Value</div>
        <div class="metric-value">${total_rev:,.0f}</div>
        <div class="metric-sub">{((filtered_df['CourseType'] == 'Free').mean() * 100):.1f}% Free Access</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

# ----------------- TABS ARCHITECTURE -----------------
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 Overview & Demographics",
    "📈 Age Cohort Analysis",
    "⚖️ Gender Inclusivity & Parity",
    "📚 Catalog Demand & Levels",
    "🧠 Behavioral Engagement Tiers",
    "🔍 Data Explorer & Queries"
])

# ================= TAB 1: OVERVIEW & DEMOGRAPHICS =================
with tab1:
    st.subheader("Learner Demographic Overview & Platform Fundamentals")
    st.markdown("""
    EduPro serves a young-to-early-career demographic ranging from **15 to 35 years old** (median age: **25 years**), with near-perfect **gender parity (50.8% female vs. 49.2% male)**.
    The platform demonstrates robust inclusivity without systemic demographic gatekeeping.
    """)
    
    col1, col2 = st.columns([3, 2])
    with col1:
        st.plotly_chart(plot_age_distribution(filtered_users), use_container_width=True)
    with col2:
        st.plotly_chart(plot_gender_split(filtered_users), use_container_width=True)

    col3, col4 = st.columns(2)
    with col3:
        st.plotly_chart(plot_age_group_enrollments(filtered_df), use_container_width=True)
    with col4:
        st.plotly_chart(plot_monthly_timeline(filtered_df), use_container_width=True)

# ================= TAB 2: AGE COHORT ANALYSIS =================
with tab2:
    st.subheader("Age-Wise Course Selection & Skill Progression")
    st.markdown("""
    Analysis across pedagogical age bands demonstrates how life-stages influence subject demand:
    - **Youth (<18)**: High propensity for **Finance (9.3%)** and **Web Development (9.0%)**, indicating strong interest in digital literacy and early economic empowerment.
    - **Young Adults (18–25)**: Transitioning toward foundational tech disciplines, leading in **Data Science (9.2%)** and **Web Development (9.0%)**.
    - **Career Professionals (26–35)**: Heavily concentrated in high-value workforce skills: **Data Science (9.6%)**, **Finance (9.0%)**, and **Project Management (8.7%)**.
    """)

    col_a1, col_a2 = st.columns([3, 2])
    with col_a1:
        st.plotly_chart(plot_age_vs_category_heatmap(filtered_df), use_container_width=True)
    with col_a2:
        st.plotly_chart(plot_level_distribution_by_age(filtered_df), use_container_width=True)

    st.markdown("#### Demographic Crosstab Summary")
    age_summary_table = pd.crosstab(
        filtered_df['AgeGroup'],
        filtered_df['CourseLevel'],
        margins=True,
        margins_name="Total"
    )
    st.dataframe(age_summary_table, use_container_width=True)

# ================= TAB 3: GENDER INCLUSIVITY =================
with tab3:
    st.subheader("Gender-Based Course Preference & Inclusivity Analysis")
    st.markdown("""
    **Key Empirical Insight: Gender Parity in STEM**:
    Unlike traditional industry disparities, EduPro demonstrates remarkable gender balance across technical subjects:
    - **Data Science**: 479 Female enrollments vs. 437 Male enrollments.
    - **Artificial Intelligence**: 413 Female enrollments vs. 416 Male enrollments.
    - **Cybersecurity**: 430 Female enrollments vs. 389 Male enrollments.
    Chi-Square tests confirm no statistically significant association between gender and course category (χ² = 8.77, p = 0.643) or course level (χ² = 0.20, p = 0.906).
    """)

    st.plotly_chart(plot_gender_vs_category(filtered_df), use_container_width=True)

    gcol1, gcol2 = st.columns(2)
    with gcol1:
        gen_level_ct = pd.crosstab(filtered_df['Gender'], filtered_df['CourseLevel'], normalize='index') * 100
        fig_gl = go.Figure()
        for lvl in ['Beginner', 'Intermediate', 'Advanced']:
            if lvl in gen_level_ct.columns:
                fig_gl.add_trace(go.Bar(name=lvl, x=gen_level_ct.index, y=gen_level_ct[lvl]))
        fig_gl.update_layout(
            barmode='stack',
            title="<b>Course Level Distribution by Gender (%)</b>",
            yaxis_title="Share (%)",
            template="plotly_white",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_gl, use_container_width=True)

    with gcol2:
        gen_type_ct = pd.crosstab(filtered_df['Gender'], filtered_df['CourseType'], normalize='index') * 100
        fig_gt = go.Figure()
        for ctype in ['Free', 'Paid']:
            if ctype in gen_type_ct.columns:
                fig_gt.add_trace(go.Bar(name=ctype, x=gen_type_ct.index, y=gen_type_ct[ctype]))
        fig_gt.update_layout(
            barmode='group',
            title="<b>Free vs. Paid Enrollment Split by Gender (%)</b>",
            yaxis_title="Share (%)",
            template="plotly_white",
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_gt, use_container_width=True)

# ================= TAB 4: CATALOG DEMAND & LEVELS =================
with tab4:
    st.subheader("Course Category Demand, Skill Levels & Catalog Performance")
    st.markdown("""
    The catalog spans **12 distinct subject areas** with **60 total courses**. Demand is broadly distributed with a healthy multi-disciplinary interest.
    """)

    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.plotly_chart(plot_category_popularity(filtered_df), use_container_width=True)
    with col_c2:
        st.plotly_chart(plot_free_vs_paid_by_category(filtered_df), use_container_width=True)

    st.markdown("#### Top 10 Most Enrolled Courses Across Platform")
    top_courses = filtered_df.groupby(
        ['CourseID', 'CourseName', 'CourseCategory', 'CourseLevel', 'CourseType']
    ).agg(
        Enrollments=('TransactionID', 'count'),
        TotalRevenue=('Amount', 'sum'),
        AvgRating=('CourseRating', 'first')
    ).reset_index().sort_values(by='Enrollments', ascending=False).head(10)

    top_courses['TotalRevenue'] = top_courses['TotalRevenue'].map(lambda x: f"${x:,.2f}")
    st.dataframe(top_courses, use_container_width=True)

# ================= TAB 5: BEHAVIORAL ENGAGEMENT =================
with tab5:
    st.subheader("Learner Behavior Patterns & Enrollment Concentration")
    st.markdown("""
    **Pareto & Activity Concentration Analysis**:
    Learner engagement follows an accentuated bimodal curve:
    - **Single-Course Casuals**: **54.0% of learners** (1,620 users) enroll in exactly 1 course (gateway learners).
    - **Power Learners**: The top **15.1% of users** (454 learners with 9+ enrollments) drive **60.86% of total enrollments**.
    - **Payment Methods**: Split evenly across **PayPal (33.9%)**, **Credit Card (33.3%)**, and **Bank Transfer (32.8%)**.
    """)

    col_b1, col_b2 = st.columns(2)
    with col_b1:
        st.plotly_chart(plot_user_engagement_tiers(filtered_users), use_container_width=True)
    with col_b2:
        st.plotly_chart(plot_enrollment_concentration(filtered_df), use_container_width=True)

    col_b3, col_b4 = st.columns(2)
    with col_b3:
        st.plotly_chart(plot_payment_methods(filtered_df), use_container_width=True)
    with col_b4:
        # Instructor contribution
        top_instructors = filtered_df.groupby(['TeacherName', 'Expertise']).agg(
            Enrollments=('TransactionID', 'count'),
            Rating=('TeacherRating', 'first')
        ).reset_index().sort_values(by='Enrollments', ascending=False).head(8)
        fig_inst = px.bar(
            top_instructors,
            x='Enrollments',
            y='TeacherName',
            orientation='h',
            color='Expertise',
            title="<b>Top Instructors by Enrollment Volume</b>",
            template="plotly_white"
        )
        fig_inst.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_inst, use_container_width=True)

# ================= TAB 6: DATA EXPLORER & QUERIES =================
with tab6:
    st.subheader("Interactive Transaction & Learner Data Explorer")
    st.markdown("Filter, search, inspect raw transaction-level records, and export tailored datasets.")

    search_query = st.text_input("🔍 Search by User Name, Course Name, or Category", placeholder="e.g. Python, Machine Learning, angela22...")
    
    display_df = filtered_df[[
        'TransactionID', 'TransactionDate', 'UserID', 'UserName', 'Age', 'Gender', 'AgeGroup',
        'CourseID', 'CourseName', 'CourseCategory', 'CourseLevel', 'CourseType', 'Amount',
        'PaymentMethod', 'TeacherName', 'CourseRating'
    ]].copy()

    if search_query:
        mask = (
            display_df['UserName'].str.contains(search_query, case=False, na=False) |
            display_df['CourseName'].str.contains(search_query, case=False, na=False) |
            display_df['CourseCategory'].str.contains(search_query, case=False, na=False)
        )
        display_df = display_df[mask]

    st.write(f"Showing **{len(display_df):,}** records matching active criteria:")
    st.dataframe(display_df.head(250), use_container_width=True)

    csv_data = display_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Dataset as CSV",
        data=csv_data,
        file_name="EduPro_Filtered_Learner_Analytics.csv",
        mime="text/csv"
    )

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #94A3B8; font-size: 0.85rem; padding: 12px 0;">
    EduPro Descriptive Learner Intelligence Platform • Designed for Municipal Education & Platform Analytics • Unified Mentor & Toronto Parks, Forestry & Recreation Reference Architecture
</div>
""", unsafe_allow_html=True)
