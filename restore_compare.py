import re
import os

updates = {
    'compare/james-ruse-vs-baulkham-hills/index.html': '''<section class="faq-section"><h2>Frequently Asked Questions About Sydney's Top Selective Schools</h2><details><summary>Is the academic pressure higher at James Ruse?</summary><p>James Ruse is famously known for its incredibly intense academic environment, heavily focused on accelerated mathematics and sciences. While Baulkham Hills also fosters a highly competitive cohort, some students and parents report that Baulkham Hills offers a slightly more balanced approach to extracurriculars and sports, though the HSC expectations remain exceptionally high at both institutions.</p></details><details><summary>How do the HSC results compare historically?</summary><p>James Ruse has maintained the number one position in the NSW HSC rankings for almost three decades consecutively, which is an unprecedented record. Baulkham Hills typically ranks securely within the top 5 (often 2nd or 3rd) in the state. Both schools routinely produce dozens of students who achieve a perfect 99.95 ATAR, making the academic distinction between the two practically negligible for top-tier students.</p></details><details><summary>Which school has better agricultural facilities?</summary><p>As an officially designated Agricultural High School, James Ruse has a fully functioning working farm on campus, and the study of agriculture is compulsory for all students in the junior years. Baulkham Hills does not have this agricultural focus or infrastructure, operating as a standard comprehensive-style selective school with traditional science labs and facilities.</p></details></section>''',

    'compare/mcgill-vs-university-of-toronto/index.html': '''<section class="faq-section"><h2>Frequently Asked Questions: McGill vs UofT</h2><details><summary>Which university has better global recognition?</summary><p>Both the University of Toronto (UofT) and McGill University enjoy elite global reputations. UofT typically ranks slightly higher in global commercial rankings (often in the top 20 worldwide) due to its massive research output and larger faculty. McGill (often top 40) is highly prestigious, particularly in the United States, where it is frequently dubbed the "Harvard of Canada" due to its rigorous academics and historic prestige.</p></details><details><summary>How does student life differ between Montreal and Toronto?</summary><p>This is often the deciding factor for students. Montreal (McGill) is widely considered one of the best student cities in the world—it is highly affordable, culturally rich, bilingual, and has a vibrant nightlife. Toronto (UofT) is Canada's financial capital, offering unparalleled corporate networking and internship opportunities, but it comes with an extraordinarily high cost of living and a more intense, commuter-heavy campus vibe.</p></details><details><summary>Is it harder to get high grades at UofT or McGill?</summary><p>Both universities are infamous in Canada for their rigorous grading curves and academic intensity, a phenomenon often referred to as "grade deflation." First-year life sciences and engineering at both institutions act as intense "weeder" programs. However, UofT's massive class sizes in the first two years often make students feel they must fight harder to stand out to professors.</p></details></section>''',

    'compare/oxford-vs-cambridge/index.html': '''<section class="faq-section"><h2>Frequently Asked Questions: Oxbridge Admissions</h2><details><summary>Should I apply to Oxford or Cambridge for Science?</summary><p>While both are world-leading, the University of Cambridge is historically and structurally more famous for the natural sciences and mathematics, boasting alumni like Newton, Darwin, and Hawking. Cambridge offers a unique "Natural Sciences" tripos that allows students to study a broad range of sciences before specializing. Oxford requires you to apply for a specific science (e.g., Chemistry or Physics) from day one.</p></details><details><summary>How does the college system differ between the two?</summary><p>The collegiate structures are fundamentally identical. Both universities are composed of dozens of independent colleges where students live, eat, and receive small-group teaching. Oxford calls its small-group teaching "tutorials" (usually 1-on-1 or 2-on-1), while Cambridge calls them "supervisions." The intensity and format of this pedagogical method are exactly the same.</p></details><details><summary>Which city is better for student life?</summary><p>Oxford is a slightly larger, busier, and more industrialized city with a slightly more urban feel. Cambridge is a smaller, quieter, and arguably more picturesque "market town" dominated entirely by the university and the River Cam. Both are deeply historic, heavily cycled, and incredibly expensive to live in.</p></details></section>''',

    'compare/usa-vs-uk-boarding-schools/index.html': '''<section class="faq-section"><h2>Frequently Asked Questions: Transatlantic Boarding</h2><details><summary>How do the academic systems compare?</summary><p>UK boarding schools typically follow the highly specialized A-Level (or occasionally IB) curriculum, where students narrow their focus to just 3 or 4 subjects in their final two years. US boarding schools follow a broader liberal arts high school diploma model, often incorporating Advanced Placement (AP) classes, requiring students to maintain breadth across math, science, humanities, and languages until graduation.</p></details><details><summary>Is there a difference in university admissions outcomes?</summary><p>Yes. UK boarding schools are explicitly engineered to prepare students for the UCAS system (Oxford, Cambridge, Russell Group), focusing heavily on deep, subject-specific academic mastery. US boarding schools are optimized for the holistic Ivy League admissions process, placing massive emphasis on leadership, varsity athletics, and multifaceted extracurricular profiles.</p></details><details><summary>Which system is more strict or traditional?</summary><p>Traditional UK boarding schools (like Eton or Harrow) retain many historic eccentricities, including highly formal uniforms (tailcoats), hierarchical prefect systems, and mandatory chapel attendance. US elite boarding schools (like Andover or Exeter) tend to feel more like small progressive liberal arts colleges, with looser dress codes, first-name basis with some faculty, and a highly discussion-based seminar culture.</p></details></section>''',

    'compare/harvard-vs-yale/index.html': '''<section class="faq-section"><h2>Frequently Asked Questions: The Big Three Rivalry</h2><details><summary>What is the difference in campus culture between Harvard and Yale?</summary><p>While both are highly elite, Yale is famously known for having a slightly more collaborative, arts-focused, and tightly knit undergraduate community, heavily anchored by its Residential College system. Harvard is often perceived as more intense, pre-professional, and heavily focused on individual ambition, proximity to Boston's biotech/political hubs, and its massive graduate schools.</p></details><details><summary>How do the residential systems compare?</summary><p>Both universities use a residential college system modeled after Oxford and Cambridge. Yale assigns students to one of 14 residential colleges before they arrive, and students generally stay affiliated with that college for all four years, creating deep loyalty. Harvard places all freshmen in Harvard Yard, and then sorts them into one of 12 upperclassman "Houses" for their final three years.</p></details><details><summary>Which school is better for STEM vs. Humanities?</summary><p>Yale is historically celebrated as a powerhouse for the humanities, literature, drama, and history. Harvard is also exceptional in the humanities but has invested billions in recent years into its engineering, computer science, and applied sciences facilities (like the new SEC complex in Allston), making it marginally stronger in quantitative and biotech fields.</p></details></section>'''
}

