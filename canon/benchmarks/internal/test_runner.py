#!/usr/bin/env python3
"""
test_runner.py — Unified, Modular Test Runner for Spiral Codex Testing Methods

   /)/)
  (o.o)
 (")("))o

**Theme (mandatory)**: Edification, elucidation, cosmic truth, and the power of friendship.
ASCII bunnies for flavor and creativity in computer science.
Base + variants generated via bunny_configurator.py (and bunny_flavor.py). See --guide there.
G_exp authorization controls richness of personalization in runs/packets.

Workable format for streamlining testing (as requested for elegant, repeatable code).

Integrates:
- benchmark_associator.py (outside-first associations to known methods).
- codified.py (baselines, G_exp, configs, ledger coherency, audits).
- Existing harness logic (via codified assimilation).
- Standard outputs: JSON audits, association dicts, ledger entries, optional MD snippets.

Supported formats/configs (extensible):
- "baseline_only": Quick coherency/applicability (codified coherency_quick or full_baselines).
- "associational": Generate + apply association from benchmark_associator, tie to a work.
- "ledger_compare": Focus on coherency between previous and new (codified ledger_coherency).
- "traditional_contrast": Full + external benchmark contrast (uses our compilations).
- "full_internal": Everything with G_exp, ledger write, summary.
- "agent_playground": Tailored for agent/tool theories (associational + agent benchmarks).

Usage (as Cosmic Scribe or playground routine):
  python test_runner.py --work "Theory Name" --text "..." --config associational --benchmark GAIA --output-dir audits/

This unifies the methods into one .py entrypoint while keeping components modular. Produces consistent, citable artifacts for the corpus.

Run more unique/well-calibrated tests here to inform planning and code elegance.
"""

import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional

# Modular imports (assumes run from internal/ or adjust paths)
try:
    from benchmark_associator import get_predefined_association, associate_benchmark
except ImportError:
    # Fallback for direct run
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from benchmark_associator import get_predefined_association, associate_benchmark

# codified functions (assimilated; import or re-use logic)
# For simplicity in this workable format, we simulate codified run via subprocess or direct (here we define a thin wrapper)
import subprocess
import sys as _sys

def run_codified_test(work_name: str, work_text: str, config: str = "full_baselines", 
                      previous_ledger: Optional[str] = None, output_ledger: Optional[str] = None) -> Dict[str, Any]:
    """Thin wrapper to invoke codified.py and return the audit dict."""
    cmd = [
        _sys.executable, "codified.py",
        "--work", work_name,
        "--text", work_text,
        "--config", config
    ]
    if previous_ledger:
        cmd += ["--previous-ledger", previous_ledger]
    if output_ledger:
        cmd += ["--output-ledger", output_ledger]
    
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=Path(__file__).parent)
    if result.returncode != 0:
        print("Codified stderr:", result.stderr)
        raise RuntimeError(f"codified.py failed: {result.stderr}")
    
    # Parse the final JSON from stdout (assumes the print at end)
    # In practice, codified writes the ledger; we can also load it
    try:
        # Look for the JSON block in output
        stdout = result.stdout
        start = stdout.find('{')
        end = stdout.rfind('}') + 1
        if start != -1 and end > start:
            audit = json.loads(stdout[start:end])
            return audit
    except Exception:
        pass
    
    # Fallback: return summary from output
    return {
        "work": work_name,
        "config": config,
        "stdout_summary": result.stdout[-500:],
        "note": "Full audit written to ledger if --output-ledger provided. See codified output."
    }

