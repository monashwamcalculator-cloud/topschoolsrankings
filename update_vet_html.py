import os

file_path = 'top-ranked-vet-schools-in-us/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace inline 1
content = content.replace(
    '<img alt="Veterinary student examining a dog in a clinic" class="article-inline-img" src="/media/articles/vet-schools-inline-1.jpg" style="width:100%; aspect-ratio:16/9; object-fit:cover; border-radius:8px; margin:24px 0;"/>',
    '<img alt="US Veterinary School Admissions Evaluation Weights (2026)" class="article-inline-img" src="/media/articles/vet-schools-methodology.svg" style="width:100%; aspect-ratio:16/9; border-radius:8px; margin:24px 0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);"/>'
)

# Replace inline 2
content = content.replace(
    '<img alt="Historic university campus building representing top veterinary institutions" class="article-inline-img" src="/media/articles/vet-schools-inline-2.jpg" style="width:100%; aspect-ratio:16/9; object-fit:cover; border-radius:8px; margin:24px 0;"/>',
    '<img alt="Top 5 US Veterinary Colleges Comparison Matrix and NAVLE Pass Rates" class="article-inline-img" src="/media/articles/vet-schools-top5-matrix.svg" style="width:100%; aspect-ratio:16/9; border-radius:8px; margin:24px 0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);"/>'
)

# Replace inline 3
content = content.replace(
    '<img alt="Veterinary laboratory research facility" class="article-inline-img" src="/media/articles/vet-schools-inline-3.jpg" style="width:100%; aspect-ratio:16/9; object-fit:cover; border-radius:8px; margin:24px 0;"/>',
    '<img alt="VMCAS Veterinary Application Lifecycle and Strategic Milestones" class="article-inline-img" src="/media/articles/vet-schools-vmcas-roadmap.svg" style="width:100%; aspect-ratio:16/9; border-radius:8px; margin:24px 0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);"/>'
)

# Replace inline 4
content = content.replace(
    '<img alt="Veterinary student studying clinical medical books" class="article-inline-img" src="/media/articles/vet-schools-inline-4.jpg" style="width:100%; aspect-ratio:16/9; object-fit:cover; border-radius:8px; margin:24px 0;"/>',
    '<img alt="Veterinary Practice Specializations and Financial ROI Benchmarks" class="article-inline-img" src="/media/articles/vet-schools-career-roi.svg" style="width:100%; aspect-ratio:16/9; border-radius:8px; margin:24px 0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);"/>'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html successfully.")

# Remove old JPGs
for i in range(1, 5):
    jpg_path = f"media/articles/vet-schools-inline-{i}.jpg"
    if os.path.exists(jpg_path):
        os.remove(jpg_path)
        print(f"Removed {jpg_path}")
