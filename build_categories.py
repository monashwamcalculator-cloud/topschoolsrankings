import os
import glob
import re

cat_map = {
    "Global Universities": {
        "slug": "global-universities",
        "h1": "Global Universities Guides",
        "desc": "Independent research, rankings, and deep-dives on the world's top universities."
    },
    "Schools & Boarding": {
        "slug": "schools-and-boarding",
        "h1": "Schools & Boarding Guides",
        "desc": "Admissions insights and fee comparisons for elite Schools & Boarding and boarding programs."
    },
    "Admissions & Visas": {
        "slug": "admissions-and-visas",
        "h1": "Admissions & Visas Guides",
        "desc": "Practical checklists and policy updates for university applications and student visas."
    },
    "Degree & Career Guides": {
        "slug": "degree-and-career-guides",
        "h1": "Degree & Career Guides",
        "desc": "Explore academic pathways, degree ROIs, and career opportunities for international students."
    }
}

# 1. Update the Footer globally across all files
def update_footers():
    new_footer_column = """<div><h2>Research</h2><a href="/blogs/">All Guides</a><a href="/category/global-universities/">Global Universities</a><a href="/category/schools-and-boarding/">Schools &amp; Boarding</a><a href="/category/admissions-and-visas/">Admissions &amp; Visas</a><a href="/category/degree-and-career-guides/">Degree &amp; Career Guides</a></div>"""
    
    old_footer_pattern = r'<div>\s*<h2>Research</h2>\s*<a href="/blogs/">All Guides</a>\s*<a href="/blogs/\?category=global-universities">Global Universities</a>.*?</div>'
    
    count = 0
    for file_path in glob.glob("**/*.html", recursive=True):
        if "node_modules" in file_path: continue
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                html = f.read()
            
            # Re-run the generic replacement from previous step just in case, or target the specific string
            # We'll just replace the whole Research column
            new_html = re.sub(r'<div>\s*<h2>Research</h2>.*?</div>', new_footer_column, html, flags=re.IGNORECASE | re.DOTALL)
            
            if new_html != html:
                with open(file_path, "w", encoding="utf-8", newline='\n') as f:
                    f.write(new_html)
                count += 1
        except Exception:
            pass
    print(f"Updated footers in {count} files")

# 2. Update category badges (in card-meta spans and eyebrow spans) globally
def update_category_badges():
    count = 0
    for file_path in glob.glob("**/*.html", recursive=True):
        if "node_modules" in file_path: continue
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                html = f.read()
                
            new_html = html
            
            # Replace card-meta spans
            def card_meta_replacer(match):
                prefix = match.group(1) # <div class="card-meta"><span>
                cat_name = match.group(2) # Schools & Boarding
                suffix = match.group(3) # </span>
                
                # Check if it's already a link
                if "<a " in cat_name: return match.group(0)
                
                clean_name = cat_name.replace("&amp;", "&").strip()
                if clean_name in cat_map:
                    slug = cat_map[clean_name]["slug"]
                    return f'{prefix}<a href="/category/{slug}/" style="color:inherit;text-decoration:none;">{cat_name}</a>{suffix}'
                return match.group(0)
                
            new_html = re.sub(r'(<div[^>]*class=["\']card-meta["\'][^>]*>\s*<span[^>]*>)(.*?)(</span>)', card_meta_replacer, new_html, flags=re.IGNORECASE)

            # Replace eyebrow spans
            def eyebrow_replacer(match):
                prefix = match.group(1) # <span class="eyebrow">
                cat_name = match.group(2)
                suffix = match.group(3)
                
                if "<a " in cat_name: return match.group(0)
                
                clean_name = cat_name.replace("&amp;", "&").strip()
                if clean_name in cat_map:
                    slug = cat_map[clean_name]["slug"]
                    return f'{prefix}<a href="/category/{slug}/" style="color:inherit;text-decoration:none;">{cat_name}</a>{suffix}'
                return match.group(0)
                
            new_html = re.sub(r'(<span[^>]*class=["\']eyebrow["\'][^>]*>)(.*?)(</span>)', eyebrow_replacer, new_html, flags=re.IGNORECASE)

            if new_html != html:
                with open(file_path, "w", encoding="utf-8", newline='\n') as f:
                    f.write(new_html)
                count += 1
        except Exception:
            pass
    print(f"Updated badges in {count} files")

