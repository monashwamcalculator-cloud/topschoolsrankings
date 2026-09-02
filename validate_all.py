import os

print("--- VALIDATION RESULTS ---")
os.system('python check_caltech.py')
os.system('python check_promo.py')
os.system('python scan_mojibake.py')

exclusions = {'.vercel', 'assets', 'author', 'blogs', 'category', 'compare', 'contact-us', 'disclaimer', 'editorial-policy', 'listings', 'media', 'privacy-policy', 'ranking-methodology', 'terms-and-conditions', 'tools', 'utils', 'about-us', 'listing', 'how-it-works', 'faq', 'wp-content', 'wpress-extracted', '_uploads_extract', '_import-live-jul2026', '_import-well-known', 'live-site-backup', 'dist', 'dist-deploy', 'upload-addon', '_zip-staging-tools-rich', '.git', 'write-for-us'}
print(f"Articles: {len([d for d in os.listdir('.') if os.path.isdir(d) and d not in exclusions])}")
print(f"Tools: {len([d for d in os.listdir('tools') if os.path.isdir(os.path.join('tools', d))])}")
print(f"Listings: {len([d for d in os.listdir('listing') if os.path.isdir(os.path.join('listing', d))])}")