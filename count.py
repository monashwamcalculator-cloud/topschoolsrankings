import subprocess

def get_count(commit, filepath):
    try:
        content = subprocess.check_output(['git', 'show', f'{commit}:{filepath}']).decode('utf-8')
        return content.count('class="guide-card"')
    except Exception as e:
        return str(e)

commits = subprocess.check_output(['git', 'log', '--format=%h']).decode('utf-8').strip().split('\n')

for c in commits:
    print(f'Commit {c}: {get_count(c, "blogs/index.html")} blogs')
