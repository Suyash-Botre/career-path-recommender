"""
logic/output_engine.py
Smart Career Path Recommender for CSE Students
-----------------------------------------------
Generates the complete career output report for the
top recommended career using rule-based dictionaries.

Function:
    generate_output(top_careers, student_profile)

Covers all 12 careers present in the dataset:
    ML Engineer, Data Analyst, Backend Developer,
    Frontend Developer, Cybersecurity Analyst, Cloud Engineer,
    System Software Engineer, UI UX Designer, Full Stack Developer,
    DevOps Engineer, Mobile App Developer, Research Engineer

Return keys:
    top_careers, best_fit, career_reason, skill_gap,
    action_plan, roadmap_link, reality, backup,
    closing, confidence_note
"""


# ══════════════════════════════════════════════════════════════════
# DICTIONARY 1 — Best Fit Explanation
# Full paragraph explaining why this career suits the student.
# ══════════════════════════════════════════════════════════════════
best_fit_explanations = {
    "ML Engineer": (
        "Your profile shows strong mathematical reasoning, high Python skill, "
        "and a clear preference for pattern-based problem solving. "
        "Combined with your AI/ML interest, this makes ML Engineering a natural fit. "
        "You enjoy deep, long-focused work — exactly what model building requires."
    ),
    "Data Analyst": (
        "Your profile reflects strong SQL ability, data science curiosity, and "
        "a preference for structured logical thinking. "
        "You enjoy finding patterns in information and presenting findings clearly — "
        "core strengths every Data Analyst needs."
    ),
    "Backend Developer": (
        "You show solid Java/Python skills, good API understanding, and a structured "
        "problem-solving style. You prefer building systems that work reliably behind "
        "the scenes — exactly the mindset of a strong Backend Developer."
    ),
    "Frontend Developer": (
        "Your high JavaScript confidence, visual design comfort, and UI/UX interest "
        "indicate a creative-technical blend. You enjoy building things users can see "
        "and interact with — the core identity of a Frontend Developer."
    ),
    "Cybersecurity Analyst": (
        "Your profile shows strong interest in cybersecurity, comfort with system "
        "behavior analysis, and logical debugging preference. "
        "You think like an attacker and a defender simultaneously — "
        "a key trait of a Cybersecurity Analyst."
    ),
    "Cloud Engineer": (
        "You demonstrate good cloud basics knowledge, DevOps interest, and comfort "
        "with structured systems. Your preference for deep long work and reliability "
        "aligns well with cloud infrastructure roles."
    ),
    "System Software Engineer": (
        "Your strong C/C++ skills, Linux command line comfort, and preference for "
        "system behavior challenges show you enjoy working close to the hardware. "
        "System Software Engineering rewards exactly this kind of low-level thinking."
    ),
    "UI UX Designer": (
        "Your high UI/UX interest, visual design comfort, and preference for "
        "user-focused challenges make UI/UX Design your strongest direction. "
        "You think about how things look and feel — and that is the entire job."
    ),
    "Full Stack Developer": (
        "You show balanced strength across frontend and backend skills, with strong "
        "JavaScript, Python, and API understanding. You prefer fast-output work and "
        "enjoy seeing the complete picture — traits of a natural Full Stack Developer."
    ),
    "DevOps Engineer": (
        "Your cloud interest, Linux comfort, version control habits, and structured "
        "working style align tightly with DevOps. You enjoy automating processes and "
        "keeping systems running reliably — the DevOps mindset exactly."
    ),
    "Mobile App Developer": (
        "Your mobile development interest, Java/JavaScript skills, and preference for "
        "fast visible output suggest Mobile App Development is a strong fit. "
        "You enjoy building things people use on their phones every day."
    ),
    "Research Engineer": (
        "Your strong mathematics, research/theory interest, and preference for abstract "
        "thinking and deep sustained focus indicate Research Engineering suits you well. "
        "You enjoy exploring unsolved problems rather than shipping fast features."
    ),
}


