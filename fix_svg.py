import sys
import re

with open('tools/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

def replace_card_colors(url, color):
    global content
    start = content.rfind('<article class="listing-card"', 0, content.find(url))
    if start != -1:
        svg_start = content.find('<svg', start)
        svg_end = content.find('>', svg_start)
        
        svg_tag = content[svg_start:svg_end+1]
        new_svg_tag = re.sub(r'color:[^;]+;', f'color:{color};', svg_tag)
        content = content[:svg_start] + new_svg_tag + content[svg_end+1:]

replace_card_colors('/tools/cumulative-gpa-calculator/', '#0056b3')
replace_card_colors('/tools/target-gpa-calculator/', '#ffc107')
replace_card_colors('/tools/wam-to-gpa-converter/', '#17a2b8')
replace_card_colors('/tools/gpa-to-wam-converter/', '#fd7e14')

with open('tools/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated SVG colors to match the border colors!')
