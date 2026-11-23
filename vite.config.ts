import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { defineConfig, type Plugin } from 'vite';

// Publishes the Textile Interface ThreadButton reference at /lab/thread-button/.
// The root entry (index.html) and its bundle are untouched: this plugin only
// emits two extra static assets under dist/lab/thread-button/.
const ROOT = fileURLToPath(new URL('.', import.meta.url));
const REFERENCE = 'initiatives/textile-interface/reference/thread-button/index.html';
const STYLESHEET = 'initiatives/textile-interface/generated/textile.css';
const ROUTE = 'lab/thread-button';
const REWRITES: Array<[string, string]> = [
  ['href="../../generated/textile.css"', `href="/${ROUTE}/textile.css"`],
  [
    'href="../../workshop/README.md"',
    'href="https://github.com/MelodicBloom/seed-loom/blob/main/initiatives/textile-interface/workshop/README.md"'
  ]
];

function labThreadButton(): Plugin {
  return {
    name: 'seed-loom-lab-thread-button',
    apply: 'build',
    generateBundle() {
      let html = readFileSync(ROOT + REFERENCE, 'utf8');
      for (const [from, to] of REWRITES) {
        if (html.split(from).length !== 2) {
          this.error(`${REFERENCE}: expected exactly one occurrence of ${from}`);
        }
        html = html.replace(from, to);
      }
      this.emitFile({ type: 'asset', fileName: `${ROUTE}/index.html`, source: html });
      this.emitFile({ type: 'asset', fileName: `${ROUTE}/textile.css`, source: readFileSync(ROOT + STYLESHEET) });
    }
  };
}

export default defineConfig({ plugins: [labThreadButton()] });
