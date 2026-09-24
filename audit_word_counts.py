import os
import re

root_dir = '.'
skip_dirs = ['listing', 'tools', 'author', 'assets', 'media', '.git', 'node_modules', 'how-it-works', 'privacy-policy', 'terms-of-service', 'about', 'contact']

results = []

for dirpath, dirnames, filenames in os.walk(root_dir):
    # Skip specified directories
    dirnames[:] = [d for d in dirnames if d not in skip_dirs]
    
    if 'index.html' in filenames:
        filepath = os.path.join(dirpath, 'index.html')
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                html = f.read()
                
                # Skip noindex pages
                if 'content="noindex' in html.lower() or 'noindex, nofollow' in html.lower():
                    continue
                
                # We are looking for editorial articles with <article class="article-body">
                match = re.search(r'<article class="article-body">(.*?)</article>', html, re.DOTALL)
                if match:
                    body = match.group(1)
                    # Strip tags
                    clean_text = re.sub(r'<[^>]+>', ' ', body)
                    words = len(clean_text.split())
                    results.append({'path': filepath, 'words': words})
                else:
                    # Might be the homepage or a section hub like blogs/index.html
                    pass
        except Exception as e:
            pass

results = sorted(results, key=lambda x: x['words'])
print(f'Found {len(results)} indexable articles.')
print('\n--- Articles under 1000 words ---')
for r in results:
    if r['words'] < 1000:
        print(f"{r['words']} words - {r['path']}")

print('\n--- Articles 1000+ words (Sample of 5) ---')
for r in results[-5:]:
    print(f"{r['words']} words - {r['path']}")
