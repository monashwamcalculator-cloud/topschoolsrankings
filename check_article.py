import re
with open('appleby-college-canada-boarding-school-admissions-fees-student-life-guide-for-international-students/index.html', 'r', encoding='utf-8') as f:
    text = f.read()
    m = re.search(r'<img[^>]*class="article-hero-image"[^>]*>', text)
    if m:
        print(m.group(0))
