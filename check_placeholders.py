import os
import re

for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
                if '[email' in content.lower() or '[your' in content.lower() or '123-456' in content:
                    print(f"Possible placeholder in: {filepath}")