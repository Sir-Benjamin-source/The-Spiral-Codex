"""test_pipeline.py — hard checks for examination cycle runner."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pipeline.examination_cycle import run_examination_cycle

def test_cycle_produces_packet():
    packet = run_examination_cycle(context="pipeline test", out_dir="/tmp/smurf_cycles")
    assert packet["format"] == "examination_cycle_packet"
    assert "sense" in packet and "differentiate" in packet and "express" in packet
    print("PASS: cycle produces packet")

def test_handshake_valid_under_defaults():
    packet = run_examination_cycle(out_dir="/tmp/smurf_cycles")
    assert packet["differentiate"]["handshake_valid"] is True
    print("PASS: handshake valid under defaults")

if __name__ == "__main__":
    test_cycle_produces_packet()
    test_handshake_valid_under_defaults()
    print("\nAll pipeline tests passed.")
