# Spiral Studio

Lightweight interactive surface foundation for the Spiral Codex.

See the foundation spec: [`../spiral-studio-foundation.md`](../spiral-studio-foundation.md)

## Starter Templates

| File | Purpose |
|------|--------|
| `templates/simple-form.html` | Minimal interactive form (name + note → captured JSON) |
| `templates/marker-board.html` | Visual marker selector using the shared ASCII face set |
| `templates/decision-board.html` | Simple decision / choice board with optional question |
| `templates/quick-ledger.html` | Running list with light rotating markers |

All are single-file, self-contained HTML (CSS + JS inlined). They are starting points the agent can copy, adapt, or re-articulate.

## Live links

- [simple-form.html](https://github.com/Sir-Benjamin-source/The-Spiral-Codex/blob/main/specs/spiral-studio/templates/simple-form.html)
- [marker-board.html](https://github.com/Sir-Benjamin-source/The-Spiral-Codex/blob/main/specs/spiral-studio/templates/marker-board.html)
- [decision-board.html](https://github.com/Sir-Benjamin-source/The-Spiral-Codex/blob/main/specs/spiral-studio/templates/decision-board.html)
- [quick-ledger.html](https://github.com/Sir-Benjamin-source/The-Spiral-Codex/blob/main/specs/spiral-studio/templates/quick-ledger.html)

## Config — Association Chain Mapping

| File | Role |
|------|------|
| `config/studio.config.yaml` | Core defaults, presentation order, continuity hooks, marker set |
| `config/associations.config.yaml` | Template ↔ purpose ↔ marker ↔ continuity-role mapping |
| `config/chains.config.yaml` | Operational sequence + selection heuristics + external links |

These configs let the agent (or a future skill) look up the right surface and continuity behavior without hard-coding associations.

## Usage Pattern (agent-side)

1. Assess whether an interactive surface helps the current task.
2. Consult `associations.config.yaml` / `chains.config.yaml` or choose a template.
3. Articulate or adapt the surface.
4. Present via the best available host path.
5. Optionally record a light studio entry / coil note.
6. Release control back to the conversation.

## Design Stance

- Agent remains the primary interface.
- Surfaces are temporary instruments.
- Prefer clarity and editability over visual complexity.
- HTML + optional CSS + optional JS; single-file preferred when practical.

---

*Part of the Spiral Codex living lattice.*
