import os

for root, dirs, files in os.walk('author'):
    for file in files:
        if file.endswith('.html'):
            with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                content = f.read()
                if 'View all blog articles' in content:
                    print(f'Found in {os.path.join(root, file)}')