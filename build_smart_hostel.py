import os
import shutil
from bs4 import BeautifulSoup
from PIL import Image
import re

workspace = r'c:\Users\Hp\Downloads\topschoolsrankings-new-site-upload-v2'
slug = "smart-hostel-management-in-indian-universities"
dest_dir = os.path.join(workspace, slug)
os.makedirs(dest_dir, exist_ok=True)

# 1. Process Featured Image
img_src = r'C:\Users\Hp\.gemini\antigravity\brain\726bddf1-4614-4b0e-a924-9a6f84cfa50e\.user_uploaded\media_1787821345453.jpg'
img_dest_webp = os.path.join(workspace, 'media', 'new-guides', f'{slug}-featured.webp')
img_dest_jpg = os.path.join(workspace, 'media', 'new-guides', f'{slug}-featured.jpg')

# Copy the jpg
shutil.copy2(img_src, img_dest_jpg)
# Convert to webp
with Image.open(img_src) as img:
    img.save(img_dest_webp, 'webp', quality=80)

# 2. Template
template_path = os.path.join(workspace, 'how-to-choose-a-university-course-uk', 'index.html')
with open(template_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

title_text = "Smart Hostel Management in Indian Universities: Building Safer, Better Campus Experiences"
# Update title and meta
soup.title.string = f"{title_text} | Top Schools Rankings"

# Update h1
h1 = soup.find('h1')
if h1:
    h1.string = title_text

# Update eyebrow
eyebrow = soup.find('span', class_='eyebrow')
if eyebrow:
    eyebrow.string = "India Universities"

# Update featured image
figure = soup.find('figure', class_='featured-media')
if figure:
    img_tag = figure.find('img')
    if img_tag:
        img_tag['src'] = f"/media/new-guides/{slug}-featured.webp"
        img_tag['alt'] = title_text

# Update content
article_body = soup.find('article', class_='article-body')

# Collect all elements before answer-box and remove them
to_remove = []
for child in article_body.children:
    if child.name == 'div' and child.get('class') == ['answer-box']:
        break
    if child.name == 'div' and child.get('class') == ['author-bio-box']:
        continue
    to_remove.append(child)

for el in to_remove:
    try:
        el.extract()
    except Exception:
        pass
    
# Remove answer-box entirely as it's not in the new HTML
ans_box = article_body.find('div', class_='answer-box')
if ans_box:
    ans_box.decompose()
editor_note = article_body.find('div', class_='editor-note')
if editor_note:
    editor_note.decompose()

# Read the HTML content
html_content = """
<h2>Quick Summary</h2>
<p>Hostel facilities are becoming an increasingly important part of the university experience in India. The Union Budget 2026–27 proposed establishing <strong>one girls' hostel in every district</strong>, with the stated objective of promoting scientific culture through STEM education.</p>
<p>As universities expand residential capacity, the next challenge is how these facilities are managed. Digital hostel management, automated attendance, student communication, security systems, maintenance workflows and analytics can help universities create safer and more responsive residential environments.</p>
<p>For students and parents evaluating universities, therefore, <strong>hostel quality should increasingly be considered alongside academic programmes, fees, placements and campus infrastructure.</strong></p>
<h2>Why Hostel Infrastructure Matters in Indian Universities</h2>
<p>Choosing a university is no longer only about selecting a degree programme.</p>
<p>For students who move from one city or state to another, campus life includes accommodation, food, security, transportation, healthcare, student activities and access to support services.</p>
<p>For parents, hostel facilities can be equally important.</p>
<p>Questions such as these often influence the final university decision:</p>
<ul>
  <li>Is the hostel safe?</li>
  <li>How are visitors managed?</li>
  <li>How are complaints handled?</li>
  <li>Can parents communicate easily with the institution?</li>
  <li>How are rooms allocated?</li>
  <li>How are hostel fees managed?</li>
  <li>Is attendance monitored?</li>
  <li>How quickly are maintenance problems resolved?</li>
  <li>What happens if a student requires assistance?</li>
</ul>
<p>These questions make hostel management an important part of the overall university experience.</p>
<p>The Union Budget 2026–27 has given this issue additional significance by proposing one girls' hostel in every district. The announcement is particularly relevant to increasing access to higher education and STEM opportunities for women.</p>
<p>The next step is to ensure that new residential infrastructure is not simply available, but <strong>well managed and student-centred</strong>.</p>
<h2>What Is a Smart Hostel?</h2>
<p>A smart hostel is more than a building equipped with Wi-Fi, CCTV cameras or biometric devices.</p>
<p>It is a residential environment in which <strong>technology connects everyday administrative and student-support processes</strong>.</p>
<p>A university's hostel management system can potentially bring together:</p>
<ul>
    <li>Hostel admission and room allocation</li>
    <li>Biometric or RFID-based attendance tracking</li>
    <li>Fee collection and receipts</li>
    <li>Visitor and gate management</li>
    <li>Maintenance and complaint workflows</li>
    <li>Student notifications and communication</li>
    <li>Inventory management (e.g. mess and cleaning supplies)</li>
</ul>
<p>The objective is not to replace the people who manage hostels.</p>
<p>It is to give wardens, administrators and university leadership <strong>better information and more efficient workflows</strong>.</p>
<h2>From Registers to Real-Time Campus Management</h2>
<p>Traditional hostel administration often depends on registers, spreadsheets, paper-based complaints and multiple disconnected records.</p>
<p>Such processes may work when the number of residents is small.</p>
<p>The challenge becomes much greater when a university operates multiple hostels serving thousands of students.</p>
<p>A digital platform can provide administrators with a real-time view of areas such as:</p>
<ul>
  <li>Current occupancy</li>
  <li>Room availability</li>
  <li>Pending maintenance requests</li>
  <li>Student complaints</li>
  <li>Visitor activity</li>
  <li>Fee status</li>
  <li>Attendance information</li>
  <li>Hostel-wise utilisation</li>
</ul>
<p>This can reduce the amount of time spent compiling information manually.</p>
<p>More importantly, it can help university administrators identify operational issues earlier.</p>
<p>For example, a maintenance dashboard can show whether a particular hostel is generating a disproportionate number of complaints. Occupancy analytics can help administrators plan room allocation. Digital grievance workflows can make it easier to identify unresolved complaints.</p>
<p>This represents a shift from <strong>record keeping to operational intelligence</strong>.</p>
<h2>Hostel Safety: What Students and Parents Should Look For</h2>
<p>Safety is one of the most important considerations when evaluating university accommodation.</p>
<p>This becomes particularly significant for students moving away from home for the first time.</p>
<p>A well-managed hostel should have clearly defined processes for:</p>
<ul>
  <li>Visitor management</li>
  <li>Entry and exit monitoring</li>
  <li>Emergency response</li>
  <li>Complaint escalation</li>
  <li>Maintenance and electrical safety</li>
  <li>Communication with parents</li>
  <li>Warden and support-staff availability</li>
  <li>Incident documentation</li>
</ul>
<p>Technology can strengthen many of these processes.</p>
<p>For example, digital visitor management can create a record of authorised visitors, while online complaint systems can provide a documented escalation trail.</p>
<p>But technology should complement—not replace—trained wardens, security personnel and responsive university administration.</p>
<p><strong>A secure campus is ultimately created by people, processes and technology working together.</strong></p>
<h2>The Importance of Student Experience</h2>
<p>Hostel life is also an important part of student development.</p>
<p>Students living on campus are not simply residents. They participate in clubs, sports, cultural activities, peer communities and academic interactions.</p>
<p>The residential environment can influence how connected a student feels to the university.</p>
<p>This means universities should look beyond physical facilities.</p>
<p>A strong hostel experience can include:</p>
<ul>
  <li>Clean and well-maintained living spaces</li>
  <li>Reliable food and essential services</li>
  <li>Responsive complaint resolution</li>
  <li>Recreational and common areas</li>
  <li>Student communities</li>
  <li>Digital access to campus services</li>
  <li>Effective communication with the institution</li>
  <li>Appropriate academic and wellbeing support</li>
</ul>
<p>The objective should be to create a residential environment in which students feel <strong>safe, supported and connected</strong>.</p>
<h2>Connecting Hostel Management with Academic Administration</h2>
<p>One of the next major developments in university technology is likely to be greater integration between residential and academic systems.</p>
<p>Today, many institutions still operate different systems for:</p>
<p><strong>Hostels | Attendance | Fees | Student Services | Complaints | Security | Academic Administration</strong></p>
<p>From the student's perspective, however, these are not separate experiences.</p>
<p>They are part of one university journey.</p>
<p>Connecting these systems can potentially help university leadership gain a broader view of student life.</p>
<p>For example, appropriate integration can allow institutions to understand relationships between residential operations and academic participation without requiring administrators to manually reconcile information across multiple systems.</p>
<p>This can support better:</p>
<ul>
  <li>Student support</li>
  <li>Resource planning</li>
  <li>Institutional reporting</li>
  <li>Compliance management</li>
  <li>Communication</li>
  <li>Operational decision-making</li>
</ul>
<p>The long-term direction is therefore not simply a <strong>Hostel Management System</strong>.</p>
<p>It is a broader <strong>Campus Management Ecosystem</strong>.</p>
<h2>What NEP 2020 Means for Digital University Governance</h2>
<p>The move towards digital campus management also aligns with the broader direction of India's National Education Policy 2020.</p>
<p>NEP 2020 includes dedicated provisions relating to <strong>technology use and integration</strong>, and identifies educational technology as an important component of improving educational processes and outcomes. It also discusses technology-enabled planning and management.</p>
<p>The policy's emphasis on effective governance, transparency and technology creates an important context for universities considering digital transformation.</p>
<p>For institutions, the question is increasingly becoming:</p>
<p><strong>How can technology improve the quality of the student experience while also strengthening institutional governance?</strong></p>
<p>Smart hostel management can be one component of that larger transformation.</p>
<h2>What Students Should Check Before Choosing a University Hostel</h2>
<p>Students and parents comparing universities should consider more than the number of hostel buildings or whether rooms are air-conditioned.</p>
<p>A useful hostel evaluation checklist could include:</p>
<ul>
    <li>Are hostels on campus or off campus?</li>
    <li>Is transportation required and provided?</li>
    <li>How is security managed at the gate and within the building?</li>
    <li>Is there a digital system for reporting maintenance or other complaints?</li>
    <li>What are the procedures if a student is unwell outside normal hours?</li>
    <li>How are parents informed in an emergency?</li>
    <li>Is there an orientation programme for new residents?</li>
</ul>
<p>These factors can provide a more realistic picture of residential life than a hostel brochure alone.</p>
<h2>The Future of Hostel Management in Indian Universities</h2>
<p>The next generation of Indian universities is likely to see a gradual shift from standalone hostel administration towards integrated campus management.</p>
<p>Platforms such as <strong>FretBox</strong> are examples of this direction, connecting hostel operations with broader campus administration and AI-enabled attendance capabilities.</p>
<p>The larger transformation, however, is bigger than any single software platform.</p>
<p>Universities will need to consider:</p>
<ol>
  <li><strong>Digital-first administration</strong></li>
  <li><strong>Student-centric services</strong></li>
  <li><strong>Responsible AI adoption</strong></li>
  <li><strong>Data privacy and cybersecurity</strong></li>
  <li><strong>Integrated campus systems</strong></li>
  <li><strong>Real-time operational visibility</strong></li>
  <li><strong>Better communication with students and parents</strong></li>
</ol>
<p>The objective should always remain the same:</p>
<p><strong>Better governance. Better safety. Better student experience.</strong></p>
<h2>What Will Define the Smart University Campus?</h2>
<p>The university campus of the future will not be defined only by modern academic buildings, smart classrooms or high-speed internet.</p>
<p>Its competitiveness will increasingly depend on how effectively it manages the <strong>complete student journey</strong>.</p>
<p>That journey begins before admission and continues through classrooms, laboratories, hostels, dining facilities, student services, internships and ultimately graduation.</p>
<p>Residential infrastructure is therefore not separate from education.</p>
<p>It is part of the education experience.</p>
<p>India's proposal to establish girls' hostels across districts creates an opportunity to think about this infrastructure differently. The priority should not only be to create more accommodation, but to build residential environments that are <strong>safe, accessible, digitally enabled and connected to the university's wider student-support ecosystem.</strong></p>
<p>The goal should be simple:</p>
<p><strong>Not just more hostels, but better university living.</strong></p>
<p>And ultimately:</p>
<p><strong>Smart Hostels. Safe Campuses. Better Student Experiences.</strong></p>
<h2>Frequently Asked Questions</h2>
<h3>1. What is a smart hostel in a university?</h3>
<p>A smart hostel uses digital systems to manage functions such as room allocation, fees, attendance, visitor management, complaints, maintenance, communication and administrative reporting.</p>
<h3>2. How can AI be used in university hostels?</h3>
<p>AI can support attendance analytics, operational alerts, reporting, predictive insights and decision-making. Its use should be governed by appropriate privacy, security and responsible-AI policies.</p>
<h3>3. Why is hostel infrastructure important when choosing a university?</h3>
<p>For students living away from home, hostel facilities directly affect safety, convenience, cost, wellbeing and campus experience. Hostel quality can therefore be an important part of comparing universities.</p>
<h3>4. What did the Union Budget 2026–27 announce regarding girls' hostels?</h3>
<p>The Union Budget 2026–27 proposed establishing <strong>one girls' hostel in every district</strong>, with the initiative linked to promoting scientific culture through STEM education.</p>
<h3>5. Can hostel management be integrated with academic systems?</h3>
<p>Yes. Universities can integrate appropriate residential, attendance, student-service, communication and administrative systems to create a more connected campus-management environment.</p>
<h3>6. Does technology replace hostel wardens and administrators?</h3>
<p>No. Properly implemented technology should support wardens and administrators by reducing repetitive work and providing better information. Human interaction and judgement remain essential to student support.</p>
"""

content_soup = BeautifulSoup(html_content, 'html.parser')
article_body.insert(0, content_soup)

# Author bio box
author_box = soup.find('div', class_='author-bio-box')
if author_box:
    # Remove author image if present
    img = author_box.find('img')
    if img: img.decompose()
    h3 = author_box.find('h3')
    if h3:
        if h3.find('a'):
            h3.find('a').string = "Dr. Satya Vir Singh"
            h3.find('a')['href'] = "#"
        else:
            h3.string = "Dr. Satya Vir Singh"
    p = author_box.find('p')
    if p:
        p.string = "Dr. Satya Vir Singh is a Partner & Chief Experience Officer (CXO) at FretBox with over 25 years of global experience in Higher Education administration, operations, and technology across India, Central Asia, Africa, and the Gulf. He holds a Ph.D. in Computer Science and has been instrumental in university setup and strategic planning globally."

with open(os.path.join(dest_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(str(soup))

# Now update blogs/index.html
blogs_path = os.path.join(workspace, 'blogs', 'index.html')
with open(blogs_path, 'r', encoding='utf-8') as f:
    blogs_soup = BeautifulSoup(f.read(), 'html.parser')

# Update article count
page_meta = blogs_soup.find('div', class_='page-meta')
if page_meta:
    # '102 editorial guides' -> '103 editorial guides'
    m = re.search(r'(\d+)\s+editorial guides', page_meta.text)
    if m:
        new_count = int(m.group(1)) + 1
        page_meta.string = page_meta.text.replace(f"{m.group(1)} editorial guides", f"{new_count} editorial guides")

articles_grid = blogs_soup.find('div', class_='guide-grid')
new_card = f'''
<article class="guide-card">
<a aria-label="Read {title_text}" class="guide-card-image" href="/{slug}/">
<img alt="{title_text}" decoding="async" height="900" loading="lazy" src="/media/new-guides/{slug}-featured.webp" width="1600"/>
</a>
<div class="card-meta">
<span>India</span>
<span>7 min read</span>
</div>
<h3><a href="/{slug}/">{title_text}</a></h3>
<p>Hostel facilities are becoming an increasingly important part of the university experience in India. The Union Budget 2026–27 proposed establishing one girls' hostel in every district...</p>
<a class="text-link" href="/{slug}/">Read guide <span>→</span></a>
</article>
'''
new_card_soup = BeautifulSoup(new_card, 'html.parser')
articles_grid.insert(0, new_card_soup)

with open(blogs_path, 'w', encoding='utf-8') as f:
    f.write(str(blogs_soup))

print("Article generated successfully.")
