"""
data_loader.py - Data ingestion and feature engineering for EduPro Learner Analytics.
"""

import pandas as pd
import numpy as np
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')

def load_raw_data():
    """Load individual raw CSV tables."""
    users = pd.read_csv(os.path.join(DATA_DIR, 'users.csv'))
    teachers = pd.read_csv(os.path.join(DATA_DIR, 'teachers.csv'))
    courses = pd.read_csv(os.path.join(DATA_DIR, 'courses.csv'))
    tx = pd.read_csv(os.path.join(DATA_DIR, 'transactions.csv'))
    return users, teachers, courses, tx

def load_and_prepare_data():
    """
    Load merged dataset or build it with all derived behavioral and demographic attributes.
    """
    merged_path = os.path.join(DATA_DIR, 'merged_edupro_data.csv')
    if os.path.exists(merged_path):
        df = pd.read_csv(merged_path)
        df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])
        return df

    # Fallback to merging if not pre-built
    users, teachers, courses, tx = load_raw_data()
    
    # Calculate User lifetime course enrollments
    user_tx_counts = tx.groupby('UserID').size().rename('TotalCoursesEnrolled')
    users = users.merge(user_tx_counts, on='UserID', how='left')

    # Activity Tiers
    user_bins = [0, 1, 2, 4, 8, 50]
    user_labels = ['Casual (1 course)', 'Explorer (2 courses)', 'Engaged (3-4 courses)', 'Active (5-8 courses)', 'Power Learner (9+ courses)']
    users['LearnerTier'] = pd.cut(users['TotalCoursesEnrolled'], bins=user_bins, labels=user_labels)

    # Standard Pedagogical Age Brackets
    age_bins = [0, 17, 25, 35, 100]
    age_labels = ['<18 (Youth)', '18-25 (Young Adult)', '26-35 (Early/Mid Career)', '36+ (Mature)']
    users['AgeGroup'] = pd.cut(users['Age'], bins=age_bins, labels=age_labels)

    # Merge to transaction grain
    df = tx.merge(users, on='UserID', how='left')
    df = df.merge(courses, on='CourseID', how='left')
    df = df.merge(teachers, on='TeacherID', how='left', suffixes=('', '_Instructor'))

    df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])
    df['Year'] = df['TransactionDate'].dt.year
    df['Month'] = df['TransactionDate'].dt.month
    df['MonthName'] = df['TransactionDate'].dt.strftime('%b')
    df['YearMonth'] = df['TransactionDate'].dt.strftime('%Y-%m')
    df['DayOfWeek'] = df['TransactionDate'].dt.day_name()
    df['Quarter'] = df['TransactionDate'].dt.to_period('Q').astype(str)

    df.to_csv(merged_path, index=False)
    return df
