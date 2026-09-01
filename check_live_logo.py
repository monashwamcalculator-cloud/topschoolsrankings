import urllib.request
import re

url = 'https://topschoolsrankings.com/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
res = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')

match = re.search(r'<a class="brand".*?</a>', res, re.DOTALL)
if match: 
    print(match.group(0))
else: 
    print('No brand logo HTML found!')
