import re

files = [
    'seneca-polytechnic-seneca-college-admissions-fees-courses-career-opportunities-for-international-students/index.html',
    'monash-university-a-complete-2026-guide-for-usa-applicants/index.html'
]

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('\\,000', ',000') # Fix Seneca and Monash manually
    html = html.replace('ranges from ,000 to ,000 CAD', 'ranges from ,000 to ,000 CAD')
    html = html.replace('additional ,000500 to ,000500 CAD', 'additional ,500 to ,500 CAD')
    html = html.replace('ranges from ,000 to ,000 AUD per year (roughly ,000 to ,000 USD', 'ranges from ,000 to ,000 AUD per year (roughly ,000 to ,000 USD')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Fixed {file}")