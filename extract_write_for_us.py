import re

with open('write-for-us/index.html', 'r', encoding='utf-8', errors='replace') as f:
    html = f.read()

start_marker = '<div class="rich-article-content">'
end_marker = '</div>\n  </article></section></main>'
end_marker_fallback = '</article></section></main>'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)
if end_idx == -1:
    end_idx = html.find(end_marker_fallback)

if start_idx != -1 and end_idx != -1:
    with open('write_for_us_extracted.txt', 'w', encoding='utf-8') as out_f:
        out_f.write(html[start_idx:end_idx])
    print("Wrote to write_for_us_extracted.txt")
else:
    print("Could not find markers.")