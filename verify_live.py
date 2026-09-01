import urllib.request
import time

url = 'https://topschoolsrankings.com/bodwell-high-school-acceptance-rate-admissions-strategy/?v=123'

for _ in range(5):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req).read().decode('utf-8')
        if 'Bodwell High School Admissions Guide' in res:
            print('DEPLOYMENT IS LIVE!')
            break
        else:
            print('Waiting for deployment...')
            time.sleep(2)
    except Exception as e:
        print(e)
        time.sleep(2)
