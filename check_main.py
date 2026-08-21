import re
import sys
with open('listing/appleby-college/index.html', 'r', encoding='utf-8') as f:
    text = f.read()
    m = re.search(r'<main>.*?</main>', text, re.DOTALL)
    if m:
        # Just print the first 1000 characters
        sys.stdout.buffer.write(m.group(0)[:2000].encode('utf-8'))
