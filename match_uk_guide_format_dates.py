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

with open(os.path.join(site_dir, 'how-to-choose-a-university-course-uk', 'index.html'), 'r', encoding='utf-8') as f:
    ref_soup = BeautifulSoup(f.read(), 'html.parser')

template_header = str(ref_soup.find('header', class_='site-header'))
template_footer = str(ref_soup.find('footer', class_='site-footer'))
evidence_bar = str(ref_soup.find('div', class_='evidence-bar'))
author_bio_box = str(ref_soup.find('div', class_='author-bio-box'))
related_guides = str(ref_soup.find('section', class_='related-guides'))
template_aside = str(ref_soup.find('aside', class_='article-aside'))

def build_html_page(slug, title, meta_title, meta_desc, html_content, schema_json, featured_src, featured_alt, fact_date):
    
    # Replace the hardcoded date in the aside block
    dynamic_aside = template_aside.replace('20 August 2026', fact_date)
    
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
<meta property="og:image" content="https://topschoolsrankings.com{featured_src}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://topschoolsrankings.com{featured_src}">
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
        <p>{meta_desc}</p>
        <div class="page-meta">Published {fact_date} · Reviewed by the TSR Editorial Desk · Official sources linked</div>
      </div>
    </header>
    
    <figure class="featured-media site-container narrow">
      <img src="{featured_src}" alt="{featured_alt}" width="1672" height="941" loading="eager" decoding="async">
      <figcaption>A practical visual introduction to this guide.</figcaption>
    </figure>
    
    <section class="section site-container article-layout">
      <article class="article-body">
        {html_content}
        
        {author_bio_box}
        
        {related_guides}
      </article>
      {dynamic_aside}
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

    # EXTRACT FACT CHECKED DATE
    fact_date = "24 August 2026"
    match = re.search(r'fact_checked:\s*"([^"]+)"', md_text)
    if match:
        fact_date = match.group(1)

    # STRIP YAML FRONTMATTER
    if md_text.startswith('---'):
        md_text = re.sub(r'^---[\s\S]*?---\n', '', md_text)
        
    # STRIP FIRST H1 TITLE if present
    md_text = re.sub(r'^# .*\n', '', md_text).lstrip()
    
    html_content = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])
    html_content = re.sub(r'src="[^"]*/assets/featured/([^"]+)"', r'src="/media/articles/\1"', html_content)
    html_content = re.sub(r'src="[^"]*/assets/in-content/([^"]+)"', r'src="/media/articles/\1"', html_content)
    html_content = html_content.replace('<table>', '<div style="overflow-x:auto;"><table>')
    html_content = html_content.replace('</table>', '</table></div>')
    
    soup_content = BeautifulSoup(html_content, 'html.parser')
    
    # Extract the first image (which is the featured image from markdown)
    featured_src = ""
    featured_alt = ""
    first_p = soup_content.find('p')
    if first_p and first_p.find('img'):
        img_tag = first_p.find('img')
        featured_src = img_tag.get('src', '')
        featured_alt = img_tag.get('alt', h1_title)
        first_p.decompose() # Remove from body content
        
    if not featured_src:
        featured_src = '/media/articles/' + metadata['featured_image'].split('/')[-1]
        featured_alt = h1_title

    html_content = str(soup_content)
    
    schema_file = schema_map[filename]
    with open(os.path.join(schema_dir, schema_file), 'r', encoding='utf-8') as sf:
        schema_json = sf.read()

    full_html = build_html_page(slug, h1_title, meta_title, meta_desc, html_content, schema_json, featured_src, featured_alt, fact_date)
    
    out_dir = os.path.join(site_dir, slug)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f'Re-generated formatting for /{slug}/ matching the UK course guide structure with dynamic dates')
