import os
import json
import re

file_path = 'ranking-methodology/index.html'

# UTF-8 check
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    print("UTF-8 Check: PASS")
except Exception as e:
    print("UTF-8 Check: FAIL -", e)

# JSON-LD check
jsonld_match = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
if jsonld_match:
    try:
        json.loads(jsonld_match.group(1))
        print("JSON-LD Check: PASS")
    except Exception as e:
        print("JSON-LD Check: FAIL -", e)
else:
    print("JSON-LD Check: FAIL - Not found")

# Internal Links check
links = re.findall(r'href="(/(?:[^"]+)?)"', html)
all_links_valid = True
for link in set(links):
    if link == '/': continue
    local_path = "." + link
    if not os.path.exists(local_path) and not os.path.exists(os.path.join(local_path, 'index.html')):
        # Let's check without trailing slash or specific cases
        path_to_check = local_path + 'index.html' if local_path.endswith('/') else local_path
        if not os.path.exists(path_to_check):
            print(f"Internal Link Check: FAIL - {link} does not exist locally.")
            all_links_valid = False
            
if all_links_valid:
    print("Internal Links Check: PASS")

