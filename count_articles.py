import re
import html

with open('blogs/index.html', 'r', encoding='utf-8') as f:
    blog_text = f.read()

articles_in_blog = re.findall(r'<article class="guide-card">.*?</article>', blog_text, re.DOTALL)
print('Articles in blog:', len(articles_in_blog))

with open('author/saahil/index.html', 'r', encoding='utf-8') as f:
    author_text = f.read()

author_h2 = re.findall(r'<h2>(.*?)</h2>', author_text)
print('H2s in author:', len(author_h2))
