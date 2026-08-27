export default async function handler(req, res) {
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
}