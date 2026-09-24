import re

with open('complete-university-cost-comparison-checklist/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'<article class="article-body">(.*?)</article>', html, re.DOTALL)
if match:
    text = match.group(1)
    with open('cost_content.md', 'w', encoding='utf-8') as f2:
        f2.write(text)