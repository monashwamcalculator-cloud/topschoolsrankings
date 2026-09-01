import json
with open('sj_aug29.json', 'r', encoding='utf-8') as f:
    sj = json.load(f)

existing_paths = set([item['path'] for item in sj])
missing_blogs = ["top-100-international-schools-in-the-world", "boarding-schools-in-canada", "top-100-private-schools-in-canada", "top-100-private-schools-in-the-world", "top-100-grammar-schools-in-uk", "how-smart-hostels-are-changing-student-life-at-indian-universities", "top-100-schools-in-australia", "ap-vs-ib-diploma", "write-for-us", "top-100-boarding-schools-in-the-world", "top-100-international-schools-in-asia", "top-100-high-schools-in-usa", "top-100-high-schools-in-canada", "temp_docx_extract"]

for mb in missing_blogs:
    print(f'{mb} in sj: {f"/{mb}/" in existing_paths}')