import os
import csv
import markdown
import re
from bs4 import BeautifulSoup

pack_dir = 'C:/Users/Hp/Downloads/seo_pack/topschools-content-pack'
site_dir = 'c:/Users/Hp/Downloads/topschoolsrankings-new-site-upload-v2'
articles_dir = os.path.join(pack_dir, 'articles')
schema_dir = os.path.join(pack_dir, 'schema')

# Read CSV to get exact meta title, description and slugs
csv_path = os.path.join(pack_dir, 'CONTENT-MAP.csv')
content_map = {}
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        content_map[row['article_file']] = row

# Mapping to schema files
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

blogs_list_cards = []

for filename, metadata in content_map.items():
    slug = metadata['slug']
    meta_title = metadata['meta_title']
    meta_desc = metadata['meta_description'].replace('"', '&quot;')
    
    filepath = os.path.join(articles_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        md_text = f.read()

    lines = md_text.split('\n')
    h1_title = lines[0].replace('# ', '').strip()
    md_text = '\n'.join(lines[1:])
    
    html_content = markdown.markdown(md_text, extensions=['tables', 'fenced_code'])
    html_content = re.sub(r'src="[^"]*/assets/featured/([^"]+)"', r'src="/media/articles/\1"', html_content)
    html_content = re.sub(r'src="[^"]*/assets/in-content/([^"]+)"', r'src="/media/articles/\1"', html_content)
    html_content = html_content.replace('<table>', '<div style="overflow-x:auto;"><table>')
    html_content = html_content.replace('</table>', '</table></div>')
    
    # Read schema
    schema_file = schema_map[filename]
    with open(os.path.join(schema_dir, schema_file), 'r', encoding='utf-8') as sf:
        schema_json = sf.read()

    full_html = build_html_page(slug, h1_title, meta_title, meta_desc, html_content, schema_json)
    
    out_dir = os.path.join(site_dir, slug)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    blogs_list_cards.append(f"""
<article class="listing-card">
  <h2><a href="/{slug}/">{h1_title}</a></h2>
  <p>{meta_desc}</p>
  <a href="/{slug}/">Read guide →</a>
</article>
""")
    
    print(f'Updated /{slug}/ with Schema & Exact Meta')

# Add to /blogs/index.html (replace old injected ones)
blogs_index_path = os.path.join(site_dir, 'blogs', 'index.html')
if os.path.exists(blogs_index_path):
    with open(blogs_index_path, 'r', encoding='utf-8') as f:
        soup_blogs = BeautifulSoup(f.read(), 'html.parser')
    
    grid = soup_blogs.find('div', class_='listing-grid')
    if grid:
        # Clear out existing ones if we run this multiple times by looking at the URL
        # For simplicity, let's just clear the grid entirely and re-add from our list
        # Wait, there might be other blogs in there. I'll just remove the newly added ones first.
        for a_tag in grid.find_all('a'):
            if any(v['slug'] in a_tag['href'] for v in content_map.values()):
                card = a_tag.find_parent('article')
                if card:
                    card.decompose()
                    
        for card_html in reversed(blogs_list_cards):
            new_card = BeautifulSoup(card_html, 'html.parser').article
            grid.insert(0, new_card)
            
        with open(blogs_index_path, 'w', encoding='utf-8') as f:
            f.write(str(soup_blogs))
        print('Updated /blogs/index.html cleanly')
