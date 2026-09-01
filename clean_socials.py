import glob
import re
import os

count_cleaned = 0
count_removed_entirely = 0

for filepath in glob.glob("listing/*/index.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the social media block
    match = re.search(r'(<div><dt>Social Media</dt><dd[^>]*>)(.*?)(</dd></div>)', content, re.DOTALL)
    if match:
        prefix = match.group(1)
        links_html = match.group(2)
        suffix = match.group(3)

        # We will parse out individual <a> tags and keep only the valid ones
        # A tag looks like <a href="...">...</a>
        valid_links = []
        
        # Regex to find all <a> tags
        a_tags = re.findall(r'<a [^>]*>.*?</a>', links_html, re.DOTALL)
        
        for a_tag in a_tags:
            href_match = re.search(r'href="([^"]+)"', a_tag)
            if href_match:
                href = href_match.group(1).strip()
                # Check if it is a generic or search link
                is_invalid = False
                if href in [
                    "https://instagram.com/", "https://www.instagram.com/",
                    "https://facebook.com/", "https://www.facebook.com/",
                    "https://twitter.com/", "https://www.twitter.com/",
                    "https://x.com/", "https://www.x.com/"
                ]:
                    is_invalid = True
                if "search?q=" in href or "explore/search" in href or "search/pages" in href:
                    is_invalid = True
                
                if not is_invalid:
                    valid_links.append(a_tag)
        
        if len(valid_links) == 0:
            # Remove the whole block
            content = content.replace(match.group(0), "")
            count_removed_entirely += 1
            count_cleaned += 1
        elif len(valid_links) < len(a_tags):
            # Replace inner html with only valid links
            new_block = prefix + "\n".join(valid_links) + suffix
            content = content.replace(match.group(0), new_block)
            count_cleaned += 1
            
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

print(f"Cleaned generic social links in {count_cleaned} files. Removed entire block in {count_removed_entirely} files.")
