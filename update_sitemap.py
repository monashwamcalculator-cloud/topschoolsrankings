import xml.etree.ElementTree as ET
import os

ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')
tree = ET.parse('sitemap.xml')
root = tree.getroot()

existing_urls = set()
for loc in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
    existing_urls.add(loc.text)

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

import json
with open('assets/search-index.json', 'r', encoding='utf-8') as f:
    sj = json.load(f)

for item in sj:
    add_url(item['path'])

tree.write('sitemap.xml', encoding='utf-8', xml_declaration=True)
print('Updated sitemap.xml')