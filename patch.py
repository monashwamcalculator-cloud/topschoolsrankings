import os

with open("assets/site.js", "r", encoding="utf-8") as f:
    js = f.read()

if "data-custom" not in js:
    js = js.replace("function renderTool(panel) {", "function renderTool(panel) {\n    if (panel.hasAttribute('data-custom')) return;\n")
    with open("assets/site.js", "w", encoding="utf-8") as f:
        f.write(js)
    print("Patched site.js")