for filepath, new_content in updates.items():
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # 1. Remove the noindex tag
        html = re.sub(r'<meta name="robots" content="noindex, follow">\s*', '', html)
        
        # 2. Inject the expanded content before </article>
        if '</article>' in html and new_content not in html:
            html = html.replace('</article>', new_content + '\n</article>')
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated {filepath}")
    else:
        print(f"File not found: {filepath}")

# 3. Add them back to sitemap.xml
sitemap_urls = '''
<url>
  <loc>https://topschoolsrankings.com/compare/harvard-vs-yale/</loc>
  <lastmod>2026-09-24T12:00:00+00:00</lastmod>
  <priority>0.80</priority>
</url>
<url>
  <loc>https://topschoolsrankings.com/compare/james-ruse-vs-baulkham-hills/</loc>
  <lastmod>2026-09-24T12:00:00+00:00</lastmod>
  <priority>0.80</priority>
</url>
<url>
  <loc>https://topschoolsrankings.com/compare/mcgill-vs-university-of-toronto/</loc>
  <lastmod>2026-09-24T12:00:00+00:00</lastmod>
  <priority>0.80</priority>
</url>
<url>
  <loc>https://topschoolsrankings.com/compare/oxford-vs-cambridge/</loc>
  <lastmod>2026-09-24T12:00:00+00:00</lastmod>
  <priority>0.80</priority>
</url>
<url>
  <loc>https://topschoolsrankings.com/compare/usa-vs-uk-boarding-schools/</loc>
  <lastmod>2026-09-24T12:00:00+00:00</lastmod>
  <priority>0.80</priority>
</url>'''

with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()

if 'compare/harvard-vs-yale' not in sitemap:
    sitemap = sitemap.replace('</urlset>', sitemap_urls + '\n</urlset>')
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print("Added compare URLs back to sitemap.xml")