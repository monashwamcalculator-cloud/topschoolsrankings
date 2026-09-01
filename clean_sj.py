import json
with open('assets/search-index.json', 'r', encoding='utf-8') as f:
    sj = json.load(f)

sj = [item for item in sj if 'temp_docx_extract' not in item['path'] and 'write-for-us' not in item['path']]

with open('assets/search-index.json', 'w', encoding='utf-8') as f:
    json.dump(sj, f, separators=(',', ':'))

print(f'Cleaned search index length: {len(sj)}')