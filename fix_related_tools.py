import glob
import re

# 1. Build a dictionary of tool names to URLs from tools/index.html
with open('tools/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

url_map = {}
matches = re.finditer(r'<h2><a href="([^"]+)">([^<]+)</a></h2>', html)
for m in matches:
    url = m.group(1)
    name = m.group(2)
    # create variations of the name
    clean_name = re.sub(r'\s*\(.*?\)', '', name).strip().lower()
    split_name = clean_name.split(':')[0].strip().lower()
    
    url_map[name.lower()] = url
    url_map[clean_name] = url
    url_map[split_name] = url
    url_map[clean_name.replace(' & ', ' and ')] = url

# specific manual overrides just in case they don't match exactly
url_map['sat score estimator'] = '/tools/sat-score-estimator/'
url_map['act score estimator'] = '/tools/act-score-estimator/'
url_map['merit aid estimator'] = '/tools/merit-aid-estimator/'
url_map['act to sat converter'] = '/tools/act-to-sat-converter/'
url_map['ielts to toefl converter'] = '/tools/ielts-toefl-converter/'
url_map['university application timeline planner'] = '/tools/application-timeline-planner/'
url_map['boarding school cost calculator'] = '/tools/boarding-school-cost-calculator/'
url_map['gap year budget planner'] = '/tools/gap-year-budget-planner/'
url_map['study abroad budget planner'] = '/tools/study-abroad-budget-planner/'
url_map['student cost of living comparison'] = '/tools/cost-of-living-comparison/'
url_map['university cost calculator'] = '/tools/university-cost-calculator/'
url_map['a-level average grade calculator'] = '/tools/a-level-average-calculator/'
url_map['ib total points calculator'] = '/tools/ib-total-points-calculator/'
url_map['ucas tariff calculator'] = '/tools/ucas-tariff-calculator/'
url_map['international student application checklist'] = '/tools/international-student-checklist/'
url_map['boarding school readiness quiz'] = '/tools/boarding-school-readiness-quiz/'
url_map['us college fit quiz'] = '/tools/us-college-fit-quiz/'
url_map['scholarship eligibility quiz'] = '/tools/scholarship-eligibility-quiz/'
url_map['ap gpa calculator'] = '/tools/ap-gpa-calculator/'
url_map['weighted gpa calculator'] = '/tools/weighted-gpa-calculator/'
url_map['atar to gpa converter'] = '/tools/atar-gpa-converter/'
url_map['ib to gpa converter'] = '/tools/ib-to-gpa-converter/'
url_map['gpa to percentage converter'] = '/tools/gpa-percentage-converter/'
url_map['cgpa to percentage converter'] = '/tools/cgpa-percentage-converter/'
url_map['class rank percentile calculator'] = '/tools/class-rank-percentile-estimator/'
url_map['gre score estimator'] = '/tools/gre-score-estimator/'
url_map['duolingo english test to ielts converter'] = '/tools/duolingo-ielts-converter/'
url_map['pte to ielts converter'] = '/tools/pte-ielts-converter/'
url_map['uk boarding school fees calculator'] = '/tools/uk-boarding-fees-calculator/'
url_map['private vs public school cost comparison'] = '/tools/private-vs-public-school-cost/'
url_map['dorm vs off-campus housing cost calculator'] = '/tools/dorm-vs-off-campus-calculator/'
url_map['nsw selective school score estimator'] = '/tools/nsw-selective-score-estimator/'
url_map['hsc to atar estimator'] = '/tools/hsc-atar-estimator/'
url_map['student loan repayment calculator'] = '/tools/student-loan-repayment-calculator/'

# Some variations might have slightly different names in the related tools section
url_map['class rank percentile estimator'] = '/tools/class-rank-percentile-estimator/'
url_map['international student checklist'] = '/tools/international-student-checklist/'
url_map['dorm vs off-campus cost calculator'] = '/tools/dorm-vs-offcampus-calculator/'
url_map['private vs public school cost'] = '/tools/private-vs-public-school-cost/'

def replace_h3(match):
    name = match.group(1)
    name_clean = name.strip().lower()
    url = url_map.get(name_clean)
    if url:
        return f'<h3><a href="{url}">{name}</a></h3>'
    else:
        # Debug missing
        pass # print(f"Warning: Could not find URL for related tool: '{name}'")
        return match.group(0) # don't change if not found

count_fixed = 0
for filepath in glob.glob('tools/**/*.html', recursive=True):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if '<h2>Related tools</h2>' in html:
        original = html
        
        # We need to only replace <h3> inside the Related tools section to avoid breaking other h3s
        # Let's split at "<h2>Related tools</h2>"
        parts = html.split('<h2>Related tools</h2>')
        
        # It should only appear once
        if len(parts) == 2:
            # We want to replace <h3> until the next <h2>
            subparts = parts[1].split('<h2>', 1)
            if len(subparts) == 2:
                related_section = subparts[0]
                rest = '<h2>' + subparts[1]
                
                # Replace <h3>...</h3> inside related_section
                related_section = re.sub(r'<h3>(.*?)</h3>', replace_h3, related_section)
                
                html = parts[0] + '<h2>Related tools</h2>' + related_section + rest
            else:
                related_section = parts[1]
                related_section = re.sub(r'<h3>(.*?)</h3>', replace_h3, related_section)
                html = parts[0] + '<h2>Related tools</h2>' + related_section
                
            if html != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(html)
                count_fixed += 1

pass # print(f"Fixed related tools in {count_fixed} files.")
