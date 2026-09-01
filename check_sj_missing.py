import json
with open('assets/search-index.json', 'r', encoding='utf-8') as f:
    sj = json.load(f)

paths = [item['path'] for item in sj]
print('/top-100-international-schools-in-the-world/' in paths)
print('/tools/wam-calculator/' in paths)
print('/listing/boston-college/' in paths)