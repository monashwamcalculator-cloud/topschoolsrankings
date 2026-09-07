import re

with open('top50_old_content.html', 'r', encoding='utf-8') as f:
    html = f.read()

tables = []
idx = 0
while True:
    start = html.find('<table>', idx)
    if start == -1:
        break
    end = html.find('</table>', start) + len('</table>')
    tables.append(html[start:end])
    idx = end

for i, t in enumerate(tables):
    print(f"Table {i}: {len(t)} chars. First 50 chars: {t[:50]}")