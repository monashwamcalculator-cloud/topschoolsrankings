import re

files = [
    'seneca-polytechnic-seneca-college-admissions-fees-courses-career-opportunities-for-international-students/index.html',
    'monash-university-a-complete-2026-guide-for-usa-applicants/index.html'
]

# Just run a straight string replacement for the mangled sections
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = re.sub(r'International tuition typically ranges from.*?CAD per year', 'International tuition typically ranges from ,000 to ,000 CAD per year', html)
    html = re.sub(r'budget an additional.*?CAD per month', 'budget an additional ,500 to ,500 CAD per month', html)
    
    html = re.sub(r'International tuition at Monash ranges from.*?USD, depending on exchange rates\)', 'International tuition at Monash ranges from ,000 to ,000 AUD per year (roughly ,000 to ,000 USD, depending on exchange rates)', html)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)