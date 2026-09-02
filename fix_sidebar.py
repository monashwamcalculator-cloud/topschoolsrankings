import re
with open('how-universities-are-using-custom-software-solutions-to-build-smarter-digital-education-ecosystems/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

good_end = '''</article><aside class="article-aside"><div><span class="aside-label">Reviewed</span><strong>2 September 2026</strong><p>Edited for editorial guidelines. Statistics rely on author's external sources.</p></div><div><span class="aside-label">Correction</span><a href="/contact-us/">Report an issue &#x2192;</a></div></aside></section>'''

html = re.sub(r'</article>\s*</section>', good_end, html)

with open('how-universities-are-using-custom-software-solutions-to-build-smarter-digital-education-ecosystems/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Successfully added the sidebar via regex!')