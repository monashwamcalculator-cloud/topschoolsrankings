import sys

with open('tools/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

def replace_card(url, color, span_text):
    global content
    start = content.rfind('<article class="listing-card"', 0, content.find(url))
    if start != -1:
        end_of_tag = content.find('>', start)
        tag = content[start:end_of_tag+1]
        
        # If it already has some style, just overwrite the tag
        new_tag = f'<article class="listing-card" style="border-top: 4px solid {color}; padding-top: 20px;">'
        content = content[:start] + new_tag + content[end_of_tag+1:]
        
        # update svg_end based on new content length
        start = content.rfind('<article class="listing-card"', 0, content.find(url))
        svg_end = content.find('</svg>', start) + 6
        
        next_chars = content[svg_end:svg_end+30]
        if '<span>' not in next_chars:
            content = content[:svg_end] + f' <span>{span_text}</span>' + content[svg_end:]

replace_card('/tools/cumulative-gpa-calculator/', '#0056b3', 'Planning tool')
replace_card('/tools/target-gpa-calculator/', '#ffc107', 'Planning tool')
replace_card('/tools/wam-to-gpa-converter/', '#17a2b8', 'Planning tool')
replace_card('/tools/gpa-to-wam-converter/', '#fd7e14', 'Planning tool')

with open('tools/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Cards updated successfully!')
