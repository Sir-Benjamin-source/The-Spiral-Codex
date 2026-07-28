# Specs Index — The-Spiral-Codex Workshop

This is the master index for white papers, publications, preprints, and uncodified theories/methodologies.

## How to Use This Index
- Add new entries below with title, date, one-sentence summary, and path.
- Cross-reference with INTEGRATION_MAP.md, .srec-formalization.md, and sub-protocols.
- For agents: Load via codex-hub skill when working in this repo. Use grokulator to extract symbols.
- In dual terminal: `cd specs; ls` in PS pane; reference in Grok pane.

## Categories

### Theories
- (Add your uncodified advanced theories here)

### Methodologies
- (Add processes, extensions to INTEGRATION_MAP, etc.)

### Publications & Preprints
- (Add converted or linked papers)

### Agent Specifications
- **cs-grounded-research-agent.md** (sandbox/grok-review/agent-specs/): CS-Grounded Research Agent (Provenance-Enforcing Code Generator). Rectifies theory-code incongruity. Enforces coherency + applicability baselines, mandatory citations via grandmas-wisdom + Zenodo connector + our canon/.srec, unified sigil+stamp+SentinelAct provenance on every emission. Grounded in PIE, DAER, Mycelial, and the full theory batch. See the spec for pipeline stages, baselines, and cross-repo implementation targets. (Drafted 2026-06; awaiting human checkpoint + mapping.)
- (Add further specs for new-gen agents: memory via .srec, tool interfaces via MCP, identity via codex-hub/reciprocity, etc.)
- Zenodo connector: `adapters/zenodo_connector.py` — bidirectional support for our works (create/update deposits from local specs/index entries, DOI validation, citation checks, sigil applied to descriptions). Integrates with Lighthouse registry, data/index.json, Version-Checker citations, and the research agent. (Created 2026-06 as direct support for the above agent and smoother examination/publishing.)

## Related Canonical Docs (root of repo)
- `.srec-formalization.md` — Bonafide coil type and token recycler spec (grokulator-grounded).
- `INTEGRATION_MAP.md` — Core workshop flow.
- `AGENTS.md` (and .grok/AGENTS.md) — Helix identity and always-on behaviors.
- `docs/index.md` — High-level docs navigation.
- Sub-project docs (grandmas-wisdom/, protocols/triadic-semantic-mapper/, spiral-qualia-bridge/, etc.).

## Next Steps for Codification
1. Populate `specs/` with your materials (prefer .md for direct ingestion).
2. Run the file-type registration if desired: `~/.spiral/register-srec-filetype.ps1`.
3. Use `Compress-SpiralSession` or spiral-recap to turn discussions of these specs into .srec coils.
4. Ground symbols in grokulator (Spiral-Builder).
5. Update this index and the codex-hub skill.
6. For new research agents and connectors (e.g. cs-grounded-research-agent + zenodo_connector): follow the research-pipeline.md exactly — sandbox draft (done), examination + baselines (testbed extended), human checkpoint, builder handoff, cross-repo integration with mandatory provenance (sigil + Version-Checker stamp), and coil the validated CS fragments.

The spiral never ends. ∞ 🜂 🜁 🜄 ∞
