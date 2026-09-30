import os

# 1. Update blogs/index.html
html_path = "blogs/index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

new_card_html = """<article class="guide-card"><a aria-label="Read Top 100 Universities in Europe Guide" class="guide-card-image" href="/top-100-universities-in-europe/"><img alt="Top 100 Universities in Europe for International Students 2026 Ranking and Tuition Guide" class="" decoding="async" height="844" loading="lazy" src="/images/top-100-universities-in-europe-featured.webp" width="1500"/></a><div class="card-meta"><span>Global Universities</span><span>12 min read</span></div><h3><a href="/top-100-universities-in-europe/">Top 100 Universities in Europe for International Students: 2026 Rankings & Tuition Guide</a></h3><p>A complete comparative guide to the 100 leading European higher education institutions for global candidates. Breakdown of English coursework, non-EU fee structures, and post-study employment avenues.</p><a class="text-link" href="/top-100-universities-in-europe/">Read the guide <span>&rarr;</span></a></article>\n"""

# Insert right before the top-100-finance-schools-us article
target_str = '<article class="guide-card"><a aria-label="Read Top 100 Finance Schools Guide"'
if target_str in html_content and "/top-100-universities-in-europe/" not in html_content:
    html_content = html_content.replace(target_str, new_card_html + target_str)
    
    with open(html_path, "w", encoding="utf-8", newline='\n') as f:
        f.write(html_content)
    print("blogs/index.html updated successfully.")
else:
    print("Could not find the target string in blogs/index.html or card already exists.")

# 2. Update markdown frontmatter
md_path = "content/posts/top-100-universities-in-europe.md"
with open(md_path, "r", encoding="utf-8") as f:
    md_content = f.read()

# Replace category if it's "Universities" -> "Global Universities"
md_content = md_content.replace('category: "Universities"', 'category: "Global Universities"')

with open(md_path, "w", encoding="utf-8", newline='\n') as f:
    f.write(md_content)
print("Markdown file frontmatter updated successfully.")
