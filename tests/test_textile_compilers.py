"""Regression tests for the Textile adapters, workshop compiler and validator."""

import contextlib
import copy
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import generate_textile_adapters as adapters
from scripts import generate_textile_workshop as workshop

# Match the verifier's direct-script import path without changing sys.path.
with patch.dict(sys.modules, {"generate_textile_workshop": workshop}):
    from scripts import verify_textile_workshop as verifier


class AdapterTests(unittest.TestCase):
    def setUp(self):
        self.tokens = json.loads(adapters.SOURCE.read_text())

    def test_motion_converts_duration_but_preserves_composite_easing(self):
        motion = self.tokens["motion"]["threadButton"]
        motion["durationMs"]["$value"] = 1250
        easing = [0.1, 0.3, 0.7, 0.9]
        motion["easing"]["$value"] = easing

        exports = {path.name: value for path, value in adapters.outputs(self.tokens).items()}

        self.assertIn("--til-thread-button-duration: 1250ms;", exports["textile.css"])
        self.assertIn("durationMs: 1250", exports["textile.tokens.ts"])
        preset = json.loads(exports["motion.presets.json"])
        self.assertEqual(preset["threadButton"]["transition"], {"duration": 1.25, "ease": easing})
        figma = json.loads(exports["figma.variables.json"])
        variables = figma["collections"]["Textile Interface"]["variables"]
        self.assertEqual(variables["motion/threadButton/durationMs"], 1250)
        self.assertNotIn("motion/threadButton/easing", variables)
        self.assertEqual(figma["compositeTokens"]["motion/threadButton/easing"], easing)

    def test_check_reports_missing_and_stale_exports_without_repairing_them(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with (
                patch.multiple(adapters, ROOT=root, GENERATED=root / "generated"),
                patch.object(sys, "argv", ["generate_textile_adapters.py", "--check"]),
                contextlib.redirect_stdout(io.StringIO()) as stdout,
            ):
                stale = adapters.GENERATED / "textile.css"
                stale.parent.mkdir()
                stale.write_text("stale")
                self.assertEqual(adapters.main(), 1)
                self.assertIn(str(stale.relative_to(root)), stdout.getvalue())
                missing = adapters.GENERATED / "motion.presets.json"
                self.assertIn(str(missing.relative_to(root)), stdout.getvalue())
                self.assertEqual(stale.read_text(), "stale")
                self.assertFalse(missing.exists())


class WorkshopCompilerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = json.loads(workshop.SOURCE.read_text())
        cls.core = json.loads(workshop.CORE.read_text())

    def test_material_options_separate_coverage_modes_and_convert_signed_mm(self):
        surface = copy.deepcopy(self.registry["surfaces"][0])
        surface["pbr"].update(
            alphaCutoff=0.4, displacementScaleMm=2.5, displacementBiasMm=-0.5
        )
        for mode, alpha_test, transparent in (
            ("OPAQUE", 0, False), ("MASK", 0.4, False), ("BLEND", 0, True)
        ):
            with self.subTest(mode=mode):
                surface["pbr"]["alphaMode"] = mode
                recipe = workshop.material_options(surface)
                options = recipe["optionsWithoutTextures"]
                self.assertEqual(recipe["status"], "recipe-not-rendered")
                self.assertEqual(options["alphaTest"], alpha_test)
                self.assertIs(options["transparent"], transparent)
                self.assertAlmostEqual(options["displacementScale"], 0.0025)
                self.assertAlmostEqual(options["displacementBias"], -0.0005)

    def test_standalone_prompt_resolves_cycle_and_shared_source_once(self):
        data = copy.deepcopy(self.registry)
        for group in workshop.GROUPS:
            data[group] = []
        first = {"id": "C01", "name": "First", "componentIds": ["C02", "C03"]}
        second = {"id": "C02", "name": "Second", "componentIds": ["C03", "C01"]}
        third = {"id": "C03", "name": "Third", "sourceIds": ["S00", "S01"]}
        data["components"] = [first, second, third]
        original = copy.deepcopy(data)

        exports = workshop.compile_outputs(data, self.core, standalone=True)
        text = exports[workshop.BASE / "generated/prompts/components.md"]
        payload = json.loads(text.split("```json\n", 1)[1].split("\n```", 1)[0])

        self.assertEqual(payload["promptId"], "P-C01")
        self.assertEqual(payload["resolvedDependencies"], [
            {"id": "C02", "specification": second},
            {"id": "C03", "specification": third},
        ])
        self.assertEqual([source["sourceId"] for source in payload["sources"]], ["S00", "S01"])
        self.assertEqual(data, original)

    def test_prompt_cli_accepts_unprefixed_lowercase_id_and_rejects_unknown_id(self):
        for prompt, expected in (("m14", "P-M14"), ("no-such-prompt", None)):
            with (
                self.subTest(prompt=prompt),
                patch.object(sys, "argv", ["generate_textile_workshop.py", "--prompt", prompt]),
                contextlib.redirect_stdout(io.StringIO()) as stdout,
                contextlib.redirect_stderr(io.StringIO()) as stderr,
            ):
                if expected is None:
                    with self.assertRaises(SystemExit) as exc:
                        workshop.main()
                    self.assertEqual(exc.exception.code, 2)
                    self.assertIn("Unknown prompt ID P-NO-SUCH-PROMPT", stderr.getvalue())
                    self.assertEqual(stdout.getvalue(), "")
                else:
                    self.assertEqual(workshop.main(), 0)
                    payload = json.loads(stdout.getvalue())
                    self.assertEqual(payload["promptId"], expected)
                    self.assertEqual(payload["specification"]["id"], "M14")
                    self.assertTrue(payload["relevantLightPresets"])

    def test_export_cli_rejects_destination_nested_under_canonical_directory(self):
        with (
            patch.object(sys, "argv", [
                "generate_textile_workshop.py", "--export-directory",
                str(workshop.BASE / "generated/prompts"),
            ]),
            contextlib.redirect_stderr(io.StringIO()) as stderr,
            self.assertRaises(SystemExit) as exc,
        ):
            workshop.main()
        self.assertEqual(exc.exception.code, 2)
        self.assertIn("Export outside the canonical workshop directory", stderr.getvalue())


class WorkshopValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = json.loads(workshop.SOURCE.read_text())

    def test_normalized_fields_accept_endpoints_and_reject_non_numeric_or_nonfinite_values(self):
        for value in (0, 1, True, "0.5", float("nan"), float("inf"), -0.001, 1.001):
            with self.subTest(value=value):
                data = copy.deepcopy(self.registry)
                surface = data["surfaces"][0]
                surface["pbr"]["roughness"] = value
                if type(value) is int:
                    self.assertGreater(verifier.validate(data), 0)
                else:
                    with self.assertRaisesRegex(ValueError, rf'{surface["id"]}\.roughness: outside 0\.\.1'):
                        verifier.validate(data)

    def test_validator_rejects_duplicate_records_in_different_categories(self):
        data = copy.deepcopy(self.registry)
        data["components"][0]["id"] = data["surfaces"][0]["id"]
        with self.assertRaisesRegex(ValueError, "duplicate record IDs"):
            verifier.validate(data)

    def test_validator_rejects_sheen_roughness_in_wrong_texture_channel(self):
        data = copy.deepcopy(self.registry)
        data["surfaces"][0]["textureContract"]["requiredMaps"]["sheenRoughness"]["channels"] = "R=roughness"
        with self.assertRaisesRegex(ValueError, "sheen roughness must occupy alpha"):
            verifier.validate(data)
