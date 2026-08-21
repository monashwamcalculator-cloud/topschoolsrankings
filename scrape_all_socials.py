import os
import re
import requests
from bs4 import BeautifulSoup
import glob
import time
import urllib3
import urllib.parse

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

svg_x = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="display:block;"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>'
svg_ig = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="display:block;"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16c-2.21 0-4-1.79-4-4s1.79-4 4-4 4 1.79 4 4-1.79 4-4 4zm7.846-10.405a1.44 1.44 0 11-2.88 0 1.44 1.44 0 012.88 0z"/></svg>'
svg_fb = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="currentColor" style="display:block;"><path d="M22.675 0h-21.35C.593 0 0 .593 0 1.325v21.351C0 23.407.593 24 1.325 24H12.82v-9.294H9.692v-3.622h3.128V8.413c0-3.1 1.893-4.788 4.659-4.788 1.325 0 2.463.099 2.795.143v3.24l-1.918.001c-1.504 0-1.795.715-1.795 1.763v2.313h3.587l-.467 3.622h-3.12V24h6.116c.73 0 1.323-.593 1.323-1.325V1.325C24 .593 23.407 0 22.675 0z"/></svg>'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

count = 0
limit = 125 # Try to do all

for filepath in glob.glob("listing/*/index.html"):
    if count >= limit:
        break
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    if "Social Media" in content:
        continue # Already processed
        
    # Find official website URL
    match = re.search(r'<a class="button button-primary" href="([^"]+)"', content)
    if not match:
        continue
        
    official_url = match.group(1)
    
    # Defaults in case not found on homepage
    tw_url = f"https://twitter.com/search?q={urllib.parse.quote(official_url)}"
    ig_url = f"https://instagram.com/"
    fb_url = f"https://facebook.com/"
    
    try:
        res = requests.get(official_url, headers=headers, timeout=10, verify=False)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        for a in soup.find_all('a', href=True):
            href = a['href'].lower()
            if 'twitter.com' in href or 'x.com' in href:
                if 'share' not in href and 'intent' not in href:
                    tw_url = a['href']
            if 'instagram.com' in href:
                ig_url = a['href']
            if 'facebook.com' in href:
                if 'sharer' not in href:
                    fb_url = a['href']
                    
    except Exception as e:
        print(f"Failed to fetch {official_url}: {e}")
        # We will still add the block, but with default links that maybe point to general search if we couldn't find them, 
        # or we can skip. Let's add them with what we have.
        pass

    # Build replacement
    replacement = f"""<div><dt>Social Media</dt><dd style="display:flex; gap:12px; align-items:center; flex-wrap:wrap; margin:0;">
      <a href="{tw_url}" target="_blank" rel="noopener noreferrer" style="color:#025492; text-decoration:none;" aria-label="X/Twitter">{svg_x}</a>
      <a href="{ig_url}" target="_blank" rel="noopener noreferrer" style="color:#025492; text-decoration:none;" aria-label="Instagram">{svg_ig}</a>
      <a href="{fb_url}" target="_blank" rel="noopener noreferrer" style="color:#025492; text-decoration:none;" aria-label="Facebook">{svg_fb}</a>
    </dd></div>"""
    
    # Insert before </dl>
    if "</dl>" in content:
        content = content.replace("</dl>", f"{replacement}</dl>")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Added socials for {filepath}")
        count += 1
    
    time.sleep(0.5) # Be nice to servers

print(f"Finished processing {count} listings.")
