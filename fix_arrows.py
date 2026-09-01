import os

count = 0
for root, dirs, files in os.walk('.'):
    if '.git' in root or '.vercel' in root: continue
    for file in files:
        if file.endswith('.html') or file.endswith('.json') or file.endswith('.js'):
            path = os.path.join(root, file)
            with open(path, 'rb') as f:
                content = f.read()
            
            orig = content
            content = content.replace(b'\xe2\x86\xe2\x80\x99', b'\xe2\x86\x92')
            
            if content != orig:
                with open(path, 'wb') as f:
                    f.write(content)
                count += 1

print(f"Fixed {count} files with corrupted right arrows.")
