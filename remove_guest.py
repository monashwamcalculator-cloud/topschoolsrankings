with open('how-universities-are-using-custom-software-solutions-to-build-smarter-digital-education-ecosystems/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Header replacements
html = html.replace('<span class="eyebrow">Guest Editorial Guide</span>', '<span class="eyebrow">Education research guide</span>')
html = html.replace('Published 2 September 2026 &middot; Guest Contribution</div>', 'Published 2 September 2026</div>')

# Author box replacements
html = html.replace('<strong>Guest Contributor</strong> &middot; ', '')

with open('how-universities-are-using-custom-software-solutions-to-build-smarter-digital-education-ecosystems/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Removed guest labels from article.')