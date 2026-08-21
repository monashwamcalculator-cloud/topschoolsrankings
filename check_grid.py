import re
with open('listings/index.html', 'r', encoding='utf-8') as f:
    text = f.read()
    m = re.findall(r'<article class="listing-card">.*?</article>', text, re.DOTALL)
    for art in m[:3]:
        print(art)
        print("-----")
