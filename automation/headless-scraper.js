/*
 * headless-scraper.js
 * Purpose:      Extract clean readable text from a web page, including
 *               pages that render content with JavaScript.
 * Requirements: Node.js 18+
 *               npm install playwright
 *               npx playwright install chromium
 * Usage:        node headless-scraper.js https://example.com
 * Be polite:    Check the site's robots.txt and terms first, and do not
 *               send rapid repeated requests.
 */
const { chromium } = require("playwright");

(async () => {
  const url = process.argv[2];
  if (!url) {
    console.error("Usage: node headless-scraper.js <url>");
    process.exit(1);
  }
  const browser = await chromium.launch();
  try {
    const page = await browser.newPage();
    await page.goto(url, { waitUntil: "domcontentloaded", timeout: 30000 });
    const text = await page.evaluate(() => {
      document
        .querySelectorAll("script,style,nav,footer,header,aside,noscript")
        .forEach((el) => el.remove());
      const root = document.querySelector("article, main") || document.body;
      return root.innerText.replace(/\n{3,}/g, "\n\n").trim();
    });
    console.log(text);
  } finally {
    await browser.close();
  }
})();
