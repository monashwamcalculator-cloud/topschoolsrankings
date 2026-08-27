import os
import re
import shutil

workspace = r'c:\Users\Hp\Downloads\topschoolsrankings-new-site-upload-v2'

# 1. Update blogs/index.html
blogs_path = os.path.join(workspace, 'blogs', 'index.html')
with open(blogs_path, 'r', encoding='utf-8') as f:
    blogs_html = f.read()

# Decrement count
blogs_html = re.sub(r'(\d+)\s+editorial guides', lambda m: str(int(m.group(1)) - 1) + ' editorial guides', blogs_html)

# Remove the specific guide-card using regex (no quotes issue here)
pattern = r'<article class="guide-card">\s*<img[^>]*src="/media/new-guides/smart-hostel-india\.webp".*?</article>\s*'
blogs_html = re.sub(pattern, '', blogs_html, flags=re.DOTALL)

with open(blogs_path, 'w', encoding='utf-8') as f:
    f.write(blogs_html)

# 2. Delete files and folders
article_dir = os.path.join(workspace, 'how-smart-hostels-are-changing-student-life-at-indian-universities')
if os.path.exists(article_dir):
    shutil.rmtree(article_dir)

featured_img = os.path.join(workspace, 'media', 'new-guides', 'smart-hostel-india.webp')
if os.path.exists(featured_img):
    os.remove(featured_img)

for i in range(1, 4):
    inline_img = os.path.join(workspace, 'media', 'new-guides', f'smart-hostels-india-inline-{i}.webp')
    if os.path.exists(inline_img):
        os.remove(inline_img)

author_img = os.path.join(workspace, 'media', 'authors', 'dr-satya-vir-singh.webp')
if os.path.exists(author_img):
    os.remove(author_img)
    
print('Deletion cleanup complete!')