# ══════════════════════════════════════════════════════════════════
# DICTIONARY 2 — Skill Gap Analysis
# strengths  = skills the student already has for this career
# improvements = skills that still need development
# ══════════════════════════════════════════════════════════════════
skill_gap = {
    "ML Engineer": {
        "strengths":    ["Python", "Mathematics", "AI/ML Interest", "Deep Focus Ability"],
        "improvements": ["SQL for data wrangling", "Cloud deployment (AWS/GCP)", "MLOps & model monitoring"],
    },
    "Data Analyst": {
        "strengths":    ["SQL", "Python", "Data Science Interest", "Structured Thinking"],
        "improvements": ["Tableau or Power BI", "Business domain knowledge", "Statistical inference"],
    },
    "Backend Developer": {
        "strengths":    ["Python / Java", "API Understanding", "OOP Concepts", "SQL"],
        "improvements": ["System design basics", "Docker & containerization", "Database query optimization"],
    },
    "Frontend Developer": {
        "strengths":    ["JavaScript", "UI/UX Interest", "Visual Design Thinking", "Web Dev Interest"],
        "improvements": ["React or Vue framework", "CSS layout & Flexbox mastery", "Accessibility standards"],
    },
    "Cybersecurity Analyst": {
        "strengths":    ["Cybersecurity Interest", "Logical Debugging", "Computer Networks", "Linux CLI"],
        "improvements": ["Ethical hacking tools (Kali, Nmap)", "CTF challenge practice", "Security certifications (CEH/CompTIA)"],
    },
    "Cloud Engineer": {
        "strengths":    ["Cloud Basics", "Cloud/DevOps Interest", "Linux Command Line", "Version Control"],
        "improvements": ["AWS / Azure / GCP certification", "Kubernetes & Docker", "Infrastructure as Code (Terraform)"],
    },
    "System Software Engineer": {
        "strengths":    ["C / C++", "Linux Command Line", "Operating Systems", "System Behavior Interest"],
        "improvements": ["Memory management deep dive", "Compiler design basics", "Multithreading & concurrency"],
    },
    "UI UX Designer": {
        "strengths":    ["UI/UX Design Interest", "Visual Design Comfort", "Presentation Confidence", "Creative Thinking"],
        "improvements": ["Figma / Adobe XD proficiency", "User research methods", "Prototyping & wireframing"],
    },
    "Full Stack Developer": {
        "strengths":    ["JavaScript", "Python", "API Understanding", "Web Development Interest"],
        "improvements": ["React (frontend framework)", "Node.js or Django (backend)", "Database integration & deployment"],
    },
    "DevOps Engineer": {
        "strengths":    ["Linux Command Line", "Version Control (Git)", "Cloud Basics", "Structured Work Style"],
        "improvements": ["CI/CD pipelines (GitHub Actions)", "Docker & Kubernetes", "Monitoring tools (Grafana/Prometheus)"],
    },
    "Mobile App Developer": {
        "strengths":    ["Mobile Development Interest", "Java / JavaScript", "Fast Output Preference", "Project Completion"],
        "improvements": ["Flutter or React Native framework", "App store publishing process", "Mobile UI/UX patterns"],
    },
    "Research Engineer": {
        "strengths":    ["Mathematics", "Research/Theory Interest", "Abstract Thinking", "Sustained Focus"],
        "improvements": ["Academic paper reading & writing", "LaTeX for documentation", "Research methodology & experimentation"],
    },
}


