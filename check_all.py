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
        
        if 'Guest Post' in html or 'Guest Contributor' in html or 'Sponsored' in html or 'Partner Content' in html:
            print(f'Found forbidden term in {file}')
    except Exception as e:
        pass