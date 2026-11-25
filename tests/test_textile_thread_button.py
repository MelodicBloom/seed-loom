"""Chromium fallback for the reference page's native DOM and CSS behavior.

After installing the workshop's Playwright and Chromium dependencies:
python -m unittest discover -s tests -p test_textile_thread_button.py
"""

import os
from pathlib import Path
import unittest

from playwright.sync_api import expect, sync_playwright


REFERENCE = (
    Path(__file__).resolve().parents[1]
    / "initiatives/textile-interface/reference/thread-button/index.html"
)


class ThreadButtonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        playwright = cls.enterClassContext(sync_playwright())
        cls.browser = playwright.chromium.launch(
            executable_path=os.environ.get("TEXTILE_CHROMIUM_EXECUTABLE") or None,
            timeout=10000,
        )
        cls.addClassCleanup(cls.browser.close)

    def open_reference(self, **options):
        context = self.browser.new_context(**options)
        self.addCleanup(context.close)
        context.set_default_timeout(3000)
        page = context.new_page()
        page.goto(REFERENCE.as_uri(), timeout=3000)
        return page, page.get_by_role("button", name="Stitch commitment", exact=True)

    def test_mobile_has_no_tap_overlay_and_can_reverse_a_commitment(self):
        page, button = self.open_reference(
            viewport={"width": 375, "height": 812}, is_mobile=True, has_touch=True,
        )
        status = page.locator("#button-status")
        expect(button).to_have_css("-webkit-tap-highlight-color", "rgba(0, 0, 0, 0)", timeout=3000)
        expect(status).to_have_attribute("aria-live", "polite", timeout=3000)

        for pressed, state, announcement in (
            ("true", "committed", "Commitment stitched."),
            ("false", "loose", "Commitment removed."),
        ):
            with self.subTest(state=state):
                button.tap()
                expect(button).to_have_attribute("aria-pressed", pressed, timeout=3000)
                expect(button).to_have_attribute("data-state", state, timeout=3000)
                expect(status).to_have_text(announcement, timeout=3000)

    def test_reduced_motion_suppresses_press_geometry_even_during_activation(self):
        page, button = self.open_reference(reduced_motion="reduce")
        button.hover()
        page.mouse.down()
        try:
            expect(button).to_have_css("transform", "none", timeout=3000)
            expect(button).to_have_attribute("aria-pressed", "false", timeout=3000)
        finally:
            page.mouse.up()
        expect(button).to_have_attribute("aria-pressed", "true", timeout=3000)
