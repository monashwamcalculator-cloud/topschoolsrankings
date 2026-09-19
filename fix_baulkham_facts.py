import os

filepath = "baulkham-hills-high-school-entry-requirements-2026-comprehensive-guide/index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace D, E, F
old_prep = """<h3><strong>D. Vocabulary &amp; Reading Strategy</strong></h3> <p>The Reading section is often highly challenging. Students need to read complex materials regularly, such as classic literature and modern scientific journals, to build a diverse vocabulary.</p> <h3><strong>E. Thinking Skills &amp; Logic</strong></h3> <p>This section requires students to solve syllogisms and critical thinking puzzles. Practice "lateral thinking" puzzles regularly to train the brain for unconventional patterns.</p> <h3><strong>F. Writing Task Mastery</strong></h3> <p>Markers look for strong voice and structure. Avoid clich&eacute; stories. Use sophisticated punctuation and varied sentence lengths to demonstrate authority over the language.</p>"""

new_prep = """<h3><strong>D. Reading Strategy</strong></h3> <p>The Reading section assesses comprehension, vocabulary, and the ability to draw inferences. Students should practice reading widely across different genres and text types to improve their ability to analyze complex information effectively.</p> <h3><strong>E. Thinking Skills</strong></h3> <p>This section focuses on critical thinking and finding logical patterns rather than general knowledge. Familiarizing students with problem-solving formats can help them navigate these questions effectively under time pressure.</p> <h3><strong>F. Writing Task</strong></h3> <p>The Writing component evaluates creativity, grammar, and persuasive structure. According to the official marking framework, clear communication of ideas, relevance to the prompt, and well-structured responses are key components of a successful writing task.</p>"""

# Replace FAQ
old_faq = """<p><strong>Q: Can international or temporary resident students apply?</strong></p> <p><strong>A:</strong> To sit the test, the student must generally be an Australian citizen, a New Zealand citizen, or a permanent resident. Students on certain temporary visas (like the 482 or 457) can apply but may be required to pay the Temporary Residents Program fee if successful. Standard international students on a 500 visa usually cannot apply for selective schools.</p>"""

new_faq = """<p><strong>Q: Can international or temporary resident students apply?</strong></p> <p><strong>A:</strong> Eligibility depends on NSW residency requirements and the applicant's specific visa and enrolment conditions. Families should verify their exact visa subclass eligibility directly through the <a href="https://education.nsw.gov.au/public-schools/selective-high-schools-and-opportunity-classes/year-7/information-for-applicants" target="_blank" rel="noopener noreferrer">official NSW Department of Education selective high school enrolment guidelines</a>.</p>"""

html = html.replace(old_prep, new_prep)
html = html.replace(old_faq, new_faq)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated factual claims in Baulkham Hills article.")