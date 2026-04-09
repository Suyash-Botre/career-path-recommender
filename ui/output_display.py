"""
ui/output_display.py
Smart Career Path Recommender for CSE Students
-----------------------------------------------
Renders the complete career analysis report using Streamlit.

Function:
    display_output(advanced_output)

Receives the dictionary returned by generate_output() and
renders all 10 output sections in order, exactly as defined
in the project output blueprint.

Sections rendered:
    1.  Personalized Result Header
    2.  Top 3 Career Recommendation Cards
    3.  Confidence Insight Box
    4.  Best Fit Explanation Box
    5.  Skill Gap Analysis (2 columns)
    6.  30 / 60 / 90 Day Action Plan Cards
    7.  Professional Roadmap Link
    8.  Career Reality Layer (3 cards)
    9.  Backup Career Suggestion
    10. Personalized Closing Advice
"""

import streamlit as st


def display_output(advanced_output: dict):
    """
    Render the full career analysis report for the student.

    Parameters
    ----------
    advanced_output : dict
        The dictionary returned by generate_output() in
        logic/output_engine.py. All 10 keys are expected.
    """

    # ─────────────────────────────────────────────────────────────
    # CSS — scoped styles for all custom HTML cards in this screen
    # ─────────────────────────────────────────────────────────────
    st.markdown("""
    <style>

    /* ── Career recommendation card ── */
    .career-card {
        background-color: #ffffff;
        border: 1px solid #d0d7de;
        border-top: 4px solid #1f77b4;
        border-radius: 10px;
        padding: 20px 18px;
        height: 100%;
        box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    }
    .career-card h3 {
        color: #1f4e79;
        margin-bottom: 6px;
        font-size: 1.1rem;
    }
    .career-card .match-badge {
        display: inline-block;
        background-color: #e8f4fd;
        color: #1f77b4;
        font-weight: 700;
        font-size: 1.3rem;
        padding: 4px 12px;
        border-radius: 20px;
        margin-bottom: 10px;
    }
    .career-card .reason-text {
        color: #555;
        font-size: 0.88rem;
        line-height: 1.5;
    }

    /* ── Info / highlight boxes ── */
    .info-box {
        background-color: #eef6fb;
        border-left: 5px solid #1f77b4;
        border-radius: 8px;
        padding: 16px 20px;
        margin-bottom: 8px;
        color: #1a1a2e;
        font-size: 0.95rem;
        line-height: 1.65;
    }
    .warning-box {
        background-color: #fff8e6;
        border-left: 5px solid #f0a500;
        border-radius: 8px;
        padding: 16px 20px;
        margin-bottom: 8px;
        color: #3b2f00;
        font-size: 0.95rem;
        line-height: 1.65;
    }
    .success-box {
        background-color: #eafaf1;
        border-left: 5px solid #27ae60;
        border-radius: 8px;
        padding: 16px 20px;
        margin-bottom: 8px;
        color: #1a3c2a;
        font-size: 0.95rem;
        line-height: 1.65;
    }

    /* ── Skill gap items ── */
    .strength-item {
        background-color: #eafaf1;
        border-radius: 6px;
        padding: 8px 14px;
        margin-bottom: 7px;
        color: #1e5631;
        font-size: 0.9rem;
    }
    .improve-item {
        background-color: #fef9e7;
        border-radius: 6px;
        padding: 8px 14px;
        margin-bottom: 7px;
        color: #7d5a00;
        font-size: 0.9rem;
    }

    /* ── Action plan card ── */
    .plan-card {
        background-color: #ffffff;
        border: 1px solid #d0d7de;
        border-top: 4px solid #27ae60;
        border-radius: 10px;
        padding: 18px 16px;
        height: 100%;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }
    .plan-card h4 {
        color: #1e5631;
        margin-bottom: 10px;
        font-size: 1rem;
    }
    .plan-card p {
        color: #444;
        font-size: 0.88rem;
        line-height: 1.6;
    }

    /* ── Reality card ── */
    .reality-card {
        background-color: #ffffff;
        border: 1px solid #d0d7de;
        border-top: 4px solid #8e44ad;
        border-radius: 10px;
        padding: 18px 16px;
        text-align: center;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }
    .reality-card .label {
        color: #8e44ad;
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 8px;
    }
    .reality-card .value {
        color: #2c3e50;
        font-size: 1rem;
        font-weight: 600;
    }

    /* ── Section headings ── */
    .section-heading {
        color: #4da6ff;
        font-size: 1.15rem;
        font-weight: 700;
        margin-top: 10px;
        margin-bottom: 14px;
        padding-bottom: 6px;
        border-bottom: 2px solid #d0e8f7;
    }

    </style>
    """, unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════
    # SECTION 1 — Personalized Result Header
    # ═══════════════════════════════════════════════════════════════
    st.markdown("---")
    st.markdown(
        "<h1 style='text-align:center; color:#4da6ff;'>"
        "🎯 Your Personalized Career Analysis Report"
        "</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align:center; color:#d0d7de; font-size:1rem; margin-bottom:30px;'>"
        "Based on your technical profile, learning style, and career preferences, "
        "here are your strongest career matches."
        "</p>",
        unsafe_allow_html=True
    )

    # ═══════════════════════════════════════════════════════════════
    # SECTION 2 — Top 3 Career Recommendation Cards
    # ═══════════════════════════════════════════════════════════════
    st.markdown(
        "<div class='section-heading'>🏆 Top 3 Career Recommendations</div>",
        unsafe_allow_html=True
    )

    top_careers  = advanced_output["top_careers"]    # list of (career, percent)
    career_reason = advanced_output["career_reason"]  # dict of career → reason

    col1, col2, col3 = st.columns(3)
    columns = [col1, col2, col3]

    # Medal labels for rank 1, 2, 3
    medals = ["🥇", "🥈", "🥉"]

    for i, (career, percent) in enumerate(top_careers):
        reason = career_reason.get(career, "Strong overall profile match.")
        with columns[i]:
            st.markdown(f"""
            <div class="career-card">
                <h3>{medals[i]} {career}</h3>
                <div class="match-badge">{percent}% Match</div>
                <div class="reason-text">{reason}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════
    # SECTION 3 — Confidence Insight Box
    # ═══════════════════════════════════════════════════════════════
    st.markdown(
        "<div class='section-heading'>💡 Confidence Insight</div>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<div class='info-box'>🔍 {advanced_output['confidence_note']}</div>",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════
    # SECTION 4 — Best Fit Explanation Box
    # ═══════════════════════════════════════════════════════════════
    st.markdown(
        "<div class='section-heading'>🎯 Why This Career Fits You</div>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<div class='info-box'>{advanced_output['best_fit']}</div>",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════
    # SECTION 5 — Skill Gap Analysis
    # ═══════════════════════════════════════════════════════════════
    st.markdown(
        "<div class='section-heading'>📊 Skill Gap Analysis</div>",
        unsafe_allow_html=True
    )

    strengths    = advanced_output["skill_gap"]["strengths"]
    improvements = advanced_output["skill_gap"]["improvements"]

    left_col, right_col = st.columns(2)

    with left_col:
        st.markdown("**✅ Current Strengths**")
        for item in strengths:
            st.markdown(
                f"<div class='strength-item'>✔ {item}</div>",
                unsafe_allow_html=True
            )

    with right_col:
        st.markdown("**📈 Skills to Improve**")
        for item in improvements:
            st.markdown(
                f"<div class='improve-item'>✘ {item}</div>",
                unsafe_allow_html=True
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════
    # SECTION 6 — 30 / 60 / 90 Day Action Plan
    # ═══════════════════════════════════════════════════════════════
    st.markdown(
        "<div class='section-heading'>🗓️ Your 30 / 60 / 90 Day Action Plan</div>",
        unsafe_allow_html=True
    )

    plan = advanced_output["action_plan"]
    p30, p60, p90 = st.columns(3)

    with p30:
        st.markdown(f"""
        <div class="plan-card">
            <h4>📅 Next 30 Days</h4>
            <p>{plan['30_days']}</p>
        </div>
        """, unsafe_allow_html=True)

    with p60:
        st.markdown(f"""
        <div class="plan-card">
            <h4>📅 Next 60 Days</h4>
            <p>{plan['60_days']}</p>
        </div>
        """, unsafe_allow_html=True)

    with p90:
        st.markdown(f"""
        <div class="plan-card">
            <h4>📅 Next 90 Days</h4>
            <p>{plan['90_days']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════
    # SECTION 7 — Professional Roadmap Link
    # ═══════════════════════════════════════════════════════════════
    st.markdown(
        "<div class='section-heading'>🗺️ Full Professional Roadmap</div>",
        unsafe_allow_html=True
    )
    roadmap_url = advanced_output["roadmap_link"]
    st.markdown(
        f"""
        <div class="info-box">
            📌 Follow the complete professional roadmap for your career path.<br><br>
            <a href="{roadmap_url}" target="_blank"
               style="background-color:#1f77b4; color:white; padding:10px 22px;
                      border-radius:6px; text-decoration:none; font-weight:600;
                      font-size:0.95rem;">
                🔗 View Full Professional Roadmap
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════
    # SECTION 8 — Career Reality Layer
    # ═══════════════════════════════════════════════════════════════
    st.markdown(
        "<div class='section-heading'>⚡ Career Reality Check</div>",
        unsafe_allow_html=True
    )

    reality = advanced_output["reality"]
    r1, r2, r3 = st.columns(3)

    with r1:
        st.markdown(f"""
        <div class="reality-card">
            <div class="label">Difficulty Level</div>
            <div class="value">⚠️ {reality['difficulty']}</div>
        </div>
        """, unsafe_allow_html=True)

    with r2:
        st.markdown(f"""
        <div class="reality-card">
            <div class="label">Preparation Time</div>
            <div class="value">⏱️ {reality['prep_time']}</div>
        </div>
        """, unsafe_allow_html=True)

    with r3:
        st.markdown(f"""
        <div class="reality-card">
            <div class="label">Entry-Level Role</div>
            <div class="value">💼 {reality['entry_role']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════
    # SECTION 9 — Backup Career Suggestion
    # ═══════════════════════════════════════════════════════════════
    st.markdown(
        "<div class='section-heading'>🔄 Backup Career Suggestion</div>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<div class='warning-box'>💡 {advanced_output['backup']}</div>",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════
    # SECTION 10 — Personalized Closing Advice
    # ═══════════════════════════════════════════════════════════════
    st.markdown(
        "<div class='section-heading'>✨ Personalized Advice</div>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<div class='success-box'>🌟 {advanced_output['closing']}</div>",
        unsafe_allow_html=True
    )

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align:center; color:#aaa; font-size:0.8rem;'>"
        "Smart Career Path Recommender · Built for CSE Students"
        "</p>",
        unsafe_allow_html=True
    )
 