"""
logic/similarity_engine.py
Smart Career Path Recommender for CSE Students
------------------------------------------------
This file contains the core recommendation logic.
It reads the career dataset, compares the student's
profile against every career row using cosine similarity,
and returns the top 3 best-matching careers with
their match percentage.
"""

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


# ──────────────────────────────────────────────
# Dataset file path
# Primary format: CSV
# Fallback format: XLSX (if CSV not found)
# ──────────────────────────────────────────────
DATASET_CSV_PATH  = "dataset/career_recommender_dataset.csv"
DATASET_XLSX_PATH = "dataset/career_recommender_dataset.xlsx"


def load_dataset() -> pd.DataFrame:
    """
    Load the career dataset from CSV.
    Falls back to XLSX if CSV is not found.
    Returns a pandas DataFrame.
    """
    try:
        df = pd.read_csv(DATASET_CSV_PATH)
    except FileNotFoundError:
        # Fallback to Excel if CSV is missing
        df = pd.read_excel(DATASET_XLSX_PATH)

    return df


def recommend_careers(student_profile: dict) -> list:
    """
    Compare the student profile against all careers in the dataset
    using cosine similarity and return the top 3 matches.

    Parameters
    ----------
    student_profile : dict
        Dictionary returned by collect_input() in ui/input_form.py.
        Keys exactly match the dataset column names.

    Returns
    -------
    list of tuples: [ ("Career Name", match_percent), ... ]
    Example:
        [
            ("ML Engineer", 84),
            ("Data Analyst", 79),
            ("Backend Developer", 74)
        ]
    """

    # ── Step 1: Load the dataset ──────────────────
    df = load_dataset()

    # ── Step 2: Separate Career column from feature columns ──
    # 'Career' is the label column — we don't use it for math
    career_names   = df["Career"].tolist()          # list of career name strings
    feature_columns = [col for col in df.columns if col != "Career"]  # all numeric columns

    # Extract only the feature values from the dataset as a 2D numpy array
    # Shape: (number_of_careers, number_of_features)
    dataset_matrix = df[feature_columns].values

    # ── Step 3: Build the student vector ─────────────────────
    # IMPORTANT: values must be in the exact same column order as the dataset
    # If a column is somehow missing from student_profile, default to 0 safely
    student_vector = [
        student_profile.get(col, 0) for col in feature_columns
    ]

    # Convert to 2D numpy array — sklearn expects shape (1, n_features)
    student_vector = np.array(student_vector).reshape(1, -1)

    # ── Step 4: Compute cosine similarity ────────────────────
    # cosine_similarity returns a 2D array of shape (1, number_of_careers)
    # Each value is between 0.0 (no match) and 1.0 (perfect match)
    similarity_scores = cosine_similarity(student_vector, dataset_matrix)[0]

    # ── Step 5: Get indices of top 3 highest scores ──────────
    # argsort() sorts ascending, so we reverse with [::-1] to get descending
    top3_indices = np.argsort(similarity_scores)[::-1][:3]

    # ── Step 6: Build and return results ─────────────────────
    # Convert similarity score (0.0 to 1.0) → percentage (0 to 100)
    results = []
    for idx in top3_indices:
        career_name  = career_names[idx]
        match_percent = round(similarity_scores[idx] * 100)  # rounded integer
        results.append((career_name, match_percent))

    return results