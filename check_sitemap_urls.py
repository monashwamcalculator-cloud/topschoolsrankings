import xml.etree.ElementTree as ET

tree = ET.parse('sitemap_aug29.xml')
existing_urls = set([loc.text for loc in tree.getroot().findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')])

missing_blogs = ["top-100-international-schools-in-the-world", "boarding-schools-in-canada", "top-100-private-schools-in-canada", "top-100-private-schools-in-the-world", "top-100-grammar-schools-in-uk", "how-smart-hostels-are-changing-student-life-at-indian-universities", "top-100-schools-in-australia", "ap-vs-ib-diploma", "write-for-us", "top-100-boarding-schools-in-the-world", "top-100-international-schools-in-asia", "top-100-high-schools-in-usa", "top-100-high-schools-in-canada", "temp_docx_extract"]

for mb in missing_blogs:
    url = f'https://topschoolsrankings.com/{mb}/'
    print(f'{mb} in sitemap: {url in existing_urls}')