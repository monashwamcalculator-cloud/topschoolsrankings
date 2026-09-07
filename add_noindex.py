import os
import re

files_to_noindex = [
    'write-for-us/index.html',
    'author/saahil/index.html',
    'author/samrat-biswas/index.html'
]

for filepath in files_to_noindex:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace index, follow with noindex, follow
        if '<meta name="robots" content="index, follow">' in content:
            content = content.replace('<meta name="robots" content="index, follow">', '<meta name="robots" content="noindex, follow">')
        else:
            # Inject it before </head> if not found
            content = content.replace('</head>', '<meta name="robots" content="noindex, follow"></head>')
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added noindex to {filepath}")
    else:
        print(f"File not found: {filepath}")