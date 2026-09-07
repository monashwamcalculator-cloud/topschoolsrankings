import re

with open('top-50-universities-in-usa/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<div class="rich-article-content">'
end_marker = '</div>\n<div class="author-bio-box"'
start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    content = html[start_idx:end_idx]
    with open('top50_old_content.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Extracted to top50_old_content.html")
else:
    print("Could not find markers.")