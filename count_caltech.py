import os

files_to_check = []
for root, dirs, files in os.walk('.'):
    if '.git' in root or '.vercel' in root: continue
    for file in files:
        if file.endswith('.html') or file.endswith('.js') or file.endswith('.json'):
            files_to_check.append(os.path.join(root, file))

def count_in_repo(phrase):
    c = 0
    for path in files_to_check:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            if phrase.lower() in f.read().lower(): c += 1
    return c

print('Strictly Test-Blind:', count_in_repo('Strictly Test-Blind'))
print('Do not submit SAT/ACT:', count_in_repo('Do not submit SAT/ACT'))
print('Test-Blind:', count_in_repo('Test-Blind'))
print('Even a 1600:', count_in_repo('Even a 1600'))
print('test-blind policy:', count_in_repo('test-blind policy'))
print('Calculus:', count_in_repo('Calculus course in high school to even be considered'))
