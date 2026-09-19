import json
import re

# 1. Update blogs/index.html
with open('blogs/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace("The Ultimate Guide", "A Guide")
html = html.replace("the ultimate guide", "a guide")
html = html.replace("The ultimate guide", "A guide")

# 2. Update search-index.json
with open('assets/search-index.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    if "title" in item:
        item["title"] = item["title"].replace("The Ultimate Guide", "A Guide").replace("the ultimate guide", "a guide").replace("The ultimate guide", "A guide")
    if "description" in item:
        item["description"] = item["description"].replace("The Ultimate Guide", "A Guide").replace("the ultimate guide", "a guide").replace("The ultimate guide", "A guide")

with open('blogs/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('assets/search-index.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Cleaned superlatives in blogs index and search index.")