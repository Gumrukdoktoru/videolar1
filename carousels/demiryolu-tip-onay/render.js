// Export each .slide of carousel.html as a 1080x1350 PNG, plus a combined PDF.
const path = require("path");
const fs = require("fs");
const { chromium } = require(require.resolve("playwright", { paths: ["/opt/node22/lib/node_modules"] }));

(async () => {
  const dir = __dirname;
  const out = path.join(dir, "png");
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  await page.goto("file://" + path.join(dir, "carousel.html"));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(300);
  const slides = await page.$$(".slide");
  for (let i = 0; i < slides.length; i++) {
    const f = path.join(out, `demiryolu-tip-onay-${String(i + 1).padStart(2, "0")}.png`);
    await slides[i].screenshot({ path: f });
    console.log(f);
  }
  // PDF: one slide per page
  await page.addStyleTag({ content: "@page{size:1080px 1350px;margin:0} body{background:#F6F4EE} .slide{margin:0 !important; page-break-after:always; break-after:page;}" });
  await page.pdf({ path: path.join(dir, "demiryolu-tip-onay-carousel.pdf"), width: "1080px", height: "1350px", printBackground: true });
  const fontsOk = await page.evaluate(() => [...document.fonts].filter((f) => f.status === "loaded").map((f) => f.family + " " + f.weight));
  console.log("fonts loaded:", [...new Set(fontsOk)].join(", "));
  await browser.close();
})();
