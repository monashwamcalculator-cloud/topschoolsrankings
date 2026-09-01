with open('scan_mojibake.py', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()
with open('scan_mojibake.py', 'w', encoding='utf-8') as f:
    for line in lines:
        if "''" in line and "mojibake_patterns" not in line:
            pass # wait, it's in the list
        line = line.replace(", ''", "")
        f.write(line)