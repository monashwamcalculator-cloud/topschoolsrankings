import glob
import re
import os
from datetime import datetime

# 1. Gather Trust Pages & Homepage
trust_pages = [
    "index.html",
    "blogs/index.html",
    "about-us/index.html",
    "contact-us/index.html",
    "privacy-policy/index.html",
    "terms-and-conditions/index.html",
    "disclaimer/index.html",
    "ranking-methodology/index.html",
    "editorial-policy/index.html",
    "how-it-works/index.html"
]

# 2. Extract the 106 articles from blogs/index.html
editorial_articles = []
try:
    with open("blogs/index.html", "r", encoding="utf-8") as f:
        blogs_html = f.read()
    # Find all hrefs in the guide cards
    matches = re.findall(r'href="/([^/"]+)/"', blogs_html)
    for m in set(matches):
        # some links might be /category/ - ignore those
        if not m.startswith("category"):
            path = f"{m}/index.html"
            editorial_articles.append(path)
except Exception as e:
    print(f"Error reading blogs: {e}")

# We only want genuine articles, exclude category, compare, listing, etc
editorial_articles = [a for a in editorial_articles if not a.startswith(('category', 'listing', 'compare'))]

whitelist_paths = set([os.path.normpath(p) for p in (trust_pages + editorial_articles)])

noindex_count = 0
index_count = 0
ai_leaks = []
ai_patterns = [r"1200-word", r"As an AI", r"I cannot fulfill", r"prompt", r"language model"]

sitemap_urls = []
now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

for fpath in glob.glob("**/*.html", recursive=True):
    if "node_modules" in fpath: continue
    
    normalized_path = os.path.normpath(fpath)
    
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()
            
        # Strip existing robots
        html = re.sub(r'<meta\s+name=["\']robots["\'][^>]*>', '', html, flags=re.IGNORECASE)
        
        is_indexed = False
        
        # Check rules
        # 1. Must be in whitelist OR (not in listing, compare, category, tools)
        # Wait, the prompt says: "ALL genuine editorial articles / blog directories across the repository (~106 articles)".
        # And "Keep Listings/Compare Noindexed"
        
        if normalized_path in whitelist_paths:
            is_indexed = True
        else:
            # Let's enforce strict noindex for listing, compare, category
            if any(x in normalized_path for x in ['listing', 'compare', 'category']):
                is_indexed = False
            else:
                # Tools and other random directories? We'll set them to noindex unless whitelisted.
                is_indexed = False

        if is_indexed:
            # AI Sweep
            for pattern in ai_patterns:
                if re.search(pattern, html, flags=re.IGNORECASE):
                    # Check if it's not a false positive (e.g. "prompt" might be in code, but let's just log it)
                    # "prompt" is common (e.g. prompt action). Let's restrict to 'As an AI', 'language model', etc.
                    pass
                    
            # Let's do a stricter AI sweep
            strict_ai_patterns = [r"As an AI", r"I cannot fulfill", r"I cannot provide", r"language model"]
            for pattern in strict_ai_patterns:
                if re.search(pattern, html, flags=re.IGNORECASE):
                    ai_leaks.append((fpath, pattern))
            
            # "1200-word" specifically
            if "1200-word" in html:
                ai_leaks.append((fpath, "1200-word"))

            # Add Index, Follow
            html = html.replace('</head>', '  <meta name="robots" content="index, follow">\n</head>')
            index_count += 1
            
            # Sitemap
            rel_path = normalized_path.replace("\\", "/")
            if rel_path == "index.html":
                url = "https://topschoolsrankings.com/"
                priority = "1.0"
            else:
                url = "https://topschoolsrankings.com/" + rel_path.replace("index.html", "")
                priority = "0.8"
                
            sitemap_urls.append(f"""  <url>
    <loc>{url}</loc>
    <lastmod>{now}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>""")
            
        else:
            html = html.replace('</head>', '  <meta name="robots" content="noindex, follow">\n</head>')
            noindex_count += 1
            
        with open(fpath, "w", encoding="utf-8", newline='\n') as f:
            f.write(html)
            
    except Exception as e:
        pass

sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(sitemap_urls)}
</urlset>"""

with open("sitemap.xml", "w", encoding="utf-8", newline='\n') as f:
    f.write(sitemap_xml)

print(f"Index count: {index_count}")
print(f"NoIndex count: {noindex_count}")
print(f"AI Leaks found: {len(ai_leaks)}")
for f, p in ai_leaks:
    print(f"Leak: {p} in {f}")
