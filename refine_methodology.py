import os

file_path = 'ranking-methodology/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Claim 5: Common Data Set
content = content.replace(
    'Common Data Set (CDS) where available',
    'Common Data Set (CDS) where published by the institution'
)

# Fix Claim 7: Periodic Audits
content = content.replace(
    '<li><strong>Periodic Audits:</strong> We regularly audit tuition figures and contact information.</li>',
    '<li><strong>Policy Updates:</strong> We audit and update guides when major policy shifts (such as test-optional changes) are officially announced.</li>'
)

# Fix Claim 9: Missing Data Exclusion
content = content.replace(
    'If critical data points are entirely missing and cannot be sourced from government datasets, the institution may be excluded from data-heavy comparative lists.',
    'If a specific data point is entirely missing and cannot be sourced from government datasets, we simply omit that metric from their profile rather than calculating an artificial estimate.'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Adjustments made to ranking-methodology/index.html')
