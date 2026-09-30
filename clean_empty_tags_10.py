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

empty_tags = [
    '<div class="page-meta"></div>',
    '<figure></figure>',
    '<figure>\n</figure>',
    '<figure> \n</figure>',
    '<figure> </figure>'
]

for u in urls:
    filepath = f"{u}/index.html"
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        
        original_html = html
        for tag in empty_tags:
            html = html.replace(tag, '')
            
        if html != original_html:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Cleaned empty tags in {filepath}")