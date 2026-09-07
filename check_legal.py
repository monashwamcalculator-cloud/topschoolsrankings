import os
import re

files = [
    'privacy-policy/index.html',
    'terms-and-conditions/index.html',
    'ranking-methodology/index.html'
]

for f in files:
    print(f"--- {f} ---")
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            words = len(re.findall(r'\w+', content))
            print(f"Found. Words: {words}")
            if words < 200:
                print("WARNING: Thin content.")
    else:
        print("NOT FOUND.")