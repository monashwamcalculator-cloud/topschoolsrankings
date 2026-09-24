import os

root_dir = '.'
modified_bio = 0

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
                
                # Replace 'student tools' with 'student guides' in the author bio
                html = html.replace('admissions strategies, and student tools.', 'admissions strategies, and student guides.')
                
                if original_html != html:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(html)
                    modified_bio += 1
            except Exception as e:
                pass

print(f"Updated author bio in {modified_bio} files.")