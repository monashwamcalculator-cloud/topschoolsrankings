import re

with open('top-25-universities-in-canada-for-international-students/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<div class="rich-article-content">'
start_idx = html.find(start_marker)
table_idx = html.find('<table>', start_idx)

if start_idx != -1 and table_idx != -1:
    print(html[start_idx:table_idx])
else:
    print("Could not find markers.")