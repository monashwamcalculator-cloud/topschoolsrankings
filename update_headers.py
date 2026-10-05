import os
import glob
import re

# Update JS logic in assets/site.js
js_file = "assets/site.js"
with open(js_file, "r", encoding="utf-8") as f:
    js_content = f.read()

new_js = """// Category Filter Logic
document.addEventListener('DOMContentLoaded', function() {
    const filterPills = document.querySelectorAll('.filter-pill');
    const guideCards = document.querySelectorAll('.guide-card[data-category]');
    
    const headerH1 = document.querySelector('.page-header h1');
    const headerP = document.querySelector('.page-header p');
    const headerMeta = document.querySelector('.page-header .page-meta');

    const copyData = {
        'all': {
            h1: 'All Educational Guides & Rankings',
            p: 'Evidence-led comparisons, admissions explainers, and practical research checklists for students and families.'
        },
        'Global Universities': {
            h1: 'Global Universities Guides & Rankings',
            p: 'Authoritative world university rankings, institutional breakdowns, and campus guides.'
        },
        'Schools & Boarding': {
            h1: 'Schools & Boarding Guides',
            p: 'Comparative rankings and admissions pathways for elite day, grammar, and boarding schools.'
        },
        'Admissions & Visas': {
            h1: 'Admissions & Visas Guides',
            p: 'Practical checklists, CRICOS guidance, and visa requirements for international students.'
        },
        'Degree & Career Guides': {
            h1: 'Degree & Career Guides',
            p: 'Strategic roadmaps for specialized degrees, professional careers, and higher education technology.'
        }
    };

    function updateHeader(filterValue, visibleCount) {
        if (!headerH1 || !headerP || !headerMeta) return;
        
        let key = filterValue;
        if (key === 'Schools &amp; Boarding') key = 'Schools & Boarding';
        if (key === 'Admissions &amp; Visas') key = 'Admissions & Visas';
        if (key === 'Degree &amp; Career Guides') key = 'Degree & Career Guides';
        
        const data = copyData[key] || copyData['all'];
        headerH1.textContent = data.h1;
        headerP.textContent = data.p;
        headerMeta.textContent = `${visibleCount} EDITORIAL GUIDES`;
    }

    if (filterPills.length > 0 && guideCards.length > 0) {
        if (headerMeta && headerH1) {
            updateHeader('all', guideCards.length);
        }

        filterPills.forEach(pill => {
            pill.addEventListener('click', () => {
                filterPills.forEach(p => p.classList.remove('active'));
                pill.classList.add('active');

                const filterValue = pill.getAttribute('data-filter');
                let visibleCount = 0;

                guideCards.forEach(card => {
                    const category = card.getAttribute('data-category');
                    
                    card.style.animation = 'none';
                    card.offsetHeight; 
                    card.style.animation = null;

                    if (filterValue === 'all') {
                        card.classList.remove('hidden');
                        visibleCount++;
                    } else if (category === filterValue || category === filterValue.replace(/&amp;/g, '&')) {
                        card.classList.remove('hidden');
                        visibleCount++;
                    } else {
                        card.classList.add('hidden');
                    }
                });

                updateHeader(filterValue, visibleCount);
            });
        });
    }
});"""

js_content = re.sub(r'// Category Filter Logic\s*document.addEventListener.*?\}\);\s*\}\);\s*\}\);', new_js, js_content, flags=re.DOTALL)
with open(js_file, "w", encoding="utf-8", newline='\n') as f:
    f.write(js_content)

print("Updated JS filter logic.")

# Update blogs/index.html default header to match "All Guides" statically so it matches pre-hydration
blogs_index = "blogs/index.html"
with open(blogs_index, "r", encoding="utf-8") as f:
    b_html = f.read()

# I will parse the total number of articles in blogs/index.html manually to inject the right static count
total_cards = b_html.count('class="guide-card"')

b_html = re.sub(r'<h1>School &amp; University Guides</h1>', '<h1>All Educational Guides &amp; Rankings</h1>', b_html)
b_html = re.sub(r'<p>Evidence-led comparisons.*?</p>', '<p>Evidence-led comparisons, admissions explainers, and practical research checklists for students and families.</p>', b_html)
b_html = re.sub(r'<div class="page-meta">.*?</div>', f'<div class="page-meta">{total_cards} EDITORIAL GUIDES</div>', b_html)

with open(blogs_index, "w", encoding="utf-8", newline='\n') as f:
    f.write(b_html)

print("Updated blogs/index.html static header.")

# Update static category archives
cats = {
    'global-universities': {
        'h1': 'Global Universities Guides & Rankings',
        'p': 'Authoritative world university rankings, institutional breakdowns, and campus guides.'
    },
    'schools-and-boarding': {
        'h1': 'Schools & Boarding Guides',
        'p': 'Comparative rankings and admissions pathways for elite day, grammar, and boarding schools.'
    },
    'admissions-and-visas': {
        'h1': 'Admissions & Visas Guides',
        'p': 'Practical checklists, CRICOS guidance, and visa requirements for international students.'
    },
    'degree-and-career-guides': {
        'h1': 'Degree & Career Guides',
        'p': 'Strategic roadmaps for specialized degrees, professional careers, and higher education technology.'
    }
}

for slug, data in cats.items():
    cat_file = f"category/{slug}/index.html"
    if os.path.exists(cat_file):
        with open(cat_file, "r", encoding="utf-8") as f:
            html = f.read()
        
        c_cards = html.count('class="guide-card"')
        
        # Replace H1
        html = re.sub(r'<h1>.*?</h1>', f'<h1>{data["h1"].replace("&", "&amp;")}</h1>', html)
        # Replace P in page-header
        html = re.sub(r'</h1><p>.*?</p><div class="page-meta">', f'</h1><p>{data["p"]}</p><div class="page-meta">', html)
        # Replace Meta count
        html = re.sub(r'<div class="page-meta">.*?</div>', f'<div class="page-meta">{c_cards} EDITORIAL GUIDES</div>', html)
        
        with open(cat_file, "w", encoding="utf-8", newline='\n') as f:
            f.write(html)
        print(f"Updated category/{slug}/index.html with count {c_cards}")
