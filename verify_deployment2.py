import urllib.request
import urllib.error

urls = [
    'https://topschoolsrankings.com/',
    'https://topschoolsrankings.com/write-for-us/',
    'https://topschoolsrankings.com/ranking-methodology/',
    'https://topschoolsrankings.com/editorial-policy/',
    'https://topschoolsrankings.com/about-us/',
    'https://topschoolsrankings.com/contact-us/',
    'https://topschoolsrankings.com/top-50-universities-in-usa/',
    'https://topschoolsrankings.com/top-25-universities-in-canada-for-international-students/',
    'https://topschoolsrankings.com/top-20-universities-in-australia/',
    'https://topschoolsrankings.com/top-10-uk-universities-for-international-students/',
    'https://topschoolsrankings.com/sitemap.xml',
    'https://topschoolsrankings.com/robots.txt'
]

redirect_url = 'https://topschoolsrankings.com/top-20-canadian-boarding-schools/'

class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

opener = urllib.request.build_opener(NoRedirectHandler())

for u in urls:
    req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
    try:
        response = opener.open(req)
        print(f"URL: {u} | Status: {response.status}")
    except Exception as e:
        print(f"URL: {u} | Error: {e}")

try:
    req = urllib.request.Request(redirect_url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
    response = opener.open(req)
    print(f"REDIRECT TEST: {redirect_url} | Status: {response.status}")
except urllib.error.HTTPError as e:
    print(f"REDIRECT TEST: {redirect_url} | Status: {e.code} | Location: {e.headers.get('Location')}")
except Exception as e:
    print(f"REDIRECT TEST Error: {e}")
