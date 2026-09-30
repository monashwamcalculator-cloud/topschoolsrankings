import os

md_path = "content/posts/top-100-universities-in-europe.md"
with open(md_path, "r", encoding="utf-8") as f:
    md_content = f.read()

md_content = md_content.replace('category: "Universities"', 'category: "Rankings & Guides"')
md_content = md_content.replace('date: "2026-08-25"', 'date: "2026-09-30"')

with open(md_path, "w", encoding="utf-8", newline='\n') as f:
    f.write(md_content)
print("Markdown file frontmatter updated safely.")
