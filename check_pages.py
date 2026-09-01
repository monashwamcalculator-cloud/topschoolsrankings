import urllib.request
import re

urls = [
    'https://topschoolsrankings.com/',
    'https://topschoolsrankings.com/about-us/',
    'https://topschoolsrankings.com/contact-us/',
    'https://topschoolsrankings.com/privacy-policy/',
    'https://topschoolsrankings.com/blogs/',
    'https://topschoolsrankings.com/california-institute-of-technology-acceptance-rate-2026-how-hard-is-it-to-get-into-caltech/'
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
        
        title = re.search(r'<title>(.*?)</title>', res)
        desc = re.search(r'<meta name="description" content="(.*?)"', res)
        canonical = re.search(r'<link rel="canonical" href="(.*?)"', res)
        jsonld = re.search(r'<script type="application/ld\+json">(.*?)</script>', res, re.DOTALL)
        
        print(f"\n--- {url} ---")
        print(f"Title: {title.group(1) if title else 'MISSING'}")
        print(f"Description: {desc.group(1)[:50] + '...' if desc else 'MISSING'}")
        print(f"Canonical: {canonical.group(1) if canonical else 'MISSING'}")
        print(f"JSON-LD: {'PRESENT' if jsonld else 'MISSING'}")
        
    except Exception as e:
        print(f"Error fetching {url}: {e}")
