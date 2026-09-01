import os
import re

MOJIBAKE = ['Ã¢', 'Ã‚', 'Ãƒ', 'â€™', 'â€œ', 'â€', 'â€“', 'â€”', 'Â']

found = 0
for root, dirs, files in os.walk('.'):
    if '.git' in root or '.vercel' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                for bp in MOJIBAKE:
                    if bp in content:
                        print(f'Found "{bp}" in {path}')
                        found += 1

print(f'Total mojibake found: {found}')