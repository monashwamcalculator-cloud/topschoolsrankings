import os

wam_content = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>WAM Calculator | Weighted Average Mark Calculator | Top Schools Rankings</title><meta name="description" content="Calculate your WAM (Weighted Average Mark) for Australian universities like Monash, Melbourne, and UNSW."><meta name="robots" content="index, follow"><link rel="canonical" href="https://topschoolsrankings.com/tools/wam-calculator/"><meta name="google-adsense-account" content="ca-pub-5825245351059712"><meta property="og:type" content="website"><meta property="og:site_name" content="Top Schools Rankings"><meta property="og:title" content="WAM Calculator | Weighted Average Mark Calculator"><meta property="og:description" content="Calculate your WAM (Weighted Average Mark) for Australian universities like Monash, Melbourne, and UNSW."><meta property="og:url" content="https://topschoolsrankings.com/tools/wam-calculator/"><meta property="og:image" content="https://topschoolsrankings.com/og.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="https://topschoolsrankings.com/og.png"><link rel="icon" href="/favicon.jpg"><link rel="stylesheet" href="/assets/site.css"><script async crossorigin="anonymous" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5825245351059712"></script><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","name":"WAM Calculator","description":"Calculate your WAM (Weighted Average Mark) for Australian universities like Monash, Melbourne, and UNSW.","image":"https://topschoolsrankings.com/og.png","url":"https://topschoolsrankings.com/tools/wam-calculator/","publisher":{"@type":"Organization","name":"Top Schools Rankings","url":"https://topschoolsrankings.com"}}</script><script src="/assets/site.js" defer></script>
<style>
.subject-row { display: grid; grid-template-columns: 2fr 1fr 1fr 40px; gap: 10px; margin-bottom: 10px; align-items: end; }
.subject-row input { width: 100%; height: 42px; border: 1px solid rgba(255, 255, 255, .2); border-radius: 6px; padding: 0 10px; background: rgba(255, 255, 255, .09); color: white; outline: none; font-size: 14px; }
.subject-row input:focus { border-color: var(--gold-500); }
.remove-btn { height: 42px; background: rgba(220, 53, 69, 0.2); color: #f596a0; border: 1px solid rgba(220, 53, 69, 0.3); border-radius: 6px; cursor: pointer; display: flex; align-items: center; justify-content: center; font-weight: bold; }
.remove-btn:hover { background: rgba(220, 53, 69, 0.4); }
.add-btn { background: rgba(255, 255, 255, 0.1); color: white; border: 1px dashed rgba(255, 255, 255, 0.3); padding: 10px; border-radius: 6px; cursor: pointer; width: 100%; margin-bottom: 20px; font-weight: 600; }
.add-btn:hover { background: rgba(255, 255, 255, 0.15); border-color: rgba(255, 255, 255, 0.5); }
.result-success { background: rgba(40, 167, 69, 0.15); color: #8de49f; border-color: rgba(40, 167, 69, 0.3); }
.tool-result h3 { margin: 0 0 8px 0; color: inherit; font-size: 24px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; }
.tool-result p { margin: 0; font-size: 16px; opacity: 0.9; font-weight: normal; }
@media (max-width: 600px) {
  .subject-row { grid-template-columns: 1fr 1fr; }
  .subject-row .remove-btn { grid-column: span 2; }
}
</style>
</head><body>
  <div class="evidence-bar"><div class="site-container evidence-bar-inner"><span>Independent education research</span><span>Sources shown · Dates checked · Corrections welcomed</span></div></div>
  <header class="site-header"><div class="site-container header-inner">
  <a class="brand" href="/" aria-label="Top Schools Rankings home" style="display:flex; align-items:center;">
    <img src="/assets/logo.png" alt="Top Schools Rankings" style="height:60px; width:auto; max-width:100%;">
  </a>
    <nav class="desktop-nav" aria-label="Primary navigation"><a href="/blogs/">Guides</a><a href="/listings/">Listings</a><a href="/compare/">Compare</a><a href="/tools/">Tools</a><a href="/ranking-methodology/">Methodology</a></nav>
    <div class="header-search">
  <div class="search-box search-box-compact" data-search>
    <label class="sr-only">Search schools, universities and guides</label>
    <div class="search-input-wrap"><span aria-hidden="true">⌕</span><input type="search" placeholder="Search guides…" autocomplete="off"></div>
    <div class="search-results" hidden></div>
  </div></div>
    <details class="mobile-nav"><summary aria-label="Open menu">Menu</summary><nav><a href="/blogs/">Guides</a><a href="/listings/">Listings</a><a href="/compare/">Compare</a><a href="/tools/">Tools</a><a href="/ranking-methodology/">Methodology</a><a href="/about-us/">About</a></nav></details>
  </div></header><main>
  <nav class="breadcrumbs site-container" aria-label="Breadcrumb"><a href="/">Home</a><span><i aria-hidden="true">/</i><a href="/tools/">Tools</a></span><span><i aria-hidden="true">/</i><b>WAM Calculator</b></span></nav>
  <header class="page-header"><div class="site-container narrow"><span class="eyebrow">Interactive planning resource</span><h1>Weighted Average Mark (WAM) Calculator</h1><p>Calculate your WAM for Australian universities like Monash, Melbourne, and UNSW.</p><div class="page-meta">Free to use · No account · Instant calculation</div></div></header><section class="section site-container article-layout"><article class="article-body">
  
  <section class="tool-panel" data-custom>
    <div class="tool-panel-head" style="margin-bottom: 20px;">
      <span>Interactive planning tool</span>
      <h2>WAM Calculator</h2>
      <p>Enter your subject marks and credit points to calculate your Weighted Average Mark.</p>
    </div>
    
    <div id="subjects_container">
      <div class="subject-row">
        <div><label style="font-size:12px; color:#c9d5e4; margin-bottom:5px; display:block;">Subject Name</label><input type="text" placeholder="e.g. FIT1045" class="subj-name"></div>
        <div><label style="font-size:12px; color:#c9d5e4; margin-bottom:5px; display:block;">Mark (0-100)</label><input type="number" placeholder="e.g. 85" min="0" max="100" class="subj-mark"></div>
        <div><label style="font-size:12px; color:#c9d5e4; margin-bottom:5px; display:block;">Credit Pts</label><input type="number" placeholder="e.g. 6" min="1" class="subj-credit" value="6"></div>
        <button class="remove-btn" type="button" title="Remove row">X</button>
      </div>
      <div class="subject-row">
        <div><input type="text" placeholder="e.g. MAT1830" class="subj-name"></div>
        <div><input type="number" placeholder="e.g. 78" min="0" max="100" class="subj-mark"></div>
        <div><input type="number" placeholder="e.g. 6" min="1" class="subj-credit" value="6"></div>
        <button class="remove-btn" type="button" title="Remove row">X</button>
      </div>
    </div>
    
    <button class="add-btn" type="button" id="add_btn">+ Add Another Subject</button>
    <button class="button button-primary" type="button" id="calc_btn" style="width: 100%;">Calculate My WAM</button>
    <div id="result_box" class="tool-result result-success" hidden style="text-align:center; padding: 25px;"></div>
  </section>
  
  <script>
    document.getElementById("add_btn").addEventListener("click", function() {
      var container = document.getElementById("subjects_container");
      var row = document.createElement("div");
      row.className = "subject-row";
      row.innerHTML = '<div><input type="text" placeholder="Subject" class="subj-name"></div>' +
                      '<div><input type="number" placeholder="Mark" min="0" max="100" class="subj-mark"></div>' +
                      '<div><input type="number" placeholder="Credit" min="1" class="subj-credit" value="6"></div>' +
                      '<button class="remove-btn" type="button" title="Remove row">X</button>';
      container.appendChild(row);
    });

    document.getElementById("subjects_container").addEventListener("click", function(e) {
      if(e.target.classList.contains("remove-btn")) {
        if(document.querySelectorAll(".subject-row").length > 1) {
          e.target.parentElement.remove();
        }
      }
    });

    document.getElementById("calc_btn").addEventListener("click", function() {
      var rows = document.querySelectorAll(".subject-row");
      var totalWeightedMarks = 0;
      var totalCredits = 0;
      
      rows.forEach(function(row) {
        var mark = parseFloat(row.querySelector(".subj-mark").value);
        var credit = parseFloat(row.querySelector(".subj-credit").value);
        
        if (!isNaN(mark) && !isNaN(credit)) {
          totalWeightedMarks += (mark * credit);
          totalCredits += credit;
        }
      });
      
      var resultBox = document.getElementById("result_box");
      if (totalCredits === 0) {
        resultBox.innerHTML = "<p>Please enter at least one valid mark and credit point value.</p>";
        resultBox.style.borderColor = "rgba(255,193,7,0.3)";
        resultBox.style.color = "#ffe68a";
        resultBox.style.background = "rgba(255,193,7,0.15)";
      } else {
        var wam = (totalWeightedMarks / totalCredits).toFixed(3);
        var gradeDesc = "";
        
        if (wam >= 80) gradeDesc = "High Distinction (HD)";
        else if (wam >= 70) gradeDesc = "Distinction (D)";
        else if (wam >= 60) gradeDesc = "Credit (C)";
        else if (wam >= 50) gradeDesc = "Pass (P)";
        else gradeDesc = "Fail (N)";
        
        resultBox.innerHTML = "<h3>Your WAM is " + wam + "</h3><p>Equivalent to a <strong>" + gradeDesc + "</strong></p>";
        resultBox.style.borderColor = "rgba(40,167,69,0.3)";
        resultBox.style.color = "#8de49f";
        resultBox.style.background = "rgba(40,167,69,0.15)";
      }
      resultBox.hidden = false;
    });
  </script>

  <p>The Weighted Average Mark (WAM) is the primary method used by Australian universities—including Monash University, University of Melbourne, UNSW, and University of Sydney—to measure your overall academic performance. Unlike a standard GPA (which runs on a 4.0 or 7.0 scale), a WAM is calculated out of 100.</p>
  
  <h2>How is WAM calculated?</h2>
  <p>Your WAM is calculated by multiplying the mark you received in each unit by the credit points of that unit, adding those totals together, and then dividing by the total number of credit points you have attempted.</p>
  <p><strong>Formula:</strong> <em>WAM = Sum of (Mark × Credit Points) / Total Credit Points</em></p>
  
  <h2>Why do Credit Points matter?</h2>
  <p>At most universities, a standard subject is worth 6 or 12 credit points. A subject worth 12 credit points (often a double unit or capstone project) will have twice the impact on your WAM as a standard 6-credit point subject. Our calculator automatically factors this weighting in when you adjust the credit points field.</p>
  
  <h2>Standard Australian Grading Scale</h2>
  <ul>
    <li><strong>80 - 100:</strong> High Distinction (HD)</li>
    <li><strong>70 - 79:</strong> Distinction (D)</li>
    <li><strong>60 - 69:</strong> Credit (C)</li>
    <li><strong>50 - 59:</strong> Pass (P)</li>
    <li><strong>0 - 49:</strong> Fail (N)</li>
  </ul>
  
  <h2>Frequently asked questions</h2>
  <h3>Is WAM the same at all Australian universities?</h3>
  <p>The formula for WAM is almost universally identical across Australian institutions. However, some universities (like UNSW or Unimelb) might apply different weighting based on the year level of the subject (e.g., first-year subjects might count for less). Always check your specific faculty's handbook for advanced weighting rules.</p>
  
  <h3>What is a "good" WAM?</h3>
  <p>A WAM of 70 (Distinction) is generally considered very competitive and is often the baseline required for entry into Honours programs or competitive graduate roles. A WAM above 80 (High Distinction) places you in the top tier of students.</p>

  <h2>Related tools</h2>
  <h3><a href="/tools/gpa-percentage-converter/">GPA to percentage converter</a></h3>
  <p>Convert your WAM percentage into a US 4.0 GPA scale.</p>
  <h3><a href="/tools/final-grade-calculator/">Final grade calculator</a></h3>
  <p>Find out what you need on your final exam to maintain your desired WAM.</p>
  
  </article><aside class="article-aside"><div><span class="aside-label">Important</span><strong>Check your handbook</strong><p>Some universities apply year-level weighting (where Level 1 units count for 0.5x and Level 3 units count for 1.0x). This calculator assumes a standard 1.0x weight for all entered units.</p></div></aside></section></main>
  <footer class="site-footer"><div class="site-container footer-grid">
    <div class="footer-about">
  <a class="brand" href="/" aria-label="Top Schools Rankings home" style="display:flex; align-items:center;">
    <img src="/assets/logo.png" alt="Top Schools Rankings" style="height:60px; width:auto; max-width:100%;">
  </a><p>Independent school and university research for students and families. We are not an admissions agency and do not sell rankings.</p><a class="correction-link" href="/contact-us/">Report a correction →</a><div class="social-links" style="margin-top:20px; display:flex; gap:15px; font-size:13px;"><a href="https://www.youtube.com/@TopSchoolsRankings" target="_blank" rel="noopener noreferrer" style="color:#a9b8ca; text-decoration:none;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#a9b8ca'" aria-label="YouTube"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor" style="display:block;"><path d="M23.498 6.186a3.016 3.016 0 00-2.122-2.136C19.505 3.5 12 3.5 12 3.5s-7.505 0-9.377.55a3.016 3.016 0 00-2.122 2.136C0 8.07 0 12 0 12s0 3.93.501 5.814a3.016 3.016 0 002.122 2.136c1.872.55 9.377.55 9.377.55s7.505 0 9.377-.55a3.016 3.016 0 002.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg></a><a href="https://www.instagram.com/topschoolsrankings/" target="_blank" rel="noopener noreferrer" style="color:#a9b8ca; text-decoration:none;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#a9b8ca'" aria-label="Instagram"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor" style="display:block;"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4zm7.846-10.405a1.44 1.44 0 11-2.88 0 1.44 1.44 0 012.88 0z"/></svg></a><a href="https://www.facebook.com/topschoolsrankings/" target="_blank" rel="noopener noreferrer" style="color:#a9b8ca; text-decoration:none;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='#a9b8ca'" aria-label="Facebook"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor" style="display:block;"><path d="M22.675 0h-21.35C.593 0 0 .593 0 1.325v21.351C0 23.407.593 24 1.325 24H12.82v-9.294H9.692v-3.622h3.128V8.413c0-3.1 1.893-4.788 4.659-4.788 1.325 0 2.463.099 2.795.143v3.24l-1.918.001c-1.504 0-1.795.715-1.795 1.763v2.313h3.587l-.467 3.622h-3.12V24h6.116c.73 0 1.323-.593 1.323-1.325V1.325C24 .593 23.407 0 22.675 0z"/></svg></a></div></div>
    <div><h2>Research</h2><a href="/blogs/">All guides</a><a href="/listings/">Listings</a><a href="/compare/">Comparisons</a><a href="/tools/">Student tools</a></div>
    <div><h2>Standards</h2><a href="/ranking-methodology/">Ranking methodology</a><a href="/editorial-policy/">Editorial policy</a><a href="/author/saahil/">Our writer</a><a href="/about-us/">About us</a></div>
    <div><h2>Legal</h2><a href="/privacy-policy/">Privacy policy</a><a href="/terms-and-conditions/">Terms &amp; conditions</a><a href="/disclaimer/">Disclaimer</a><a href="/contact-us/">Contact us</a></div>
  </div><div class="site-container footer-bottom"><p>© 2026 Top Schools Rankings. Educational information only.</p><p>Advertising, when enabled, is visually separated from editorial content.</p></div></footer></body></html>"""

with open("tools/wam-calculator/index.html", "w", encoding="utf-8") as f:
    f.write(wam_content)

# Add to tools index page
with open("tools/index.html", "r", encoding="utf-8") as f:
    index_content = f.read()

new_card = """<article class="listing-card" style="border-top: 4px solid #17a2b8; padding-top: 20px;"><svg style="width:32px; height:32px; margin-bottom:15px; color:#17a2b8; display:block;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="9" y1="9" x2="15" y2="15"></line><line x1="15" y1="9" x2="9" y2="15"></line></svg> <span>High Demand Tool 🔥</span><h2><a href="/tools/wam-calculator/">WAM Calculator</a></h2><p>Calculate your Weighted Average Mark (WAM) for Monash, Melbourne, UNSW, and other Australian universities.</p><a href="/tools/wam-calculator/">Use tool →</a></article>
"""

# Insert right after the opening tag of <div class="listing-grid tools-directory">
index_content = index_content.replace('<div class="listing-grid tools-directory">', '<div class="listing-grid tools-directory">\n' + new_card)

# Update the count
index_content = index_content.replace("36 free education", "37 free education").replace("36 tools", "37 tools")

with open("tools/index.html", "w", encoding="utf-8") as f:
    f.write(index_content)

print("WAM Calculator created successfully!")
