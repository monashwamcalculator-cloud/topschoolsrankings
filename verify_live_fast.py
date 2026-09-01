import urllib.request
import time
import random

url_base = 'https://topschoolsrankings.com/ranking-methodology/'

for attempt in range(60):
    cb = random.randint(100000, 999999)
    url = f"{url_base}?v={cb}"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
        
        if "September 2026" in res and "Semi-Annual Spot Audits" not in res:
            print("LIVE VERIFICATION: PASS")
            break
        else:
            print(f"WAITING on attempt {attempt+1}")
            
    except Exception as e:
        print(f"Error fetching: {e}")
        
    time.sleep(5)
