import glob

tag = '<meta name="yandex-verification" content="e3b79ee5ab31d1de" />'
count = 0

for f in glob.glob('**/*.html', recursive=True):
    if 'node_modules' in f: continue
    
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        if tag not in content and '</head>' in content:
            new_content = content.replace('</head>', f'  {tag}\n</head>')
            with open(f, 'w', encoding='utf-8', newline='\n') as file:
                file.write(new_content)
            count += 1
    except Exception as e:
        pass

print(f"Added Yandex verification tag to {count} files.")
