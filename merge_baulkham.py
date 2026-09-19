import os
import json
import re

# 1. Update vercel.json
with open('vercel.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['redirects'].append({
    "source": "/how-to-get-into-baulkham-hills-high-school-2026-admissions-rankings-and-preparation-strategy/",
    "destination": "/baulkham-hills-high-school-entry-requirements-2026-comprehensive-guide/",
    "permanent": True
})
data['redirects'].append({
    "source": "/how-to-get-into-baulkham-hills-high-school-2026-admissions-rankings-and-preparation-strategy",
    "destination": "/baulkham-hills-high-school-entry-requirements-2026-comprehensive-guide/",
    "permanent": True
})

with open('vercel.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

# 2. Update blogs/index.html
with open('blogs/index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'<article class="guide-card"><a [^>]+href="/how-to-get-into-baulkham-hills-high-school-2026-admissions-rankings-and-preparation-strategy/".*?</article>', '', html, flags=re.DOTALL)
with open('blogs/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 3. Update sitemap.xml
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()
sitemap = re.sub(r'<url>\s*<loc>https://topschoolsrankings\.com/how-to-get-into-baulkham-hills-high-school-2026-admissions-rankings-and-preparation-strategy/?</loc>.*?</url>', '', sitemap, flags=re.DOTALL)
with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap)

# 4. Update search-index.json
with open('assets/search-index.json', 'r', encoding='utf-8') as f:
    search_data = json.load(f)
search_data = [item for item in search_data if item.get('path') != '/how-to-get-into-baulkham-hills-high-school-2026-admissions-rankings-and-preparation-strategy/']
with open('assets/search-index.json', 'w', encoding='utf-8') as f:
    json.dump(search_data, f, indent=2)

print("Merged and setup redirects.")