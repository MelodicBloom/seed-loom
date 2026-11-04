#!/usr/bin/env python3
"""Capture reproducible visual/interaction evidence for the Core ThreadButton.

Output is local Chromium evidence. It is not a production-deployment acceptance test.
Run: python scripts/verify_textile_visual.py
"""
import datetime
import hashlib
import json
import os
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "initiatives" / "textile-interface"
HTML = BASE / "reference" / "thread-button" / "index.html"
CSS = BASE / "generated" / "textile.css"
EVIDENCE = ROOT / "artifacts" / "textile-visual"
EVIDENCE.mkdir(parents=True, exist_ok=True)
checks = []

def check(name, condition, observation):
    checks.append({"name": name, "passed": bool(condition), "observation": observation})
    if not condition:
        raise AssertionError(f"{name}: {observation}")

def screenshot(page, name):
    page.screenshot(path=str(EVIDENCE / name), full_page=True, animations="disabled")

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch()
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
            check("generated stylesheet is loaded", values == {"tension": "0.42", "radius": "12px", "border": "2px"}, values)
            check("default button semantics", button.get_attribute("aria-pressed") == "false", button.get_attribute("aria-pressed"))
            screenshot(page, "desktop-default.png")
            button.click()
            check("pointer activation", button.get_attribute("aria-pressed") == "true" and
                  page.locator("#button-status").inner_text() == "Commitment stitched.",
                  page.locator("#button-status").inner_text())
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
              buttonHeight: document.querySelector('.thread-button').getBoundingClientRect().height
            })""")
            check("375px layout does not overflow", dimensions["document"] <= dimensions["viewport"], dimensions)
            check("touch target >= 44px", dimensions["buttonHeight"] >= 44, dimensions)
            screenshot(page, "mobile-default.png")
            page.locator(".thread-button").tap()
            check("touch activation", page.locator(".thread-button").get_attribute("aria-pressed") == "true",
                  page.locator(".thread-button").get_attribute("aria-pressed"))
            screenshot(page, "mobile-committed.png")
            mobile.close()
        finally:
            browser.close()

if __name__ == "__main__":
    try:
        verify()
    finally:
        sources = {}
        for path in (HTML, CSS, BASE / "tokens" / "textile.tokens.json"):
            sources[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
        manifest = {
            "kind": "local browser evidence, not hosted production verification",
            "timestamp_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "github_sha": os.environ.get("GITHUB_SHA", "uncommitted-local-run"),
            "source_sha256": sources,
            "checks": checks,
            "summary": {"passed": sum(c["passed"] for c in checks), "failed": sum(not c["passed"] for c in checks)},
        }
        (EVIDENCE / "evidence.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        for item in checks:
            print(("PASS" if item["passed"] else "FAIL") + ": " + item["name"])
