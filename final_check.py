import os
def get_dirs(path):
    exclusions = {'.vercel', 'assets', 'author', 'blogs', 'category', 'compare', 'contact-us', 'disclaimer', 'editorial-policy', 'listings', 'media', 'privacy-policy', 'ranking-methodology', 'terms-and-conditions', 'tools', 'utils', 'about-us', 'listing', 'how-it-works', 'faq', 'wp-content', 'wpress-extracted', '_uploads_extract', '_import-live-jul2026', '_import-well-known', 'live-site-backup', 'dist', 'dist-deploy', 'upload-addon', '_zip-staging-tools-rich', '.git'}
    return set([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d)) and d not in exclusions])

print('BLOGS:', len(get_dirs('.')))
print('TOOLS:', len([d for d in os.listdir('tools') if os.path.isdir(os.path.join('tools', d))]))
print('LISTINGS:', len([d for d in os.listdir('listing') if os.path.isdir(os.path.join('listing', d))]))

import json
with open('assets/search-index.json', 'r', encoding='utf-8') as f:
    sj = json.load(f)
    print('SEARCH INDEX ITEMS:', len(sj))

import xml.etree.ElementTree as ET
try:
    sitemap = ET.parse('sitemap.xml').getroot()
    locs = sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
    print('SITEMAP URLs:', len(locs))
except Exception as e:
    print('Sitemap error:', e)