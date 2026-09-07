import re

with open('top50_old_content.html', 'r', encoding='utf-8') as f:
    html = f.read()

# We need to extract the tables to preserve them perfectly.
def extract_table(html_str, title_hint):
    idx = html_str.find(title_hint)
    if idx == -1:
        return ""
    start_table = html_str.find('<table>', idx)
    end_table = html_str.find('</table>', start_table) + len('</table>')
    return html_str[start_table:end_table]

table_changes = extract_table(html, 'What changed in the 2026 top 50?')
table_top50 = extract_table(html, 'Top 50 universities in USA - full 2026 list')
table_tuition = extract_table(html, '2026 estimated costs & admissions')
table_goals = extract_table(html, 'Best top-50 choices by international student goal')
table_public_private = extract_table(html, 'Public vs private in the 2026 top 50')

print(f"Tables extracted:")
print(f"Changes: {len(table_changes)} chars")
print(f"Top 50: {len(table_top50)} chars")
print(f"Tuition: {len(table_tuition)} chars")
print(f"Goals: {len(table_goals)} chars")
print(f"Pub/Priv: {len(table_public_private)} chars")