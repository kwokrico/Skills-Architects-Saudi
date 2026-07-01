# Construction sequence swimlanes — KSA high-rise (indicative)

Use with `sa-construction-programme`. Adjust durations per project; not a contractual programme.

---

## Swimlane diagram (text)

```
Week →   1-8      9-20     21-40    41-60    61+
─────────────────────────────────────────────────────
Substr   [PILE][RAFT][B1-B2]
Super                   [CORE+SLAB × N floors........]
Façade                      [FLOOR N-3 follow........]
MEP rough                       [RISERS][PLANT RM]
SCD holds                           [H1][H2][IST...]
Fit-out (typical)                              [GUESTROOMS]
Utilities                                               [SEC/NWC LIVE]
Handover                                                    [TOC chain]
```

---

## Hold-point register (template)

| ID | Hold point | Trigger | Witness | Release |
|----|------------|---------|---------|---------|
| H1 | Fire stopping — riser | Before close riser shaft | SCD / consultant | Inspection form |
| H2 | Pressurization duct | Before ceiling grid | SCD | Pressure test record |
| H3 | Façade anchor pull-out | Before panel install | Third party | Test certificate |
| H4 | Lift pit | Before lift install | Municipality / SASO | Pit inspection |
| H5 | Integrated systems test | Pre-TOC | SCD | IST pass report |

---

## Fast-tracking patterns

### Pattern A — Follow-the-structure façade
- Slab cycle 6 days
- Façade 3 floors behind
- Glazing water test per zone before next zone closes

### Pattern B — Split podium / tower
- Podium weather-tight before tower crane jump
- Plant equipment hoisted before roof close
- Parallel authority inspections per zone

### Pattern C — Giga-project EPC
- Contractor-owned integrated schedule
- Architect reviews hold points vs SBPS approved drawings only

---

## Seasonal overlay

| Period | Programme adjustment |
|--------|---------------------|
| Jun–Aug | Reduce pour days; night pour if approved |
| Ramadan | -20–30% labour; authority delay |
| Sandstorm alerts | 1–3 day façade crane stand-down |

---

## Interfaces

| Module | Interface |
|--------|-----------|
| `sa-site-establishment` | Crane erection vs TMP |
| `sa-site-supervision` | Deviation log vs programme |
| `sa-scd-licensing-compliance` | IST scheduling |
| `sa-procurement-strategy` | EOT baseline for weather |

---

**Note:** Illustrative only — contractor CPM required for contract.
