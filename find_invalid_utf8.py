import os

for root, dirs, files in os.walk('.'):
    if '.git' in root or '.vercel' in root: continue
    for file in files:
        if file.endswith('.html') or file.endswith('.json') or file.endswith('.js'):
            path = os.path.join(root, file)
            with open(path, 'rb') as f:
                b = f.read()
            
            try:
                b.decode('utf-8')
            except UnicodeDecodeError as e:
                start = max(0, e.start - 10)
                end = min(len(b), e.end + 10)
                print(f"File: {path}")
                print(f"Error at {e.start}: {b[start:end]}")
                print(f"Bad bytes hex: {[hex(x) for x in b[e.start:e.end]]}")
