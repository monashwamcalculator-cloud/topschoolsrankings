import os
for r, d, files in os.walk('.'):
    if '.git' in r: continue
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(r, f)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
            if 'Supporting visual context' in content:
                print(f"Found image caption in {filepath}")
                start = content.find('Supporting visual context')
                print(content[start-50:start+150])
                break