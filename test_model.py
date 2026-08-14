import joblib

model = joblib.load("models/resume_model.pkl")
tfidf = joblib.load("models/tfidf_vectorizer.pkl")

print("Model loaded successfully!")
print("Model:", model)
print("TF-IDF loaded successfully!")
print("TF-IDF:", tfidf)