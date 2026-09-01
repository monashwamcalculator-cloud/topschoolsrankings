import os
import re

MOJIBAKE_MAP = {
    'Ã¢â‚¬â„¢': "'",
    'Ã¢â‚¬Â ': '”',
    'Ã¢â‚¬Å“': '“',
    'Ã¢â‚¬â€œ': '–',
    'Ã¢â‚¬â€ ': '—',
    'Ã¢â‚¬Â¦': '…',
    'Ã‚Â£': '£',
    'Ã‚Â': '',
    'Ã¢â€žÂ¢': '™',
    'Ã‚Â©': '©',
    'Ã¢â‚¬Ëœ': '‘',
    'â€™': "'",
    'â€œ': '“',
    'â€': '”',
    'â€“': '–',
    'â€”': '—',
    'Â': ''
}

CALTECH_PHRASES = [
    ("strictly test-blind", "test-free"),
    ("even a 1600 won't be looked at", "standardized test scores are optional but considered if submitted"),
    ("they do not look at sat/act scores at all.", "they will consider sat/act scores as part of their evaluation process."),
    ("do not submit sat/act", "sat/act submission is optional"),
    ("Test-Blind", "Test-Free")
]

PROMO_PHRASES = [
    ("Cracking the Bodwell Admission Code", "Bodwell High School Admissions Guide"),
    ("best private boys' school", "independent boys' school")
]

def fix_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(filepath, 'r', encoding='cp1252') as f:
                content = f.read()
        except Exception:
            return False
            
    original = content
    
    # 1. Fix Mojibake
    for bad, good in MOJIBAKE_MAP.items():
        content = content.replace(bad, good)
        
    # 2. Fix Caltech (Case insensitive)
    if 'california-institute-of-technology' in filepath or 'caltech' in filepath.lower() or 'top-10' in filepath or 'top-50' in filepath:
        for bad, good in CALTECH_PHRASES:
            content = re.sub(re.escape(bad), good, content, flags=re.IGNORECASE)
            
    # 3. Fix Promo / Bodwell / UCC
    for bad, good in PROMO_PHRASES:
        content = content.replace(bad, good)
        
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

count = 0
for root, dirs, files in os.walk('.'):
    if '.git' in root or '.vercel' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith('.html') or file.endswith('.json') or file.endswith('.xml'):
            if fix_file(os.path.join(root, file)):
                count += 1
print(f'Fixed {count} files.')