import xml.etree.ElementTree as ET

tree = ET.parse('sitemap_aug29.xml')
existing_urls = set([loc.text for loc in tree.getroot().findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')])

missing_tools = ['semester-gpa-required-calculator', 'target-gpa-calculator', 'cumulative-gpa-calculator', 'exam-passing-internal-marks-calculator', 'final-grade-calculator', 'cgpa-recovery-placement-target-calculator', 'backlog-cgpa-calculator', 'wam-calculator', 'college-chances-calculator', 'wam-to-gpa-converter', 'gpa-to-wam-converter', 'college-attendance-safe-bunk-calculator']

for mt in missing_tools:
    url = f'https://topschoolsrankings.com/tools/{mt}/'
    print(f'{mt} in sitemap: {url in existing_urls}')