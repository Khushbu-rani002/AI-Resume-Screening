import joblib

from backend.preprocessing import clean_resume
from backend.skill_extractor import extract_skills


model = joblib.load("models/resume_model.pkl")
tfidf = joblib.load("models/tfidf_vectorizer.pkl")


def screen_resume(resume_text, job_description):

    # -----------------------------
    # Predict Resume Role
    # -----------------------------

    cleaned_resume = clean_resume(resume_text)

    resume_tfidf = tfidf.transform([cleaned_resume])

    predicted_category = model.predict(resume_tfidf)[0]


    # -----------------------------
    # Extract Skills
    # -----------------------------

    resume_skills = extract_skills(resume_text)

    job_skills = extract_skills(job_description)


    # -----------------------------
    # Compare Skills
    # -----------------------------

    matched_skills = set(resume_skills) & set(job_skills)

    missing_skills = set(job_skills) - set(resume_skills)


    # -----------------------------
    # Calculate Match %
    # -----------------------------

    if len(job_skills) > 0:

        match_percentage = (
            len(matched_skills) /
            len(set(job_skills))
        ) * 100

    else:

        match_percentage = 0


    # -----------------------------
    # Decision
    # -----------------------------

    if match_percentage >= 75:

        decision = "SHORTLIST"

    elif match_percentage >= 50:

        decision = "REVIEW"

    else:

        decision = "REJECT"


    # -----------------------------
    # Return Results
    # -----------------------------

    return {
        "category": predicted_category,
        "resume_skills": resume_skills,
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills),
        "match_percentage": round(match_percentage, 2),
        "decision": decision
    }