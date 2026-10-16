import os
import xml.etree.ElementTree as ET

os.makedirs("media/articles", exist_ok=True)

svg1 = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675" role="img" aria-labelledby="vsm-title vsm-desc">
  <title id="vsm-title">US Veterinary School Admissions Evaluation Weights (2026)</title>
  <desc id="vsm-desc">Empirical multi-factor criteria used by AVMA-accredited DVM admissions committees: Science &amp; Prerequisite GPA 35%, Veterinary &amp; Clinical Experience 25%, Evaluator Recommendations 15%, Casper Situational Judgment 15%, Personal Statement 10%.</desc>
  <defs>
    <linearGradient id="bg-grad-1" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#f8fafc"/>
    </linearGradient>
    <filter id="shadow-1" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.04"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1200" height="675" fill="url(#bg-grad-1)"/>
  <rect width="1200" height="675" fill="none" stroke="#e2e8f0" stroke-width="2"/>
  <line x1="0" y1="5" x2="1200" y2="5" stroke="#2563eb" stroke-width="8"/>

  <!-- Header Section -->
  <text x="60" y="58" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="13" font-weight="700" fill="#2563eb" letter-spacing="1.5">TOP SCHOOLS RANKINGS • ADMISSIONS EVALUATION MODEL</text>
  <text x="60" y="98" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="28" font-weight="800" fill="#0f2237">US Veterinary School Admissions Criteria &amp; Weights (2026)</text>
  <text x="60" y="128" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="15" fill="#64748b">Empirical evaluation standards prioritized by AVMA Council on Education accredited DVM selection committees</text>

  <!-- Overview Summary Bar -->
  <g transform="translate(60, 150)">
    <rect width="1080" height="24" rx="6" fill="#e2e8f0"/>
    <rect x="0" width="378" height="24" rx="6" fill="#1e40af"/>
    <rect x="378" width="270" height="24" fill="#059669"/>
    <rect x="648" width="162" height="24" fill="#d97706"/>
    <rect x="810" width="162" height="24" fill="#7c3aed"/>
    <rect x="972" width="108" height="24" rx="6" fill="#e11d48"/>
  </g>

  <!-- Criteria Card 1: Science GPA -->
  <g transform="translate(60, 195)" filter="url(#shadow-1)">
    <rect width="1080" height="74" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.2"/>
    <rect x="0" y="0" width="8" height="74" rx="4" fill="#1e40af"/>
    <text x="28" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="17" font-weight="700" fill="#0f2237">Science &amp; Prerequisite Cumulative GPA</text>
    <text x="28" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="13" fill="#64748b">Biochemistry, Organic Chemistry, Genetics, Cellular Biology &amp; Physics academic rigor</text>
    <rect x="820" y="24" width="150" height="26" rx="13" fill="#eff6ff"/>
    <text x="895" y="42" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" font-weight="600" fill="#1d4ed8">Benchmark: 3.70+ GPA</text>
    <text x="1045" y="46" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="24" font-weight="800" fill="#1e40af">35%</text>
  </g>

  <!-- Criteria Card 2: Veterinary Experience -->
  <g transform="translate(60, 280)" filter="url(#shadow-1)">
    <rect width="1080" height="74" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.2"/>
    <rect x="0" y="0" width="8" height="74" rx="4" fill="#059669"/>
    <text x="28" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="17" font-weight="700" fill="#0f2237">Veterinary &amp; Clinical Experience Hours</text>
    <text x="28" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="13" fill="#64748b">Direct shadowing with licensed DVMs, clinical observation, surgical prep &amp; animal care duties</text>
    <rect x="820" y="24" width="150" height="26" rx="13" fill="#ecfdf5"/>
    <text x="895" y="42" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" font-weight="600" fill="#047857">Target: 400–1,000+ Hrs</text>
    <text x="1045" y="46" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="24" font-weight="800" fill="#059669">25%</text>
  </g>

  <!-- Criteria Card 3: Evaluator Letters -->
  <g transform="translate(60, 365)" filter="url(#shadow-1)">
    <rect width="1080" height="74" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.2"/>
    <rect x="0" y="0" width="8" height="74" rx="4" fill="#d97706"/>
    <text x="28" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="17" font-weight="700" fill="#0f2237">Evaluator Letters of Recommendation (eLORs)</text>
    <text x="28" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="13" fill="#64748b">Minimum two letters from practicing DVMs confirming ethical aptitude &amp; clinical acumen</text>
    <rect x="820" y="24" width="150" height="26" rx="13" fill="#fffbeb"/>
    <text x="895" y="42" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" font-weight="600" fill="#b45309">2 DVMs + 1 Academic</text>
    <text x="1045" y="46" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="24" font-weight="800" fill="#d97706">15%</text>
  </g>

  <!-- Criteria Card 4: Casper Assessment -->
  <g transform="translate(60, 450)" filter="url(#shadow-1)">
    <rect width="1080" height="74" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.2"/>
    <rect x="0" y="0" width="8" height="74" rx="4" fill="#7c3aed"/>
    <text x="28" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="17" font-weight="700" fill="#0f2237">Acuity Insights Casper Assessment</text>
    <text x="28" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="13" fill="#64748b">Online situational judgment test evaluating empathy, ethical conflict resolution &amp; teamwork</text>
    <rect x="820" y="24" width="150" height="26" rx="13" fill="#f5f3ff"/>
    <text x="895" y="42" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" font-weight="600" fill="#6d28d9">Q4 Score Benchmark</text>
    <text x="1045" y="46" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="24" font-weight="800" fill="#7c3aed">15%</text>
  </g>

  <!-- Criteria Card 5: Personal Statement -->
  <g transform="translate(60, 535)" filter="url(#shadow-1)">
    <rect width="1080" height="74" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.2"/>
    <rect x="0" y="0" width="8" height="74" rx="4" fill="#e11d48"/>
    <text x="28" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="17" font-weight="700" fill="#0f2237">Personal Statement, Leadership &amp; Diversity</text>
    <text x="28" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="13" fill="#64748b">Clear professional vision, resilience under pressure, community service &amp; life perspective</text>
    <rect x="820" y="24" width="150" height="26" rx="13" fill="#fff1f2"/>
    <text x="895" y="42" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" font-weight="600" fill="#be123c">Holistic Essay Review</text>
    <text x="1045" y="46" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="24" font-weight="800" fill="#e11d48">10%</text>
  </g>

  <!-- Footer -->
  <line x1="60" y1="630" x2="1140" y2="630" stroke="#cbd5e1" stroke-width="1"/>
  <text x="60" y="652" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" fill="#64748b">Source: AAVMC Annual Data Report &amp; AVMA Council on Education Admissions Guidelines (2025/2026 Cycle).</text>
  <text x="1140" y="652" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" font-weight="600" fill="#0f2237">TopSchoolsRankings.com Research</text>
