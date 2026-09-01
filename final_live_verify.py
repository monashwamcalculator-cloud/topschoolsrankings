import urllib.request
import re
import json
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_parts = []
    
    def handle_data(self, data):
        self.text_parts.append(data)
        
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for attr, val in attrs:
                if attr == 'alt' and val:
                    self.text_parts.append(val)

def extract_semantic_text(html_content):
    parser = TextExtractor()
    try:
        parser.feed(html_content)
    except:
        pass
    text = " ".join(parser.text_parts)
    text = re.sub(r'[\'’\x91\x92\x93\x94\x9d]|&#0?39;|&apos;|&quot;', "'", text)
    text = re.sub(r'\s+', ' ', text)
    return text.lower()

urls = [
    'https://topschoolsrankings.com/california-institute-of-technology-acceptance-rate-2026-how-hard-is-it-to-get-into-caltech/?verify=123',
    'https://topschoolsrankings.com/blogs/?verify=123'
]

phrases = {
    'tb': 'test-blind',
    'dn': 'do not submit sat/act',
    '16': "even a 1600 won't be looked at",
    'mn': 'mandatory calculus',
    'ct': 'they do not look at sat/act scores at all',
    'rq': 'caltech requires first-year applicants to submit either sat or act scores'
}

live_results = []
for url in urls:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        resp = urllib.request.urlopen(req, timeout=10)
        content = resp.read().decode('utf-8', errors='ignore')
        norm = extract_semantic_text(content)
        
        counts = {k: norm.count(v) for k, v in phrases.items()}
        live_results.append({'url': url, 'counts': counts})
    except Exception as e:
        print(f"Error fetching {url}: {e}")

print(json.dumps(live_results, indent=2))
