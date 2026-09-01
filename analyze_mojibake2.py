import os
import re

unique = set()
with open('mojibake_context.txt', 'w', encoding='utf-8') as out:
    for root, dirs, files in os.walk('.'):
        if '.git' in root or '.vercel' in root: continue
        for file in files:
            if file.endswith('.html') or file.endswith('.js'):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8', errors='replace') as f:
                        content = f.read()
                except Exception:
                    continue
                
                # We also look for Ac 
                for m in re.finditer(r'(.{0,15})(\ufffd.{0,3}|Ac )(.{0,15})', content):
                    match_str = m.group(2)
                    if match_str not in unique:
                        unique.add(match_str)
                        out.write(f"Pattern: {repr(match_str)} | Context: {repr(m.group(0))}\n")
