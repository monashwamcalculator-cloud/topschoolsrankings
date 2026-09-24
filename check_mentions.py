import os
for r, d, files in os.walk('.'):
    if '.git' in r: continue
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(r, f)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
            if '135 retained profiles' in content or '46 free planning tools' in content:
                print(f"Found mention in {filepath}")