"""Run from the repository root: python -m unittest discover -s tests -p test_textile_contract.py."""

import copy
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from subprocess import CompletedProcess
from unittest.mock import patch

from scripts import generate_textile_adapters as adapters
from scripts import generate_textile_workshop as workshop
from scripts import verify_textile_evidence_failure as evidence

# The verifier imports its sibling as a top-level module when run as a script.
with patch.dict(sys.modules, {"generate_textile_workshop": workshop}):
    from scripts import verify_textile_workshop as verifier


class AdapterTests(unittest.TestCase):
    def test_exports_preserve_platform_units_and_composite_easing(self):
        tokens = json.loads(adapters.SOURCE.read_text())
        tokens["motion"]["threadButton"]["durationMs"]["$value"] = 375
        easing = [0.25, 0, 0.75, 1]
        tokens["motion"]["threadButton"]["easing"]["$value"] = easing
        original = copy.deepcopy(tokens)

        exports = {path.name: content for path, content in adapters.outputs(tokens).items()}

        self.assertIn("--til-thread-button-duration: 375ms;", exports["textile.css"])
        self.assertIn("cubic-bezier(0.25, 0, 0.75, 1)", exports["textile.css"])
        self.assertIn("durationMs: 375", exports["textile.tokens.ts"])
        motion = json.loads(exports["motion.presets.json"])
        self.assertEqual(motion["threadButton"]["transition"], {"duration": 0.375, "ease": easing})
        figma = json.loads(exports["figma.variables.json"])
        scalars = figma["collections"]["Textile Interface"]["variables"]
        self.assertEqual(scalars["motion/threadButton/durationMs"], 375)
        self.assertNotIn("motion/threadButton/easing", scalars)
        self.assertEqual(figma["compositeTokens"]["motion/threadButton/easing"], easing)
        self.assertEqual(tokens, original)

    def test_check_reports_missing_and_stale_exports_without_repairing_them(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            generated = root / "generated"
            with patch.multiple(adapters, ROOT=root, GENERATED=generated), redirect_stdout(io.StringIO()) as report:
                with patch.object(sys, "argv", ["generate_textile_adapters.py"]):
                    self.assertEqual(adapters.main(), 0)
                stale = generated / "textile.css"
                missing = generated / "textile.tokens.ts"
                stale.write_text("stale\n")
                missing.unlink()
                with patch.object(sys, "argv", ["generate_textile_adapters.py", "--check"]):
                    self.assertEqual(adapters.main(), 1)
                diagnostic = report.getvalue().partition("Generated adapters are stale:")[2]
                self.assertIn("textile.css", diagnostic)
                self.assertIn("textile.tokens.ts", diagnostic)
                self.assertEqual(stale.read_text(), "stale\n")
                self.assertFalse(missing.exists())


class WorkshopCompilerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = json.loads(workshop.SOURCE.read_text())
        cls.core = json.loads(workshop.CORE.read_text())

    def test_material_options_distinguish_all_coverage_modes_and_convert_signed_mm(self):
        for mode, alpha_test, transparent, double_sided, side in (
            ("OPAQUE", 0, False, False, "FrontSide"),
            ("MASK", 0.37, False, True, "DoubleSide"),
            ("BLEND", 0, True, True, "DoubleSide"),
        ):
            with self.subTest(mode=mode):
                surface = copy.deepcopy(self.registry["surfaces"][0])
                surface["pbr"].update(
                    alphaMode=mode, alphaCutoff=0.37, opacity=0.61,
                    displacementScaleMm=2.5, displacementBiasMm=-1.25, doubleSided=double_sided,
                )
                material = workshop.material_options(surface)
                options = material["optionsWithoutTextures"]
                self.assertEqual(options["alphaTest"], alpha_test)
                self.assertIs(options["transparent"], transparent)
                self.assertEqual(options["side"], side)
                self.assertEqual(options["opacity"], 0.61)
                self.assertAlmostEqual(options["displacementScale"], 0.0025)
                self.assertAlmostEqual(options["displacementBias"], -0.00125)
                self.assertEqual(material["construction"], surface["construction"])
                self.assertEqual(material["mapContract"], surface["textureContract"])

    def test_standalone_prompt_resolves_transitive_dependencies_once_despite_cycle(self):
        registry = {**self.registry, **{group: [] for group in workshop.GROUPS}}
        sources = self.registry["sources"][:2]
        first_source, second_source = (source["sourceId"] for source in sources)
        registry["sources"] = sources
        subject = {
            "id": "C01", "name": "Subject", "componentIds": ["C02", "C02"],
            "sourceIds": [first_source],
        }
        intermediate = {
            "id": "C02", "name": "Intermediate", "componentIds": ["C03"],
            "sourceIds": [second_source],
        }
        leaf = {
            "id": "C03", "name": "Leaf", "componentIds": ["C01"],
            "sourceIds": [first_source],
        }
        registry["components"] = [subject, intermediate, leaf]
        original_registry = copy.deepcopy(registry)
        original_core = copy.deepcopy(self.core)
        filename = workshop.BASE / "generated/prompts/components.md"

        compact = workshop.compile_outputs(registry, self.core)[filename]
        standalone = workshop.compile_outputs(registry, self.core, standalone=True)[filename]

        def first_payload(document):
            return json.loads(document.split("```json\n", 1)[1].split("\n```", 1)[0])

        self.assertEqual(first_payload(compact)["dependencyIds"], ["C02", "C03"])
        self.assertEqual(first_payload(compact)["sourceIds"], [first_source, second_source])
        payload = first_payload(standalone)
        self.assertEqual(payload["promptId"], "P-C01")
        self.assertEqual(payload["resolvedDependencies"], [
            {"id": "C02", "specification": intermediate},
            {"id": "C03", "specification": leaf},
        ])
        self.assertEqual(payload["sources"], sources)
        bindings = payload["globalContract"]["coreTokenValues"]
        easing_values = [row["value"] for row in bindings
                         if row["path"] == "motion.threadButton.easing.$value[]"]
        self.assertEqual(easing_values, original_core["motion"]["threadButton"]["easing"]["$value"])
        self.assertEqual(registry, original_registry)
        self.assertEqual(self.core, original_core)

    def test_prompt_cli_accepts_lowercase_short_id_and_rejects_unknown_id(self):
        output = io.StringIO()
        with patch.object(sys, "argv", ["generate_textile_workshop.py", "--prompt", "m14"]), redirect_stdout(output):
            self.assertEqual(workshop.main(), 0)
        prompt = json.loads(output.getvalue())
        self.assertEqual(prompt["promptId"], "P-M14")
        self.assertEqual(prompt["specification"], next(
            surface for surface in self.registry["surfaces"] if surface["id"] == "M14"
        ))

        output, error = io.StringIO(), io.StringIO()
        with patch.object(sys, "argv", ["generate_textile_workshop.py", "--prompt", "unknown"]):
            with redirect_stdout(output), redirect_stderr(error), self.assertRaises(SystemExit) as exit_error:
                workshop.main()
        self.assertEqual(exit_error.exception.code, 2)
        self.assertIn("Unknown prompt ID P-UNKNOWN", error.getvalue())
        self.assertEqual(output.getvalue(), "")

    def test_check_rejects_extra_files_and_export_cannot_overwrite_canonical_workshop(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            base = root / "workshop"
            with patch.multiple(workshop, ROOT=root, BASE=base), redirect_stdout(io.StringIO()) as report:
                with patch.object(sys, "argv", ["generate_textile_workshop.py"]):
                    self.assertEqual(workshop.main(), 0)
                extra = base / "generated/prompts/obsolete.md"
                extra.write_text("obsolete\n")
                with patch.object(sys, "argv", ["generate_textile_workshop.py", "--check"]):
                    self.assertEqual(workshop.main(), 1)
                self.assertIn("unexpected or absent generated file set", report.getvalue())
                self.assertEqual(extra.read_text(), "obsolete\n")

                forbidden = base / "standalone"
                with patch.object(sys, "argv", ["generate_textile_workshop.py", "--export-directory", str(forbidden)]):
                    error = io.StringIO()
                    with redirect_stderr(error), self.assertRaises(SystemExit) as exit_error:
                        workshop.main()
                self.assertEqual(exit_error.exception.code, 2)
                self.assertIn("Export outside the canonical workshop directory", error.getvalue())
                self.assertFalse(forbidden.exists())


class WorkshopValidationTests(unittest.TestCase):
    def setUp(self):
        self.registry = json.loads(workshop.SOURCE.read_text())

    def test_normalized_range_accepts_endpoints(self):
        self.registry["surfaces"][0]["pbr"].update(roughness=0, opacity=1)
        self.assertEqual(verifier.validate(self.registry), len(list(workshop.records(self.registry))))

    def test_normalized_range_rejects_nonfinite_values_and_booleans(self):
        for invalid in (float("nan"), float("inf"), -0.01, True):
            with self.subTest(invalid=invalid):
                surface = self.registry["surfaces"][0]
                surface["pbr"]["roughness"] = invalid
                with self.assertRaisesRegex(ValueError, rf"{surface['id']}\.roughness: outside 0\.\.1"):
                    verifier.validate(self.registry)

    def test_rejects_duplicate_ids_and_unknown_sources(self):
        self.registry["components"][0]["id"] = self.registry["surfaces"][0]["id"]
        with self.assertRaisesRegex(ValueError, "duplicate record IDs"):
            verifier.validate(self.registry)
        self.registry = json.loads(workshop.SOURCE.read_text())
        self.registry["components"][0]["sourceIds"] = ["missing-source"]
        with self.assertRaisesRegex(ValueError, "unknown source missing-source"):
            verifier.validate(self.registry)


class InterruptedEvidenceTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.receipts = self.root / "artifacts/textile-visual"
        self.valid = {
            "status": "failed-or-incomplete",
            "diagnostic_only": True,
            "completed_check_count": 3,
            "expected_check_count": 17,
            "error": "RuntimeError: Controlled interruption for verifier negative test",
        }
        self.write_receipt("old", self.valid)

    def write_receipt(self, run_id, content):
        path = self.receipts / run_id / "evidence.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(content))

    def run_control(self, *, returncode=1, fresh=()):
        def run_child(command, *, env, capture_output, text, timeout):
            self.assertEqual(command, [sys.executable, str(self.root / "scripts/verify_textile_visual.py")])
            self.assertEqual(env["TEXTILE_TEST_INJECT_FAILURE"], "1")
            for index, receipt in enumerate(fresh):
                self.write_receipt(f"new-{index}", receipt)
            return CompletedProcess(command, returncode, stdout="", stderr="child diagnostic")

        with patch.object(evidence, "ROOT", self.root), patch.object(evidence.subprocess, "run", side_effect=run_child):
            with redirect_stdout(io.StringIO()):
                return evidence.main()

    def test_accepts_one_fresh_diagnostic_and_ignores_prior_receipt(self):
        self.assertEqual(self.run_control(fresh=[self.valid]), 0)

    def test_rejects_success_without_failure_or_ambiguous_receipt_count(self):
        for returncode, fresh in ((0, [self.valid]), (1, []), (1, [self.valid, self.valid])):
            with self.subTest(returncode=returncode, count=len(fresh)):
                # Each subcase starts with the same prior receipt.
                for path in self.receipts.glob("new-*/evidence.json"):
                    path.unlink()
                with self.assertRaisesRegex(ValueError, "exactly one fresh receipt"):
                    self.run_control(returncode=returncode, fresh=fresh)

    def test_rejects_misleading_receipt_and_unrelated_child_error(self):
        for override in (
            {"status": "complete"},
            {"diagnostic_only": False},
            {"completed_check_count": 17},
            {"error": "Chromium failed to launch"},
        ):
            with self.subTest(override=override):
                with self.assertRaisesRegex(ValueError, "mistaken for a complete pass"):
                    self.run_control(fresh=[{**self.valid, **override}])
                (self.receipts / "new-0/evidence.json").unlink()
