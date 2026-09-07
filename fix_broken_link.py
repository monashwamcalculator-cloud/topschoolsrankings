import os

filepath = 'how-smart-hostels-are-changing-student-life-at-indian-universities/index.html'
if os.path.exists(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('href="/category/india/"', 'href="/blogs/"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed broken link in {filepath}")