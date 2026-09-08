import os

target_string = '<div style="margin-top:20px;"><a href="https://useneedle.net/directory/topschoolsrankings" target="_blank" rel="noopener noreferrer"><img src="https://useneedle.net/badges/needle-directory.svg" alt="Listed on Needle Directory" height="44" /></a></div>'

modified_count = 0
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            try:
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                if target_string in content:
                    new_content = content.replace(target_string, '')
                    with open(filepath, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    modified_count += 1
            except Exception as e:
                pass

print(f"Removed Needle Directory button from {modified_count} HTML files.")