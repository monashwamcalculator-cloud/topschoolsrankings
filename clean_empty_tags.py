import os

empty_tags = [
    '<div class="page-meta"></div>',
    '<figure></figure>',
    '<figure>\n</figure>',
    '<figure> \n</figure>',
    '<figure> </figure>'
]

for root, dirs, files in os.walk('.'):
    for name in files:
        if name.endswith('index.html'):
            filepath = os.path.join(root, name)
            with open(filepath, 'r', encoding='utf-8') as f:
                html = f.read()
            
            original_html = html
            for tag in empty_tags:
                html = html.replace(tag, '')
                
            if html != original_html:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(html)
                print(f"Cleaned empty tags in {filepath}")