</svg>"""

svg2 = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675" role="img" aria-labelledby="vst-title vst-desc">
  <title id="vst-title">Elite US Veterinary Medical Colleges Comparison (Top 5 Overview)</title>
  <desc id="vst-desc">Comparative breakdown of top 5 US veterinary schools: UC Davis, Cornell University, Colorado State University, North Carolina State, and Ohio State University across NAVLE pass rates, tuition, and clinical caseload.</desc>
  <defs>
    <linearGradient id="bg-grad-2" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#f8fafc"/>
    </linearGradient>
    <filter id="shadow-2" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.04"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1200" height="675" fill="url(#bg-grad-2)"/>
  <rect width="1200" height="675" fill="none" stroke="#e2e8f0" stroke-width="2"/>
  <line x1="0" y1="5" x2="1200" y2="5" stroke="#059669" stroke-width="8"/>

  <!-- Header Section -->
  <text x="60" y="58" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="13" font-weight="700" fill="#059669" letter-spacing="1.5">TSR EDITORIAL DATASET • INSTITUTIONAL COMPARISON</text>
  <text x="60" y="98" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="28" font-weight="800" fill="#0f2237">Top 5 US Veterinary Schools: Key Metrics Comparison</text>
  <text x="60" y="128" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="15" fill="#64748b">Comparing 5-year NAVLE pass rates, estimated annual tuition, clinical hospital volume &amp; core research strengths</text>

  <!-- Column Headers -->
  <g transform="translate(60, 155)">
    <text x="20" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" font-weight="700" fill="#64748b">COLLEGE &amp; RANK</text>
    <text x="360" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" font-weight="700" fill="#64748b">ANNUAL TUITION (RES / NON-RES)</text>
    <text x="660" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" font-weight="700" fill="#64748b">NAVLE PASS RATE</text>
    <text x="860" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" font-weight="700" fill="#64748b">CLINICAL CASELOAD</text>
  </g>

  <!-- Row 1: UC Davis -->
  <g transform="translate(60, 175)" filter="url(#shadow-2)">
    <rect width="1080" height="78" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.2"/>
    <circle cx="36" cy="39" r="18" fill="#eff6ff"/>
    <text x="36" y="45" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="15" font-weight="800" fill="#1d4ed8">#1</text>
    <text x="68" y="34" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="16" font-weight="700" fill="#0f2237">University of California, Davis</text>
    <text x="68" y="54" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" fill="#64748b">Davis, CA • One Health Institute &amp; Equine Health Center</text>
    <text x="360" y="37" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="15" font-weight="600" fill="#0f2237">$36,800 / $49,000</text>
    <text x="360" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="11" fill="#64748b">In-state statutory subsidy</text>
    <rect x="660" y="24" width="75" height="28" rx="14" fill="#ecfdf5"/>
    <text x="697" y="43" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="13" font-weight="700" fill="#047857">98.2%</text>
    <text x="860" y="37" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="15" font-weight="600" fill="#0f2237">52,000+ cases/yr</text>
    <text x="860" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="11" fill="#64748b">William R. Pritchard Hospital</text>
  </g>

  <!-- Row 2: Cornell -->
  <g transform="translate(60, 265)" filter="url(#shadow-2)">
    <rect width="1080" height="78" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.2"/>
    <circle cx="36" cy="39" r="18" fill="#eff6ff"/>
    <text x="36" y="45" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="15" font-weight="800" fill="#1d4ed8">#2</text>
    <text x="68" y="34" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="16" font-weight="700" fill="#0f2237">Cornell University</text>
    <text x="68" y="54" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" fill="#64748b">Ithaca, NY • Problem-Based Learning &amp; Wildlife Health Center</text>
    <text x="360" y="37" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="15" font-weight="600" fill="#0f2237">$44,200 / $65,500</text>
    <text x="360" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="11" fill="#64748b">Contract college framework</text>
    <rect x="660" y="24" width="75" height="28" rx="14" fill="#ecfdf5"/>
    <text x="697" y="43" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="13" font-weight="700" fill="#047857">97.5%</text>
    <text x="860" y="37" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="15" font-weight="600" fill="#0f2237">30,000+ cases/yr</text>
    <text x="860" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="11" fill="#64748b">Hospital for Animals</text>
  </g>

  <!-- Row 3: Colorado State -->
  <g transform="translate(60, 355)" filter="url(#shadow-2)">
    <rect width="1080" height="78" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.2"/>
    <circle cx="36" cy="39" r="18" fill="#eff6ff"/>
    <text x="36" y="45" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="15" font-weight="800" fill="#1d4ed8">#3</text>
    <text x="68" y="34" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="16" font-weight="700" fill="#0f2237">Colorado State University</text>
    <text x="68" y="54" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" fill="#64748b">Fort Collins, CO • Flint Animal Cancer Center &amp; Orthopedics</text>
    <text x="360" y="37" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="15" font-weight="600" fill="#0f2237">$37,400 / $64,800</text>
    <text x="360" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="11" fill="#64748b">In-state petition after Year 1</text>
    <rect x="660" y="24" width="75" height="28" rx="14" fill="#ecfdf5"/>
    <text x="697" y="43" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="13" font-weight="700" fill="#047857">96.8%</text>
    <text x="860" y="37" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="15" font-weight="600" fill="#0f2237">45,000+ cases/yr</text>
    <text x="860" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="11" fill="#64748b">James L. Voss Teaching Hospital</text>
  </g>

  <!-- Row 4: NC State -->
  <g transform="translate(60, 445)" filter="url(#shadow-2)">
    <rect width="1080" height="78" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.2"/>
    <circle cx="36" cy="39" r="18" fill="#eff6ff"/>
    <text x="36" y="45" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="15" font-weight="800" fill="#1d4ed8">#4</text>
    <text x="68" y="34" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="16" font-weight="700" fill="#0f2237">North Carolina State University</text>
    <text x="68" y="54" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" fill="#64748b">Raleigh, NC • Equine &amp; Farm Animal Clinical Operations</text>
    <text x="360" y="37" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="15" font-weight="600" fill="#0f2237">$23,900 / $51,200</text>
    <text x="360" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="11" fill="#64748b">Lowest in-state cost index</text>
    <rect x="660" y="24" width="75" height="28" rx="14" fill="#ecfdf5"/>
    <text x="697" y="43" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="13" font-weight="700" fill="#047857">96.4%</text>
    <text x="860" y="37" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="15" font-weight="600" fill="#0f2237">38,000+ cases/yr</text>
    <text x="860" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="11" fill="#64748b">NC State Veterinary Hospital</text>
  </g>

  <!-- Row 5: Ohio State -->
  <g transform="translate(60, 535)" filter="url(#shadow-2)">
    <rect width="1080" height="78" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.2"/>
    <circle cx="36" cy="39" r="18" fill="#eff6ff"/>
    <text x="36" y="45" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="15" font-weight="800" fill="#1d4ed8">#5</text>
    <text x="68" y="34" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="16" font-weight="700" fill="#0f2237">Ohio State University</text>
    <text x="68" y="54" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" fill="#64748b">Columbus, OH • Frank Stanton Spectrum of Care Clinic</text>
    <text x="360" y="37" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="15" font-weight="600" fill="#0f2237">$36,400 / $77,800</text>
    <text x="360" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="11" fill="#64748b">Comprehensive DVM cohort</text>
    <rect x="660" y="24" width="75" height="28" rx="14" fill="#ecfdf5"/>
    <text x="697" y="43" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="13" font-weight="700" fill="#047857">95.8%</text>
    <text x="860" y="37" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="15" font-weight="600" fill="#0f2237">42,000+ cases/yr</text>
    <text x="860" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="11" fill="#64748b">Hummel &amp; Galbreath Centers</text>
  </g>

  <!-- Footer -->
  <line x1="60" y1="630" x2="1140" y2="630" stroke="#cbd5e1" stroke-width="1"/>
  <text x="60" y="652" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" fill="#64748b">Data compiled from official AVMA Council on Education accreditation reports and university disclosures (2025/2026).</text>
  <text x="1140" y="652" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" font-weight="600" fill="#0f2237">TopSchoolsRankings.com Research</text>
</svg>"""

