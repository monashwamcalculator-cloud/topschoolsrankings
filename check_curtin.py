import re
with open('listing/curtin-university/index.html', 'r', encoding='utf-8') as f:
    text = f.read()
    m = re.search(r'<div class="listing-profile-identity">.*?<span class="eyebrow">', text, re.DOTALL)
    if m:
        print(m.group(0))
