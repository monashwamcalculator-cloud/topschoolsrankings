import os

site_dir = 'c:/Users/Hp/Downloads/topschoolsrankings-new-site-upload-v2'
slugs = [
    'top-100-high-schools-usa',
    'top-100-grammar-schools-uk',
    'boarding-schools-canada',
    'top-100-boarding-schools-world',
    'top-100-international-schools-asia',
    'top-100-international-schools-world',
    'top-100-private-schools-canada',
    'top-100-high-schools-canada',
    'top-100-schools-australia',
    'top-100-private-schools-world'
]

for slug in slugs:
    filepath = os.path.join(site_dir, slug, 'index.html')
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('<article class="article-body">', '<article class="article-body rich-article-content">')
    html = html.replace('<div style="overflow-x:auto;"><table>', '<div class="table-scroll"><table>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        
print('Added rich-article-content to all 10 articles')
