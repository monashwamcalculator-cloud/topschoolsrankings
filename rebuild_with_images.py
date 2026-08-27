import mammoth
import base64
import os
import io
from PIL import Image
from bs4 import BeautifulSoup

workspace = r'c:\Users\Hp\Downloads\topschoolsrankings-new-site-upload-v2'
docx_path = r'C:\Users\Hp\Downloads\How Smart Hostels Are Changing Student Life at Indian Universities AI, Safety and the Future of Campus Living - With Images.docx'
article_slug = 'how-smart-hostels-are-changing-student-life-at-indian-universities'
html_path = os.path.join(workspace, article_slug, 'index.html')
media_dir = os.path.join(workspace, 'media', 'new-guides')

# Custom image handler for mammoth
image_counter = 1
def convert_image(image):
    global image_counter
    with image.open() as image_bytes:
        image_data = image_bytes.read()
    
    # Save base64 image via PIL to WebP
    img = Image.open(io.BytesIO(image_data))
    filename = f'smart-hostels-india-inline-{image_counter}.webp'
    filepath = os.path.join(media_dir, filename)
    img.save(filepath, 'webp')
    
    image_counter += 1
    
    # Return the new src
    return {"src": f"/media/new-guides/{filename}"}

with open(docx_path, "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file, convert_image=mammoth.images.img_element(convert_image))
    html = result.value
    messages = result.messages

# Now we need to inject this HTML into the existing page
# Clean up HTML: mammoth outputs raw p and img tags.
# We also want to skip the title and author bio since we already handled them.
soup_content = BeautifulSoup(html, 'html.parser')

# We can remove the first H1/P if it's the title
for p in soup_content.find_all('p'):
    if 'How Smart Hostels Are Changing' in p.text:
        p.decompose()
        break

# We can convert some things to H2 based on bold or size, but mammoth handles styles if they were used.
# If mammoth just made everything <p>, let's convert our known headers to <h2>
for p in soup_content.find_all('p'):
    text = p.get_text(strip=True)
    if 'Author' in text and 'Dr. Satya Vir Singh' in text:
        p.decompose() # remove author block
        continue
    if text.startswith('Author'):
        p.decompose()
        continue
    
    if text == 'Frequently Asked Questions':
        p.name = 'h2'
        continue
        
    if text in ['How AI Could Improve University Hostel Management', 
                'Hostel Safety: What Students and Parents Should Look For', 
                'The Importance of Student Experience', 
                'Connecting Hostel Management with Academic Administration', 
                'What NEP 2020 Means for Digital University Governance', 
                'What Students Should Check Before Choosing a University Hostel', 
                'The Future of Hostel Management in Indian Universities',
                'What Will Define the Smart University Campus?']:
        p.name = 'h2'
        
    # FAQs
    if text.startswith('1.') or text.startswith('2.') or text.startswith('3.') or text.startswith('4.') or text.startswith('5.') or text.startswith('6.'):
        # Only if it's a question
        if '?' in text:
            p.name = 'h3'

# Read the existing page
with open(html_path, 'r', encoding='utf-8') as f:
    page_soup = BeautifulSoup(f.read(), 'html.parser')

# Replace the article content
rich_content = page_soup.find('article', class_='article-body')

# Remove existing paragraphs, lists, headings (which was our previous flawed text)
for tag in list(rich_content.children):
    if getattr(tag, 'name', None) in ['p', 'h2', 'h3', 'ul', 'ol', 'img', 'figure', 'div']:
        # Don't remove the bottom boxes
        if tag.name == 'div' and tag.get('class') and ('author-bio-box' in tag.get('class') or 'answer-box' in tag.get('class') or 'editor-note' in tag.get('class') or 'related-grid' in tag.get('class')):
            continue
        tag.decompose()

# Insert new content
wrapper = BeautifulSoup('<div class="rich-article-content"></div>', 'html.parser')
wrapper.div.append(soup_content)
rich_content.insert(0, wrapper.div)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(str(page_soup))
    
print("Successfully extracted images and injected full HTML.")
