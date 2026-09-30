import os

urls = [
    "how-to-verify-university-accreditation-before-you-apply",
    "how-to-check-a-canadian-school-dli-before-applying",
    "how-to-choose-a-university-course-uk",
    "complete-university-cost-comparison-checklist",
    "how-to-compare-universities-beyond-rankings",
    "2026-selective-school-exam-the-ultimate-guide-for-nsw-parents",
    "albert-campbell-collegiate-institute-school-overview",
    "baulkham-hills-high-school-entry-requirements-2026-comprehensive-guide",
    "arizona-state-university-the-2026-insider-guide-to-admissions-fees-and-innovation",
    "appleby-college-canada-boarding-school-admissions-fees-student-life-guide-for-international-students"
]

replacements = {
    "Parents should": "Families can",
    "parents should": "families can",
    "It is important to": "It is helpful to",
    "it is important to": "it is helpful to",
    "Always check": "Verify",
    "always check": "verify",
    "In today's": "Currently,",
    "in today's": "currently,"
}

for u in urls:
    filepath = f"{u}/index.html"
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        for old, new in replacements.items():
            html = html.replace(old, new)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Fixed AI phrases in {filepath}")
