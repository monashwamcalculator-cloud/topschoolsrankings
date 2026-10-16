import os
import re
from bs4 import BeautifulSoup

target_files = [
    "blogs/index.html",
    "category/degree-career-guides/index.html",
    "category/degree-and-career-guides/index.html"
]

for file_path in target_files:
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist, skipping.")
        continue

    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")
    
    # Locate the <a> or <article> card that links to /top-ranked-vet-schools-in-us/
    card = soup.find(lambda tag: (tag.name in ['a', 'article'] and tag.get('href', '') == '/top-ranked-vet-schools-in-us/') or 
                     (tag.name == 'article' and tag.find('a', href=lambda h: h and '/top-ranked-vet-schools-in-us/' in h)))
    
    # If found via <a>, grab parent article if available
    if card and card.name != 'article':
        parent_article = card.find_parent('article')
        if parent_article:
            card = parent_article

    if not card:
        # Fallback search for any element linking to the target
        link = soup.find('a', href=lambda h: h and '/top-ranked-vet-schools-in-us/' in h)
        if link:
            card = link.find_parent('article') or link

    if not card:
        print(f"Could not find card linking to /top-ranked-vet-schools-in-us/ in {file_path}")
        continue

    # Inside that specific card, find the element that currently contains October 16, 2026
    found = False
    for el in card.find_all(['time', 'span', 'div']):
        if el.string and re.search(r'october\s+16,\s+2026', el.string, re.IGNORECASE):
            print(f"Replacing text in <{el.name}>: '{el.string.strip()}' -> '12 MIN READ'")
            el.string.replace_with("12 MIN READ")
            found = True
            break
        elif el.children:
            for child in list(el.children):
                if isinstance(child, str) and re.search(r'october\s+16,\s+2026', child, re.IGNORECASE):
                    print(f"Replacing text node in <{el.name}>: '{child.strip()}' -> '12 MIN READ'")
                    child.replace_with("12 MIN READ")
                    found = True
                    break
            if found:
                break

    if found:
        with open(file_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(str(soup))
        print(f"Successfully updated {file_path}")
    else:
        print(f"No date matching 'October 16, 2026' found in card for {file_path}")

print("Completed card meta updates.")
