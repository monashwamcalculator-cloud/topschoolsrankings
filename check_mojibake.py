with open('top-25-universities-in-canada-for-international-students/index.html', 'rb') as f:
    content = f.read()

count = content.count(b'\xef\xbf\xbd')
print(f"Number of U+FFFD replacement characters: {count}")

if count > 0:
    idx = content.find(b'\xef\xbf\xbd')
    print(content[max(0, idx-10):idx+20].decode('utf-8', errors='replace'))