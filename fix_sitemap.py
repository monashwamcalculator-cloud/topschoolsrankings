import os, re
sitemap_path = 'sitemap.xml'
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap = f.read()
new_sitemap = re.sub(r'<url>\s*<loc>[^<]*(/listings/)[^<]*</loc>.*?</url>', '', sitemap, flags=re.IGNORECASE|re.DOTALL)
with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(new_sitemap)