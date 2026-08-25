import os
from bs4 import BeautifulSoup

html_path = "tools/index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

container = soup.find("div", class_="listing-grid tools-directory")
cards = container.find_all("article", class_="listing-card")

categories = {
    "College & University Academics": [
        "attendance", "cgpa-recovery", "target-gpa", "cumulative-gpa", "final-grade", "wam-calculator", "class-rank", "cgpa"
    ],
    "International Grade Converters": [
        "wam-to-gpa", "gpa-to-wam", "atar-gpa", "cgpa-percentage", "gpa-percentage", "ib-to-gpa", "ib-total-points", "hsc-atar"
    ],
    "Test Scores & English Proficiency": [
        "act-score", "act-to-sat", "sat-score", "duolingo-ielts", "gre-score", "ielts-toefl", "pte-ielts"
    ],
    "High School & Admissions Planning": [
        "college-chances", "a-level", "ap-gpa", "application-timeline", "nsw-selective", "us-college-fit", "weighted-gpa", "international-student", "ucas-tariff"
    ],
    "Cost, Budget & Financial Planning": [
        "boarding-school", "cost-of-living", "dorm-vs-offcampus", "gap-year", "merit-aid", "private-vs-public", "scholarship-eligibility", "student-loan", "study-abroad", "uk-boarding-fees", "university-cost"
    ]
}

categorized_cards = {cat: [] for cat in categories.keys()}
categorized_cards["Other Tools"] = []

for card in cards:
    link = card.find("a")
    if not link:
        categorized_cards["Other Tools"].append(card)
        continue
    
    href = link.get("href", "")
    placed = False
    # Manual overrides or matching
    for cat, keywords in categories.items():
        if placed:
            break
        for kw in keywords:
            if kw in href:
                # Extra check to not mix cgpa-recovery with cgpa-percentage
                if kw == "cgpa" and "percentage" in href:
                    continue # goes to Grade Converters instead
                
                categorized_cards[cat].append(card)
                placed = True
                break
    
    if not placed:
        categorized_cards["Other Tools"].append(card)

# Now rebuild the inner HTML of the section
new_content = ""

for cat_name, cards_list in categorized_cards.items():
    if len(cards_list) == 0:
        continue
    
    # Add section title
    new_content += f'<div style="grid-column: 1 / -1; margin-top: 40px; margin-bottom: 20px; border-bottom: 2px solid rgba(255,255,255,0.1); padding-bottom: 10px;">'
    new_content += f'<h2 style="font-size: 24px; color: #fff; margin: 0;">{cat_name}</h2>'
    new_content += f'</div>\n'
    
    # Add cards
    for card in cards_list:
        new_content += str(card) + "\n"

# Create a new div with the same class but updated content
new_grid = soup.new_tag("div")
new_grid["class"] = "listing-grid tools-directory"
# We parse the new_content to append the elements
parsed_new_content = BeautifulSoup(new_content, "html.parser")
for element in parsed_new_content:
    new_grid.append(element)

container.replace_with(new_grid)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Categorization complete.")
