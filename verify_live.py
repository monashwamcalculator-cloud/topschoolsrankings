import urllib.request
import time

urls = [
    'https://topschoolsrankings.com/how-universities-are-using-custom-software-solutions-to-build-smarter-digital-education-ecosystems/?bust=' + str(time.time()),
    'https://topschoolsrankings.com/author/samrat-biswas/?bust=' + str(time.time())
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urllib.request.urlopen(req)
        print(f'{url.split("?")[0]}: HTTP {resp.getcode()}')
    except Exception as e:
        print(f'{url.split("?")[0]}: ERROR {e}')