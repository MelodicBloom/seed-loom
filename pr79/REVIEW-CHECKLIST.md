# PR #79 human review packet (ThreadButton, head 8f39e580e461d4ef013249d6688c1e1fa817aa1e)

Prepared 2026-11-22 (America/New_York) by Grok Bot, Group B writer lease.
Nothing here is an acceptance decision; gates 2 and 3 of
initiatives/textile-interface/EVIDENCE-v0.2.md require a named human.

## Folders
- screenshots-post-fix/ : local Chromium (playwright 1.55.0, headless shell 140.0.7339.16), clean clone at 8f39e58; 17/17 checks. Byte-identical across two clean clones.
- screenshots-ci-run-45075532540/ : hosted CI artifact (Signal Validation, pull_request, merge ref 1a6ae08), 17/17, plus the controlled-interruption diagnostic receipt. Hashes differ from local (different fonts/rasteriser), same content.
- screenshots-pre-fix/mobile-committed.png : head 4b56fea, shows the square light-blue tap-highlight overlay the fix removes.

## Local post-fix SHA-256
998e00d8b6d69d972e19564c7a3ff096c3ca5d715149038690769a18701462d2  desktop-committed.png
0f65ffd98bd396ac60333b65b2b6f5a3e8d56f8c735946e7d74f6f26042480ae  desktop-default.png
068e24c8cfe4a72873aed9aaf9cff24391d09a814233e8de28ddaeb9a1b49f7a  desktop-forced-colors.png
a70a504c9192734de2667bcccc27de6fff4d6894fe5af49c9aecfc7da0b02b2c  desktop-keyboard-focus.png
0f65ffd98bd396ac60333b65b2b6f5a3e8d56f8c735946e7d74f6f26042480ae  desktop-reduced-motion.png
e77300a22c67b16bcd62ff7f76aec98197136888b33292c25d0940e6ea93cd74  mobile-committed.png
66f6fecab273ccc6803b4c530bedc482af234cfc08a4190209ed10c10129fbee  mobile-default.png

## CI post-fix SHA-256
fa6062d459c569e6d4c77f5cba78711d6dff85c16e94d4150c21638be5e76ba3  desktop-committed.png
b663a9a441241b4ed3e36f10f0bfa62300d0993a7e0acad7bd52d3adb4a6afd7  desktop-default.png
0bb59e46f5fe7789b3753b29a171177a8b790b3baea3b932b9aaac2691850392  desktop-forced-colors.png
029b5f0bad1711c04c825730863a36c738a17757eea1ab4e77868c16dd69734f  desktop-keyboard-focus.png
b663a9a441241b4ed3e36f10f0bfa62300d0993a7e0acad7bd52d3adb4a6afd7  desktop-reduced-motion.png
e3e8075b47b96b51c0cda8f9c3243574782c137508fc50654a61e1e4a4aa89fa  mobile-committed.png
21231ead00ff5ab9d44b45fc694e99d23c0e34a529ef317f4704b7688009a9a1  mobile-default.png

## Gate 2 – screenshot review (human)
For each of the seven images, confirm and initial:
- [ ] desktop-default: dashed indigo border, "Not committed.", no clipping
- [ ] desktop-committed: solid indigo fill, white text, "Commitment stitched."
- [ ] desktop-keyboard-focus: 3px focus ring visible with offset
- [ ] desktop-reduced-motion: identical to default at rest (expected; same hash)
- [ ] desktop-forced-colors: solid visible border, system colours
- [ ] mobile-default (375px): no horizontal overflow, button >= 48px tall
- [ ] mobile-committed (375px): rounded navy button, white text, NO square light-blue highlight (pixel check: corners (33,301)/(220,301) = page beige, fill (100,325) = (44,62,126))
- [ ] Contrast acceptable for text/button in all states; no unintended clipping
- [ ] No claim beyond implemented states (loading/success/error are future)
Reviewer name / date / verdict: ______________________

## Gate 3 – deployed-route acceptance (human) — CURRENTLY BLOCKED
Finding: Vercel preview for 8f39e58 was "Ignored" by scripts/reproducibility/vercel-ignore-build.mjs (deployable paths are only root config, index.html, src/, packages/svg-filter-atlas/, tokens/). The Vite build has no config and only bundles root index.html, so initiatives/textile-interface/reference/thread-button/index.html is not on any deployed route today (preview URL path returns 404). Providing a route requires a hosting change outside PR #79's scope and a deployment decision by the owner.
Once a route exists:
- [ ] Open the URL in a real browser (desktop + a phone or 375px emulation); record URL, commit SHA, browser/version
- [ ] Generated textile.css loads (no 404 in network panel); dashed indigo default renders
- [ ] Click toggles to committed and back; status text updates; aria-pressed flips; name stays "Stitch commitment"
- [ ] Tab shows focus ring; Enter commits; Space reverses
- [ ] Touch tap on phone: no square tap-highlight flash
- [ ] OS reduced-motion: no transition; forced colours / high contrast: border visible
- [ ] 375px: no horizontal scroll
- [ ] No console errors
Reviewer name / date / URL / verdict: ______________________
