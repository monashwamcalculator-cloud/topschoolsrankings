with open('top-25-universities-in-canada-for-international-students/index.html', 'rb') as f:
    content = f.read()
    
idx = content.find(b'Montr')
if idx != -1:
    print(content[idx:idx+20].hex(' '))
    print(content[idx:idx+20].decode('utf-8', errors='replace'))