# 3. Build Category Archives
def build_category_archives():
    with open("blogs/index.html", "r", encoding="utf-8") as f:
        master_html = f.read()
        
    for cat_name, data in cat_map.items():
        slug = data["slug"]
        
        # 1. Setup directory
        cat_dir = os.path.join("category", slug)
        os.makedirs(cat_dir, exist_ok=True)
        
        # 2. Extract articles matching category
        articles = []
        for match in re.finditer(r'<article[^>]*class=["\']guide-card["\'][^>]*>.*?</article>', master_html, flags=re.IGNORECASE | re.DOTALL):
            article_html = match.group(0)
            clean_cat_name = cat_name.replace("&", "&amp;")
            
            # Check either data-category="Global Universities" or inside card-meta
            if f'data-category="{cat_name}"' in article_html or f'data-category="{clean_cat_name}"' in article_html:
                articles.append(article_html)

        # 3. Create the new page HTML
        # Extract everything before category-filters or guide-grid
        split_pre = re.split(r'<div class="category-filters">|<div class="guide-grid">', master_html, 1)
        header_part = split_pre[0]
        
        # Modify header (H1, p, breadcrumbs)
        header_part = re.sub(r'<h1>.*?</h1>', f'<h1>{data["h1"]}</h1>', header_part)
        header_part = re.sub(r'<p>.*?</p>', f'<p>{data["desc"]}</p>', header_part, count=1)
        header_part = re.sub(r'<div class="page-meta">.*?</div>', f'<div class="page-meta">{len(articles)} editorial guides</div>', header_part)
        
        # Breadcrumbs
        # Replace: <a href="/">Home</a><span><i aria-hidden="true">/</i><b>Guides</b></span>
        new_breadcrumbs = f'<a href="/">Home</a><span><i aria-hidden="true">/</i><a href="/blogs/">Guides</a></span><span><i aria-hidden="true">/</i><b>{cat_name}</b></span>'
        header_part = re.sub(r'<nav aria-label="Breadcrumb".*?</nav>', f'<nav aria-label="Breadcrumb" class="breadcrumbs site-container">{new_breadcrumbs}</nav>', header_part)
        
        # We don't include the JS category filters on the dedicated category pages.
        # Then the grid, then footer
        # Extract footer part (everything after the closing </div> of guide-grid)
        split_post = re.split(r'</article>\s*</div>\s*</section>', master_html, 1)
        footer_part = split_post[1] if len(split_post) > 1 else ""
        
        final_html = header_part + '\n<div class="guide-grid">\n' + '\n'.join(articles) + '\n</div>\n</section>\n' + footer_part
        
        # Ensure footer is properly updated in this generated file too (since master_html was read earlier, maybe footers weren't fully propagated in memory? Just to be safe)
        new_footer_column = """<div><h2>Research</h2><a href="/blogs/">All Guides</a><a href="/category/global-universities/">Global Universities</a><a href="/category/schools-and-boarding/">Schools &amp; Boarding</a><a href="/category/admissions-and-visas/">Admissions &amp; Visas</a><a href="/category/degree-and-career-guides/">Degree &amp; Career Guides</a></div>"""
        final_html = re.sub(r'<div>\s*<h2>Research</h2>.*?</div>', new_footer_column, final_html, flags=re.IGNORECASE | re.DOTALL)
        
        out_path = os.path.join(cat_dir, "index.html")
        with open(out_path, "w", encoding="utf-8", newline='\n') as f:
            f.write(final_html)
        print(f"Created {out_path} with {len(articles)} articles.")

# Execute all steps
update_footers()
update_category_badges()
build_category_archives()

