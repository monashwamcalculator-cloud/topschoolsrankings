import os

replacements = [
    ("Hard Strategy to Get Admitted", "Bodwell High School Admissions Guide"),
    ("Hidden Academic Filter", "Academic Requirements"),
    ("To bypass the standard filters, follow this precise three-step application strategy", "Applicants can use the following steps to prepare their application"),
    ("To bypass the standard filters and get a firm letter of acceptance, follow this precise three-step application strategy", "Applicants can use the following steps to prepare their application"),
    ("exact strategy", "application approach"),
    ("acceptance secrets", "admissions information"),
    ("interview secrets", "admissions information"),
    ("one of the premier undergraduate entry processes globally", "a highly selective undergraduate admissions process")
]

count = 0
for root, dirs, files in os.walk('.'):
    if '.git' in root or '.vercel' in root: continue
    for file in files:
        if file.endswith('.html') or file.endswith('.json') or file.endswith('.js'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            orig = content
            # Apply targeted replacements
            if 'bodwell' in path.lower() or 'oxford' in path.lower() or 'index.html' in path.lower():
                # wait, these strings might be in index pages. Let's just apply to all files.
                for old, new in replacements:
                    content = content.replace(old, new)
            
            if content != orig:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1

print(f"Fixed {count} files with specific promotional phrases.")
