# Daily harvest (not daily release)

**Date:** 2026-09-01  
**Status:** Specified. Not switched on.  
**Depends on:** Rel. campaign + rounded analysis card + Grandma filter + AIS birth.

We will automate **collection**. We will not automate **canon**.

A clock that prints training rows before the pipeline is Verified is a slurry factory with a schedule.

## What "certainty" means here

The testing / authentication pipeline is allowed to *release* a daily set only when **all** of these are true. Until then the cron may only write `inbox/`.

| Gate | Meaning |
|------|--------|
| **Task Verified** | `claim_substance` or `trunk_membership` complement claim is Istest on a locked split (n ≥ 50, paired accuracy reported, majority beaten, no baked meter/prestige). |
| **Two ledgers** | Task metrics *and* process residual both recorded. Neither substitutes. |
| **Snapshot** | Each released cut has a hash / stamp. Labels do not silently drift overnight. |
| **Grandma filter** | No row enters as ground truth if the claim cannot survive a meter pass. |
| **Δ open** | Every leaf-shaped row has Δ = R × C × E above threshold or it is decoration. |
| **Human mark** | A person signs the day's *release*, not every harvested line. Harvest can be machine. Promotion cannot. |
| **Balance** | Overclaim is not the mode. Scope pairs stay paired. |
| **Rights** | Source is ours, public-domain seed, or DOI-backed work we may use. No scrape-of-the-commons. |

Today (2026-09-01): n=10 weather. Majority 0.50 > TF-IDF 0.40. **Certainty is not reached.** Cron stays off for release.

## Two directories, always

```
inbox/YYYY-MM-DD/     candidate rows the machine may write
release/YYYY-MM-DD/   only after human sign + gates
```

`inbox` is cheap. `release` is canon. Mixing them is how datasets rot.

## What the daily job may do (when switched on)

1. Walk signed trees, Test_Cases, Grandma hard-example DB, Codex `data/index.json` DOIs that already have a human mark.
2. Emit **scope pairs** (modest claim / overclaim) or **belong / decoration** swaps. Never a lone overclaim.
3. Attach provenance: path, method, date, Δ if known.
4. Drop meter into a *note* column. Never into a feature column.
5. Write `inbox/` + a harvest log (counts by band, pair completeness, rejected-by-gate).
6. Stop. Do not train. Do not push to comparative-eval. Do not mint.

## What the daily job may not do

- Promote inbox → release.
- Scrape news, novels, or social for "more volume."
- Use yesterday's model score as today's label.
- Quote SCitance F1 as if the harvest were that bench.
- Run if any gate file (`CERTAINTY.md` below) is `closed`.

## CERTAINTY.md (living switch)

A one-line file in this folder:

```
status: closed   # open only when the table above is all true
```

Default: `closed`. Opening it is a human commit, not a cron side effect.

## Cadence once open

- Daily harvest: yes.
- Daily release: no. Release is weekly or when n-new ≥ 20 clean pairs, whichever is slower.
- Retrain of any spiral candidate: only on `release/` cuts, pre-registered.

## First harvest recipe (manual until the switch opens)

Same as now: add scope pairs from the Grandma DB until overclaim is not the mode; rerun leave-one-case-out *and* paired accuracy; keep weather labeled weather until n ≥ 50.

Automation is the reward for a pipeline that already knows how to refuse.
