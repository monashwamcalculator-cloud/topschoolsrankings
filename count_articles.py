import os
import glob
import json
import xml.etree.ElementTree as ET
import subprocess

def get_dirs(commit):
    res = subprocess.check_output(['git', 'ls-tree', '-d', '--name-only', commit]).decode('utf-8')
    return set([d.strip() for d in res.split('\n') if d.strip() and d.strip() not in ('.vercel', 'assets', 'author', 'blogs', 'category', 'compare', 'contact-us', 'disclaimer', 'editorial-policy', 'listings', 'media', 'privacy-policy', 'ranking-methodology', 'terms-and-conditions', 'tools', 'utils', 'about-us', 'ranking-methodology')])

current_dirs = get_dirs('HEAD')
first_commit = subprocess.check_output(['git', 'rev-list', '--max-parents=0', 'HEAD']).decode('utf-8').strip()
initial_dirs = get_dirs(first_commit)

deleted = initial_dirs - current_dirs
added = current_dirs - initial_dirs

print(f'Initial article dirs: {len(initial_dirs)}')
print(f'Current article dirs: {len(current_dirs)}')
print('DELETED DIRS:', deleted)
print('ADDED DIRS:', added)

with open('blogs/index.html', 'r', encoding='utf-8') as f:
    html = f.read()
    print('Articles in blogs/index.html:', html.count('class="guide-card"'))

with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()
    print('Locs in sitemap.xml:', sitemap.count('<loc>'))

with open('assets/search-index.json', 'r', encoding='utf-8') as f:
    sj = json.load(f)
    print('Items in search-index.json:', len(sj))
