skills = [
    # Technology
    "python",
    "java",
    "sql",
    "pandas",
    "numpy",
    "machine learning",
    "natural language processing",
    "git",
    "tensorflow",
    "scikit-learn",
    "deep learning",
    "javascript",
    "html",
    "css",
    "c++",
    "power bi",
    "excel",

    # Legal
    "legal research",
    "contract drafting",
    "contract review",
    "litigation",
    "legal documentation",
    "compliance",
    "negotiation",
    "case management",
    "regulatory analysis",
    "legal writing",
    "corporate law",
    "contract law",

    # Accounting
    "accounting",
    "bookkeeping",
    "financial reporting",
    "accounts payable",
    "accounts receivable",
    "financial analysis",
    "reconciliation",
    "auditing",
    "taxation",

    # General
    "communication",
    "leadership",
    "problem solving",
    "data analysis",
]


def extract_skills(text):
    text = text.lower()

    found_skills = []

    for skill in skills:
        if skill in text:
            found_skills.append(skill)

    return found_skills