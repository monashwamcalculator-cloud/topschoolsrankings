import re

md_path = "content/posts/top-100-universities-in-europe.md"
with open(md_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to cut everything from <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 32px 0;" />
# down to the end, where the author box starts.
# Actually, the user says to end right after:
# ## Related TopSchoolsRankings Guides
# (with the two internal links)

# Let's find the exact text of the Related TopSchoolsRankings Guides section and keep it, cutting the rest.

target = "<!-- Author Bio Box -->"
if target in content:
    index = content.find(target)
    # also remove the <hr> immediately preceding it
    content = content[:index].strip()
    # remove trailing <hr> if it exists
    content = re.sub(r'<hr[^>]*>\s*$', '', content).strip()

with open(md_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content + "\n")
