import os

replacements = [
    (b'\xe2\x80\xe2\x80\x9c', b'\xe2\x80\x93'), # en dash
    (b'\xe2\x80\xe2\x80\xe2\x80\xe2\x80\x9d', b'\xe2\x80\x94'), # em dash
    (b'\xe2\x80\xe2\x80\xe2\x80\x9d', b'\xe2\x80\x9d'), # right double quote
]

count = 0
for root, dirs, files in os.walk('.'):
    if '.git' in root or '.vercel' in root: continue
    for file in files:
        if file.endswith('.html') or file.endswith('.js') or file.endswith('.json'):
            path = os.path.join(root, file)
            with open(path, 'rb') as f:
                content = f.read()
            
            orig = content
            for old, new in replacements:
                content = content.replace(old, new)
            
            if content != orig:
                with open(path, 'wb') as f:
                    f.write(content)
                count += 1

print(f"Fixed {count} files with corrupted UTF-8 sequences.")
