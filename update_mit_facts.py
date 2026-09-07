import re

with open('massachusetts-institute-of-technology-complete-overview-key-facts-and-official-contact-details/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_text = 'Families with total incomes below certain thresholds (historically around ,000 USD) often receive substantial aid, and those below lower thresholds pay zero tuition.'
new_text = 'Families with total incomes below ,000 USD (with typical assets) generally attend tuition-free, and families earning under ,000 USD typically pay nothing for tuition, room, or board.'

if old_text in html:
    html = html.replace(old_text, new_text)
    with open('massachusetts-institute-of-technology-complete-overview-key-facts-and-official-contact-details/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully updated MIT financial aid thresholds.")
else:
    print("Could not find old text to replace.")