import urllib.request
import time

url = 'https://topschoolsrankings-new-site-upload-v2-dnjcpc0vj.vercel.app/how-universities-are-using-custom-software-solutions-to-build-smarter-digital-education-ecosystems/'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    resp = urllib.request.urlopen(req)
    print(f'{url}: HTTP {resp.getcode()}')
except Exception as e:
    print(f'{url}: ERROR {e}')