svg3 = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675" role="img" aria-labelledby="vsr-title vsr-desc">
  <title id="vsr-title">Strategic VMCAS Veterinary Application Roadmap (Cycle 2026)</title>
  <desc id="vsr-desc">Four-phase admissions roadmap for US veterinary colleges: Phase 1 Prerequisite Audit &amp; Shadowing, Phase 2 VMCAS Portal &amp; Experience Log, Phase 3 Casper Assessment &amp; Final Submission, Phase 4 Supplemental Applications &amp; Interviews.</desc>
  <defs>
    <linearGradient id="bg-grad-3" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#f8fafc"/>
    </linearGradient>
    <filter id="shadow-3" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.04"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1200" height="675" fill="url(#bg-grad-3)"/>
  <rect width="1200" height="675" fill="none" stroke="#e2e8f0" stroke-width="2"/>
  <line x1="0" y1="5" x2="1200" y2="5" stroke="#7c3aed" stroke-width="8"/>

  <!-- Header Section -->
  <text x="60" y="58" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="13" font-weight="700" fill="#7c3aed" letter-spacing="1.5">ADMISSIONS STRATEGY ROADMAP • 12-MONTH TIMELINE</text>
  <text x="60" y="98" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="28" font-weight="800" fill="#0f2237">VMCAS Application Lifecycle &amp; Strategic Milestones</text>
  <text x="60" y="128" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="15" fill="#64748b">Operational steps required to assemble a competitive Doctor of Veterinary Medicine (DVM) submission</text>

  <!-- Timeline Flow Connectors -->
  <g transform="translate(60, 160)">
    <!-- Phase 1 -->
    <g transform="translate(0, 0)" filter="url(#shadow-3)">
      <rect width="250" height="430" rx="10" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.2"/>
      <rect x="0" y="0" width="250" height="8" rx="4" fill="#2563eb"/>
      <circle cx="36" cy="42" r="16" fill="#eff6ff"/>
      <text x="36" y="47" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="14" font-weight="800" fill="#1d4ed8">1</text>
      <text x="62" y="36" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="13" font-weight="700" fill="#2563eb">PHASE 1</text>
      <text x="62" y="52" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="15" font-weight="800" fill="#0f2237">JANUARY – APRIL</text>
      <line x1="20" y1="72" x2="230" y2="72" stroke="#f1f5f9" stroke-width="1.5"/>
      <text x="20" y="100" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="14" font-weight="700" fill="#0f2237">Prerequisites &amp; Audits</text>
      <text x="20" y="124" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" fill="#475569" width="210">
        <tspan x="20" dy="0">• Audit science prerequisites</tspan>
        <tspan x="20" dy="18">  (Biochem, Genetics, Physics)</tspan>
        <tspan x="20" dy="24">• Log clinical hours with DVMs</tspan>
        <tspan x="20" dy="18">  (Target minimum 400+ hrs)</tspan>
        <tspan x="20" dy="24">• Order official transcripts</tspan>
        <tspan x="20" dy="18">  from all post-secondary units</tspan>
        <tspan x="20" dy="24">• Secure evaluation commitments</tspan>
        <tspan x="20" dy="18">  from 2 DVMs and 1 professor</tspan>
      </text>
      <rect x="20" y="375" width="210" height="32" rx="6" fill="#eff6ff"/>
      <text x="125" y="396" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="11" font-weight="700" fill="#1e40af">GOAL: 3.7+ SCIENCE GPA</text>
    </g>

    <!-- Phase 2 -->
    <g transform="translate(276, 0)" filter="url(#shadow-3)">
      <rect width="250" height="430" rx="10" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.2"/>
      <rect x="0" y="0" width="250" height="8" rx="4" fill="#059669"/>
      <circle cx="36" cy="42" r="16" fill="#ecfdf5"/>
      <text x="36" y="47" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="14" font-weight="800" fill="#047857">2</text>
      <text x="62" y="36" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="13" font-weight="700" fill="#059669">PHASE 2</text>
      <text x="62" y="52" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="15" font-weight="800" fill="#0f2237">MAY – JUNE</text>
      <line x1="20" y1="72" x2="230" y2="72" stroke="#f1f5f9" stroke-width="1.5"/>
      <text x="20" y="100" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="14" font-weight="700" fill="#0f2237">Portal &amp; Experience</text>
      <text x="20" y="124" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" fill="#475569">
        <tspan x="20" dy="0">• VMCAS portal opens early May</tspan>
        <tspan x="20" dy="18">  (Initialize candidate profile)</tspan>
        <tspan x="20" dy="24">• Categorize hours accurately:</tspan>
        <tspan x="20" dy="18">  Veterinary vs Animal Care</tspan>
        <tspan x="20" dy="24">• Enter coursework line-by-line</tspan>
        <tspan x="20" dy="18">  for professional transcript verify</tspan>
        <tspan x="20" dy="24">• Send automated eLOR links</tspan>
        <tspan x="20" dy="18">  directly to evaluator portals</tspan>
      </text>
      <rect x="20" y="375" width="210" height="32" rx="6" fill="#ecfdf5"/>
      <text x="125" y="396" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="11" font-weight="700" fill="#065f46">PORTAL INITIALIZATION</text>
    </g>

    <!-- Phase 3 -->
    <g transform="translate(552, 0)" filter="url(#shadow-3)">
      <rect width="250" height="430" rx="10" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.2"/>
      <rect x="0" y="0" width="250" height="8" rx="4" fill="#d97706"/>
      <circle cx="36" cy="42" r="16" fill="#fffbeb"/>
      <text x="36" y="47" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="14" font-weight="800" fill="#b45309">3</text>
      <text x="62" y="36" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="13" font-weight="700" fill="#d97706">PHASE 3</text>
      <text x="62" y="52" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="15" font-weight="800" fill="#0f2237">JULY – SEPTEMBER</text>
      <line x1="20" y1="72" x2="230" y2="72" stroke="#f1f5f9" stroke-width="1.5"/>
      <text x="20" y="100" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="14" font-weight="700" fill="#0f2237">Casper &amp; Deadline</text>
      <text x="20" y="124" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" fill="#475569">
        <tspan x="20" dy="0">• Schedule and sit for Casper</tspan>
        <tspan x="20" dy="18">  situational judgment test</tspan>
        <tspan x="20" dy="24">• Finalize personal statement</tspan>
        <tspan x="20" dy="18">  (5,000 character limit)</tspan>
        <tspan x="20" dy="24">• Complete institution-specific</tspan>
        <tspan x="20" dy="18">  custom essay prompts</tspan>
        <tspan x="20" dy="24">• Submit by mid-September</tspan>
        <tspan x="20" dy="18">  (Strict hard deadline cutoff)</tspan>
      </text>
      <rect x="20" y="375" width="210" height="32" rx="6" fill="#fffbeb"/>
      <text x="125" y="396" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="11" font-weight="700" fill="#92400e">SUBMISSION DEADLINE</text>
    </g>

    <!-- Phase 4 -->
    <g transform="translate(828, 0)" filter="url(#shadow-3)">
      <rect width="250" height="430" rx="10" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.2"/>
      <rect x="0" y="0" width="250" height="8" rx="4" fill="#7c3aed"/>
      <circle cx="36" cy="42" r="16" fill="#f5f3ff"/>
      <text x="36" y="47" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="14" font-weight="800" fill="#6d28d9">4</text>
      <text x="62" y="36" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="13" font-weight="700" fill="#7c3aed">PHASE 4</text>
      <text x="62" y="52" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="15" font-weight="800" fill="#0f2237">OCTOBER – APRIL</text>
      <line x1="20" y1="72" x2="230" y2="72" stroke="#f1f5f9" stroke-width="1.5"/>
      <text x="20" y="100" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="14" font-weight="700" fill="#0f2237">Interviews &amp; Offers</text>
      <text x="20" y="124" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" fill="#475569">
        <tspan x="20" dy="0">• Secondary supplemental review</tspan>
        <tspan x="20" dy="18">  and processing fees</tspan>
        <tspan x="20" dy="24">• Multiple Mini Interviews (MMI)</tspan>
        <tspan x="20" dy="18">  and faculty panel interviews</tspan>
        <tspan x="20" dy="24">• Admissions offers released</tspan>
        <tspan x="20" dy="18">  (Dec through February)</tspan>
        <tspan x="20" dy="24">• Seat deposit confirmation</tspan>
        <tspan x="20" dy="18">  by national deadline: April 15</tspan>
      </text>
      <rect x="20" y="375" width="210" height="32" rx="6" fill="#f5f3ff"/>
      <text x="125" y="396" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="11" font-weight="700" fill="#5b21b6">FINAL MATCH: APRIL 15</text>
    </g>
  </g>

  <!-- Footer -->
  <line x1="60" y1="630" x2="1140" y2="630" stroke="#cbd5e1" stroke-width="1"/>
  <text x="60" y="652" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" fill="#64748b">VMCAS Application timeline published by the American Association of Veterinary Medical Colleges.</text>
  <text x="1140" y="652" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" font-weight="600" fill="#0f2237">TopSchoolsRankings.com Research</text>
