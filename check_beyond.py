import re

with open('how-to-compare-universities-beyond-rankings/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'<article class="article-body">(.*?)</article>', html, re.DOTALL)
if match:
    text = match.group(1)
    with open('beyond_content.md', 'w', encoding='utf-8') as f2:
        f2.write(text)