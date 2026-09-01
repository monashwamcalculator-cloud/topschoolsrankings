import os
import re

PROMO_PHRASES = [
    "Cracking the Bodwell Admission Code",
    "best private boys' school"
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
                for bp in PROMO_PHRASES:
                    if bp in content:
                        print(f'Found "{bp}" in {path}')
                        found += 1

print(f'Total bad promo phrases found: {found}')