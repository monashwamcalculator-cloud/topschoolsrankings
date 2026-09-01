import os
for root, dirs, files in os.walk('.'):
    if '.git' in root or '.vercel' in root or 'node_modules' in root: continue
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'rb') as f:
                content = f.read()
            if not content.startswith(b'\xef\xbb\xbf'):
                with open(path, 'wb') as f:
                    f.write(b'\xef\xbb\xbf' + content)