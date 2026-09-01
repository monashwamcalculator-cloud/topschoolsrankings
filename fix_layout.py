import re

filepath = 'tools/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update tools count
tool_count = content.count('<article class="listing-card"')
print(f"Found {tool_count} tools.")
# Use regex to find and replace the count safely
content = re.sub(r'\d+\s+tools\s*·', f'{tool_count} tools ·', content)

# 2. Fix the extra spacing on the first category heading
# Replace the FIRST instance of margin-top: 40px; with margin-top: 0px;
content = content.replace('margin-top: 40px;', 'margin-top: 0px;', 1)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated successfully.")
