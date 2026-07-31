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
| `templates/data-table.html` | Sortable, filterable table (spreadsheet-style view) |
| `templates/simple-chart.html` | Pure SVG bar chart (no external libraries) |

All are single-file, self-contained HTML. They are starting points the agent can copy, adapt, or re-articulate.

## Live links

- [simple-form.html](https://github.com/Sir-Benjamin-source/The-Spiral-Codex/blob/main/specs/spiral-studio/templates/simple-form.html)
- [marker-board.html](https://github.com/Sir-Benjamin-source/The-Spiral-Codex/blob/main/specs/spiral-studio/templates/marker-board.html)
- [decision-board.html](https://github.com/Sir-Benjamin-source/The-Spiral-Codex/blob/main/specs/spiral-studio/templates/decision-board.html)
- [quick-ledger.html](https://github.com/Sir-Benjamin-source/The-Spiral-Codex/blob/main/specs/spiral-studio/templates/quick-ledger.html)
- [data-table.html](https://github.com/Sir-Benjamin-source/The-Spiral-Codex/blob/main/specs/spiral-studio/templates/data-table.html)
- [simple-chart.html](https://github.com/Sir-Benjamin-source/The-Spiral-Codex/blob/main/specs/spiral-studio/templates/simple-chart.html)

## Config — Association & Data Chains

| File | Role |
|------|------|
| `config/studio.config.yaml` | Core defaults, presentation order, continuity hooks, marker set |
| `config/associations.config.yaml` | Template ↔ purpose ↔ marker ↔ continuity-role mapping |
| `config/chains.config.yaml` | Operational sequence + selection heuristics + external links |
| `config/data-articulation.config.yaml` | Spreadsheet hooks, table/chart presenters, field-role mapping |

## Examples

| File | Role |
|------|------|
| `examples/usage-new-session.md` | Short agent paths for common new-session uses |

## Usage Pattern (agent-side)

1. Assess whether an interactive surface helps.
2. Consult associations / data-articulation / chains configs as needed.
3. Articulate or adapt the surface (inject real data when relevant).
4. Present via the best available host path.
5. Optionally record a light studio entry / coil note.
6. Release control back to the conversation.

## Design Stance

- Agent remains the primary interface.
- Surfaces are temporary instruments.
- Prefer clarity and editability over visual complexity.
- HTML + optional CSS + optional JS; single-file preferred when practical.
- Charts stay pure SVG by default (no external chart libraries required).

---

*Part of the Spiral Codex living lattice.*
