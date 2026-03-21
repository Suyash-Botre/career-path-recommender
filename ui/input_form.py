import streamlit as st


# ──────────────────────────────────────────────
# PAGE CONFIG
# ──────────────────────────────────────────────
st.set_page_config(
    page_title="Smart Career Path Recommender",
    layout="wide"
)

# ──────────────────────────────────────────────
# SAFE CSS STYLING
# ──────────────────────────────────────────────
st.markdown("""
<style>
.main {
    background-color: #f7f9fc;
}

h1 {
    color: #1f4e79;
    text-align: center;
}

div[data-testid="stExpander"] {
    border-radius: 10px;
    border: 1px solid #d0d7de;
    margin-bottom: 10px;
}

.stButton > button {
    background-color: #1f77b4;
    color: white;
    border-radius: 8px;
    height: 3em;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────
# Helper: ordinal label → numeric score
# Beginner / Low       → 1
# Intermediate / Medium → 3
# Strong / High        → 5
# ──────────────────────────────────────────────
def ordinal_to_score(label: str) -> int:
    mapping = {
        "Low": 1,
        "Beginner": 1,
        "Medium": 3,
        "Intermediate": 3,
        "High": 5,
        "Strong": 5,        # blueprint uses "Strong" not "Expert"
    }
    return mapping.get(label, 1)


# ──────────────────────────────────────────────
# Helper: activity label → numeric score
# ──────────────────────────────────────────────
def activity_to_score(label: str, scale: dict) -> int:
    return scale.get(label, 1)


# ══════════════════════════════════════════════
# MAIN FUNCTION
# ══════════════════════════════════════════════
def collect_input() -> dict:

    st.markdown("<h1>🎓 Smart Career Path Recommender</h1>", unsafe_allow_html=True)
    st.markdown("### Personalized Career Assessment for CSE Students")
    st.markdown("Fill all sections carefully — your answers directly influence recommendation quality.")
    st.markdown("---")

    # This dictionary is returned at the end
    # Every key matches the dataset column name exactly
    student_profile = {}

    # ──────────────────────────────────────────────
    # SECTION 1 OF 10 — Technical Skills Profile
    # ──────────────────────────────────────────────
    with st.expander("📌 Section 1 of 10 — Technical Skills Profile", expanded=True):
        st.caption("Rate your current technical strength honestly.")

        # Blueprint labels: Beginner / Intermediate / Strong → 1 / 3 / 5
        lang_options = ["Beginner", "Intermediate", "Strong"]

        col1, col2 = st.columns(2)

        with col1:
            student_profile["Python"]     = ordinal_to_score(st.selectbox("Python",     lang_options, key="python"))
            student_profile["C"]          = ordinal_to_score(st.selectbox("C",          lang_options, key="c"))
            student_profile["C++"]        = ordinal_to_score(st.selectbox("C++",        lang_options, key="cpp"))
            student_profile["Java"]       = ordinal_to_score(st.selectbox("Java",       lang_options, key="java"))
            student_profile["JavaScript"] = ordinal_to_score(st.selectbox("JavaScript", lang_options, key="js"))

        with col2:
            # Blueprint labels: Low / Medium / High → 1 / 3 / 5
            lmh_options = ["Low", "Medium", "High"]
            student_profile["SQL"]                = ordinal_to_score(st.selectbox("SQL",                       lmh_options, key="sql"))
            student_profile["API_Understanding"]  = ordinal_to_score(st.selectbox("API Understanding",         lmh_options, key="api"))
            student_profile["Version_Control"]    = ordinal_to_score(st.selectbox("Version Control (Git/GitHub)", lmh_options, key="git"))
            student_profile["Linux_Command_Line"] = ordinal_to_score(st.selectbox("Linux Command Line",        lmh_options, key="linux"))
            student_profile["Cloud_Basics"]       = ordinal_to_score(st.selectbox("Cloud Basics",              lmh_options, key="cloud"))

    # ──────────────────────────────────────────────
    # SECTION 2 OF 10 — Domain Interest Mapping
    # ──────────────────────────────────────────────
    with st.expander("📌 Section 2 of 10 — Domain Interest Mapping", expanded=True):
        st.caption("Select your genuine domain interest level.")

        # Sliders map directly to numeric values (0–5)
        student_profile["AI_ML"]              = st.slider("AI / ML",            0, 5, 0, key="s_aiml")
        student_profile["Data_Science"]       = st.slider("Data Science",       0, 5, 0, key="s_ds")
        student_profile["Web_Development"]    = st.slider("Web Development",    0, 5, 0, key="s_web")
        student_profile["Cybersecurity"]      = st.slider("Cybersecurity",      0, 5, 0, key="s_cyber")
        student_profile["Cloud_DevOps"]       = st.slider("Cloud / DevOps",     0, 5, 0, key="s_cloud")
        student_profile["System_Programming"] = st.slider("System Programming", 0, 5, 0, key="s_sys")
        student_profile["Mobile_Development"] = st.slider("Mobile Development", 0, 5, 0, key="s_mob")
        student_profile["Game_Development"]   = st.slider("Game Development",   0, 5, 0, key="s_game")
        student_profile["UI_UX_Design"]       = st.slider("UI/UX Design",       0, 5, 0, key="s_uiux")
        student_profile["Research_Theory"]    = st.slider("Research / Theory",  0, 5, 0, key="s_res")

    # ──────────────────────────────────────────────
    # SECTION 3 OF 10 — Academic Strength
    # ──────────────────────────────────────────────
    with st.expander("📌 Section 3 of 10 — Academic Strength", expanded=True):
        st.caption("Evaluate your subject confidence.")

        lmh_options = ["Low", "Medium", "High"]

        # FIX: all 6 selectboxes now have explicit unique keys — prevents Streamlit crash
        student_profile["Mathematics"]          = ordinal_to_score(st.selectbox("Mathematics",          lmh_options, key="math"))
        student_profile["DBMS"]                 = ordinal_to_score(st.selectbox("DBMS",                 lmh_options, key="dbms"))
        student_profile["Operating_Systems"]    = ordinal_to_score(st.selectbox("Operating Systems",    lmh_options, key="os"))
        student_profile["Computer_Networks"]    = ordinal_to_score(st.selectbox("Computer Networks",    lmh_options, key="cn"))
        student_profile["OOP_Concepts"]         = ordinal_to_score(st.selectbox("OOP Concepts",         lmh_options, key="oop"))
        student_profile["Software_Engineering"] = ordinal_to_score(st.selectbox("Software Engineering", lmh_options, key="se"))

    # ──────────────────────────────────────────────
    # SECTION 4 OF 10 — Existing Activity Profile
    # ──────────────────────────────────────────────
    with st.expander("📌 Section 4 of 10 — Existing Activity Profile", expanded=True):
        st.caption("Answer honestly so the recommendation becomes more accurate.")

        # Projects Completed: 0 / 1-2 / 3+  →  1 / 3 / 5
        proj_scale = {"0": 1, "1-2": 3, "3+": 5}
        student_profile["Projects_Completed"] = activity_to_score(
            st.selectbox("Projects Completed", list(proj_scale.keys()), key="proj"), proj_scale
        )

        # GitHub Usage: Never / Sometimes / Regular  →  1 / 3 / 5
        github_scale = {"Never": 1, "Sometimes": 3, "Regular": 5}
        student_profile["GitHub_Usage"] = activity_to_score(
            st.selectbox("GitHub Usage", list(github_scale.keys()), key="github"), github_scale
        )

        # Hackathon Participation: No / Once / Multiple  →  1 / 3 / 5
        hack_scale = {"No": 1, "Once": 3, "Multiple": 5}
        student_profile["Hackathon_Participation"] = activity_to_score(
            st.selectbox("Hackathon Participation", list(hack_scale.keys()), key="hackathon"), hack_scale
        )

        # Coding Contest: No / Sometimes / Regular  →  1 / 3 / 5
        contest_scale = {"No": 1, "Sometimes": 3, "Regular": 5}
        student_profile["Coding_Contest_Participation"] = activity_to_score(
            st.selectbox("Coding Contest Participation", list(contest_scale.keys()), key="contest"), contest_scale
        )

        # Open Source: No / Sometimes / Yes  →  1 / 3 / 5
        oss_scale = {"No": 1, "Sometimes": 3, "Yes": 5}
        student_profile["Open_Source_Contribution"] = activity_to_score(
            st.selectbox("Open Source Contribution", list(oss_scale.keys()), key="oss"), oss_scale
        )

    # ──────────────────────────────────────────────
    # SECTION 5 OF 10 — Cognitive Preference
    # ──────────────────────────────────────────────
    with st.expander("📌 Section 5 of 10 — Cognitive Preference", expanded=True):
        st.caption("Answer honestly so the recommendation becomes more accurate.")

        # Preferred Challenge → one-hot across 4 columns
        challenge_options = ["Logic Bugs", "Data Patterns", "UI Design", "System Behavior"]
        selected_challenge = st.radio("Preferred Challenge", challenge_options, key="challenge")
        student_profile["Challenge_Logic_Bugs"]      = 1 if selected_challenge == "Logic Bugs"      else 0
        student_profile["Challenge_Data_Patterns"]   = 1 if selected_challenge == "Data Patterns"   else 0
        student_profile["Challenge_UI_Design"]       = 1 if selected_challenge == "UI Design"       else 0
        student_profile["Challenge_System_Behavior"] = 1 if selected_challenge == "System Behavior" else 0

        # Problem Solving Style → one-hot across 4 columns
        problem_options = ["Break logically", "Search docs", "Ask help", "Trial & error"]
        selected_problem = st.radio("Problem Solving Style", problem_options, key="problem")
        student_profile["Problem_Break_Logically"] = 1 if selected_problem == "Break logically" else 0
        student_profile["Problem_Search_Docs"]     = 1 if selected_problem == "Search docs"     else 0
        student_profile["Problem_Ask_Help"]        = 1 if selected_problem == "Ask help"        else 0
        student_profile["Problem_Trial_Error"]     = 1 if selected_problem == "Trial & error"   else 0

        # Comfort Zone → one-hot across 4 columns
        comfort_options = ["Abstract Thinking", "Structured Logic", "Visual Design", "Repeated Refinement"]
        selected_comfort = st.radio("Comfort Zone", comfort_options, key="comfort")
        student_profile["Comfort_Abstract_Thinking"]   = 1 if selected_comfort == "Abstract Thinking"   else 0
        student_profile["Comfort_Structured_Logic"]    = 1 if selected_comfort == "Structured Logic"    else 0
        student_profile["Comfort_Visual_Design"]       = 1 if selected_comfort == "Visual Design"       else 0
        student_profile["Comfort_Repeated_Refinement"] = 1 if selected_comfort == "Repeated Refinement" else 0

    # ──────────────────────────────────────────────
    # SECTION 6 OF 10 — Working Style Preference
    # ──────────────────────────────────────────────
    with st.expander("📌 Section 6 of 10 — Working Style Preference", expanded=True):
        st.caption("Answer honestly so the recommendation becomes more accurate.")

        # Work Preference → one-hot across 2 columns
        selected_work = st.radio("Work Preference", ["Alone", "Team"], key="work_pref")
        student_profile["Work_Alone"] = 1 if selected_work == "Alone" else 0
        student_profile["Work_Team"]  = 1 if selected_work == "Team"  else 0

        # Task Preference → one-hot across 2 columns
        selected_task = st.radio("Task Preference", ["Fast Output", "Deep Long Work"], key="task_pref")
        student_profile["Task_Fast_Output"]    = 1 if selected_task == "Fast Output"    else 0
        student_profile["Task_Deep_Long_Work"] = 1 if selected_task == "Deep Long Work" else 0

        # Style Preference → one-hot across 2 columns
        selected_style = st.radio("Style Preference", ["Structured", "Exploratory"], key="style_pref")
        student_profile["Style_Structured"]  = 1 if selected_style == "Structured"  else 0
        student_profile["Style_Exploratory"] = 1 if selected_style == "Exploratory" else 0

    # ──────────────────────────────────────────────
    # SECTION 7 OF 10 — Learning Capacity & Discipline
    # ──────────────────────────────────────────────
    with st.expander("📌 Section 7 of 10 — Learning Capacity & Discipline", expanded=True):
        st.caption("Answer honestly so the recommendation becomes more accurate.")

        # Hours Available Daily: <1 / 1-2 / 2-4 / 4+  →  1 / 2 / 3 / 4
        hours_scale = {"<1": 1, "1-2": 2, "2-4": 3, "4+": 4}
        student_profile["Hours_Available_Daily"] = activity_to_score(
            st.selectbox("Hours Available Daily", list(hours_scale.keys()), key="hours"), hours_scale
        )

        # Consistency: Low / Medium / High  →  1 / 3 / 5
        student_profile["Consistency"] = ordinal_to_score(
            st.selectbox("Consistency", ["Low", "Medium", "High"], key="consistency")
        )

        # Sustain One Topic: Yes / Sometimes / No  →  5 / 3 / 1
        sustain_scale = {"Yes": 5, "Sometimes": 3, "No": 1}
        student_profile["Sustain_One_Topic"] = activity_to_score(
            st.selectbox("Can Sustain One Topic for Months?", list(sustain_scale.keys()), key="sustain"),
            sustain_scale
        )

    # ──────────────────────────────────────────────
    # SECTION 8 OF 10 — Career Goal Intention
    # ──────────────────────────────────────────────
    with st.expander("📌 Section 8 of 10 — Career Goal Intention", expanded=True):
        st.caption("Answer honestly so the recommendation becomes more accurate.")

        # Main Goal → one-hot across 4 columns
        goal_options = ["Quick Placement", "High Salary", "Research", "Startup"]
        selected_goal = st.radio("Main Goal", goal_options, key="goal")
        student_profile["Goal_Quick_Placement"] = 1 if selected_goal == "Quick Placement" else 0
        student_profile["Goal_High_Salary"]     = 1 if selected_goal == "High Salary"     else 0
        student_profile["Goal_Research"]        = 1 if selected_goal == "Research"        else 0
        student_profile["Goal_Startup"]         = 1 if selected_goal == "Startup"         else 0

        # Work Location → one-hot across 3 columns
        location_options = ["Remote", "Office", "Hybrid"]
        selected_location = st.radio("Work Preference (Location)", location_options, key="work_loc")
        student_profile["Work_Remote"] = 1 if selected_location == "Remote" else 0
        student_profile["Work_Office"] = 1 if selected_location == "Office" else 0
        student_profile["Work_Hybrid"] = 1 if selected_location == "Hybrid" else 0

        # Difficulty Acceptance → one-hot across 3 columns
        difficulty_options = ["Easy Entry", "Moderate", "Long Hard Path"]
        selected_difficulty = st.radio("Difficulty Acceptance", difficulty_options, key="difficulty")
        student_profile["Difficulty_Easy_Entry"]     = 1 if selected_difficulty == "Easy Entry"     else 0
        student_profile["Difficulty_Moderate"]       = 1 if selected_difficulty == "Moderate"       else 0
        student_profile["Difficulty_Long_Hard_Path"] = 1 if selected_difficulty == "Long Hard Path" else 0

    # ──────────────────────────────────────────────
    # SECTION 9 OF 10 — Tool Exposure
    # ──────────────────────────────────────────────
    with st.expander("📌 Section 9 of 10 — Tool Exposure", expanded=True):
        st.caption("Answer honestly so the recommendation becomes more accurate.")

        lmh_options = ["Low", "Medium", "High"]
        student_profile["VSCode_Familiarity"]  = ordinal_to_score(st.selectbox("VS Code Familiarity", lmh_options, key="vscode"))
        student_profile["Terminal_Usage"]      = ordinal_to_score(st.selectbox("Terminal Usage",      lmh_options, key="terminal"))
        student_profile["Postman_Familiarity"] = ordinal_to_score(st.selectbox("Postman Familiarity", lmh_options, key="postman"))
        student_profile["Jupyter_Familiarity"] = ordinal_to_score(st.selectbox("Jupyter Familiarity", lmh_options, key="jupyter"))

    # ──────────────────────────────────────────────
    # SECTION 10 OF 10 — Communication & Presentation
    # ──────────────────────────────────────────────
    with st.expander("📌 Section 10 of 10 — Communication & Presentation", expanded=True):
        st.caption("Answer honestly so the recommendation becomes more accurate.")

        lmh_options = ["Low", "Medium", "High"]
        student_profile["Technical_Explanation_Confidence"] = ordinal_to_score(st.selectbox("Technical Explanation Confidence",  lmh_options, key="tech_conf"))
        student_profile["Presentation_Confidence"]          = ordinal_to_score(st.selectbox("Presentation Confidence",           lmh_options, key="pres_conf"))
        student_profile["Documentation_Writing_Confidence"] = ordinal_to_score(st.selectbox("Documentation Writing Confidence",  lmh_options, key="doc_conf"))
        student_profile["Team_Coordination_Confidence"]     = ordinal_to_score(st.selectbox("Team Coordination Confidence",      lmh_options, key="team_conf"))

    # ──────────────────────────────────────────────
    # SUBMIT BUTTON
    # ──────────────────────────────────────────────
    st.markdown("---")
    submitted = st.button("🔍 Get My Career Recommendation", use_container_width=True)

    # Return the filled profile only after submit is clicked
    if submitted:
        return student_profile

    # Return None if user hasn't submitted yet
    return None