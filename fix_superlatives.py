import os

replacements = {
    "baulkham-hills-high-school-entry-requirements-2026-comprehensive-guide/index.html": [
        ("is the ultimate goal for many.", "is a popular goal for many.")
    ],
    "arizona-state-university-the-2026-insider-guide-to-admissions-fees-and-innovation/index.html": [
        ("Widely considered the best honors college in the", "Widely recognized for its honors college in the"),
        ("best of both worlds", "ideal combination")
    ],
    "how-to-compare-universities-beyond-rankings/index.html": [
        ("The best option is the one that fits", "The ideal option is the one that fits"),
        ("identify the best university?", "identify the right university?")
    ],
    "how-to-choose-a-university-course-uk/index.html": [
        ("most popular", "widely chosen")
    ]
}

for file, changes in replacements.items():
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            html = f.read()
        for old, new in changes:
            html = html.replace(old, new)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Fixed superlatives in {file}")
