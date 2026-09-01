import os
import glob
import markdown
import shutil
import re
from bs4 import BeautifulSoup

pack_dir = 'C:/Users/Hp/Downloads/seo_pack/topschools-content-pack'
site_dir = 'c:/Users/Hp/Downloads/topschoolsrankings-new-site-upload-v2'
articles_dir = os.path.join(pack_dir, 'articles')
assets_dir = os.path.join(pack_dir, 'assets')

slug_map = {
    'top-100-international-schools-world.md': 'top-100-international-schools-in-the-world',
    'top-100-international-schools-asia.md': 'top-100-international-schools-in-asia',
    'top-100-boarding-schools-world.md': 'top-100-boarding-schools-in-the-world',
    'boarding-schools-canada.md': 'boarding-schools-in-canada',
    'top-100-private-schools-world.md': 'top-100-private-schools-in-the-world',
    'top-100-private-schools-canada.md': 'top-100-private-schools-in-canada',
    'top-100-high-schools-canada.md': 'top-100-high-schools-in-canada',
    'top-100-high-schools-usa.md': 'top-100-high-schools-in-usa',
    'top-100-schools-australia.md': 'top-100-schools-in-australia',
    'top-100-grammar-schools-uk.md': 'top-100-grammar-schools-in-uk'
}

media_dest = os.path.join(site_dir, 'media', 'articles')
os.makedirs(media_dest, exist_ok=True)

for root, _, files in os.walk(assets_dir):
    for file in files:
        if file.endswith('.webp') or file.endswith('.svg') or file.endswith('.png'):
            shutil.copy2(os.path.join(root, file), os.path.join(media_dest, file))

with open(os.path.join(site_dir, 'top-50-universities-in-usa', 'index.html'), 'r', encoding='utf-8') as f:
    template_html = f.read()

soup = BeautifulSoup(template_html, 'html.parser')
template_header = str(soup.find('header', class_='site-header'))
template_footer = str(soup.find('footer', class_='site-footer'))
evidence_bar = str(soup.find('div', class_='evidence-bar'))

def build_html_page(slug, title, html_content, meta_desc):
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | Top Schools Rankings</title>
<meta name="description" content="{meta_desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://topschoolsrankings.com/{slug}/">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Top Schools Rankings">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta_desc}">
<meta property="og:url" content="https://topschoolsrankings.com/{slug}/">
<meta property="og:image" content="https://topschoolsrankings.com/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://topschoolsrankings.com/og.png">
<link rel="icon" href="/favicon.jpg">
<link rel="stylesheet" href="/assets/site.css">
<script src="/assets/site.js" defer></script>
</head>
<body>
  {evidence_bar}
  {template_header}
  <main>
    <nav class="breadcrumbs site-container" aria-label="Breadcrumb">
      <a href="/">Home</a><span><i aria-hidden="true">/</i><a href="/blogs/">Guides</a></span><span><i aria-hidden="true">/</i><b>{title}</b></span>
    </nav>
    
    <header class="page-header">
      <div class="site-container narrow">
        <span class="eyebrow">Comprehensive Guide</span>
        <h1>{title}</h1>
      </div>
    </header>
    
    <section class="section site-container article-layout">
      <article class="article-body rich-article-content">
        {html_content}
      </article>
      <aside class="article-aside">
        <div>
          <span class="aside-label">Author</span>
          <strong>Saahil</strong>
          <p>Educational researcher and writer.</p>
        </div>
        <div>
          <span class="aside-label">Correction</span>
          <a href="/contact-us/">Report an issue →</a>
        </div>
      </aside>
    </section>
  </main>
  {template_footer}
</body>
</html>"""
    return page

sitemap_links = []
blogs_list_cards = []

for filename, slug in slug_map.items():
    filepath = os.path.join(articles_dir, filename)
    if not os.path.exists(filepath):
        print(f'Missing {filepath}')
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        md_text = f.read()

    lines = md_text.split('\\n')
    title = lines[0].replace('# ', '').strip()
    
    # Let's fix lines parsing, split by newline character properly
    lines = md_text.split('\n')
    title = lines[0].replace('# ', '').strip()
    md_text = '\n'.join(lines[1:])
    
    html_content = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])
    
    # Fix image paths
    html_content = re.sub(r'src="[^"]*/assets/featured/([^"]+)"', r'src="/media/articles/\1"', html_content)
    html_content = re.sub(r'src="[^"]*/assets/in-content/([^"]+)"', r'src="/media/articles/\1"', html_content)
    
    # Add responsive class to tables
    html_content = html_content.replace('<table>', '<div style="overflow-x:auto;"><table>')
    html_content = html_content.replace('</table>', '</table></div>')

    out_dir = os.path.join(site_dir, slug)
    os.makedirs(out_dir, exist_ok=True)
    
    first_p = re.search(r'<p>(.*?)</p>', html_content, re.DOTALL)
    meta_desc = (first_p.group(1)[:150] + '...') if first_p else title
    meta_desc = re.sub(r'<[^>]+>', '', meta_desc).replace('"', '&quot;')
    
    full_html = build_html_page(slug, title, html_content, meta_desc)
    
    with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    sitemap_links.append(f"""  <url>
    <loc>https://topschoolsrankings.com/{slug}/</loc>
    <lastmod>2026-08-25</lastmod>
  </url>""")

    blogs_list_cards.append(f"""
<article class="listing-card">
  <h2><a href="/{slug}/">{title}</a></h2>
  <p>{meta_desc}</p>
  <a href="/{slug}/">Read guide →</a>
</article>
""")
    
    print(f'Generated /{slug}/')

# Handle Redirect
redirect_html = """<!doctype html><html><head><meta http-equiv="refresh" content="0; url=/boarding-schools-in-canada/"><link rel="canonical" href="https://topschoolsrankings.com/boarding-schools-in-canada/"></head><body>Redirecting to <a href="/boarding-schools-in-canada/">/boarding-schools-in-canada/</a></body></html>"""
redirect_dir = os.path.join(site_dir, 'top-20-canadian-boarding-schools')
os.makedirs(redirect_dir, exist_ok=True)
with open(os.path.join(redirect_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(redirect_html)
print('Added redirect for /top-20-canadian-boarding-schools/')

# Update sitemap
sitemap_path = os.path.join(site_dir, 'sitemap.xml')
if os.path.exists(sitemap_path):
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        sm_content = f.read()
    sm_content = sm_content.replace('</urlset>', '\n'.join(sitemap_links) + '\n</urlset>')
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sm_content)
    print('Updated sitemap.xml')

# Add to /blogs/index.html
blogs_index_path = os.path.join(site_dir, 'blogs', 'index.html')
if os.path.exists(blogs_index_path):
    with open(blogs_index_path, 'r', encoding='utf-8') as f:
        soup_blogs = BeautifulSoup(f.read(), 'html.parser')
    
    grid = soup_blogs.find('div', class_='listing-grid')
    if grid:
        for card_html in reversed(blogs_list_cards): # so they appear in order
            new_card = BeautifulSoup(card_html, 'html.parser').article
            grid.insert(0, new_card)
        with open(blogs_index_path, 'w', encoding='utf-8') as f:
            f.write(str(soup_blogs))
        print('Updated /blogs/index.html with 10 new articles')
