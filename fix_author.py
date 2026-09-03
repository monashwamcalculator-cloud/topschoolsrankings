import os

file_path = 'author/samrat-biswas/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<span class="eyebrow">Guest Contributor</span>', '<span class="eyebrow">Author</span>')
content = content.replace('<span>Guest Post</span>', '<span>Education Technology</span>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated author page.')