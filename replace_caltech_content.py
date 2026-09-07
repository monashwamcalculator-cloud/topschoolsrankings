import re

with open('california-institute-of-technology-acceptance-rate-2026-how-hard-is-it-to-get-into-caltech/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<div class="rich-article-content">'
end_marker = '</div>\n<div class="author-bio-box"'
end_marker_fallback = '</div>\n  <div class="author-bio-box"'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)
if end_idx == -1:
    end_idx = html.find(end_marker_fallback)

new_content = '''<div class="rich-article-content">
  <p><strong>California Institute of Technology (Caltech) Admissions Guide</strong> &mdash; This independent editorial guide helps prospective applicants understand the intense selectivity, academic prerequisites, and international student policies at Caltech.</p>
  
  <p><strong>Please note:</strong> This is an independent research guide compiled by Top Schools Rankings. We are not affiliated with, nor officially endorsed by, the California Institute of Technology. Always verify deadlines, statistics, and requirements directly on the official <a href="https://admissions.caltech.edu/" target="_blank" rel="noopener noreferrer">Caltech Undergraduate Admissions website</a>.</p>

  <h2>How Hard is it to Get Into Caltech?</h2>
  <p>The short answer: <strong>Extremely hard.</strong> Caltech is widely considered one of the most rigorous and selective STEM-focused universities in the world.</p>
  <p>Unlike larger research universities, Caltech intentionally maintains a microscopic undergraduate population, typically enrolling an incoming freshman class of roughly 225 to 235 students. Because global interest in elite STEM education continues to grow, this small class size naturally creates an intensely competitive admissions environment.</p>

  <h3>Latest Acceptance Rate Data</h3>
  <p>It is crucial not to confuse historical estimates with current data. For recent admissions cycles (such as the Class of 2028), Caltech received over 13,000 applications and admitted slightly over 300 students, resulting in an overall acceptance rate hovering <strong>between 2% and 3%</strong>.</p>
  <p>This statistical bottleneck makes Caltech quantitatively harder to enter than almost every Ivy League university.</p>

  <figure class="editorial-figure">
    <img src="/media/articles/top-50-universities-in-usa-inline-03.webp" alt="Students reviewing education choices using evidence and official information" width="1400" height="933" loading="lazy" decoding="async">
    <figcaption>Caltech evaluates applicants on profound quantitative ability and a deep, demonstrated passion for STEM.</figcaption>
  </figure>

  <h2>Caltech Academic Prerequisites (2026 Update)</h2>
  <p>You cannot simply have a high GPA to be admitted to Caltech. The institute enforces exceptionally strict academic prerequisites. If you do not meet these minimums in high school, your application will not be competitive.</p>
  <ul>
    <li><strong>Mandatory Calculus:</strong> You must have completed a full year of calculus before graduating high school.</li>
    <li><strong>Mandatory Physics and Chemistry:</strong> You must have completed a full year of physics and a full year of chemistry.</li>
    <li><strong>Standardized Testing (Test-Required):</strong> Caltech has reinstated its standardized testing requirement. All first-year applicants must submit either an <strong>SAT or ACT</strong> score.</li>
  </ul>

  <h2>International Student Admissions at Caltech</h2>
  <p>International applicants are evaluated under the same rigorous academic standards as domestic students, but face a uniquely challenging admissions and financial aid landscape.</p>
  <ul>
    <li><strong>English Proficiency:</strong> If English is not your native language, or if English was not the primary language of instruction at your secondary school, Caltech strongly recommends submitting scores from the Duolingo English Test (DET) or the TOEFL.</li>
    <li><strong>Need-Aware Admissions:</strong> Unlike some of its elite peers (such as MIT or Harvard), Caltech is <strong>need-aware</strong> for international applicants during the admissions process. This means a family's ability to pay may be factored into the admissions decision for non-US citizens.</li>
    <li><strong>100% Demonstrated Need Met:</strong> Despite being need-aware during the application read, if an international student is admitted and applies for financial aid, Caltech guarantees to meet <strong>100% of their demonstrated financial need</strong>.</li>
  </ul>

  <h2>Why is Caltech so Selective?</h2>
  <ol>
    <li><strong>Microscopic Class Size:</strong> Enrolling roughly 230 students per year means there is no room to admit applicants who are merely "good." Every admitted student must show exceptional potential for scientific discovery.</li>
    <li><strong>STEM-Only Focus:</strong> Caltech's curriculum is relentlessly focused on math, physics, engineering, and the sciences. Every student, regardless of major, must pass the rigorous Core Curriculum, which includes advanced calculus, classical mechanics, electromagnetism, chemistry, and biology.</li>
    <li><strong>Research DNA:</strong> Caltech manages the Jet Propulsion Laboratory (JPL) for NASA and operates numerous global observatories. They look for applicants who have already demonstrated an authentic passion for research, often through Science Olympiads, independent lab work, or high-level coding projects.</li>
  </ol>

  <h2>Caltech Application Deadlines (2026–2027 Cycle)</h2>
  <p>Applying to Caltech requires careful planning. Always verify the exact calendar dates for the current application cycle on the official Caltech admissions site.</p>
  <ul>
    <li><strong>Restrictive Early Action (REA):</strong> Typically due <strong>November 1</strong>. This is non-binding, but if you apply REA to Caltech, you may not apply Early Action or Early Decision to any other private US university.</li>
    <li><strong>Regular Decision (RD):</strong> Typically due <strong>January 3</strong>. This is the standard timeline for the majority of the applicant pool.</li>
    <li><strong>Financial Aid Deadlines:</strong> The CSS Profile and related financial documents are usually due around the same time as the application. Submitting these late can jeopardize your aid package.</li>
  </ul>

  <h2>FAQs About Caltech Admissions</h2>
  <h3>Is Caltech harder to get into than MIT?</h3>
  <p>Statistically, yes. Because Caltech's freshman class is roughly one-quarter the size of MIT's, its acceptance rate often dips below 3%, making it quantitatively more selective, though both seek the highest caliber of STEM talent in the world.</p>

  <h3>Does Caltech require the SAT or ACT?</h3>
  <p>Yes. Caltech officially reinstated the SAT/ACT requirement for undergraduate admissions. All applicants must submit valid test scores.</p>

  <h3>Is Caltech need-blind for international students?</h3>
  <p>No. Caltech is <strong>need-aware</strong> for international applicants during the admissions process. However, if admitted, Caltech will meet 100% of your demonstrated financial need.</p>

  <h3>Can I apply to Caltech without taking Calculus?</h3>
  <p>No. One full year of high school calculus is a strict, non-negotiable prerequisite for admission.</p>

  <p><em>Disclaimer: Admissions policies, deadlines, and financial aid rules are subject to change. This guide summarizes publicly available data for planning purposes only. Confirm all details directly on admissions.caltech.edu and finaid.caltech.edu before applying.</em></p>
</div>'''

if start_idx != -1 and end_idx != -1:
    final_html = html[:start_idx] + new_content + html[end_idx:]
    with open('california-institute-of-technology-acceptance-rate-2026-how-hard-is-it-to-get-into-caltech/index.html', 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Successfully replaced content.")
else:
    print(f"Could not find markers for replacement. start: {start_idx}, end: {end_idx}")