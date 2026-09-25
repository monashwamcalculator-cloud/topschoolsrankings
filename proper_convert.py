import os
import re
import mammoth

docx_path = r'C:\Users\Hp\Downloads\Top_100_Finance_Schools_US_Guide.docx'
dst_img = r'media/articles/top-100-finance-schools-us.webp'

# 1. Convert DOCX to HTML using mammoth
with open(docx_path, 'rb') as docx_file:
    result = mammoth.convert_to_html(docx_file)
    raw_html = result.value
    # Print any warnings from mammoth
    for msg in result.messages:
        print(msg)

# 2. Extract boilerplate from a standard article
base_article = r'douglas-college-canada-admissions-fees-courses-university-transfer-guide-for-international-students/index.html'
with open(base_article, 'r', encoding='utf-8') as f:
    base_html = f.read()

new_title = 'Top 100 Finance Schools & Business Universities in the US | 2026 Guide'
new_desc = 'Discover the top 100 finance schools in the US. Compare target universities, Ivy League programs, placement outcomes, and understand Wall Street recruiting.'
new_url = 'https://topschoolsrankings.com/top-100-finance-schools-in-us-guide/'

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

# Fix article body (Inject the perfectly formatted mammoth HTML)
new_html = re.sub(r'<article class="article-body">.*?</article>', f'<article class="article-body">\n{raw_html}\n</article>', new_html, flags=re.DOTALL)

# Write to file
with open('top-100-finance-schools-in-us-guide/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Properly formatted HTML generated and overwritten.")