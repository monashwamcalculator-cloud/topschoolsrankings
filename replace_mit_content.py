import re

with open('massachusetts-institute-of-technology-complete-overview-key-facts-and-official-contact-details/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<div class="rich-article-content">'
end_marker = '</div>\n<div class="author-bio-box"'
end_marker_fallback = '</div>\n  <div class="author-bio-box"'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)
if end_idx == -1:
    end_idx = html.find(end_marker_fallback)

new_content = '''<div class="rich-article-content">
  <p><strong>Massachusetts Institute of Technology (MIT) Complete Overview</strong> — This independent editorial guide provides prospective applicants with verified facts, admissions requirements, and essential contact details for MIT.</p>
  
  <p><strong>Please note:</strong> This is a research guide compiled by Top Schools Rankings. We are not affiliated with, nor officially endorsed by, the Massachusetts Institute of Technology. Always verify deadlines, fees, and requirements directly on the official <a href="https://mitadmissions.org/" target="_blank" rel="noopener noreferrer">MIT Admissions website</a>.</p>

  <h2>History and Mission</h2>
  <p>Founded in 1861 by William Barton Rogers, MIT was established to accelerate the United States' industrial revolution. The institute quickly distinguished itself by combining rigorous scientific theory with practical application. Today, located across the Charles River from Boston in Cambridge, Massachusetts, MIT's mission is to advance knowledge in science, technology, and other areas of scholarship to serve the nation and the world.</p>

  <figure>
    <img src="/media/articles/top-50-universities-in-usa-inline-03.webp" alt="Students reviewing education choices using evidence and official information" width="1400" height="933" loading="lazy" decoding="async">
    <figcaption>MIT evaluates applicants on both their quantitative rigor and their collaborative spirit.</figcaption>
  </figure>

  <h2>Academic Structure</h2>
  <p>MIT is globally renowned for its STEM curriculum, but it also houses elite programs in architecture, management, and the humanities. Academics are organized into five primary schools and one college:</p>
  <ul>
    <li><strong>School of Architecture and Planning:</strong> Media and design innovation, urban studies.</li>
    <li><strong>School of Engineering:</strong> MIT's largest school, covering mechanical, electrical, computer science, aerospace, and biological engineering.</li>
    <li><strong>School of Humanities, Arts, and Social Sciences (HASS):</strong> Elite programs in economics, political science, and linguistics.</li>
    <li><strong>MIT Sloan School of Management:</strong> Finance, business analytics, and entrepreneurship.</li>
    <li><strong>School of Science:</strong> Physics, mathematics, chemistry, biology, and cognitive sciences.</li>
    <li><strong>Schwarzman College of Computing:</strong> Cross-cutting programs in artificial intelligence, data science, and computing.</li>
  </ul>
  <p>All undergraduates must complete the <strong>General Institute Requirements (GIRs)</strong>, a rigorous core curriculum encompassing calculus, physics, chemistry, biology, and humanities, regardless of their declared major.</p>

  <h2>Undergraduate Admissions &amp; Selectivity</h2>
  <p>MIT is one of the most selective universities in the world. Recent admissions cycles have seen acceptance rates hover around <strong>4.5% to 4.8%</strong>.</p>
  <ul>
    <li><strong>Standardized Testing:</strong> MIT <strong>requires</strong> the SAT or ACT for all applicants. They do not accept the IB or A-Levels as substitutes for this requirement.</li>
    <li><strong>Application Platform:</strong> MIT does not use the Common Application or Coalition Application. All applicants must apply through MIT's own proprietary application portal.</li>
    <li><strong>Evaluation Criteria:</strong> Admissions officers look for extreme academic rigor, exceptional quantitative ability, resilience, and a demonstrated history of collaborative problem-solving. MIT heavily values what you build, create, or discover over passive club memberships.</li>
  </ul>

  <h2>International Student Admissions</h2>
  <p>International applicants face an intensely competitive pool, but they are evaluated using the exact same holistic criteria as domestic students. Furthermore, MIT is one of only a handful of US universities that is strictly <strong>need-blind for international students</strong>.</p>
  <ul>
    <li>Your financial need will never negatively impact your chance of admission.</li>
    <li>If admitted, MIT will meet <strong>100% of your demonstrated financial need</strong>, regardless of citizenship.</li>
    <li>English proficiency exams (TOEFL, IELTS, or Pearson PTE) are strongly recommended for non-native English speakers.</li>
  </ul>

  <h2>Tuition, Costs, and Financial Aid</h2>
  <p>MIT operates with a commitment to making education affordable for admitted students. Below is the estimated cost of attendance before financial aid is applied (often referred to as the "sticker price").</p>
  <table>
    <thead>
      <tr><th>Expense Category</th><th>Estimated Annual Cost (USD)</th></tr>
    </thead>
    <tbody>
      <tr><td>Tuition &amp; Fees</td><td>~,000+</td></tr>
      <tr><td>Room &amp; Board</td><td>~,000 &ndash; ,000</td></tr>
      <tr><td>Books &amp; Personal Expenses</td><td>~,000 &ndash; ,000</td></tr>
      <tr><td><strong>Total Estimated Cost</strong></td><td><strong>~,000+</strong></td></tr>
    </tbody>
  </table>
  <p>Many students do not pay this full amount. Families with total incomes below certain thresholds (historically around ,000 USD) often receive substantial aid, and those below lower thresholds pay zero tuition. Always use the Net Price Calculator and verify the current academic year's rates directly with <a href="https://sfs.mit.edu/" target="_blank" rel="noopener noreferrer">MIT Student Financial Services</a>.</p>

  <h2>Career Outcomes and Innovation</h2>
  <p>MIT's innovation ecosystem is legendary. The institute supports entrepreneurship through the Martin Trust Center and numerous accelerators. MIT graduates are highly recruited globally, frequently securing roles in tech, finance, aerospace, and consulting, with average starting salaries consistently ranking among the highest in the United States.</p>

  <h2>Official Contact Information</h2>
  <p>When applying, interacting directly with the official university offices is critical. Below are the verified contact details for the Massachusetts Institute of Technology.</p>
  <table>
    <thead>
      <tr><th>Department</th><th>Contact Details</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>Official Name</strong></td><td>Massachusetts Institute of Technology (MIT)</td></tr>
      <tr><td><strong>Main Campus Address</strong></td><td>77 Massachusetts Ave, Cambridge, MA 02139, USA</td></tr>
      <tr><td><strong>Main Telephone</strong></td><td>+1 (617) 253-1000</td></tr>
      <tr><td><strong>General Website</strong></td><td><a href="https://www.mit.edu/" target="_blank" rel="noopener noreferrer">https://www.mit.edu/</a></td></tr>
      <tr><td><strong>Admissions Portal</strong></td><td><a href="https://mitadmissions.org/" target="_blank" rel="noopener noreferrer">https://mitadmissions.org/</a></td></tr>
      <tr><td><strong>Financial Aid Office</strong></td><td><a href="https://sfs.mit.edu/" target="_blank" rel="noopener noreferrer">https://sfs.mit.edu/</a></td></tr>
    </tbody>
  </table>

  <h2>FAQs: MIT Admissions</h2>
  <h3>Does MIT use the Common App?</h3>
  <p>No. MIT has its own dedicated application system. You cannot apply to MIT using the Common App or Coalition App.</p>

  <h3>Does MIT require the SAT or ACT?</h3>
  <p>Yes. MIT explicitly requires all applicants, including international students, to submit SAT or ACT scores.</p>

  <h3>Is MIT need-blind for international students?</h3>
  <p>Yes. MIT is fully need-blind for all applicants, regardless of citizenship, and meets 100% of demonstrated financial need.</p>

  <p><em>Disclaimer: Admissions policies, deadlines, testing requirements, and tuition fees are subject to change. This guide summarizes publicly available data for planning purposes only. Confirm all details directly on the official MIT websites before applying.</em></p>
</div>'''

if start_idx != -1 and end_idx != -1:
    final_html = html[:start_idx] + new_content + html[end_idx:]
    with open('massachusetts-institute-of-technology-complete-overview-key-facts-and-official-contact-details/index.html', 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Successfully replaced content.")
else:
    print(f"Could not find markers for replacement. start: {start_idx}, end: {end_idx}")