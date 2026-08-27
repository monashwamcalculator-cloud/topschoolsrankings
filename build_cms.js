const fs = require('fs');
const path = require('path');
const marked = require('marked');
const fm = require('front-matter');

const templatePath = path.join(__dirname, 'how-to-choose-a-university-course-uk', 'index.html');
const templateHtml = fs.readFileSync(templatePath, 'utf8');

const cmsDir = path.join(__dirname, 'cms-articles');
if (!fs.existsSync(cmsDir)) {
  fs.mkdirSync(cmsDir);
}

const files = fs.readdirSync(cmsDir);

files.forEach(file => {
  if (file.endsWith('.md')) {
    const slug = file.replace('.md', '');
    const content = fs.readFileSync(path.join(cmsDir, file), 'utf8');
    const parsed = fm(content);
    
    const htmlBody = marked.parse(parsed.body);
    
    let newHtml = templateHtml;
    
    // Replace Title
    newHtml = newHtml.replace(/<title>.*?<\/title>/, `<title>${parsed.attributes.title} | Top Schools Rankings</title>`);
    newHtml = newHtml.replace(/<h1 class="hero-title">.*?<\/h1>/s, `<h1 class="hero-title">${parsed.attributes.title}</h1>`);
    
    // Replace featured image
    if (parsed.attributes.image) {
      newHtml = newHtml.replace(/<div class="article-featured-image">\s*<img src="[^"]+"/s, `<div class="article-featured-image">\n          <img src="${parsed.attributes.image}"`);
    }
    
    // Replace body content
    const articleBodyRegex = /(<article class="article-body">)([\s\S]*?)(<div class="answer-box">)/;
    newHtml = newHtml.replace(articleBodyRegex, `$1\n<div class="rich-article-content">\n${htmlBody}\n</div>\n$3`);
    
    // Replace author bio box
    if (parsed.attributes.author_name) {
      // Find author h3 and p
      const authorRegex = /(<div class="author-info">\s*<h3>)[^<]*(<\/h3>\s*<p>)[^<]*(<\/p>)/;
      newHtml = newHtml.replace(authorRegex, `$1${parsed.attributes.author_name}$2${parsed.attributes.author_bio || ''}$3`);
      
      if (parsed.attributes.author_image) {
        const authorImgRegex = /(<div class="author-bio-box">\s*<img src=")[^"]+(")/;
        newHtml = newHtml.replace(authorImgRegex, `$1${parsed.attributes.author_image}$2`);
      }
    }
    
    // Create directory and save HTML
    const outDir = path.join(__dirname, slug);
    if (!fs.existsSync(outDir)) {
        fs.mkdirSync(outDir);
    }
    fs.writeFileSync(path.join(outDir, 'index.html'), newHtml, 'utf8');
    console.log(`Built HTML for article: ${slug}`);
  }
});

// To truly implement CMS, we'd also need to update blogs/index.html to append the new cards.
// But for now, we leave blogs/index.html alone or they can add it via CMS (we would need to script the blogs insertion too).
