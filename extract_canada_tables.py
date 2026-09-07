import re

with open('top-25-universities-in-canada-for-international-students/index.html', 'r', encoding='utf-8', errors='replace') as f:
    html = f.read()

def extract_table(html_str, idx_start_search):
    start = html_str.find('<table', idx_start_search)
    if start == -1: return "", -1
    end = html_str.find('</table>', start) + len('</table>')
    return html_str[start:end], end

t1, idx1 = extract_table(html, 0)
t2, idx2 = extract_table(html, idx1)

# Fix mojibake in tables
def fix_mojibake(t):
    t = t.replace('Universit de Montral', 'Université de Montréal')
    t = t.replace('Queens', "Queen's")
    t = t.replace('Universit Laval', 'Université Laval')
    t = t.replace('Montral', 'Montréal')
    return t

t1 = fix_mojibake(t1)
t2 = fix_mojibake(t2)

print("Table 1:", t1[:100])
print("Table 2:", t2[:100])

with open('canada_tables.py', 'w', encoding='utf-8') as f:
    f.write(f'T1 = """{t1}"""\nT2 = """{t2}"""\n')