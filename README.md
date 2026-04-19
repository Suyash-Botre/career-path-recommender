# 🎯 Smart Career Path Recommender for CSE Students

A beginner-friendly software mini project that helps Computer Science students discover the most suitable career paths based on their technical skills, interests, learning style, and work preferences.

---

## 🌐 Live Demo

👉 https://career-path-recommender-cse.streamlit.app/

---

## 📌 Project Overview

This project is designed to recommend the **top 3 most suitable career paths for a CSE student** using a structured assessment form and cosine similarity-based matching against an expert-designed career dataset.

The system collects student input through a guided interface, converts responses into numerical feature vectors, compares them with career profiles stored in a dataset, and generates explainable career recommendations with additional guidance.

The output is not limited to career names only. It also provides:

* ✅ Best-fit explanation
* ✅ Skill gap analysis
* ✅ 30 / 60 / 90 day action plan
* ✅ Career roadmap link
* ✅ Career reality layer
* ✅ Backup career suggestion
* ✅ Personalized closing advice

---

## 🛠 Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Cosine Similarity
* CSV / Excel Dataset

---

## 🧠 Core Recommendation Logic

The recommendation engine uses **cosine similarity** to compare:

**Student Profile Vector**
vs
**Career Dataset Feature Vectors**

The system then returns the **top 3 careers with highest similarity scores**.

---

## 🔄 Project Workflow

Student fills assessment form
⬇
Input converted into numerical profile vector
⬇
Career dataset loaded
⬇
Cosine similarity calculated
⬇
Top 3 careers selected
⬇
Rule-based output engine generates advanced explanation
⬇
Output displayed through Streamlit UI

---

## 📂 Project Folder Structure

career-path-recommender/

├── app.py
├── requirements.txt

├── dataset/
│   ├── career_recommender_dataset.csv
│   └── career_recommender_dataset.xlsx

├── ui/
│   ├── input_form.py
│   └── output_display.py

├── logic/
│   ├── similarity_engine.py
│   └── output_engine.py

├── docs/
│   ├── career_recommender_input_blueprint.docx
│   └── career_recommender_output_blueprint.docx

├── README.md

---

## ⚙ Module Description

### 📝 input_form.py

Handles student input collection using Streamlit form elements.

### 📊 similarity_engine.py

Computes cosine similarity between student profile and career dataset.

### 🧾 output_engine.py

Generates explainable advanced recommendation output using rule-based dictionaries.

### 🎨 output_display.py

Renders structured UI output with cards, sections, and styled layout.

### 🚀 app.py

Main execution layer connecting all modules.

---

## 💼 Supported Career Paths

The current dataset includes:

* ML Engineer
* Data Analyst
* Backend Developer
* Frontend Developer
* Cybersecurity Analyst
* Cloud Engineer
* System Software Engineer
* UI UX Designer
* Full Stack Developer
* DevOps Engineer
* Mobile App Developer
* Research Engineer

---

## ▶ How to Run Locally

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

---

## 🎓 Academic Purpose

This project was developed as a beginner-level CSE mini project to demonstrate:

* modular software design
* recommendation systems
* similarity-based decision logic
* explainable output generation
* deployment using Streamlit Cloud

---

## 👥 Contributors

Created by:

* [Suyash Botre]
* [Tejas Gundawar]
* [Vedant Wakulkar]
* [Shrivallabh Newasekar]
* [Kunal Wangal]

---

## 🚀 Future Improvements

Possible future enhancements:

* dataset refinement for stronger career separation
* more career paths
* stronger adaptive output personalization
* dashboard analytics
* export recommendation report

---

## 📜 License

This project is licensed under the MIT License.

The source code is provided for academic and educational use under open-source licensing conditions.

See LICENSE file for full details.