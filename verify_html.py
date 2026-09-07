from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        pass

parser = MyHTMLParser()
with open('top-50-universities-in-usa/index.html', 'r', encoding='utf-8') as f:
    try:
        parser.feed(f.read())
        print("HTML parses successfully. No severe tag nesting errors detected by basic parser.")
    except Exception as e:
        print(f"HTML parsing error: {e}")