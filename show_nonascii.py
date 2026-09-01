import os
import re

with open('index.html', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

non_ascii = re.finditer(r'[^\x00-\x7F]+', content)
unique_snippets = set()

with open('nonascii_out.txt', 'w', encoding='utf-8') as out:
    for m in non_ascii:
        idx = m.start()
        char = content[idx:m.end()]
        if char not in unique_snippets:
            unique_snippets.add(char)
            snippet = content[max(0, idx-10):min(len(content), idx+10)]
            out.write(f"Char: {repr(char)} | Snippet: {repr(snippet)}\n")
