import re

with open('top-20-uk-boarding-schools-for-international-students/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<div class="rich-article-content">'
end_marker = '</div>\n<div class="author-bio-box"'
end_marker_fallback = '</div>\n  <div class="author-bio-box"'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)
if end_idx == -1:
    end_idx = html.find(end_marker_fallback)

new_content = '''<div class="rich-article-content">
  <p><strong>Top 20 UK Boarding Schools for International Students</strong> &mdash; This independent editorial guide helps international families navigate the complexities of elite British boarding schools, from the historic "Public Schools" to modern IB powerhouses.</p>
  
  <p><strong>Please note:</strong> This is a research guide compiled by TopSchoolsRankings. We are not affiliated with, nor officially endorsed by, The Sunday Times, Tatler, Ofsted, the UK Department for Education, or any of the listed schools (Eton, Harrow, Winchester, etc.). The top 20 list below is an editorial shortlist referencing public reputation, historic prestige, and 2025/2026 academic performance metrics.</p>

  <h2>Why International Students Choose UK Boarding Schools</h2>
  <p>British boarding schools offer unparalleled academic rigour, centuries of history, and a globally recognized pathway to elite universities (like Oxbridge, the Russell Group, and the US Ivy League). For international students, these institutions provide full academic immersion, deep pastoral care, and a structured environment designed to develop independence before university.</p>

  <figure>
    <img src="/media/articles/top-20-uk-boarding-schools-for-international-students-inline-02.webp" alt="Students walking across a leafy college campus" width="1400" height="933" loading="lazy" decoding="async">
    <figcaption>Top UK independent schools combine centuries-old architecture with world-class academic facilities.</figcaption>
  </figure>

  <h2>Top 20 UK Boarding Schools (2026 Editorial Shortlist)</h2>
  <p>This list highlights 20 of the most sought-after boarding schools for international applicants, balancing academic dominance (such as those highlighted in The Sunday Times Parent Power guide) with global brand recognition.</p>
  <table>
    <thead>
      <tr><th>#</th><th>School</th><th>Location</th><th>Snapshot / Focus</th></tr>
    </thead>
    <tbody>
      <tr><td>1</td><td>Eton College</td><td>Windsor</td><td>Historic all-boys public school; global brand</td></tr>
      <tr><td>2</td><td>Harrow School</td><td>London</td><td>All-boys boarding; excellent capital access</td></tr>
      <tr><td>3</td><td>Winchester College</td><td>Winchester</td><td>Intellectual culture; massive Oxbridge pipeline</td></tr>
      <tr><td>4</td><td>Brighton College</td><td>Brighton</td><td>Leading co-ed academic powerhouse</td></tr>
      <tr><td>5</td><td>Charterhouse</td><td>Godalming</td><td>Historic co-ed Surrey campus</td></tr>
      <tr><td>6</td><td>Rugby School</td><td>Rugby</td><td>Co-ed public school tradition</td></tr>
      <tr><td>7</td><td>Marlborough College</td><td>Wiltshire</td><td>Co-ed; strong arts and sporting tradition</td></tr>
      <tr><td>8</td><td>Sevenoaks School</td><td>Kent</td><td>World-leading International Baccalaureate (IB) school</td></tr>
      <tr><td>9</td><td>Cheltenham Ladies' College</td><td>Cheltenham</td><td>Leading all-girls boarding</td></tr>
      <tr><td>10</td><td>Westminster School</td><td>London</td><td>Day/boarding hybrid; extreme academic selectivity</td></tr>
      <tr><td>11</td><td>Wycombe Abbey</td><td>High Wycombe</td><td>Top all-girls exam results</td></tr>
      <tr><td>12</td><td>Tonbridge School</td><td>Kent</td><td>Exceptional boys' boarding</td></tr>
      <tr><td>13</td><td>Dulwich College</td><td>London</td><td>Strong international network</td></tr>
      <tr><td>14</td><td>Oundle School</td><td>Northamptonshire</td><td>Full 7-day boarding culture</td></tr>
      <tr><td>15</td><td>Shrewsbury School</td><td>Shropshire</td><td>Co-ed public school; strong rowing tradition</td></tr>
      <tr><td>16</td><td>Gordonstoun</td><td>Scotland</td><td>Famous outdoor education ethos</td></tr>
      <tr><td>17</td><td>Benenden School</td><td>Kent</td><td>Elite all-girls boarding</td></tr>
      <tr><td>18</td><td>Wellington College</td><td>Berkshire</td><td>Co-ed; modern pastoral and wellbeing model</td></tr>
      <tr><td>19</td><td>The King's School, Canterbury</td><td>Kent</td><td>Historic Cathedral city setting</td></tr>
      <tr><td>20</td><td>St Paul's School</td><td>London</td><td>Academic leader (predominantly day, limited boarding)</td></tr>
    </tbody>
  </table>

  <h2>Understanding Academic Pathways: A-Levels vs. IB</h2>
  <p>International families must choose between two distinct academic tracks offered in the Sixth Form (ages 16-18):</p>
  <ul>
    <li><strong>A-Levels:</strong> The traditional UK system, requiring students to specialize deeply in 3 or 4 subjects. Ideal for students who know exactly what they want to study at a UK university.</li>
    <li><strong>International Baccalaureate (IB):</strong> A broader curriculum requiring 6 subjects across sciences, humanities, and languages. Schools like <strong>Sevenoaks</strong> are globally renowned for their IB programs, which are highly favored by US universities.</li>
  </ul>

  <h2>Fees, Scholarships, and Bursaries</h2>
  <p>Elite UK boarding schools require a substantial financial commitment. For the 2024&ndash;2026 academic cycles, full boarding fees at top "Public Schools" (like Eton, Harrow, or Winchester) typically range from <strong>&pound;45,000 to &pound;55,000+ per year</strong>.</p>
  <ul>
    <li><strong>Scholarships:</strong> Merit-based awards (for academics, music, or sport) offer prestige but usually only provide a tiny fee discount (e.g., 5% to 10%).</li>
    <li><strong>Bursaries:</strong> Means-tested financial aid. While domestic bursaries are common, <strong>bursaries for international students are incredibly rare</strong>. International families should generally expect to pay full fees.</li>
  </ul>

  <figure>
    <img src="/media/articles/top-20-uk-boarding-schools-for-international-students-inline-03.webp" alt="Group of international students studying together outdoors" width="1400" height="933" loading="lazy" decoding="async">
    <figcaption>A thriving international community is a hallmark of modern British boarding schools.</figcaption>
  </figure>

  <h2>Admissions &amp; Visas for International Applicants</h2>
  <p>Applying from overseas requires careful planning, often beginning 2 to 3 years before entry.</p>
  <ul>
    <li><strong>English Proficiency:</strong> Top schools expect near-fluent English. Many require international applicants to take the <strong>UKiset</strong> (UK Independent Schools Entry Test) as a pre-screening tool before inviting them to sit formal entrance exams.</li>
    <li><strong>Guardianship:</strong> UK boarding schools mandate that international students whose parents live overseas appoint an educational guardian based in the UK to act on their behalf during emergencies and closed weekends (exeats).</li>
    <li><strong>Child Student Visa:</strong> International students require sponsorship to study in the UK. Most schools on this list are highly experienced licensed sponsors. <em>Note: TopSchoolsRankings does not provide legal or immigration advice. Visa rules change frequently; always confirm current requirements and sponsorship eligibility directly on the official <a href="https://www.gov.uk/child-study-visa" target="_blank" rel="noopener noreferrer">UK Government (GOV.UK) website</a>.</em></li>
  </ul>

  <h2>FAQs: UK Boarding Schools for International Students</h2>
  <h3>Is Eton College always #1 in exam league tables?</h3>
  <p>No. While Eton has arguably the strongest global brand and historic prestige, intense academic hothouses (often day-heavy schools like St Paul's) frequently place higher in raw A* exam percentages. Elite boarding schools focus on holistic education, not just exam metrics.</p>

  <h3>Can a UK boarding school help me get into a US university?</h3>
  <p>Yes. Many top UK schools now have dedicated US university counselors. Schools like Wellington College, Winchester, and Sevenoaks send dozens of graduates to the Ivy League and elite US colleges every year.</p>

  <h3>How do I verify a school's quality?</h3>
  <p>Do not rely solely on rankings. Verify a school's pastoral care, academic outcomes, and boarding quality by reading their latest official inspection report on the Independent Schools Inspectorate (ISI) website.</p>

  <p><em>Disclaimer: School fees, admission timelines, and visa rules change frequently. This guide summarizes publicly available data for planning purposes only. Confirm all details directly with the individual schools and official UK government sources before applying.</em></p>
</div>'''

if start_idx != -1 and end_idx != -1:
    final_html = html[:start_idx] + new_content + html[end_idx:]
    with open('top-20-uk-boarding-schools-for-international-students/index.html', 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Successfully replaced content.")
else:
    print(f"Could not find markers for replacement. start: {start_idx}, end: {end_idx}")