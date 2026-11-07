#!/usr/bin/env python3
"""Capture reproducible visual/interaction evidence for the Core ThreadButton.

Output is local Chromium evidence. It is not a production-deployment acceptance test.
Run: python scripts/verify_textile_visual.py
"""
import datetime
import hashlib
import json
import os
import re
import sys
import platform
from importlib.metadata import version
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "initiatives" / "textile-interface"
HTML = BASE / "reference" / "thread-button" / "index.html"
CSS = BASE / "generated" / "textile.css"
RUN_ID = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%f')
EVIDENCE = ROOT / "artifacts" / "textile-visual" / RUN_ID
EVIDENCE.mkdir(parents=True, exist_ok=True)
checks = []
EXPECTED_CHECK_COUNT = 17
EXPECTED_CHECK_NAMES = {
    'generated stylesheet is loaded','default button semantics','suite is linked from the Core workflow',
    'normalized force mappings affect CSS','compression and press scale reach active geometry',
    'pointer activation','toggle accessible name remains stable','reversible activation','no page script errors',
    'keyboard visible focus','Enter activates','Space reverses','reduced motion disables transition',
    'forced-colors border stays visible','375px layout does not overflow','touch target >= 48px','touch activation',
}
EXPECTED_SCREENSHOTS = {'desktop-default.png','desktop-committed.png','desktop-keyboard-focus.png','desktop-reduced-motion.png','desktop-forced-colors.png','mobile-default.png','mobile-committed.png'}
TOKENS = json.loads((BASE / 'tokens/textile.tokens.json').read_text())
OBSERVED_ENVIRONMENT = {'python': platform.python_version(), 'playwright': version('playwright'), 'chromiumExecutableOverride': os.environ.get('TEXTILE_CHROMIUM_EXECUTABLE', 'none; Playwright bundled browser'), 'browserVersion': 'not-launched'}

def token(*keys):
    """Read browser expectations from the same canonical source as the CSS."""
    node=TOKENS
    for key in keys:node=node[key]
    return node['$value']

def check(name, condition, observation):
    """Record an actual assertion and stop immediately on failure."""
    if name not in EXPECTED_CHECK_NAMES or any(c['name']==name for c in checks):
        raise ValueError('Unknown or duplicated check '+name)
    checks.append({"name": name, "passed": bool(condition), "observation": observation})
    if not condition:
        raise AssertionError(f"{name}: {observation}")

def screenshot(page, name):
    """Capture this run's page; stale screenshots cannot enter its receipt."""
    page.screenshot(path=str(EVIDENCE / name), full_page=True, animations="disabled")

