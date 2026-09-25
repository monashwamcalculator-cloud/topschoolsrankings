import os
import shutil
import re

repo_dir = r'c:\Users\Hp\Downloads\topschoolsrankings-new-site-upload-v2'
src_img = r'C:\Users\Hp\.gemini\antigravity\brain\726bddf1-4614-4b0e-a924-9a6f84cfa50e\.user_uploaded\media_1790316467263.jpg'
dst_img_rel = r'media/articles/top-100-finance-schools-us-featured.jpg'
dst_img = os.path.join(repo_dir, dst_img_rel)
slug = 'top-100-finance-schools-us'
new_dir = os.path.join(repo_dir, slug)
new_html_path = os.path.join(new_dir, 'index.html')

if os.path.exists(src_img):
    os.makedirs(os.path.dirname(dst_img), exist_ok=True)
    shutil.copy(src_img, dst_img)

base_article = os.path.join(repo_dir, 'top-100-high-schools-in-usa', 'index.html')
with open(base_article, 'r', encoding='utf-8') as f:
    base_html = f.read()

new_title = 'Top 100 Finance Schools & Business Universities in the US | Definitive Guide'
new_desc = 'Discover the top 100 finance schools in the US. Compare target universities, Ivy League programs, and understand Wall Street recruiting pipelines and placement analysis.'
new_url = f'https://topschoolsrankings.com/{slug}/'
img_url = f'https://topschoolsrankings.com/{dst_img_rel}'

def replace_tag(html, start_tag, end_tag, replacement):
    pattern = re.compile(f'({re.escape(start_tag)}).*?({re.escape(end_tag)})', re.DOTALL)
    return pattern.sub(rf'\1{replacement}\2', html)

new_html = base_html
new_html = replace_tag(new_html, '<title>', '</title>', new_title)
new_html = replace_tag(new_html, '<meta name="description" content="', '">', new_desc)
new_html = replace_tag(new_html, '<link rel="canonical" href="', '">', new_url)
new_html = replace_tag(new_html, '<meta property="og:title" content="', '">', new_title)
new_html = replace_tag(new_html, '<meta property="og:description" content="', '">', new_desc)
new_html = replace_tag(new_html, '<meta property="og:url" content="', '">', new_url)

new_html = re.sub(r'<meta property="og:image" content=".*?">', f'<meta property="og:image" content="{img_url}">', new_html)
new_html = re.sub(r'<meta name="twitter:image" content=".*?">', f'<meta name="twitter:image" content="{img_url}">', new_html)
new_html = re.sub(r'"image": ".*?"', f'"image": "{img_url}"', new_html)
new_html = re.sub(r'"mainEntityOfPage": ".*?"', f'"mainEntityOfPage": "{new_url}"', new_html)
new_html = re.sub(r'"headline": ".*?"', f'"headline": "{new_title}"', new_html)

breadcrumbs = f'<nav class="breadcrumbs site-container" aria-label="Breadcrumb"><a href="/">Home</a><span><i aria-hidden="true">/</i><a href="/blogs/">Guides</a></span><span><i aria-hidden="true">/</i><b>Top 100 Finance Schools US</b></span></nav>'
new_html = re.sub(r'<nav class="breadcrumbs.*?</nav>', breadcrumbs, new_html, flags=re.DOTALL)

with open('user_html.txt', 'r', encoding='utf-8') as f:
    user_html = f.read()

new_html = re.sub(r'<header class="page-header">.*?</article>', user_html, new_html, flags=re.DOTALL)

os.makedirs(new_dir, exist_ok=True)
with open(new_html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

blogs_path = os.path.join(repo_dir, 'blogs/index.html')
with open(blogs_path, 'r', encoding='utf-8') as f:
    blogs_html = f.read()

new_card = f'<article class="guide-card"><a aria-label="Read Top 100 Finance Schools Guide" class="guide-card-image" href="/{slug}/"><img alt="Top 100 Finance Schools Guide" class="" decoding="async" height="844" loading="lazy" src="/{dst_img_rel}" width="1500"/></a><div class="card-meta"><span>Rankings & Guides</span><span>12 min read</span></div><h3><a href="/{slug}/">{new_title}</a></h3><p>{new_desc}</p><a class="text-link" href="/{slug}/">Read the guide <span> </span></a></article>'

if f'/{slug}/' not in blogs_html:
    blogs_html = blogs_html.replace('<div class="guides-grid">', f'<div class="guides-grid">\n{new_card}')
    with open(blogs_path, 'w', encoding='utf-8') as f:
        f.write(blogs_html)

sitemap_path = os.path.join(repo_dir, 'sitemap.xml')
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap = f.read()

new_sitemap_entry = f'<url>\n  <loc>https://topschoolsrankings.com/{slug}/</loc>\n  <lastmod>2026-09-25T12:00:00+00:00</lastmod>\n  <priority>0.80</priority>\n</url>'

if f'/{slug}/' not in sitemap:
    sitemap = sitemap.replace('</urlset>', f'{new_sitemap_entry}\n</urlset>')
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap)
