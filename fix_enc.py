import os
import re

def fix_encoding(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    content = content.replace('â†’', '→')
    content = content.replace('â†\'', '→')
    content = content.replace('â€¢', '•')
    content = content.replace('Â·', '·')
    content = content.replace('â€”', '—')
    content = content.replace('Â©', '©')
    content = content.replace("Report a correction +'", 'Report a correction →')
    content = content.replace("Report a correction \x81'", 'Report a correction →')
    
    # Catch any remaining "Use tool â..." stuff 
    content = re.sub(r'Use tool â[^<]+', 'Use tool →', content)
        
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed {filepath}')

for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            fix_encoding(os.path.join(root, file))
