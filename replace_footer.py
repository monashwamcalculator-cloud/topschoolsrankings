import os

target = '<a class="correction-link" href="/contact-us/">Report a correction →</a></div>'
replacement = '<a class="correction-link" href="/contact-us/">Report a correction →</a><div class="social-links" style="margin-top:20px; display:flex; gap:15px; font-size:13px;"><a href="https://www.youtube.com/@TopSchoolsRankings" target="_blank" rel="noopener noreferrer" style="color:#a9b8ca; text-decoration:none;" onmouseover="this.style.color=\'#fff\'" onmouseout="this.style.color=\'#a9b8ca\'">YouTube</a><a href="https://www.instagram.com/topschoolsrankings/" target="_blank" rel="noopener noreferrer" style="color:#a9b8ca; text-decoration:none;" onmouseover="this.style.color=\'#fff\'" onmouseout="this.style.color=\'#a9b8ca\'">Instagram</a><a href="https://www.facebook.com/topschoolsrankings/" target="_blank" rel="noopener noreferrer" style="color:#a9b8ca; text-decoration:none;" onmouseover="this.style.color=\'#fff\'" onmouseout="this.style.color=\'#a9b8ca\'">Facebook</a></div></div>'

count = 0
for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(root, f)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            if target in content:
                content = content.replace(target, replacement)
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(content)
                count += 1

print(f'Replaced in {count} files')
