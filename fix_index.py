import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace "tools-" with "guides-"
html = html.replace('practical decision tools-not a single unexplained rank.', 'practical decision guides-not a single unexplained rank.')

# Strip out the commented stat-grid and tool-link-grid completely to be safe from bots
html = re.sub(r'<!--\s*<div class="stat-grid">.*?</div>\s*-->', '', html, flags=re.DOTALL)
html = re.sub(r'<!--\s*<div class="tool-link-grid">.*?</div>\s*-->', '', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)