import re

svgs = {
    "math": '<svg style="width:32px; height:32px; margin-bottom:10px; color:#0056b3;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2" ry="2"></rect><line x1="8" y1="6" x2="16" y2="6"></line><line x1="16" y1="14" x2="16" y2="18"></line><path d="M16 10h.01"></path><path d="M12 10h.01"></path><path d="M8 10h.01"></path><path d="M12 14h.01"></path><path d="M8 14h.01"></path><path d="M12 18h.01"></path><path d="M8 18h.01"></path></svg>',
    "money": '<svg style="width:32px; height:32px; margin-bottom:10px; color:#28a745;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>',
    "calendar": '<svg style="width:32px; height:32px; margin-bottom:10px; color:#e83e8c;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>',
    "document": '<svg style="width:32px; height:32px; margin-bottom:10px; color:#17a2b8;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>',
    "convert": '<svg style="width:32px; height:32px; margin-bottom:10px; color:#fd7e14;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 3 21 3 21 8"></polyline><line x1="4" y1="14" x2="21" y2="3"></line><polyline points="8 21 3 21 3 16"></polyline><line x1="20" y1="10" x2="3" y2="21"></line></svg>',
    "quiz": '<svg style="width:32px; height:32px; margin-bottom:10px; color:#ffc107;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>'
}

def get_icon(title):
    t = title.lower()
    if 'convert' in t: return svgs['convert']
    if 'cost' in t or 'budget' in t or 'aid' in t or 'scholarship' in t or 'fee' in t or 'loan' in t: return svgs['money']
    if 'timeline' in t or 'planner' in t or 'year' in t: return svgs['calendar']
    if 'quiz' in t or 'check' in t: return svgs['quiz']
    if 'checklist' in t or 'guide' in t: return svgs['document']
    return svgs['math']  # Default for calculators/estimators

with open('tools/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

def replace_article(m):
    article = m.group(0)
    # Get title
    title_match = re.search(r'<h2><a[^>]*>(.*?)</a></h2>', article)
    if title_match:
        title = title_match.group(1)
        icon = get_icon(title)
        # Check if already has svg
        if '<svg ' not in article:
            # Insert icon before <span>Planning tool</span>
            article = article.replace('<span>Planning tool</span>', f'{icon} <span>Planning tool</span>')
    return article

html = re.sub(r'<article class="listing-card">.*?</article>', replace_article, html, flags=re.DOTALL)

with open('tools/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
