import re

with open(r'how-it-works\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('independent school listings', 'independent school guides')
content = content.replace('comprehensive directories', 'comprehensive resources')
content = content.replace('browse our directory', 'browse our guides')
content = content.replace('Browse school & university listings', 'Browse school & university guides')
content = content.replace('How We Rank and List Schools', 'How We Review Schools')
content = content.replace('Our listings and rankings', 'Our guides and rankings')
content = content.replace('List Your School or University', 'Submit Your School or University')
content = content.replace('included in our directory', 'included in our coverage')
content = content.replace('request a listing', 'request coverage')

with open(r'how-it-works\index.html', 'w', encoding='utf-8') as f:
    f.write(content)