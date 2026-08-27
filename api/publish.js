export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  const { auth, title, category, author_name, author_bio, content, feature_image, author_image } = req.body;

  // 1. Verify Credentials
  if (!auth || auth.username !== process.env.ADMIN_USER || auth.password !== process.env.ADMIN_PASS) {
    return res.status(401).json({ error: 'Unauthorized: Invalid username or password' });
  }

  try {
    const repo = 'monashwamcalculator-cloud/topschoolsrankings';
    const branch = 'master';
    const token = process.env.GITHUB_TOKEN;

    const slugify = (text) => text.toString().toLowerCase()
      .replace(/\s+/g, '-')           // Replace spaces with -
      .replace(/[^\w\-]+/g, '')       // Remove all non-word chars
      .replace(/\-\-+/g, '-')         // Replace multiple - with single -
      .replace(/^-+/, '')             // Trim - from start of text
      .replace(/-+$/, '');            // Trim - from end of text

    const slug = slugify(title);

    // Helper to upload a file to GitHub
    const uploadToGitHub = async (filePath, fileContent, isBase64 = false) => {
      const url = `https://api.github.com/repos/${repo}/contents/${filePath}`;
      
      // We don't check for existence to keep it fast, assuming new posts have unique slugs.
      // If we needed to update, we'd GET first to get the SHA.
      const body = {
        message: `Admin CMS: Publish ${filePath}`,
        content: isBase64 ? fileContent : Buffer.from(fileContent).toString('base64'),
        branch: branch
      };

      const putRes = await fetch(url, {
        method: 'PUT',
        headers: {
          Authorization: `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
      });

      if (!putRes.ok) {
        const errorText = await putRes.text();
        // If it's a 422, it might mean the file already exists and we didn't provide a SHA.
        // For a simple CMS, we ignore updates for now, or just throw.
        if (putRes.status === 422 && errorText.includes('sha')) {
            throw new Error(`File ${filePath} already exists. Updating existing files requires fetching SHA first (not implemented in simple version). Please use a unique title.`);
        }
        throw new Error(`GitHub Error: ${errorText}`);
      }
    };

    let featureImgPath = '';
    let authorImgPath = '';

    // 2. Upload Featured Image
    if (feature_image) {
      const ext = feature_image.name.split('.').pop() || 'webp';
      featureImgPath = `media/new-guides/${slug}-featured.${ext}`;
      await uploadToGitHub(featureImgPath, feature_image.data, true);
    }

    // 3. Upload Author Image (optional)
    if (author_image) {
      const ext = author_image.name.split('.').pop() || 'webp';
      const authorSlug = slugify(author_name);
      authorImgPath = `media/authors/${authorSlug}.${ext}`;
      try {
        await uploadToGitHub(authorImgPath, author_image.data, true);
      } catch(e) {
        // If author image already exists, it throws 422. We can safely ignore it.
        console.log("Author image might exist:", e.message);
      }
    }

    // 4. Generate Markdown
    const dateStr = new Date().toISOString();
    const markdownContent = `---
title: "${title.replace(/"/g, '\\"')}"
date: ${dateStr}
image: "/${featureImgPath}"
category: "${category}"
author_name: "${author_name.replace(/"/g, '\\"')}"
author_bio: "${author_bio.replace(/"/g, '\\"')}"
author_image: "/${authorImgPath}"
---

${content}
`;

    // 5. Upload Markdown File
    const mdPath = `cms-articles/${slug}.md`;
    await uploadToGitHub(mdPath, markdownContent, false);

    // Done!
    return res.status(200).json({ success: true, slug });

  } catch (err) {
    return res.status(500).json({ error: err.message });
  }
}
