import os, glob
import re

svg_dir = 'c:/Users/Hp/Downloads/topschoolsrankings-new-site-upload-v2/media/articles'

for filepath in glob.glob(os.path.join(svg_dir, '*.svg')):
    with open(filepath, 'r', encoding='utf-8') as f:
        svg_content = f.read()
    
    lines = svg_content.split('\n')
    
    max_y = 0
    footer_line_idx = -1
    footer_text_idx = -1
    bg_rect_idx = -1
    side_rect_idx = -1
    
    for i, line in enumerate(lines):
        if 'fill="#f7f5ef"' in line and 'width="1200"' in line:
            bg_rect_idx = i
            continue
        if 'width="18"' in line and 'x="0"' in line and 'y="0"' in line:
            side_rect_idx = i
            continue
            
        if 'stroke="#ccd2d6"' in line and 'x1="70"' in line:
            footer_line_idx = i
            continue
        if 'Source: TopSchoolsRankings' in line:
            footer_text_idx = i
            continue
            
        y_match = re.search(r'\by="(\d+)"', line)
        h_match = re.search(r'\bheight="(\d+)"', line)
        if y_match:
            y_val = int(y_match.group(1))
            if h_match:
                y_val += int(h_match.group(1))
            if y_val > max_y:
                max_y = y_val

    if footer_line_idx != -1 and footer_text_idx != -1:
        new_footer_y1 = max_y + 40
        new_footer_text_y = new_footer_y1 + 29
        new_total_height = new_footer_text_y + 26
        
        current_height_match = re.search(r'height="(\d+)"', lines[0])
        if current_height_match:
            current_height = int(current_height_match.group(1))
            
            # ALWAYS adjust to standardized padding, whether expanding or shrinking
            if current_height != new_total_height:
                # Replace in root svg tag
                lines[0] = re.sub(r'height="\d+"', f'height="{new_total_height}"', lines[0])
                lines[0] = re.sub(r'viewBox="0 0 1200 \d+"', f'viewBox="0 0 1200 {new_total_height}"', lines[0])
                
                # Replace bg rect height
                if bg_rect_idx != -1:
                    lines[bg_rect_idx] = re.sub(r'height="\d+"', f'height="{new_total_height}"', lines[bg_rect_idx])
                
                # Replace side rect height
                if side_rect_idx != -1:
                    lines[side_rect_idx] = re.sub(r'height="\d+"', f'height="{new_total_height}"', lines[side_rect_idx])
                
                # Replace footer line y1 and y2
                lines[footer_line_idx] = re.sub(r'y1="\d+"', f'y1="{new_footer_y1}"', lines[footer_line_idx])
                lines[footer_line_idx] = re.sub(r'y2="\d+"', f'y2="{new_footer_y1}"', lines[footer_line_idx])
                
                # Replace footer text y
                lines[footer_text_idx] = re.sub(r'y="\d+"', f'y="{new_footer_text_y}"', lines[footer_text_idx])
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(lines))
                
                print(f"Standardized {os.path.basename(filepath)} from {current_height} to {new_total_height}")

print("Done standardizing all SVGs padding.")
