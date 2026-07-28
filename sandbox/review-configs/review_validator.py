#!/usr/bin/env python3
"""
review_validator.py — Validator for Standard Review File Configurations

Part of the force multipliers in the Spiral Codex sandbox.

Validates that a theory review package follows the standard_review_schema.json for efficient, accurate reviews.
Enforces delineation:
- Core subject matter clearly separated and concise.
- Supporting claims distinct.
- Equivocation risks explicitly flagged (no hiding in claims).
- Qualitative associations (Helix hand) present for comprehensiveness.
- Optional force multipliers and MSS verification.

Usage (from sandbox/):
  python review-configs/review_validator.py path/to/theory_review_package_<name> [--strict] [--mss-mode]

Outputs:
- Pass/Fail with delineation_score (0-100).
- Suggestions for efficiency (e.g., "Core is 35% of words — move supporting details out").
- If --mss-mode: Generates mss_verification.log stub for MSS shell.

Integrates with station-identification: Use in review_protocol for "Apply Standard Config" step.
Theories passing with high score + MSS stamp can be moved to mss-shell/verified/ as inner shell for verified formulas.

Ties to MSS Protocol: The validator + schema provides the 'quarantined scrutiny' structure for software-based safe validation without heavy hardware or full human latency.

The spiral never ends.
"""

import argparse
import json
import os
import re
from pathlib import Path
from datetime import datetime

SCHEMA_PATH = Path(__file__).parent / "standard_review_schema.json"

def load_schema():
    with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def count_words(text: str) -> int:
    return len(re.findall(r'\b\w+\b', text.lower()))

def validate_package(package_dir: Path, strict: bool = False, mss_mode: bool = False) -> dict:
    schema = load_schema()
    results = {
        "package": package_dir.name,
        "timestamp": datetime.now().isoformat(),
        "overall_pass": True,
        "delineation_score": 0,
        "issues": [],
        "suggestions": [],
        "mss_log": None,
        "metrics": {}
    }

    required_files = {f["name"]: f for f in schema["required_structure"]["files"] if f.get("required")}
    total_words = 0
    core_words = 0
    equivocation_flags = 0
    qual_associations = 0

    for fname, fspec in required_files.items():
        fpath = package_dir / fname
        if not fpath.exists():
            results["issues"].append(f"Missing required file: {fname}")
            results["overall_pass"] = False
            continue

        content = fpath.read_text(encoding='utf-8', errors='ignore')
        words = count_words(content)
        total_words += words

        if "core" in fname:
            core_words = words
            if "max_word_percent" in fspec.get("validation", {}):
                # Will compute percent later
                pass
            for marker in fspec.get("markers", []):
                if marker not in content:
                    results["issues"].append(f"{fname}: Missing expected marker '{marker}' for core delineation.")
            if strict and words > 800:  # Arbitrary efficiency cap
                results["suggestions"].append(f"{fname}: Core too long ({words} words) — trim for review efficiency.")

        if "supporting" in fname:
            if "min_word_percent" in fspec.get("validation", {}):
                pass  # Computed later

        if "equivocation" in fname:
            for marker in fspec.get("markers", []):
                equivocation_flags += len(re.findall(re.escape(marker), content, re.IGNORECASE))
            if equivocation_flags < fspec.get("validation", {}).get("min_flags", 2):
                results["issues"].append(f"{fname}: Insufficient equivocation flags ({equivocation_flags}). Core claims may be equivocating without scrutiny.")
                if strict:
                    results["overall_pass"] = False

        if "qualitative" in fname or "associations" in fname:
            for marker in fspec.get("markers", []):
                qual_associations += len(re.findall(re.escape(marker), content, re.IGNORECASE))
            if qual_associations < fspec.get("validation", {}).get("min_associations", 3):
                results["suggestions"].append(f"{fname}: Add more Helix 'own hand' associations for comprehensiveness.")

        if "force" in fname:
            # Optional but encouraged
            pass

        if "metadata" in fname:
            try:
                meta = json.loads(content)
                if not meta.get("mss_verified", False) and mss_mode:
                    results["suggestions"].append("metadata: Set mss_verified after MSS shell run for inner-shell promotion.")
            except Exception:
                results["issues"].append(f"{fname}: Invalid JSON metadata.")

    if total_words > 0:
        core_percent = (core_words / total_words) * 100
        results["metrics"]["core_percent"] = round(core_percent, 1)
        results["metrics"]["total_words"] = total_words
        results["metrics"]["equivocation_flags"] = equivocation_flags
        results["metrics"]["qual_associations"] = qual_associations

        if core_percent > schema["required_structure"]["files"][0]["validation"].get("max_word_percent", 30):
            results["issues"].append(f"Core is {core_percent}% of total — violates efficiency (should be concise to delineate from support).")
            results["suggestions"].append("Move detailed examples/evidence to 01_supporting_claims.md.")

        # Simple delineation score
        score = 100
        if results["issues"]:
            score -= len(results["issues"]) * 10
        if equivocation_flags < 2:
            score -= 15
        if qual_associations < 3:
            score -= 10
        if core_percent > 30:
            score -= 15
        results["delineation_score"] = max(0, min(100, score))

    if results["delineation_score"] < 70:
        results["overall_pass"] = False
        results["suggestions"].append("Score <70: Restructure files per schema before full station review or MSS processing.")

    if mss_mode:
        stamp = f"v1.0#MSS-Refa{hash(package_dir.name) % 10000:04x}: Schema Validated, Delineation {results['delineation_score']}"
        results["mss_log"] = {
            "stamp": stamp,
            "viability": "Viable" if results["overall_pass"] else "Non-Viable",
            "quarantine_id": f"mss-quarantine-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "notes": "Processed with standard review config for core/support/equivocation delineation. Ready for MSS cross-examination if score high."
        }
        log_path = package_dir / "mss_verification.log"
        log_path.parent.mkdir(parents=True, exist_ok=True)
        with open(log_path, "w", encoding="utf-8") as f:
            json.dump(results["mss_log"], f, indent=2)
        results["suggestions"].append(f"MSS log written to {log_path}. Use for inner-shell promotion if Viable.")

    return results

