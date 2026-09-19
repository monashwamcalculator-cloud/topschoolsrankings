import os
import re

def preserve_case_replace(match):
    word = match.group(0)
    
    mapping = {
        r'most prestigious': 'highly competitive',
        r'the ultimate': 'the comprehensive',
        r'ultimate guide': 'comprehensive guide',
        r'ultimate parent': 'comprehensive parent',
        r'premier institution': 'leading institution',
        r'finest institution': 'leading institution',
        r'premier school': 'leading school',
        r'finest school': 'leading school',
        r'second to none': 'highly regarded',
        r'world-class': 'highly regarded',
        r'unrivaled': 'highly competitive'
    }
    
    rep_text = "replaced"
    for pat, rep in mapping.items():
        if re.match(pat, word, re.IGNORECASE):
            rep_text = rep
            break
            
    if word.istitle(): return rep_text.title()
    elif word.isupper(): return rep_text.upper()
    elif word.islower(): return rep_text.lower()
    elif word[0].isupper(): return rep_text.capitalize()
    return rep_text

patterns = [
    r'\bmost prestigious\b',
    r'\bthe ultimate\b',
    r'\bultimate guide\b',
    r'\bultimate parent\b',
    r'\bpremier institution\b',
    r'\bfinest institution\b',
    r'\bpremier school\b',
    r'\bfinest school\b',
    r'\bsecond to none\b',
    r'\bworld-class\b',
    r'\bunrivaled\b'
]

combined_pattern = re.compile('|'.join(patterns), re.IGNORECASE)

modified_count = 0
for root_dir, dirs, files in os.walk('.'):
    if '.git' in root_dir or 'node_modules' in root_dir: continue
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root_dir, f)
            try:
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
            except: continue
            
            new_content = combined_pattern.sub(preserve_case_replace, content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                modified_count += 1

print(f"Successfully applied targeted text replacements in {modified_count} files.")