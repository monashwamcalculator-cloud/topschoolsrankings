import urllib.request
import re
import json

base_url = 'https://topschoolsrankings.com'
# append a query param to bust cache
def get_url(path):
    req = urllib.request.Request(f"{base_url}{path}?v=1", headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8'), response.status
    except Exception as e:
        return str(e), 500

print("VERIFYING HOMEPAGE...")
html, status = get_url('/')
print(f"Homepage Status: {status}")
print(f"Counters (104): {'104' in html}")
print(f"Counters (46): {'46' in html}")
print(f"Counters (135): {'135' in html}")

print("\nVERIFYING CLS PAGES (HTTP 200)...")
for page in [
    '/top-high-schools-in-england-rankings-guide/',
    '/top-10-computer-science-universities-in-usa/',
    '/top-10-universities-in-london/',
    '/tools/student-loan-repayment-calculator/'
]:
    _, s = get_url(page)
    print(f"{page} -> {s}")

print("\nVERIFYING LOGO FIX IN PRODUCTION...")
print("aspect-ratio" in html and "logo.png" in html)

print("\nVERIFYING NO MOJIBAKE...")
print("Ã" not in html)

print("\nVERIFYING CANONICAL FOR INDIA HOSTEL...")
hostel_html, s = get_url('/how-smart-hostels-are-changing-student-life-at-indian-universities/')
can_match = re.search(r'<link[^>]+rel="canonical"[^>]+href="([^"]+)"', hostel_html)
if can_match: print(can_match.group(1))

print("\nVERIFYING HIGH-RISK TOOLS NOINDEX...")
for tool in [
    '/tools/merit-aid-estimator/',
    '/tools/college-chances-calculator/',
    '/tools/nsw-selective-score-estimator/',
    '/tools/hsc-atar-estimator/',
    '/tools/ib-to-gpa-converter/',
    '/tools/atar-gpa-converter/'
]:
    t_html, t_status = get_url(tool)
    print(f"{tool} -> {'noindex,follow' in t_html or 'noindex, follow' in t_html}")

print("\nVERIFYING SITEMAP...")
xml, _ = get_url('/sitemap.xml')
urls = re.findall(r'<url>', xml)
print(f"Sitemap URL count: {len(urls)}")

print("\nVERIFYING SEARCH INDEX...")
idx, _ = get_url('/assets/search-index.json')
try:
    data = json.loads(idx)
    print(f"Search index entries: {len(data)}")
except:
    print("Invalid JSON")
