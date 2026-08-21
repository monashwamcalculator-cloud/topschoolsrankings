import re
import sys
with open('listings/index.html', 'r', encoding='utf-8') as f:
    text = f.read()
    m = re.search(r'<article class="listing-card">.*?Australian National University.*?</article>', text, re.DOTALL)
    if m:
        sys.stdout.buffer.write(m.group(0).encode('utf-8'))
