with open('blogs/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('103 editorial guides', '104 editorial guides')

with open('blogs/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Successfully updated article count on blogs page.')