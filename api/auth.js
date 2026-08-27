export default function handler(req, res) {
  const host = req.headers.host;
  const url = new URL('https://github.com/login/oauth/authorize');
  url.searchParams.append('client_id', process.env.OAUTH_CLIENT_ID);
  url.searchParams.append('redirect_uri', `https://${host}/api/callback`);
  url.searchParams.append('scope', 'repo,user');
  res.redirect(url.toString());
}