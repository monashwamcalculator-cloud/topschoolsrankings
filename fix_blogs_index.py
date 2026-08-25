import os
import bs4
import csv

pack_dir = 'C:/Users/Hp/Downloads/seo_pack/topschools-content-pack'
site_dir = 'c:/Users/Hp/Downloads/topschoolsrankings-new-site-upload-v2'
csv_path = os.path.join(pack_dir, 'CONTENT-MAP.csv')
content_map = {}
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        content_map[row['article_file']] = row

blogs_list_cards = []
for filename, metadata in content_map.items():
    slug = metadata['slug']
    h1_title = metadata['meta_title'].split(' | ')[0]
    meta_desc = metadata['meta_description'].replace('"', '&quot;')
    featured = metadata['featured_image']
    
    # Format exactly as a guide-card
    blogs_list_cards.append(f"""
<article class="guide-card">
  <a class="guide-card-image" href="/{slug}/" aria-label="Read {h1_title}">
    <img src="/media/articles/{featured}" alt="{h1_title}" width="1600" height="900" loading="lazy" decoding="async">
  </a>
  <div class="card-meta">
    <span>New 2026 Ranking</span>
    <span>15 min read</span>
  </div>
  <h3><a href="/{slug}/">{h1_title}</a></h3>
  <p>{meta_desc}</p>
  <a class="text-link" href="/{slug}/">Read guide <span>→</span></a>
</article>
""")

blogs_index_path = os.path.join(site_dir, 'blogs', 'index.html')
with open(blogs_index_path, 'r', encoding='utf-8') as f:
    soup = bs4.BeautifulSoup(f.read(), 'html.parser')

grid = soup.find('div', class_='guide-grid')
if grid:
    # First remove any old injections if they somehow exist
    for a_tag in grid.find_all('a', class_='guide-card-image'):
        if any(v['slug'] in a_tag['href'] for v in content_map.values()):
            card = a_tag.find_parent('article')
            if card:
                card.decompose()
                
    # Insert new cards at top
    for card_html in reversed(blogs_list_cards):
        new_card = bs4.BeautifulSoup(card_html, 'html.parser').article
        grid.insert(0, new_card)

with open(blogs_index_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))
print('Successfully injected into guide-grid')
