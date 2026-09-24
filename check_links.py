import os
for r, d, files in os.walk('.'):
    if '.git' in r: continue
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(r, f)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
            if 'href="/tools/' in content or 'href="/listings/' in content or 'href="/listing/' in content:
                print(f"Found link in {filepath}")