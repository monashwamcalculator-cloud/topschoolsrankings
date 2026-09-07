import os
import re

found = False
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html') or f.endswith('.json') or f.endswith('.xml') or f.endswith('.js'):
            filepath = os.path.join(root, f)
            try:
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                    if 'debug_vercel.html' in content:
                        print(f"Reference found in: {filepath}")
                        found = True
            except:
                pass
if not found:
    print("No references to debug_vercel.html found.")