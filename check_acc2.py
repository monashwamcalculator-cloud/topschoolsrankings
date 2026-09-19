import os
for r, d, files in os.walk('.'):
    if '.git' in r: continue
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(r, f)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
            start = content.find('<div class="editor-note"><strong>Accuracy note:</strong>')
            if start != -1:
                end = content.find('</div>', start)
                print(content[start:end+6])
                break