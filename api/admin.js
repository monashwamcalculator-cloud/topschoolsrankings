export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { action, password, slug, title, desc, content, image } = req.body;

  // Verify Password
  if (!password || password !== process.env.ADMIN_PASSWORD) {
    return res.status(401).json({ error: 'Unauthorized: Invalid password' });
  }

  const GITHUB_TOKEN = process.env.GITHUB_TOKEN;
  if (!GITHUB_TOKEN) {
    return res.status(500).json({ error: 'Server misconfiguration: GITHUB_TOKEN is missing.' });
  }

  const REPO = 'monashwamcalculator-cloud/topschoolsrankings';
  const BRANCH = 'master';

  async function ghAPI(endpoint, method = 'GET', body = null) {
    const opts = {
      method,
      headers: {
        'Authorization': `Bearer ${GITHUB_TOKEN}`,
        'Accept': 'application/vnd.github.v3+json',
        'Content-Type': 'application/json'
      }
    };
    if (body) opts.body = JSON.stringify(body);
    const response = await fetch(`https://api.github.com/repos/${REPO}/${endpoint}`, opts);
    if (!response.ok) {
      const err = await response.text();
      throw new Error(`GitHub API Error (${response.status}): ${err}`);
    }
    return response.json();
  }

  async function getFileContent(path) {
    try {
      const data = await ghAPI(`contents/${path}?ref=${BRANCH}`);
      return Buffer.from(data.content, 'base64').toString('utf-8');
    } catch (e) {
      if (e.message.includes('404')) return null;
      throw e;
    }
  }

  try {
    if (action === 'create') {
      if (!slug || !title || !content) return res.status(400).json({ error: 'Missing required fields' });

      // 1. Get current commit and tree
      const refData = await ghAPI(`git/ref/heads/${BRANCH}`);
      const latestCommitSha = refData.object.sha;
      const commitData = await ghAPI(`git/commits/${latestCommitSha}`);
      const baseTreeSha = commitData.tree.sha;

      // 2. Prepare new article HTML
      const dateStr = new Date().toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' });
      const articleHtml = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${title} | Top Schools Rankings</title>
  <meta name="description" content="${desc || title}">
  <link rel="stylesheet" href="/styles.css">
</head>
<body>
  <header class="site-header"><div class="site-container header-inner">
    <a class="brand" href="/" aria-label="Top Schools Rankings home" style="display:flex; align-items:center;">
      <img src="/assets/logo.png" alt="Top Schools Rankings" style="height:60px; width:auto; max-width:100%;">
    </a>
    <nav class="desktop-nav" aria-label="Primary navigation"><a href="/blogs/">Guides</a><a href="/listings/">Listings</a><a href="/compare/">Compare</a><a href="/tools/">Tools</a><a href="/ranking-methodology/">Methodology</a></nav>
  </div></header>
  <main>
    <nav class="breadcrumbs site-container" aria-label="Breadcrumb"><a href="/">Home</a><span><i aria-hidden="true">/</i><a href="/blogs/">Guides</a></span><span><i aria-hidden="true">/</i><b>${title}</b></span></nav>
    <header class="page-header"><div class="site-container narrow"><span class="eyebrow">Education research guide</span>
      <h1>${title}</h1>
      <div class="page-meta">
        <a href="/author/saahil/" class="author-link"><img src="/assets/saahil.jpg" alt="Saahil" class="author-avatar" loading="lazy"><span>By Saahil</span></a>
        <span>Published ${dateStr}</span>
      </div>
    </div></header>
    ${image ? `<figure class="featured-media site-container narrow"><img src="${image}" alt="${title}"></figure>` : ''}
    <section class="section site-container article-layout">
      <article class="article-body">
        <div class="rich-article-content">
          ${content}
        </div>
        
        <div class="author-bio-box" style="margin-top: 40px; margin-bottom: 40px; padding: 20px; background: #f8f9fa; border-radius: 8px; display: flex; align-items: center; gap: 20px; border: 1px solid #e2e8f0; clear: both;">
          <img src="/assets/saahil.jpg" alt="Saahil" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover;">
          <div>
            <h3 style="margin: 0 0 5px 0; font-size: 18px;"><a href="/author/saahil/" style="color: #1a202c; text-decoration: none;">Saahil</a></h3>
            <p style="margin: 0; font-size: 14px; color: #4a5568; line-height: 1.5;">Saahil is an education researcher and content creator specializing in university rankings, admissions strategies, and student tools. He is dedicated to helping students make informed academic decisions.</p>
          </div>
        </div>
      </article>
    </section>
  </main>
</body>
</html>`;

      // 3. Update blogs/index.html
      let blogsHtml = await getFileContent('blogs/index.html');
      if (blogsHtml) {
        const insertToken = '<div class="listings-grid">';
        const cardHtml = `\n      <article class="listing-card">
        ${image ? `<a class="listing-card-image" href="/${slug}/"><img src="${image}" alt="${title}" loading="lazy"></a>` : ''}
        <div class="card-meta"><span>Editorial guide</span><span>\u2022 Just updated</span></div>
        <h3><a href="/${slug}/">${title}</a></h3>
        <p>${desc || ''}</p>
        <div class="card-footer"><a class="text-link" href="/${slug}/">Read the guide <span>\u2020'</span></a></div>
      </article>`;
        blogsHtml = blogsHtml.replace(insertToken, insertToken + cardHtml);
      }

      // 4. Update sitemap.xml
      let sitemapXml = await getFileContent('sitemap.xml');
      if (sitemapXml) {
        const today = new Date().toISOString().split('T')[0];
        const sitemapEntry = `\n  <url>\n    <loc>https://topschoolsrankings.com/${slug}/</loc>\n    <lastmod>${today}</lastmod>\n  </url>`;
        sitemapXml = sitemapXml.replace('</urlset>', `${sitemapEntry}\n</urlset>`);
      }

      // 5. Create new tree
      const treeItems = [
        { path: `${slug}/index.html`, mode: '100644', type: 'blob', content: articleHtml }
      ];
      if (blogsHtml) treeItems.push({ path: 'blogs/index.html', mode: '100644', type: 'blob', content: blogsHtml });
      if (sitemapXml) treeItems.push({ path: 'sitemap.xml', mode: '100644', type: 'blob', content: sitemapXml });

      const newTreeData = await ghAPI('git/trees', 'POST', {
        base_tree: baseTreeSha,
        tree: treeItems
      });

      // 6. Create Commit
      const newCommitData = await ghAPI('git/commits', 'POST', {
        message: `Admin Panel: Created article ${slug}`,
        tree: newTreeData.sha,
        parents: [latestCommitSha]
      });

      // 7. Update Ref
      await ghAPI(`git/refs/heads/${BRANCH}`, 'PATCH', {
        sha: newCommitData.sha
      });

      return res.status(200).json({ success: true, message: 'Article created successfully!', slug });
    }

    if (action === 'delete') {
      if (!slug) return res.status(400).json({ error: 'Missing slug for deletion' });

      const refData = await ghAPI(`git/ref/heads/${BRANCH}`);
      const latestCommitSha = refData.object.sha;
      const commitData = await ghAPI(`git/commits/${latestCommitSha}`);
      const baseTreeSha = commitData.tree.sha;

      // To delete a folder via trees API, you simply specify sha: null and the mode 040000 (tree).
      // Actually, wait, it's easier to just pass the file with sha: null
      const treeItems = [
        { path: `${slug}/index.html`, mode: '100644', type: 'blob', sha: null }
      ];

      // Remove from blogs/index.html
      let blogsHtml = await getFileContent('blogs/index.html');
      if (blogsHtml) {
        // Simple string manipulation to remove the block (might be fragile, but works for automated cards)
        // Alternatively, let the user manually remove cards for now.
        // Let's use regex to remove the card if possible.
        const regex = new RegExp(`\\s*<article class="listing-card">\\s*(?:<a class="listing-card-image" href="/${slug}/">.*?</a>\\s*)?<div class="card-meta">.*?</div>\\s*<h3><a href="/${slug}/">.*?</a></h3>\\s*<p>.*?</p>\\s*<div class="card-footer"><a class="text-link" href="/${slug}/">.*?</a></div>\\s*</article>`, 'g');
        blogsHtml = blogsHtml.replace(regex, '');
        treeItems.push({ path: 'blogs/index.html', mode: '100644', type: 'blob', content: blogsHtml });
      }

      // Remove from sitemap.xml
      let sitemapXml = await getFileContent('sitemap.xml');
      if (sitemapXml) {
        const regex = new RegExp(`\\s*<url>\\s*<loc>https://topschoolsrankings\\.com/${slug}/</loc>\\s*<lastmod>.*?</lastmod>\\s*</url>`, 'g');
        sitemapXml = sitemapXml.replace(regex, '');
        treeItems.push({ path: 'sitemap.xml', mode: '100644', type: 'blob', content: sitemapXml });
      }

      const newTreeData = await ghAPI('git/trees', 'POST', {
        base_tree: baseTreeSha,
        tree: treeItems
      });

      const newCommitData = await ghAPI('git/commits', 'POST', {
        message: `Admin Panel: Deleted article ${slug}`,
        tree: newTreeData.sha,
        parents: [latestCommitSha]
      });

      await ghAPI(`git/refs/heads/${BRANCH}`, 'PATCH', {
        sha: newCommitData.sha
      });

      return res.status(200).json({ success: true, message: 'Article deleted successfully!' });
    }

    return res.status(400).json({ error: 'Invalid action' });

  } catch (err) {
    console.error(err);
    return res.status(500).json({ error: 'Internal Server Error', details: err.message });
  }
}
