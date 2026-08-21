import os
import re
import urllib.request
import urllib.parse

def get_domain(url):
    parsed_uri = urllib.parse.urlparse(url)
    domain = parsed_uri.netloc
    if domain.startswith('www.'):
        domain = domain[4:]
    return domain

count_added = 0
for root, dirs, files in os.walk('listing'):
    if 'index.html' in files:
        filepath = os.path.join(root, 'index.html')
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        # Check if logo exists
        m_logo = re.search(r'<img class="listing-profile-logo"[^>]*src="([^"]+)"', html)
        needs_logo = False
        
        if not m_logo:
            needs_logo = True
        else:
            local_path = '.' + m_logo.group(1) if m_logo.group(1).startswith('/') else os.path.join(root, m_logo.group(1))
            if not os.path.exists(local_path):
                needs_logo = True
                # Remove the broken tag
                html = re.sub(r'<img class="listing-profile-logo"[^>]*>', '', html)

        if needs_logo:
            # Find website URL
            m_url = re.search(r'<a[^>]*href="([^"]+)"[^>]*>Visit official website</a>', html, re.IGNORECASE)
            if m_url:
                url = m_url.group(1)
                domain = get_domain(url)
                listing_id = os.path.basename(root)
                
                logo_url = f"https://logo.clearbit.com/{domain}"
                save_path = f"media/listings/{listing_id}-logo.png"
                
                try:
                    req = urllib.request.Request(logo_url, headers={'User-Agent': 'Mozilla/5.0'})
                    with urllib.request.urlopen(req) as response:
                        img_data = response.read()
                        
                    os.makedirs('media/listings', exist_ok=True)
                    with open(save_path, 'wb') as f:
                        f.write(img_data)
                        
                    # Insert the img tag
                    img_tag = f'<img class="listing-profile-logo" src="/{save_path}" alt="{listing_id} logo" width="200" height="200" loading="eager" decoding="async">'
                    
                    # Insert after <div class="listing-profile-identity">
                    html = re.sub(
                        r'(<div class="listing-profile-identity">)',
                        r'\1' + img_tag,
                        html
                    )
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(html)
                    
                    print(f"Added logo for {listing_id} from {domain}")
                    count_added += 1
                except Exception as e:
                    print(f"Failed to get logo for {domain}: {e}")
            else:
                print(f"No official URL found for {root}")

print(f"Total logos added: {count_added}")
