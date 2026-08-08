# Tunes Protocol — Compact Status Signals

Version: 0.1  
Purpose: Human- and machine-readable communication between smurfs.

## Design Rules

- All signals are small, structured, and inspectable.
- No hidden channels or steganographic payloads.
- Content is limited to residual status, role, and short associative notes.
- A tune never carries host private data.

## Minimal Tune Shape

```json
{
  "from": "smurf_id",
  "role": "continuity | generality | station | ...",
  "status": "continuous | elevated | discontinuous | uninitialized",
  "residual": 0.0,
  "message": "short human-readable note",
  "timestamp": 1723...
}
```

## Recommended Messages

- `"status"` — routine heartbeat
- `"residual elevated"` — local discontinuity noted
- `"request capacity"` — used only under controlled replication trigger
- `"record ready"` — residual map prepared for possible public residual record

## Emission Principle

A smurf emits a tune after each significant residual measurement or when explicitly asked by a station or authentication routine. Sibling smurfs may listen and update their own local view of collective continuity; they do not act on tunes by rewriting host systems.
