import json
with open('assets/search-index.json', 'r', encoding='utf-8') as f:
    sj = json.load(f)

for item in sj:
    if 'Bodwell' in item.get('title', ''):
        print(item)
    if 'Upper Canada' in item.get('title', ''):
        print(item)