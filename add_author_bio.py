import os
import glob

html_files = glob.glob('**/*.html', recursive=True)

author_bio_html = """
<div class="author-bio-box" style="margin-top: 40px; padding: 20px; background: #f8f9fa; border-radius: 8px; display: flex; align-items: center; gap: 20px; border: 1px solid #e2e8f0;">
  <img src="/assets/saahil.jpg" alt="Saahil" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover;">
  <div>
    <h3 style="margin: 0 0 5px 0; font-size: 18px;"><a href="/author/saahil/" style="color: #1a202c; text-decoration: none;">Saahil</a></h3>
    <p style="margin: 0; font-size: 14px; color: #4a5568; line-height: 1.5;">Saahil is an education researcher and content creator specializing in university rankings, admissions strategies, and student tools. He is dedicated to helping students make informed academic decisions.</p>
  </div>
</div>
"""

count = 0
for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if this is an article by looking for the author link at the top
        if 'class="author-link"' in content and '</article>' in content:
            # Check if we already added it to prevent duplicates
            if 'class="author-bio-box"' not in content:
                new_content = content.replace('</article>', f"{author_bio_html}</article>")
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
    except Exception as e:
        print(f"Error processing {file}: {e}")

print(f"Added author bio to {count} articles.")