def verify():
    """Exercise actual source, force mappings and semantic state in Chromium."""
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=os.environ.get('TEXTILE_CHROMIUM_EXECUTABLE') or None)
        OBSERVED_ENVIRONMENT['browserVersion'] = browser.version
        try:
            page = browser.new_page(viewport={"width": 1440, "height": 900})
            errors = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            page.goto(HTML.as_uri())
            button = page.locator(".thread-button")
            values = button.evaluate("""e => ({
              tension: getComputedStyle(document.documentElement).getPropertyValue('--til-thread-button-tension').trim(),
              radius: getComputedStyle(e).borderRadius,
              border: getComputedStyle(e).borderWidth
            })""")
            check("generated stylesheet is loaded", values == {"tension": str(token('force','threadButton','tension')), "radius": str(token('shape','threadButton','radiusPx'))+'px', "border": str(token('shape','threadButton','borderPx'))+'px'}, values)
            check("default button semantics", button.get_attribute("aria-pressed") == "false" and page.get_by_role('button',name='Stitch commitment',exact=True).count()==1, button.get_attribute("aria-pressed"))
            check("suite is linked from the Core workflow", page.locator('.suite-link').get_attribute('href') == '../../workshop/README.md' and (BASE / 'workshop/README.md').is_file(), 'Core reference -> workshop suite')
            if os.environ.get('TEXTILE_TEST_INJECT_FAILURE') == '1':
                raise RuntimeError('Controlled interruption for verifier negative test')
            screenshot(page, "desktop-default.png")
            effects = button.evaluate("e => ({shadow: getComputedStyle(e).boxShadow, duration: getComputedStyle(e).transitionDuration})")
            shadow_numbers = [float(n) for n in re.findall(r'-?\d+(?:\.\d+)?',effects['shadow'].split(')')[-1])]
            expected_offset=3+2*token('force','threadButton','tension')
            expected_blur=8+4*token('force','threadButton','elasticity')
            expected_seconds=token('motion','threadButton','durationMs')*(.7+.3*token('force','threadButton','recovery'))/1000
            check("normalized force mappings affect CSS", len(shadow_numbers)==4 and abs(shadow_numbers[1]-expected_offset)<.01 and abs(shadow_numbers[2]-expected_blur)<.01 and abs(float(effects['duration'].split(',')[0].rstrip('s')) - expected_seconds) < .001, effects)
            bounds = button.bounding_box()
            page.mouse.move(bounds['x']+bounds['width']/2,bounds['y']+bounds['height']/2)
            page.mouse.down()
            page.wait_for_timeout(220)
            transform = button.evaluate('e => getComputedStyle(e).transform')
            values = [float(n) for n in re.findall(r'-?\d+(?:\.\d+)?', transform)]
            check("compression and press scale reach active geometry", len(values)==6 and abs(values[0]-token('motion','threadButton','pressScale'))<.001 and abs(values[5]-2*token('force','threadButton','compression'))<.01, transform)
            page.mouse.up()
            button.click() # Restore loose after the active-state probe.
            button.click()
            check("pointer activation", button.get_attribute("aria-pressed") == "true" and
                  page.locator("#button-status").inner_text() == "Commitment stitched.",
                  page.locator("#button-status").inner_text())
            check("toggle accessible name remains stable", page.get_by_role('button',name='Stitch commitment',exact=True).count()==1, button.inner_text())
            screenshot(page, "desktop-committed.png")
            button.click()
            check("reversible activation", button.get_attribute("aria-pressed") == "false", button.get_attribute("aria-pressed"))
            check("no page script errors", not errors, errors)
            page.close()

            page = browser.new_page(viewport={"width": 1440, "height": 900})
            page.goto(HTML.as_uri())
            page.keyboard.press("Tab")
            button = page.locator(".thread-button")
            focus = button.evaluate("e => ({active: document.activeElement === e, outline: getComputedStyle(e).outlineWidth})")
            check("keyboard visible focus", focus == {"active": True, "outline": "3px"}, focus)
            screenshot(page, "desktop-keyboard-focus.png")
            page.keyboard.press("Enter")
            check("Enter activates", button.get_attribute("aria-pressed") == "true", button.get_attribute("aria-pressed"))
            page.keyboard.press("Space")
            check("Space reverses", button.get_attribute("aria-pressed") == "false", button.get_attribute("aria-pressed"))
            page.close()

            reduced = browser.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="reduce")
            page = reduced.new_page()
            page.goto(HTML.as_uri())
            duration = page.locator(".thread-button").evaluate("e => getComputedStyle(e).transitionDuration")
            check("reduced motion disables transition", duration == "0s", duration)
            screenshot(page, "desktop-reduced-motion.png")
            reduced.close()

            contrast = browser.new_context(forced_colors="active")
            page = contrast.new_page()
            page.goto(HTML.as_uri())
            border = page.locator(".thread-button").evaluate("e => getComputedStyle(e).borderStyle")
            check("forced-colors border stays visible", border == "solid", border)
            screenshot(page, "desktop-forced-colors.png")
            contrast.close()

            mobile = browser.new_context(viewport={"width": 375, "height": 812}, is_mobile=True, has_touch=True)
            page = mobile.new_page()
            page.goto(HTML.as_uri())
            dimensions = page.evaluate("""() => ({
              viewport: innerWidth,
              document: document.documentElement.scrollWidth,
              buttonWidth: document.querySelector('.thread-button').getBoundingClientRect().width,
              buttonHeight: document.querySelector('.thread-button').getBoundingClientRect().height
            })""")
            check("375px layout does not overflow", dimensions["document"] <= dimensions["viewport"], dimensions)
            check("touch target >= 48px", min(dimensions['buttonWidth'],dimensions['buttonHeight']) >= 48, dimensions)
            screenshot(page, "mobile-default.png")
            page.locator(".thread-button").tap()
            check("touch activation", page.locator(".thread-button").get_attribute("aria-pressed") == "true",
                  page.locator(".thread-button").get_attribute("aria-pressed"))
            screenshot(page, "mobile-committed.png")
            mobile.close()
        finally:
            browser.close()

if __name__ == "__main__":
    error = None
    try:
        for required in (HTML,CSS,BASE/'tokens/textile.tokens.json',BASE/'workshop/registry.json'):
            if not required.is_file():raise FileNotFoundError(str(required))
        verify()
        if len(checks) != EXPECTED_CHECK_COUNT or {c['name'] for c in checks} != EXPECTED_CHECK_NAMES:
            raise RuntimeError(f'Expected {EXPECTED_CHECK_COUNT} checks; received {len(checks)}')
        if {p.name for p in EVIDENCE.glob('*.png')} != EXPECTED_SCREENSHOTS:
            raise RuntimeError('Screenshot set is incomplete or unexpected')
    except Exception as exc:
        error = f'{type(exc).__name__}: {exc}'
    finally:
        sources = {}
        for path in (HTML, CSS, BASE / "tokens" / "textile.tokens.json", BASE / 'workshop/registry.json', Path(__file__)):
            sources[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else 'missing'
        complete = error is None and len(checks) == EXPECTED_CHECK_COUNT and all(c['passed'] for c in checks)
        manifest = {
            "kind": "local browser evidence, not hosted production verification",
            "timestamp_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "github_sha": os.environ.get("GITHUB_SHA", "uncommitted-local-run"),
            "status": 'complete' if complete else 'failed-or-incomplete',
            "diagnostic_only": not complete,
            "error": error,
            "expected_check_count": EXPECTED_CHECK_COUNT,
            "completed_check_count": len(checks),
            "run_id": RUN_ID,
            "environment": OBSERVED_ENVIRONMENT,
            "screenshots_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(EVIDENCE.glob('*.png'))},
            "source_sha256": sources,
            "checks": checks,
            "summary": {"passed": sum(c["passed"] for c in checks), "failed": sum(not c["passed"] for c in checks)},
        }
        (EVIDENCE / "evidence.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        for item in checks:
            print(("PASS" if item["passed"] else "FAIL") + ": " + item["name"])
    if error:print(error,file=sys.stderr)
    raise SystemExit(0 if complete else 1)
