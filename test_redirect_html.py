import urllib.request

url = 'https://topschoolsrankings.com/top-20-canadian-boarding-schools/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8-sig')
        if "Redirecting to" in html:
            print("FOUND old HTML redirect page!")
        else:
            print("Did not find old HTML redirect page.")
            print(html[:200])
except Exception as e:
    print(e)