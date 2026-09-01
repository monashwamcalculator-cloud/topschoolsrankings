import os
import json
import xml.etree.ElementTree as ET

ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')
tree = ET.parse('sitemap_aug29.xml')
root = tree.getroot()

existing_urls = set()
for loc in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
    existing_urls.add(loc.text)

# We want to make sure temp_docx_extract is completely removed from sitemap if it was there
for url_el in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
    loc = url_el.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
    if loc is not None and 'temp_docx_extract' in loc.text:
        root.remove(url_el)
        existing_urls.remove(loc.text)

def get_dirs(path):
    exclusions = {'.vercel', 'assets', 'author', 'blogs', 'category', 'compare', 'contact-us', 'disclaimer', 'editorial-policy', 'listings', 'media', 'privacy-policy', 'ranking-methodology', 'terms-and-conditions', 'tools', 'utils', 'about-us', 'listing', 'how-it-works', 'faq', 'wp-content', 'wpress-extracted', '_uploads_extract', '_import-live-jul2026', '_import-well-known', 'live-site-backup', 'dist', 'dist-deploy', 'upload-addon', '_zip-staging-tools-rich', '.git', 'temp_docx_extract'}
    return set([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d)) and d not in exclusions])

articles = get_dirs('.')
tools = set([d for d in os.listdir('tools') if os.path.isdir(os.path.join('tools', d))])
listings = set([d for d in os.listdir('listing') if os.path.isdir(os.path.join('listing', d))])

with open('sj_aug29.json', 'r', encoding='utf-8') as f:
    sj = json.load(f)

# filter out temp_docx_extract if it exists
sj = [item for item in sj if 'temp_docx_extract' not in item['path']]

existing_paths = set([item['path'] for item in sj])

added_sj = 0
for a in articles:
    if a == 'write-for-us':
        continue # not an article in search index
    path = f'/{a}/'
    if path not in existing_paths:
        try:
            with open(os.path.join(a, 'index.html'), 'r', encoding='utf-8', errors='ignore') as f:
                html = f.read()
            title = html.split('<title>')[1].split('</title>')[0] if '<title>' in html else a.replace('-', ' ').title()
            sj.append({"path": path, "title": title, "type": "article"})
            added_sj += 1
        except: pass

for t in tools:
    if t == 'index.html': continue
    path = f'/tools/{t}/'
    if path not in existing_paths:
        try:
            with open(os.path.join('tools', t, 'index.html'), 'r', encoding='utf-8', errors='ignore') as f:
                html = f.read()
            title = html.split('<title>')[1].split('</title>')[0] if '<title>' in html else t.replace('-', ' ').title()
            sj.append({"path": path, "title": title, "type": "tool"})
            added_sj += 1
        except: pass

for l in listings:
    path = f'/listing/{l}/'
    if path not in existing_paths:
        try:
            with open(os.path.join('listing', l, 'index.html'), 'r', encoding='utf-8', errors='ignore') as f:
                html = f.read()
            title = html.split('<title>')[1].split('</title>')[0].split(' | ')[0] if '<title>' in html else l.replace('-', ' ').title()
            sj.append({"path": path, "title": title, "type": "listing"})
            added_sj += 1
        except: pass

with open('assets/search-index.json', 'w', encoding='utf-8') as f:
    json.dump(sj, f, separators=(',', ':'))

def add_url(path):
    url = f'https://topschoolsrankings.com{path}'
    if url not in existing_urls:
        url_el = ET.SubElement(root, 'url')
        loc_el = ET.SubElement(url_el, 'loc')
        loc_el.text = url
        lastmod_el = ET.SubElement(url_el, 'lastmod')
        lastmod_el.text = '2026-08-29'
        priority_el = ET.SubElement(url_el, 'priority')
        priority_el.text = '0.80'
        existing_urls.add(url)

# Make sure all valid paths are in sitemap
for item in sj:
    add_url(item['path'])

if 'write-for-us' in articles:
    add_url('/write-for-us/')

# We need to manually make sure all articles are in the sitemap if they were somehow missed in search-index
for a in articles:
    add_url(f'/{a}/')
for t in tools:
    if t != 'index.html': add_url(f'/tools/{t}/')
for l in listings:
    add_url(f'/listing/{l}/')

tree.write('sitemap.xml', encoding='utf-8', xml_declaration=True)
print(f'New search index length: {len(sj)}')
print(f'New sitemap length: {len(existing_urls)}')