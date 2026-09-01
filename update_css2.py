import os

path1 = "tools/final-grade-calculator/index.html"
with open(path1, "r", encoding="utf-8") as f:
    c = f.read()

c = c.replace("""<style>
.result-success { background: #d4edda; color: #155724; border-color: #c3e6cb; }
.result-warning { background: #fff3cd; color: #856404; border-color: #ffeeba; }
.result-danger { background: #f8d7da; color: #721c24; border-color: #f5c6cb; }
</style>""", """<style>
.result-success { background: rgba(40, 167, 69, 0.15); color: #8de49f; border-color: rgba(40, 167, 69, 0.3); }
.result-warning { background: rgba(255, 193, 7, 0.15); color: #ffe68a; border-color: rgba(255, 193, 7, 0.3); }
.result-danger { background: rgba(220, 53, 69, 0.15); color: #f596a0; border-color: rgba(220, 53, 69, 0.3); }
</style>""")

with open(path1, "w", encoding="utf-8") as f:
    f.write(c)

print("Updated colors to dark theme")
