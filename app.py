import streamlit as st
from pathlib import Path

from backend.pdf_parser import extract_text_from_pdf
from backend.screening import screen_resume


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Smart Resume Screening",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# LOAD CSS
# ============================================================

BASE_DIR = Path(__file__).parent


def load_css():
    css_path = BASE_DIR / "style.css"

    with open(css_path, "r", encoding="utf-8") as file:
        st.markdown(
            f"<style>{file.read()}</style>",
            unsafe_allow_html=True
        )


# ============================================================
# LOAD HTML
# ============================================================

def load_html(filename):
    html_path = BASE_DIR / filename

    with open(html_path, "r", encoding="utf-8") as file:
        return file.read()


load_css()


# ============================================================
# HEADER
# ============================================================

st.markdown(
    load_html("header.html"),
    unsafe_allow_html=True
)

# Added standard visual space instead of st.divider() to avoid top line artifacts
st.markdown("<br>", unsafe_allow_html=True)


# ============================================================
# TWO COLUMN LAYOUT
# ============================================================

left, right = st.columns([1, 1])


# ============================================================
# LEFT SIDE
# RESUME + JOB DESCRIPTION
# ============================================================

with left:

    st.markdown(
        '<h2>📤 Resume & Job Details</h2>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # RESUME UPLOAD
    # --------------------------------------------------------

    st.markdown("**📄 Upload Resume**")

    uploaded_file = st.file_uploader(
        "Choose a PDF resume",
        type=["pdf"],
        label_visibility="collapsed"
    )

    if uploaded_file is not None:
        st.caption(
            f"📎 {uploaded_file.name}"
        )

    # --------------------------------------------------------
    # JOB DESCRIPTION
    # --------------------------------------------------------

    st.markdown("**💼 Job Description**")

    job_description = st.text_area(
        "Paste the job description below",
        height=180,
        label_visibility="collapsed",
        placeholder="""Example:

We are looking for a Data Analyst with experience in
Python, SQL, Pandas, NumPy, Power BI and Excel.

Requirements:
- Strong Python knowledge
- SQL experience
- Data analysis
- Data visualization
- Problem-solving skills
"""
    )

    # --------------------------------------------------------
    # ANALYZE BUTTON
    # --------------------------------------------------------

    analyze = st.button(
        "🔍 Analyze Resume",
        use_container_width=True
    )


# ============================================================
# RIGHT SIDE
# ANALYSIS
# ============================================================

with right:

    st.markdown(
        '<h2>📊 Resume Analysis</h2>',
        unsafe_allow_html=True
    )

    # ========================================================
    # BEFORE ANALYSIS
    # ========================================================

    if not analyze:
        st.info(
            "Upload a resume and enter a job description, "
            "then click **Analyze Resume**."
        )

    # ========================================================
    # ANALYSIS
    # ========================================================

    if analyze:

        # ----------------------------------------------------
        # VALIDATION
        # ----------------------------------------------------

        if uploaded_file is None:
            st.error(
                "❌ Please upload a PDF resume."
            )

        elif not job_description.strip():
            st.error(
                "❌ Please enter a job description."
            )

        else:
            with st.spinner("Analyzing resume..."):
                try:

                    # ----------------------------------------
                    # EXTRACT PDF TEXT
                    # ----------------------------------------

                    resume_text = extract_text_from_pdf(
                        uploaded_file
                    )

                    if not resume_text.strip():
                        st.error(
                            "❌ Could not extract text from the PDF."
                        )

                    else:

                        # ------------------------------------
                        # SCREEN RESUME
                        # ------------------------------------

                        result = screen_resume(
                            resume_text,
                            job_description
                        )

                        # ------------------------------------
                        # SUCCESS
                        # ------------------------------------

                        st.success(
                            "Resume analyzed successfully!"
                        )

                        # =================================================
                        # PREDICTED ROLE + MATCH SCORE
                        # =================================================

                        col1, col2 = st.columns(2)

                        with col1:
                            st.markdown(
                                "**Predicted Role**"
                            )
                            st.markdown(
                                f"### {result['category']}"
                            )

                        with col2:
                            st.markdown(
                                "**Match Score**"
                            )
                            st.markdown(
                                f"### {result['match_percentage']}%"
                            )

                        # =================================================
                        # DECISION
                        # =================================================

                        decision = result["decision"]

                        if decision == "SHORTLIST":
                            st.success(
                                f"✅ Decision: **{decision}**"
                            )

                        elif decision == "REVIEW":
                            st.warning(
                                f"⚠️ Decision: **{decision}**"
                            )

                        else:
                            st.error(
                                f"❌ Decision: **{decision}**"
                            )

                        st.divider()

                        # =================================================
                        # SKILLS
                        # =================================================

                        skill_col1, skill_col2 = st.columns(2)

                        # ------------------------------------------------
                        # MATCHED SKILLS
                        # ------------------------------------------------

                        with skill_col1:
                            st.markdown(
                                "### ✅ Matched Skills"
                            )

                            matched = result[
                                "matched_skills"
                            ]

                            if matched:
                                for skill in matched:
                                    st.write(
                                        f"✓ {skill}"
                                    )
                            else:
                                st.write(
                                    "No matching skills found."
                                )

                        # ------------------------------------------------
                        # MISSING SKILLS
                        # ------------------------------------------------

                        with skill_col2:
                            st.markdown(
                                "### ❌ Missing Skills"
                            )

                            missing = result[
                                "missing_skills"
                            ]

                            if missing:
                                for skill in missing:
                                    st.write(
                                        f"• {skill}"
                                    )
                            else:
                                st.write(
                                    "No required skills missing."
                                )

                # =================================================
                # ERROR HANDLING
                # =================================================

                except Exception as e:
                    st.error(
                        f"❌ An error occurred: {e}"
                    )