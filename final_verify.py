import urllib.request
import time

url = f'https://topschoolsrankings.com/?bust={int(time.time())}'
try:
    response = urllib.request.urlopen(url)
    status = response.getcode()
    raw_bytes = response.read()
    html = raw_bytes.decode('utf-8')
    
    bom_present = raw_bytes.startswith(b'\xef\xbb\xbf')
    counters_correct = '104' in html and '46' in html and '135' in html
    logo_correct = 'logo.png' in html
    tools_present = '/tools/a-level-average-calculator/' in html
    
    print(f'HTTP: {status}')
    print(f'BOM Present: {bom_present}')
    print(f'Counters Correct: {counters_correct}')
    print(f'Logo Correct: {logo_correct}')
    print(f'Tools Present: {tools_present}')
    
    if status == 200 and bom_present and counters_correct and logo_correct and tools_present:
        print('LIVE VERIFICATION: PASS')
    else:
        print('LIVE VERIFICATION: FAIL')
except Exception as e:
    print('Error:', e)
    print('LIVE VERIFICATION: FAIL')