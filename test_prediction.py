import joblib

from backend.preprocessing import clean_resume

model = joblib.load("models/resume_model.pkl")
tfidf = joblib.load("models/tfidf_vectorizer.pkl")

test_resume = """
AI/ML Engineer with experience in Python, machine learning,
deep learning, pandas, numpy, scikit-learn, TensorFlow,
data preprocessing and model development.
"""

cleaned = clean_resume(test_resume)

resume_tfidf = tfidf.transform([cleaned])

prediction = model.predict(resume_tfidf)

print("Predicted Role:", prediction[0])