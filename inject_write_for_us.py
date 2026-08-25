import re

html_path = 'c:/Users/Hp/Downloads/topschoolsrankings-new-site-upload-v2/write-for-us/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

replacement = '</header><figure class="featured-media site-container narrow"><img alt="Freelance education writer typing an article draft on a laptop for Top Schools Rankings" class="" decoding="async" height="941" loading="eager" src="/media/articles/write-for-us.webp" width="1672"/></figure><section class="section site-container article-layout">'

if '</header><section class="section site-container article-layout">' in html:
    html = html.replace('</header><section class="section site-container article-layout">', replacement)
else:
    html = re.sub(r'</header>\s*<section class="section site-container article-layout">', replacement, html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print('Successfully injected HTML figure')
