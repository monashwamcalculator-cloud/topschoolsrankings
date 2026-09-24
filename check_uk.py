import re

with open('how-to-choose-a-university-course-uk/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'<article class="article-body">(.*?)</article>', html, re.DOTALL)
if match:
    text = match.group(1)
    with open('uk_course_content.md', 'w', encoding='utf-8') as f2:
        f2.write(text)