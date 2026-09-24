with open('top-100-schools-in-india/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

append_block = '''
<p><strong>Editorial disclosure:</strong> No school paid for inclusion or position. Generated visual scenes are illustrative and do not depict a named institution. The ranking contains editorial judgment wherever an official common table does not exist.</p>

<h2>Related TopSchoolsRankings Guides</h2>
<ul>
<li><a href="https://topschoolsrankings.com/how-parents-can-choose-the-right-cbse-school/">How Parents Can Choose the Right CBSE School</a></li>
<li><a href="https://topschoolsrankings.com/how-smart-hostels-are-changing-student-life-at-indian-universities/">How Smart Hostels Are Changing Student Life at Indian Universities</a></li>
</ul>

<hr style="margin: 40px 0; border: none; border-top: 1px solid #e2e8f0;">

<div class="author-bio-box" style="margin-bottom: 40px; padding: 20px; background: #f8f9fa; border-radius: 8px; display: flex; align-items: center; gap: 20px; border: 1px solid #e2e8f0; clear: both;">
  <img width="80" height="80" src="/assets/saahil.jpg" alt="Saahil" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover;">
  <div>
    <h3 style="margin: 0 0 5px 0; font-size: 18px;"><a href="/author/saahil/" style="color: #1a202c; text-decoration: none;">Saahil</a></h3>
    <p style="margin: 0; font-size: 14px; color: #4a5568; line-height: 1.5;">Saahil is an education researcher and content creator specializing in university rankings, admissions strategies, and student tools. He is dedicated to helping students make informed academic decisions.</p>
  </div>
</div>

<hr style="margin: 40px 0; border: none; border-top: 1px solid #e2e8f0;">

<section class="related-guides"><h2>Continue your research</h2><div class="related-grid">
  <article class="guide-card"><a class="guide-card-image" href="/how-to-verify-an-australian-cricos-course/"><img class="" src="/media/new-guides/australia-cricos-check.webp" alt="International student verifying an Australian course registration" width="1672" height="941" loading="lazy" decoding="async"></a><div class="card-meta"><span>New research guide</span><span>8-12 min read</span></div><h3><a href="/how-to-verify-an-australian-cricos-course/">How to Verify an Australian Course on CRICOS</a></h3><p>Check an Australian provider, course code, location and duration in the official CRICOS register before applying as an international student.</p><a class="text-link" href="/how-to-verify-an-australian-cricos-course/">Read the guide <span>&rarr;</span></a></article>
  <article class="guide-card"><a class="guide-card-image" href="/algoma-university-for-international-students-admissions-fees-courses-visa-guide/"><img class="" src="/media/articles/algoma-university-for-international-students-admissions-fees-courses-visa-guide-featured.webp" alt="Students walking on a modern university campus with green lawns and academic buildings." width="1500" height="1000" loading="lazy" decoding="async"></a><div class="card-meta"><span>Editorial guide</span><span>8-12 min read</span></div><h3><a href="/algoma-university-for-international-students-admissions-fees-courses-visa-guide/">Algoma University for International Students: Admissions, Fees, Courses &amp; Visa Guide</a></h3><p>Choosing the right university in Canada is a crucial decision for international students.</p><a class="text-link" href="/algoma-university-for-international-students-admissions-fees-courses-visa-guide/">Read the guide <span>&rarr;</span></a></article>
  <article class="guide-card"><a class="guide-card-image" href="/douglas-college-canada-admissions-fees-courses-university-transfer-guide-for-international-students/"><img class="" src="/media/articles/douglas-college-canada-admissions-fees-courses-university-transfer-guide-for-international-students-featured.webp" alt="Douglas College Canada: Admissions, Fees, Courses &amp; University Transfer Guide for International Students" width="316" height="314" loading="lazy" decoding="async"></a><div class="card-meta"><span>Editorial guide</span><span>8-12 min read</span></div><h3><a href="/douglas-college-canada-admissions-fees-courses-university-transfer-guide-for-international-students/">Douglas College Canada: Admissions, Fees, Courses &amp; University Transfer Guide for International Students</a></h3><p>For international students looking for an affordable and career-focused education in Canada, Douglas College is one of the most popular choices in British Columbia.</p><a class="text-link" href="/douglas-college-canada-admissions-fees-courses-university-transfer-guide-for-international-students/">Read the guide <span>&rarr;</span></a></article>
  <article class="guide-card"><a class="guide-card-image" href="/how-parents-can-choose-the-right-cbse-school/"><img class="" src="/media/articles/how-parents-can-choose-the-right-cbse-school-featured.webp" alt="How Parents Can Choose the Right CBSE School in 2026" width="1500" height="844" loading="lazy" decoding="async"></a><div class="card-meta"><span>Editorial guide</span><span>8-12 min read</span></div><h3><a href="/how-parents-can-choose-the-right-cbse-school/">How Parents Can Choose the Right CBSE School in 2026</a></h3><p>Learn how parents can choose the right CBSE school in 2026 by checking affiliation, teaching quality, safety, fees, technology, academics, and student support.</p><a class="text-link" href="/how-parents-can-choose-the-right-cbse-school/">Read the guide <span>&rarr;</span></a></article>
</div></section>
'''

html = html.replace('      </div>\n    </article>', f'      {append_block}\n      </div>\n    </article>')

with open('top-100-schools-in-india/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Updated top-100-schools-in-india/index.html with footer')