# ══════════════════════════════════════════════════════════════════
# DICTIONARY 3 — 30 / 60 / 90 Day Action Plan
# ══════════════════════════════════════════════════════════════════
action_plan = {
    "ML Engineer": {
        "30_days": "Learn NumPy and Pandas deeply. Complete one end-to-end ML project using Scikit-learn on a Kaggle dataset.",
        "60_days": "Study supervised learning algorithms. Build a classification and regression project. Push both to GitHub.",
        "90_days": "Deploy a model using Streamlit or Flask. Write a project README. Apply for ML internships.",
    },
    "Data Analyst": {
        "30_days": "Master SQL joins, aggregations, and subqueries. Complete a data cleaning project using Pandas.",
        "60_days": "Build an interactive dashboard using Matplotlib or Seaborn. Learn basic statistics for analysis.",
        "90_days": "Create a complete analytics case study from a real dataset. Publish it on GitHub and LinkedIn.",
    },
    "Backend Developer": {
        "30_days": "Build a REST API using Flask or Spring Boot. Practice OOP design patterns and CRUD operations.",
        "60_days": "Connect your API to PostgreSQL. Add JWT authentication. Write basic unit tests.",
        "90_days": "Dockerize your application. Deploy on Railway or Render. Document the API using Swagger.",
    },
    "Frontend Developer": {
        "30_days": "Strengthen HTML, CSS, and vanilla JavaScript. Build a fully responsive personal portfolio website.",
        "60_days": "Learn React fundamentals. Rebuild your portfolio as a React app with component structure.",
        "90_days": "Add animations, dark mode, and performance optimizations. Deploy on Netlify or Vercel.",
    },
    "Cybersecurity Analyst": {
        "30_days": "Set up a Kali Linux environment. Complete beginner rooms on TryHackMe (networking + Linux modules).",
        "60_days": "Practice 10 CTF challenges. Study common vulnerabilities: SQL injection, XSS, CSRF.",
        "90_days": "Complete CEH or CompTIA Security+ preparation. Document findings in a personal security blog.",
    },
    "Cloud Engineer": {
        "30_days": "Create a free AWS or GCP account. Deploy a static website and a basic virtual machine.",
        "60_days": "Learn Docker basics. Set up a containerized application and push it to a cloud registry.",
        "90_days": "Study Kubernetes fundamentals. Automate infrastructure with Terraform. Attempt AWS Cloud Practitioner exam.",
    },
    "System Software Engineer": {
        "30_days": "Revise C/C++ pointers, memory management, and file I/O. Build a small shell program.",
        "60_days": "Study OS concepts: process scheduling, memory paging, and threading. Implement a thread pool in C.",
        "90_days": "Contribute to an open-source systems project on GitHub. Study compiler basics using a small interpreter project.",
    },
    "UI UX Designer": {
        "30_days": "Learn Figma from scratch. Redesign a popular app screen with improved UX and present your reasoning.",
        "60_days": "Study user research techniques. Conduct 3 user interviews and build wireframes based on findings.",
        "90_days": "Create a complete case study with problem statement, research, wireframes, and final prototype. Add to portfolio.",
    },
    "Full Stack Developer": {
        "30_days": "Build a frontend page using React and connect it to a backend API using Flask or Node.js.",
        "60_days": "Add a database (SQLite or PostgreSQL). Implement full CRUD with user authentication.",
        "90_days": "Deploy the complete app. Write documentation. Share on GitHub with a live demo link.",
    },
    "DevOps Engineer": {
        "30_days": "Learn Git branching strategy deeply. Set up a basic CI/CD pipeline using GitHub Actions.",
        "60_days": "Dockerize an existing project. Push to Docker Hub. Learn basic Kubernetes pod deployment.",
        "90_days": "Set up monitoring using Grafana + Prometheus. Automate a deployment pipeline end to end.",
    },
    "Mobile App Developer": {
        "30_days": "Install Flutter or React Native. Build a simple to-do app with basic navigation and state.",
        "60_days": "Add API integration to your app. Build a weather or news app using a public API.",
        "90_days": "Publish your app on Google Play (internal testing). Polish UI and write a project case study.",
    },
    "Research Engineer": {
        "30_days": "Read 5 research papers in your area of interest. Summarize each with key findings and methodology.",
        "60_days": "Reproduce results from one paper using Python. Write up your process as a technical blog post.",
        "90_days": "Identify a research gap and draft a small experiment. Consider submitting to a college symposium.",
    },
}


# ══════════════════════════════════════════════════════════════════
# DICTIONARY 4 — Roadmap.sh Links
# ══════════════════════════════════════════════════════════════════
roadmap_links = {
    "ML Engineer":              "https://roadmap.sh/ai-data-scientist",
    "Data Analyst":             "https://roadmap.sh/ai-data-scientist",
    "Backend Developer":        "https://roadmap.sh/backend",
    "Frontend Developer":       "https://roadmap.sh/frontend",
    "Cybersecurity Analyst":    "https://roadmap.sh/cyber-security",
    "Cloud Engineer":           "https://roadmap.sh/aws",
    "System Software Engineer": "https://roadmap.sh/cpp",
    "UI UX Designer":           "https://roadmap.sh/ux-design",
    "Full Stack Developer":     "https://roadmap.sh/full-stack",
    "DevOps Engineer":          "https://roadmap.sh/devops",
    "Mobile App Developer":     "https://roadmap.sh/android",
    "Research Engineer":        "https://roadmap.sh/ai-data-scientist",
}


