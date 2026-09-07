import re

with open('top-50-universities-in-usa/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Princeton alumni giving
html = html.replace(
    'due to its strong undergraduate focus and alumni giving',
    'due to its strong graduation rates, extensive faculty resources, and peer assessment scores'
)

# 2. MIT/Caltech "gold standard"
html = html.replace(
    'remain the gold standard for engineering and physical sciences',
    'are globally recognized for engineering and physical sciences'
)

# 3. U.S. News methodology mentioning
html = html.replace(
    'Domestic lists like U.S. News place more weight on undergraduate graduation rates and peer assessment.',
    'Domestic lists like U.S. News place significant weight on graduation rates, retention, and peer assessment.'
)

# 4. Out-of-state cost
html = html.replace(
    'often at a lower out-of-state cost compared to private peers',
    'often at a lower out-of-state tuition rate compared to the sticker price of private peers'
)

# 5. Ivy League "often need-blind"
# Text is: "generous, often need-blind financial aid." -> Princeton, Harvard, Yale are universally need-blind.
html = html.replace(
    'generous, often need-blind financial aid.',
    'generous financial aid, with policies that are need-blind even for international students.'
)

with open('top-50-universities-in-usa/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Factual corrections applied.")