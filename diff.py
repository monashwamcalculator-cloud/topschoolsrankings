import os
def get_dirs(path):
    exclusions = {'.vercel', 'assets', 'author', 'blogs', 'category', 'compare', 'contact-us', 'disclaimer', 'editorial-policy', 'listings', 'media', 'privacy-policy', 'ranking-methodology', 'terms-and-conditions', 'tools', 'utils', 'about-us', 'listing', 'how-it-works', 'faq', 'wp-content', 'wpress-extracted', '_uploads_extract', '_import-live-jul2026', '_import-well-known', 'live-site-backup', 'dist', 'dist-deploy', 'upload-addon', '_zip-staging-tools-rich', '.git'}
    return set([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d)) and d not in exclusions])

aug_blogs = get_dirs('.')
aug_tools = set([d for d in os.listdir('tools') if os.path.isdir(os.path.join('tools', d))])
aug_listings = set([d for d in os.listdir('listing') if os.path.isdir(os.path.join('listing', d))])

os.system('git checkout master')

cur_blogs = get_dirs('.')
cur_tools = set([d for d in os.listdir('tools') if os.path.isdir(os.path.join('tools', d))])
cur_listings = set([d for d in os.listdir('listing') if os.path.isdir(os.path.join('listing', d))])

print('MISSING BLOGS:', ', '.join(aug_blogs - cur_blogs))
print('MISSING TOOLS:', ', '.join(aug_tools - cur_tools))
print('MISSING LISTINGS:', ', '.join(aug_listings - cur_listings))
