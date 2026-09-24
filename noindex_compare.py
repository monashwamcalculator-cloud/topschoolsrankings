import os
import re

compare_dir = 'compare'
modified_files = []

for dirpath, _, filenames in os.walk(compare_dir):
    if 'index.html' in filenames:
        filepath = os.path.join(dirpath, 'index.html')
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Check if noindex is already there
        if 'content="noindex' not in html.lower():
            # Inject noindex into head
            noindex_tag = '\n    <meta name="robots" content="noindex, follow">'
            # Let's insert it right after the <head> tag or before </head>
            if '</head>' in html:
                new_html = html.replace('</head>', f'{noindex_tag}\n</head>', 1)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_html)
                modified_files.append(filepath)

print(f"Added noindex to {len(modified_files)} files in /compare/.")

# Now let's remove from sitemap.xml
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()

# Pattern to match <url> blocks containing /compare/
pattern = r'<url>\s*<loc>[^<]*/compare/[^<]*</loc>.*?</url>\s*'
new_sitemap = re.sub(pattern, '', sitemap, flags=re.DOTALL)

if sitemap != new_sitemap:
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(new_sitemap)
    print("Removed /compare/ URLs from sitemap.xml")
else:
    print("No /compare/ URLs found in sitemap.xml (or already removed).")