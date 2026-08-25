import os
import csv

site_dir = 'c:/Users/Hp/Downloads/topschoolsrankings-new-site-upload-v2'
pack_dir = 'C:/Users/Hp/Downloads/seo_pack/topschools-content-pack'
csv_path = os.path.join(pack_dir, 'CONTENT-MAP.csv')

slugs = []
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        slugs.append(row['slug'])

for slug in slugs:
    filepath = os.path.join(site_dir, slug, 'index.html')
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('<article class="article-body">', '<article class="article-body rich-article-content">')
    html = html.replace('<div style="overflow-x:auto;"><table>', '<div class="table-scroll"><table>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        
print('Added rich-article-content to all 10 articles')
