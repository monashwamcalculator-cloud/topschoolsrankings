import glob
import re

url_map = {}
url_map['gpa ↔ percentage converter'] = '/tools/gpa-percentage-converter/'
url_map['cgpa ↔ percentage converter'] = '/tools/cgpa-percentage-converter/'
url_map['act ↔ sat converter'] = '/tools/act-to-sat-converter/'
url_map['ielts ↔ toefl converter'] = '/tools/ielts-toefl-converter/'
url_map['pte ↔ ielts converter'] = '/tools/pte-ielts-converter/'
url_map['duolingo ↔ ielts converter'] = '/tools/duolingo-ielts-converter/'
url_map['atar ↔ gpa converter'] = '/tools/atar-gpa-converter/'
url_map['class rank percentile'] = '/tools/class-rank-percentile-estimator/'
url_map['uk boarding fees calculator'] = '/tools/uk-boarding-fees-calculator/'
url_map['cost of living comparison'] = '/tools/cost-of-living-comparison/'
url_map['dorm vs off-campus calculator'] = '/tools/dorm-vs-offcampus-calculator/'
url_map['application timeline planner'] = '/tools/application-timeline-planner/'
url_map['a-level average calculator'] = '/tools/a-level-average-calculator/'
url_map['nsw selective score estimator'] = '/tools/nsw-selective-score-estimator/'
url_map['international student application checklist'] = '/tools/international-student-checklist/'
url_map['student loan repayment calculator'] = '/tools/student-loan-repayment-calculator/'
url_map['dorm vs off-campus housing cost calculator'] = '/tools/dorm-vs-offcampus-calculator/'

def replace_h3(match):
    name = match.group(1)
    name_clean = name.strip().lower()
    url = url_map.get(name_clean)
    if url:
        return f'<h3><a href="{url}">{name}</a></h3>'
    else:
        return match.group(0)

count = 0
for filepath in glob.glob('tools/**/*.html', recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    original = html
    if '<h2>Related tools</h2>' in html:
        parts = html.split('<h2>Related tools</h2>')
        if len(parts) == 2:
            subparts = parts[1].split('<h2>', 1)
            if len(subparts) == 2:
                related_section = subparts[0]
                rest = '<h2>' + subparts[1]
                related_section = re.sub(r'<h3>([^<]+)</h3>', replace_h3, related_section)
                html = parts[0] + '<h2>Related tools</h2>' + related_section + rest
            else:
                related_section = parts[1]
                related_section = re.sub(r'<h3>([^<]+)</h3>', replace_h3, related_section)
                html = parts[0] + '<h2>Related tools</h2>' + related_section
                
            if original != html:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(html)
                count += 1
print(f"Fixed missing tool links in {count} files.")
