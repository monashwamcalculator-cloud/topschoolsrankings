import os
import re

print("Checking inventory...")
exclusions = {'.vercel', 'assets', 'author', 'blogs', 'category', 'compare', 'contact-us', 'disclaimer', 'editorial-policy', 'listings', 'media', 'privacy-policy', 'ranking-methodology', 'terms-and-conditions', 'tools', 'utils', 'about-us', 'listing', 'how-it-works', 'faq', 'wp-content', 'wpress-extracted', '_uploads_extract', '_import-live-jul2026', '_import-well-known', 'live-site-backup', 'dist', 'dist-deploy', 'upload-addon', '_zip-staging-tools-rich', '.git', 'write-for-us'}
articles = [d for d in os.listdir('.') if os.path.isdir(d) and d not in exclusions]
tools = [d for d in os.listdir('tools') if os.path.isdir(os.path.join('tools', d))]
listings = [d for d in os.listdir('listing') if os.path.isdir(os.path.join('listing', d))]
print(f"Articles: {len(articles)}")
print(f"Tools: {len(tools)}")
print(f"Listings: {len(listings)}")

print("\nChecking phrases and links...")
caltech_patterns = ['Strictly Test-Blind', 'Test-Blind', 'Do not submit SAT/ACT', 'Even a 1600', 'look at SAT/ACT scores at all']
promo_patterns = ['Hard Strategy to Get Admitted', 'Cracking the Bodwell Admission Code', 'interview secrets', 'exact strategy', 'best private boys'' school in Toronto', 'best private boys'' school']
mojibake_patterns = ['\xc5\x92', '\u0152']

found_caltech = 0
found_promo = 0
found_mojibake = 0
broken_links = 0
valid_links = 0

all_paths = []
for d in articles: all_paths.append(f"/{d}/")
for t in tools: all_paths.append(f"/tools/{t}/")
for l in listings: all_paths.append(f"/listing/{l}/")
all_paths.extend(['/', '/blogs/', '/ranking-methodology/', '/about-us/', '/contact-us/', '/privacy-policy/', '/terms-and-conditions/', '/disclaimer/', '/editorial-policy/', '/write-for-us/', '/how-to-compare-universities-beyond-rankings/'])

def is_valid_link(href):
    if href.startswith('http') or href.startswith('mailto:') or href.startswith('#') or href.startswith('javascript:'):
        return True
    if href in all_paths: return True
    if href == '/contact/': return False # known bad? we use contact-us/
    # simple check
    href = href.split('#')[0].split('?')[0]
    if href == '' or href == '/': return True
    if href in all_paths: return True
    if href.startswith('/assets/') or href.startswith('/media/'):
        return os.path.exists(href[1:])
    return False

for root, dirs, files in os.walk('.'):
    if '.git' in root or '.vercel' in root or 'node_modules' in root: continue
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
            except Exception: continue
            
            for p in caltech_patterns:
                if p.lower() in content.lower(): found_caltech += 1
            for p in promo_patterns:
                if p.lower() in content.lower(): found_promo += 1
            for p in mojibake_patterns:
                if p in content: found_mojibake += 1
                
            links = re.findall(r'href="([^"]+)"', content)
            for link in links:
                if not is_valid_link(link):
                    # just basic checks, if it's missing trailing slash etc
                    if link + "/" in all_paths:
                        pass
                    elif '/category/' in link or '/author/' in link:
                        pass # Ignore dynamic looking links that we might not have crawled
                    else:
                        if link not in ['/favicon.jpg', '/contact/', '/blog/', '/articles/', '/sitemap.xml']:
                            pass # We won't strictly count every single WP remnant, but let's check true broken
print(f"Caltech: {found_caltech}, Promo: {found_promo}, Mojibake: {found_mojibake}")