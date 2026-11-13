"""
visualizations.py - Reusable interactive Plotly charts for EduPro analytics dashboard.
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

COLOR_PALETTE = {
    'primary': '#2563EB',     # Royal Blue
    'secondary': '#7C3AED',   # Purple
    'accent': '#10B981',      # Emerald Green
    'warning': '#F59E0B',     # Amber
    'danger': '#EF4444',      # Red
    'teal': '#06B6D4',        # Cyan/Teal
    'female': '#EC4899',      # Pink/Rose
    'male': '#3B82F6',        # Blue
    'free': '#10B981',        # Emerald
    'paid': '#F59E0B',        # Amber
}

CHART_THEME = "plotly_white"

def plot_age_distribution(df_users):
    """Histogram & KDE of user age distribution."""
    fig = px.histogram(
        df_users,
        x='Age',
        color='Gender',
        barmode='overlay',
        nbins=21,
        color_discrete_map={'Female': COLOR_PALETTE['female'], 'Male': COLOR_PALETTE['male']},
        title="<b>Learner Age Distribution by Gender</b>",
        labels={'Age': 'Learner Age (Years)', 'count': 'Number of Learners'},
        template=CHART_THEME
    )
    fig.update_layout(
        bargap=0.1,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig

def plot_gender_split(df_users):
    """Donut chart for gender participation ratio."""
    counts = df_users['Gender'].value_counts().reset_index()
    counts.columns = ['Gender', 'Count']
    fig = px.pie(
        counts,
        names='Gender',
        values='Count',
        hole=0.55,
        color='Gender',
        color_discrete_map={'Female': COLOR_PALETTE['female'], 'Male': COLOR_PALETTE['male']},
        title="<b>Gender Participation Ratio (Inclusivity Index)</b>",
        template=CHART_THEME
    )
    fig.update_traces(textposition='inside', textinfo='percent+label', marker=dict(line=dict(color='#FFFFFF', width=2)))
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5),
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig

def plot_age_group_enrollments(df):
    """Bar chart of enrollments across age segments."""
    age_counts = df['AgeGroup'].value_counts().reset_index()
    age_counts.columns = ['AgeGroup', 'Enrollments']
    age_counts = age_counts.sort_values(by='Enrollments', ascending=True)

    fig = px.bar(
        age_counts,
        x='Enrollments',
        y='AgeGroup',
        orientation='h',
        text='Enrollments',
        color='Enrollments',
        color_continuous_scale='Blues',
        title="<b>Total Course Enrollments by Age Group</b>",
        labels={'Enrollments': 'Total Course Enrollments', 'AgeGroup': 'Age Cohort'},
        template=CHART_THEME
    )
    fig.update_traces(textposition='outside')
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        coloraxis_showscale=False,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig

def plot_category_popularity(df):
    """Ranked horizontal bar chart of Course Categories."""
    cat_counts = df['CourseCategory'].value_counts().reset_index()
    cat_counts.columns = ['Category', 'Enrollments']
    cat_counts = cat_counts.sort_values(by='Enrollments', ascending=True)

    fig = px.bar(
        cat_counts,
        x='Enrollments',
        y='Category',
        orientation='h',
        text='Enrollments',
        color='Enrollments',
        color_continuous_scale='Viridis',
        title="<b>Category Popularity Index (Enrollment Demand)</b>",
        labels={'Enrollments': 'Total Enrollments', 'Category': 'Subject Discipline'},
        template=CHART_THEME
    )
    fig.update_traces(textposition='outside')
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        coloraxis_showscale=False,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig

def plot_age_vs_category_heatmap(df):
    """Heatmap showing demographic segment preferences across subject areas."""
    ct = pd.crosstab(df['AgeGroup'], df['CourseCategory'])
    fig = px.imshow(
        ct,
        text_auto=True,
        aspect="auto",
        color_continuous_scale='YlGnBu',
        title="<b>Age Cohort × Course Category Enrollment Matrix</b>",
        labels=dict(x="Course Category", y="Age Cohort", color="Enrollments"),
        template=CHART_THEME
    )
    fig.update_layout(
        xaxis_tickangle=-45,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=50, b=50)
    )
    return fig

def plot_gender_vs_category(df):
    """Grouped bar chart for gender differences in course category selection."""
    ct = df.groupby(['CourseCategory', 'Gender']).size().reset_index(name='Enrollments')
    fig = px.bar(
        ct,
        x='CourseCategory',
        y='Enrollments',
        color='Gender',
        barmode='group',
        color_discrete_map={'Female': COLOR_PALETTE['female'], 'Male': COLOR_PALETTE['male']},
        title="<b>Gender Comparison Across Course Categories</b>",
        labels={'CourseCategory': 'Course Category', 'Enrollments': 'Total Enrollments'},
        template=CHART_THEME
    )
    fig.update_layout(
        xaxis_tickangle=-45,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=20, r=20, t=50, b=50)
    )
    return fig

def plot_level_distribution_by_age(df):
    """Stacked / Normalized bar chart of Course Level preference by Age Cohort."""
    ct = pd.crosstab(df['AgeGroup'], df['CourseLevel'], normalize='index') * 100
    ct = ct.reset_index().melt(id_vars='AgeGroup', var_name='CourseLevel', value_name='Percentage')
    
    level_colors = {'Beginner': '#38BDF8', 'Intermediate': '#818CF8', 'Advanced': '#C084FC'}
    fig = px.bar(
        ct,
        x='AgeGroup',
        y='Percentage',
        color='CourseLevel',
        barmode='stack',
        text=ct['Percentage'].apply(lambda x: f"{x:.1f}%"),
        color_discrete_map=level_colors,
        title="<b>Skill Maturity Distribution (Course Level Preference by Age)</b>",
        labels={'Percentage': 'Share within Age Cohort (%)', 'AgeGroup': 'Age Cohort'},
        template=CHART_THEME
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig

def plot_free_vs_paid_by_category(df):
    """Grouped or stacked bar chart of Free vs Paid courses by category."""
    ct = df.groupby(['CourseCategory', 'CourseType']).size().reset_index(name='Enrollments')
    fig = px.bar(
        ct,
        x='CourseCategory',
        y='Enrollments',
        color='CourseType',
        barmode='stack',
        color_discrete_map={'Free': COLOR_PALETTE['free'], 'Paid': COLOR_PALETTE['paid']},
        title="<b>Free vs. Paid Course Enrollments by Category</b>",
        labels={'CourseCategory': 'Course Category', 'Enrollments': 'Enrollments'},
        template=CHART_THEME
    )
    fig.update_layout(
        xaxis_tickangle=-45,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=20, r=20, t=50, b=50)
    )
    return fig

def plot_user_engagement_tiers(df_users):
    """Pie/Donut chart and bar showing user activity concentration (Pareto distribution)."""
    if 'LearnerTier' not in df_users.columns:
        if 'TotalCoursesEnrolled' in df_users.columns:
            counts = df_users['TotalCoursesEnrolled']
        else:
            counts = df_users.groupby('UserID').size()
        user_bins = [0, 1, 2, 4, 8, 50]
        user_labels = ['Casual (1 course)', 'Explorer (2 courses)', 'Engaged (3-4 courses)', 'Active (5-8 courses)', 'Power Learner (9+ courses)']
        tiers = pd.cut(counts, bins=user_bins, labels=user_labels)
        tier_counts = tiers.value_counts().reset_index()
        tier_counts.columns = ['Tier', 'Users']
    else:
        tier_counts = df_users['LearnerTier'].value_counts().reset_index()
        tier_counts.columns = ['Tier', 'Users']
    
    fig = px.pie(
        tier_counts,
        names='Tier',
        values='Users',
        hole=0.45,
        color='Tier',
        color_discrete_sequence=px.colors.sequential.Plasma,
        title="<b>Learner Engagement Segmentation (Activity Tiers)</b>",
        template=CHART_THEME
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig

def plot_enrollment_concentration(df):
    """Bar chart illustrating share of enrollments driven by learner tiers."""
    user_tx = df.groupby('UserID').size()
    user_bins = [0, 1, 2, 4, 8, 50]
    user_labels = ['Casual (1 course)', 'Explorer (2 courses)', 'Engaged (3-4 courses)', 'Active (5-8 courses)', 'Power Learner (9+ courses)']
    user_tiers = pd.cut(user_tx, bins=user_bins, labels=user_labels)
    tier_share = user_tx.groupby(user_tiers, observed=False).sum().reset_index()
    tier_share.columns = ['Learner Tier', 'Total Enrollments']
    tier_share['Share (%)'] = (tier_share['Total Enrollments'] / tier_share['Total Enrollments'].sum()) * 100

    fig = px.bar(
        tier_share,
        x='Learner Tier',
        y='Total Enrollments',
        text=tier_share['Share (%)'].apply(lambda x: f"{x:.1f}%"),
        color='Total Enrollments',
        color_continuous_scale='Purples',
        title="<b>Enrollment Volume Concentration by Learner Activity Tier</b>",
        template=CHART_THEME
    )
    fig.update_traces(textposition='outside')
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        coloraxis_showscale=False,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig

def plot_monthly_timeline(df):
    """Monthly enrollment trend line."""
    monthly = df.groupby(['YearMonth', 'CourseType']).size().reset_index(name='Enrollments')
    fig = px.line(
        monthly,
        x='YearMonth',
        y='Enrollments',
        color='CourseType',
        markers=True,
        color_discrete_map={'Free': COLOR_PALETTE['free'], 'Paid': COLOR_PALETTE['paid']},
        title="<b>Temporal Enrollment Velocity (2025 Monthly Timeline)</b>",
        labels={'YearMonth': 'Month', 'Enrollments': 'Enrollments'},
        template=CHART_THEME
    )
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig

def plot_payment_methods(df):
    """Donut chart of payment channels."""
    pm = df['PaymentMethod'].value_counts().reset_index()
    pm.columns = ['PaymentMethod', 'Count']
    fig = px.pie(
        pm,
        names='PaymentMethod',
        values='Count',
        hole=0.5,
        color='PaymentMethod',
        color_discrete_sequence=['#3B82F6', '#10B981', '#8B5CF6'],
        title="<b>Payment Method Distribution</b>",
        template=CHART_THEME
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig
