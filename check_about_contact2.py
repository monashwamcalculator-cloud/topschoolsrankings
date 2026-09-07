import os
import re

files = [
    'about-us/index.html',
    'contact-us/index.html',
]

for f in files:
    print(f"--- {f} ---")
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            words = len(re.findall(r'\w+', content))
            print(f"Found. Words: {words}")
            if words < 150:
                print("WARNING: Thin content.")
    else:
        print("NOT FOUND.")