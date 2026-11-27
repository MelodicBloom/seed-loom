"""Test the interrupted-evidence gate without launching a browser."""

import contextlib
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import verify_textile_evidence_failure as gate


class InterruptedEvidenceTests(unittest.TestCase):
    def run_gate(self, *, returncode=1, fresh_count=1, **receipt_overrides):
        receipt = {
            "status": "failed-or-incomplete",
            "diagnostic_only": True,
            "completed_check_count": 3,
            "expected_check_count": 17,
            "error": "RuntimeError: Controlled interruption for verifier negative test",
            **receipt_overrides,
        }

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            evidence = root / "artifacts/textile-visual"

            def write_receipt(run, contents):
                path = evidence / run / "evidence.json"
                path.parent.mkdir(parents=True)
                path.write_text(json.dumps(contents))

            write_receipt("prior-run", receipt)

            def child_run(command, *, env, capture_output, text, timeout):
                self.assertEqual(command, [sys.executable, str(root / "scripts/verify_textile_visual.py")])
                self.assertEqual(env["TEXTILE_TEST_INJECT_FAILURE"], "1")
                self.assertTrue(capture_output and text)
                self.assertLess(timeout, 120)
                for index in range(fresh_count):
                    write_receipt(f"fresh-run-{index}", receipt)
                return subprocess.CompletedProcess(command, returncode, "", "")

            with (
                patch.object(gate, "ROOT", root),
                patch.object(gate.subprocess, "run", side_effect=child_run),
                patch.dict(os.environ, {"TEXTILE_TEST_INJECT_FAILURE": "0"}),
                contextlib.redirect_stdout(io.StringIO()),
            ):
                return gate.main()

    def test_accepts_one_fresh_diagnostic_receipt_from_failed_child(self):
        self.assertEqual(self.run_gate(), 0)

    def test_rejects_successful_child_or_wrong_number_of_fresh_receipts(self):
        for outcome in ({"returncode": 0}, {"fresh_count": 0}, {"fresh_count": 2}):
            with self.subTest(outcome=outcome):
                with self.assertRaisesRegex(ValueError, "exactly one fresh receipt"):
                    self.run_gate(**outcome)

    def test_rejects_complete_or_unrelated_failure_receipts(self):
        for override in (
            {"status": "complete"},
            {"diagnostic_only": False},
            {"completed_check_count": 17},
            {"error": "Chromium could not start"},
        ):
            with self.subTest(override=override):
                with self.assertRaisesRegex(ValueError, "mistaken for a complete pass"):
                    self.run_gate(**override)
