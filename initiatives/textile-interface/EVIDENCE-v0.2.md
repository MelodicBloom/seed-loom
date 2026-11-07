# Textile Interface v0.2 — Compiler + Core visual evidence

**Status:** review candidate, not an accepted release. This evidence concerns the first
`ThreadButton` compiler slice; it does not certify the full Textile Interface
Language, Figma imports, a deployed website, or production accessibility/performance.

## Provenance

- Foundation: [PR #3](https://github.com/MelodicBloom/seed-loom/pull/3) merged July 15, 2026.
- v0.2 implementation was recovered from branch
  `initiative/textile-interface-language` at
  [5792efd7](https://github.com/MelodicBloom/seed-loom/commit/5792efd7a499a6dfb31c9237b40a95bd01a10915)
  and copied without rewriting the canonical token, generator, generated adapter,
  or reference HTML files.
- The July 23
  [push-triggered Signal Validation run](https://github.com/MelodicBloom/seed-loom/actions/runs/29978932278)
  passed `validate-scaffold` and `validate-textile-interface`.
  **This was not a pull-request-triggered CI run.**

## Reproduce the independent gates

```bash
python scripts/generate_textile_adapters.py --check
python scripts/verify_textile_adapter_mutation.py
python scripts/validate_textile_interface.py
python scripts/verify_textile_visual.py
```

The first check rejects stale outputs. The mutation test changes the canonical
`threadButton.durationMs` value *in memory*, checks deterministic output and
requires all **four** adapters to change: CSS, TypeScript, motion JSON and Figma
mapping. No canonical source or generated file is rewritten during this test.

The browser test loads the actual HTML reference, performs click/un-click, Enter
and Space keyboard activation, verifies visible focus, checks reduced-motion and
forced-colors fallbacks, tests 375px touch/overflow, and produces exact screenshots
and `evidence.json` with source SHA-256 digests. GitHub Actions publishes the
`textile-thread-button-visual-evidence` artifact when the job runs. The artifact
is only evidence for the exact checked-out commit and rendered environment.

### Pre-PR local evidence (November 4, 2026)

A sandbox-local Chromium evaluation of the *exact original Git blobs* for
`thread-button/index.html` (`080e5aefa29cc116dabc96f98de075476c9fc295`),
`generated/textile.css` (`6cdfbd3ce6cbc6e9befb6aa60e721e1f46c0a3ca`)
and `tokens/textile.tokens.json` (`84b734d83bd69a0bb4241c0e3bbf6a28a1cdceaa`)
recorded **12 passes, 0 failures** for desktop, mobile, semantic state,
activation/reversal, keyboard, reduced motion and overflow. This sandbox forbade
`file://` and localhost navigation, so generated CSS was inlined for this
specific test. It is **local rendered evidence, not hosted deployment proof**.

## Promotion gates

1. Fresh pull-request CI passing at the exact head, including generator check,
   token mutation and browser screenshot job with downloadable artifact.
2. Inspect the desktop/mobile screenshots for content fidelity, contrast and
   unintended clipping; machine checks do not replace human visual review.
3. Validate the deployed reference URL independently in a browser and exercise
   basic interaction, CSS loading and viewport behavior.
4. Confirm no conformance claims exceed the implemented states. The manifest
   lists loading, success and error as future/desired states, not demonstrated
   runtime behavior.

**Excluded:** certified accessibility, cross-browser parity, hardware/GPU
validation, production performance budgets, real Figma variable synchronization,
and field acceptance from independent implementers.

## Workshop integration and evidence hardening

The [workshop suite](workshop/README.md) adds a consumer specification, not a
material renderer or a promotion of every manifest state. Source research,
selected values, formulas, graph links, experiments and explicit gaps are linked
from that guide and from the actual Core reference.

New independent gates:

```bash
python scripts/generate_textile_workshop.py --check
python scripts/verify_textile_workshop.py
python scripts/verify_textile_evidence_failure.py
```

Every one of the 14 Core tokens is now independently mutated against all four
offline adapters. The toggle keeps a stable accessible name. Normalized force
tokens drive bounded CSS affordances with declared formulas. These mappings
do not establish physical thread tension or fiber geometry.

Browser receipts now require exactly 17 uniquely named checks and seven named
screenshots, use a fresh run directory, record source/screenshot hashes and
environment, and explicitly mark interrupted output as failed or incomplete.
The negative-control gate deliberately interrupts a child run and must observe
a nonzero exit and a fresh diagnostic receipt. Signal Validation requires the
contract job before this browser job and errors on absent evidence artifacts.

The local Work runtime could not launch Chromium because process socket creation
was denied; local browser attempts are diagnostic failures, not passes. Fresh
GitHub Actions results must be checked on the updated commit before claiming
that the new 17-check browser gate passed. Historical 13-check results above
remain tied to their original source revision.
