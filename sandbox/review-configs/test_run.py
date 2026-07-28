#!/usr/bin/env python3
"""Simple test harness for the new review config and MSS shell (avoids quoting issues in terminal)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

# Test validator
print("=== Testing review_validator on MSS-derived test package ===")
from review_validator import validate_package
pkg = Path(__file__).parent / "test_mss_review_package"
results = validate_package(pkg, strict=True, mss_mode=True)
print(f"Pass: {results['overall_pass']}")
print(f"Delineation Score: {results['delineation_score']}")
print(f"Issues: {len(results['issues'])}")
print(f"Suggestions: {len(results['suggestions'])}")
if results.get('mss_log'):
    print(f"MSS Log generated: {results['mss_log']['stamp']}")

print("\n=== Test complete. Check sandbox/review-configs/test_mss_review_package/mss_verification.log ===")

# Note: Full mss_shell test would require running the mss_shell.py process on the pkg
# (it integrates the validator internally when mss-mode).
print("\nTo test MSS shell: cd to The-Spiral-Codex; python sandbox/mss-shell/mss_shell.py process sandbox/review-configs/test_mss_review_package --config sandbox/mss-shell/mss_config.json")
print("Then check mss-shell/verified/ and logs/ for the inner shell promotion (if viable).")
print("For idle/limited processing: python sandbox/mss-shell/mss_shell.py idle (in separate low-prio terminal).")
