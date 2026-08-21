import re
with open('listings/index.html', 'r', encoding='utf-8') as f:
    text = f.read()
    m = re.search(r'<article class="listing-card">.*?Australian National University.*?</article>', text, re.DOTALL)
    if m:
        print(m.group(0))
