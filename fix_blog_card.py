with open('blogs/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

bad_card = '''<article class="guide-card">
<div class="card-meta">
<span>Digital Education</span>
<span>6 min read</span>
</div>
<h3><a href="/how-universities-are-using-custom-software-solutions-to-build-smarter-digital-education-ecosystems/">How Universities Are Using Custom Software Solutions to Build Smarter Digital Education Ecosystems</a></h3>
<p>Explore how modern universities leverage custom software to create unified, secure, and personalized digital learning environments for students.</p>
<a class="text-link" href="/how-universities-are-using-custom-software-solutions-to-build-smarter-digital-education-ecosystems/">Read guide <span>&#x2192;</span></a>
</article>'''

good_card = '''<article class="guide-card">
<a aria-label="Read How Universities Are Using Custom Software Solutions to Build Smarter Digital Education Ecosystems" class="guide-card-image" href="/how-universities-are-using-custom-software-solutions-to-build-smarter-digital-education-ecosystems/">
<img alt="Digital education ecosystem connecting university learning, student information, analytics, advising and secure data systems" decoding="async" height="941" loading="lazy" src="/media/articles/how-universities-custom-software-digital-education-ecosystem-featured.webp" width="1672"/>
</a>
<div class="card-meta">
<span>Digital Education</span>
<span>6 min read</span>
</div>
<h3><a href="/how-universities-are-using-custom-software-solutions-to-build-smarter-digital-education-ecosystems/">How Universities Are Using Custom Software Solutions to Build Smarter Digital Education Ecosystems</a></h3>
<p>Explore how modern universities leverage custom software to create unified, secure, and personalized digital learning environments for students.</p>
<a class="text-link" href="/how-universities-are-using-custom-software-solutions-to-build-smarter-digital-education-ecosystems/">Read guide <span>&#x2192;</span></a>
</article>'''

if bad_card in html:
    html = html.replace(bad_card, good_card)
    with open('blogs/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Successfully fixed the blog card!')
else:
    print('Could not find the exact bad card string in blogs/index.html')
