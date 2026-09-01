import json
with open('assets/search-index.json', 'r', encoding='utf-8') as f:
    sj = json.load(f)

changed = False
for item in sj:
    if 'Bodwell' in item.get('title', '') and 'Hard Strategy' in item.get('title', ''):
        item['title'] = 'Bodwell High School Acceptance Rate 2026: Bodwell High School Admissions Guide'
        changed = True

if changed:
    with open('assets/search-index.json', 'w', encoding='utf-8') as f:
        json.dump(sj, f, separators=(',', ':'))
    print('Fixed search-index.json')