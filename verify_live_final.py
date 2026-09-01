import urllib.request
import time
import random

urls_to_check = {
    'https://topschoolsrankings.com/assets/search-index.json': {
        'old': "Hard Strategy to Get Admitted",
        'new': "Bodwell High School Admissions Guide"
    },
    'https://topschoolsrankings.com/bodwell-high-school-acceptance-rate-admissions-strategy/': {
        'old': "Cracking the Bodwell Admission Code",
        'new': "Bodwell High School Admissions Guide"
    },
    'https://topschoolsrankings.com/upper-canada-college-admission-fees-ib-program/': {
        'old': "best private boys' school in Toronto",
        'new': "independent boys' school in Toronto"
    }
}

max_attempts = 15
for attempt in range(max_attempts):
    print(f"--- Attempt {attempt+1} ---")
    all_passed = True
    
    for base_url, strings in urls_to_check.items():
        cb = random.randint(100000, 999999)
        url = f"{base_url}?v={cb}"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
            res_text = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
            
            old_count = res_text.lower().count(strings['old'].lower())
            new_count = res_text.lower().count(strings['new'].lower())
            
            # Note: Bodwell phrase 'Bodwell High School Admissions Guide' was already added in other places, 
            # so count might be > 0 before deployment, but old_count MUST be 0.
            
            if old_count == 0 and new_count > 0:
                print(f"[PASS] {base_url} (Old: {old_count}, New: {new_count})")
            else:
                print(f"[WAIT] {base_url} (Old: {old_count}, New: {new_count})")
                all_passed = False
        except Exception as e:
            print(f"[ERROR] {base_url} - {e}")
            all_passed = False
            
    if all_passed:
        print("\nALL LIVE URLS VERIFIED SUCCESSFULLY!")
        break
    
    time.sleep(5)
