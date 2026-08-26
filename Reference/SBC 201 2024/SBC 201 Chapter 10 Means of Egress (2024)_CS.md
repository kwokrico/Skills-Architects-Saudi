# SBC 201 Chapter 10 Means of Egress
**Architect critical summary for schematic design**
2024 | SBCNC

> Scope note: This chapter is the means of egress system — exit access, exit, and exit discharge — including occupant load, capacity, number of exits, accessible means of egress, doors/stairs/ramps, travel distance, corridors, and assembly seating. It is not occupancy classification (Ch. 3) or sprinkler thresholds (Ch. 9). Maintenance and fire-safety plans are **SBC 801**. Technical accessibility geometry for ramps/doors on accessible routes is **ICC A117.1** (no edition year in this chapter’s charging text). Existing MOE alterations: **SBC 901**.

## Regulatory Overview
Every occupied space needs a complete three-part means of egress sized from occupant load (Table 1004.5) and the number of exits (Tables 1006.2.1 / 1006.3.3 / 1006.3.4). Schematic plan shape is locked by travel distance (Table 1017.2), corridor rating/width (Table 1020.2), and whether a second accessible means of egress or area of refuge is required (1009).

## Critical main topics and subtopics

### 1. Occupant load (1004.5, 1004.8)
OL = floor area ÷ Table 1004.5 factor (function of space, **not** occupancy group). Increased OL allowed if other requirements are met; density shall not exceed **1 occupant / 0.65 m²**. Concentrated business (call centres, trading floors): actual load if approved, **not less than 1 / 4.65 m²** gross.

| Function of space | m² per occupant | Net/gross |
|-------------------|-----------------|-----------|
| Assembly concentrated (chairs only, not fixed) | 0.65 | net |
| Assembly standing | 0.46 | net |
| Assembly unconcentrated (tables and chairs) | 1.4 | net |
| Assembly exhibit/museum | 2.8 | net |
| Business areas | 14 | gross |
| Educational classroom | 1.9 | net |
| Mercantile basement and grade | 2.8 | gross |
| Mercantile other floors | 5.6 | gross |
| Parking garages | 19 | gross |
| Day care | 3.3 | net |
| Dormitories | 4.6 | gross |
| Accessory storage / mechanical | 28 | gross |

Residential and warehouse rows in the extract table are OCR-incomplete — use the published Table 1004.5, not commentary examples that conflict (e.g. business 9 m²).

**SD takeaway:** Size exits from function factors, not from occupancy group — a mosque prayer hall is assembly net density, not “A-3 office.”

### 2. Capacity (1005)
| Component | Base | Reduced (NFPA 13 or 13R **and** EVAC 907.5.2.2; not Group H or I-2) |
|-----------|------|--------|
| Stairways (1005.3.1) | **7.6 mm** / occupant | **5.08 mm** / occupant |
| Other components (1005.3.2) | **5.08 mm** / occupant | Commentary **3.8–3.81 mm** / occupant (code exception OCR-garbled) |

Loss of any one exit shall not drop remaining capacity below **50%** (1005.5). Open door may cut required width by ≤ **175 mm** and never more than half (1005.7.1).

**SD takeaway:** Stair width is a millimetre-per-occupant product, not a default 1100 mm — high-OL assembly stairs grow fast unless the reduced factor applies.

### 3. Number of exits and single-exit limits (1006)
**Table 1006.3.3** — exits per story: OL 1–500 → **2**; 501–1,000 → **3**; > 1,000 → **4**.

**Table 1006.2.1** (one exit or exit-access doorway from a space) — selected rows:

| Occupancy | Max OL | Common path with sprinkler (m) |
|-----------|--------|--------------------------------|
| A, M | 49 | 23 |
| B | 49 | 30 |
| S | 29 | 30 |
| R-2 | 20 | 38 |
| H-1/H-2/H-3 | 3 | 7.5 |

**Table 1006.3.4(1)** — single-exit R-2 stories: basement through 3rd above grade plane, **≤ 4** dwelling units, travel **≤ 38 m**, plus 13/13R and EERO 1031. Fourth story and up: not permitted.

**Table 1006.3.4(2)** — other single-exit: first story B/F/M/S among others with OL/travel caps (e.g. B/F/M/S **second** story: OL **29**, travel **23 m**). Third story and higher: NP.

**SD takeaway:** Assume two ways out from every story unless the tiny OL/travel box in 1006.3.4 is clearly met — a two-story office over 29 occupants already needs two exits.

### 4. Accessible means of egress (1009)
Accessible spaces: ≥ **1** AMOE; where more than one MOE is required, ≥ **2** AMOE. Accessible floor or occupied roof **≥ 4 stories** above or below the level of exit discharge: ≥ **1** AMOE shall be an elevator (1009.2.1), with sprinklered exceptions (horizontal exit or ramp).

