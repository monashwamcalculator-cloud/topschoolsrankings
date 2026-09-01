import os

def get_dirs(path):
    exclusions = {
        '.vercel', 'assets', 'author', 'blogs', 'category', 'compare', 'contact-us', 
        'disclaimer', 'editorial-policy', 'listings', 'media', 'privacy-policy', 
        'ranking-methodology', 'terms-and-conditions', 'tools', 'utils', 'about-us', 
        'listing', 'how-it-works', 'faq', 'wp-content', 'wpress-extracted', 
        '_uploads_extract', '_import-live-jul2026', '_import-well-known', 'live-site-backup', 
        'dist', 'dist-deploy', 'upload-addon', '_zip-staging-tools-rich', '.git',
        'cgi-bin', 'admin', 'api', 'node_modules', 'add-listing', 'single-upload-fix',
        'listings-fix-patch', 'listings-ONE-FILE-FIX', 'scripts', 'config', 'review-stats-patch',
        'site-fixes-patch', 'upload-karo-ye-sab', 'content-drafts', 'listings-PAGINATION-FIX',
        'includes', 'cron', 'account', 'upload-ab-karo', 'google-tag-patch', '.well-known', '.cursor',
        'write-for-us', 'topschoolsrankings-com-20260526-062650-1hg8h2vwtde5', 'listings-fix-v2', 'data', 'new one'
    }
    return set([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d)) and d not in exclusions])

dirs_html = get_dirs(r'C:\Users\Hp\topschoolsrankings-html')
dirs_v2 = get_dirs(r'C:\Users\Hp\Downloads\topschoolsrankings-new-site-upload-v2')

print('True article count in topschoolsrankings-html:', len(dirs_html))
print('True article count in v2:', len(dirs_v2))
print('Missing in v2:', dirs_html - dirs_v2)
