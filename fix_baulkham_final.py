import os

filepath = "baulkham-hills-high-school-entry-requirements-2026-comprehensive-guide/index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Writing Component
old_writing = "<p>The Writing component evaluates creativity, grammar, and persuasive structure. According to the official marking framework, clear communication of ideas, relevance to the prompt, and well-structured responses are key components of a successful writing task.</p>"
new_writing = "<p>The Writing component assesses how effectively students communicate ideas in response to the given task. Students should focus on staying relevant to the prompt, organising their ideas clearly, and using appropriate grammar, punctuation, spelling and vocabulary.</p>"
html = html.replace(old_writing, new_writing)

# 2. Preparation Method (Mock Tests)
old_mock = """<h3><strong>C. Mock Tests (The Simulation)</strong></h3> <p>Practice in a timed environment. Use online platforms that mimic the official NSW Education Department's digital testing software.</p>"""
new_mock = """<h3><strong>C. Official Practice Resources</strong></h3> <p>The NSW Department of Education provides official practice tests and familiarization resources. Students are encouraged to utilize these tools to practice in a timed environment and become comfortable with the official digital testing software.</p>"""
html = html.replace(old_mock, new_mock)

# 3. Preparation Method (Tutoring FAQ)
old_tutoring = """<p><strong>Q: Is tutoring mandatory for entry?</strong></p> <p><strong>A:</strong> No, but given the 7% success rate, many families use tutoring to familiarize children with the <strong>Thinking Skills</strong> section, which is not taught in standard primary schools.</p>"""
new_tutoring = """<p><strong>Q: Is tutoring mandatory for entry?</strong></p> <p><strong>A:</strong> No. The NSW Department of Education does not endorse coaching or tutoring for the test. Families are encouraged to rely on the official familiarization and practice resources provided on the Department's website.</p>"""
html = html.replace(old_tutoring, new_tutoring)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated factual claims in Baulkham Hills article.")