import re

with open('top-10-uk-universities-for-international-students/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<div class="rich-article-content">'
end_marker = '</div>\n<div class="author-bio-box"'
end_marker_fallback = '</div>\n  <div class="author-bio-box"'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)
if end_idx == -1:
    end_idx = html.find(end_marker_fallback)

if start_idx != -1 and end_idx != -1:
    print(html[start_idx:end_idx])
else:
    print("Could not find markers.")