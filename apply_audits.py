import os
import re
import json

urls = [
    "how-to-verify-university-accreditation-before-you-apply",
    "how-to-check-a-canadian-school-dli-before-applying",
    "how-to-choose-a-university-course-uk",
    "complete-university-cost-comparison-checklist",
    "how-to-compare-universities-beyond-rankings",
    "2026-selective-school-exam-the-ultimate-guide-for-nsw-parents",
    "albert-campbell-collegiate-institute-school-overview",
    "baulkham-hills-high-school-entry-requirements-2026-comprehensive-guide",
    "how-to-get-into-baulkham-hills-high-school-2026-admissions-rankings-and-preparation-strategy",
    "arizona-state-university-the-2026-insider-guide-to-admissions-fees-and-innovation",
    "appleby-college-canada-boarding-school-admissions-fees-student-life-guide-for-international-students"
]

def clean_html(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove page-meta production notes
    # Example: Tables, images and URL checked 20 August 2026 · Verify time-sensitive facts
    html = re.sub(r'(<div class="page-meta">.*?)(?:Tables, images and URL checked.*?· Verify time-sensitive facts)(.*?</div>)', r'\1\2', html)

    # 2. Remove editor-note production notes
    # Example: <div class="editor-note"><strong>Accuracy note:</strong> The original article structure, semantic table rows and useful editorial images have been restored. Admissions, fees, rankings and policies change; follow cited official sources and recheck the date before acting.</div>
    html = re.sub(r'<div class="editor-note"><strong>Accuracy note:</strong> The original article structure.*?</div>', '', html)

    # 3. Remove generic inline image
    html = re.sub(r'<figure class="editorial-figure">\s*<img[^>]*src="/media/articles/top-50-universities-in-usa-inline-03\.webp"[^>]*>\s*<figcaption>.*?</figcaption>\s*</figure>', '', html, flags=re.DOTALL)
    
    # 4. Remove superlatives (case insensitive but preserving case if we just replace with empty space or rewrite)
    # Since these are in H1s and titles, we can do targeted replacements
    
    if "The Ultimate Guide" in html:
        html = html.replace("The Ultimate Guide", "A Guide")
    if "the ultimate guide" in html:
        html = html.replace("the ultimate guide", "a guide")
    if "The ultimate guide" in html:
        html = html.replace("The ultimate guide", "A guide")
        
    html = html.replace("Best ", "")
    html = html.replace("most popular ", "")
    html = html.replace("leading ", "")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Cleaned {filepath}")

for u in urls:
    clean_html(f"{u}/index.html")
