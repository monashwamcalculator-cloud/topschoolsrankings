with open('ranking-methodology/index.html', 'r', encoding='utf-8') as f:
    html = f.read()
if '<footer class="site-footer">' in html:
    footer_idx = html.find('<footer class="site-footer">')
    print("FOOTER:")
    print(html[footer_idx:footer_idx+500])