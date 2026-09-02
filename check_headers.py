for p in ['about-us', 'contact-us', 'privacy-policy', 'terms-and-conditions', 'disclaimer', 'editorial-policy', 'write-for-us', 'ranking-methodology']:
    with open(p + '/index.html', 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    if '<div class="evidence-bar">' not in html:
        print(f'{p} is MISSING the evidence bar!')
    if 'logo.png' not in html:
        print(f'{p} is MISSING the new logo!')