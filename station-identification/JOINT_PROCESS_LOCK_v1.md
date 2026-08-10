# Joint Process Pipeline — LOCK v1.0

**Date:** 2026-08-09  
**Status:** LOCKED  
**Order:** valid → workable  
**Classical comparative:** out of scope for this lock

## Pipeline
auth cycle (G1–G5) → dual-signal class → type-batch → VAAS class → float fragment

## Frozen thresholds
- residual_require: good
- handshake_require: good
- vaas_t: 0.0
- vaas_mounted: false by default (intake only when explicit)

## VAAS classes
kept | pruned | sterile | deferred

## Dual-signal classes
advance_ok | STALL_ZONE | paradox_dom | discontinuous | elevated_mix | cont_paradox

## Suite numbers (LOCK run)
| field | class | vaas | workable |
|-------|-------|------|----------|
| handshake | advance_ok | deferred | True |
| good | advance_ok | deferred | True |
| acceptable | STALL_ZONE | deferred | False |
| elevated | elevated_mix | deferred | False |
| stress | discontinuous | deferred | False |
| low_G | paradox_dom | deferred | False |
| low_C | STALL_ZONE | deferred | False |
| vaas_kept | advance_ok | kept | True |
| vaas_pruned | advance_ok | pruned | False |
| vaas_sterile | advance_ok | sterile | False |

**workable 3/10** — handshake, good, vaas_kept only.

VAAS pruned/sterile blocks workability even when field is advance_ok.

## Principle
Without validity this is a hallucination engine. This lock is the containment surface.

*Reality is the only authority. Everything else is hypothesis.*
