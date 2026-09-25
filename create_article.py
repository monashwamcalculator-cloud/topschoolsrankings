import os
import shutil
import re

# 1. Copy image
src_img = r'C:/Users/Hp/.gemini/antigravity/brain/726bddf1-4614-4b0e-a924-9a6f84cfa50e/.user_uploaded/media_1790315498848.webp'
dst_img = r'media/articles/top-100-finance-schools-us.webp'
if os.path.exists(src_img):
    shutil.copy(src_img, dst_img)

# 2. Extract boilerplate from a standard article
base_article = r'douglas-college-canada-admissions-fees-courses-university-transfer-guide-for-international-students/index.html'
with open(base_article, 'r', encoding='utf-8') as f:
    base_html = f.read()

# Get head up to <title>
head_start = base_html.split('<title>')[0]

# Build new head
new_title = 'Top 100 Finance Schools & Business Universities in the US | 2026 Guide'
new_desc = 'Discover the top 100 finance schools in the US. Compare target universities, Ivy League programs, placement outcomes, and understand Wall Street recruiting.'
new_url = 'https://topschoolsrankings.com/top-100-finance-schools-in-us-guide/'

# 3. Read content and convert to HTML
with open('temp_content.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Basic conversion of text to HTML
paragraphs = text.split('\n\n')
article_html = []
for p in paragraphs:
    p = p.strip()
    if not p:
        continue
    if p.startswith('Q:'):
        article_html.append(f"<h3>{p}</h3>")
    elif p.startswith('A:'):
        article_html.append(f"<p>{p}</p>")
    elif p[0].isdigit() and (p[1:3] == '. ' or p[2:4] == '. '):
        article_html.append(f"<h2>{p}</h2>")
    elif p == p.upper() and len(p) < 100:
        article_html.append(f"<h2>{p}</h2>")
    else:
        # Check if it looks like a list item or just paragraph
        article_html.append(f"<p>{p}</p>")

article_content = '\n'.join(article_html)

# We need to construct the full page layout
# Just replace the title, meta tags, and the <article> content from the base_html

def replace_between(content, start_tag, end_tag, replacement):
    pattern = re.compile(f'({re.escape(start_tag)}).*?({re.escape(end_tag)})', re.DOTALL)
    return pattern.sub(rf'\1{replacement}\2', content)

new_html = base_html
new_html = replace_between(new_html, '<title>', '</title>', new_title)
new_html = replace_between(new_html, '<meta name="description" content="', '">', new_desc)
new_html = replace_between(new_html, '<link rel="canonical" href="', '">', new_url)
new_html = replace_between(new_html, '<meta property="og:title" content="', '">', new_title)
new_html = replace_between(new_html, '<meta property="og:description" content="', '">', new_desc)
new_html = replace_between(new_html, '<meta property="og:url" content="', '">', new_url)

# Fix image meta tags
new_html = re.sub(r'<meta property="og:image" content=".*?">', f'<meta property="og:image" content="https://topschoolsrankings.com/{dst_img}">', new_html)
new_html = re.sub(r'<meta name="twitter:image" content=".*?">', f'<meta name="twitter:image" content="https://topschoolsrankings.com/{dst_img}">', new_html)

# Fix breadcrumbs
new_html = re.sub(r'<nav class="breadcrumbs.*?</nav>', f'<nav class="breadcrumbs site-container" aria-label="Breadcrumb"><a href="/">Home</a><span><i aria-hidden="true">/</i><a href="/blogs/">Guides</a></span><span><i aria-hidden="true">/</i><b>Top 100 Finance Schools US</b></span></nav>', new_html, flags=re.DOTALL)

# Fix page header
new_html = re.sub(r'<header class="page-header">.*?</header>', f'<header class="page-header"><div class="site-container narrow"><span class="eyebrow">Finance Schools Guide</span><h1>Top 100 Finance Schools in the US (2026 Guide)</h1><p>{new_desc}</p><div class="page-meta"><span class="author-label">By Saahil Biswas</span> <span>&middot;</span> Updated 25 Sep 2026</div></div></header>', new_html, flags=re.DOTALL)

# Fix featured image
new_html = re.sub(r'<div class="featured-image site-container narrow">.*?</div>', f'<div class="featured-image site-container narrow"><img src="/{dst_img}" alt="Top 100 Finance Schools in the US" width="1200" height="630"></div>', new_html, flags=re.DOTALL)

# Fix article body
new_html = re.sub(r'<article class="article-body">.*?</article>', f'<article class="article-body">{article_content}</article>', new_html, flags=re.DOTALL)

# Make directory and save
os.makedirs('top-100-finance-schools-in-us-guide', exist_ok=True)
with open('top-100-finance-schools-in-us-guide/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Generated top-100-finance-schools-in-us-guide/index.html")