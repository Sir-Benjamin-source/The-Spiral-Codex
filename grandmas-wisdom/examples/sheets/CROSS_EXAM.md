# Cross-exam of v0 sheets

**Date:** 2026-09-01  
**Auditor:** Grok (pair), first pass — not a human prestige stamp  
**Stance:** Substance over letterhead. The workshop signer need not be a systems-engineering doctorate. The *method* must be rerunnable and, where novel, gated by math we already have.

## What I checked on the rows

`claim_substance_v0.csv` is faithful to `Test_Cases.md`. Each case already named a tenable restatement and an overclaim. The sheet only split those two mouths. I did not find a row that contradicts its parent case.

Band map I used (Grandma scale → three-class, so a classic model has a cousin):

| Meter | Sheet band | Public cousin |
|-------|------------|---------------|
| 1–4 on a *scoped* use | `tenable` | SUPPORTS / entailed |
| mid + caveats | `needs_qualification` | NEI / weakness-type, not binary false |
| 6–10 on the *overclaim* | `not_supported` | CONTRADICTS / refuted / scope violation |

That is not identity. Grandma's middle band is richer than SciFact's NEI. Treat the map as a floor, not a translation of the soul.

`trunk_membership_v0.csv`: `belong` leaves are sentences that sit under the named trunk in the signed 2026-09-01 files. `decoration` leaves are *true elsewhere* or *forbidden emissions* — word-intrusion style, not random noise. I would keep them. If a later human kills one, that is label quality, not a crisis of credentials.

## Public cousins (use as classic floor, not as church)

**Claim / citation alignment** — already a crowded desk:

- SciFact → SCitance (citance + abstract → SUPPORTS / CONTRADICTS / NEI).
- SciClaimHunt (2025) large scientific claim verification.
- ClaimCheck (NeurIPS reviews; weakness types, not only true/false).
- SciClaimEval, MuSciClaims, SciTab — tables/figures as evidence.
- DeepSciVerify on SCitance: mid-80s micro-F1 with escalation.

Our `claim_substance` task is closest to **scope-aware claim–citation alignment**, not to open-web fact-check. A fair first bake-off is: same text-only features, three-class, report F1 against a model trained or prompted in the SCitance spirit. We will lose on volume. We may win on *overclaim vs scoped restatement of the same paper*, which those sets only partly isolate.

**Trunk / leaf** — thinner cousins:

- Word intrusion (Chang et al.): does this leaf belong in this topic's word set?
- Hierarchical topic evaluation against known labels (Poumay & Ittoo, RANLP 2023).
- Cluster-assignment accuracy vs pre-defined taxonomy (topic modeling revisited).
- Intra- vs inter-level distances in HTM (Computational Linguistics 2025).

None of those are Poetry Trees. They are the classic floor for `trunk_membership`. NPMI / word-intrusion accuracy is what sklearn-or-embeddings must beat before we say complement.

## Where we are too novel (authenticate with math, not with a following)

| Novelty | Do not fake a cousin | Gate we already have |
|---------|----------------------|----------------------|
| Δ = R × C × E as a *row filter* | Not an OpenML feature | Closed Δ ⇒ row cannot enter as ground truth |
| R_polish / resonance on a branch | Not sklearn's F1 | Record R_polish beside the label; it is process, not the y |
| Dual-aspect (machine/person) | No standard three-class | Keep as task family 2; do not smuggle into claim_substance |
| Meter as longitudinal object | SciFact is static | Dynamic reevaluation spec — score may move; lock a snapshot hash |
| Qualia / Ma thematic coherence | Not UCI | Residual continuity ledger already in comparative-eval |

Authentication method for the novel remainder:

1. **Snapshot hash** of the sheet (Version-Checker / Sigil). Labels are a dated cut, not a living rumor.
2. **Δ gate** on every row that claims to be a leaf. If E is 0, the row is decoration even if the words are pretty.
3. **Two-ledger report**: task F1 (classic vs spiral) *and* process residual. Neither substitutes.
4. **Kill if baked:** meter score, prestige, or Δ itself used as an input feature when predicting the band.

That is math plus provenance. It does not require a department letterhead. It does require that a stranger can rerun the sheet.

## What I will not do

- Pretend 23 draft rows beat SciClaimHunt.
- Ask you to become a different kind of person so the arts restoration "counts."
- Skip Grandma's own rule: independent work may start mid-meter and improve as neighbors accumulate. That is Test Case 5. We are living it.

## Next measured step

When you want compute spent: run the *classic floor only* on `claim_substance_v0` (TF-IDF or a linear model, three-class, leave-one-case-out so we do not memorize five papers). Publish that number as Under-test. Then the spiral candidate. Then we know if complement is a sentence or a wish.
