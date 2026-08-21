import re
with open('listing/australian-national-university/index.html', 'r', encoding='utf-8') as f:
    text = f.read()
    m = re.findall(r'href="(https?://[^"]+)"', text)
    for u in set(m):
        if 'topschools' not in u and 'facebook' not in u and 'twitter' not in u and 'youtube' not in u and 'instagram' not in u:
            print('URL:', u)
