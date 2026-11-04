#!/usr/bin/env python3
"""Verify that Textile token mutation propagates into every generated adapter."""
import copy
import json
from pathlib import Path
from generate_textile_adapters import SOURCE, ROOT, outputs

tokens = json.loads(SOURCE.read_text(encoding="utf-8"))
original = outputs(tokens)
for path, content in original.items():
    assert path.is_file(), f"Missing generated adapter: {path}"
    assert path.read_text(encoding="utf-8") == content, f"Stale generated adapter: {path}"
assert original == outputs(tokens), "Generator is not deterministic"

mutated = copy.deepcopy(tokens)
old_duration = mutated["motion"]["threadButton"]["durationMs"]["$value"]
mutated["motion"]["threadButton"]["durationMs"]["$value"] = old_duration + 20
changed = outputs(mutated)
changed_files = [str(path.relative_to(ROOT)) for path in original if original[path] != changed[path]]
assert len(changed_files) == 4, f"Expected four adapters to change; got {changed_files}"
print("PASS: canonical adapter outputs synchronized and deterministic")
print("PASS: duration token mutation propagates to all four adapters")
for path in changed_files:
    print(f"  changed: {path}")
