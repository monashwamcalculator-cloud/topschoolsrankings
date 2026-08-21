import glob, re

for f in glob.glob('**/*.html', recursive=True):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        match = re.search(r'</div>\s*<figure class="editorial-figure">.*?</figure>', content, re.DOTALL)
        if match:
            print(f)
