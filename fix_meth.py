import re

with open('about-us/index.html', 'r', encoding='utf-8') as f:
    about = f.read()

with open('ranking-methodology/index.html', 'r', encoding='utf-8') as f:
    meth = f.read()

# Extract header from about-us
# Usually it starts from <div class="evidence-bar"> or <header class="site-header"> and ends at </header>
header_match = re.search(r'(<div class="evidence-bar">.*?</header>)', about, re.DOTALL)
about_header = header_match.group(1) if header_match else None

# Extract footer from about-us
footer_match = re.search(r'(<footer class="site-footer">.*?</footer>)', about, re.DOTALL)
about_footer = footer_match.group(1) if footer_match else None

# Extract old header from meth
meth_header_match = re.search(r'(<header class="site-header">.*?</header>)', meth, re.DOTALL)
meth_header = meth_header_match.group(1) if meth_header_match else None

# Extract old footer from meth
meth_footer_match = re.search(r'(<footer class="site-footer">.*?</footer>)', meth, re.DOTALL)
meth_footer = meth_footer_match.group(1) if meth_footer_match else None

if about_header and meth_header:
    meth = meth.replace(meth_header, about_header)
if about_footer and meth_footer:
    meth = meth.replace(meth_footer, about_footer)

with open('ranking-methodology/index.html', 'w', encoding='utf-8') as f:
    f.write(meth)

print("Header and Footer replaced.")