import os
from bs4 import BeautifulSoup

site_dir = 'c:/Users/Hp/Downloads/topschoolsrankings-new-site-upload-v2'

content_map = {
    'harvard-vs-yale': """<div class="rich-article-content">
<p><strong>Harvard University</strong> and <strong>Yale University</strong> are two of the most prestigious, recognized, and historically significant universities in the world. As founding members of the Ivy League, they offer world-class faculty, immense endowments, and unparalleled networking opportunities. However, for prospective students, choosing between Harvard and Yale often comes down to their distinct campus cultures, academic structures, and geographical settings.</p>
<h2>1. Location and Campus Vibe</h2>
<p><strong>Harvard</strong> is located in Cambridge, Massachusetts, just across the Charles River from Boston. It is deeply integrated into a bustling, intellectual city that is home to over 50 other colleges and universities (including MIT). The campus is vibrant, fast-paced, and urban.</p>
<p><strong>Yale</strong> is situated in New Haven, Connecticut. While New Haven is a smaller city, it offers a distinct collegiate atmosphere heavily influenced by Yale's Gothic architecture. Yale feels more enclosed and traditionally "collegiate," fostering a tight-knit campus community that heavily revolves around its residential college system.</p>
<h2>2. The Undergraduate Experience</h2>
<p>Yale is famous for its <strong>Residential College System</strong>. Every incoming freshman is assigned to one of 14 residential colleges, which become their social and living hub for all four years. This creates immediate micro-communities and intense loyalty.</p>
<p>Harvard also has a housing system (the House system), but students only enter it in their sophomore year after living in freshman dorms in Harvard Yard. While the House system is central to upperclassman life, Yale's system is often cited as being more foundational to the student experience from day one.</p>
<h2>3. Academic Strengths and Focus</h2>
<div class="table-scroll">
<table>
<thead><tr><th>Feature</th><th>Harvard University</th><th>Yale University</th></tr></thead>
<tbody>
<tr><td><strong>Curriculum</strong></td><td>Liberal Arts with a slight professional/graduate lean</td><td>Heavy focus on Undergraduate Humanities & Arts</td></tr>
<tr><td><strong>Popular Majors</strong></td><td>Economics, Government, Computer Science</td><td>Economics, Political Science, History</td></tr>
<tr><td><strong>Graduate Presence</strong></td><td>Massive graduate schools (Law, Med, Business)</td><td>Smaller graduate profile, heavily undergraduate-focused</td></tr>
<tr><td><strong>Arts & Drama</strong></td><td>Strong, but less centralized</td><td>World-renowned undergraduate drama and music scene</td></tr>
</tbody>
</table>
</div>
<h2>4. Admissions and Financial Aid</h2>
<p>Both universities boast acceptance rates consistently below 5%, making them ultra-selective. They both practice <strong>need-blind admissions</strong> for all students (including international applicants) and meet 100% of demonstrated financial need. Families earning under $85,000 typically pay nothing at either institution.</p>
<h2>5. Which Should You Choose?</h2>
<p>Choose <strong>Harvard</strong> if you thrive in a fast-paced, urban environment, want access to the broader Boston academic ecosystem, and are interested in heavily pre-professional tracks or politics.</p>
<p>Choose <strong>Yale</strong> if you prefer a close-knit, undergraduate-focused community, love Gothic architecture, and have a strong passion for the humanities, arts, or a slightly more collaborative (rather than competitive) campus culture.</p>
<h2>Frequently Asked Questions (FAQs)</h2>
<h3>Is Harvard harder to get into than Yale?</h3>
<p>Statistically, Harvard's acceptance rate (often around 3.2%) is slightly lower than Yale's (around 4.5%), but in practical terms, both are equally difficult to gain admission to. A student admitted to one is not guaranteed admission to the other, as institutional needs vary.</p>
<h3>Which school is better for STEM?</h3>
<p>Harvard generally has a larger footprint in STEM research, particularly in the biomedical sciences due to its proximity to the Boston medical hub and MIT. However, Yale has recently invested billions into expanding its science and engineering facilities.</p>
</div>""",

    'james-ruse-vs-baulkham-hills': """<div class="rich-article-content">
<p><strong>James Ruse Agricultural High School</strong> and <strong>Baulkham Hills High School</strong> are two of the most academically elite selective schools in New South Wales (NSW), Australia. Year after year, these two giants dominate the HSC (Higher School Certificate) rankings, producing some of the highest ATARs in the state. Deciding between them involves looking at academic intensity, extracurricular offerings, and the specific agricultural curriculum.</p>
<h2>1. Academic Performance and HSC Rankings</h2>
<p>For over two decades, <strong>James Ruse</strong> held the undisputed title of the #1 school in NSW based on HSC results. Its students consistently achieve exceptional ATARs, heavily dominating in high-level Mathematics and Sciences. <strong>Baulkham Hills</strong> is historically a top 5 school, frequently placing 2nd or 3rd in the state, offering a robust challenge to Ruse's dominance.</p>
<h2>2. The Agricultural Component</h2>
<p>As an agricultural high school, James Ruse has a mandatory agricultural curriculum in the junior years (Years 7-10). Students must participate in practical farm work, including caring for crops and livestock on the school's working farm. Baulkham Hills is a standard academically selective high school and does not have this mandatory agricultural component.</p>
<h2>3. School Culture and Environment</h2>
<div class="table-scroll">
<table>
<thead><tr><th>Feature</th><th>James Ruse</th><th>Baulkham Hills</th></tr></thead>
<tbody>
<tr><td><strong>Location</strong></td><td>Carlingford, NSW</td><td>Baulkham Hills, NSW</td></tr>
<tr><td><strong>Type</strong></td><td>Co-educational, Selective Agricultural</td><td>Co-educational, Fully Selective</td></tr>
<tr><td><strong>Academic Culture</strong></td><td>Intensely competitive, highly focused on STEM</td><td>Highly academic but often described as slightly more balanced</td></tr>
<tr><td><strong>Extracurriculars</strong></td><td>Strong in Cadets, Olympiads, and Music</td><td>Strong in Sports, Debating, and Leadership</td></tr>
</tbody>
</table>
</div>
<h2>4. Wellbeing and Extracurriculars</h2>
<p>Both schools are known for their high-pressure environments. However, both have actively expanded their wellbeing programs in recent years. Baulkham Hills is often praised by parents for maintaining a slightly more relaxed atmosphere compared to the intense academic pressure cooker that James Ruse is historically known for, though this varies heavily by student cohort.</p>
<h2>Frequently Asked Questions (FAQs)</h2>
<h3>Do you have to study Agriculture for the HSC at James Ruse?</h3>
<p>No. While Agriculture is compulsory in Years 7 to 10, it becomes an elective subject for the HSC in Years 11 and 12.</p>
<h3>Which school is better for humanities?</h3>
<p>While both schools excel in STEM, Baulkham Hills often fields very strong results in humanities subjects like English Advanced, History, and Economics, offering a slightly broader focus.</p>
</div>""",

    'mcgill-vs-university-of-toronto': """<div class="rich-article-content">
<p><strong>McGill University</strong> (in Montreal) and the <strong>University of Toronto</strong> (U of T) are Canada's top two internationally ranked research universities. Both attract top-tier students from around the globe, but they offer vastly different student experiences, geographic advantages, and campus cultures.</p>
<h2>1. City and Location</h2>
<p><strong>U of T</strong> is located in the heart of downtown Toronto, Canada's largest city and financial capital. The city is sprawling, multicultural, and deeply integrated into the global economy.</p>
<p><strong>McGill</strong> is situated in downtown Montreal, Quebec. Montreal is famously bilingual (French and English), culturally vibrant, and known for its European flair, affordability, and incredibly active student life.</p>
<h2>2. Academic Structure and Prestige</h2>
<p>U of T is a massive institution with a federated college system (similar to Oxford or Cambridge) at its St. George campus. It boasts the largest research network and library system in Canada. It consistently ranks as the #1 university in Canada in global league tables.</p>
<p>McGill is slightly smaller (though still large) and is often referred to as the "Harvard of the North." It is highly prestigious, particularly in medicine, law, and international relations. McGill holds the record for the highest percentage of international students among Canada's top research universities.</p>
<div class="table-scroll">
<table>
<thead><tr><th>Factor</th><th>University of Toronto</th><th>McGill University</th></tr></thead>
<tbody>
<tr><td><strong>Location</strong></td><td>Toronto, Ontario</td><td>Montreal, Quebec</td></tr>
<tr><td><strong>Global Ranking (approx.)</strong></td><td>Top 25 globally</td><td>Top 35 globally</td></tr>
<tr><td><strong>Cost of Living</strong></td><td>Very High (Toronto real estate)</td><td>Moderate to Low (Highly affordable student city)</td></tr>
<tr><td><strong>Language</strong></td><td>Strictly English</td><td>English university in a French-speaking province</td></tr>
</tbody>
</table>
</div>
<h2>3. Cost and Affordability</h2>
<p>One of the biggest deciding factors is cost. Tuition for international students at U of T has become exceptionally high, often exceeding $60,000 CAD per year. McGill's international tuition is also high but generally slightly lower than U of T's. More importantly, the cost of living (rent, food, nightlife) in Montreal is significantly cheaper than in Toronto.</p>
<h2>4. Which Should You Choose?</h2>
<p>Choose <strong>U of T</strong> if you want unparalleled research resources, access to Bay Street (finance) and Toronto's tech hub, and prefer a massive, modern metropolis.</p>
<p>Choose <strong>McGill</strong> if you want a more affordable, culturally rich, bilingual city experience, a highly international student body, and a strong "college town" vibe within a major city.</p>
<h2>Frequently Asked Questions (FAQs)</h2>
<h3>Do I need to speak French to attend McGill?</h3>
<p>No. McGill is an English-language university, and all classes (except language courses) are taught in English. However, knowing some conversational French is highly beneficial for navigating the city of Montreal and securing off-campus employment.</p>
</div>""",

    'oxford-vs-cambridge': """<div class="rich-article-content">
<p>The University of <strong>Oxford</strong> and the University of <strong>Cambridge</strong> (collectively known as "Oxbridge") are the two oldest, wealthiest, and most famous universities in the United Kingdom. Deciding between them is a luxury few have, but because you can only apply to <strong>one</strong> per year through UCAS, you must make your choice carefully.</p>
<h2>1. Course Differences</h2>
<p>The most important factor in choosing between Oxford and Cambridge is the course structure. While both offer world-class tutorials/supervisions, the subjects themselves differ:</p>
<ul>
<li><strong>Cambridge</strong> offers the <em>Natural Sciences</em> Tripos, allowing students to study a broad range of sciences in their first year before specializing. <strong>Oxford</strong> requires you to apply for a specific science (e.g., Biology, Chemistry, Physics) from day one.</li>
<li><strong>Oxford</strong> is famous for <em>PPE (Philosophy, Politics and Economics)</em>, a course that has produced numerous UK Prime Ministers. Cambridge offers Human, Social, and Political Sciences (HSPS) instead.</li>
<li><strong>Cambridge</strong> is widely considered the slightly stronger choice for pure Mathematics and Engineering, while <strong>Oxford</strong> often takes the edge in Humanities and Classics.</li>
</ul>
<h2>2. The Towns: Oxford vs. Cambridge</h2>
<p><strong>Oxford</strong> is a larger, busier city with more industry and traffic. It feels more urban, though the university buildings dominate the center. <strong>Cambridge</strong> is a smaller, quieter, and more picturesque market town, heavily defined by the River Cam and the "Backs" (the backs of the colleges facing the river).</p>
<div class="table-scroll">
<table>
<thead><tr><th>Feature</th><th>Oxford</th><th>Cambridge</th></tr></thead>
<tbody>
<tr><td><strong>Teaching Style</strong></td><td>Tutorials (usually 1-on-2)</td><td>Supervisions (usually 1-on-2)</td></tr>
<tr><td><strong>Admissions Tests</strong></td><td>Mostly standard university-wide tests (e.g., TSA, MAT)</td><td>Often college-specific or pre-interview assessments</td></tr>
<tr><td><strong>Vibe</strong></td><td>Busy, historical, slightly larger city</td><td>Quiet, fenland town, highly concentrated campus feel</td></tr>
</tbody>
</table>
</div>
<h2>3. The Collegiate System</h2>
<p>Both universities use a collegiate system. You apply to and live in a specific College (e.g., Christ Church at Oxford or Trinity at Cambridge). Your college handles your accommodation, pastoral care, and small-group teaching, while the central University provides the lectures, labs, and ultimately, your degree.</p>
<h2>Frequently Asked Questions (FAQs)</h2>
<h3>Can I apply to both Oxford and Cambridge in the same year?</h3>
<p>No. UCAS regulations prohibit applying to both Oxford and Cambridge in the same admissions cycle for undergraduate degrees. You must choose one.</p>
<h3>Which one is harder to get into?</h3>
<p>Both have overall acceptance rates around 15-18%. However, Cambridge tends to interview a higher percentage of its applicants (around 70%) and uses the interview as a major filtering tool, while Oxford heavily filters applicants prior to the interview stage using admissions tests and GCSE grades, interviewing only about 20-30% of applicants.</p>
</div>""",

    'usa-vs-uk-boarding-schools': """<div class="rich-article-content">
<p>For international families seeking elite secondary education, the choice often comes down to the historic <strong>UK Boarding Schools</strong> (such as Eton, Harrow, or Winchester) and the prestigious <strong>USA Boarding Schools</strong> (such as Phillips Exeter, Andover, or Choate). Both pathways offer exceptional resources, but their educational philosophies and university outcomes differ drastically.</p>
<h2>1. Curriculum and Academic Philosophy</h2>
<p><strong>UK Boarding Schools</strong> focus on early specialization. Students take GCSEs around age 16 and then narrow their focus to just 3 or 4 subjects for their A-Levels. This creates deep subject-matter experts who are prepared for the specialized nature of UK universities.</p>
<p><strong>USA Boarding Schools</strong> emphasize a broad, liberal arts education. Students take a wide variety of subjects through 12th grade, often including Advanced Placement (AP) courses. This broad foundation is designed to prepare students for the holistic admissions process of Ivy League and US colleges.</p>
<h2>2. Culture and Environment</h2>
<p>UK schools are steeped in centuries of tradition, featuring house systems, formal uniforms (sometimes including tailcoats), and strong hierarchical structures (prefects, head boys/girls). They place a heavy emphasis on pastoral care within the boarding house.</p>
<p>US boarding schools feel more like small liberal arts colleges. They feature modern facilities, a strong emphasis on student-led clubs and activism, and highly competitive athletics. Uniforms are rare, though dress codes exist.</p>
<div class="table-scroll">
<table>
<thead><tr><th>Factor</th><th>UK Boarding Schools</th><th>US Boarding Schools</th></tr></thead>
<tbody>
<tr><td><strong>Curriculum</strong></td><td>GCSEs and A-Levels (Early Specialization)</td><td>US High School Diploma + APs (Broad Liberal Arts)</td></tr>
<tr><td><strong>Teaching Style</strong></td><td>Traditional, rigorous, exam-focused</td><td>Discussion-based (Harkness method), continuous assessment</td></tr>
<tr><td><strong>University Pathway</strong></td><td>Direct feed into Oxbridge and Russell Group</td><td>Direct feed into Ivy League and Elite US Colleges</td></tr>
<tr><td><strong>Vibe</strong></td><td>Traditional, structured, heritage-focused</td><td>Progressive, collegiate, resource-heavy</td></tr>
</tbody>
</table>
</div>
<h2>3. The "Harkness" Table vs. Traditional Teaching</h2>
<p>Many elite US boarding schools (pioneered by Phillips Exeter) use the <strong>Harkness Method</strong>, where 12 students sit around an oval table and lead discussions with the teacher acting only as a moderator. UK schools, while highly interactive, still tend to rely more on traditional classroom instruction and lecture formats to prepare students for high-stakes A-Level exams.</p>
<h2>4. Which Pathway is Right?</h2>
<p>Choose the <strong>UK</strong> if your child knows exactly what they want to study (e.g., Medicine, Law) and prefers structured, tradition-rich environments. Choose the <strong>USA</strong> if your child is intellectually curious across many subjects, excels in continuous assessment rather than just final exams, and is targeting US universities.</p>
<h2>Frequently Asked Questions (FAQs)</h2>
<h3>Are US boarding schools more expensive than UK boarding schools?</h3>
<p>Yes. Elite US boarding schools currently cost upwards of $65,000 to $70,000 USD per year. UK boarding schools typically charge around &pound;40,000 to &pound;50,000 GBP per year. However, top US schools often have massive endowments and can offer generous need-based financial aid, even to international students, which is less common in the UK.</p>
</div>"""
}

# Process each file
for slug, new_content in content_map.items():
    filepath = os.path.join(site_dir, 'compare', slug, 'index.html')
    
    with open(filepath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    article_body = soup.find('article', class_='article-body')
    if article_body:
        rich_content = article_body.find('div', class_='rich-article-content')
        if rich_content:
            # We want to replace the ENTIRE div.rich-article-content with our new content.
            # BeautifulSoup makes it easy:
            new_soup = BeautifulSoup(new_content, 'html.parser')
            rich_content.replace_with(new_soup)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Updated content for {slug}")
        else:
            print(f"Could not find rich-article-content in {slug}")
    else:
        print(f"Could not find article-body in {slug}")
