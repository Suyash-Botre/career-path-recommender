id="vdbk6j"
from ui.input_form import collect_input
from logic.similarity_engine import recommend_careers
import streamlit as st


student_profile = collect_input()

if student_profile:
    top_careers = recommend_careers(student_profile)

    st.success("Top 3 Career Recommendations")

    for career, score in top_careers:
        st.write(f"{career} — {score}%")

