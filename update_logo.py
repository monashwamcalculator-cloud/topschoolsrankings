import os

favicon_target = '<link rel="icon" href="/favicon.svg">'
favicon_replacement = '<link rel="icon" href="/favicon.jpg">'

logo_target = """<a class="brand" href="/" aria-label="Top Schools Rankings home">
    <span class="brand-mark" aria-hidden="true"><i></i><i></i><i></i></span>
    <span class="brand-copy"><strong>Top Schools</strong><small>RANKINGS</small></span>
  </a>"""

logo_replacement = """<a class="brand" href="/" aria-label="Top Schools Rankings home" style="display:flex; align-items:center;">
    <img src="/assets/logo.png" alt="Top Schools Rankings" style="height:45px; width:auto; max-width:100%;">
  </a>"""

count = 0
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            modified = False
            if favicon_target in content:
                content = content.replace(favicon_target, favicon_replacement)
                modified = True
                
            if logo_target in content:
                content = content.replace(logo_target, logo_replacement)
                modified = True
                
            if modified:
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(content)
                count += 1

print(f'Replaced in {count} files')
