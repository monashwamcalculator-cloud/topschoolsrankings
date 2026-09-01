import urllib.request
def fetch(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        return urllib.request.urlopen(req).read().decode('utf-8')
    except Exception as e:
        return str(e)

print('--- robots.txt ---')
print(fetch('https://topschoolsrankings.com/robots.txt'))

print('\n--- sitemap.xml ---')
sitemap = fetch('https://topschoolsrankings.com/sitemap.xml')
print(sitemap[:500])
print(f'Total loc tags in sitemap: {sitemap.count("<loc>")}')
