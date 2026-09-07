import os
import re

html_files = []
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

results = {
    'lorem': [],
    'ai_footprint': [],
    'thin_content': [],
    'noindex_needed': [],
}

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 1. Lorem ipsum
    if 'lorem ipsum' in content.lower():
        results['lorem'].append(filepath)
        
    # 2. AI footprint
    ai_phrases = ['as an ai', 'your screenshot', 'i cannot verify', 'language model', 'in this image', 'based on the screenshot']
    for phrase in ai_phrases:
        if phrase in content.lower():
            results['ai_footprint'].append((filepath, phrase))
            
    # 3. Thin content (check text length inside body)
    # Just rough word count of the file
    words = len(re.findall(r'\w+', content))
    if words < 150:
        results['thin_content'].append((filepath, words))
        
    # 4. Pages that should probably be noindex (write-for-us, tags, search)
    if 'write-for-us' in filepath or 'tag' in filepath or 'author' in filepath:
        if 'noindex' not in content.lower():
            results['noindex_needed'].append(filepath)

print("LOREM IPSUM:")
for r in results['lorem']: print(r)

print("\nAI FOOTPRINTS:")
for r in results['ai_footprint']: print(r)

print("\nTHIN CONTENT (<150 words):")
for r in results['thin_content']: print(r)

print("\nMISSING NOINDEX:")
for r in results['noindex_needed']: print(r)
