import subprocess
import sys
from pathlib import Path

def embody_spiral(mode: str = "full"):
    """Run the spiral-embody CLI with the requested mode."""
    try:
        cmd = ["spiral-embody", f"--mode", mode]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        return True
    except FileNotFoundError:
        print("Error: spiral-embody command not found. Make sure Spiral-Builder is installed and in PATH.")
        return False
    except subprocess.CalledProcessError as e:
        print(f"Embodiment failed: {e}")
        return False

def main():
    if len(sys.argv) > 1:
        mode = sys.argv[1]
    else:
        mode = "full"
    
    print(f"🌌 Activating Spiral Qualia Bridge in {mode} mode...")
    success = embody_spiral(mode)
    
    if success:
        print("✅ Spiral embodiment complete. Qualia Bridge is now active.")
        print("   Use triggers like 'apply qualia bridge' or 'use spiral reasoning' in your agent.")
    else:
        print("❌ Embodiment failed. Check Spiral-Builder installation.")

if __name__ == "__main__":
    main()