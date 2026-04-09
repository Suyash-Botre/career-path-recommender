"""
app.py
Smart Career Path Recommender for CSE Students
-----------------------------------------------
Entry point for the application.

Wires all four modules together in the correct order:
    1. collect_input()       →  student_profile dict
    2. recommend_careers()   →  top 3 careers with match %
    3. generate_output()     →  full advanced output report
    4. display_output()      →  renders the styled result screen

Run with:
    streamlit run app.py
"""

from ui.input_form           import collect_input
from logic.similarity_engine import recommend_careers
from logic.output_engine     import generate_output
from ui.output_display       import display_output


# ── Step 1: Render the input form and collect student answers ──
# Returns a filled dictionary when the student clicks submit.
# Returns None while the form is still being filled.
student_profile = collect_input()


# ── Step 2: Run the recommendation pipeline after submission ──
if student_profile is not None:

    # Step 2a: Compute cosine similarity against dataset
    # Returns: [("Career Name", percent), ...]
    top_careers = recommend_careers(student_profile)

    # Step 2b: Generate the full output report using rule-based logic
    # Returns: dict with all 10 output keys
    advanced_output = generate_output(top_careers, student_profile)

    # Step 2c: Render the complete styled result screen
    display_output(advanced_output)