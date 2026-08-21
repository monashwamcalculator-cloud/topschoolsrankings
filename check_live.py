import urllib.request
import re

try:
    req = urllib.request.Request('https://topschoolsrankings.com/', headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        m = re.search(r'<footer.*?</footer>', html, re.DOTALL)
        if m:
            print(m.group(0))
except Exception as e:
    print('Error:', e)
