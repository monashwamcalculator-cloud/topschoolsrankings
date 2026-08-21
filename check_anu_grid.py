import re
with open('listings/index.html', 'r', encoding='utf-8') as f:
    text = f.read()
    m = re.search(r'<article class="listing-card">.*?Australian National University.*?</article>', text, re.DOTALL)
    if m:
        print(m.group(0))
    m2 = re.search(r'<article class="listing-card">.*?Boston University.*?</article>', text, re.DOTALL)
    if m2:
        print(m2.group(0))