# ══════════════════════════════════════════════════════════════════
# DICTIONARY 5 — Career Reality Layer
# difficulty, prep_time, entry_role
# ══════════════════════════════════════════════════════════════════
reality_layer = {
    "ML Engineer": {
        "difficulty": "Hard",
        "prep_time":  "10–14 months",
        "entry_role": "ML Intern / Junior ML Engineer",
    },
    "Data Analyst": {
        "difficulty": "Moderate",
        "prep_time":  "5–8 months",
        "entry_role": "Junior Data Analyst / BI Intern",
    },
    "Backend Developer": {
        "difficulty": "Moderate",
        "prep_time":  "6–9 months",
        "entry_role": "Junior Backend Developer / API Intern",
    },
    "Frontend Developer": {
        "difficulty": "Easy–Moderate",
        "prep_time":  "4–7 months",
        "entry_role": "Junior Frontend Developer / UI Intern",
    },
    "Cybersecurity Analyst": {
        "difficulty": "Hard",
        "prep_time":  "10–15 months",
        "entry_role": "SOC Analyst L1 / Security Intern",
    },
    "Cloud Engineer": {
        "difficulty": "Moderate–Hard",
        "prep_time":  "8–12 months",
        "entry_role": "Cloud Support Engineer / Cloud Intern",
    },
    "System Software Engineer": {
        "difficulty": "Hard",
        "prep_time":  "12–18 months",
        "entry_role": "Systems Programmer / Embedded Intern",
    },
    "UI UX Designer": {
        "difficulty": "Moderate",
        "prep_time":  "5–8 months",
        "entry_role": "Junior UI Designer / UX Intern",
    },
    "Full Stack Developer": {
        "difficulty": "Moderate–Hard",
        "prep_time":  "8–12 months",
        "entry_role": "Junior Full Stack Developer / Web Intern",
    },
    "DevOps Engineer": {
        "difficulty": "Hard",
        "prep_time":  "10–14 months",
        "entry_role": "Junior DevOps Engineer / Cloud Ops Intern",
    },
    "Mobile App Developer": {
        "difficulty": "Moderate",
        "prep_time":  "6–9 months",
        "entry_role": "Junior App Developer / Mobile Intern",
    },
    "Research Engineer": {
        "difficulty": "Very Hard",
        "prep_time":  "18–24 months",
        "entry_role": "Research Intern / Junior Research Associate",
    },
}


# ══════════════════════════════════════════════════════════════════
# DICTIONARY 6 — Backup Career Suggestion
# Shown when the top career feels too demanding to start with
# ══════════════════════════════════════════════════════════════════
backup_career = {
    "ML Engineer":              "Data Analyst — same data skills, lower math barrier to start.",
    "Data Analyst":             "Backend Developer — SQL and Python transfer directly.",
    "Backend Developer":        "Full Stack Developer — extend what you already know.",
    "Frontend Developer":       "UI UX Designer — your visual thinking is already the core skill.",
    "Cybersecurity Analyst":    "DevOps Engineer — Linux and networking skills transfer well.",
    "Cloud Engineer":           "DevOps Engineer — overlapping tools and mindset.",
    "System Software Engineer": "Backend Developer — C/C++ logic transfers to system-level backend work.",
    "UI UX Designer":           "Frontend Developer — your design eye gives you a major head start.",
    "Full Stack Developer":     "Backend Developer — narrow the focus, go deeper on one side.",
    "DevOps Engineer":          "Cloud Engineer — same ecosystem, slightly less automation focus.",
    "Mobile App Developer":     "Frontend Developer — JavaScript and UI skills transfer directly.",
    "Research Engineer":        "ML Engineer — applied research with faster career entry.",
}


# ══════════════════════════════════════════════════════════════════
# DICTIONARY 7 — Personalized Closing Message
# ══════════════════════════════════════════════════════════════════
closing_message = {
    "ML Engineer":              "Stay consistent. One solid ML project every month beats ten half-finished ones.",
    "Data Analyst":             "Data storytelling is your superpower. Learn to explain your charts, not just make them.",
    "Backend Developer":        "Master one backend stack completely before jumping to another framework.",
    "Frontend Developer":       "Ship something real. A live project impresses more than certificates alone.",
    "Cybersecurity Analyst":    "Practice in labs daily. Cybersecurity is a skill you build by doing, not watching.",
    "Cloud Engineer":           "Get certified early. Cloud certifications open doors faster than most other paths.",
    "System Software Engineer": "Read code written by others. Open source systems projects will teach you more than courses.",
    "UI UX Designer":           "Build a portfolio of 3 strong case studies. Quality beats quantity every time.",
    "Full Stack Developer":     "Deploy everything. A live link on your resume is worth ten lines of bullet points.",
    "DevOps Engineer":          "Automate something in your own life first. DevOps is a mindset before it is a toolset.",
    "Mobile App Developer":     "Publish your first app even if it is simple. Shipping is the real skill.",
    "Research Engineer":        "Focus deeply on one direction for at least 6 months before switching domains.",
}


