import re

with open('top-25-universities-in-canada-for-international-students/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add IRCC link
html = html.replace(
    'directly on the official Government of Canada (IRCC) website',
    'directly on the official <a href="https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada.html" target="_blank" rel="noopener noreferrer">Government of Canada (IRCC) website</a>'
)

# Add QS link
html = html.replace(
    'the <strong>QS World University Rankings (2026 edition)</strong>',
    'the <strong><a href="https://www.topuniversities.com/university-rankings/world-university-rankings" target="_blank" rel="noopener noreferrer">QS World University Rankings</a> (2026 edition)</strong>'
)

with open('top-25-universities-in-canada-for-international-students/index.html', 'w', encoding='utf-8') as f:
    f.write(html)