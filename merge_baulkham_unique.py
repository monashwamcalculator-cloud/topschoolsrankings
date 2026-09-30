import os

filepath = "baulkham-hills-high-school-entry-requirements-2026-comprehensive-guide/index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

unique_prep = """<h3><strong>D. Vocabulary &amp; Reading Strategy</strong></h3> <p>The Reading section is often highly challenging. Students need to read complex materials regularly, such as classic literature and modern scientific journals, to build a diverse vocabulary.</p> <h3><strong>E. Thinking Skills &amp; Logic</strong></h3> <p>This section requires students to solve syllogisms and critical thinking puzzles. Practice "lateral thinking" puzzles regularly to train the brain for unconventional patterns.</p> <h3><strong>F. Writing Task Mastery</strong></h3> <p>Markers look for strong voice and structure. Avoid clich&eacute; stories. Use sophisticated punctuation and varied sentence lengths to demonstrate authority over the language.</p> """

unique_faq = """<p><strong>Q: Can international or temporary resident students apply?</strong></p> <p><strong>A:</strong> To sit the test, the student must generally be an Australian citizen, a New Zealand citizen, or a permanent resident. Students on certain temporary visas (like the 482 or 457) can apply but may be required to pay the Temporary Residents Program fee if successful. Standard international students on a 500 visa usually cannot apply for selective schools.</p> """

# Insert prep
html = html.replace("<hr> <h2><strong>7. Key Dates for 2026/2027 Entry</strong></h2>", unique_prep + "<hr> <h2><strong>7. Key Dates for 2026/2027 Entry</strong></h2>")

# Insert FAQ
html = html.replace("<p><strong>Q: Can my child get into Baulkham Hills in Year 8, 9, or 10?</strong></p>", unique_faq + "<p><strong>Q: Can my child get into Baulkham Hills in Year 8, 9, or 10?</strong></p>")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Unique Baulkham Hills content integrated successfully.")