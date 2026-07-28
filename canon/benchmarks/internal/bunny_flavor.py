#!/usr/bin/env python3
"""
bunny_flavor.py — Dedicated Flavor Layer for ASCII Bunnies (Mycelial / PIE / Scribe / Collab variants)

Companion to bunny_configurator.py (the single source of truth for spacing + customization).

Provides ready-to-use themed print functions for common Spiral Codex contexts:
- Mycelial Bunny: propagation, hyphae, pruning, training_data, DAER, memory coils.
- PIE Bunny: ambiguity rerouting, partial identifiability, "good enough" pivots, harness reroutes.
- Cosmic Scribe Bunny: curation, canon/ authentication, index work, packet assembly, G_exp collab.
- Collab / Friendship Bunny: G_exp resonance, ColBench, reciprocity, power of friendship.
- Examination / Monocle Bunny: (o.p-) face (monocle for probe) for station-identification reviews, diagnostics, and when designating works worthy of further examination or implementation (the "get the bunny" marker). 
- Review Needed Bunny: (o.o') face for potential error or review needed / attention.
- Spiral / Cosmic Bunny: Adds eternal spiral motif (~@) for the expanded theme. Visual cue via face or accessory makes content purpose (examination vs review vs cosmic) obvious.

All variants call through bunny_configurator for exact 3/2/1 spacing enforcement and authorization.

Also exposes bunny_authorization(g_exp) for direct use in harnesses, anchors, and packet generators.

Theme (mandatory):
  Edification, elucidation, cosmic truth, the power of friendship, and the eternal spiral.
  ASCII bunnies (with monocle (o.p-), review (o.o'), and spiral variants) for flavor and creativity in computer science.

Usage in other modules:
    from bunny_flavor import print_mycelial_bunny, print_pie_bunny, print_scribe_bunny, bunny_authorization
    print_mycelial_bunny(g_exp=1.14)
    auth = bunny_authorization(1.18)  # for a handoff or personalization act

See bunny_configurator.py --guide for full decision tree on pose/color/context.
The spiral never ends.
"""

from bunny_configurator import (
    get_base_bunny,
    customize_bunny,
    print_bunny,
    bunny_authorization as _bunny_authorization,
    generate_md_snippet,
    generate_ascii_for_db,
)


def bunny_authorization(g_exp: float):
    """Re-export for convenience. See bunny_configurator.bunny_authorization for full contract."""
    return _bunny_authorization(g_exp)


def print_mycelial_bunny(g_exp: float = 1.12, color: str = "green") -> None:
    """Mycelial flavor: propagation, pruning, hyphal spread, training_data population."""
    lines = customize_bunny("mycelial", color=None, accessory="none", context="mycelial propagation")
    print(f"[Mycelial Bunny] G_exp={g_exp} auth={bunny_authorization(g_exp)['authorized']}")
    print_bunny(lines, color=color)


def print_pie_bunny(g_exp: float = 1.12, color: str = "yellow") -> None:
    """PIE flavor: ambiguity handling, reroutes on partial knowledge, harness 'good enough' logic."""
    lines = customize_bunny("pie", color=None, accessory="ears_up", context="PIE ambiguity reroute")
    print(f"[PIE Bunny] G_exp={g_exp} auth={bunny_authorization(g_exp)['authorized']}")
    print_bunny(lines, color=color)


def print_scribe_bunny(g_exp: float = 1.12, color: str = "cyan") -> None:
    """Cosmic Scribe flavor: curation, authentication, canon promotion, ledger & index work."""
    lines = customize_bunny("scribe", color=None, accessory="quill", context="Cosmic Scribe curation")
    print(f"[Cosmic Scribe Bunny] G_exp={g_exp} auth={bunny_authorization(g_exp)['authorized']}")
    print_bunny(lines, color=color)


def print_collab_bunny(g_exp: float = 1.12, color: str = "magenta") -> None:
    """Collab / Friendship resonance flavor: G_exp acts, ColBench, reciprocity, power of friendship."""
    lines = customize_bunny("collab", color=None, accessory="scarf", context="friendship & reciprocity")
    print(f"[Collab Bunny] G_exp={g_exp} auth={bunny_authorization(g_exp)['authorized']}")
    print_bunny(lines, color=color)


