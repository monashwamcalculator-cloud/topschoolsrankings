import os
import shutil
import re

old_folder = 'top-100-universities-in-russia'

# 1. Remove the folder
if os.path.exists(old_folder):
    shutil.rmtree(old_folder)

# 2. Revert the blogs/index.html
with open('blogs/index.html', 'r', encoding='utf-8') as f:
    blogs_content = f.read()

blogs_content = re.sub(r'<article class="listing-card">\s*<div class="card-image-wrap">.*?<a href="/top-100-universities-in-russia/".*?</article>', '', blogs_content, flags=re.DOTALL)

with open('blogs/index.html', 'w', encoding='utf-8') as f:
    f.write(blogs_content)

# 3. Revert sitemap.xml
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()

sitemap = re.sub(r'<url>\s*<loc>https://topschoolsrankings\.com/top-100-universities-in-russia/</loc>.*?</url>', '', sitemap, flags=re.DOTALL)

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap)

print("Russia article removed successfully!")
