import urllib.request
import time

url = 'https://topschoolsrankings-new-site-upload-v2-f61cdgs9r.vercel.app/blogs/'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    resp = urllib.request.urlopen(req)
    print(f'{url}: HTTP {resp.getcode()}')
except Exception as e:
    print(f'{url}: ERROR {e}')