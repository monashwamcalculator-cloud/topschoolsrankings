import os
import re

root_dir = '.'
skip_dirs = ['listing', 'tools', 'author', 'assets', 'media', '.git', 'node_modules', 'how-it-works', 'privacy-policy', 'terms-of-service', 'about', 'contact', 'compare', 'contact-us', 'about-us', 'disclaimer', 'terms-and-conditions', 'editorial-policy', 'faq', 'write-for-us', 'ranking-methodology']

results = []

for dirpath, dirnames, filenames in os.walk(root_dir):
    dirnames[:] = [d for d in dirnames if d not in skip_dirs]
    
    if 'index.html' in filenames:
        filepath = os.path.join(dirpath, 'index.html')
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                html = f.read()
                
                if 'content="noindex' in html.lower() or 'noindex, nofollow' in html.lower():
                    continue
                
                match = re.search(r'<article class="article-body">(.*?)</article>', html, re.DOTALL)
                if match:
                    body = match.group(1)
                    clean_text = re.sub(r'<[^>]+>', ' ', body)
                    words = len(clean_text.split())
                    if words < 1000:
                        results.append({'path': filepath, 'words': words})
        except Exception as e:
            pass

results = sorted(results, key=lambda x: x['words'])
with open("to_expand.txt", "w") as f:
    for r in results:
        f.write(r['path'] + "\n")

print(f"Found {len(results)} articles to expand.")
for r in results:
    print(f"{r['words']} - {r['path']}")