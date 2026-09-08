import urllib.request

url = 'https://topschoolsrankings.com/write-for-us/?bust=cache3'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        if '[email]' in html:
            print("FAILED: Old page is still served (placeholder found).")
        else:
            print("SUCCESS: New page is served (no placeholders).")
except Exception as e:
    print(e)