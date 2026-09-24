import os

files_to_fix = [
    'faq/index.html',
    'about-us/index.html',
    'disclaimer/index.html',
    'terms-and-conditions/index.html',
    'editorial-policy/index.html'
]

replacements = {
    'school listings, editorial guides': 'school guides, editorial guides',
    'view listings?': 'view guides?',
    'add my school or university to the directory?': 'suggest a topic or school for review?',
    'Our directories and listings are curated': 'Our guides and rankings are curated',
    'Rankings and listings are not sold.': 'Rankings and guides are not sold.',
    'directory': 'publication',
    'Directory': 'Publication',
    'listings': 'guides',
    'Listings': 'Guides',
    'tool ': 'guide '
}

for filepath in files_to_fix:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        for old, new in replacements.items():
            html = html.replace(old, new)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Fixed terms in {filepath}")