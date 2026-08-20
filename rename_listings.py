import os

target1 = '<a href="/listings/">Institutions</a>'
replacement1 = '<a href="/listings/">Listings</a>'

target2 = '<a href="/listings/">Institution profiles</a>'
replacement2 = '<a href="/listings/">Listings</a>'

count = 0
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            modified = False
            if target1 in content:
                content = content.replace(target1, replacement1)
                modified = True
            if target2 in content:
                content = content.replace(target2, replacement2)
                modified = True
                
            if modified:
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(content)
                count += 1
print(f'Replaced in {count} files')
