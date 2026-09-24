import re

files = [
    'college-ranking-red-flags-and-how-to-read-them/index.html',
    'where-is-columbia-university-in-nyc-the-ultimate-2026-location-campus-guide/index.html',
    'boarding-school-open-day-questions-checklist/index.html'
]

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    match = re.search(r'<article class="article-body">(.*?)</article>', html, re.DOTALL)
    if match:
        text = match.group(1)
        out_name = file.split('/')[0] + '.md'
        with open(out_name, 'w', encoding='utf-8') as f2:
            f2.write(text)
        print(f"Extracted {out_name}")