import os
import re

mojibake_patterns = [
    'â€™', 'â€“', 'â€”', 'â€œ', 'â€\x9d', 'â€¦', 'Ã©', 'Ã', 'Â', 
    '€¦', '€“', '€”', '‡’', 'Œ•', '\xef\xbf\xbd'
]

count = 0
files_set = set()

for root, dirs, files in os.walk('.'):
    if '.git' in root or '.vercel' in root: continue
    for file in files:
        if file.endswith('.html') or file.endswith('.js') or file.endswith('.json'):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception:
                continue
                
            for p in mojibake_patterns:
                if p in content:
                    count += content.count(p)
                    files_set.add(path)

print(f"Mojibake patterns found: {count} in {len(files_set)} files")

for sf in list(files_set)[:10]:
    with open(sf, 'r', encoding='utf-8') as f:
        content = f.read()
        for p in mojibake_patterns:
            idx = content.find(p)
            if idx != -1:
                snippet = content[max(0, idx-15):min(len(content), idx+15)]
                print(f"File: {sf} | Pattern: {repr(p)} | Snippet: {repr(snippet)}")
                break
