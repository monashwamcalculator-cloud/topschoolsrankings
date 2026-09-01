import urllib.request
import re

urls = [
    'https://topschoolsrankings.com/?v=99991',
    'https://topschoolsrankings.com/blogs/?v=99991',
    'https://topschoolsrankings.com/california-institute-of-technology-acceptance-rate-2026-how-hard-is-it-to-get-into-caltech/?v=99991'
]

strings_to_find = [
    'Œ•', '€¦', '€“', '‡’', 
    'No articles match your search', 
    'Strictly Test-Blind', 'Do not submit SAT/ACT', 'Test-Blind', 'Even a 1600', 'test-blind policy', 'Calculus course in high school to even be considered',
    'Hard Strategy to Get Admitted', 'Cracking the Bodwell Admission Code', 'interview secrets', 'exact strategy', 
    'best private boys\' school in Toronto', 'one of the premier undergraduate entry processes globally'
]

for url in urls:
    print(f"\n--- Fetching {url} ---")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res_bytes = urllib.request.urlopen(req).read()
        res_text = res_bytes.decode('utf-8', errors='replace')
        
        for s in strings_to_find:
            count = res_text.lower().count(s.lower())
            if count > 0:
                print(f"FOUND: '{s}' (Count: {count})")
    except Exception as e:
        print(f"Error: {e}")
