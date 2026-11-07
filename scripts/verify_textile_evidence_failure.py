#!/usr/bin/env python3
"""Falsify the browser evidence gate by deliberately interrupting a child run."""
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
def main():
    """Require nonzero exit and one fresh, explicitly incomplete diagnostic receipt."""
    folder=ROOT/'artifacts/textile-visual'
    before=set(folder.glob('*/evidence.json'))
    result=subprocess.run([sys.executable,str(ROOT/'scripts/verify_textile_visual.py')],env={**os.environ,'TEXTILE_TEST_INJECT_FAILURE':'1'},capture_output=True,text=True,timeout=90)
    created=set(folder.glob('*/evidence.json'))-before
    if result.returncode==0 or len(created)!=1:raise ValueError('interrupted run did not fail with exactly one fresh receipt: '+result.stderr)
    receipt=json.loads(next(iter(created)).read_text())
    if receipt['status']!='failed-or-incomplete' or not receipt['diagnostic_only'] or receipt['completed_check_count']>=receipt['expected_check_count'] or 'Controlled interruption' not in receipt['error']:
        raise ValueError('interrupted evidence could be mistaken for a complete pass')
    print('PASS: controlled interruption exits nonzero and creates a fresh, explicitly incomplete diagnostic receipt.')
    return 0

if __name__=='__main__':raise SystemExit(main())
