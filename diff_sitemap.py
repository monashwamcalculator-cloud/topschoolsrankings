import xml.etree.ElementTree as ET

ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')

tree1 = ET.parse('sitemap_aug29.xml')
urls1 = set([loc.text for loc in tree1.getroot().findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')])

tree2 = ET.parse('sitemap.xml')
urls2 = set([loc.text for loc in tree2.getroot().findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')])

print(f"August 29 URLs: {len(urls1)}")
print(f"Restoration URLs: {len(urls2)}")

added = urls2 - urls1
removed = urls1 - urls2

print("\nAdded URLs:")
for u in added: print(u)

print("\nRemoved URLs:")
for u in removed: print(u)