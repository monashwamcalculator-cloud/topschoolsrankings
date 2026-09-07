import re

with open('top-20-boarding-schools-in-usa/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<div class="rich-article-content">'
end_marker = '</div>\n<div class="author-bio-box"'
end_marker_fallback = '</div>\n  <div class="author-bio-box"'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)
if end_idx == -1:
    end_idx = html.find(end_marker_fallback)

new_content = '''<div class="rich-article-content">
  <p><strong>Top 20 Boarding Schools in the USA</strong> &mdash; This independent editorial guide helps families navigate the competitive landscape of American boarding schools. We break down curriculum styles, regional concentrations, and the critical admissions steps international applicants must consider.</p>
  
  <p><strong>Please note:</strong> This is a research guide compiled by Top Schools Rankings. We are not affiliated with, nor officially endorsed by, Niche, Boarding School Review, or any of the schools listed. The top 20 list below is provided for context and is based on publicly reported data from the <strong>Niche 2026 Best Boarding High Schools in America</strong> rankings.</p>

  <h2>Ranking Methodology &amp; Limitations</h2>
  <p>Different ranking organizations evaluate boarding schools using vastly different metrics. Organizations like Niche blend objective data (such as SAT/ACT scores and matriculation rates) with subjective user reviews from students and parents. Therefore, a school's placement at #1 vs #5 often comes down to community survey responses rather than strict academic superiority.</p>
  <p>While historic New England prep schools dominate the top tier, this list also highlights schools in California, Texas, and Florida that have scored exceptionally well on Niche's community metrics.</p>

  <figure>
    <img src="/media/articles/top-20-boarding-schools-in-usa-inline-01.webp" alt="Historic boarding school buildings" width="1400" height="917" loading="lazy" decoding="async">
    <figcaption>Top U.S. boarding schools offer world-class facilities and deeply immersive academic communities.</figcaption>
  </figure>

  <h2>Top 20 Boarding Schools in the USA (Niche 2026 Benchmark)</h2>
  <p>The table below summarizes the top 20 boarding schools according to Niche's 2026 data. Always verify current enrollment figures and academic programs directly on the official school websites.</p>
  <table>
    <thead>
      <tr><th>Niche 2026 Rank</th><th>School</th><th>Location</th><th>Niche Grade</th><th>Snapshot / Focus</th></tr>
    </thead>
    <tbody>
      <tr><td>1</td><td>The Hotchkiss School</td><td>Lakeville, CT</td><td>A+</td><td>Inquiry-based curriculum, strong arts</td></tr>
      <tr><td>2</td><td>Phillips Exeter Academy</td><td>Exeter, NH</td><td>A+</td><td>Harkness method, massive endowment</td></tr>
      <tr><td>3</td><td>Choate Rosemary Hall</td><td>Wallingford, CT</td><td>A+</td><td>Signature programs, large co-ed campus</td></tr>
      <tr><td>4</td><td>The Lawrenceville School</td><td>Lawrenceville, NJ</td><td>A+</td><td>Distinctive House system</td></tr>
      <tr><td>5</td><td>Groton School</td><td>Groton, MA</td><td>A+</td><td>Smaller, highly intimate academic cohort</td></tr>
      <tr><td>6</td><td>Phillips Academy Andover</td><td>Andover, MA</td><td>A+</td><td>Over 1,100 students, immense resources</td></tr>
      <tr><td>7</td><td>St. Paul's School</td><td>Concord, NH</td><td>A+</td><td>100% fully residential boarding model</td></tr>
      <tr><td>8</td><td>Noble and Greenough School</td><td>Dedham, MA</td><td>A+</td><td>Strong day + boarding integration</td></tr>
      <tr><td>9</td><td>Lake Forest Academy</td><td>Lake Forest, IL</td><td>A+</td><td>Leading Midwest option</td></tr>
      <tr><td>10</td><td>Cate School</td><td>Carpinteria, CA</td><td>A+</td><td>Elite West Coast boarding</td></tr>
      <tr><td>11</td><td>St. Andrew's School</td><td>Middletown, DE</td><td>A+</td><td>Classic mid-Atlantic campus</td></tr>
      <tr><td>12</td><td>Oak Crest Academy</td><td>Pomona, CA</td><td>A+</td><td>Gifted &amp; STEM-focused</td></tr>
      <tr><td>13</td><td>The Loomis Chaffee School</td><td>Windsor, CT</td><td>A+</td><td>Excellent writing and global programs</td></tr>
      <tr><td>14</td><td>The Peddie School</td><td>Hightstown, NJ</td><td>A+</td><td>Strong STEM and athletics</td></tr>
      <tr><td>15</td><td>Deerfield Academy</td><td>Deerfield, MA</td><td>A+</td><td>Historic village campus, deep traditions</td></tr>
      <tr><td>16</td><td>Milton Academy</td><td>Milton, MA</td><td>A+</td><td>Progressive academics near Boston</td></tr>
      <tr><td>17</td><td>American Heritage Schools, Broward Campus</td><td>Plantation, FL</td><td>A+</td><td>Pre-professional tracks</td></tr>
      <tr><td>18</td><td>Elite Preparatory Academy</td><td>Hopatcong, NJ</td><td>A+</td><td>East coast location</td></tr>
      <tr><td>19</td><td>The Village School</td><td>Houston, TX</td><td>A+</td><td>International Baccalaureate (IB), Texas</td></tr>
      <tr><td>20</td><td>Princeton Int'l School of Math &amp; Science</td><td>Princeton, NJ</td><td>A+</td><td>Intense STEM magnet program</td></tr>
    </tbody>
  </table>

  <h2>Understanding the Top Tier: Exeter, Andover, and Hotchkiss</h2>
  <p>The "Ten Schools" group, which includes Exeter, Andover, Hotchkiss, Choate, and Lawrenceville, represents some of the oldest and most selective secondary schools in America. </p>
  <ul>
    <li><strong>Teaching Styles:</strong> <a href="/how-to-get-into-phillips-exeter-academy-2026-admissions-fees-expert-strategies/">Phillips Exeter Academy</a> is famous for pioneering the <strong>Harkness method</strong>, where classes revolve around a seminar table to encourage student-led discussion.</li>
    <li><strong>Campus Models:</strong> <strong>St. Paul's School</strong> is one of the few remaining 100% boarding schools (all students and faculty live on campus), whereas schools like <strong>Milton Academy</strong> and <strong>Noble and Greenough</strong> blend boarding students with a large local day-student population.</li>
  </ul>

  <figure>
    <img src="/media/articles/top-20-boarding-schools-in-usa-inline-03.webp" alt="Group of international students studying together outdoors" width="1400" height="933" loading="lazy" decoding="async">
    <figcaption>Top boarding schools host highly diverse, international student bodies.</figcaption>
  </figure>

  <h2>Tuition, Financial Aid, and International Context</h2>
  <p>Attending a top U.S. boarding school requires a significant financial commitment. For the 2024&ndash;2025 and 2025&ndash;2026 academic years, boarding tuition at elite institutions typically ranges from <strong>,000 to ,000+ per year</strong>. This generally covers tuition, room, and board, but families must also budget for health insurance, technology fees, and travel.</p>
  <p><strong>Crucial note for international applicants:</strong></p>
  <ul>
    <li><strong>Financial Aid:</strong> While schools like Andover and Exeter have massive endowments and are need-blind for domestic students, financial aid for international students is often highly competitive and strictly limited. Always contact the school's financial aid office early to determine your eligibility.</li>
    <li><strong>Visas:</strong> International students require an F-1 student visa. Ensure the school is SEVP-certified and can issue the required Form I-20 upon enrollment.</li>
  </ul>

  <h2>Application Timeline for Elite Boarding Schools</h2>
  <p>Many top schools use centralized application portals like the <strong>Standard Application Online (SAO)</strong> or <strong>Gateway to Prep Schools</strong>. Deadlines for the most selective campuses are strict.</p>
  <table>
    <thead>
      <tr><th>Application Stage</th><th>Typical Timing</th><th>What to Prepare</th></tr>
    </thead>
    <tbody>
      <tr><td>Research &amp; Tours</td><td>12 &ndash; 18 months prior</td><td>Schedule campus visits or attend virtual admissions events.</td></tr>
      <tr><td>Testing (SSAT / ISEE)</td><td>October &ndash; January</td><td>Register early for standardized testing. Many schools also accept the SSAT at Home.</td></tr>
      <tr><td>Interviews</td><td>October &ndash; January</td><td>An interview is mandatory for most top schools (conducted via Zoom or on campus).</td></tr>
      <tr><td>Application Deadline</td><td>January 15 or 31</td><td>Submit parent statements, student essays, transcripts, and teacher recommendations.</td></tr>
      <tr><td>Decision Release</td><td>March 10</td><td>Standard notification date for many New England boarding schools.</td></tr>
    </tbody>
  </table>
  <p>Always verify exact application deadlines directly on each school's official admissions website.</p>

  <h2>FAQs: Top 20 Boarding Schools in the USA</h2>
  <h3>Is Hotchkiss really the #1 boarding school in the USA?</h3>
  <p>In the Niche 2026 methodology, yes. However, other platforms (such as Boarding School Review or FindingSchool) may rank Andover, Exeter, or Groton first based on different metrics like endowment size, matriculation data, or faculty degrees.</p>

  <h3>What is the acceptance rate for top boarding schools?</h3>
  <p>Acceptance rates at the most competitive schools (like Andover, Exeter, Groton, and St. Paul's) are routinely below 15%, making them as competitive as many elite universities.</p>

  <h3>Do international students need to take the TOEFL?</h3>
  <p>Yes. If your primary language is not English, or if you do not currently attend an English-medium school, highly selective boarding schools will require a TOEFL, IELTS, or Duolingo English Test (DET) score alongside the SSAT or ISEE.</p>
</div>'''

if start_idx != -1 and end_idx != -1:
    final_html = html[:start_idx] + new_content + html[end_idx:]
    with open('top-20-boarding-schools-in-usa/index.html', 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Successfully replaced content.")
else:
    print(f"Could not find markers for replacement. start: {start_idx}, end: {end_idx}")