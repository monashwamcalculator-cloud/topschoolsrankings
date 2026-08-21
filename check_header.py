import re
import sys
with open('listing/appleby-college/index.html', 'r', encoding='utf-8') as f:
    text = f.read()
    m = re.search(r'<header[^>]*>.*?</header>', text, re.DOTALL)
    if m:
        sys.stdout.buffer.write(m.group(0).encode('utf-8'))
