import os
for r, d, files in os.walk('.'):
    if '.git' in r: continue
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(r, f)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
            if 'Accuracy note:' in content:
                print(f"Found in {filepath}")
                start = content.find('Accuracy note:')
                print(content[start-50:start+150])
                break