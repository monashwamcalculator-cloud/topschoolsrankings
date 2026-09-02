import os
import re

css_path = 'assets/site.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Add display: block to .guide-card-image so aspect-ratio actually works
if 'display: block;' not in css.split('.guide-card-image {')[1].split('}')[0]:
    css = css.replace('.guide-card-image { margin: -24px -24px 20px; aspect-ratio: 16 / 9;', '.guide-card-image { display: block; margin: -24px -24px 20px; aspect-ratio: 16 / 9;')
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)
    print('Updated CSS.')

# Update logo across all HTML files
html_files = []
for root, dirs, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root or '.vercel' in root or 'venv' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            html = f.read()
            
        old_html = html
        html = html.replace(
            '<img src="/assets/logo.png" alt="Top Schools Rankings" style="height:60px; width:auto; max-width:100%;">',
            '<img src="/assets/logo.png" alt="Top Schools Rankings" width="899" height="239" style="height:60px; width:auto; max-width:100%;">'
        )
        
        if html != old_html:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(html)
    except Exception as e:
        print(f'Skipping {file}: {e}')

print('Done fixing logo in HTML.')