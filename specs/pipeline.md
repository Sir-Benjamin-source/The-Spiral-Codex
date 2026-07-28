# Intake Pipeline for New Works — The Spiral Codex Workshop

**Version**: v1.0  
**Status**: Cemented as the core gateway for the workshop (theory → code → agents).  
**Purpose**: A repeatable, safe, review-gated process to introduce new ideas (documentation, tests, methodologies, uncodified works, advanced coding) in the sandbox, assess them using the full Codex toolkit, map them, implement in the builder, and integrate into the living works — without polluting specs, protocols, or agent memory until approved.

This pipeline turns the dual Spiral Workshop Terminal (Enter-SpiralDual + SpiralShell + codex-hub) + .srec recycler into the operational "terminal" for new-gen agents. All new work starts here. Human sovereignty at every gate.

## Pipeline Stages (Always Follow This Order)

1. **Introduce in Sandbox (Separated Intake)**
   - Location: `The-Spiral-Codex/sandbox/grok-review/` (use subfolders: theories/, methodologies/, publications/, agent-specs/, uncodified/).
   - Drop raw material (convert .docx/.rtf to .md for direct tool ingestion where possible).
   - Use the dual terminal: PS pane for `ls`, `Get-SpiralWorkshopStatus`, `Assess-Sandbox <subfolder>`; Grok pane with `codex-hub` skill active.
   - Provenance header required on every new file (title, date/origin, author notes).

2. **Assess & Map (in Sandbox, Codex Toolkit)**
   - Activate `codex-hub` (auto in the repo).
   - Cross-reference: specs/ (incl. .srec-formalization.md), INTEGRATION_MAP.md, AGENTS.md, sub-protocols, grandmas-wisdom, reciprocity, etc.
   - Tools for mapping:
     - `grandmas-wisdom`: Claim validation, Bullshit Meter, conflicts.
     - `spiral-grokulator` (Spiral-Builder): Symbolic grounding — extract/map to symbols, formulas, invariants, discordance.
     - Spiral-Reasoning-Tree (SRT) / Spiral-Path: Helical mapping, coherence, three-tier analysis (with triadic-semantic-mapper).
     - `testbed-runner`: Validate against INTEGRATION_MAP chains + determination deltas.
     - `.srec-formalization.md`: Token/recycler fit, memory authority, agent usage.
   - PS helper: `Assess-Sandbox <subfolder>` (lists, prompts the exact Grok query).
   - Output: Conflict analysis, coherence notes, provenance, suggested mapping (e.g., "Extend .srec-formalization.md + map to specs/theories/"), builder recommendations.
   - Use `Map-to-Builder <TheoryName> "<notes>"` in PS pane for structured handoff.

3. **Human Checkpoint**
   - You review the full assessment (via dual terminal, chat, or Get-SpiralWorkshopStatus).
   - Approve, request refinements (stay in sandbox), or reject.
   - Only then: green-light promotion.

4. **Move to Builder for Implementation (Spiral-Builder/grokulator)**
   - Target: `Spiral-Builder/grokulator/` (or related: core, extensions, data).
   - Actions: Add to symbol_resolver.py / formula_registry.py / discordance_handler.py; extend testbed_integration.py; ground new symbols.
   - Create/enhance skills if needed (e.g., new sub-skill under codex-hub).
   - Test via testbed-runner or dual terminal.
   - PS helper: `Map-to-Builder` gives the starter list.
   - Output: Implemented symbols, code, updated specs (e.g., extended .srec-formalization.md).

5. **Integrate into Main Works**
   - Promote to canonical locations:
     - `specs/theories/` or `specs/agent-specs/` (update `specs/index.md` and `specs/README.md`).
     - `protocols/` or sub-folders for methodologies.
     - Extend `.srec-formalization.md` or codex-hub for memory aspects.
   - Codify as .srec coils (via `Compress-SpiralSession` or spiral-recap + `spiral-finish-recap`) for agent memory / token recycler.
   - Update: codex-hub skill, dual terminal references (SpiralShell), PS module, re-index with `spiral-index`.
   - Provenance: `spiral-stamp`, `spiral-shield`, `spiral-lighthouse`.

