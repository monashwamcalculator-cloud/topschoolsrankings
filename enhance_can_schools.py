import os
import urllib.request
from bs4 import BeautifulSoup

def download_images():
    os.makedirs("media/articles", exist_ok=True)
    
    opener = urllib.request.build_opener()
    opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")]
    urllib.request.install_opener(opener)

    images = [
        {
            "filename": "can-hero.jpg",
            "url": "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?auto=format&fit=crop&w=1600&q=80"
        },
        {
            "filename": "can-inline-1.jpg",
            "url": "https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=1200&q=80"
        },
        {
            "filename": "can-inline-2.jpg",
            "url": "https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&w=1200&q=80"
        },
        {
            "filename": "can-inline-3.jpg",
            "url": "https://images.unsplash.com/photo-1427504494785-3a9ca7044f45?auto=format&fit=crop&w=1200&q=80"
        }
    ]

    for item in images:
        filepath = os.path.join("media", "articles", item["filename"])
        url = item["url"]
        print(f"Downloading {item['filename']} from {url}...")
        urllib.request.urlretrieve(url, filepath)
        print(f"Saved {filepath} ({os.path.getsize(filepath)} bytes)")

def update_html():
    target_file = "top-100-high-schools-in-canada/index.html"
    print(f"Reading {target_file}...")
    with open(target_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, "html.parser")

    # 1. Update or inject featured hero image
    featured_fig = soup.find("figure", class_="featured-media")
    if featured_fig:
        img_tag = featured_fig.find("img")
        if img_tag:
            img_tag["src"] = "/media/articles/can-hero.jpg"
            img_tag["alt"] = "Top 100 High Schools in Canada Rankings Guide"
            img_tag["style"] = "width:100%; aspect-ratio:16/9; object-fit:cover; border-radius:12px;"
            img_tag["width"] = "1600"
            img_tag["height"] = "900"
            print("Updated existing featured figure image.")
    else:
        # Inject right after page-header or h1
        page_header = soup.find("header", class_="page-header")
        hero_html = """<figure class="featured-media site-container narrow">
  <img src="/media/articles/can-hero.jpg" alt="Top 100 High Schools in Canada Rankings Guide" width="1600" height="900" loading="eager" decoding="async" style="width:100%; aspect-ratio:16/9; object-fit:cover; border-radius:12px;">
  <figcaption>Editorial feature image for this education research guide.</figcaption>
</figure>"""
        hero_tag = BeautifulSoup(hero_html, "html.parser")
        if page_header:
            page_header.insert_after(hero_tag)
        else:
            h1 = soup.find("h1")
            h1.insert_after(hero_tag)
        print("Injected new featured figure image.")

    # Also update OpenGraph and Twitter meta images if present
    for meta in soup.find_all("meta"):
        if meta.get("property") == "og:image":
            meta["content"] = "https://topschoolsrankings.com/media/articles/can-hero.jpg"
        elif meta.get("name") == "twitter:image":
            meta["content"] = "https://topschoolsrankings.com/media/articles/can-hero.jpg"

    # Also update JSON-LD schema image if present
    for script in soup.find_all("script", type="application/ld+json"):
        if script.string and "top-high-schools-canada.webp" in script.string:
            script.string = script.string.replace(
                "https://topschoolsrankings.com/wp-content/uploads/top-high-schools-canada.webp",
                "https://topschoolsrankings.com/media/articles/can-hero.jpg"
            )
            script.string = script.string.replace(
                "https://topschoolsrankings.com/media/articles/top-high-schools-canada.webp",
                "https://topschoolsrankings.com/media/articles/can-hero.jpg"
            )

    # Remove any previously injected inline images to ensure idempotency
    for existing_img in soup.find_all("img", src=lambda s: s and s in [
        "/media/articles/can-inline-1.jpg",
        "/media/articles/can-inline-2.jpg",
        "/media/articles/can-inline-3.jpg"
    ]):
        existing_img.decompose()

    # 2. Inject Inline Image 1 before Top 5 Editorial Deep Dive section
    h2_top5 = soup.find(lambda t: t.name == "h2" and ("top 5" in t.get_text().lower() or "closer look" in t.get_text().lower()))
    if h2_top5:
        inline_1_html = '<img alt="Students collaborating in modern study space at Canadian high school" class="article-inline-img" decoding="async" height="675" loading="lazy" src="/media/articles/can-inline-1.jpg" style="width:100%; aspect-ratio:16/9; object-fit:cover; border-radius:8px; margin:20px 0;" width="1200"/>'
        inline_1_soup = BeautifulSoup(inline_1_html, "html.parser")
        h2_top5.insert_before(inline_1_soup)
        print(f"Injected Inline Image 1 before: {h2_top5.get_text()[:40]}...")
    else:
        print("Warning: Could not find Top 5 section heading.")

    # 3. Inject Inline Image 2 before the Main Comparison Table
    h2_table = soup.find(lambda t: t.name == "h2" and ("comparison table" in t.get_text().lower() or "full comparison" in t.get_text().lower()))
    if h2_table:
        inline_2_html = '<img alt="Canadian classroom with teacher and engaged secondary school students" class="article-inline-img" decoding="async" height="675" loading="lazy" src="/media/articles/can-inline-2.jpg" style="width:100%; aspect-ratio:16/9; object-fit:cover; border-radius:8px; margin:20px 0;" width="1200"/>'
        inline_2_soup = BeautifulSoup(inline_2_html, "html.parser")
        h2_table.insert_before(inline_2_soup)
        print(f"Injected Inline Image 2 before: {h2_table.get_text()[:40]}...")
    else:
        print("Warning: Could not find Comparison Table section heading.")

    # 4. Inject Inline Image 3 before the FAQ section
    h2_faq = soup.find(lambda t: t.name == "h2" and ("faq" in t.get_text().lower() or "frequently asked" in t.get_text().lower()))
    if h2_faq:
        inline_3_html = '<img alt="Canadian high school students studying together on campus grounds" class="article-inline-img" decoding="async" height="675" loading="lazy" src="/media/articles/can-inline-3.jpg" style="width:100%; aspect-ratio:16/9; object-fit:cover; border-radius:8px; margin:20px 0;" width="1200"/>'
        inline_3_soup = BeautifulSoup(inline_3_html, "html.parser")
        h2_faq.insert_before(inline_3_soup)
        print(f"Injected Inline Image 3 before: {h2_faq.get_text()[:40]}...")
    else:
        print("Warning: Could not find FAQ section heading.")

    with open(target_file, "w", encoding="utf-8", newline="\n") as f:
        f.write(str(soup))
    print(f"Saved changes to {target_file}.")

if __name__ == "__main__":
    download_images()
    update_html()
