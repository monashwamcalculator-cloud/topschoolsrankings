import os
import json

# Fix 1: search-index.json
file1 = 'assets/search-index.json'
with open(file1, 'r', encoding='utf-8') as f:
    content1 = f.read()
content1 = content1.replace('Hard Strategy to Get Admitted', 'Bodwell High School Admissions Guide')
with open(file1, 'w', encoding='utf-8') as f:
    f.write(content1)

# Fix 2: Bodwell article
file2 = 'bodwell-high-school-acceptance-rate-admissions-strategy/index.html'
with open(file2, 'r', encoding='utf-8') as f:
    content2 = f.read()
content2 = content2.replace('Cracking the Bodwell Admission Code', 'Bodwell High School Admissions Guide')
with open(file2, 'w', encoding='utf-8') as f:
    f.write(content2)

# Fix 3: UCC article
file3 = 'upper-canada-college-admission-fees-ib-program/index.html'
with open(file3, 'r', encoding='utf-8') as f:
    content3 = f.read()
content3 = content3.replace("best private boys' school in Toronto", "independent boys' school in Toronto")
content3 = content3.replace("best private boys’ school in Toronto", "independent boys' school in Toronto") # just in case smart quotes
with open(file3, 'w', encoding='utf-8') as f:
    f.write(content3)

print("Files modified successfully.")
