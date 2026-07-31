# Spiral Studio

Lightweight interactive surface foundation for the Spiral Codex.

See the foundation spec: [`../spiral-studio-foundation.md`](../spiral-studio-foundation.md)

## Starter Templates

| File | Purpose |
|------|--------|
| `templates/simple-form.html` | Minimal interactive form (name + note → captured JSON) |
| `templates/marker-board.html` | Visual marker selector using the shared ASCII face set |
| `templates/decision-board.html` | Simple decision / choice board with optional question |

All are single-file, self-contained HTML (CSS + JS inlined). They are meant as starting points the agent can copy, adapt, or re-articulate.

## Live links

- [simple-form.html](https://github.com/Sir-Benjamin-source/The-Spiral-Codex/blob/main/specs/spiral-studio/templates/simple-form.html)
- [marker-board.html](https://github.com/Sir-Benjamin-source/The-Spiral-Codex/blob/main/specs/spiral-studio/templates/marker-board.html)
- [decision-board.html](https://github.com/Sir-Benjamin-source/The-Spiral-Codex/blob/main/specs/spiral-studio/templates/decision-board.html)

## Usage Pattern (agent-side)

1. Assess whether an interactive surface helps the current task.
2. Start from a template or articulate a new surface.
3. Present via the best available host path (session preview, local serve, or file hand-off).
4. Optionally record a light studio entry for continuity.
5. Release control back to the conversation.

## Design Stance

- Agent remains the primary interface.
- Surfaces are temporary instruments.
- Prefer clarity and editability over visual complexity.
- HTML + optional CSS + optional JS; single-file preferred when practical.

---

*Part of the Spiral Codex living lattice.*
