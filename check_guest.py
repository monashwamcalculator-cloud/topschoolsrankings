with open('how-universities-are-using-custom-software-solutions-to-build-smarter-digital-education-ecosystems/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'Guest' in line or 'Contributor' in line or 'Contribution' in line or 'Post' in line:
        print(f"Line {i+1}: {line.strip()}")