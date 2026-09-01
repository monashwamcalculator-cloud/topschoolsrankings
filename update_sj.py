import os
import json
from bs4 import BeautifulSoup

def get_dirs(path):
    exclusions = {'.vercel', 'assets', 'author', 'blogs', 'category', 'compare', 'contact-us', 'disclaimer', 'editorial-policy', 'listings', 'media', 'privacy-policy', 'ranking-methodology', 'terms-and-conditions', 'tools', 'utils', 'about-us', 'listing', 'how-it-works', 'faq', 'wp-content', 'wpress-extracted', '_uploads_extract', '_import-live-jul2026', '_import-well-known', 'live-site-backup', 'dist', 'dist-deploy', 'upload-addon', '_zip-staging-tools-rich', '.git'}
    return set([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d)) and d not in exclusions])

articles = get_dirs('.')
tools = set([d for d in os.listdir('tools') if os.path.isdir(os.path.join('tools', d))])
listings = set([d for d in os.listdir('listing') if os.path.isdir(os.path.join('listing', d))])

with open('assets/search-index.json', 'r', encoding='utf-8') as f:
    sj = json.load(f)

existing_paths = set([item['path'] for item in sj])

added = 0
for a in articles:
    path = f'/{a}/'
    if path not in existing_paths:
        try:
            with open(os.path.join(a, 'index.html'), 'r', encoding='utf-8', errors='ignore') as f:
                html = f.read()
            title = html.split('<title>')[1].split('</title>')[0] if '<title>' in html else a.replace('-', ' ').title()
            sj.append({"path": path, "title": title, "type": "article"})
            added += 1
        except: pass

for t in tools:
    path = f'/tools/{t}/'
    if path not in existing_paths:
        try:
            with open(os.path.join('tools', t, 'index.html'), 'r', encoding='utf-8', errors='ignore') as f:
                html = f.read()
            title = html.split('<title>')[1].split('</title>')[0] if '<title>' in html else t.replace('-', ' ').title()
            sj.append({"path": path, "title": title, "type": "tool"})
            added += 1
        except: pass

for l in listings:
    path = f'/listing/{l}/'
    if path not in existing_paths:
        try:
            with open(os.path.join('listing', l, 'index.html'), 'r', encoding='utf-8', errors='ignore') as f:
                html = f.read()
            title = html.split('<title>')[1].split('</title>')[0].split(' | ')[0] if '<title>' in html else l.replace('-', ' ').title()
            sj.append({"path": path, "title": title, "type": "listing"})
            added += 1
        except: pass

with open('assets/search-index.json', 'w', encoding='utf-8') as f:
    json.dump(sj, f, separators=(',', ':'))

print(f'Added {added} items to search-index.json')
print(f'New search index length: {len(sj)}')