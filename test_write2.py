import urllib.request

url = 'https://topschoolsrankings.com/write-for-us/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8-sig')
        if "top-20-canadian-boarding-schools" in html:
            print("Found it!")
        if "TopSchoolsRankings is committed to providing independent" in html:
            print("FOUND the new write-for-us content on the LIVE site!")
        else:
            print("Did NOT find the new write-for-us content on the live site!")
            print(html[:200])
except Exception as e:
    print(e)