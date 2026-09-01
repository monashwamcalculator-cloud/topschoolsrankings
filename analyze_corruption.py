import os
import re
from collections import Counter

counts = Counter()

for root, dirs, files in os.walk('.'):
    if '.git' in root or '.vercel' in root: continue
    for file in files:
        if file.endswith('.html') or file.endswith('.json') or file.endswith('.js'):
            path = os.path.join(root, file)
            with open(path, 'rb') as f:
                b = f.read()
            
            # Find any sequence of \xe2\x80 followed by \xe2\x80... and finally a punctuation byte
            for m in re.finditer(b'(\xe2\x80)+([\x90-\x9f]|\xe2\x80[\x90-\xbf]|\xc2[\x80-\xbf])', b):
                # Only capture if it's actually invalid or part of the corruption
                match_bytes = m.group(0)
                counts[match_bytes] += 1

with open('corruptions.txt', 'w', encoding='utf-8') as out:
    for k, v in counts.most_common():
        out.write(f"{[hex(x) for x in k]}: {v}\n")
