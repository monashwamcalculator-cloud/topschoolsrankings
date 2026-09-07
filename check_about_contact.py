import os
for root, dirs, files in os.walk('.'):
    for dir in dirs:
        if 'about' in dir.lower() or 'contact' in dir.lower():
            print(f"Found dir: {os.path.join(root, dir)}")