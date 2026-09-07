import re
with open('write-for-us/index.html', 'r', encoding='utf-8') as f:
    content = f.read()
links = re.findall(r'href="([^"]+)"', content)
for l in links:
    if l in ['/editorial-policy/', '/ranking-methodology/', '/contact-us/']:
        print(f"Found link: {l}")