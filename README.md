# 📄 Smart Resume Screening System
https://ai-resume-screening-b7d3bh2iyi4lhmm2jotbsk.streamlit.app/

An AI-powered resume screening and job matching system that analyzes resumes, predicts the candidate's job role, extracts relevant skills, and compares the resume with a given job description.

## 🚀 Features

* 📄 Upload resume in PDF format
* 🔍 Extract text from PDF resumes
* 🧹 Clean and preprocess resume text using NLTK
* 🤖 Predict candidate job role using Machine Learning
* 📊 Convert resume text into numerical features using TF-IDF
* 🧠 SVM-based resume classification
* 💼 Enter a Job Description
* 🛠️ Extract skills from resume and job description
* ✅ Identify matched skills
* ❌ Identify missing skills
* 📈 Calculate resume-to-job-description match percentage
* 🎯 Generate screening decision:

  * SHORTLIST
  * REVIEW
  * REJECT
* 🌐 Streamlit web interface

## 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Support Vector Machine (SVM)
* TF-IDF Vectorization

### Natural Language Processing

* NLTK
* Stopword removal
* Text preprocessing
* Regular expressions

### PDF Processing

* PyPDF2

### Web Application

* Streamlit

### Model Saving

* Joblib

### Development Tools

* VS Code
* Google Colab
* Git
* GitHub

## 🧠 System Workflow

```text
Resume PDF
    ↓
PDF Text Extraction
    ↓
NLTK Text Preprocessing
    ↓
TF-IDF Vectorization
    ↓
SVM Machine Learning Model
    ↓
Predicted Job Role


Job Description
    ↓
Skill Extraction
    ↓
Compare Resume Skills with JD Skills
    ↓
Matched Skills + Missing Skills
    ↓
Match Percentage
    ↓
SHORTLIST / REVIEW / REJECT
```

## 📂 Project Structure

```text
resume-screening/
│
├── app.py
├── test_prediction.py
├── requirements.txt
├── README.md
│
├── backend/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── pdf_parser.py
│   ├── skill_extractor.py
│   └── screening.py
│
├── models/
│   ├── resume_model.pkl
│   └── tfidf_vectorizer.pkl
│
└── venv/
```

## 📌 Project Files

### app.py

Main Streamlit application.

It provides the user interface for:

* Uploading a resume
* Entering a job description
* Running resume analysis
* Displaying screening results

The application uses a two-column interface with resume/JD input on one side and analysis results on the other.

### backend/preprocessing.py

Contains the NLTK-based resume preprocessing function.

The preprocessing cleans resume text before it is passed to the machine learning model.

### backend/pdf_parser.py

Extracts text from uploaded PDF resumes using PyPDF2.

### backend/skill_extractor.py

Extracts technical skills from resumes and job descriptions using a predefined skill list.

### backend/screening.py

Contains the main resume screening function.

It:

1. Cleans the resume text
2. Converts the resume into TF-IDF features
3. Predicts the candidate's job role
4. Extracts resume skills
5. Extracts job-description skills
6. Finds matched skills
7. Finds missing skills
8. Calculates the match percentage
9. Generates a screening decision

### models/resume_model.pkl

Saved machine learning model used to predict the candidate's job role.

### models/tfidf_vectorizer.pkl

Saved TF-IDF vectorizer used to convert resume text into numerical features.

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Move into the project directory:

```bash
cd resume-screening
```

### 2. Create a Virtual Environment

For Windows:

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install the required packages manually:

```bash
pip install streamlit
pip install scikit-learn
pip install nltk
pip install PyPDF2
pip install joblib
```

## 🧹 NLTK Setup

Run Python and download the required NLTK resources:

```python
import nltk

nltk.download('stopwords')
nltk.download('punkt')
```

If additional NLTK resources are required by the preprocessing code, download them as needed.

## ▶️ Run the Application

Make sure the virtual environment is activated.

Run:

```bash
python -m streamlit run app.py
```

The application will open in the browser at:

```text
http://localhost:8501
```

