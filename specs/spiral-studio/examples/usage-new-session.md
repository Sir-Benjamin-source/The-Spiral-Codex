# Spiral Studio — Usage Examples (New Sessions)

Short patterns an agent can follow when Studio is available.

---

## 1. Quick status pick

**User:** “Mark this coil as notable.”

**Agent path:**
1. Assess → surface helps (visual marker choice).
2. Select template `marker-board` (see `associations.config.yaml`).
3. Present marker-board.html.
4. User clicks `(o.p)`.
5. Record light studio entry / continuity note if desired.
6. Release.

---

## 2. Capture a decision

**User:** “Should we ship the receipt skill as-is?”

**Agent path:**
1. Assess → decision surface helps.
2. Use `decision-board`.
3. Optionally pre-fill the question field via a small edit, or leave blank for the user.
4. User chooses Yes / No / Defer / Needs more info.
5. Record the choice; continue conversation with that residue.

---

## 3. Show tabular data

**User:** “Here are this month’s receipt totals — can you show them cleanly?”

**Agent path:**
1. Assess → data surface helps.
2. Consult `data-articulation.config.yaml` → prefer `data-table`, optionally `simple-chart`.
3. Inject rows into `data-table.html` (or re-articulate with the real numbers).
4. Present table; offer chart if category + numeric shape fits.
5. Optional: also emit CSV for spreadsheet hand-off.

---

## 4. Running list while working

**User:** “Keep a scratch list of open items for this session.”

**Agent path:**
1. Use `quick-ledger`.
2. User adds/removes items; markers rotate lightly.
3. At session boundary, optionally summarize the ledger into a continuity note.

---

## 5. Form capture

**User:** “I need to jot a name and a short note.”

**Agent path:**
1. Use `simple-form`.
2. User submits → agent reads the captured JSON from the surface result (or user pastes it).
3. Continue with that structured input.

---

## 6. Spreadsheet-shaped data

**User:** Drops CSV or describes columns.

**Agent path:**
1. Parse to row objects.
2. Map fields via `data-articulation.config.yaml` field_roles.
3. Present `data-table` by default.
4. If one category column + one numeric column and ≤ ~12 categories → also offer `simple-chart`.
5. Offer CSV download / copy if useful.

---

## Config quick reference

| Need | Look at |
|------|--------|
| Which template for a purpose | `config/associations.config.yaml` |
| Operational steps | `config/chains.config.yaml` |
| Tables / charts / CSV | `config/data-articulation.config.yaml` |
| Defaults & presentation order | `config/studio.config.yaml` |

---

*Keep surfaces scoped. Return to conversation when the instrument has done its job.*
