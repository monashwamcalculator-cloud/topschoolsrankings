import re

with open('top-10-uk-universities-for-international-students/index.html', 'r', encoding='utf-8', errors='replace') as f:
    html = f.read()

def extract_table(html_str, idx_start_search):
    start = html_str.find('<table', idx_start_search)
    if start == -1: return "", -1
    end = html_str.find('</table>', start) + len('</table>')
    return html_str[start:end], end

t1, idx1 = extract_table(html, 0)
t2, idx2 = extract_table(html, idx1)
t3, idx3 = extract_table(html, idx2)

with open('uk_tables.py', 'w', encoding='utf-8') as f:
    f.write(f'T1 = """{t1}"""\nT2 = """{t2}"""\nT3 = """{t3}"""\n')