import os

count = 0
for root, dirs, files in os.walk('.'):
    if '.git' in root or '.vercel' in root: continue
    for file in files:
        if file.endswith('.html') or file.endswith('.json') or file.endswith('.js'):
            path = os.path.join(root, file)
            with open(path, 'rb') as f:
                b = f.read()
            
            # Find all invalid sequences
            offset = 0
            while True:
                try:
                    b[offset:].decode('utf-8')
                    break
                except UnicodeDecodeError as e:
                    absolute_start = offset + e.start
                    absolute_end = offset + e.end
                    start = max(0, absolute_start - 10)
                    end = min(len(b), absolute_end + 10)
                    if count < 50:
                        print(f"{path} at {absolute_start}: {b[start:end]} (bad: {[hex(x) for x in b[absolute_start:absolute_end]]})")
                    count += 1
                    offset = absolute_end

print(f"Total invalid UTF-8 sequences: {count}")
