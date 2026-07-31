# Spiral Studio — Foundation Spec (Internal)

**Status:** Living draft  
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

1. **Assess**  
   Does this task benefit from an interactive surface, or is conversation still better?

2. **Articulate**  
   Generate clean HTML.  
   Add scoped CSS when visual structure or polish helps.  
   Add JS only when interaction or light state is required.

3. **Bundle**  
   Prefer one of:
   - Single self-contained `.html` (CSS/JS inlined), or
   - Small set: `index.html` + `style.css` + `script.js` when separation is cleaner.

4. **Present**  
   Hand the artifact(s) to the available presentation path (see contract below).

5. **Record lightly**  
   Optional studio log entry: purpose, files produced, session/coil reference.

6. **Release**  
   Return control to the conversation as soon as the user is finished or redirects.

---

## File Conventions

```
studio/
└── <short-slug>-<YYYYMMDD>/     # or session-tied folder
    ├── index.html               # required
    ├── style.css                # optional
    ├── script.js                # optional
    └── studio-entry.md          # optional light continuity note
```

Single-file mode is equally valid and often preferred for simple surfaces.

---

## Presentation Contract (Minimal)

The foundation expects the host agent to be able to do at least one of the following with the produced artifact(s):

- Render / preview interactive HTML inside the session, **or**
- Serve the files locally and provide a reachable URL / file path the user can open, **or**
- Hand the primary HTML file to an existing preview mechanism the agent already controls.

The methodology itself does not hard-code a single runtime. It emits clean artifacts and asks the agent to use the best available presentation path. Environments that already host HTML simply use that path; environments that lack one can fall back to local serve or file hand-off.

**Optional local path:** Spiral-Forge’s lightweight mock-server pattern (`api/mock_server.py`) is a useful reference if we later need a minimal local preview/serve helper. It is not required for the foundation and is not duplicated here.

---

## Relation to Existing Spiral Pieces

- **Spiral-Builder / ASCII Compiler** — reuse multi-format emission + provenance habits. Studio extends the “functional output” role toward interactive surfaces.
- **Spiral-Forge** — shares the philosophy of human oversight and approval checkpoints; its mock-server pattern is an optional presentation reference only. No functional duplication.
- **Spiral-Session-Manager / Continuity Coil** — surfaces can optionally be noted in continuity records so they remain findable across turns.
- **The Spiral Codex** — this foundation lives here as the coordinating spec.

---

## Out of Scope (for this foundation)

- Heavy frameworks or large dependency trees
- Long-lived multi-page applications (unless explicitly requested)
- Replacing the conversational interface
- Complex backend services

---

## Next Internal Steps

1. Keep this spec living and refine as we use it.
2. Grow a small set of practical surface templates.
3. Decide where the first concrete implementation code should live (Builder extension vs. new lightweight module).
4. Only after internal use feels solid, extract a public Spiral Studio skill.

---

*Methodologies and formulas stay open to new circumstances.*  
Hold the structural anchors. Articulate cleanly. Release when done.
