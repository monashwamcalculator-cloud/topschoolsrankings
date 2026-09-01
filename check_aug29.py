import json
with open('sj_aug29.json', 'r', encoding='utf-8') as f: sj = json.load(f)
print('Aug 29 search index:', len(sj))

import xml.etree.ElementTree as ET
tree = ET.parse('sitemap_aug29.xml')
locs = tree.getroot().findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
print('Aug 29 sitemap:', len(locs))