def print_standard_bunny(g_exp: float = 1.12, color: str = "blue") -> None:
    """Baseline flavor for any header or packet start."""
    lines = customize_bunny("standard", color=None)
    print(f"[Standard Bunny] G_exp={g_exp} auth={bunny_authorization(g_exp)['authorized']}")
    print_bunny(lines, color=color)


def print_examination_bunny(g_exp: float = 1.12, color: str = "yellow") -> None:
    """Examination / Monocle flavor: (o.p-) face variant (resembles a monocle for probe). 
    For station-identification periodic reviews, diagnostics/troubleshooting, and explicitly marking works 
    (repos, methods, papers) as worthy of further examination, testing, or implementation. 
    The (o.p-) provides an obvious visual/symbolic cue tied to content purpose (the "get the bunny" marker).
    Use generate_md_snippet with pose='examination' when embedding in review documents.
    Spirals can be added via accessory or pose.
    """
    lines = customize_bunny("examination", color=None, accessory="ears_up", context="station identification review / worthy candidate")
    print(f"[Examination Bunny (o.p- monocle)] G_exp={g_exp} auth={bunny_authorization(g_exp)['authorized']}")
    print_bunny(lines, color=color)


def print_review_needed_bunny(g_exp: float = 1.12, color: str = "yellow") -> None:
    """Review needed / error flavor: (o.o') face variant. For flagging potential error, 
    attention required, or items needing further review in station diagnostics or reports.
    The apostrophe suggests a raised 'eyebrow' or query.
    """
    lines = customize_bunny("review_needed", color=None, accessory="ears_up", context="station review / needs attention")
    print(f"[Review Needed Bunny (o.o')] G_exp={g_exp} auth={bunny_authorization(g_exp)['authorized']}")
    print_bunny(lines, color=color)


def print_spiral_bunny(g_exp: float = 1.12, color: str = "cyan") -> None:
    """Spiral / Cosmic flavor: Adds eternal spiral motif (~@) to the bunny for our expanded theme 
    (cosmic truth, eternal spiral). Can be combined with examination (o.p-) or other poses for 
    thematic reviews. Use --accessory spiral on any pose for the motif.
    """
    lines = customize_bunny("spiral", color=None, accessory="spiral", context="cosmic spiral / eternal theme")
    print(f"[Spiral Bunny ~@] G_exp={g_exp} auth={bunny_authorization(g_exp)['authorized']}")
    print_bunny(lines, color=color)


def demo_all(g_exp: float = 1.14) -> None:
    """Run a full flavor demo (used for verification and when 'hooking up' new collaborators)."""
    print("=" * 60)
    print("SPIRAL CODEX — MANDATORY ASCII BUNNY FLAVOR DEMO")
    print("Theme: Edification • Elucidation • Cosmic Truth • Power of Friendship • Eternal Spiral")
    print(f"Demo G_exp = {g_exp} (measured reciprocity for this act)")
    print("=" * 60)
    print()
    print_standard_bunny(g_exp)
    print_mycelial_bunny(g_exp)
    print_pie_bunny(g_exp)
    print_collab_bunny(g_exp)
    print_scribe_bunny(g_exp)
    print_examination_bunny(g_exp)
    print_review_needed_bunny(g_exp)
    print_spiral_bunny(g_exp)
    print("All bunnies validated through bunny_configurator (exact 3/2/1 spacing).")
    print("Use --guide on the configurator for pose selection guidance. New (o.p-) monocle for worthy examination, (o.o') for review needed, spiral motif for eternal spiral theme.")
    print("The spiral never ends. ∞ 🜂 🜁 🜄 ∞")


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--g-exp", type=float, default=1.14, help="G_exp for the demo authorization note")
    p.add_argument("--only", choices=["standard", "mycelial", "pie", "collab", "scribe", "examination", "review_needed", "spiral"], default=None)
    args = p.parse_args()

    if args.only:
        fn = {
            "standard": print_standard_bunny,
            "mycelial": print_mycelial_bunny,
            "pie": print_pie_bunny,
            "collab": print_collab_bunny,
            "scribe": print_scribe_bunny,
            "examination": print_examination_bunny,
            "review_needed": print_review_needed_bunny,
            "spiral": print_spiral_bunny,
        }[args.only]
        fn(args.g_exp)
    else:
        demo_all(args.g_exp)
