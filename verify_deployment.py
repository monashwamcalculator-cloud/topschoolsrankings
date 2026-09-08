import urllib.request
import time

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
]

redirect_url = 'https://topschoolsrankings.com/top-20-canadian-boarding-schools/'
sitemap = 'https://topschoolsrankings.com/sitemap.xml'
robots = 'https://topschoolsrankings.com/robots.txt'

print("Waiting 15 seconds for Vercel deployment to complete...")
time.sleep(15)

for u in urls + [sitemap, robots]:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            print(f"URL: {u} | Status: {response.status}")
    except Exception as e:
        print(f"URL: {u} | Error: {e}")

try:
    req = urllib.request.Request(redirect_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        # urllib follows redirects by default, so we check the final URL
        final_url = response.geturl()
        print(f"REDIRECT TEST: {redirect_url} -> {final_url} | Status: {response.status}")
except Exception as e:
    print(f"REDIRECT TEST Error: {e}")
