import os

found_files = []
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            try:
                with open(filepath, 'r', encoding='utf-8') as file:
                    if 'useneedle.net' in file.read():
                        found_files.append(filepath)
            except:
                pass

print(f"Found in {len(found_files)} HTML files.")
if len(found_files) > 0:
    print(f"Example: {found_files[0]}")