import os
import re
import urllib.request
import urllib.error

missing = []
for root, dirs, files in os.walk('listing'):
    if 'index.html' in files:
        filepath = os.path.join(root, 'index.html')
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            m = re.search(r'<img[^>]*src="([^"]+)"[^>]*alt="([^"]*logo)"[^>]*>', html, re.IGNORECASE)
            
            # The logo in listing pages might be styled differently, let's search for an img that is not the hero image.
            # Usually it's right under <header> or next to <h1>
            m2 = re.search(r'<h1>.*?</h1>.*?<img[^>]*src="([^"]+)"', html, re.DOTALL)
            m3 = re.search(r'<img[^>]*class="[^"]*logo[^"]*"[^>]*src="([^"]+)"', html)
            m4 = re.search(r'<img[^>]*src="([^"]+)"[^>]*class="[^"]*logo[^"]*"', html)
            
            logo_src = None
            if m3: logo_src = m3.group(1)
            elif m4: logo_src = m4.group(1)
            elif m: logo_src = m.group(1)
            
            if logo_src:
                if logo_src.startswith('/'):
                    local_path = '.' + logo_src
                else:
                    local_path = os.path.join(root, logo_src)
                    
                if not os.path.exists(local_path):
                    name_m = re.search(r'<h1>(.*?)</h1>', html)
                    name = name_m.group(1) if name_m else root
                    missing.append((name, logo_src, root))
            else:
                name_m = re.search(r'<h1>(.*?)</h1>', html)
                name = name_m.group(1) if name_m else root
                missing.append((name, 'No logo tag found', root))

print('Total missing or no tag:', len(missing))
for m in missing[:30]:
    print(m)
