import glob, re
with open('missing.txt', 'w', encoding='utf-8') as out:
    for filepath in glob.glob('tools/**/*.html', recursive=True):
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        if '<h2>Related tools</h2>' in html:
            parts = html.split('<h2>Related tools</h2>')
            if len(parts) == 2:
                subparts = parts[1].split('<h2>', 1)
                related_section = subparts[0]
                matches = re.findall(r'<h3>([^<]+)</h3>', related_section)
                for m in matches:
                    out.write(f'MISSING LINK IN {filepath}: {m}\n')
