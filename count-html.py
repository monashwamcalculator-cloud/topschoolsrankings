import os
import glob
dirs = [d for d in os.listdir(r'C:\Users\Hp\topschoolsrankings-html') if os.path.isdir(os.path.join(r'C:\Users\Hp\topschoolsrankings-html', d)) and d not in ('.vercel', 'assets', 'author', 'blogs', 'category', 'compare', 'contact-us', 'disclaimer', 'editorial-policy', 'listings', 'media', 'privacy-policy', 'ranking-methodology', 'terms-and-conditions', 'tools', 'utils', 'about-us', 'listing', 'ranking-methodology', 'how-it-works', 'faq', 'wp-content', 'wpress-extracted', '_uploads_extract', '_import-live-jul2026', '_import-well-known', 'live-site-backup', 'dist', 'dist-deploy', 'upload-addon', '_zip-staging-tools-rich')]
print('Total article dirs in topschoolsrankings-html:', len(dirs))
