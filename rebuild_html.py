import re
import os
import markdown

# 1. Read the clean Markdown file
md_path = "content/posts/top-100-universities-in-europe.md"
with open(md_path, 'r', encoding='utf-8') as f:
    md_content = f.read()

parts = md_content.split('---', 2)
if len(parts) >= 3:
    body = parts[2].strip()
else:
    body = md_content

html_body = markdown.markdown(body, extensions=['tables'])

# Read original template from finance schools
template_path = "top-100-finance-schools-us/index.html"
with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()

# Meta and Head swaps
template = re.sub(r'<title>.*?</title>', r'<title>Top 100 Universities in Europe for International Students: 2026 Rankings & Tuition Guide | Top Schools Rankings</title>', template)
template = re.sub(r'<meta name="description" content=".*?">', r'<meta name="description" content="A complete comparative guide to the 100 leading European higher education institutions for global candidates. Breakdown of English coursework, non-EU fee structures, and post-study employment avenues.">', template)
template = re.sub(r'href="https://topschoolsrankings\.com/top-100-finance-schools-us/"', r'href="https://topschoolsrankings.com/top-100-universities-in-europe/"', template)
template = re.sub(r'content="https://topschoolsrankings\.com/top-100-finance-schools-us/"', r'content="https://topschoolsrankings.com/top-100-universities-in-europe/"', template)
template = re.sub(r'<meta property="og:title" content=".*?">', r'<meta property="og:title" content="Top 100 Universities in Europe for International Students: 2026 Rankings & Tuition Guide">', template)
template = re.sub(r'<meta property="og:description" content=".*?">', r'<meta property="og:description" content="A complete comparative guide to the 100 leading European higher education institutions for global candidates. Breakdown of English coursework, non-EU fee structures, and post-study employment avenues.">', template)
template = re.sub(r'content="https://topschoolsrankings\.com/media/articles/top-100-finance-schools-us-featured\.jpg"', r'content="https://topschoolsrankings.com/images/top-100-universities-in-europe-featured.webp"', template)
template = re.sub(r'(<header class="page-header">.*?<h1>)(.*?)(</h1>)', r'\1Top 100 Universities in Europe for International Students: 2026 Rankings, English-Taught Degrees & Tuition Guide\3', template, flags=re.DOTALL)
template = re.sub(r'<div class="page-meta">Last reviewed .*?</div>', r'<div class="page-meta">Published August 2026 &middot; Reviewed by the TSR Editorial Desk</div>', template)
template = re.sub(r'src="/media/articles/top-100-finance-schools-us-featured\.jpg"', r'src="/images/top-100-universities-in-europe-featured.webp"', template)
template = re.sub(r'alt="Top 100 Finance Schools in the United States Ranking and Wall Street Placement Guide"', r'alt="Top 100 Universities in Europe for International Students 2026 Ranking and Tuition Guide"', template)
template = re.sub(r'<figcaption>.*?</figcaption>', r'<figcaption>Top 100 Universities in Europe for International Students 2026 Ranking and Tuition Guide.</figcaption>', template)

# In the template, we replace ONLY the contents inside <div class="rich-article-content">
# The template has: <div class="rich-article-content">...</div>
# Followed by <div class="author-bio-box">...</div> and <section class="related-guides">...
# Let's extract the exact bounds of rich-article-content. 
# We'll use a regex that matches `<div class="rich-article-content">` up to the FIRST `</div>\n</div>\n\n<section class="related-guides">` or similar... Wait. 
# In top-100-finance-schools-us, what is immediately after the rich-article-content?

# Let's just do a string split.
before, after = template.split('<div class="rich-article-content">', 1)
# The end of rich article content is just before:
#   </div>
# </div>
# <section class="related-guides">  OR  <div class="author-bio-box">
# Let's split `after` by `<div class="author-bio-box"`
if '<div class="author-bio-box"' in after:
    _, end_part = after.split('<div class="author-bio-box"', 1)
    new_html = before + '<div class="rich-article-content">\n' + html_body + '\n</div>\n\n<div class="author-bio-box"' + end_part
else:
    print("Could not find author-bio-box in template")
    sys.exit(1)

out_dir = "top-100-universities-in-europe"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "index.html"), 'w', encoding='utf-8', newline='\n') as f:
    f.write(new_html)

print("HTML rebuilt correctly.")
