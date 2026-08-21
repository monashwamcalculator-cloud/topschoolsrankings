import os
import glob
import re

count_fixed = 0

for filepath in glob.glob('**/*.html', recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    modified = False
    
    # Check if there is a dangling editorial-figure after rich-article-content
    figure_match = re.search(r'(</div>)\s*(<figure class="editorial-figure">.*?</figure>)', html, re.DOTALL)
    if figure_match:
        figure_html = figure_match.group(2)
        html = html.replace(figure_match.group(0), '</div>')
        
        content_match = re.search(r'(<div class="rich-article-content">)(.*?)(</div>\s*<section class="related-guides">|</div>\s*<aside class="article-aside">|</div>\s*</article>)', html, re.DOTALL)
        
        if content_match:
            content_start = content_match.group(1)
            content_body = content_match.group(2)
            content_end = content_match.group(3)
            
            # Insert figure before the 3rd <h2> (or 2nd if less)
            # Find all indices of <h2>
            h2_indices = [m.start() for m in re.finditer(r'<h2[^>]*>', content_body)]
            insert_idx = -1
            if len(h2_indices) >= 3:
                insert_idx = h2_indices[2] # 3rd h2
            elif len(h2_indices) == 2:
                insert_idx = h2_indices[1] # 2nd h2
            elif len(h2_indices) == 1:
                insert_idx = h2_indices[0] # 1st h2
            
            if insert_idx != -1:
                content_body = content_body[:insert_idx] + figure_html + '\n\n' + content_body[insert_idx:]
            else:
                # No <h2>, find middle <p>
                p_indices = [m.end() for m in re.finditer(r'</p>', content_body)]
                if len(p_indices) >= 2:
                    mid = len(p_indices) // 2
                    insert_idx = p_indices[mid]
                    content_body = content_body[:insert_idx] + '\n\n' + figure_html + '\n\n' + content_body[insert_idx:]
                else:
                    # just append at end of content_body
                    content_body = content_body + '\n\n' + figure_html
            
            html = html[:content_match.start()] + content_start + content_body + content_end + html[content_match.end():]
            modified = True

    # Now let's fix any "faltu gaps" in the entire html, mostly in rich-article-content
    # Empty paragraphs with non-breaking spaces or just empty
    original_html = html
    html = re.sub(r'<p>\s*(?:&nbsp;| )\s*</p>', '', html)
    html = re.sub(r'<p>\s*</p>', '', html)
    html = re.sub(r'\n\s*(?:&nbsp;| )\s*\n', '\n\n', html)
    # clean up multiple empty newlines if there are more than 3
    html = re.sub(r'\n{4,}', '\n\n', html)
    
    if html != original_html:
        modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        count_fixed += 1

print(f"Fixed figures and gaps in {count_fixed} files.")
