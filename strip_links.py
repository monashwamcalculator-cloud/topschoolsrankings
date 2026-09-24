import os
import re

files_modified = 0

for r, d, files in os.walk('.'):
    if '.git' in r: continue
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(r, f)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
            
            orig = content
            # Strip links to /listing/ and /listings/
            # Example: <a href="/listing/mit/">MIT</a> -> MIT
            content = re.sub(r'<a[^>]+href="[^"]*/listing(s)?/[^"]*"[^>]*>(.*?)</a>', r'\2', content, flags=re.IGNORECASE)
            # Strip links to /tools/
            content = re.sub(r'<a[^>]+href="[^"]*/tools/[^"]*"[^>]*>(.*?)</a>', r'\1', content, flags=re.IGNORECASE)

            if content != orig:
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(content)
                files_modified += 1

print(f"Modified {files_modified} files to remove listing/tools links.")