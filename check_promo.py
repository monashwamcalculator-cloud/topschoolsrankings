import os

patterns = [
    'Hard Strategy to Get Admitted',
    'Cracking the Bodwell Admission Code',
    'interview secrets',
    'exact strategy',
    'best private boys'' school in Toronto',
    'best private boys'' school'
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
                    print(f"FOUND Promo pattern '{p}' in {path}")
                    found += 1
print(f"Total promo found: {found}")