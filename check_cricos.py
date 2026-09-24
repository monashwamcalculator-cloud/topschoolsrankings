import re

with open('how-to-verify-an-australian-cricos-course/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'<article class="article-body">(.*?)</article>', html, re.DOTALL)
if match:
    text = match.group(1)
    with open('cricos_content.md', 'w', encoding='utf-8') as f2:
        f2.write(text)