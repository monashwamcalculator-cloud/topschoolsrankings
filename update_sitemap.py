import re

with open('sitemap.xml', 'r', encoding='utf-8') as f:
    xml = f.read()

new_url = '''<url>
    <loc>https://topschoolsrankings.com/how-universities-are-using-custom-software-solutions-to-build-smarter-digital-education-ecosystems/</loc>
    <lastmod>2026-09-02</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
</url>
<url>
    <loc>https://topschoolsrankings.com/author/samrat-biswas/</loc>
    <lastmod>2026-09-02</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
</url>
'''

if 'samrat-biswas' not in xml:
    xml = xml.replace('</urlset>', new_url + '</urlset>')
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(xml)
    print('Added to sitemap.')