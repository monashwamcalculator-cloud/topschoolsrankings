import urllib.request
import urllib.error

redirect_url = 'https://topschoolsrankings.com/top-20-canadian-boarding-schools'

class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

opener = urllib.request.build_opener(NoRedirectHandler())
req = urllib.request.Request(redirect_url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})

try:
    response = opener.open(req)
    print(f"Status: {response.status}")
except urllib.error.HTTPError as e:
    print(f"Status: {e.code}")
    print(f"Headers Location: {e.headers.get('Location')}")
except Exception as e:
    print(f"Error: {e}")