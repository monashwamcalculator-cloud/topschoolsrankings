import os
import re

images = set()
for root, dirs, files in os.walk('.'):
    if '.git' in root or '.vercel' in root: continue
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                matches = re.findall(r'<img[^>]+src="([^"]+)"', content)
                for m in matches:
                    if m.startswith('/'):
                        images.add(m.strip('/'))

broken = []
for img in images:
    if not os.path.exists(img):
        broken.append(img)
if broken:
    print('Broken images:', len(broken))
else:
    print('All images exist locally.')
