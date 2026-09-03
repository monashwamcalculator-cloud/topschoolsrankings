import os

ga4_code = '''<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-YPHSD05VY0"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-YPHSD05VY0');
</script>
</head>'''

html_files = []
for root, dirs, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root or '.vercel' in root or 'venv' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            html = f.read()
        
        if 'G-YPHSD05VY0' not in html:
            html = html.replace('</head>', ga4_code)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(html)
    except Exception as e:
        print(f"Skipping {file}: {e}")

print('GA4 tracking code injected into all HTML files.')