import urllib.request
import time
import random
import re

url_base = 'https://topschoolsrankings.com/ranking-methodology/'

required_phrases = [
    "About Our Rankings",
    "Data Sources",
    "Ranking Factors",
    "Scoring Method",
    "Data Verification",
    "Missing Data",
    "Updates",
    "Corrections Policy",
    "Editorial Independence",
    "Limitations",
    "Last Updated: September 2026"
]

forbidden_phrases = [
    "Semi-Annual Spot Audits",
    "may be excluded from data-heavy comparative lists"
]

for attempt in range(12):
    cb = random.randint(100000, 999999)
    url = f"{url_base}?v={cb}"
    print(f"Attempt {attempt+1} fetching {url}")
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
        
        all_required_present = True
        for phrase in required_phrases:
            if phrase not in res:
                all_required_present = False
                break
                
        all_forbidden_absent = True
        for phrase in forbidden_phrases:
            if phrase in res:
                all_forbidden_absent = False
                break
                
        if all_required_present and all_forbidden_absent:
            print("LIVE VERIFICATION: PASS")
            break
        else:
            print(f"WAITING: Required={all_required_present}, ForbiddenAbsent={all_forbidden_absent}")
            
    except Exception as e:
        print(f"Error fetching: {e}")
        
    time.sleep(5)
else:
    print("LIVE VERIFICATION: TIMEOUT")