AMOE stair clear width **1200 mm** between handrails (exceptions if sprinkled or from a horizontal-exit refuge). Area of refuge: **750 × 1300 mm** wheelchair space per **200** occupants served; smoke barrier or horizontal exit; two-way communication. Sprinklered buildings often omit the stair AOR (1009.3.3 exceptions).

**SD takeaway:** Four stories of accessible occupancy locks an evacuation elevator (or a documented exception) into the core at SD — not a late lift specification.

### 5. Doors, stairs, ramps, guards (1010–1015)
| Element | Schematic lock |
|---------|----------------|
| Door clear width (1010.1.1) | **800 mm** (I-2 bed movement **1000 mm**); clear height **2000 mm** |
| Stair width (1011.2) | **≥ 1100 mm** and ≥ 1005 capacity |
| Stair headroom | **≥ 2100 mm** |
| Riser / tread (1011.5.2) | Riser **100–175 mm**; rectangular tread **≥ 275 mm** (R-2/R-3/U exception: riser ≤ 200 mm, tread ≥ 250 mm) |
| Ramp slope (1012.2) | MOE ≤ **1:12**; other pedestrian ≤ **1:8**; max rise per run **750 mm** |
| Ramp clear width | **≥ 900 mm** between handrails; landings **≥ 1500 mm** |
| Guards (1015.2–1015.3) | Required where drop **> 750 mm** within **900 mm** of the edge; height **≥ 1100 mm** (some R-2/R-3 ≤ 3 stories: **≥ 900 mm**) |

**SD takeaway:** Budget 1100 mm stairs, 800 mm door leaves, 1:12 ramps, and 1100 mm guards at every drop over 750 mm — those four numbers set corridor and terrace sections.

### 6. Exit-access travel distance (Table 1017.2)
| Occupancy | Without sprinkler (m) | With sprinkler (m) |
|-----------|----------------------|--------------------|
| A, E, F-1, M, R, S-1 | 60 | 75 |
| B | 60 | 90 |
| F-2, S-2, U | 90 | 120 |
| I-1 | NP | 75 |
| I-2, I-3 | NP | 60 |
| I-4 | 46 | 60 |
| H-1 / H-2 / H-3 / H-4 / H-5 | NP | 23 / 30 / 46 / 53 / 60 |

(I-1 appears in a garbled first table row and as a separate NP/75 line; treat I-1 as **NP / 75**.)

**SD takeaway:** Sprinklering is a plan-depth decision: Group B travel jumps 60 → 90 m; unsprinklered I and H travel is not permitted.

### 7. Corridors (Table 1020.2)
| Occupancy | OL served | Rating NS | Rating sprinkled |
|-----------|-----------|-----------|------------------|
| A, B, E, F, M, S, U | > 30 | 1 h | 0 |
| R | > 10 | NP | 0.5 or 1 h (note d) |
| I-1, I-3 | All | NP | 1 h |
| H-1/H-2/H-3 | All | NP | 1 h |

Minimum width: general **1100 mm**; OL < 50 or within a dwelling **900 mm**; Group E corridor OL ≥ 100 or stretcher ambulatory care **1800 mm**; I-2 bed movement **2400 mm**.

**SD takeaway:** Unsprinklered public corridors over 30 occupants are 1-hour walls; sprinkled B/M/E corridors can be 0-hour but still 1100 mm (1800 mm in large schools).

### 8. Exits, discharge, assembly (1023, 1026, 1028, 1030)
Interior exit stair/ramp enclosure: **2 h** if connecting **≥ 4 stories**, **1 h** if fewer (1023.2). Horizontal exit: **2 h** separation; refuge **0.28 m²**/occupant (1026). Exit discharge: to grade; lobby/vestibule exceptions each ≤ **50%** of number and capacity; vestibule depth ≤ **3000 mm**, length ≤ **9 m**. Safe dispersal: **≥ 0.46 m²**/person and **≥ 15 m** from the building.

Assembly OL > **300** with a main exit: main exit ≥ **half** the OL and fronts a street or **≥ 3000 mm** of unoccupied space to the public way (1030.2). Balcony/gallery seating ≥ **50** → two MOE, one each side (1030.5).

**SD takeaway:** Four or more stories means 2-hour exit enclosures; assembly over 300 occupants needs a street-facing main exit sized for half the house.

### Source
`Chapter_10 — MEANS OF EGRESS.txt`. Companions named in this chapter: **SBC 801** (maintenance, evacuation plans); **SBC 901** (existing MOE); **ICC A117.1** (accessible route/door/ramp/signage geometry; no year in charging text); **SBC 1101/1102** (residential stair/landing alignment); ASME A17.1/CSA B44 (AMOE elevators); Chapter 11 scoping; Chapter 9 sprinkler/EVAC rows used by the tables.
