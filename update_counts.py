import os

path = 'index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<strong>92</strong><span>research guides</span>', '<strong>104</strong><span>research guides</span>')
html = html.replace('<strong>34</strong><span>free planning tools</span>', '<strong>46</strong><span>free planning tools</span>')
html = html.replace('<strong>110</strong><span>retained profiles</span>', '<strong>135</strong><span>retained profiles</span>')

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)