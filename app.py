import streamlit as st

from ui.input_form import collect_input
from logic.similarity_engine import recommend_careers
from logic.output_engine import generate_output


# ---------------------------------------------------
# Page Config
# ---------------------------------------------------
st.set_page_config(
    page_title="Smart Career Path Recommender",
    layout="wide"
)


# ---------------------------------------------------
# Main Title
# ---------------------------------------------------
st.title("Smart Career Path Recommender for CSE Students")

st.markdown(
    "Fill the assessment form below to receive your personalized career analysis report."
)


# ---------------------------------------------------
# Collect Input
# collect_input already contains your original submit button
# ---------------------------------------------------
student_profile = collect_input()


# ---------------------------------------------------
# Only run after collect_input returns actual dictionary
# ---------------------------------------------------
if student_profile is not None:

    # Step 1
    top_careers = recommend_careers(student_profile)

    # Step 2
    advanced_output = generate_output(top_careers, student_profile)

    # ---------------------------------------------------
    # Official Output Header
    # ---------------------------------------------------
    st.header("Your Personalized Career Analysis Report")

    st.write(
        "Based on your technical profile, learning style, and career preferences, "
        "here are your strongest career matches."
    )

    # ---------------------------------------------------
    # Top 3 Career Recommendations
    # ---------------------------------------------------
    st.subheader("Top 3 Career Recommendations")

    for career, score in advanced_output["top_careers"]:
        reason = advanced_output["career_reason"].get(career, "")

        st.write(f"**{career} — {score}%**")
        st.write(f"Reason: {reason}")
        st.write("---")

    # ---------------------------------------------------
    # Confidence Note
    # ---------------------------------------------------
    st.subheader("Confidence Insight")
    st.write(advanced_output["confidence_note"])

    # ---------------------------------------------------
    # Best Fit Explanation
    # ---------------------------------------------------
    st.subheader("Best Fit Explanation")
    st.write(advanced_output["best_fit"])

    # ---------------------------------------------------
    # Skill Gap Analysis
    # ---------------------------------------------------
    st.subheader("Skill Gap Analysis")

    st.write("**Current Strengths:**")
    for item in advanced_output["skill_gap"]["strengths"]:
        st.write(f"- {item}")

    st.write("**Skills to Improve:**")
    for item in advanced_output["skill_gap"]["improvements"]:
        st.write(f"- {item}")

    # ---------------------------------------------------
    # Action Plan
    # ---------------------------------------------------
    st.subheader("30 / 60 / 90 Day Action Plan")

    st.write(f"**30 Days:** {advanced_output['action_plan']['30_days']}")
    st.write(f"**60 Days:** {advanced_output['action_plan']['60_days']}")
    st.write(f"**90 Days:** {advanced_output['action_plan']['90_days']}")

    # ---------------------------------------------------
    # Roadmap Link
    # ---------------------------------------------------
    st.subheader("Professional Roadmap")
    st.write(advanced_output["roadmap_link"])

    # ---------------------------------------------------
    # Reality Layer
    # ---------------------------------------------------
    st.subheader("Career Reality")

    st.write(f"Difficulty: {advanced_output['reality']['difficulty']}")
    st.write(f"Preparation Time: {advanced_output['reality']['prep_time']}")
    st.write(f"Entry Role: {advanced_output['reality']['entry_role']}")

    # ---------------------------------------------------
    # Backup Career
    # ---------------------------------------------------
    st.subheader("Backup Career Suggestion")
    st.write(advanced_output["backup"])

    # ---------------------------------------------------
    # Closing Message
    # ---------------------------------------------------
    st.subheader("Personalized Closing Advice")
    st.write(advanced_output["closing"])