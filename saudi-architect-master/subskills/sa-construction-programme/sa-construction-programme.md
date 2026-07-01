---
name: sa-construction-programme
description: >
  KSA construction sequencing: fast-track giga-project swimlanes, RC tower floor cycle, follow-the-structure façade,
  hold-point register, and 4-week look-ahead for Vision 2030 high-rise delivery.
user-invocable: true
disable-model-invocation: true
---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Construction sequence, fast-tracking, floor cycle, look-ahead, hold points | `sa-construction-programme` | `sa-project-management` |
| Authority permit sequencing | `sa-consent-scheduling` | — |
| Site supervision, deviations, inspection records | `sa-site-supervision` | — |
| Mobilisation, hoarding, TMP | `sa-site-establishment` | — |
| Procurement route / contract programme clauses | `sa-procurement-strategy` | — |

## Halt conditions

- Stop and request data if **AHJ**, occupancy, or approval status is unknown (see `../../references/compliance.md`).
- Do not assert regulatory compliance without verified code edition and authority pathway.
- Durations are **illustrative** — project-specific contractor programme required.

# KSA Construction Programme

## 1. Archetype defaults (KSA high-rise)

| Typology | Typical floor cycle (indicative) | Notes |
|----------|----------------------------------|-------|
| RC flat slab tower | 5–8 days / floor | Summer heat may extend pours |
| Composite steel + deck | 4–6 days / floor | Façade follow-structure |
| Podium + tower | Podium 12–16 weeks | Plant room long-leads |
| Hospitality fit-out | 12–20 weeks / floor post shell | Brand standards |

## 2. Swimlane index

See `references/sa-construction-sequence-swimlanes.md` for lane diagrams.

| Lane | Activities |
|------|------------|
| Substructure | Piling, raft, basement waterproofing |
| Superstructure | Core, slabs, climbing formwork |
| Envelope | Façade panels, glazing, roof |
| MEP rough-in | Risers, plant install |
| Authority | SBPS inspections, SCD witness points |
| Commissioning | IST, TAB, integrated testing |

## 3. KSA substitution table (programme drivers)

| Driver | Impact |
|--------|--------|
| SCD hold points | Smoke test, pressurization before ceiling close |
| SASO lifts | 16–24 week lead — order at DD |
| Sandstorms | Crane / façade shutdown days |
| Ramadan | ~25% productivity reduction if not priced |
| Prayer breaks | Daily non-productive windows on site |

## 4. Architect / PM early-freezes

Freeze before tender / IFC issue where programme critical:
- Façade system and bracket layout
- MEP plant room equipment selections
- Lift cores and fire stair widths (SBC 501)
- Structural transfer levels

## 5. Interface rules

- **Follow-the-structure façade:** Glazing ≤ 3 floors below slab above — wind load in KSA.
- **MEP vs ceiling close:** No permanent ceiling until SCD hold point signed.
- **Authority inspections:** Book 2 weeks ahead in Riyadh peak periods.

## 6. Programme artefacts

| Artefact | Frequency |
|----------|-----------|
| Master schedule | Baseline + monthly update |
| 4-week look-ahead | Weekly (`../../references/templates/construction-look-ahead.md`) |
| Hold-point register | Live |
| Procurement log | Weekly (long-leads) |

## 7. Six success keys (KSA fast-track)

1. Single integrated BIM / drawing truth for SBPS
2. SCD NOC frozen before bulk MEP procurement
3. Façade mock-up and IST early on giga-projects
4. Utility energization dates in master programme
5. Seasonal float explicit in contract baseline
6. Look-ahead linked to TMP windows (`sa-site-establishment`)

## 8. Output checklist

- [ ] Typology and floor cycle stated as indicative
- [ ] Swimlane or sequence narrative provided
- [ ] Hold points identified with authority owner
- [ ] Long-lead items listed
- [ ] Cross-links to supervision and mobilisation modules
- [ ] Assumptions on seasonal productivity declared
