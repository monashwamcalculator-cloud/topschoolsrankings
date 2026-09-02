import os

html_files = []
for root, dirs, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root or '.vercel' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        print(f'Error reading {file}: {e}')