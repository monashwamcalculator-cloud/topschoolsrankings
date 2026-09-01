import os

def get_dirs(commit):
    import subprocess
    res = subprocess.check_output(['git', 'ls-tree', '-d', '--name-only', commit]).decode('utf-8')
    return set([d.strip() for d in res.split('\n') if d.strip() and d.strip() not in ('.vercel', 'assets', 'author', 'blogs', 'category', 'compare', 'contact-us', 'disclaimer', 'editorial-policy', 'listings', 'media', 'privacy-policy', 'ranking-methodology', 'terms-and-conditions', 'tools', 'utils', 'about-us', 'listing', 'ranking-methodology')])

dirs = get_dirs('HEAD')
print(f'Total article dirs: {len(dirs)}')

with open('blogs/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

missing_from_index = []
for d in dirs:
    if f'/{d}/' not in html:
        missing_from_index.append(d)

print('Dirs not in blogs/index.html:', missing_from_index)
