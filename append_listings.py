import os
import re

file_path = "listings/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

new_listings = """<article class="listing-card">
  <div class="listing-card-top">
    <span class="listing-lettermark" aria-hidden="true" style="display:flex; align-items:center; justify-content:center; background:#1e293b; color:white; font-size:40px; font-weight:bold; width:180px; height:180px;">PU</span>
    <span>University profile</span>
  </div>
  <h2><a href="/listing/purdue-university/">Purdue University</a></h2>
  <p>Public land-grant research university in West Lafayette, Indiana, known for its highly ranked engineering, agriculture and aviation programmes.</p>
  <a href="/listing/purdue-university/">Open profile →</a>
</article>
<article class="listing-card">
  <div class="listing-card-top">
    <span class="listing-lettermark" aria-hidden="true" style="display:flex; align-items:center; justify-content:center; background:#1e293b; color:white; font-size:40px; font-weight:bold; width:180px; height:180px;">UCSD</span>
    <span>University profile</span>
  </div>
  <h2><a href="/listing/university-of-california-san-diego/">University of California, San Diego</a></h2>
  <p>Public land-grant research university in La Jolla, California, known for STEM, oceanography, and a unique residential college system.</p>
  <a href="/listing/university-of-california-san-diego/">Open profile →</a>
</article>
<article class="listing-card">
  <div class="listing-card-top">
    <span class="listing-lettermark" aria-hidden="true" style="display:flex; align-items:center; justify-content:center; background:#1e293b; color:white; font-size:40px; font-weight:bold; width:180px; height:180px;">UF</span>
    <span>University profile</span>
  </div>
  <h2><a href="/listing/university-of-florida/">University of Florida</a></h2>
  <p>Public land-grant research university in Gainesville, Florida, offering extensive undergraduate and graduate programmes.</p>
  <a href="/listing/university-of-florida/">Open profile →</a>
</article>
<article class="listing-card">
  <div class="listing-card-top">
    <span class="listing-lettermark" aria-hidden="true" style="display:flex; align-items:center; justify-content:center; background:#1e293b; color:white; font-size:40px; font-weight:bold; width:180px; height:180px;">UMD</span>
    <span>University profile</span>
  </div>
  <h2><a href="/listing/university-of-maryland-college-park/">University of Maryland, College Park</a></h2>
  <p>Public land-grant research university in College Park, Maryland, near Washington, D.C., known for research and strong academic programmes.</p>
  <a href="/listing/university-of-maryland-college-park/">Open profile →</a>
</article>
<article class="listing-card">
  <div class="listing-card-top">
    <span class="listing-lettermark" aria-hidden="true" style="display:flex; align-items:center; justify-content:center; background:#1e293b; color:white; font-size:40px; font-weight:bold; width:180px; height:180px;">UW</span>
    <span>University profile</span>
  </div>
  <h2><a href="/listing/university-of-wisconsin-madison/">University of Wisconsin–Madison</a></h2>
  <p>Public land-grant research university in Madison, Wisconsin, known for extensive research output and strong academic programmes.</p>
  <a href="/listing/university-of-wisconsin-madison/">Open profile →</a>
</article>
"""

# Insert right after <div class="listing-grid">
if '<div class="listing-grid">' in content:
    content = content.replace('<div class="listing-grid">', '<div class="listing-grid">\n' + new_listings, 1)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Injected successfully.")
else:
    print("Could not find <div class=\"listing-grid\">")
