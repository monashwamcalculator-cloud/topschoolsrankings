import os
import re

root_dir = '.'
skip_dirs = ['listing', 'tools', 'compare', 'author', 'assets', 'media', '.git', 'node_modules']

keywords = ['listing', 'listings', 'directory', 'tool ', 'tools']
findings = []

for dirpath, dirnames, filenames in os.walk(root_dir):
    dirnames[:] = [d for d in dirnames if d not in skip_dirs]
    
    for filename in filenames:
        if filename.endswith('.html'):
            filepath = os.path.join(dirpath, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    html = f.read()
                
                # strip script/style and html tags just to check text
                text = re.sub(r'<script.*?</script>', ' ', html, flags=re.DOTALL)
                text = re.sub(r'<style.*?</style>', ' ', text, flags=re.DOTALL)
                text = re.sub(r'<[^>]+>', ' ', text)
                
                text_lower = text.lower()
                for kw in keywords:
                    if kw in text_lower:
                        findings.append(f"{kw} found in {filepath}")
            except Exception as e:
                pass

for f in set(findings):
    print(f)
print(f"Total findings: {len(set(findings))}")