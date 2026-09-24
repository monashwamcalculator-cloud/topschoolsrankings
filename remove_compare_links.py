import os

root_dir = '.'
modified_count = 0

for dirpath, dirnames, filenames in os.walk(root_dir):
    if '.git' in dirnames:
        dirnames.remove('.git')
    
    for filename in filenames:
        if filename.endswith('.html'):
            filepath = os.path.join(dirpath, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    html = f.read()
                
                original_html = html
                # Remove from desktop-nav and mobile-nav
                html = html.replace('<a href="/compare/">Compare</a>', '')
                # Remove from footer Research section
                html = html.replace('<a href="/compare/">Comparisons</a>', '')
                
                if original_html != html:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(html)
                    modified_count += 1
            except Exception as e:
                pass

print(f"Removed /compare/ navigation links from {modified_count} HTML files.")