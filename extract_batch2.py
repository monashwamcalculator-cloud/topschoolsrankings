import re

files = [
    'seneca-polytechnic-seneca-college-admissions-fees-courses-career-opportunities-for-international-students/index.html',
    'glenunga-ignite-program-assessment-key-dates-acer-hast-registration-guide/index.html',
    'monash-university-a-complete-2026-guide-for-usa-applicants/index.html'
]

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    match = re.search(r'<article class="article-body">(.*?)</article>', html, re.DOTALL)
    if match:
        text = match.group(1)
        out_name = file.split('/')[0][:30] + '.md'
        with open(out_name, 'w', encoding='utf-8') as f2:
            f2.write(text)
        print(f"Extracted {out_name}")