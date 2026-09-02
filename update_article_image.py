import re

with open('how-universities-are-using-custom-software-solutions-to-build-smarter-digital-education-ecosystems/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update og:image and twitter:image
img_url = 'https://topschoolsrankings.com/media/articles/how-universities-custom-software-digital-education-ecosystem-featured.webp'
html = html.replace('content="https://topschoolsrankings.com/og.png"', f'content="{img_url}"')

# Update structured data
schema_old = '"image":"https://topschoolsrankings.com/og.png"'
schema_new = f'"image":"{img_url}"'
html = html.replace(schema_old, schema_new)

# Add <figure> after <header class="page-header">...</header>
# But wait, looking at brown-university guide, it is placed exactly after </header> and before <section class="section site-container article-layout">
figure_html = '''<figure class="featured-media site-container narrow"><img class="" src="/media/articles/how-universities-custom-software-digital-education-ecosystem-featured.webp" alt="Digital education ecosystem connecting university learning, student information, analytics, advising and secure data systems" width="1672" height="941" loading="eager" decoding="async"><figcaption>Editorial feature image for this education research guide.</figcaption></figure>'''

html = html.replace('</header>\n  \n  <section', '</header>\n  ' + figure_html + '\n  <section')

with open('how-universities-are-using-custom-software-solutions-to-build-smarter-digital-education-ecosystems/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated article HTML with featured image.")