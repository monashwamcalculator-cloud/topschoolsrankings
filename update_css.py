import os
import glob

# For final grade calculator
path1 = "tools/final-grade-calculator/index.html"
with open(path1, "r", encoding="utf-8") as f:
    c = f.read()

# Replace custom classes with original classes
c = c.replace('<section class="custom-tool-panel">', '<section class="tool-panel" data-custom>')
c = c.replace('<div class="custom-tool-fields">', '<div class="tool-fields">')
c = c.replace('class="custom-tool-result', 'class="tool-result')
# Remove the custom styles
c = c.replace("""<style>
.custom-tool-panel { background: #f8f9fa; border: 1px solid #dee2e6; border-radius: 8px; padding: 24px; margin-bottom: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.02); }
.custom-tool-fields { display: flex; flex-direction: column; gap: 16px; margin-bottom: 20px; }
.custom-tool-fields label { display: flex; flex-direction: column; font-weight: 500; font-size: 14px; }
.custom-tool-fields input { padding: 10px; border: 1px solid #ccc; border-radius: 4px; font-size: 16px; margin-top: 6px; }
.custom-tool-result { margin-top: 20px; padding: 15px; border-radius: 6px; font-weight: 600; font-size: 18px; text-align: center; }
.result-success { background: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
.result-warning { background: #fff3cd; color: #856404; border: 1px solid #ffeeba; }
.result-danger { background: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }
</style>""", """<style>
.result-success { background: #d4edda; color: #155724; border-color: #c3e6cb; }
.result-warning { background: #fff3cd; color: #856404; border-color: #ffeeba; }
.result-danger { background: #f8d7da; color: #721c24; border-color: #f5c6cb; }
</style>""")

with open(path1, "w", encoding="utf-8") as f:
    f.write(c)

# For chances predictor
path2 = "tools/college-chances-calculator/index.html"
with open(path2, "r", encoding="utf-8") as f:
    c2 = f.read()

c2 = c2.replace('<section class="custom-tool-panel">', '<section class="tool-panel" data-custom>')
c2 = c2.replace('<div class="custom-tool-fields">', '<div class="tool-fields">')
c2 = c2.replace('class="custom-tool-result', 'class="tool-result')

c2 = c2.replace("""<style>
.custom-tool-panel { background: #f8f9fa; border: 1px solid #dee2e6; border-radius: 8px; padding: 24px; margin-bottom: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.02); }
.custom-tool-fields { display: flex; flex-direction: column; gap: 16px; margin-bottom: 20px; }
.custom-tool-fields label { display: flex; flex-direction: column; font-weight: 500; font-size: 14px; }
.custom-tool-fields input, .custom-tool-fields select { padding: 10px; border: 1px solid #ccc; border-radius: 4px; font-size: 16px; margin-top: 6px; }
.custom-tool-result { margin-top: 20px; padding: 20px; border-radius: 6px; text-align: center; }
.custom-tool-result h3 { margin: 0 0 10px 0; font-size: 24px; text-transform: uppercase; letter-spacing: 1px; }
.custom-tool-result p { margin: 0; font-size: 16px; opacity: 0.9; }
.tier-safety { background: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
.tier-match { background: #cce5ff; color: #004085; border: 1px solid #b8daff; }
.tier-reach { background: #fff3cd; color: #856404; border: 1px solid #ffeeba; }
.tier-far-reach { background: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }
</style>""", """<style>
.tool-fields select { width: 100%; height: 48px; border: 1px solid rgba(255, 255, 255, .2); border-radius: 9px; padding: 0 13px; background: rgba(255, 255, 255, .09); color: white; outline: none; }
.tool-fields select:focus { border-color: var(--gold-500); box-shadow: 0 0 0 3px rgba(230, 173, 58, .16); }
.tool-fields select option { background: #1a2535; color: white; }
.tool-result h3 { margin: 0 0 8px 0; color: inherit; font-size: 20px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; }
.tool-result p { margin: 0; font-size: 15px; opacity: 0.9; font-weight: normal; }
.tier-safety { background: rgba(40, 167, 69, 0.15); color: #8de49f; border-color: rgba(40, 167, 69, 0.3); }
.tier-match { background: rgba(0, 86, 179, 0.15); color: #9bc5ff; border-color: rgba(0, 86, 179, 0.3); }
.tier-reach { background: rgba(255, 193, 7, 0.15); color: #ffe68a; border-color: rgba(255, 193, 7, 0.3); }
.tier-far-reach { background: rgba(220, 53, 69, 0.15); color: #f596a0; border-color: rgba(220, 53, 69, 0.3); }
</style>""")

with open(path2, "w", encoding="utf-8") as f:
    f.write(c2)
    
print("Updated CSS classes")
