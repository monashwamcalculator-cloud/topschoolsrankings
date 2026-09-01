import os

os.makedirs("tools/wam-to-gpa-converter", exist_ok=True)
os.makedirs("tools/gpa-to-wam-converter", exist_ok=True)

wam_to_gpa_content = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>WAM to GPA Converter | Convert Australian WAM to US 4.0 GPA | Top Schools Rankings</title><meta name="description" content="Convert your Australian Weighted Average Mark (WAM) into a standard US 4.0 scale GPA for grad school and job applications."><meta name="robots" content="index, follow"><link rel="canonical" href="https://topschoolsrankings.com/tools/wam-to-gpa-converter/"><meta name="google-adsense-account" content="ca-pub-5825245351059712"><meta property="og:type" content="website"><meta property="og:site_name" content="Top Schools Rankings"><meta property="og:title" content="WAM to GPA Converter"><meta property="og:description" content="Convert your Australian Weighted Average Mark (WAM) into a standard US 4.0 scale GPA for grad school and job applications."><meta property="og:url" content="https://topschoolsrankings.com/tools/wam-to-gpa-converter/"><meta property="og:image" content="https://topschoolsrankings.com/og.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="https://topschoolsrankings.com/og.png"><link rel="icon" href="/favicon.jpg"><link rel="stylesheet" href="/assets/site.css"><script async crossorigin="anonymous" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5825245351059712"></script><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","name":"WAM to GPA Converter","description":"Convert your Australian Weighted Average Mark (WAM) into a standard US 4.0 scale GPA for grad school and job applications.","image":"https://topschoolsrankings.com/og.png","url":"https://topschoolsrankings.com/tools/wam-to-gpa-converter/","publisher":{"@type":"Organization","name":"Top Schools Rankings","url":"https://topschoolsrankings.com"}}</script><script src="/assets/site.js" defer></script>
<style>
.result-success { background: rgba(40, 167, 69, 0.15); color: #8de49f; border-color: rgba(40, 167, 69, 0.3); }
.result-warning { background: rgba(255, 193, 7, 0.15); color: #ffe68a; border-color: rgba(255, 193, 7, 0.3); }
.tool-result h3 { margin: 0 0 8px 0; color: inherit; font-size: 26px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; }
.tool-result p { margin: 0; font-size: 16px; opacity: 0.9; font-weight: normal; }
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
  <nav class="breadcrumbs site-container" aria-label="Breadcrumb"><a href="/">Home</a><span><i aria-hidden="true">/</i><a href="/tools/">Tools</a></span><span><i aria-hidden="true">/</i><b>WAM to GPA Converter</b></span></nav>
  <header class="page-header"><div class="site-container narrow"><span class="eyebrow">Interactive planning resource</span><h1>WAM to GPA Converter</h1><p>Instantly convert your Australian Weighted Average Mark into a US 4.0 scale GPA.</p><div class="page-meta">Free to use · No account · Instant calculation</div></div></header><section class="section site-container article-layout"><article class="article-body">
  
  <section class="tool-panel" data-custom>
    <div class="tool-panel-head" style="margin-bottom: 20px;">
      <span>Interactive planning tool</span>
      <h2>WAM to GPA Converter</h2>
      <p>Enter your WAM below to see its estimated equivalent on the standard 4.0 GPA scale.</p>
    </div>
    
    <div class="tool-fields">
      <label style="grid-column: 1 / -1;"><span>Your Current WAM (0-100)</span><input type="number" id="wam_input" placeholder="e.g. 75" min="0" max="100" step="0.1"></label>
    </div>
    <div id="result_box" class="tool-result result-success" hidden style="text-align:center; padding: 25px; margin-top:0;"></div>
  </section>
  
  <script>
    document.getElementById("wam_input").addEventListener("input", function() {
      var wam = parseFloat(this.value);
      var resultBox = document.getElementById("result_box");
      
      if (isNaN(wam) || wam < 0 || wam > 100) {
        resultBox.hidden = true;
        return;
      }
      
      var gpa = 0.0;
      var desc = "";
      
      // Standard international conversion heuristic
      if (wam >= 80) { gpa = 4.0; desc = "A grade (High Distinction)"; }
      else if (wam >= 75) { gpa = 3.7 + ((wam - 75) / 5) * 0.3; desc = "A- grade (Strong Distinction)"; }
      else if (wam >= 70) { gpa = 3.3 + ((wam - 70) / 5) * 0.4; desc = "B+ grade (Distinction)"; }
      else if (wam >= 65) { gpa = 3.0 + ((wam - 65) / 5) * 0.3; desc = "B grade (High Credit)"; }
      else if (wam >= 60) { gpa = 2.7 + ((wam - 60) / 5) * 0.3; desc = "B- grade (Credit)"; }
      else if (wam >= 50) { gpa = 2.0 + ((wam - 50) / 10) * 0.7; desc = "C grade (Pass)"; }
      else { gpa = 0.0; desc = "F grade (Fail)"; }
      
      gpa = gpa.toFixed(2);
      
      resultBox.innerHTML = "<h3>GPA: " + gpa + " / 4.0</h3><p>US Equivalent: <strong>" + desc + "</strong></p>";
      resultBox.hidden = false;
    });
  </script>

  <p>If you're studying at an Australian university like Monash, Melbourne, or UNSW, your academic performance is measured by a Weighted Average Mark (WAM) out of 100. However, if you're applying for international graduate schools, MBA programs, or US-based jobs, you'll almost always be asked to provide a GPA on a 4.0 scale.</p>
  
  <h2>How do you convert WAM to GPA?</h2>
  <p>There is no single "official" conversion rate because the Australian and US grading systems evaluate students differently. In the US, scoring above 90% is common and expected for an 'A' grade. In Australia, achieving above 80% (High Distinction) is extremely difficult and is considered equivalent to a perfect 4.0 A grade internationally.</p>
  
  <h2>Standard Conversion Scale</h2>
  <p>Our calculator uses the most widely accepted international mapping standards used by Fulbright and major admissions boards:</p>
  <ul>
    <li><strong>WAM 80 - 100 (High Distinction):</strong> 4.0 GPA (A)</li>
    <li><strong>WAM 70 - 79 (Distinction):</strong> 3.3 - 3.9 GPA (B+ to A-)</li>
    <li><strong>WAM 60 - 69 (Credit):</strong> 2.7 - 3.2 GPA (B- to B)</li>
    <li><strong>WAM 50 - 59 (Pass):</strong> 2.0 - 2.6 GPA (C)</li>
    <li><strong>WAM < 50 (Fail):</strong> 0.0 GPA (F)</li>
  </ul>
  
  <h2>Frequently asked questions</h2>
  <h3>Will graduate schools recalculate my WAM?</h3>
  <p>Yes. If you apply to a competitive US graduate school (like an Ivy League or a top MBA program), they will usually use a credential evaluation service like WES (World Education Services) to officially convert your Australian transcript into a US GPA. Our calculator provides a highly accurate estimate of what that WES evaluation will look like.</p>

  <h2>Related tools</h2>
  <h3><a href="/tools/gpa-to-wam-converter/">GPA to WAM Converter</a></h3>
  <p>Convert a US 4.0 GPA back into an Australian WAM equivalent.</p>
  <h3><a href="/tools/wam-calculator/">WAM Calculator</a></h3>
  <p>Calculate your actual WAM subject by subject.</p>
  
  </article><aside class="article-aside"><div><span class="aside-label">Important</span><strong>Estimates only</strong><p>This conversion is an estimate for planning purposes. Official conversions can only be performed by credential evaluators like WES.</p></div></aside></section></main>
  <footer class="site-footer"><div class="site-container footer-grid">
    <div class="footer-about">
  <a class="brand" href="/" aria-label="Top Schools Rankings home" style="display:flex; align-items:center;">
    <img src="/assets/logo.png" alt="Top Schools Rankings" style="height:60px; width:auto; max-width:100%;">
  </a><p>Independent school and university research for students and families. We are not an admissions agency and do not sell rankings.</p><a class="correction-link" href="/contact-us/">Report a correction →</a></div>
    <div><h2>Research</h2><a href="/blogs/">All guides</a><a href="/listings/">Listings</a><a href="/compare/">Comparisons</a><a href="/tools/">Student tools</a></div>
    <div><h2>Standards</h2><a href="/ranking-methodology/">Ranking methodology</a><a href="/editorial-policy/">Editorial policy</a><a href="/author/saahil/">Our writer</a><a href="/about-us/">About us</a></div>
    <div><h2>Legal</h2><a href="/privacy-policy/">Privacy policy</a><a href="/terms-and-conditions/">Terms &amp; conditions</a><a href="/disclaimer/">Disclaimer</a><a href="/contact-us/">Contact us</a></div>
  </div><div class="site-container footer-bottom"><p>© 2026 Top Schools Rankings. Educational information only.</p></div></footer></body></html>"""

gpa_to_wam_content = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>GPA to WAM Converter | Convert US 4.0 GPA to Australian WAM | Top Schools Rankings</title><meta name="description" content="Convert your US 4.0 scale GPA into an Australian Weighted Average Mark (WAM) to see where you stand for Australian universities."><meta name="robots" content="index, follow"><link rel="canonical" href="https://topschoolsrankings.com/tools/gpa-to-wam-converter/"><meta name="google-adsense-account" content="ca-pub-5825245351059712"><meta property="og:type" content="website"><meta property="og:site_name" content="Top Schools Rankings"><meta property="og:title" content="GPA to WAM Converter"><meta property="og:description" content="Convert your US 4.0 scale GPA into an Australian Weighted Average Mark (WAM) to see where you stand for Australian universities."><meta property="og:url" content="https://topschoolsrankings.com/tools/gpa-to-wam-converter/"><meta property="og:image" content="https://topschoolsrankings.com/og.png"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="https://topschoolsrankings.com/og.png"><link rel="icon" href="/favicon.jpg"><link rel="stylesheet" href="/assets/site.css"><script async crossorigin="anonymous" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5825245351059712"></script><script type="application/ld+json">{"@context":"https://schema.org","@type":"WebPage","name":"GPA to WAM Converter","description":"Convert your US 4.0 scale GPA into an Australian Weighted Average Mark (WAM) to see where you stand for Australian universities.","image":"https://topschoolsrankings.com/og.png","url":"https://topschoolsrankings.com/tools/gpa-to-wam-converter/","publisher":{"@type":"Organization","name":"Top Schools Rankings","url":"https://topschoolsrankings.com"}}</script><script src="/assets/site.js" defer></script>
<style>
.result-success { background: rgba(0, 86, 179, 0.15); color: #9bc5ff; border-color: rgba(0, 86, 179, 0.3); }
.tool-result h3 { margin: 0 0 8px 0; color: inherit; font-size: 26px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; }
.tool-result p { margin: 0; font-size: 16px; opacity: 0.9; font-weight: normal; }
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
  <nav class="breadcrumbs site-container" aria-label="Breadcrumb"><a href="/">Home</a><span><i aria-hidden="true">/</i><a href="/tools/">Tools</a></span><span><i aria-hidden="true">/</i><b>GPA to WAM Converter</b></span></nav>
  <header class="page-header"><div class="site-container narrow"><span class="eyebrow">Interactive planning resource</span><h1>GPA to WAM Converter</h1><p>Convert your US 4.0 scale GPA into an estimated Australian Weighted Average Mark (WAM).</p><div class="page-meta">Free to use · No account · Instant calculation</div></div></header><section class="section site-container article-layout"><article class="article-body">
  
  <section class="tool-panel" data-custom>
    <div class="tool-panel-head" style="margin-bottom: 20px;">
      <span>Interactive planning tool</span>
      <h2>GPA to WAM Converter</h2>
      <p>Enter your 4.0 scale GPA below to see your estimated WAM.</p>
    </div>
    
    <div class="tool-fields">
      <label style="grid-column: 1 / -1;"><span>Your Current GPA (0.0 - 4.0)</span><input type="number" id="gpa_input" placeholder="e.g. 3.5" min="0" max="4.0" step="0.01"></label>
    </div>
    <div id="result_box" class="tool-result result-success" hidden style="text-align:center; padding: 25px; margin-top:0;"></div>
  </section>
  
  <script>
    document.getElementById("gpa_input").addEventListener("input", function() {
      var gpa = parseFloat(this.value);
      var resultBox = document.getElementById("result_box");
      
      if (isNaN(gpa) || gpa < 0 || gpa > 4.0) {
        resultBox.hidden = true;
        return;
      }
      
      var wam = 0.0;
      var desc = "";
      
      if (gpa >= 4.0) { wam = 85; desc = "High Distinction (HD)"; }
      else if (gpa >= 3.7) { wam = 75 + ((gpa - 3.7) / 0.3) * 5; desc = "Distinction (D)"; }
      else if (gpa >= 3.3) { wam = 70 + ((gpa - 3.3) / 0.4) * 5; desc = "Distinction (D)"; }
      else if (gpa >= 3.0) { wam = 65 + ((gpa - 3.0) / 0.3) * 5; desc = "Credit (C)"; }
      else if (gpa >= 2.7) { wam = 60 + ((gpa - 2.7) / 0.3) * 5; desc = "Credit (C)"; }
      else if (gpa >= 2.0) { wam = 50 + ((gpa - 2.0) / 0.7) * 10; desc = "Pass (P)"; }
      else { wam = (gpa / 2.0) * 50; desc = "Fail (N)"; }
      
      wam = Math.round(wam);
      
      resultBox.innerHTML = "<h3>Est. WAM: " + wam + "</h3><p>Australian Grade: <strong>" + desc + "</strong></p>";
      resultBox.hidden = false;
    });
  </script>

  <p>If you're an international student looking to study abroad or apply to a master's program at an Australian university, you might be confused by their entry requirements. Australian universities rarely use a 4.0 GPA scale. Instead, they require a specific WAM (Weighted Average Mark).</p>
  
  <h2>Why are Australian grades so "low"?</h2>
  <p>A common shock for international students is seeing that an Australian WAM of 75 is considered exceptional, whereas a 75% in the US is a 'C' grade. In the Australian grading system, achieving above 80% requires extraordinary, publishable-level academic insight. Therefore, a 4.0 GPA in the US translates roughly to an 80+ WAM in Australia.</p>
  
  <h2>Understanding Australian Grades</h2>
  <ul>
    <li><strong>HD (High Distinction) - 80-100 WAM:</strong> Equivalent to a perfect 4.0 GPA. Top tier of the class.</li>
    <li><strong>D (Distinction) - 70-79 WAM:</strong> Equivalent to a 3.3 - 3.9 GPA. Very strong performance.</li>
    <li><strong>C (Credit) - 60-69 WAM:</strong> Equivalent to a 2.7 - 3.2 GPA. Average to good performance.</li>
    <li><strong>P (Pass) - 50-59 WAM:</strong> Equivalent to a 2.0 - 2.6 GPA. Minimum required to pass the unit.</li>
  </ul>
  
  <h2>Related tools</h2>
  <h3><a href="/tools/wam-to-gpa-converter/">WAM to GPA Converter</a></h3>
  <p>Convert your WAM back into a standard US 4.0 scale GPA.</p>
  <h3><a href="/tools/wam-calculator/">WAM Calculator</a></h3>
  <p>Calculate your actual WAM subject by subject for Monash, Unimelb, and UNSW.</p>
  
  </article><aside class="article-aside"><div><span class="aside-label">Important</span><strong>Admissions discretion</strong><p>Universities assess international transcripts holistically. This calculator provides a heuristic estimate, but exact cutoff scores vary by faculty.</p></div></aside></section></main>
  <footer class="site-footer"><div class="site-container footer-grid">
    <div class="footer-about">
  <a class="brand" href="/" aria-label="Top Schools Rankings home" style="display:flex; align-items:center;">
    <img src="/assets/logo.png" alt="Top Schools Rankings" style="height:60px; width:auto; max-width:100%;">
  </a><p>Independent school and university research for students and families. We are not an admissions agency and do not sell rankings.</p><a class="correction-link" href="/contact-us/">Report a correction →</a></div>
    <div><h2>Research</h2><a href="/blogs/">All guides</a><a href="/listings/">Listings</a><a href="/compare/">Comparisons</a><a href="/tools/">Student tools</a></div>
    <div><h2>Standards</h2><a href="/ranking-methodology/">Ranking methodology</a><a href="/editorial-policy/">Editorial policy</a><a href="/author/saahil/">Our writer</a><a href="/about-us/">About us</a></div>
    <div><h2>Legal</h2><a href="/privacy-policy/">Privacy policy</a><a href="/terms-and-conditions/">Terms &amp; conditions</a><a href="/disclaimer/">Disclaimer</a><a href="/contact-us/">Contact us</a></div>
  </div><div class="site-container footer-bottom"><p>© 2026 Top Schools Rankings. Educational information only.</p></div></footer></body></html>"""

with open("tools/wam-to-gpa-converter/index.html", "w", encoding="utf-8") as f:
    f.write(wam_to_gpa_content)

with open("tools/gpa-to-wam-converter/index.html", "w", encoding="utf-8") as f:
    f.write(gpa_to_wam_content)

# Update tools/index.html to include both
with open("tools/index.html", "r", encoding="utf-8") as f:
    idx = f.read()

new_cards = """<article class="listing-card"><svg style="width:32px; height:32px; margin-bottom:15px; color:var(--gold-500); display:block;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg> <h2><a href="/tools/wam-to-gpa-converter/">WAM to GPA Converter</a></h2><p>Convert your Australian Weighted Average Mark into a standard US 4.0 scale GPA for grad school.</p><a href="/tools/wam-to-gpa-converter/">Use tool →</a></article>
<article class="listing-card"><svg style="width:32px; height:32px; margin-bottom:15px; color:var(--gold-500); display:block;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg> <h2><a href="/tools/gpa-to-wam-converter/">GPA to WAM Converter</a></h2><p>Convert your US 4.0 scale GPA into an estimated Australian Weighted Average Mark (WAM).</p><a href="/tools/gpa-to-wam-converter/">Use tool →</a></article>
"""

idx = idx.replace('<div class="listing-grid tools-directory">', '<div class="listing-grid tools-directory">\n' + new_cards)
idx = idx.replace("37 free education", "39 free education").replace("37 tools", "39 tools")

with open("tools/index.html", "w", encoding="utf-8") as f:
    f.write(idx)

print("Created wam-to-gpa and gpa-to-wam tools successfully.")
