import os
import json

phrases = [
    "Hard Strategy to Get Admitted",
    "Cracking the Bodwell Admission Code",
    "best private boys' school in Toronto",
    "best private boys’ school in Toronto"
]

found = False
for root, dirs, files in os.walk('.'):
    if '.git' in root or '.vercel' in root: continue
    for file in files:
        if file.endswith('.html') or file.endswith('.json') or file.endswith('.js'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                for p in phrases:
                    if p.lower() in content.lower():
                        print(f"ERROR: Found '{p}' in {path}")
                        found = True

if not found:
    print("Repository search: ZERO occurrences.")

# Validate JSON
try:
    with open('assets/search-index.json', 'r', encoding='utf-8') as f:
        json.loads(f.read())
    print("assets/search-index.json is valid JSON.")
except Exception as e:
    print("ERROR validating JSON:", e)

