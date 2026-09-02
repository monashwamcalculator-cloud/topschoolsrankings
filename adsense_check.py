import urllib.request
import time
from bs4 import BeautifulSoup
import json

ts = int(time.time())
base = "https://topschoolsrankings.com"

urls_to_check = [
    "/",
    "/blogs/",
    "/ranking-methodology/",
    "/about-us/",
    "/contact-us/",
    "/privacy-policy/",
    "/terms-and-conditions/",
    "/disclaimer/",
    "/editorial-policy/",
    "/california-institute-of-technology-acceptance-rate-2026-how-hard-is-it-to-get-into-caltech/",
    "/robots.txt",
    "/sitemap.xml",
    "/assets/search-index.json"
]

results = {}

for u in urls_to_check:
    url = f"{base}{u}?bust={ts}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        resp = urllib.request.urlopen(req)
        status = resp.getcode()
        body = resp.read()
        
        is_html = u.endswith('/')
        
        if is_html:
            try:
                html = body.decode('utf-8')
            except Exception:
                try:
                    html = body.decode('cp1252')
                except:
                    html = ""
            
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.title.string if soup.title else None
            
            mojibake = ('\xc5\x92' in html) or ('\u0152' in html) or ('\xe2\x80\xa1\xe2\x80\x99' in html)
            caltech_bad = 'test-blind' in html.lower() or 'do not submit sat/act' in html.lower() or 'even a 1600' in html.lower()
            promo_bad = 'hard strategy to get admitted' in html.lower() or 'interview secrets' in html.lower()
            
            content_len = len(soup.get_text())
            results[u] = {
                'status': status,
                'title': title,
                'content_len': content_len,
                'mojibake': mojibake,
                'caltech_bad': caltech_bad,
                'promo_bad': promo_bad
            }
        else:
            results[u] = {'status': status, 'len': len(body)}
            
    except Exception as e:
        results[u] = {'status': 500, 'error': str(e)}

for k, v in results.items():
    print(k, v)