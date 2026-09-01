import os
import re

bad_phrases = [
    "Strictly Test-Blind",
    "Test-Blind",
    "Do not submit SAT/ACT",
    "Even a 1600 won't be looked at",
    "They do not look at SAT/ACT scores at all."
]

found = 0
for root, dirs, files in os.walk('.'):
    if '.git' in root or '.vercel' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                for bp in bad_phrases:
                    if re.search(re.escape(bp), content, flags=re.IGNORECASE):
                        print(f'Found "{bp}" in {path}')
                        found += 1

print(f'Total bad Caltech phrases found: {found}')