import os

path = 'california-institute-of-technology-acceptance-rate-2026-how-hard-is-it-to-get-into-caltech/index.html'

with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

orig = html

html = html.replace('This shifted all competition to your GPA and research.', "SAT/ACT results are considered as one part of Caltech's holistic admissions review, alongside the broader academic and application context.")

html = html.replace('SAT/ACT submission is mandatory for all applicants.', "Caltech requires first-year applicants to submit either SAT or ACT scores, with a process for applicants who are unable to access a standardized exam.")

if orig == html:
    print("NO REPLACEMENTS MADE! Strings not found.")
else:
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Replacements made successfully.")