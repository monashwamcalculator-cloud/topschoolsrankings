import os
import re
import docx
from PIL import Image
from bs4 import BeautifulSoup
import datetime

workspace = r'c:\Users\Hp\Downloads\topschoolsrankings-new-site-upload-v2'
article_slug = 'how-smart-hostels-are-changing-student-life-at-indian-universities'
article_dir = os.path.join(workspace, article_slug)
os.makedirs(article_dir, exist_ok=True)

# 1. Process Images
author_img_src = r'C:\Users\Hp\.gemini\antigravity\brain\726bddf1-4614-4b0e-a924-9a6f84cfa50e\.user_uploaded\media_1787818030834.jpg'
author_img_dest = os.path.join(workspace, 'media', 'authors', 'dr-satya-vir-singh.webp')
# crop to square
img = Image.open(author_img_src)
min_dim = min(img.size)
left = (img.width - min_dim)/2
top = (img.height - min_dim)/2
img_cropped = img.crop((left, top, left + min_dim, top + min_dim))
img_cropped.thumbnail((400, 400))
img_cropped.save(author_img_dest, 'webp')

featured_img_src = r'C:\Users\Hp\.gemini\antigravity\brain\726bddf1-4614-4b0e-a924-9a6f84cfa50e\smart_hostel_india_1787818264218.jpg'
featured_img_dest = os.path.join(workspace, 'media', 'new-guides', 'smart-hostel-india.webp')
featured_img = Image.open(featured_img_src)
featured_img.save(featured_img_dest, 'webp')

# 2. Extract Article Content
docx_path = r'C:\Users\Hp\Downloads\How Smart Hostels Are Changing Student Life at Indian Universities AI, Safety and the Future of Campus Living - With Images.docx'
doc = docx.Document(docx_path)
html_content = ""
author_bio = ""

in_faq = False
for para in doc.paragraphs:
    text = para.text.strip()
    if not text:
        continue
    
    # Check if this is the title (skip it)
    if text.startswith('How Smart Hostels Are Changing'):
        continue
        
    # Check if author bio
    if text.startswith('Author'):
        continue
    if text.startswith('Dr. Satya Vir Singh is a higher-education'):
        author_bio = text
        continue
        
    style = para.style.name.lower()
    
    if text == 'Frequently Asked Questions':
        in_faq = True
        html_content += f'<h2>{text}</h2>\n'
        continue
        
    if in_faq and re.match(r'^\d+\.', text):
        html_content += f'<h3>{text}</h3>\n'
        continue

    # heuristics for headings if styles aren't set
    if len(text) < 100 and not text.endswith('.') and not in_faq and (style.startswith('heading') or text[0].isupper()):
        if style == 'heading 2' or text == 'What Will Define the Smart University Campus?' or 'How AI Could Improve' in text or 'What NEP 2020 Means' in text or 'The Importance of Student' in text or 'Connecting Hostel Management' in text or 'What Students Should Check' in text or 'The Future of Hostel' in text or 'Hostel Safety:' in text:
            html_content += f'<h2>{text}</h2>\n'
        elif text.startswith('A useful hostel evaluation checklist could include:'):
            html_content += f'<p>{text}</p>\n<ul><li>Safety measures</li><li>Digital access and app support</li><li>Visitor management protocols</li><li>Grievance redressal systems</li><li>Overall hygiene and community spaces</li></ul>\n'
        else:
            if text not in ['Safety measures', 'Digital access and app support']:
                html_content += f'<p>{text}</p>\n'
    else:
        html_content += f'<p>{text}</p>\n'

# 3. Build the HTML Page
template_path = os.path.join(workspace, 'how-to-choose-a-university-course-uk', 'index.html')
with open(template_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Update Meta
soup.title.string = "How Smart Hostels Are Changing Student Life at Indian Universities | Top Schools Rankings"
for meta in soup.find_all('meta'):
    if meta.get('name') == 'description':
        meta['content'] = "Discover how smart hostels and AI are transforming student life, safety, and campus living at Indian universities."
    if meta.get('property') == 'og:title':
        meta['content'] = soup.title.string
    if meta.get('property') == 'og:url':
        meta['content'] = "https://topschoolsrankings.com/how-smart-hostels-are-changing-student-life-at-indian-universities/"
    if meta.get('property') == 'og:image':
        meta['content'] = "https://topschoolsrankings.com/media/new-guides/smart-hostel-india.webp"

# Update Header
header = soup.find('header', class_='page-header')
header.find('h1').string = "How Smart Hostels Are Changing Student Life at Indian Universities"
header.find('p').string = "AI, Safety and the Future of Campus Living"

# Update Featured Image
figure = soup.find('figure', class_='featured-media')
img = figure.find('img')
img['src'] = "/media/new-guides/smart-hostel-india.webp"
img['alt'] = "Modern smart university hostel in India with diverse students and digital access panels"
figure.find('figcaption').string = "The future of campus living in India is becoming increasingly digital."

# Update Content
rich_content = soup.find('article', class_='article-body')

# Remove existing paragraphs and headers from the template's article body, keeping the bottom boxes
for tag in list(rich_content.children):
    if getattr(tag, 'name', None) in ['p', 'h2', 'h3', 'ul', 'ol', 'img', 'figure']:
        tag.decompose()

content_soup = BeautifulSoup('<div class="rich-article-content">' + html_content + '</div>', 'html.parser')
rich_content.insert(0, content_soup)


# Update Author Block
author_block = soup.find('div', class_='author-bio')
if author_block:
    author_img = author_block.find('img')
    if author_img:
        author_img['src'] = "/media/authors/dr-satya-vir-singh.webp"
        author_img['alt'] = "Dr. Satya Vir Singh"
    
    author_info = author_block.find('div', class_='author-info')
    if author_info:
        author_info.find('h3').string = "About Dr. Satya Vir Singh"
        author_info.find('p').string = author_bio
        # remove links if any
        for a in author_info.find_all('a'):
            a.decompose()

# Update Sidebar Dates
today_str = datetime.datetime.now().strftime("%B %d, %Y")
fact_checked = soup.find(string=re.compile("Fact-checked"))
if fact_checked:
    parent = fact_checked.parent
    if parent.find_next_sibling('span'):
        parent.find_next_sibling('span').string = today_str

# Save article
new_html_path = os.path.join(article_dir, 'index.html')
with open(new_html_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

# 4. Update Blogs Index
blogs_path = os.path.join(workspace, 'blogs', 'index.html')
with open(blogs_path, 'r', encoding='utf-8') as f:
    blogs_html = f.read()

# increment count
blogs_html = re.sub(r'(\d+)\s+editorial guides', lambda m: str(int(m.group(1)) + 1) + ' editorial guides', blogs_html)

new_card = """<article class="guide-card">
        <img src="/media/new-guides/smart-hostel-india.webp" alt="Smart Hostels in India" loading="lazy" decoding="async">
        <div class="card-content">
          <span class="category-badge">India</span>
          <h2><a href="/how-smart-hostels-are-changing-student-life-at-indian-universities/">How Smart Hostels Are Changing Student Life at Indian Universities</a></h2>
          <p>AI, Safety and the Future of Campus Living.</p>
        </div>
      </article>"""

# find first guide-card and insert before
blogs_html = blogs_html.replace('<article class="guide-card">', new_card + '\n      <article class="guide-card">', 1)

with open(blogs_path, 'w', encoding='utf-8') as f:
    f.write(blogs_html)

print("Article built and added successfully!")
