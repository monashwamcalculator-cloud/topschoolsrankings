with open('how-universities-are-using-custom-software-solutions-to-build-smarter-digital-education-ecosystems/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_bio = '<p style="margin: 0; font-size: 14px; color: #4a5568; line-height: 1.5;">Guest Contributor &middot; VP of Operations, Engineering, and Growth at Unified Infotech, sharing insights on digital transformation and operational efficiency.</p>'
new_bio = '<p style="margin: 0; font-size: 14px; color: #4a5568; line-height: 1.5;"><strong>Guest Contributor</strong> &middot; Samrat Biswas is a distinguished VP of Operations, Engineering, and Growth at Unified Infotech, renowned for his deep expertise in scaling teams and refining processes. Samrat’s writings are informed by his wealth of experience, offering readers valuable insights into the intricacies of engineering leadership, operational efficiency, and driving transformational change within organizations.</p>'

html = html.replace(old_bio, new_bio)

with open('how-universities-are-using-custom-software-solutions-to-build-smarter-digital-education-ecosystems/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Updated author bio in article.')