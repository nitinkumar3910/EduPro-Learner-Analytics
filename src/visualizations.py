"""
visualizations.py - Professional Interactive Plotly Visualizations Engine
EduPro Learner Demographics & Course Enrollment Behavior Analytics
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Executive Theme Palette (Navy Blue, Slate, Emerald, Coral, Amethyst)
THEME_COLORS = {
    'primary': '#1E3A8A',       # Deep Navy
    'secondary': '#2563EB',     # Royal Blue
    'accent_blue': '#38BDF8',   # Sky Blue
    'female': '#EC4899',        # Rose / Pink
    'male': '#2563EB',          # Blue
    'free': '#10B981',          # Emerald Green
    'paid': '#F59E0B',          # Amber / Gold
    'beginner': '#06B6D4',      # Cyan
    'intermediate': '#8B5CF6',  # Violet
    'advanced': '#EC4899',      # Fuchsia
    'neutral_light': '#F8FAFC',
    'neutral_dark': '#0F172A',
    'border_gray': '#E2E8F0'
}

CHART_TEMPLATE = "plotly_white"

def _apply_standard_layout(fig, title, height=420):
    """Apply consistent corporate typography, margin, and transparent background."""
    fig.update_layout(
        title=dict(text=title, font=dict(size=15, color='#0F172A', family='Inter, sans-serif')),
        template=CHART_TEMPLATE,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family='Inter, sans-serif', color='#334155', size=12),
        margin=dict(l=24, r=24, t=54, b=32),
        height=height
    )
    return fig

# ----------------- SECTION 1: LEARNER DEMOGRAPHICS -----------------

def plot_age_distribution_box(df_users):
    """Combined Histogram and Marginal Boxplot for learner age distribution."""
    fig = px.histogram(
        df_users,
        x='Age',
        color='Gender',
        marginal='box',
        nbins=21,
        barmode='overlay',
        color_discrete_map={'Female': THEME_COLORS['female'], 'Male': THEME_COLORS['male']},
        labels={'Age': 'Learner Age (Years)', 'count': 'Number of Learners'},
        opacity=0.75
    )
    fig = _apply_standard_layout(fig, "<b>Learner Age Distribution & Spread by Gender</b>", height=430)
    fig.update_layout(
        bargap=0.08,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig

def plot_gender_participation_donut(df_users):
    """Donut chart illustrating overall gender participation ratio."""
    counts = df_users['Gender'].value_counts().reset_index()
    counts.columns = ['Gender', 'Count']
    total = counts['Count'].sum()
    counts['Percentage'] = (counts['Count'] / total * 100).round(1)

    fig = go.Figure(data=[go.Pie(
        labels=counts['Gender'],
        values=counts['Count'],
        hole=0.58,
        marker=dict(
            colors=[THEME_COLORS['female'] if g == 'Female' else THEME_COLORS['male'] for g in counts['Gender']],
            line=dict(color='#FFFFFF', width=2)
        ),
        textinfo='label+percent',
        hovertemplate="<b>%{label}</b><br>Count: %{value:,}<br>Share: %{percent}<extra></extra>"
    )])
    fig.add_annotation(
        text=f"<b>{total:,}</b><br><span style='font-size:10px; color:#64748B;'>Learners</span>",
        x=0.5, y=0.5, showarrow=False, font=dict(size=14, color='#0F172A')
    )
    fig = _apply_standard_layout(fig, "<b>Gender Participation Ratio (Inclusivity Index)</b>", height=380)
    fig.update_layout(showlegend=False)
    return fig

def plot_age_cohort_breakdown(df_users):
    """Bar chart showing representation across pedagogical age bands."""
    counts = df_users['AgeGroup'].value_counts().reset_index()
    counts.columns = ['AgeGroup', 'Learners']
    counts = counts.sort_values(by='Learners', ascending=True)
    total = counts['Learners'].sum()
    counts['Share'] = (counts['Learners'] / total * 100).round(1)

    fig = px.bar(
        counts,
        x='Learners',
        y='AgeGroup',
        orientation='h',
        text=counts['Share'].apply(lambda x: f"{x}%"),
        color='Learners',
        color_continuous_scale='Blues',
        labels={'Learners': 'Total Registered Learners', 'AgeGroup': 'Age Cohort'}
    )
    fig.update_traces(textposition='outside')
    fig = _apply_standard_layout(fig, "<b>Learner Distribution by Pedagogical Age Cohort</b>", height=380)
    fig.update_layout(coloraxis_showscale=False)
    return fig

# ----------------- SECTION 2: COURSE ENROLLMENT ANALYSIS -----------------

def plot_category_popularity_ranked(df):
    """Ranked horizontal bar chart of Course Categories with enrollment counts."""
    cat_counts = df['CourseCategory'].value_counts().reset_index()
    cat_counts.columns = ['Category', 'Enrollments']
    cat_counts = cat_counts.sort_values(by='Enrollments', ascending=True)
    total = len(df)
    cat_counts['Pct'] = (cat_counts['Enrollments'] / total * 100).round(1)

    fig = px.bar(
        cat_counts,
        x='Enrollments',
        y='Category',
        orientation='h',
        text=cat_counts.apply(lambda r: f"{r['Enrollments']:,} ({r['Pct']}%)", axis=1),
        color='Enrollments',
        color_continuous_scale='Viridis',
        labels={'Enrollments': 'Total Course Enrollments', 'Category': 'Subject Discipline'}
    )
    fig.update_traces(textposition='outside')
    fig = _apply_standard_layout(fig, "<b>Category Demand Index (Total Enrollments)</b>", height=450)
    fig.update_layout(coloraxis_showscale=False)
    return fig

def plot_level_distribution_donut(df):
    """Donut chart showing skill level distribution."""
    lvl = df['CourseLevel'].value_counts().reset_index()
    lvl.columns = ['Level', 'Enrollments']
    
    color_map = {
        'Beginner': THEME_COLORS['beginner'],
        'Intermediate': THEME_COLORS['intermediate'],
        'Advanced': THEME_COLORS['advanced']
    }

    fig = go.Figure(data=[go.Pie(
        labels=lvl['Level'],
        values=lvl['Enrollments'],
        hole=0.55,
        marker=dict(colors=[color_map.get(l, '#94A3B8') for l in lvl['Level']], line=dict(color='#FFFFFF', width=2)),
        textinfo='label+percent',
        hovertemplate="<b>%{label} Level</b><br>Enrollments: %{value:,}<br>Share: %{percent}<extra></extra>"
    )])
    fig = _apply_standard_layout(fig, "<b>Course Skill Level Preference</b>", height=380)
    fig.update_layout(showlegend=False)
    return fig

def plot_free_vs_paid_by_category(df):
    """Grouped bar chart comparing Free vs Paid enrollments per discipline."""
    grouped = df.groupby(['CourseCategory', 'CourseType']).size().reset_index(name='Enrollments')
    fig = px.bar(
        grouped,
        x='CourseCategory',
        y='Enrollments',
        color='CourseType',
        barmode='group',
        color_discrete_map={'Free': THEME_COLORS['free'], 'Paid': THEME_COLORS['paid']},
        labels={'CourseCategory': 'Course Category', 'Enrollments': 'Enrollments'}
    )
    fig = _apply_standard_layout(fig, "<b>Free vs. Paid Course Enrollments by Category</b>", height=420)
    fig.update_layout(
        xaxis_tickangle=-40,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig

def plot_top_and_bottom_courses(df, n=8):
    """Side-by-side or stacked horizontal bar charts showing top and lowest enrolled courses."""
    course_counts = df.groupby(['CourseID', 'CourseName', 'CourseCategory', 'CourseLevel', 'CourseType']).size().reset_index(name='Enrollments')
    
    top_n = course_counts.sort_values(by='Enrollments', ascending=False).head(n)
    bottom_n = course_counts.sort_values(by='Enrollments', ascending=True).head(n)

    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=top_n['CourseName'],
        x=top_n['Enrollments'],
        orientation='h',
        name='Top Enrolled',
        marker_color=THEME_COLORS['secondary'],
        text=top_n['Enrollments'],
        textposition='outside'
    ))
    fig = _apply_standard_layout(fig, f"<b>Top {n} Most Enrolled Courses</b>", height=380)
    fig.update_layout(yaxis=dict(autorange="reversed"), showlegend=False)
    return fig

# ----------------- SECTION 3: ADVANCED CROSS-TABULATIONS -----------------

def plot_age_vs_category_heatmap(df):
    """Heatmap displaying enrollment concentration across age groups and subject disciplines."""
    ct = pd.crosstab(df['AgeGroup'], df['CourseCategory'])
    fig = px.imshow(
        ct,
        text_auto=True,
        aspect="auto",
        color_continuous_scale='YlGnBu',
        labels=dict(x="Subject Category", y="Age Cohort", color="Enrollments")
    )
    fig = _apply_standard_layout(fig, "<b>Age Cohort × Course Category Enrollment Matrix</b>", height=400)
    fig.update_layout(xaxis_tickangle=-40)
    return fig

def plot_gender_vs_category_diverging(df):
    """Grouped bar chart illustrating gender parity across subject disciplines."""
    grouped = df.groupby(['CourseCategory', 'Gender']).size().reset_index(name='Enrollments')
    fig = px.bar(
        grouped,
        x='CourseCategory',
        y='Enrollments',
        color='Gender',
        barmode='group',
        color_discrete_map={'Female': THEME_COLORS['female'], 'Male': THEME_COLORS['male']},
        labels={'CourseCategory': 'Course Category', 'Enrollments': 'Total Enrollments'}
    )
    fig = _apply_standard_layout(fig, "<b>Gender Representation Across Subject Categories</b>", height=420)
    fig.update_layout(
        xaxis_tickangle=-40,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig

def plot_level_by_age_stacked(df):
    """Normalized stacked bar chart showing course skill level choice across age cohorts."""
    ct = pd.crosstab(df['AgeGroup'], df['CourseLevel'], normalize='index') * 100
    ct = ct.reset_index().melt(id_vars='AgeGroup', var_name='CourseLevel', value_name='Percentage')
    
    color_map = {
        'Beginner': THEME_COLORS['beginner'],
        'Intermediate': THEME_COLORS['intermediate'],
        'Advanced': THEME_COLORS['advanced']
    }

    fig = px.bar(
        ct,
        x='AgeGroup',
        y='Percentage',
        color='CourseLevel',
        barmode='stack',
        text=ct['Percentage'].apply(lambda v: f"{v:.1f}%"),
        color_discrete_map=color_map,
        labels={'Percentage': 'Share within Cohort (%)', 'AgeGroup': 'Age Cohort'}
    )
    fig = _apply_standard_layout(fig, "<b>Course Skill Level Preference by Age Cohort (%)</b>", height=400)
    fig.update_layout(
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig

def plot_pareto_concentration(df):
    """Lorenz / Pareto cumulative concentration curve of user enrollments."""
    user_counts = df.groupby('UserID').size().sort_values(ascending=False).values
    total_enrollments = user_counts.sum()
    total_users = len(user_counts)

    cum_users_pct = (np.arange(1, total_users + 1) / total_users) * 100
    cum_enrollments_pct = (np.cumsum(user_counts) / total_enrollments) * 100

    fig = go.Figure()
    # 45-degree equality line
    fig.add_trace(go.Scatter(
        x=[0, 100], y=[0, 100],
        mode='lines',
        name='Perfect Equality Line',
        line=dict(color='#94A3B8', dash='dash')
    ))
    # Actual Lorenz curve
    fig.add_trace(go.Scatter(
        x=np.insert(cum_users_pct, 0, 0),
        y=np.insert(cum_enrollments_pct, 0, 0),
        mode='lines',
        name='Actual Learner Concentration',
        line=dict(color=THEME_COLORS['primary'], width=3),
        fill='tonexty',
        fillcolor='rgba(37, 99, 235, 0.08)'
    ))
    
    # 80-20 reference marker
    p20_vol = (user_counts[:int(total_users * 0.20)].sum() / total_enrollments) * 100
    fig.add_vline(x=20, line_width=1, line_dash="dot", line_color="#EF4444")
    fig.add_annotation(
        x=20, y=p20_vol,
        text=f"Top 20% Learners = {p20_vol:.1f}% Volume",
        showarrow=True, arrowhead=2, arrowcolor="#EF4444", font=dict(color="#EF4444")
    )

    fig = _apply_standard_layout(fig, "<b>Learner Enrollment Concentration Curve (Pareto Analysis)</b>", height=420)
    fig.update_layout(
        xaxis_title="Cumulative Share of Learners (%)",
        yaxis_title="Cumulative Share of Enrollments (%)",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig

def plot_activity_tiers_distribution(df_users):
    """Donut chart illustrating segmentation of learners into activity tiers."""
    tier_counts = df_users['LearnerTier'].value_counts().reset_index()
    tier_counts.columns = ['Tier', 'Users']
    
    fig = px.pie(
        tier_counts,
        names='Tier',
        values='Users',
        hole=0.52,
        color='Tier',
        color_discrete_sequence=['#3B82F6', '#60A5FA', '#93C5FD', '#F59E0B', '#10B981']
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig = _apply_standard_layout(fig, "<b>Learner Engagement Segmentation (Activity Tiers)</b>", height=380)
    fig.update_layout(showlegend=False)
    return fig

def plot_monthly_velocity_timeline(df):
    """Line chart tracking monthly enrollment velocity across Free and Paid courses."""
    monthly = df.groupby(['YearMonth', 'CourseType']).size().reset_index(name='Enrollments')
    fig = px.line(
        monthly,
        x='YearMonth',
        y='Enrollments',
        color='CourseType',
        markers=True,
        color_discrete_map={'Free': THEME_COLORS['free'], 'Paid': THEME_COLORS['paid']},
        labels={'YearMonth': 'Enrollment Month', 'Enrollments': 'Verified Transactions'}
    )
    fig = _apply_standard_layout(fig, "<b>Monthly Enrollment Velocity Across Course Types (2025)</b>", height=400)
    fig.update_layout(
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig

def plot_payment_channel_distribution(df):
    """Payment method breakdown."""
    pm = df['PaymentMethod'].value_counts().reset_index()
    pm.columns = ['PaymentMethod', 'Transactions']
    fig = px.pie(
        pm,
        names='PaymentMethod',
        values='Transactions',
        hole=0.55,
        color='PaymentMethod',
        color_discrete_sequence=['#2563EB', '#10B981', '#8B5CF6']
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig = _apply_standard_layout(fig, "<b>Payment Channel Usage Distribution</b>", height=380)
    fig.update_layout(showlegend=False)
    return fig

# ----------------- SECTION 4: FORECASTING VISUALIZATION -----------------

def plot_enrollment_forecast(forecast_results):
    """Plotly visualization of historical actuals, held-out test predictions, and future forecasts with confidence bounds."""
    train = forecast_results['train_data']
    test = forecast_results['test_data']
    future = forecast_results['future_forecast']
    metrics = forecast_results['metrics']

    fig = go.Figure()

    # 1. Historical Train actuals
    fig.add_trace(go.Scatter(
        x=train['Date'], y=train['Enrollments'],
        mode='lines+markers',
        name='Training Actuals',
        line=dict(color='#64748B', width=2),
        marker=dict(size=4)
    ))

    # 2. Test Actuals
    fig.add_trace(go.Scatter(
        x=test['Date'], y=test['Actual'],
        mode='lines+markers',
        name='Validation Actuals',
        line=dict(color='#0F172A', width=2.5),
        marker=dict(size=5)
    ))

    # 3. Test Predictions
    fig.add_trace(go.Scatter(
        x=test['Date'], y=test['Predicted'],
        mode='lines+markers',
        name='Model Predictions (Test)',
        line=dict(color='#F59E0B', width=2, dash='dash'),
        marker=dict(size=5, symbol='diamond')
    ))

    # 4. Future Forecast Confidence Interval Upper & Lower
    fig.add_trace(go.Scatter(
        x=future['Date'], y=future['Upper_CI'],
        mode='lines',
        line=dict(width=0),
        showlegend=False,
        name='Upper 95% Bound'
    ))
    fig.add_trace(go.Scatter(
        x=future['Date'], y=future['Lower_CI'],
        mode='lines',
        line=dict(width=0),
        fill='tonexty',
        fillcolor='rgba(37, 99, 235, 0.15)',
        name='95% Prediction Interval'
    ))

    # 5. Future Forecast
    fig.add_trace(go.Scatter(
        x=future['Date'], y=future['Forecast'],
        mode='lines+markers',
        name='Future Forecast',
        line=dict(color=THEME_COLORS['secondary'], width=3),
        marker=dict(size=6, symbol='star')
    ))

    title_str = (f"<b>Experimental Enrollment Forecast (MAE: {metrics['mae']}, "
                 f"RMSE: {metrics['rmse']}, MAPE: {metrics['mape']}%)</b>")
    fig = _apply_standard_layout(fig, title_str, height=450)
    fig.update_layout(
        xaxis_title="Timeline Date",
        yaxis_title="Weekly Course Enrollments",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig
