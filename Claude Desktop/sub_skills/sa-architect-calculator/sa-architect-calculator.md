---
name: sa-architect-calculator
description: >
  Deterministic helper calculators for early-stage coordination: area aggregation, simple geometric checks,
  and envelope sanity checks. Not a substitute for full SBC/SCD compliance analysis.
user-invocable: true
---

# Architect Calculator (Helpers)

## Available calculators
Use the dispatcher tool `run_saudi_calculator` with:
- `calc_type`: `egress_1004_7` or `egress_diagonal_proxy`\n  - Data: `{ "length": <m>, "width": <m>, "limit_m": <optional> }`
- `calc_type`: `gfa_aggregator`\n  - Data: `[ { "area": <float>, "is_exempt": <bool> }, ... ]`
- `calc_type`: `u_value_from_layers`\n  - Data: `[ { "name": "...", "r": <m2K/W> }, ... ]`
- `calc_type`: `delta_t_check`\n  - Data: `{ "t_inside_c": 24, "t_outside_c": 46 }`

## Notes
- For egress, these are **sanity checks only**. Always validate routes and final compliance against the applicable SBC edition and AHJ expectations.