# ══════════════════════════════════════════════════════════════════
# DICTIONARY 8 — Career Reason (short one-liner for cards)
# Used in the top 3 recommendation cards in the UI
# ══════════════════════════════════════════════════════════════════
career_reason = {
    "ML Engineer":              "Strong AI interest + Python + analytical problem-solving profile",
    "Data Analyst":             "High SQL + data curiosity + structured logical thinking",
    "Backend Developer":        "Solid API knowledge + Java/Python + systems-oriented mindset",
    "Frontend Developer":       "High JavaScript + visual design comfort + UI/UX passion",
    "Cybersecurity Analyst":    "Cybersecurity interest + networking strength + logical debugging style",
    "Cloud Engineer":           "Cloud basics + DevOps interest + structured and reliable work style",
    "System Software Engineer": "Strong C/C++ + Linux comfort + low-level systems thinking",
    "UI UX Designer":           "High UI/UX interest + visual creativity + user-first thinking",
    "Full Stack Developer":     "Balanced frontend + backend + API skills with fast delivery preference",
    "DevOps Engineer":          "Linux + Git + cloud interest + automation-focused work style",
    "Mobile App Developer":     "Mobile interest + Java/JavaScript + fast visible output preference",
    "Research Engineer":        "Strong mathematics + research passion + abstract and sustained focus",
}


# ══════════════════════════════════════════════════════════════════
# SAFE FALLBACKS
# Used when a career is not found in any dictionary above.
# .get() with these defaults prevents any runtime crash.
# ══════════════════════════════════════════════════════════════════
DEFAULT_BEST_FIT    = "Your profile shows a strong match with this career based on your skills and interests."
DEFAULT_REASON      = "Your skills and interests align well with this career direction."
DEFAULT_SKILL_GAP   = {
    "strengths":    ["Core programming skills"],
    "improvements": ["Domain-specific tools and frameworks"],
}
DEFAULT_ACTION_PLAN = {
    "30_days": "Identify the core tools for this career and begin one beginner project.",
    "60_days": "Complete a mid-level project and push it to GitHub.",
    "90_days": "Build a portfolio piece and start applying for internships.",
}
DEFAULT_LINK        = "https://roadmap.sh"
DEFAULT_REALITY     = {
    "difficulty": "Moderate",
    "prep_time":  "6–12 months",
    "entry_role": "Intern / Junior Role",
}
DEFAULT_BACKUP      = "Explore adjacent roles that share similar skill requirements."
DEFAULT_CLOSING     = "Stay consistent. One focused month of learning beats six scattered ones."


# ══════════════════════════════════════════════════════════════════
# HELPER — Confidence Note
# Compares the top 3 match percentages.
# If scores are close (difference <= 3), the student profile
# overlaps multiple domains — practical exposure will decide.
# ══════════════════════════════════════════════════════════════════
def get_confidence_note(top_careers: list) -> str:
    """
    Return a confidence note based on how far apart the top 3 scores are.

    If the gap between 1st and 3rd score is <= 3 percent, the profile
    overlaps multiple domains and practical exposure is needed to decide.
    Otherwise, the top recommendation shows a clear direction.
    """
    if len(top_careers) < 2:
        return "Your top recommendation shows a clear direction."

    top_score    = top_careers[0][1]   # highest match percent
    third_score  = top_careers[-1][1]  # lowest of the top 3

    if (top_score - third_score) <= 3:
        return (
            "Your profile matches multiple nearby domains. "
            "Practical exposure will decide your final fit."
        )
    return "Your top recommendation shows a clear direction."


