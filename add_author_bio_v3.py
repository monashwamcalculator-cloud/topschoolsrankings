import os
import glob
import re

html_files = glob.glob('**/index.html', recursive=True)

author_bio_html = """
<div class="author-bio-box" style="margin-top: 40px; padding: 20px; background: #f8f9fa; border-radius: 8px; display: flex; align-items: center; gap: 20px; border: 1px solid #e2e8f0; clear: both;">
  <img src="/assets/saahil.jpg" alt="Saahil" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover;">
  <div>
    <h3 style="margin: 0 0 5px 0; font-size: 18px;"><a href="/author/saahil/" style="color: #1a202c; text-decoration: none;">Saahil</a></h3>
    <p style="margin: 0; font-size: 14px; color: #4a5568; line-height: 1.5;">Saahil is an education researcher and content creator specializing in university rankings, admissions strategies, and student tools. He is dedicated to helping students make informed academic decisions.</p>
  </div>
</div>
"""

excluded_dirs = {
    'assets', 'author', 'blogs', 'compare', 'contact-us', 'listings', 'media', 
    'ranking-methodology', 'tools', 'about-us', 'privacy-policy', 'terms-and-conditions', 
    'editorial-policy', 'write-for-us'
}

count = 0
for file in html_files:
    parts = file.replace('\\', '/').split('/')
    if len(parts) > 1:
        parent_dir = parts[0]
        if parent_dir in excluded_dirs:
            continue
            
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        if '<article class="article-body">' in content or '<article class="listing-body">' in content:
            if 'class="author-bio-box"' not in content:
                new_content = re.sub(r'</article>(\s*<aside)', f'\n{author_bio_html}\n</article>\\1', content, count=1)
                     
                if new_content != content:
                    with open(file, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    count += 1
    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"Added author bio to {count} articles.")
