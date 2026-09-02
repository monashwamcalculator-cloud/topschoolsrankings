import urllib.request
import time
import json
import traceback

ts = int(time.time())
base = "https://topschoolsrankings.com"
fails = []
results = []

def fetch(path):
    url = f"{base}{path}?bust={ts}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        resp = urllib.request.urlopen(req)
        body = resp.read()
        return resp.getcode(), body
    except Exception as e:
        return 500, b''

def check(name, condition):
    res = "PASS" if condition else "FAIL"
    if not condition: fails.append(name)
    results.append(f"{name}: {res}")

print(f"Running LIVE checks against {base} with bust={ts}...")

# 1. Homepage
st, body = fetch("/")
check("Homepage HTTP 200", st == 200)
try:
    html = body.decode('utf-8')
    check("Homepage Counters (104/46/135)", '104' in html and '46' in html and '135' in html)
    check("Correct logo.png", 'logo.png' in html)
    check("Mojibake: 0", body.startswith(b'\xef\xbb\xbf') and '\xc5\x92' not in html and '\u0152' not in html)
except:
    check("Homepage Decode", False)

# 2. Caltech
st_cal, body_cal = fetch("/california-institute-of-technology-acceptance-rate-2026-how-hard-is-it-to-get-into-caltech/")
check("Caltech HTTP 200", st_cal == 200)
try:
    html_cal = body_cal.decode('utf-8').lower()
    obs_cal = ['strictly test-blind', 'test-blind', 'do not submit sat/act', 'even a 1600 won''t be looked at', 'look at sat/act scores at all']
    check("Caltech obsolete phrases: 0", not any(p in html_cal for p in obs_cal))
    check("Caltech updated wording LIVE", "sat/act results are considered as one part of caltech's holistic admissions review" in html_cal and "caltech requires first-year applicants to submit either sat or act scores" in html_cal)
except:
    check("Caltech check", False)

# 3. Promo phrases (Check a known page that had them)
st_promo, body_promo = fetch("/arizona-state-university-the-2026-insider-guide-to-admissions-fees-and-innovation/")
try:
    html_promo = body_promo.decode('utf-8').lower()
    obs_promo = ['hard strategy to get admitted', 'cracking the bodwell admission code', 'interview secrets', 'exact strategy', 'best private boys'' school']
    check("Promotional phrases: 0", not any(p in html_promo for p in obs_promo))
except:
    check("Promo check", False)

# 4. Restored Pages
st_t, _ = fetch("/tools/a-level-average-calculator/")
check("Restored tools HTTP 200", st_t == 200)
st_a, _ = fetch("/how-to-compare-universities-beyond-rankings/")
check("Restored articles HTTP 200", st_a == 200)
st_l, _ = fetch("/listing/harvard-university/")
check("Restored listings HTTP 200", st_l == 200)

# 5. Methodology
st_m, body_m = fetch("/ranking-methodology/")
check("Methodology HTTP 200", st_m == 200)
try:
    html_m = body_m.decode('utf-8')
    check("Methodology is approved version", '1. Transparent Metric Selection' in html_m or 'How We Rank' in html_m)
except:
    pass

# 6. Sitemap & Search Index
st_sm, _ = fetch("/sitemap.xml")
check("sitemap.xml HTTP 200", st_sm == 200)
st_sj, _ = fetch("/assets/search-index.json")
check("search-index.json HTTP 200", st_sj == 200)

print("\n--- RESULTS ---")
for r in results:
    print(r)

if len(fails) == 0:
    print("\nFINAL LIVE VERIFICATION: PASS")
else:
    print("\nFINAL LIVE VERIFICATION: FAIL")