import os
import re

replacements = {
    "Hard Strategy to Get Admitted": "Admissions Guide",
    "Cracking the Bodwell Admission Code": "Bodwell High School Admissions Guide",
    "interview secrets": "interview guide",
    "exact strategy": "preparation guide",
    "best private boys' school in Toronto": "independent boys' school in Toronto",
    "best private boys' school": "independent boys' school"
}

count = 0
for root, dirs, files in os.walk('.'):
    if '.git' in root or '.vercel' in root or 'node_modules' in root: continue
    for file in files:
        if file.endswith('.html') or file.endswith('.json'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            orig = content
            for bad, good in replacements.items():
                content = re.sub(re.escape(bad), good, content, flags=re.IGNORECASE)
            
            if content != orig:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
print(f"Fixed {count} files for promotional wording.")