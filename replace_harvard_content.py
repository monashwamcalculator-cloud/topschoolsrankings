import re

with open('harvard-university-admissions-guide-for-international-students/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<div class="rich-article-content">'
end_marker = '</div>\n<div class="author-bio-box"'
end_marker_fallback = '</div>\n  <div class="author-bio-box"'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)
if end_idx == -1:
    end_idx = html.find(end_marker_fallback)

new_content = '''<div class="rich-article-content">
  <p><strong>Harvard University admissions guide for international students (2026)</strong> — This independent editorial guide helps international applicants navigate Harvard College’s highly competitive admissions process. We break down the application timeline, testing requirements, and Harvard's exceptional financial aid policies.</p>
  
  <p><strong>Please note:</strong> This is an independent research guide compiled by Top Schools Rankings. We are not affiliated with, nor officially endorsed by, Harvard University. Always verify deadlines, fees, and requirements directly on the official <a href="https://college.harvard.edu/admissions" target="_blank" rel="noopener noreferrer">Harvard College Admissions website</a>.</p>

  <h2>Latest Official Harvard Admissions Data</h2>
  <p>Harvard College admissions are extraordinarily competitive. The table below reflects the latest verified statistics published by the Harvard Office of Institutional Research &amp; Analytics for recent incoming classes.</p>
  <table>
    <thead>
      <tr><th>Class year</th><th>Applicants</th><th>Admitted</th><th>Admit rate</th><th>Yield rate</th></tr>
    </thead>
    <tbody>
      <tr><td>2029</td><td>47,893</td><td>2,003</td><td>4.2%</td><td>83.6%</td></tr>
      <tr><td>2028</td><td>54,008</td><td>1,970</td><td>3.6%</td><td>83.6%</td></tr>
      <tr><td>2027</td><td>56,937</td><td>1,965</td><td>3.5%</td><td>83.7%</td></tr>
      <tr><td>2026</td><td>61,221</td><td>1,984</td><td>3.2%</td><td>83.0%</td></tr>
    </tbody>
  </table>
  <p><em>Source: Harvard Office of Institutional Research &amp; Analytics Fact Book.</em></p>

  <h2>Harvard Application Process &amp; Timeline</h2>
  <p>International students apply to Harvard College using the same process as US citizens, primarily through the <strong>Common Application</strong> or the <strong>Coalition Application</strong>. There are no separate international quotas or caps.</p>
  <table>
    <thead>
      <tr><th>Stage</th><th>Typical timing</th><th>What to do</th></tr>
    </thead>
    <tbody>
      <tr><td>Restrictive Early Action (REA)</td><td>Apply early November; decisions mid-December</td><td>Only if Harvard is your clear first choice. You may not apply early to any other private US university.</td></tr>
      <tr><td>Regular Decision</td><td>Apply early January; decisions late March (Ivy Day)</td><td>The standard application timeline for the vast majority of applicants.</td></tr>
      <tr><td>Financial aid forms</td><td>Align with CSS Profile / institutional deadlines</td><td>Submit your CSS Profile on time to ensure you receive an aid estimate with your admissions decision.</td></tr>
      <tr><td>Enrollment reply</td><td>Typically May 1</td><td>Compare offers before committing.</td></tr>
    </tbody>
  </table>

  <h2>Standardized Testing &amp; English Proficiency</h2>
  <ul>
    <li><strong>SAT / ACT Requirement:</strong> Harvard reinstated its standardized testing requirement for incoming classes. You must submit SAT or ACT scores (or approved alternatives if applying from regions where these tests are inaccessible).</li>
    <li><strong>English Proficiency:</strong> While Harvard does not rigidly require the TOEFL, IELTS, or Duolingo English Test, international students whose native language is not English and who have not attended an English-speaking secondary school are strongly encouraged to submit scores to demonstrate fluency.</li>
  </ul>

  <h2>Harvard Financial Aid for International Students</h2>
  <p>This is one of the most critical advantages for international applicants: <strong>Harvard’s financial aid policies are completely need-blind for all students, regardless of citizenship.</strong></p>
  <ul>
    <li>Applying for financial aid will <strong>never</strong> negatively impact an international student’s chance of admission.</li>
    <li>Harvard commits to meeting <strong>100% of demonstrated financial need</strong> for all admitted students, including international students.</li>
    <li>There are no merit-based scholarships at Harvard; all aid is based entirely on financial need.</li>
  </ul>
  <p>Families with annual incomes below specific thresholds (often around ,000 USD) typically pay nothing for tuition, room, or board. Always use the Net Price Calculator and review official policies on the <a href="https://college.harvard.edu/financial-aid" target="_blank" rel="noopener noreferrer">Harvard Financial Aid website</a>.</p>

  <h2>Estimated Cost of Attendance (Planning Table)</h2>
  <p>If a family does not qualify for need-based aid, the "sticker price" applies. However, a significant majority of Harvard students receive financial assistance.</p>
  <table>
    <thead>
      <tr><th>Cost line (indicative)</th><th>Planning range (USD / year)</th><th>Notes</th></tr>
    </thead>
    <tbody>
      <tr><td>Tuition</td><td>~,000+</td><td>Billed directly by the university.</td></tr>
      <tr><td>Room, board &amp; fees</td><td>~,000 &ndash; ,000+</td><td>Mandatory for first-year students living on campus.</td></tr>
      <tr><td>Books &amp; personal expenses</td><td>~,000 &ndash; ,000</td><td>Estimated variable costs.</td></tr>
      <tr><td>Total before aid</td><td>Often <strong>,000+</strong></td><td>Many aided families pay significantly less, or nothing at all.</td></tr>
    </tbody>
  </table>

  <h2>How to Strengthen Your Application (Checklist)</h2>
  <ol>
    <li><strong>Academic Rigor:</strong> Maximize the hardest courses available in your national curriculum (e.g., A-Levels, IB Diploma, APs, French Baccalaureate). Harvard evaluates your grades in the context of what your specific school offers.</li>
    <li><strong>Extracurricular Depth:</strong> Harvard looks for sustained leadership, exceptional talent, or deep community impact. A long list of superficial club memberships is less effective than significant dedication to two or three core passions.</li>
    <li><strong>Teacher Recommendations:</strong> Choose teachers who can speak specifically to your intellectual curiosity and classroom contributions.</li>
    <li><strong>Alumni Interview:</strong> If offered, the alumni interview is a chance to add dimension to your application. Because international interview availability varies by country, not being offered an interview will not penalize your application.</li>
  </ol>

  <figure>
    <img src="/media/articles/top-50-universities-in-usa-inline-03.webp" alt="Students reviewing education choices using evidence and official information" width="1400" height="933" loading="lazy" decoding="async">
    <figcaption>Harvard evaluates applicants holistically, balancing academic excellence with personal character and extracurricular impact.</figcaption>
  </figure>

  <h2>FAQs: Harvard University Admissions (2026)</h2>
  <h3>What is Harvard's acceptance rate?</h3>
  <p>Harvard's acceptance rate historically hovers between 3% and 4%. For the Class of 2029, the official admit rate was 4.2%.</p>
  
  <h3>Does Harvard require the SAT or ACT for international students?</h3>
  <p>Yes. Harvard has reinstated its standardized testing requirement. International students must submit SAT or ACT scores, subject to specific regional exceptions outlined on their official site.</p>
  
  <h3>Is Harvard need-blind for international students?</h3>
  <p>Yes. Harvard is one of only a handful of US universities that is strictly need-blind for all international applicants and guarantees to meet 100% of demonstrated financial need.</p>
  
  <h3>Are there separate international quotas?</h3>
  <p>No. Harvard does not use quotas or caps for specific countries or regions; international students are evaluated in the same holistic pool as domestic applicants.</p>
  
  <h3>How can I get an application fee waiver?</h3>
  <p>If the application fee presents a financial hardship, international students can request a fee waiver directly through the Common Application or Coalition Application. Harvard is committed to ensuring application fees do not prevent any student from applying.</p>

  <p><em>Disclaimer: Admissions policies, testing requirements, and tuition fees change. This guide summarizes publicly available data for planning purposes only. Confirm all details directly on college.harvard.edu before applying.</em></p>
</div>'''

if start_idx != -1 and end_idx != -1:
    final_html = html[:start_idx] + new_content + html[end_idx:]
    with open('harvard-university-admissions-guide-for-international-students/index.html', 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Successfully replaced content.")
else:
    print(f"Could not find markers for replacement. start: {start_idx}, end: {end_idx}")