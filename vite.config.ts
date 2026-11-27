import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { defineConfig, type Plugin } from 'vite';

// Publishes the Textile Interface ThreadButton reference at /lab/thread-button/.
// The root entry (index.html) and its bundle are untouched: this plugin only
// emits the reference and its static dependencies under dist/lab/thread-button/.
const ROOT = fileURLToPath(new URL('.', import.meta.url));
const TEXTILE = 'initiatives/textile-interface';
const REFERENCE_DIR = `${TEXTILE}/reference/thread-button`;
const REFERENCE = `${REFERENCE_DIR}/index.html`;
const ROUTE = 'lab/thread-button';
// These source links also work on preview builds before #79 reaches main.
const REVIEWED_SOURCE = 'https://github.com/MelodicBloom/seed-loom/blob/e753b5a6c434bcbf426673b25e86a954ca7af24d';
const REWRITES: Array<[string, string]> = [
  ['href="../../generated/textile.css"', `href="/${ROUTE}/textile.css"`],
  ['href="./textile-material.css"', `href="/${ROUTE}/textile-material.css"`],
  ['href="../../workshop/README.md"', `href="${REVIEWED_SOURCE}/${TEXTILE}/workshop/README.md"`],
  ['href="./VISUAL-TARGET.md"', `href="${REVIEWED_SOURCE}/${REFERENCE_DIR}/VISUAL-TARGET.md"`]
];
const ASSETS = [
  [`${TEXTILE}/generated/textile.css`, 'textile.css'],
  [`${REFERENCE_DIR}/textile-material.css`, 'textile-material.css'],
  [`${REFERENCE_DIR}/assets/linen-weave.svg`, 'assets/linen-weave.svg'],
  [`${REFERENCE_DIR}/assets/indigo-yarn.svg`, 'assets/indigo-yarn.svg']
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
      for (const [source, destination] of ASSETS) {
        this.emitFile({ type: 'asset', fileName: `${ROUTE}/${destination}`, source: readFileSync(ROOT + source) });
      }
    }
  };
}

export default defineConfig({ plugins: [labThreadButton()] });
