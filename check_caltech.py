import os
import re

CALTECH_PHRASES = [
    ("strictly test-blind", "test-free"),
    ("even a 1600 won't be looked at", "standardized test scores are optional but considered if submitted"),
    ("they do not look at sat/act scores at all.", "they will consider sat/act scores as part of their evaluation process."),
    ("do not submit sat/act", "sat/act submission is optional"),
    ("test-blind", "test-free")
]

count = 0
for root, dirs, files in os.walk('.'):
    if '.git' in root or '.vercel' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html') or file.endswith('.json') or file.endswith('.xml'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception:
                continue
                
            original = content
            for bad, good in CALTECH_PHRASES:
                content = re.sub(re.escape(bad), good, content, flags=re.IGNORECASE)
                
            if content != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
print(f'Fixed {count} files.')