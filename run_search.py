import os
import json

strings_to_find = [
    'Œ•', '€¦', '€“', '‡’', 
    'No articles match your search', 
    'Strictly Test-Blind', 'Do not submit SAT/ACT', 'Test-Blind', 'Even a 1600', 'test-blind policy', 
    'Hard Strategy to Get Admitted', 'Cracking the Bodwell Admission Code', 'interview secrets', 'exact strategy', 
    'best private boys\' school in Toronto', 'one of the premier undergraduate entry processes globally'
]

results = {s: [] for s in strings_to_find}

for root, dirs, files in os.walk('.'):
    if '.git' in root or '.vercel' in root: continue
    for file in files:
        if file.endswith('.html') or file.endswith('.js') or file.endswith('.json'):
            path = os.path.join(root, file).replace('\\', '/')
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                for s in strings_to_find:
                    if s.lower() in content.lower():
                        results[s].append(path)
            except Exception:
                pass

for s, paths in results.items():
    if paths:
        print(f"FOUND '{s}' in {len(paths)} files. Sample: {paths[:3]}")
    else:
        print(f"NOT FOUND '{s}'")
