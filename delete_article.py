import os
import shutil
import re

# 1. Delete the directory
dir_path = 'top-100-finance-schools-in-us-guide'
if os.path.exists(dir_path):
    shutil.rmtree(dir_path)
    print(f"Deleted {dir_path}")

# 2. Delete the image
img_path = 'media/articles/top-100-finance-schools-us.webp'
if os.path.exists(img_path):
    os.remove(img_path)
    print(f"Deleted {img_path}")

# 3. Remove from blogs/index.html
blogs_path = 'blogs/index.html'
if os.path.exists(blogs_path):
    with open(blogs_path, 'r', encoding='utf-8') as f:
        blogs_html = f.read()
    
    # Regex to remove the specific article card
    pattern = re.compile(r'<article class="guide-card">.*?href="/top-100-finance-schools-in-us-guide/".*?</article>', re.DOTALL)
    blogs_html = pattern.sub('', blogs_html)
    
    with open(blogs_path, 'w', encoding='utf-8') as f:
        f.write(blogs_html)
    print(f"Removed from {blogs_path}")

# 4. Remove from sitemap.xml
sitemap_path = 'sitemap.xml'
if os.path.exists(sitemap_path):
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        sitemap = f.read()
    
    # Regex to remove the specific url block
    pattern = re.compile(r'<url>\s*<loc>https://topschoolsrankings\.com/top-100-finance-schools-in-us-guide/</loc>.*?</url>', re.DOTALL)
    sitemap = pattern.sub('', sitemap)
    
    # Also clean up multiple blank lines if any
    sitemap = re.sub(r'\n\s*\n', '\n', sitemap)
    
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print(f"Removed from {sitemap_path}")