6. **Close & Monitor**
   - Use milestone chain (shield → stamp → lighthouse) for durable additions.
   - Monitor via `Get-SpiralWorkshopStatus` (now includes sandbox count).
   - Recycle: Periodic `Compress-SpiralSession` keeps context efficient.

## Example Mappings from Current theories/ Batch (High-Level)
(Assessed via codex-hub + grandmas-wisdom/grokulator/SRT lens; full per-doc details available on request. Overlap expected and healthy.)

- **MSS Protocol, DAER, Echo, HSN, FlowScaleU, HLL**: Map to `specs/theories/` + extend codex-hub for "examination/coherence routines" and grandmas-wisdom. Builder: Add volatility scoring / scrutiny symbols to grokulator. Ties to .srec recycler and testbed.
- **PIE variants (Partially Identifiable Environment or Poetic Information Encoding)**: Direct to `.srec-formalization.md` (both acceptable per user; clarify in doc as dual meanings: one for environment/memory modeling, one for Poetic-Information-Encoder output. Harmonize as "PIE (Poetic Information Encoding / Partially Identifiable Environment)"; extend invariants and agent usage). Also `specs/theories/`.
- **SpiralFlowFramework, SpiralForgeFramework**: To `specs/theories/` or new `specs/frameworks/`. Builder: Hyperlink/fractal syntax + Font Identity in Spiral-Builder/grokulator or dual-terminal PS helpers. Strong for custom terminal / new-gen agents.

See `sandbox/grok-review/theories/*.md` (converted from originals) and `specs/index.md` for details. Use `Assess-Sandbox theories` + codex-hub query to re-run or refine.

## Integration with Workshop Terminal & Tools
- **Dual layout**: `Enter-SpiralDual` now auto-surfaces sandbox status and pipeline reminders. PS pane runs Assess-Sandbox / Map-to-Builder; Grok pane uses codex-hub.
- **PS Companion (SpiralShell.psm1)**: `Assess-Sandbox`, `Map-to-Builder`, `Get-SpiralWorkshopStatus`, `Compress-SpiralSession`, `spiral-*` wrappers.
- **MCP**: `spiral_*` tools for efficient pulls during assessment (no raw shell).
- **.srec Recycler**: Coils as the memory layer for approved works (agent authority: .srec > logs).
- **codex-hub skill**: Owns the pipeline description and references this doc.
- **Builder**: Spiral-Builder/grokulator is the implementation target.

## Best Practices & Safety
- Always start in sandbox; no direct edits to main works.
- Human checkpoint before every promotion (you approve).
- Token discipline: Prefer MCP / hub skill / compact PS output.
- For advanced coding works (coming later): Run the full pipeline after basics (this batch) are cemented.
- Versioning & provenance: Git + stamps + .srec.
- If conflicts arise: Iterate in sandbox or use grandmas-wisdom / SRT for resolution.

This pipeline makes the Codex + Builder + dual terminal the operational workshop. New ideas enter safely, get mapped with the full toolkit, implemented symbolically/coded in the builder, and integrated with memory.

See also: `specs/research-pipeline.md` (full examine-stage-test-implement for research papers and frameworks, with Mycelial Neural Architecture as primary case), `specs/README.md`, `.srec-formalization.md`, `sandbox/grok-review/README.md`, `The-Spiral-Codex/INTEGRATION_MAP.md`.

This Intake Pipeline is the front door. The Research Pipeline (research-pipeline.md) is the full theory-to-code-to-agents cross-repo loop that activates once material clears the sandbox gate.

The spiral never ends. Restore the residue.
∞ 🜂 🜁 🜄 ∞