</svg>"""

svg4 = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675" role="img" aria-labelledby="vsc-title vsc-desc">
  <title id="vsc-title">Veterinary Medicine Career Distribution &amp; Financial ROI</title>
  <desc id="vsc-desc">Economic breakdown of DVM graduates: 67% Companion Animal, 12% Equine &amp; Food Animal, 9% Biomedical Research, 7% Public Health &amp; Government, 5% Zoo &amp; Wildlife, with starting salary and educational debt benchmarks.</desc>
  <defs>
    <linearGradient id="bg-grad-4" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="#f8fafc"/>
    </linearGradient>
    <filter id="shadow-4" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.04"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1200" height="675" fill="url(#bg-grad-4)"/>
  <rect width="1200" height="675" fill="none" stroke="#e2e8f0" stroke-width="2"/>
  <line x1="0" y1="5" x2="1200" y2="5" stroke="#d97706" stroke-width="8"/>

  <!-- Header Section -->
  <text x="60" y="58" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="13" font-weight="700" fill="#d97706" letter-spacing="1.5">ECONOMIC ANALYSIS • SALARY VS EDUCATIONAL DEBT PROFILE</text>
  <text x="60" y="98" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="28" font-weight="800" fill="#0f2237">Veterinary Medicine Career Distribution &amp; Financial Realities</text>
  <text x="60" y="128" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="15" fill="#64748b">Empirical market outcomes, starting associate compensation, and educational debt amortization</text>

  <!-- Panel 1: Career Distribution (Left, width 525) -->
  <g transform="translate(60, 160)" filter="url(#shadow-4)">
    <rect width="525" height="430" rx="10" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.2"/>
    <text x="28" y="38" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="18" font-weight="800" fill="#0f2237">DVM Practice Specialization Breakdown</text>
    <text x="28" y="58" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" fill="#64748b">Primary employment sector choices among recent graduates</text>

    <!-- Bar 1 -->
    <text x="28" y="100" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="14" font-weight="600" fill="#1e293b">Companion / Small Animal Clinical Practice</text>
    <text x="495" y="100" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="14" font-weight="700" fill="#2563eb">67%</text>
    <rect x="28" y="110" width="467" height="12" rx="4" fill="#f1f5f9"/>
    <rect x="28" y="110" width="313" height="12" rx="4" fill="#2563eb"/>

    <!-- Bar 2 -->
    <text x="28" y="160" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="14" font-weight="600" fill="#1e293b">Equine &amp; Food Animal / Mixed Practice</text>
    <text x="495" y="160" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="14" font-weight="700" fill="#059669">12%</text>
    <rect x="28" y="170" width="467" height="12" rx="4" fill="#f1f5f9"/>
    <rect x="28" y="170" width="56" height="12" rx="4" fill="#059669"/>

    <!-- Bar 3 -->
    <text x="28" y="220" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="14" font-weight="600" fill="#1e293b">Biomedical &amp; Pharmaceutical Research</text>
    <text x="495" y="220" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="14" font-weight="700" fill="#d97706">9%</text>
    <rect x="28" y="230" width="467" height="12" rx="4" fill="#f1f5f9"/>
    <rect x="28" y="230" width="42" height="12" rx="4" fill="#d97706"/>

    <!-- Bar 4 -->
    <text x="28" y="280" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="14" font-weight="600" fill="#1e293b">Public Health &amp; Government (USDA, CDC, Military)</text>
    <text x="495" y="280" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="14" font-weight="700" fill="#7c3aed">7%</text>
    <rect x="28" y="290" width="467" height="12" rx="4" fill="#f1f5f9"/>
    <rect x="28" y="290" width="33" height="12" rx="4" fill="#7c3aed"/>

    <!-- Bar 5 -->
    <text x="28" y="340" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="14" font-weight="600" fill="#1e293b">Zoological, Aquatic &amp; Wildlife Conservation</text>
    <text x="495" y="340" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="14" font-weight="700" fill="#e11d48">5%</text>
    <rect x="28" y="350" width="467" height="12" rx="4" fill="#f1f5f9"/>
    <rect x="28" y="350" width="23" height="12" rx="4" fill="#e11d48"/>

    <rect x="28" y="380" width="467" height="30" rx="6" fill="#f8fafc"/>
    <text x="261" y="400" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="11" fill="#64748b">Private clinical practice absorbs ~79% of all practicing US veterinarians</text>
  </g>

  <!-- Panel 2: Financial Metrics & Debt Profile (Right, width 525) -->
  <g transform="translate(615, 160)" filter="url(#shadow-4)">
    <rect width="525" height="430" rx="10" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.2"/>
    <text x="28" y="38" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="18" font-weight="800" fill="#0f2237">Financial Benchmarks &amp; Debt Realities</text>
    <text x="28" y="58" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" fill="#64748b">AVMA Economic Survey 2025/2026 Reporting Standards</text>

    <!-- Stat Box 1: Starting Salary -->
    <g transform="translate(28, 85)">
      <rect width="469" height="72" rx="8" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1"/>
      <text x="18" y="28" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" font-weight="700" fill="#1d4ed8">AVERAGE ENTRY ASSOCIATE SALARY</text>
      <text x="18" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="22" font-weight="800" fill="#0f2237">$105,000 – $125,000</text>
      <text x="450" y="52" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" font-weight="600" fill="#2563eb">+ Production Bonuses</text>
    </g>

    <!-- Stat Box 2: Mean Educational Debt -->
    <g transform="translate(28, 170)">
      <rect width="469" height="72" rx="8" fill="#fff1f2" stroke="#fecdd3" stroke-width="1"/>
      <text x="18" y="28" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" font-weight="700" fill="#be123c">MEAN GRADUATING EDUCATIONAL DEBT</text>
      <text x="18" y="55" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="22" font-weight="800" fill="#0f2237">$185,000 (In-State) / $275,000+ (Non-Res)</text>
    </g>

    <!-- Strategy Section -->
    <g transform="translate(28, 258)">
      <text x="0" y="20" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="13" font-weight="700" fill="#0f2237">Debt Mitigation &amp; Repayment Pathways:</text>
      <text x="0" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" fill="#475569">
        <tspan x="0" dy="0">• Public Service Loan Forgiveness (PSLF) for academic &amp; non-profit practice</tspan>
        <tspan x="0" dy="20">• SAVE / Income-Driven Repayment (IDR) to cap monthly obligations</tspan>
        <tspan x="0" dy="20">• USDA Veterinary Medicine Loan Repayment Program (VMLRP) for food animal</tspan>
        <tspan x="0" dy="20">• Corporate employer educational loan contribution &amp; signing bonuses</tspan>
      </text>
    </g>

    <rect x="28" y="380" width="469" height="30" rx="6" fill="#f8fafc"/>
    <text x="262" y="400" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="11" fill="#64748b">Debt-to-income ratio remains the #1 financial factor for prospective DVMs</text>
  </g>

  <!-- Footer -->
  <line x1="60" y1="630" x2="1140" y2="630" stroke="#cbd5e1" stroke-width="1"/>
  <text x="60" y="652" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" fill="#64748b">Source: American Veterinary Medical Association (AVMA) Economic State of the Veterinary Profession Report.</text>
  <text x="1140" y="652" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif" font-size="12" font-weight="600" fill="#0f2237">TopSchoolsRankings.com Research</text>
</svg>"""

files = [
    ("media/articles/vet-schools-methodology.svg", svg1),
    ("media/articles/vet-schools-top5-matrix.svg", svg2),
    ("media/articles/vet-schools-vmcas-roadmap.svg", svg3),
    ("media/articles/vet-schools-career-roi.svg", svg4)
]

for filepath, content in files:
    # Validate XML
    ET.fromstring(content)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated and validated {filepath} ({os.path.getsize(filepath)} bytes)")

print("All 4 SVGs successfully created and validated.")
