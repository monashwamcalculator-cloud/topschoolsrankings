import os

def get_dirs(path):
    return set([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d)) and d not in ('.vercel', 'assets', 'author', 'blogs', 'category', 'compare', 'contact-us', 'disclaimer', 'editorial-policy', 'listings', 'media', 'privacy-policy', 'ranking-methodology', 'terms-and-conditions', 'tools', 'utils', 'about-us', 'listing', 'ranking-methodology', 'how-it-works', 'faq', 'wp-content', 'wpress-extracted', '_uploads_extract', '_import-live-jul2026', '_import-well-known', 'live-site-backup', 'dist', 'dist-deploy', 'upload-addon', '_zip-staging-tools-rich', '.git')])

dirs_html = get_dirs(r'C:\Users\Hp\topschoolsrankings-html')
dirs_v2 = get_dirs(r'C:\Users\Hp\Downloads\topschoolsrankings-new-site-upload-v2')

print('Missing in v2:', dirs_html - dirs_v2)