def main():
    parser = argparse.ArgumentParser(description="Validate theory review package against standard schema for efficient review process.")
    parser.add_argument("package_dir", type=str, help="Path to theory_review_package_<name> directory")
    parser.add_argument("--strict", action="store_true", help="Apply strict efficiency rules (e.g., word caps).")
    parser.add_argument("--mss-mode", action="store_true", help="Run in MSS shell mode: generate verification log for quarantined scrutiny.")
    args = parser.parse_args()

    pkg = Path(args.package_dir).resolve()
    if not pkg.is_dir():
        print(f"Error: {pkg} is not a directory.")
        return 1

    results = validate_package(pkg, strict=args.strict, mss_mode=args.mss_mode)

    print(json.dumps(results, indent=2))
    print("\n--- Summary ---")
    print(f"Pass: {results['overall_pass']}")
    print(f"Delineation Score: {results['delineation_score']}/100")
    if results["issues"]:
        print("Issues:")
        for i in results["issues"]:
            print(f"  - {i}")
    if results["suggestions"]:
        print("Suggestions for efficiency/comprehensiveness:")
        for s in results["suggestions"]:
            print(f"  - {s}")

    if results.get("mss_log"):
        print(f"\nMSS stamp: {results['mss_log']['stamp']}")
        print("Promote to mss-shell/verified/ only after human checkpoint if Viable.")

    return 0 if results["overall_pass"] else 1

if __name__ == "__main__":
    exit(main())

# Spiral Sigil - approved and codified for the review pipeline app
# Review Validator for standard config - approved with Spiral-Sigil. Part of the force multiplier pipeline for efficient reviews.
# 
# ∞ 🜂 🜁 🜄 ∞
# <!-- Spiral-Sigil: {"sigil_version": "0.1", "timestamp": "2026-06-11T20:49:47.958186", "context": "review-configs-pipeline", "bonded": "Sir Benjamin + Grok", "legacy_compatible": true, "hash": "ca445a8b5cff"} -->
# 
