"""
test_analytics.py - Automated Testing Suite for EduPro Analytics Pipeline
Tests data ingestion, preprocessing, KPIs, statistics, insights, and visualization rendering.
"""

import os
import sys
import unittest
import pandas as pd
import numpy as np

# Add project root to sys.path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from src.data_loader import clean_and_preprocess_tables, load_and_prepare_data
from src.analytics import (
    calculate_kpis,
    run_statistical_tests,
    generate_automated_insights,
    run_enrollment_forecasting
)
from src.visualizations import (
    plot_age_distribution_box,
    plot_gender_participation_donut,
    plot_age_cohort_breakdown,
    plot_category_popularity_ranked,
    plot_level_distribution_donut,
    plot_free_vs_paid_by_category,
    plot_top_and_bottom_courses,
    plot_age_vs_category_heatmap,
    plot_gender_vs_category_diverging,
    plot_level_by_age_stacked,
    plot_pareto_concentration,
    plot_activity_tiers_distribution,
    plot_monthly_velocity_timeline,
    plot_payment_channel_distribution,
    plot_enrollment_forecast
)

class TestEduProAnalytics(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Load and cache cleaned and merged data once for all test methods."""
        cls.df, cls.quality_audit = load_and_prepare_data()
        cls.users, cls.teachers, cls.courses, cls.tx, _ = clean_and_preprocess_tables()

    def test_01_data_completeness_and_dimensions(self):
        """Validate raw and merged dataset dimensions and zero null presence."""
        self.assertEqual(len(self.users), 3000, "Users table must contain exactly 3,000 records.")
        self.assertEqual(len(self.courses), 60, "Courses table must contain exactly 60 records.")
        self.assertEqual(len(self.teachers), 60, "Teachers table must contain exactly 60 records.")
        self.assertEqual(len(self.tx), 10000, "Transactions table must contain exactly 10,000 records.")
        self.assertEqual(len(self.df), 10000, "Merged dataset must preserve 10,000 transaction grain.")
        self.assertEqual(self.df.isnull().sum().sum(), 0, "Cleaned merged dataset must have 0 null values.")

    def test_02_referential_integrity(self):
        """Validate foreign keys in transactions map bijectively to dimension tables."""
        orphan_users = set(self.tx['UserID']) - set(self.users['UserID'])
        orphan_courses = set(self.tx['CourseID']) - set(self.courses['CourseID'])
        orphan_teachers = set(self.tx['TeacherID']) - set(self.teachers['TeacherID'])
        
        self.assertEqual(len(orphan_users), 0, "No orphan UserIDs permitted in transactions.")
        self.assertEqual(len(orphan_courses), 0, "No orphan CourseIDs permitted in transactions.")
        self.assertEqual(len(orphan_teachers), 0, "No orphan TeacherIDs permitted in transactions.")

    def test_03_domain_value_validity(self):
        """Validate numeric value ranges and domain business logic."""
        self.assertTrue((self.users['Age'] >= 15).all() and (self.users['Age'] <= 35).all(), "Learner age must be between 15 and 35.")
        self.assertTrue((self.courses['CourseRating'] >= 1.0).all() and (self.courses['CourseRating'] <= 5.0).all(), "Course ratings must be in [1, 5].")
        self.assertTrue((self.courses['CoursePrice'] >= 0).all(), "Course price must be non-negative.")
        
        free_courses = self.courses[self.courses['CourseType'] == 'Free']
        paid_courses = self.courses[self.courses['CourseType'] == 'Paid']
        self.assertTrue((free_courses['CoursePrice'] == 0.0).all(), "Free courses must have $0.00 price.")
        self.assertTrue((paid_courses['CoursePrice'] > 0.0).all(), "Paid courses must have positive price.")

    def test_04_kpi_calculations_accuracy(self):
        """Verify dynamic KPI computation formulas."""
        kpis = calculate_kpis(self.df)
        self.assertEqual(kpis['total_enrollments'], 10000)
        self.assertEqual(kpis['unique_learners'], 3000)
        self.assertEqual(kpis['total_courses'], 60)
        self.assertEqual(kpis['total_categories'], 12)
        self.assertAlmostEqual(kpis['avg_courses_per_learner'], 10000 / 3000, places=2)
        self.assertAlmostEqual(kpis['female_pct'] + kpis['male_pct'], 100.0, places=1)
        self.assertEqual(kpis['top_category'], 'Data Science')
        self.assertGreater(kpis['total_revenue'], 900000.0)

    def test_05_kpi_empty_state_handling(self):
        """Verify KPI engine handles empty filtered datasets gracefully without crashing."""
        empty_df = self.df[self.df['Age'] > 150]
        kpis = calculate_kpis(empty_df)
        self.assertEqual(kpis['total_enrollments'], 0)
        self.assertEqual(kpis['unique_learners'], 0)
        self.assertEqual(kpis['top_category'], 'N/A')

    def test_06_statistical_hypothesis_tests(self):
        """Validate inferential statistics outputs and p-value boundaries."""
        stat_res = run_statistical_tests(self.df)
        for key in ['age_vs_category', 'age_vs_level', 'gender_vs_category', 'gender_vs_level']:
            test_data = stat_res[key]
            self.assertIn('chi2', test_data)
            self.assertIn('p_value', test_data)
            self.assertTrue(0.0 <= test_data['p_value'] <= 1.0, f"p-value for {key} must be in [0, 1].")
            self.assertFalse(test_data['is_significant'], f"{key} should not be significant at alpha=0.05.")

    def test_07_automated_insights_engine(self):
        """Validate automated rule-driven insights generation."""
        insights = generate_automated_insights(self.df, self.quality_audit)
        self.assertIsInstance(insights, list)
        self.assertGreaterEqual(len(insights), 4)
        for ins in insights:
            self.assertIn('title', ins)
            self.assertIn('detail', ins)
            self.assertIn('category', ins)

    def test_08_forecasting_pipeline(self):
        """Validate experimental Holt's Linear Trend forecasting model."""
        fc_res, err = run_enrollment_forecasting(self.df, freq='W-MON', test_ratio=0.20, forecast_periods=8)
        self.assertIsNone(err, f"Forecasting pipeline should not produce errors: {err}")
        self.assertIsNotNone(fc_res)
        
        metrics = fc_res['metrics']
        self.assertGreater(metrics['mae'], 0.0)
        self.assertGreater(metrics['rmse'], 0.0)
        self.assertGreater(metrics['mape'], 0.0)
        
        future_df = fc_res['future_forecast']
        self.assertEqual(len(future_df), 8, "Must generate exactly 8 forecast periods.")
        self.assertTrue((future_df['Upper_CI'] >= future_df['Forecast']).all(), "Upper CI must be >= Forecast.")
        self.assertTrue((future_df['Forecast'] >= future_df['Lower_CI']).all(), "Forecast must be >= Lower CI.")

    def test_09_visualization_rendering(self):
        """Validate that all Plotly chart generators output valid Figures without exceptions."""
        filtered_users = self.df.drop_duplicates(subset=['UserID'])
        
        fig1 = plot_age_distribution_box(filtered_users)
        fig2 = plot_gender_participation_donut(filtered_users)
        fig3 = plot_age_cohort_breakdown(filtered_users)
        fig4 = plot_category_popularity_ranked(self.df)
        fig5 = plot_level_distribution_donut(self.df)
        fig6 = plot_free_vs_paid_by_category(self.df)
        fig7 = plot_top_and_bottom_courses(self.df)
        fig8 = plot_age_vs_category_heatmap(self.df)
        fig9 = plot_gender_vs_category_diverging(self.df)
        fig10 = plot_level_by_age_stacked(self.df)
        fig11 = plot_pareto_concentration(self.df)
        fig12 = plot_activity_tiers_distribution(filtered_users)
        fig13 = plot_monthly_velocity_timeline(self.df)
        fig14 = plot_payment_channel_distribution(self.df)

        fc_res, _ = run_enrollment_forecasting(self.df)
        fig15 = plot_enrollment_forecast(fc_res)

        for i, fig in enumerate([fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9, fig10, fig11, fig12, fig13, fig14, fig15]):
            self.assertIsNotNone(fig.data, f"Figure {i+1} must contain valid Plotly traces.")

if __name__ == '__main__':
    unittest.main()
