import urllib.request

url = 'https://topschoolsrankings-new-site-upload-v2-lq8o8c4ws.vercel.app/media/articles/how-universities-custom-software-digital-education-ecosystem-featured.webp'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    resp = urllib.request.urlopen(req)
    print(f'{url}: HTTP {resp.getcode()}')
except Exception as e:
    print(f'{url}: ERROR {e}')