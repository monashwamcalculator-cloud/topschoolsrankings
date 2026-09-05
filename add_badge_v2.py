import os

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
            # We look for the exact end of the social links block
            target = '</svg></a></div></div>'
            replacement = '</svg></a></div><div style="margin-top:20px;"><a href="https://useneedle.net/directory/topschoolsrankings" target="_blank" rel="noopener noreferrer"><img src="https://useneedle.net/badges/needle-directory.svg" alt="Listed on Needle Directory" height="44" /></a></div></div>'
            
            # Since target might appear multiple times if the footer is repeated (it shouldn't be), we only replace the last occurrence or just replace all (only 1 expected)
            if target in html:
                html = html.replace(target, replacement)
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(html)
    except Exception as e:
        pass

print('Done.')