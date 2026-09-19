import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'<div class="tool-link-grid">.*?</div></section>'
replacement = r'<!-- <div class="tool-link-grid">...</div> --></section>'

# Just hide the tool-link-grid
content = re.sub(r'(<div class="tool-link-grid">.*?</div>)</section>', r'<!-- \1 --></section>', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)