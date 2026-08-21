import glob
import re

for filepath in glob.glob('listing/**/*.html', recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if '</div><figure class="listing-campus-image">' in html:
        print(f"Found in {filepath}")
        idx = html.find('</div><figure class="listing-campus-image">')
        print(html[idx-100:idx+150])
        break
