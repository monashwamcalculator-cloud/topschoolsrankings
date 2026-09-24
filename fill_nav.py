import os

root_dir = '.'
modified_count = 0

old_desktop = 'class="desktop-nav" aria-label="Primary navigation"><a href="/blogs/">Guides</a><a href="/ranking-methodology/">Methodology</a></nav>'
new_desktop = 'class="desktop-nav" aria-label="Primary navigation"><a href="/blogs/">All Guides</a><a href="/top-50-universities-in-usa/">US Universities</a><a href="/top-25-universities-in-canada-for-international-students/">Study in Canada</a><a href="/top-100-boarding-schools-in-the-world/">Boarding Schools</a><a href="/ranking-methodology/">Methodology</a><a href="/about-us/">About Us</a></nav>'

old_mobile = 'class="mobile-nav"><summary aria-label="Open menu">Menu</summary><nav><a href="/blogs/">Guides</a><a href="/ranking-methodology/">Methodology</a><a href="/about-us/">About</a></nav>'
new_mobile = 'class="mobile-nav"><summary aria-label="Open menu">Menu</summary><nav><a href="/blogs/">All Guides</a><a href="/top-50-universities-in-usa/">US Universities</a><a href="/top-25-universities-in-canada-for-international-students/">Study in Canada</a><a href="/top-100-boarding-schools-in-the-world/">Boarding Schools</a><a href="/ranking-methodology/">Methodology</a><a href="/about-us/">About Us</a></nav>'

old_footer = '<div><h2>Research</h2><a href="/blogs/">All guides</a></div>'
new_footer = '<div><h2>Research</h2><a href="/blogs/">All Guides</a><a href="/top-50-universities-in-usa/">US Universities Rankings</a><a href="/top-25-universities-in-canada-for-international-students/">Canadian Admissions</a><a href="/top-100-boarding-schools-in-the-world/">Global Boarding Schools</a></div>'

for dirpath, dirnames, filenames in os.walk(root_dir):
    if '.git' in dirnames:
        dirnames.remove('.git')
    
    for filename in filenames:
        if filename.endswith('.html'):
            filepath = os.path.join(dirpath, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    html = f.read()
                
                original_html = html
                
                html = html.replace(old_desktop, new_desktop)
                html = html.replace(old_mobile, new_mobile)
                html = html.replace(old_footer, new_footer)
                
                if original_html != html:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(html)
                    modified_count += 1
            except Exception as e:
                pass

print(f"Updated navigation and footer in {modified_count} HTML files.")