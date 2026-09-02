import re

with open('blogs/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_card = '''<article class="guide-card">
<div class="card-meta">
<span>Digital Education</span>
<span>6 min read</span>
</div>
<h3><a href="/how-universities-are-using-custom-software-solutions-to-build-smarter-digital-education-ecosystems/">How Universities Are Using Custom Software Solutions to Build Smarter Digital Education Ecosystems</a></h3>
<p>Explore how modern universities leverage custom software to create unified, secure, and personalized digital learning environments for students.</p>
<a class="text-link" href="/how-universities-are-using-custom-software-solutions-to-build-smarter-digital-education-ecosystems/">Read guide <span>&#x2192;</span></a>
</article>
'''

# Insert the new card right after <div class="guide-grid">
html = html.replace('<div class="guide-grid">', '<div class="guide-grid">\n' + new_card)

with open('blogs/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added card to blogs/index.html")