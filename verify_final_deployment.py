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

max_attempts = 30
success = False

for attempt in range(max_attempts):
    cb = random.randint(1000000, 9999999)
    url = f"{url_base}?v={cb}"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
        
        all_present = True
        for phrase in required_phrases:
            if phrase not in res:
                all_present = False
                break
                
        if all_present and "20 August 2026" not in res:
            print("LIVE VERIFICATION: PASS")
            success = True
            break
        else:
            print(f"WAITING... (Attempt {attempt+1}/{max_attempts}) - 'September 2026' found: {'September 2026' in res}")
            
    except Exception as e:
        print(f"Error fetching: {e}")
        
    time.sleep(15)

if not success:
    print("LIVE VERIFICATION: TIMEOUT")
