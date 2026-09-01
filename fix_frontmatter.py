import os
import csv
import markdown
import re
from bs4 import BeautifulSoup

pack_dir = 'C:/Users/Hp/Downloads/seo_pack/topschools-content-pack'
site_dir = 'c:/Users/Hp/Downloads/topschoolsrankings-new-site-upload-v2'
articles_dir = os.path.join(pack_dir, 'articles')
schema_dir = os.path.join(pack_dir, 'schema')

csv_path = os.path.join(pack_dir, 'CONTENT-MAP.csv')
content_map = {}
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        content_map[row['article_file']] = row

schema_map = {
    'top-100-high-schools-usa.md': 'usa.json',
    'top-100-grammar-schools-uk.md': 'grammar_uk.json',
    'boarding-schools-canada.md': 'boarding_canada.json',
    'top-100-boarding-schools-world.md': 'boarding_world.json',
    'top-100-international-schools-asia.md': 'international_asia.json',
    'top-100-international-schools-world.md': 'international_world.json',
    'top-100-private-schools-canada.md': 'private_canada.json',
    'top-100-high-schools-canada.md': 'high_canada.json',
    'top-100-schools-australia.md': 'australia.json',
    'top-100-private-schools-world.md': 'private_world.json'
}

with open(os.path.join(site_dir, 'top-50-universities-in-usa', 'index.html'), 'r', encoding='utf-8') as f:
    template_html = f.read()

soup = BeautifulSoup(template_html, 'html.parser')
template_header = str(soup.find('header', class_='site-header'))
template_footer = str(soup.find('footer', class_='site-footer'))
evidence_bar = str(soup.find('div', class_='evidence-bar'))

def build_html_page(slug, title, meta_title, meta_desc, html_content, schema_json):
    page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{meta_title}</title>
<meta name="description" content="{meta_desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://topschoolsrankings.com/{slug}/">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Top Schools Rankings">
<meta property="og:title" content="{meta_title}">
<meta property="og:description" content="{meta_desc}">
<meta property="og:url" content="https://topschoolsrankings.com/{slug}/">
<meta property="og:image" content="https://topschoolsrankings.com/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://topschoolsrankings.com/og.png">
<link rel="icon" href="/favicon.jpg">
<link rel="stylesheet" href="/assets/site.css">
<script src="/assets/site.js" defer></script>
<script type="application/ld+json">
{schema_json}
</script>
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

for filename, metadata in content_map.items():
    slug = metadata['slug']
    meta_title = metadata['meta_title']
    meta_desc = metadata['meta_description'].replace('"', '&quot;')
    h1_title = metadata['meta_title'].split(' | ')[0]
    
    filepath = os.path.join(articles_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # STRIP YAML FRONTMATTER
    if md_text.startswith('---'):
        md_text = re.sub(r'^---[\s\S]*?---\n', '', md_text)
        
    # STRIP FIRST H1 TITLE if present
    md_text = re.sub(r'^# .*\n', '', md_text).lstrip()
    
    # STRIP the featured image at the top if it's the first thing
    # e.g. ![...](../assets/featured/...)
    # This avoids duplication if we want to cleanly start with the content
    # Wait, the markdown has the image at the top of the body. Let's keep the image so it shows at the top of the article body, just replace the path.
    
    html_content = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])
    html_content = re.sub(r'src="[^"]*/assets/featured/([^"]+)"', r'src="/media/articles/\1"', html_content)
    html_content = re.sub(r'src="[^"]*/assets/in-content/([^"]+)"', r'src="/media/articles/\1"', html_content)
    html_content = html_content.replace('<table>', '<div style="overflow-x:auto;"><table>')
    html_content = html_content.replace('</table>', '</table></div>')
    
    schema_file = schema_map[filename]
    with open(os.path.join(schema_dir, schema_file), 'r', encoding='utf-8') as sf:
        schema_json = sf.read()

    full_html = build_html_page(slug, h1_title, meta_title, meta_desc, html_content, schema_json)
    
    out_dir = os.path.join(site_dir, slug)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f'Fixed formatting for /{slug}/')

