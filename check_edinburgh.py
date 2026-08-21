import re
import sys
with open('listing/university-of-edinburgh/index.html', 'r', encoding='utf-8') as f:
    text = f.read()
    m = re.search(r'<div class="listing-profile-identity">.*?<span class="eyebrow">', text, re.DOTALL)
    if m:
        sys.stdout.buffer.write(m.group(0).encode('utf-8'))