## 🖥️ How to Use

### Step 1: Upload Resume

Upload a candidate resume in PDF format.

### Step 2: Enter Job Description

Paste the required job description into the Job Description field.

Example:

```text
We are looking for a Machine Learning Engineer
with experience in Python, Machine Learning,
Pandas, NumPy, SQL and Scikit-learn.

The candidate should have knowledge of data
preprocessing, model development and Git.
```

### Step 3: Analyze Resume

Click:

```text
🔍 Analyze Resume
```

### Step 4: View Results

The system displays:

* Predicted Job Role
* Match Score
* Screening Decision
* Matched Skills
* Missing Skills

## 📊 Resume-to-Job Matching

The system compares the skills extracted from the resume with the skills extracted from the job description.

The match percentage is calculated as:

```text
Match Percentage =
(Matched Skills / Required Job Skills) × 100
```

For example:

```text
Job Description Skills:
Python
SQL
Pandas
NumPy
Scikit-learn

Resume Skills:
Python
SQL
Pandas
NumPy

Matched Skills = 4

Match Percentage = 4 / 5 × 100

Match Percentage = 80%
```

## 🎯 Screening Decision

The current system uses the following thresholds:

| Match Score  | Decision  |
| ------------ | --------- |
| 75% or above | SHORTLIST |
| 50% - 74%    | REVIEW    |
| Below 50%    | REJECT    |

These thresholds can be changed in `backend/screening.py`.

## 🤖 Machine Learning Pipeline

The machine learning component follows this pipeline:

```text
Resume Text
     ↓
NLTK Preprocessing
     ↓
TF-IDF Vectorization
     ↓
SVM Classifier
     ↓
Predicted Job Role
```

The trained model and TF-IDF vectorizer are saved using Joblib and loaded by the application.

## 📈 Model Evaluation

The model can be evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

The model performance depends on the dataset, preprocessing technique, model, and train/test split.

## 🗃️ Dataset

The project uses a resume dataset containing resume text and job-role information.

The dataset is used to train the machine learning model to classify resumes into different job roles.

Example roles can include:

```text
Machine Learning Engineer
Data Analyst
Software Developer
Web Developer
Accountant
Designer
Teacher
Engineer
HR
Banking
Finance
```

The available roles depend on the dataset used during model training.

## 🔐 Privacy

Resumes can contain personal and sensitive information.

For production use:

* Do not permanently store uploaded resumes unless necessary.
* Protect candidate information.
* Avoid exposing personal information in application logs.
* Use secure file handling.
* Follow applicable privacy and data-protection requirements.

## ⚠️ Limitations

The current system has some limitations:

* Skill extraction uses a predefined skill list.
* Skill synonyms and variations may not always be detected.
* Prediction quality depends on the training dataset.
* TF-IDF does not understand text semantics as deeply as transformer-based models.
* Scanned/image-only PDFs may not produce usable text with standard PDF extraction.
* Match percentage is primarily based on extracted skills.
* The system should assist recruiters rather than make final hiring decisions automatically.

## 🔮 Future Improvements

Possible future improvements include:

* BERT or transformer-based resume classification
* Semantic resume-JD similarity
* More advanced skill extraction
* Named Entity Recognition
* Experience-level matching
* Education requirement matching
* Location and salary matching
* Multiple resume comparison
* Candidate ranking
* Recruiter dashboard
* Database integration
* User authentication
* Cloud deployment
* Explainable AI for screening decisions

## 📚 Project Objective

The objective of this project is to demonstrate how Natural Language Processing, Machine Learning, and a web application can be combined to automate the initial resume screening process.

The system helps recruiters quickly understand:

* What role a resume most closely matches
* Which required skills the candidate has
* Which skills are missing
* How closely the resume matches a job description
* Whether the candidate should be shortlisted, reviewed, or rejected

## 👩‍💻 Author

**Khushbu Rani**

Student | AI/ML & Software Development

## 📜 License

This project is developed for educational and academic purposes.
