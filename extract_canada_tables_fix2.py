import re

with open('top-25-universities-in-canada-for-international-students/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def extract_table(html_str, idx_start_search):
    start = html_str.find('<table', idx_start_search)
    if start == -1: return "", -1
    end = html_str.find('</table>', start) + len('</table>')
    return html_str[start:end], end

t1, idx1 = extract_table(html, 0)
t2, idx2 = extract_table(html, idx1)

# Fix mojibake
t1 = t1.replace('Universit de Montral', 'Université de Montréal')
t1 = t1.replace('Queens', "Queen's")
t1 = t1.replace('Universit Laval', 'Université Laval')

t2 = t2.replace('Montral', 'Montréal')

with open('canada_tables.py', 'w', encoding='utf-8') as f:
    f.write(f'T1 = """{t1}"""\nT2 = """{t2}"""\n')
print("Extracted t1 length:", len(t1))