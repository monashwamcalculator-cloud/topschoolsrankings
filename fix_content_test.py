import re

with open('yale-university-complete-guide/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# I need to get the figure back first.
# Oh, it's currently at: <h2><figure...> \n <h2>1.2
html = html.replace('<h2><figure class="editorial-figure">', '<figure class="editorial-figure">')
# Actually let's just reset the file from git
