import subprocess
import json

commits = subprocess.check_output(['git', 'log', '--format=%h']).decode('utf-8').strip().split('\n')

for c in commits:
    content = subprocess.check_output(['git', 'show', f'{c}:assets/search-index.json']).decode('utf-8')
    data = json.loads(content)
    articles = [x for x in data if x.get('type') == 'article']
    print(f'Commit {c}: {len(articles)} articles, {len(data)} total items')
