import re

# Add to blogs/index.html
with open('blogs/index.html', 'r', encoding='utf-8') as f:
    blogs_html = f.read()

new_card = '''<article class="guide-card"><a aria-label="Read Top 100 Finance Schools US Guide" class="guide-card-image" href="/top-100-finance-schools-in-us-guide/"><img alt="Top 100 Finance Schools US Guide" class="" decoding="async" height="844" loading="lazy" src="/media/articles/top-100-finance-schools-us.webp" width="1500"/></a><div class="card-meta"><span>Rankings & Guides</span><span>10 min read</span></div><h3><a href="/top-100-finance-schools-in-us-guide/">Top 100 Finance Schools & Business Universities in the US | 2026 Guide</a></h3><p>Discover the top 100 finance schools in the US. Compare target universities, Ivy League programs, and understand Wall Street recruiting.</p><a class="text-link" href="/top-100-finance-schools-in-us-guide/">Read the guide <span> </span></a></article>'''

if '/top-100-finance-schools-in-us-guide/' not in blogs_html:
    blogs_html = blogs_html.replace('<div class="guides-grid">', f'<div class="guides-grid">\n{new_card}')
    with open('blogs/index.html', 'w', encoding='utf-8') as f:
        f.write(blogs_html)
    print("Added to blogs")

# Add to sitemap.xml
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()

new_sitemap_entry = '''<url>
  <loc>https://topschoolsrankings.com/top-100-finance-schools-in-us-guide/</loc>
  <lastmod>2026-09-25T12:00:00+00:00</lastmod>
  <priority>0.80</priority>
</url>'''

if '/top-100-finance-schools-in-us-guide/' not in sitemap:
    sitemap = sitemap.replace('</urlset>', f'{new_sitemap_entry}\n</urlset>')
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print("Added to sitemap")