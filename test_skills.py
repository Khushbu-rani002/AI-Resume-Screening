from backend.skill_extractor import extract_skills


job_description = """
We are looking for a Lawyer.

Excellent legal research and analytical skills.
Strong written and verbal communication skills.
Ability to draft and review legal documents.
Good negotiation and problem-solving skills.

Preferred Skills:
Legal Research, Contract Drafting, Litigation,
Legal Documentation, Law, Negotiation, Compliance,
Communication, Case Management.
"""


print("JOB SKILLS:")
print(extract_skills(job_description))