def run_test(
    work_name: str,
    work_text: str,
    config: str = "full_internal",
    benchmark: Optional[str] = None,  # for associational
    previous_ledger: Optional[str] = None,
    output_dir: str = ".",
    output_ledger: Optional[str] = None
) -> Dict[str, Any]:
    """
    Unified runner. Returns combined result in standard format.
    Outputs: audit JSON, optional association JSON, ledger (via codified), summary.
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    result: Dict[str, Any] = {
        "runner": "test_runner.py",
        "timestamp": datetime.now().isoformat(),
        "work": work_name,
        "config": config,
        "formats_used": []
    }
    
    # 1. Associational component (if requested or part of config)
    if config in ("associational", "full_internal") and benchmark:
        try:
            assoc = get_predefined_association(benchmark)
            assoc_file = output_dir / f"{benchmark.lower()}_assoc_{timestamp}.json"
            with open(assoc_file, "w") as f:
                json.dump(assoc, f, indent=2)
            result["association"] = assoc
            result["association_file"] = str(assoc_file)
            result["formats_used"].append("association_dict (outside-first)")
        except Exception as e:
            result["association_error"] = str(e)
    
    # 2. Core codified run (baselines, G_exp, ledger, etc.)
    codified_config = {
        "baseline_only": "coherency_quick",
        "associational": "full_baselines",
        "ledger_compare": "ledger_coherency",
        "traditional_contrast": "traditional_contrast",
        "full_internal": "full_baselines",
        "agent_playground": "agent_playground"
    }.get(config, "full_baselines")
    
    ledger_name = output_ledger or str(output_dir / f"{work_name.replace(' ', '_')}_{config}_{timestamp}.json")
    try:
        audit = run_codified_test(work_name, work_text, codified_config, previous_ledger, ledger_name)
        result["codified_audit"] = audit
        result["ledger_file"] = ledger_name
        result["formats_used"].append("codified_audit_json (baselines + G_exp + ledger)")
    except Exception as e:
        result["codified_error"] = str(e)
        audit = {}
    
    # 3. Internal summary / combined format
    summary = {
        "work": work_name,
        "config_run": config,
        "overall_gate": audit.get("overall_gate_passed", "N/A") if 'audit' in locals() else "N/A",
        "g_exp": audit.get("g_exp", {}) if 'audit' in locals() else {},
        "pie_fidelity": audit.get("coherency", {}).get("pie_fidelity", "N/A") if 'audit' in locals() else "N/A",
        "citation_validity": audit.get("applicability", {}).get("citation_validity", "N/A") if 'audit' in locals() else "N/A",
        "notes": "Generated via unified test_runner. More unique tests improve corpus and code elegance.",
        "formats": result["formats_used"]
    }
    summary_file = output_dir / f"test_summary_{work_name.replace(' ', '_')}_{config}_{timestamp}.json"
    with open(summary_file, "w") as f:
        json.dump(summary, f, indent=2)
    result["summary"] = summary
    result["summary_file"] = str(summary_file)
    result["formats_used"].append("test_summary_json (workable internal format)")
    
    # 4. Optional: Simple MD snippet for corpus
    md_snippet = f"""## Test Run: {work_name} ({config})
- Timestamp: {result['timestamp']}
- Overall Gate: {summary['overall_gate']}
- G_exp: {summary['g_exp']}
- Key Metrics: PIE fidelity {summary['pie_fidelity']}, Citation validity {summary['citation_validity']}
- Formats: {', '.join(result['formats_used'])}
- Files: See {summary_file.name} and ledger.
"""
    md_file = output_dir / f"test_report_{work_name.replace(' ', '_')}_{config}_{timestamp}.md"
    with open(md_file, "w") as f:
        f.write(md_snippet)
    result["md_report"] = str(md_file)
    result["formats_used"].append("md_report_snippet (for corpus)")
    
    print(f"\n=== Test Runner Complete for {work_name} ({config}) ===")
    print(f"Overall Gate: {summary['overall_gate']}")
    print(f"Files written to {output_dir}")
    
    # --- Integrated Builder Handoff + DB Export (if gate passed or explicitly requested) ---
    # Communicates authenticated works to Spiral-Builder for codification and custom DB (ASCII-to-xlsx) as final destination.
    # Call handoff after auth (per standard workflow in associational-testing-methodology.md).
    if summary.get("overall_gate", False) or config == "handoff":
        try:
            from builder_handoff import handoff_authenticated_work
            assoc_path = None  # Caller can pass association JSON if available
            handoff_result = handoff_authenticated_work(
                audit_path=str(summary_file),  # or the full audit JSON
                association_path=assoc_path,
                output_dir=str(Path(output_dir) / "handoffs")
            )
            result["handoff"] = handoff_result
            print(f"\nHandoff artifacts: {handoff_result}")
            print("G_exp for this handoff act: measured (logged in Populated_Reciprocity_Ledger for circulation to builder/DB impl).")
        except Exception as e:
            result["handoff_error"] = str(e)
            print(f"Handoff skipped or error: {e} (ensure builder_handoff.py present and audit passed gates).")
    
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Unified Spiral Test Runner")
    parser.add_argument("--work", required=True, help="Name of the work/theory")
    parser.add_argument("--text", required=True, help="Text content of the work")
    parser.add_argument("--config", default="full_internal", 
                        choices=["baseline_only", "associational", "ledger_compare", "traditional_contrast", "full_internal", "agent_playground"],
                        help="Test configuration/format")
    parser.add_argument("--benchmark", default=None, help="Benchmark for associational (e.g. GAIA)")
    parser.add_argument("--previous-ledger", default=None)
    parser.add_argument("--output-dir", default=".", help="Directory for outputs")
    args = parser.parse_args()
    
    result = run_test(
        work_name=args.work,
        work_text=args.text,
        config=args.config,
        benchmark=args.benchmark,
        previous_ledger=args.previous_ledger,
        output_dir=args.output_dir
    )
    
    print("\nFinal combined result (JSON):")
    print(json.dumps({k: v for k, v in result.items() if k not in ["codified_audit"]}, indent=2, default=str))
    print("\nWorkable formats produced: " + ", ".join(result.get("formats_used", [])))
    print("Use these for corpus population and further streamlining.")