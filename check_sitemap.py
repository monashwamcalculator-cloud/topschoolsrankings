import xml.etree.ElementTree as ET
ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')
tree = ET.parse('sitemap.xml')
root = tree.getroot()
locs = root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
print(len(locs))