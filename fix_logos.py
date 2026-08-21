import os
import urllib.request
import re

universities = [
    {'id': 'purdue-university', 'domain': 'purdue.edu', 'name': 'Purdue University'},
    {'id': 'university-of-florida', 'domain': 'ufl.edu', 'name': 'University of Florida'},
    {'id': 'university-of-wisconsin-madison', 'domain': 'wisc.edu', 'name': 'University of Wisconsin-Madison'},
    {'id': 'university-of-california-san-diego', 'domain': 'ucsd.edu', 'name': 'University of California, San Diego'},
    {'id': 'university-of-maryland-college-park', 'domain': 'umd.edu', 'name': 'University of Maryland, College Park'}
]

# 1. Download logos
for uni in universities:
    logo_path = f"media/listings/{uni['id']}-logo.webp"
    url = f"https://www.google.com/s2/favicons?domain={uni['domain']}&sz=256"
    try:
        urllib.request.urlretrieve(url, logo_path)
        print(f"Downloaded logo for {uni['name']}")
    except Exception as e:
        print(f"Failed to download logo for {uni['name']}: {e}")

# 2. Fix individual profile pages
for uni in universities:
    filepath = f"listing/{uni['id']}/index.html"
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace the span with the img tag
        span_pattern = r'<span class="listing-profile-logo" aria-hidden="true"[^>]*>.*?</span>'
        img_tag = f'<img class="listing-profile-logo" src="/media/listings/{uni["id"]}-logo.webp" alt="{uni["name"]} logo" width="180" height="180" loading="eager" decoding="async">'
        content = re.sub(span_pattern, img_tag, content)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated profile page for {uni['name']}")
    except Exception as e:
        print(f"Failed to update profile for {uni['name']}: {e}")

# 3. Fix listings/index.html
listings_file = "listings/index.html"
try:
    with open(listings_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    for uni in universities:
        # Find the specific article and replace the span inside it
        # Since the spans are identical except for initials, we should use a generic regex for the span, but replacing it might be tricky if we don't know which one.
        # It's easier to find <article class="listing-card"> containing the university name, and replace the span inside.
        
        # Actually, let's just find the exact span for each initials:
        initials_map = {
            'purdue-university': 'PU',
            'university-of-florida': 'UF',
            'university-of-wisconsin-madison': 'UW',
            'university-of-california-san-diego': 'UCSD',
            'university-of-maryland-college-park': 'UMD'
        }
        initial = initials_map[uni['id']]
        
        span_str = f'<span class="listing-lettermark" aria-hidden="true" style="display:flex; align-items:center; justify-content:center; background:#1e293b; color:white; font-size:40px; font-weight:bold; width:180px; height:180px;">{initial}</span>'
        img_tag = f'<img class="listing-card-logo" src="/media/listings/{uni["id"]}-logo.webp" alt="{uni["name"]} logo" width="180" height="180" loading="lazy" decoding="async">'
        
        content = content.replace(span_str, img_tag)
        
    with open(listings_file, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated listings/index.html")
except Exception as e:
    print(f"Failed to update listings index: {e}")
