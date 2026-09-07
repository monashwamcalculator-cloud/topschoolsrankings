import json

with open('vercel.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

if 'redirects' not in config:
    config['redirects'] = []

# Check if redirect already exists to avoid duplicates
existing_sources = [r.get('source') for r in config['redirects']]

new_rules = [
    {
      "source": "/top-20-canadian-boarding-schools/",
      "destination": "/boarding-schools-in-canada/",
      "permanent": True
    },
    {
      "source": "/top-20-canadian-boarding-schools",
      "destination": "/boarding-schools-in-canada/",
      "permanent": True
    }
]

for rule in new_rules:
    if rule['source'] not in existing_sources:
        config['redirects'].append(rule)

with open('vercel.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, indent=2)

print("Successfully updated vercel.json")