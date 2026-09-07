import re

with open('top-10-uk-universities-for-international-students/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add UCAS link
html = html.replace(
    'through <strong>UCAS</strong>. You apply to up to five courses',
    'through <strong><a href="https://www.ucas.com/" target="_blank" rel="noopener noreferrer">UCAS</a></strong>. You apply to up to five courses'
)

with open('top-10-uk-universities-for-international-students/index.html', 'w', encoding='utf-8') as f:
    f.write(html)