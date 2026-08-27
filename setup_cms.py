import os

workspace = r'c:\Users\Hp\Downloads\topschoolsrankings-new-site-upload-v2'
os.makedirs(os.path.join(workspace, 'api'), exist_ok=True)
os.makedirs(os.path.join(workspace, 'admin'), exist_ok=True)
os.makedirs(os.path.join(workspace, 'cms-articles'), exist_ok=True)

# admin/index.html
with open(os.path.join(workspace, 'admin', 'index.html'), 'w', encoding='utf-8') as f:
    f.write('''<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Admin CMS | Top Schools Rankings</title>
  </head>
  <body>
    <!-- Decap CMS Script -->
    <script src="https://unpkg.com/decap-cms@^3.0.0/dist/decap-cms.js"></script>
  </body>
</html>''')

# admin/config.yml
with open(os.path.join(workspace, 'admin', 'config.yml'), 'w', encoding='utf-8') as f:
    f.write('''backend:
  name: github
  repo: monashwamcalculator-cloud/topschoolsrankings
  branch: master
  base_url: https://topschoolsrankings.com
  auth_endpoint: api/auth

media_folder: "media/new-guides"
public_folder: "/media/new-guides"

collections:
  - name: "articles"
    label: "Articles"
    folder: "cms-articles"
    create: true
    slug: "{{slug}}"
    fields:
      - {label: "Title", name: "title", widget: "string"}
      - {label: "Publish Date", name: "date", widget: "datetime"}
      - {label: "Featured Image", name: "image", widget: "image"}
      - {label: "Category", name: "category", widget: "select", options: ["UK", "Australia", "USA", "Canada", "India"]}
      - {label: "Author Name", name: "author_name", widget: "string", default: "Saahil"}
      - {label: "Author Bio", name: "author_bio", widget: "text", default: ""}
      - {label: "Author Image", name: "author_image", widget: "image", required: false}
      - {label: "Body", name: "body", widget: "markdown"}
''')

# api/auth.js
with open(os.path.join(workspace, 'api', 'auth.js'), 'w', encoding='utf-8') as f:
    f.write('''export default function handler(req, res) {
  const host = req.headers.host;
  const url = new URL('https://github.com/login/oauth/authorize');
  url.searchParams.append('client_id', process.env.OAUTH_CLIENT_ID);
  url.searchParams.append('redirect_uri', `https://${host}/api/callback`);
  url.searchParams.append('scope', 'repo,user');
  res.redirect(url.toString());
}''')

# api/callback.js
with open(os.path.join(workspace, 'api', 'callback.js'), 'w', encoding='utf-8') as f:
    f.write('''export default async function handler(req, res) {
  try {
    const { code } = req.query;
    if (!code) return res.status(400).send('No code provided');

    const tokenRes = await fetch('https://github.com/login/oauth/access_token', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        client_id: process.env.OAUTH_CLIENT_ID,
        client_secret: process.env.OAUTH_CLIENT_SECRET,
        code
      })
    });
    
    const data = await tokenRes.json();
    const token = data.access_token;
    
    if (!token) return res.status(400).send('Failed to get token: ' + JSON.stringify(data));
    
    const script = `
      <script>
        (function() {
          function receiveMessage(e) {
            window.opener.postMessage(
              'authorization:github:success:{"token":"${token}","provider":"github"}',
              e.origin
            )
          }
          window.addEventListener("message", receiveMessage, false)
          window.opener.postMessage("authorizing:github", "*")
        })()
      </script>
    `;
    res.setHeader('Content-Type', 'text/html');
    res.send(script);
  } catch (error) {
    res.status(500).send('Error: ' + error.message);
  }
}''')

print('CMS Frontend and Backend configuration created successfully.')
