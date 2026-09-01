import os

patterns = [
    'Strictly Test-Blind',
    'Test-Blind',
    'Do not submit SAT/ACT',
    'Even a 1600',
    'look at SAT/ACT scores at all',
    'test-optional'
]

found = 0
for root, dirs, files in os.walk('.'):
    if '.git' in root or '.vercel' in root or 'node_modules' in root: continue
    for file in files:
        if file.endswith('.html') or file.endswith('.json') or file.endswith('.js') or file.endswith('.css'):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception: continue
            
            for p in patterns:
                if p.lower() in content.lower():
                    print(f"FOUND Caltech pattern '{p}' in {path}")
                    found += 1
print(f"Total found: {found}")