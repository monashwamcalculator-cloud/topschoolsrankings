import os

mojibake_patterns = [
    'â€™', 'â€“', 'â€”', 'â€œ', 'â€\x9d', 'â€¦', 'Ã©', 'Ã', 'Â', '€¦', '€“', '€”', '‡’', 'Œ•', ''
]

count_before = 0
files_with_mojibake = set()

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
                
            found_in_file = False
            for p in mojibake_patterns:
                if p in content:
                    count_before += content.count(p)
                    found_in_file = True
            
            if found_in_file:
                files_with_mojibake.add(path)

print(f"Mojibake patterns found: {count_before} occurrences in {len(files_with_mojibake)} files")

for sf in list(files_with_mojibake)[:10]:
    with open(sf, 'r', encoding='utf-8') as f:
        content = f.read()
        for p in mojibake_patterns:
            idx = content.find(p)
            if idx != -1:
                print(f"File: {sf} | Pattern: {repr(p)} | Snippet: {repr(content[max(0, idx-15):min(len(content), idx+15)])}")
                break
