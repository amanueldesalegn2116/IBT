// Accessibility check using axe-core inside jsdom.
// No real browser or Chromium sandbox required -- this is what made the
// pa11y/Puppeteer version unreliable on GitHub-hosted runners.
//
// Checks every top-level *.html file in the repo (skips node_modules).

import { JSDOM } from "jsdom";
import axeCore from "axe-core";
import { readFileSync } from "fs";
import { globSync } from "glob";

const htmlFiles = globSync("*.html", { ignore: ["node_modules/**"] });

if (htmlFiles.length === 0) {
  console.log("No HTML files found at repo root to check.");
  process.exit(0);
}

let hadViolations = false;

for (const file of htmlFiles) {
  const html = readFileSync(file, "utf-8");
  const dom = new JSDOM(html, {
    runScripts: "outside-only",
    resources: "usable",
    url: "http://localhost/"
  });

  const { window } = dom;

  global.window = window;
  global.document = window.document;

  const axeSource = readFileSync(
    new URL("../node_modules/axe-core/axe.min.js", import.meta.url),
    "utf-8"
  );
  window.eval(axeSource);

  const results = await window.axe.run(window.document, {
    runOnly: {
      type: "tag",
      values: ["wcag2a", "wcag2aa"]
    }
  });

  console.log(`\n--- ${file} ---`);

  if (results.violations.length === 0) {
    console.log("✓ No accessibility violations found.");
  } else {
    hadViolations = true;
    for (const violation of results.violations) {
      console.log(`✗ [${violation.impact}] ${violation.id}: ${violation.help}`);
      for (const node of violation.nodes) {
        console.log(`    ${node.target.join(", ")}`);
      }
    }
  }
}

if (hadViolations) {
  console.log("\nAccessibility check FAILED — see violations above.");
  process.exit(1);
} else {
  console.log("\nAll HTML files passed the accessibility check.");
  process.exit(0);
}
