// Serves designlab_html/ locally and saves full-page screenshots of every page
// at phone (390px) and desktop (1440px) widths into screenshots/.
// Also fails the run if a page scrolls sideways on a phone or logs a console error.
// Used by .github/workflows/deploy.yml; run locally with `node .github/ci/screenshots.mjs`
// after `npm i --no-save playwright && npx playwright install chromium`.

import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { chromium } from 'playwright';

const root = path.resolve('designlab_html');
const out = path.resolve('screenshots');
const pages = ['/', '/architecture/', '/privacy/', '/styleguide/'];
const sizes = { phone: [390, 844], desktop: [1440, 900] };
const types = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.ico': 'image/x-icon', '.woff2': 'font/woff2', '.xml': 'application/xml', '.txt': 'text/plain' };

const server = http.createServer((req, res) => {
  let file = path.join(root, decodeURIComponent(req.url.split('?')[0]));
  if (file.endsWith(path.sep) || fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');
  if (!file.startsWith(root) || !fs.existsSync(file)) { res.writeHead(404); res.end(); return; }
  res.writeHead(200, { 'Content-Type': types[path.extname(file)] || 'application/octet-stream' });
  fs.createReadStream(file).pipe(res);
});
await new Promise((r) => server.listen(4173, r));
fs.mkdirSync(out, { recursive: true });

const browser = await chromium.launch();
const problems = [];
for (const [name, [width, height]] of Object.entries(sizes)) {
  const page = await browser.newPage({ viewport: { width, height } });
  page.on('console', (m) => { if (m.type() === 'error') problems.push(`${name}: console error: ${m.text()}`); });
  for (const p of pages) {
    const res = await page.goto(`http://localhost:4173${p}`, { waitUntil: 'networkidle' });
    if (!res || res.status() !== 200) problems.push(`${name} ${p}: HTTP ${res && res.status()}`);
    const sideways = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth);
    if (sideways) problems.push(`${name} ${p}: page scrolls sideways`);
    const slug = p.replace(/\//g, '_').replace(/^_|_$/g, '') || 'home';
    await page.screenshot({ path: path.join(out, `${slug}-${name}.png`), fullPage: true });
    console.log(`saved ${slug}-${name}.png`);
  }
  await page.close();
}
await browser.close();
server.close();

if (problems.length) {
  console.error('Problems found:\n' + problems.join('\n'));
  process.exit(1);
}
console.log('All pages render cleanly.');
