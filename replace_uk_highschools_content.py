import re

with open('top-high-schools-in-england-rankings-guide/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<div class="rich-article-content">'
end_marker = '</div>\n<div class="author-bio-box"'
end_marker_fallback = '</div>\n  <div class="author-bio-box"'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)
if end_idx == -1:
    end_idx = html.find(end_marker_fallback)

new_content = '''<div class="rich-article-content">
  <p><strong>Top High Schools in England Rankings Guide (2026)</strong> &mdash; This independent editorial guide by TopSchoolsRankings helps families navigate the competitive secondary education landscape in England. We explain how league tables work, the differences between state grammars and independent schools, and what international applicants need to know.</p>
  
  <p><strong>Please note:</strong> This is an independent research guide. TopSchoolsRankings is not affiliated with, nor officially endorsed by, the UK Department for Education (DfE), Ofsted, The Sunday Times (Parent Power), or any listed school. Ranking data discussed below references publicly available 2025/2026 performance metrics and should be used only as a starting point for your research.</p>

  <h2>Understanding UK School Rankings &amp; League Tables</h2>
  <p>In England, there is no single "official" ranking of the top 100 schools. Instead, parents rely on two primary sources of information to evaluate secondary schools (high schools):</p>
  <ol>
    <li><strong>Government Performance Data (DfE):</strong> The Department for Education publishes objective exam metrics, most notably <strong>Progress 8</strong> (how much value a school adds from age 11 to 16) and <strong>Attainment 8</strong> (raw GCSE scores). These tables primarily cover state-funded schools.</li>
    <li><strong>Editorial League Tables:</strong> Publications like <em>The Sunday Times Parent Power</em> create blended rankings by combining GCSE (Grade 9-7) and A-Level (A*-B) results across both state and independent (fee-paying) schools.</li>
  </ol>
  <p><strong>Ofsted Inspections vs. Rankings:</strong> Do not confuse Ofsted ratings with exam league tables. Ofsted is the government body that inspects state schools for safeguarding, teaching quality, and leadership, awarding grades from "Outstanding" to "Inadequate." A school can be ranked #1 for exam results but face criticism in an Ofsted report for pastoral care, or vice versa.</p>

  <figure>
    <img src="/media/articles/top-10-uk-universities-for-international-students-inline-03.webp" alt="Historic English school architecture" width="1400" height="933" loading="lazy" decoding="async">
    <figcaption>Top English schools range from historic independent boarding schools to highly selective state grammars.</figcaption>
  </figure>

  <h2>School Types in the Elite Tiers</h2>
  <p>When reviewing any top 100 list in England, you will encounter three distinct types of secondary schools:</p>
  <table>
    <thead>
      <tr><th>Feature</th><th>Independent (Private)</th><th>Grammar (State Selective)</th><th>Comprehensive (State)</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>Funding</strong></td><td>Fee-paying (&pound;20,000 &ndash; &pound;50,000+/year)</td><td>State-funded (Free tuition)</td><td>State-funded (Free tuition)</td></tr>
      <tr><td><strong>Admissions</strong></td><td>Internal exams, interviews, ISEB</td><td>11+ selective entrance exams</td><td>Usually catchment-area based</td></tr>
      <tr><td><strong>Demographics</strong></td><td>Nationwide &amp; International</td><td>Specific regions (e.g., Kent, Bucks)</td><td>Nationwide in all local authorities</td></tr>
    </tbody>
  </table>

  <h2>The Regional Divide</h2>
  <p>Top exam results in England are heavily clustered in specific regions:</p>
  <ul>
    <li><strong>London &amp; The South East:</strong> This region overwhelmingly dominates national league tables. It houses elite independent day schools (like St Paul's School and Westminster School) and the most competitive state grammars (like Queen Elizabeth's School in Barnet and The Henrietta Barnett School).</li>
    <li><strong>The Rest of England:</strong> Grammar schools are not evenly distributed. Large parts of the country have zero state grammar schools. Families outside grammar regions looking for top-tier exam results often have to rely on independent schools or highly rated local comprehensives.</li>
  </ul>

  <h2>Fees for Independent Schools (2025&ndash;2026)</h2>
  <p>If you are targeting an independent school, expect significant costs. Always verify the current academic year's fee schedule on the official school website.</p>
  <table>
    <thead>
      <tr><th>School Type</th><th>Estimated Annual Fees (GBP)</th></tr>
    </thead>
    <tbody>
      <tr><td>London Independent Day Schools</td><td>&pound;25,000 &ndash; &pound;35,000+ per year</td></tr>
      <tr><td>Regional Independent Day Schools</td><td>&pound;16,000 &ndash; &pound;26,000+ per year</td></tr>
      <tr><td>Full Boarding (Major Public Schools)</td><td>&pound;45,000 &ndash; &pound;55,000+ per year</td></tr>
    </tbody>
  </table>
  <p><em>Note: Many independent schools offer means-tested bursaries to widen access, though competition for these funds is fierce.</em></p>

  <h2>Admissions Information for International Students</h2>
  <p>International families relocating to the UK face specific admissions hurdles:</p>
  <ul>
    <li><strong>State Grammars:</strong> Generally, you must have UK residency and live within the specific local authority catchment area to apply for a state grammar school. You cannot secure a grammar school place while living overseas.</li>
    <li><strong>Independent Boarding Schools:</strong> For international families without UK residency, independent boarding schools (like Eton, Harrow, Winchester, or Wycombe Abbey) are the standard route. These schools are highly experienced in international admissions and typically sponsor <strong>Child Student Visas</strong>.</li>
    <li><strong>English Proficiency:</strong> Top independent schools require near-fluent English, often assessing this through their own entrance exams or standardized tests like UKiset.</li>
  </ul>

  <h2>Frequently Asked Questions</h2>
  <h3>What is the number one high school in England?</h3>
  <p>There is no single official answer. In recent independent editorial rankings (like The Sunday Times Parent Power), <strong>St Paul's School</strong> (independent) and <strong>Queen Elizabeth's School, Barnet</strong> (state grammar) frequently take the top spots based on their exceptionally high percentages of A*&ndash;A grades at A-Level and 9&ndash;7 grades at GCSE.</p>

  <h3>Does a top ranking guarantee a place at Oxford or Cambridge?</h3>
  <p>No. While schools at the top of these tables send dozens of students to Oxbridge annually, university admissions in the UK are entirely merit-based on individual A-Level predictions, entrance exams (like the UCAT, LNAT, or MAT), and academic interviews.</p>

  <h3>How do I verify official school performance?</h3>
  <p>Do not rely solely on commercial league tables. You should verify any state school's exam results and student progression data using the UK Government's official <a href="https://www.compare-school-performance.service.gov.uk/" target="_blank" rel="noopener noreferrer">Compare School Performance service</a>. You can also read their latest inspection reports directly on the <a href="https://reports.ofsted.gov.uk/" target="_blank" rel="noopener noreferrer">Ofsted website</a>.</p>

  <p><em>Disclaimer: School fees, admission rules, and academic performance change annually. This guide summarizes publicly available data for planning purposes only. Confirm all details directly with the individual schools and official government sources before making educational decisions.</em></p>
</div>'''

if start_idx != -1 and end_idx != -1:
    final_html = html[:start_idx] + new_content + html[end_idx:]
    with open('top-high-schools-in-england-rankings-guide/index.html', 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Successfully replaced content.")
else:
    print(f"Could not find markers for replacement. start: {start_idx}, end: {end_idx}")