# ══════════════════════════════════════════════════════════════════
# HELPER — Profile-Sensitive Improvement Rules
# Checks key skill scores from student_profile and appends
# targeted warnings to the improvements list when a critical
# skill for the top career is weak (score == 1 = Beginner/Low).
# ══════════════════════════════════════════════════════════════════
def apply_profile_rules(top_career: str, student_profile: dict, improvements: list) -> list:
    """
    Add personalised improvement hints based on the student's actual scores.

    Works on a copy of the improvements list — does not mutate the original
    dictionary. Returns the updated list.
    """
    # Make a copy so the original dictionary entry stays unchanged
    updated = improvements.copy()

    # Rule 1 — ML Engineer needs strong Python; warn if weak
    if top_career == "ML Engineer" and student_profile.get("Python", 0) == 1:
        updated.append("Strengthen Python fundamentals before advancing to ML libraries")

    # Rule 2 — Frontend Developer needs JavaScript; warn if weak
    if top_career == "Frontend Developer" and student_profile.get("JavaScript", 0) == 1:
        updated.append("Build core JavaScript skills before moving to React or any framework")

    # Rule 3 — Data Analyst needs SQL; warn if weak
    if top_career == "Data Analyst" and student_profile.get("SQL", 0) == 1:
        updated.append("SQL is non-negotiable for a Data Analyst — prioritise it immediately")

    # Rule 4 — Backend Developer needs API Understanding; warn if weak
    if top_career == "Backend Developer" and student_profile.get("API_Understanding", 0) == 1:
        updated.append("Study REST API concepts and HTTP basics before building backend projects")

    # Rule 5 — DevOps / Cloud Engineer needs Linux; warn if weak
    if top_career in ("DevOps Engineer", "Cloud Engineer") and student_profile.get("Linux_Command_Line", 0) == 1:
        updated.append("Linux command line proficiency is essential — complete a Linux basics course first")

    # Rule 6 — System Software Engineer needs C/C++; warn if weak
    if top_career == "System Software Engineer" and student_profile.get("C++", 0) == 1:
        updated.append("C/C++ is the foundation of this path — revisit pointers and memory management first")

    return updated


# ══════════════════════════════════════════════════════════════════
# MAIN FUNCTION
# ══════════════════════════════════════════════════════════════════
def generate_output(top_careers: list, student_profile: dict) -> dict:
    """
    Generate the complete career output report for the top recommended career.

    Parameters
    ----------
    top_careers : list of tuples
        Output from recommend_careers().
        Format: [("Career Name", percent), ...]

    student_profile : dict
        Output from collect_input().
        Keys match dataset column names exactly.

    Returns
    -------
    dict with keys:
        top_careers, best_fit, career_reason, skill_gap,
        action_plan, roadmap_link, reality, backup,
        closing, confidence_note
    """

    # Primary career used for all detailed sections
    top_career = top_careers[0][0]

    # Fetch base skill gap for the top career
    base_gap = skill_gap.get(top_career, DEFAULT_SKILL_GAP)

    # Apply profile-sensitive rules to personalise the improvements list
    personalised_improvements = apply_profile_rules(
        top_career,
        student_profile,
        base_gap["improvements"]
    )

    # Build the complete output report
    output = {

        # All 3 career matches with percentages — used for recommendation cards
        "top_careers": top_careers,

        # Short one-liner reason per career — shown on each card
        "career_reason": {
            career: career_reason.get(career, DEFAULT_REASON)
            for career, _ in top_careers
        },

        # Best fit paragraph for the top career
        "best_fit": best_fit_explanations.get(top_career, DEFAULT_BEST_FIT),

        # Skill gap with profile-personalised improvements
        "skill_gap": {
            "strengths":    base_gap["strengths"],
            "improvements": personalised_improvements,
        },

        # 30 / 60 / 90 day action plan
        "action_plan": action_plan.get(top_career, DEFAULT_ACTION_PLAN),

        # Full professional roadmap link
        "roadmap_link": roadmap_links.get(top_career, DEFAULT_LINK),

        # Career reality: difficulty, prep time, entry role
        "reality": reality_layer.get(top_career, DEFAULT_REALITY),

        # Backup career if top path feels too demanding
        "backup": backup_career.get(top_career, DEFAULT_BACKUP),

        # Personalized closing advice
        "closing": closing_message.get(top_career, DEFAULT_CLOSING),

        # Confidence note based on how close the top 3 scores are
        "confidence_note": get_confidence_note(top_careers),
    }

    return output