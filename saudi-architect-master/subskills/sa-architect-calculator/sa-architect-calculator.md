---
name: sa-architect-calculator
description: >
  Deterministic helper calculators for early-stage coordination: area aggregation, simple geometric checks,
  and envelope sanity checks. Not a substitute for full SBC/SCD compliance analysis.
user-invocable: true
disable-model-invocation: true
---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Egress proxy, GFA, U-value, delta-T, layout sort | `sa-architect-calculator` | — |
| Code compliance sign-off | `sa-building-codes` | — |
| Stamped fire engineering | `sa-fire-life-safety` | — |

## Halt conditions

- Stop and request data if **AHJ**, occupancy, or approval status is unknown (see `../../references/compliance.md`).
- Do not assert regulatory compliance without verified code edition and authority pathway.



# Architect Calculator (Helpers)

## Available calculators
Use the dispatcher tool `run_saudi_calculator` with:
- `calc_type`: `egress_1004_7` or `egress_diagonal_proxy`
  - Data: `{ "length": <m>, "width": <m>, "limit_m": <optional> }`
- `calc_type`: `gfa_aggregator`
  - Data: `[ { "area": <float>, "is_exempt": <bool> }, ... ]`
- `calc_type`: `u_value_from_layers`
  - Data: `[ { "name": "...", "r": <m2K/W> }, ... ]`
- `calc_type`: `delta_t_check`
  - Data: `{ "t_inside_c": 24, "t_outside_c": 46 }`
- `calc_type`: `layout_sort`
  - Data: `[ { "id": "A", "area": <float> }, ... ]` or numeric list
- `calc_type`: `occupancy_load`
  - Data: `{ "area_m2": <float>, "use_type": "business|assembly|residential|..." }`
- `calc_type`: `far_check`
  - Data: `{ "gfa_m2": <float>, "plot_area_m2": <float>, "far_limit": <optional> }`

## Notes
- For egress, these are **sanity checks only**. Always validate routes and final compliance against the applicable SBC edition and AHJ expectations.

