import os
import re

social_data = {
    'purdue-university': {
        'Twitter': 'https://twitter.com/LifeAtPurdue',
        'Instagram': 'https://www.instagram.com/lifeatpurdue/',
        'Facebook': 'https://www.facebook.com/PurdueUniversity/'
    },
    'university-of-florida': {
        'Twitter': 'https://twitter.com/UF',
        'Instagram': 'https://www.instagram.com/uflorida/',
        'Facebook': 'https://www.facebook.com/uflorida/'
    },
    'university-of-wisconsin-madison': {
        'Twitter': 'https://twitter.com/UWMadison',
        'Instagram': 'https://www.instagram.com/uwmadison/',
        'Facebook': 'https://www.facebook.com/UWMadison/'
    },
    'university-of-california-san-diego': {
        'Twitter': 'https://twitter.com/UCSanDiego',
        'Instagram': 'https://www.instagram.com/ucsandiego/',
        'Facebook': 'https://www.facebook.com/UCSanDiego/'
    },
    'university-of-maryland-college-park': {
        'Twitter': 'https://twitter.com/UofMaryland',
        'Instagram': 'https://www.instagram.com/univofmaryland/',
        'Facebook': 'https://www.facebook.com/UnivofMaryland/'
    },
    'ohio-state-university': {
        'Twitter': 'https://twitter.com/OhioState',
        'Instagram': 'https://www.instagram.com/theohiostateuniversity/',
        'Facebook': 'https://www.facebook.com/osu/'
    },
    'pennsylvania-state-university': {
        'Twitter': 'https://twitter.com/penn_state',
        'Instagram': 'https://www.instagram.com/pennstate/',
        'Facebook': 'https://www.facebook.com/pennstate/'
    },
    'rutgers-university': {
        'Twitter': 'https://twitter.com/RutgersU',
        'Instagram': 'https://www.instagram.com/rutgersu/',
        'Facebook': 'https://www.facebook.com/RutgersU/'
    },
    'texas-a-and-m-university': {
        'Twitter': 'https://twitter.com/TAMU',
        'Instagram': 'https://www.instagram.com/tamu/',
        'Facebook': 'https://www.facebook.com/tamu/'
    },
    'michigan-state-university': {
        'Twitter': 'https://twitter.com/michiganstateu',
        'Instagram': 'https://www.instagram.com/michiganstateu/',
        'Facebook': 'https://www.facebook.com/spartans.msu/'
    }
}

for uni_id, socials in social_data.items():
    filepath = f"listing/{uni_id}/index.html"
    if not os.path.exists(filepath):
        print(f"Skipping {uni_id}, file not found.")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Build social media HTML
    social_links_html = " · ".join([f'<a href="{url}" target="_blank" rel="noopener noreferrer">{platform}</a>' for platform, url in socials.items()])
    social_block = f'<div><dt>Social Media</dt><dd>{social_links_html}</dd></div>'
    
    # Check if already added
    if "Social Media" in content:
        print(f"{uni_id} already has social media.")
        continue
        
    # Insert before the closing </dl>
    if "</dl>" in content:
        content = content.replace("</dl>", f"{social_block}</dl>")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added social media to {uni_id}")
    else:
        print(f"Could not find <dl> tag in {uni_id}")

print("Done.")
