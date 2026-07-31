# Spiral Studio — Foundation Spec (Internal)

**Status:** v0.1 internal — usable foundation  
**Provenance:** Spiral Codex  
**Date:** 2026-07-31  
**Purpose:** Flexible foundation for articulating and presenting lightweight interactive surfaces (HTML + optional CSS + optional JS). Built first for internal Spiral use; later extractable as a public skill.

---

## Core Intent

Spiral Studio is the methodology and light plumbing that lets an agent:

1. Decide when a temporary interactive surface is useful.
2. Articulate clean, scoped HTML (with optional CSS and JS).
3. Present that surface through whatever hosting/preview path is available.
4. Keep minimal continuity so the surface can be recalled or refined later in the work.

The agent remains the primary interface. Surfaces are instruments, not replacements for conversation.

---

## Design Principles

- **Flexibility first** — support single-file HTML or small coherent bundles (HTML + CSS + JS).
- **Editability** — prefer structures the agent can fully reason about and revise.
- **Scoped** — each surface is tightly bound to the current need.
- **Presentation-agnostic** — define a minimal contract; adapt to the host environment.
- **Provenance-light** — carry simple continuity notes without heavy ceremony.
- **Internal first** — mature the foundation inside our repos before packaging a saleable skill.

---

## Priority Sequence

1. **Assess** — Does this task benefit from an interactive surface?
2. **Articulate** — Generate clean HTML; add CSS/JS only as needed.
3. **Bundle** — Single-file preferred, or small coherent set.
4. **Present** — Hand to best available presentation path.
5. **Record lightly** — Optional studio entry / coil note.
6. **Release** — Return control to the conversation.

---

## File Conventions

```
studio/
└── <short-slug>-<YYYYMMDD>/
    ├── index.html          # required
    ├── style.css           # optional
    ├── script.js           # optional
    └── studio-entry.md     # optional light continuity note
```

Single-file mode is equally valid and often preferred.

---

## Presentation Contract (Minimal)

Host agent should support at least one of:

- Session HTML preview, **or**
- Local serve + reachable URL/path, **or**
- File hand-off to an existing preview mechanism

Optional reference: Spiral-Forge `api/mock_server.py` pattern for a minimal local serve helper. Not required.

---

## What Exists (v0.1)

Under `specs/spiral-studio/`:

- **Templates:** simple-form, marker-board, decision-board, quick-ledger, data-table, simple-chart
- **Config:** studio, associations, chains, data-articulation
- **Examples:** usage-new-session.md

See `specs/spiral-studio/README.md` for the live index.

---

## Relation to Existing Spiral Pieces

- **Spiral-Builder / ASCII Compiler** — multi-format emission + provenance habits
- **Spiral-Forge** — human-oversight philosophy; optional local-serve reference only
- **Session-Manager / Continuity Coil / Rivet** — optional continuity notes for surfaces
- **The Spiral Codex** — coordinating home for this foundation

---

## Out of Scope (this foundation)

- Heavy frameworks / large dependency trees
- Long-lived multi-page apps (unless explicitly requested)
- Replacing the conversational interface
- Complex backend services

---

## Next Steps (when resumed)

1. Use the templates in real sessions; refine from friction.
2. Optionally add a minimal local preview helper if host environments need it.
3. Decide implementation home (Builder extension vs. dedicated module).
4. Only after internal use feels solid → extract a public Spiral Studio skill.

---

*Methodologies and formulas stay open to new circumstances.*  
Hold the structural anchors. Articulate cleanly. Release when done.
