# Rounded analysis card

**Date:** 2026-09-01  
**Use:** every analysis routine (Market brief, Grandma pass, eval fold, Price Tree, Reasoning Complex emission).

A routine that only emits a score is flat.  
A routine that only emits a metaphor is also flat.  
Rounded analysis emits **four mouths** or it is not finished.

## The four mouths

1. **Classic floor** — what a plain method already says on the same inputs. Majority class, TF-IDF, OpenML Arm A, WALCL over minutes. If this paragraph is the whole brief, stop.
2. **Cousin map** — which public task this most resembles (SciFact/SCitance three-class; word intrusion; cluster assignment). Name the gap. Do not fake identity.
3. **Math gate** — Δ = R × C × E on each emitted leaf; R_polish or residual on the process. Closed gate ⇒ the leaf does not leave as ground truth.
4. **Substance band** — Grandma: tenable / needs qualification / not supported. Prestige is not a feature.

If a mouth is empty, say empty. Ghost mouths are slurry.

## Public cousins we now treat as floor, not church

**Claims.** SciFact (Wadden et al., 2020): claim + abstract → Supports / Refutes / NoInfo, plus rationale sentences. SCitance (Alvarez et al., 2024) uses citances instead of rewritten claims — closer to how a paper is actually cited. DeepSciVerify reports 86.7 micro-F1 / 81.5 macro-F1 on SCitance with evidence escalation. QMUL-SDS at SCIVER splits the decision: first enough-info vs not, then support vs contradict. That two-step is closer to Grandma than a single softmax.

**Leaves.** Chang et al. 2009 word intrusion: five in-topic words plus one high-probability-elsewhere intruder. Humans find the stranger. Perplexity did **not** track interpretability. Our `decoration` leaves are that task with sentences instead of topic words.

**What those benches do not give us**

- A first-class *scope pair* (same paper, modest claim vs overclaim).
- A longitudinal meter that is allowed to move.
- Dual-aspect (machine fact / person fact).
- Δ as a row filter.

Those we authenticate with our math and dated sheet hashes.

## Default numbers a card must show

| Number | Meaning |
|--------|--------|
| n | Rows actually scored |
| majority acc / F1 | Dumb floor |
| classic acc / macro-F1 / micro-F1 | TF-IDF or Arm A |
| process residual | Continuity ledger; not the y |
| snapshot | Hash or commit of the sheet |

No card may quote a published SCitance F1 as if it were *our* F1.

## Weather rule

n < 50 is weather. Report it. Do not promote it. Under-test stays Under-test.

∞ ǂ ǂ ǂ ∞
