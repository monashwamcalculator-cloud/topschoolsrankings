import os
import re
from collections import Counter

counts = Counter()

for root, dirs, files in os.walk('.'):
    if '.git' in root or '.vercel' in root: continue
    for file in files:
        if file.endswith('.html') or file.endswith('.js') or file.endswith('.json'):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8', errors='replace') as f:
                    content = f.read()
            except Exception:
                continue
            
            # Find all occurrences of the replacement char and get the 2 chars after it
            for m in re.finditer(r'\ufffd.{1,2}', content):
                counts[m.group(0)] += 1
                
            # Also look for 'Ac ' and 'A'
            for m in re.finditer(r'A\ufffd', content):
                counts[m.group(0)] += 1
            for m in re.finditer(r'Ac ', content):
                counts[m.group(0)] += 1

with open('mojibake_counts.txt', 'w', encoding='utf-8') as out:
    for k, v in counts.most_common():
        out.write(f"{repr(k)}: {v}\n")
