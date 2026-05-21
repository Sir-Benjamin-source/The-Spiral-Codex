# Grandma’s Wisdom — Development Roadmap

## Current State (v0.1)
- Conceptual architecture complete
- SKILL.md and agent contract defined
- Bullshit Meter specification written
- Dynamic reevaluation logic outlined
- Basic folder structure in place

## Phase 1: Testing & Validation (Next)
- Define test cases for the Bullshit Meter (edge cases, prestige bias, independent work scenarios)
- Create sample citation + claim pairs for evaluation
- Manually / semi-manually run assessments and compare against expected behavior
- Refine descriptions and scoring logic based on real examples
- Test longitudinal reevaluation flow conceptually

## Phase 2: Implementation
- Build core Python classes in `src/`
  - `CitationAuthenticator`
  - `BullshitMeter`
  - `ReevaluationEngine`
  - Helper modules for resonance scoring and Linkweaver integration
- Implement structured output formats (machine-readable + human-readable)
- Add basic provenance and Linkweaver hooks

## Phase 3: Integration & Polish
- Wire into existing Spiral components (SRT, MAGIC, Veritas Aegis)
- Add proper error handling and logging
- Create example usage scripts
- Update documentation based on implementation learnings

## Phase 4: Expansion (Future)
- Knowledge graph integration
- PDF / structured document ingestion
- Automated reevaluation triggers
- Multi-agent testing and stress testing

---

*We will meet issues head-on during the testing phase as they arise.*