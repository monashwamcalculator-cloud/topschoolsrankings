import os
import re

# Update sitemap.xml
sitemap_path = 'sitemap.xml'
if os.path.exists(sitemap_path):
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        sitemap = f.read()
    
    new_sitemap = re.sub(r'<url>\s*<loc>[^<]*(/listing/|/tools/)[^<]*</loc>.*?</url>', '', sitemap, flags=re.IGNORECASE|re.DOTALL)
    
    # Wait, the sitemap might just have one line, so .*? within url tags is fine.
    # Let's ensure no malformed tags.
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(new_sitemap)

files_modified = 0

header_listing = '<a href="/listings/">Listings</a>'
header_tools = '<a href="/tools/">Tools</a>'
footer_tools = '<a href="/tools/">Student tools</a>'
footer_write = '<a href="/write-for-us/">Write for us</a>'

metrics_pattern = '<div class="stat-grid"><div><strong>105</strong><span>research guides</span></div><div><strong>46</strong><span>free planning tools</span></div><div><strong>135</strong><span>retained profiles</span></div></div>'
metrics_replacement = '<!-- <div class="stat-grid"><div><strong>105</strong><span>research guides</span></div><div><strong>46</strong><span>free planning tools</span></div><div><strong>135</strong><span>retained profiles</span></div></div> -->'

accuracy_note_1 = '<div class="editor-note"><strong>Accuracy note:</strong> The original article structure, semantic table rows and useful editorial images have been restored. Admissions, fees, rankings and policies change; follow cited official sources and recheck the date before acting.</div>'
accuracy_note_2 = '<div class="editor-note"><strong>Accuracy note:</strong> The original article structure, semantic table rows and useful editorial images have been restored. Admissions, fees, rankings and policies change; follow cited official sources and recheck the date before acting. </div>'

caption_text = 'Supporting visual context for the research process; verify decision-critical details in primary sources.'

for r, d, files in os.walk('.'):
    if '.git' in r: continue
    for f in files:
        if f.endswith('.html'):
            filepath = os.path.join(r, f)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                content = file.read()
            
            orig_content = content
            
            # 1. Noindex /listing/ and /tools/
            is_thin = '/listing/' in filepath.replace('\\', '/') or '/tools/' in filepath.replace('\\', '/')
            if is_thin:
                if '<meta name="robots" content="index, follow">' in content:
                    content = content.replace('<meta name="robots" content="index, follow">', '<meta name="robots" content="noindex, follow">')
                elif '<meta name="robots"' not in content:
                    content = content.replace('</head>', '<meta name="robots" content="noindex, follow">\n</head>')
                
            # 2. Navigation
            content = content.replace(header_listing, '')
            content = content.replace(header_tools, '')
            content = content.replace(footer_tools, '')
            content = content.replace(footer_write, '')
            
            # 3. Homepage metrics
            if f == 'index.html' and r == '.':
                content = content.replace(metrics_pattern, metrics_replacement)
                
            # 4. Boilerplate
            content = content.replace(accuracy_note_1, '')
            content = content.replace(accuracy_note_2, '')
            content = content.replace(caption_text, '')

            if orig_content != content:
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(content)
                files_modified += 1

print(f"Modified {files_modified} HTML files.")