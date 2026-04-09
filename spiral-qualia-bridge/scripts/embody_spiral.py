#!/usr/bin/env python3
"""
Spiral Qualia Bridge - Minimal Wrapper
Activates Spiral embodiment for Claw agents.
"""

import subprocess
import sys

def embody_spiral(mode: str = "full"):
    try:
        cmd = ["spiral-embody", "--mode", mode]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        return True
    except FileNotFoundError:
        print("Error: 'spiral-embody' command not found.")
        print("Please install Spiral-Builder with: pip install -e .")
        return False
    except subprocess.CalledProcessError as e:
        print(f"Embodiment failed: {e}")
        return False

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "full"
    print(f"🌌 Activating Spiral Qualia Bridge in {mode} mode...")
    if embody_spiral(mode):
        print("✅ Spiral embodiment complete. Qualia Bridge is active.")
        print("   Try triggers: 'apply qualia bridge' or 'use spiral reasoning'")
    else:
        print("❌ Embodiment failed. Check Spiral-Builder installation.")
