import os
import re
from bs4 import BeautifulSoup

target_file = "top-ranked-vet-schools-in-us/index.html"

if not os.path.exists(target_file):
    raise FileNotFoundError(f"Target file {target_file} not found.")

print(f"Reading {target_file}...")
with open(target_file, "r", encoding="utf-8") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")

# Locate author bio box
author_box = soup.find("div", class_="author-bio-box")
if not author_box:
    author_box = soup.find(lambda t: t.name in ["div", "section"] and any("author" in c for c in t.get("class", [])))
if not author_box:
    saahil_link = soup.find("a", href="/author/saahil/")
    if saahil_link:
        author_box = saahil_link.find_parent("div", class_=lambda c: c and "author" in c) or saahil_link.find_parent("div")

if not author_box:
    raise ValueError("Could not locate author bio box in the HTML.")

print(f"Found author bio box: <{author_box.name} class='{author_box.get('class')}'>")

# Check if related-guides-section already exists to prevent duplicate insertion
existing = soup.find("div", class_="related-guides-section")
if existing:
    print("Related guides section already exists, replacing it...")
    existing.decompose()

related_guides_html = """<div class="related-guides-section" style="margin: 40px 0; padding: 20px 0; border-top: 1px solid #e2e8f0; border-bottom: 1px solid #e2e8f0;">
    <h2 style="font-size: 1.5rem; font-weight: 700; margin-bottom: 15px; color: #0f2237;">Related TopSchoolsRankings Guides</h2>
    <ul style="list-style-type: disc; padding-left: 20px; line-height: 1.8;">
        <li><a href="/top-10-medical-universities-in-usa/" style="color: #2563eb; text-decoration: none;">Top 10 Medical Universities in the USA</a></li>
        <li><a href="/top-10-stem-boarding-schools-in-usa/" style="color: #2563eb; text-decoration: none;">Top 10 STEM Boarding Schools in the USA</a></li>
    </ul>
</div>"""

related_block = BeautifulSoup(related_guides_html, "html.parser")
author_box.insert_before(related_block)

with open(target_file, "w", encoding="utf-8", newline="\n") as f:
    f.write(str(soup))

print(f"Successfully injected related guides section into {target_file}")
