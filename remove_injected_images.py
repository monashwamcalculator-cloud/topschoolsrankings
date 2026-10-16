import os
import re
from bs4 import BeautifulSoup

target_files = [
    "top-100-high-schools-in-canada/index.html",
    "top-100-schools-in-australia/index.html"
]

images_to_delete = [
    "media/articles/can-inline-1.jpg",
    "media/articles/can-inline-2.jpg",
    "media/articles/can-inline-3.jpg",
    "media/articles/aus-inline-1.jpg",
    "media/articles/aus-inline-2.jpg",
    "media/articles/aus-inline-3.jpg"
]

for file_path in target_files:
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist, skipping.")
        continue

    print(f"Processing {file_path}...")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")
    
    removed_count = 0
    for img in soup.find_all("img"):
        # Keep hero image inside figure.featured-media intact
        if img.find_parent("figure", class_="featured-media"):
            continue

        src = img.get("src", "")
        style = img.get("style", "")
        classes = img.get("class", [])

        # Check if matching injected inline images or attributes
        if (re.search(r"(can|aus)-inline-\d+\.jpg", src) or 
            "article-inline-img" in classes or 
            ("aspect-ratio:16/9" in style and "media/articles" in src and not src.endswith(".svg"))):
            print(f"Removing inline image: {src}")
            img.decompose()
            removed_count += 1

    with open(file_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(str(soup))
    print(f"Saved {file_path} after removing {removed_count} inline images.")

# Clean up unused local image files from disk
for img_path in images_to_delete:
    if os.path.exists(img_path):
        os.remove(img_path)
        print(f"Deleted local file {img_path}")

print("Clean-up complete.")
