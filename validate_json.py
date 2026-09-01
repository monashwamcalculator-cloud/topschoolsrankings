import json
import re

with open('ranking-methodology/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

jsonld_match = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
if jsonld_match:
    jsonld_str = jsonld_match.group(1)
    try:
        json.loads(jsonld_str)
        print('JSON-LD is valid.')
    except Exception as e:
        print('JSON-LD Error:', e)
else:
    print('JSON-LD not found.')
