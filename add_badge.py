import os

needle_badge = '''</svg></a></div><div style="margin-top:20px;"><a href="https://useneedle.net/directory/topschoolsrankings" target="_blank" rel="noopener noreferrer"><img src="https://useneedle.net/badges/needle-directory.svg" alt="Listed on Needle Directory" height="44" /></a></div></div>'''

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
        
        if 'useneedle.net' not in html:
            html = html.replace('</svg></a></div></div>\n      <div><h2>Research</h2>', needle_badge + '\n      <div><h2>Research</h2>')
            with open(file, 'w', encoding='utf-8') as f:
                f.write(html)
    except Exception as e:
        print(f"Skipping {file}: {e}")

print('Needle Directory badge injected into all HTML files.')