import os
import re

html_files = set()
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.normpath(os.path.join(root, f))
            # Convert to web path format
            webpath = filepath.replace('\\', '/').replace('index.html', '')
            if webpath.startswith('./'): webpath = webpath[2:]
            webpath = '/' + webpath
            html_files.add(webpath)

# Also add root
html_files.add('/')

broken_links = set()

for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                links = re.findall(r'href="(/[^"\.]+/?)"', content)
                for link in links:
                    if not link.endswith('/'): link += '/'
                    if link not in html_files and not link.startswith('/media') and not link.startswith('/css'):
                        broken_links.add((filepath, link))

for filepath, link in list(broken_links)[:20]:
    print(f"File: {filepath} -> Broken Link: {link}")
print(f"Total broken internal links found: {len(broken_links)}")