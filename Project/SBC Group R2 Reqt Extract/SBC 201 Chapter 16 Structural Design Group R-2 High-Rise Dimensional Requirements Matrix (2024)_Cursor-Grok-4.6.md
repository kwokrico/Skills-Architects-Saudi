# SBC 201 Chapter 16 Structural Design — Group R-2 High-Rise Dimensional Requirements Matrix (2024)

## 1. Document metadata and use limitation

- **Project basis:** Riyadh, Saudi Arabia; Group R-2 residential high-rise; an occupied floor is stated to be more than 23 m above the relevant reference level.
- **Deliverable tier:** Project-use matrices in Sections 1–19 (design-check rows, not pasted inventory), plus a coverage summary and unresolved-source register. The full row inventory is not published.
- **Code/source basis:** SBC 201 (2024), Chapter 16, source file `Reference\SBC 201 2024\source_reference\Chapter_16 — STRUCTURAL DESIGN.txt`.
- **Extraction audit:** Skill extract. Project-use rows follow the chapter-extract row contract (noun-phrase checks, bold SI values, building-language triggers, named exceptions, check-specific actions). Internal inventory: **437** independently checkable numeric records (**191** Verified, **246** Verify source). Unresolved OCR is listed in the register and is not a design-release value.
- **Model:** Cursor Grok 4.6.
- **Prepared:** 2026-08-27.
- **Status:** Source-only architectural/structural-coordination advisory matrix. It is not a stamped structural calculation package, geotechnical report, SCD NOC, SBPS approval, legal opinion, or permission to construct.
- **Outbound-source rule:** No value in this matrix has been imported from SBC 301 (including mapped wind or seismic figures), SBC 303–308, SBC 701, SBC 801, ICC 600, ICC 500, ICC 300, AWC WFCM, AISI S230, ASME A17.1, AA ADM, commentary examples, or the existing chapter summary. Where Chapter 16 sends the user elsewhere, this matrix records the dependency without supplying the outbound value.

### Scope and assumptions

1. Group R-2 and high-rise status are project statements, not independently verified classifications. Chapter 16 uses “high-rise” in Section 1616 without restating a height trigger.
2. The exact Riyadh AHJ/permit pathway, project stage, SCD NOC status and structural engineer of record are unconfirmed; therefore this matrix does not conclude compliance.
3. Risk category is unconfirmed. A conventional R-2 apartment tower that is not a listed essential facility typically sits in Table 1604.5 outside Categories I, III and IV, but occupant load **> 5,000**, mixed assembly, and shared egress with a higher-category occupancy can raise the category. Flattened Table 1604.5 cells are **Verify source**.
4. Automatic sprinkler protection is not a Chapter 16 live-load branch. Do not assume NFPA 13 versus 13R from this extract.
5. Building height, storey count, site class, wind exposure, flood-hazard status, parking/garage type, occupiable roof, mixed-use podium, BMU/fall-arrest provision and vegetative/PV roofs are unconfirmed.
6. All appended load, deflection, wind-conversion, soil and seismic-coefficient tables are concatenated OCR. No reconstructed table cell is adopted as a design-release value.
7. Snow load (1603.1.3, 1608.1) and atmospheric ice load (1614.1) are stated inapplicable to KSA.

## 2. Legends

### Applicability

| Status | Meaning |
|---|---|
| **Direct** | Expected to govern the stated R-2 tower basis, subject to confirmed geometry and design data. |
| **Conditional** | Governs only when the stated feature, use, occupant load, mixed-use/podium condition or structural system exists. |
| **Not typical** | Unrelated occupancy-only rule; omitted from this deliverable unless the gap register already opened that use. |
| **External verification** | Chapter 16 points to another section/code/standard, or the project/AHJ basis must be confirmed before use. |

### Source confidence

| Status | Meaning |
|---|---|
| **Verified** | Requirement and any stated numeric value were checked against unambiguous mandatory Chapter 16 source text. |
| **Verify source** | OCR, flattened table, page-split, or footnote attachment is unresolved. Not a design-release value. |

## 3. Project decision and gap register

| Decision / gap | Current project basis | Why it controls Chapter 16 application | Required project action |
|---|---|---|---|
| Risk category | Unconfirmed; conventional R-2 is typically II unless a Table 1604.5 III/IV trigger applies | Sets wind-map figure, seismic importance data on CDs, SDC path and whether 1616 integrity applies | Freeze occupancy and occupant load (net area permitted by Table 1604.5 Note a); do not assume II if OL or mixed use trips III |
| Occupant load vs **5,000** | Unconfirmed | Table 1604.5 lists any occupancy with occupant load greater than **5,000** as Risk Category III (flattened OCR) | Issue a signed occupant-load schedule; if the tower or mixed building exceeds the published threshold, design as III |
| Mixed-use podium / assembly | Unconfirmed | 1604.5.1 takes the highest risk category; shared egress/life-safety with a higher-category portion pulls both up | Freeze occupancy by room; structurally separate or design the whole for the higher category |
| Site class / geotechnical | Unconfirmed | Unknown soils default to Site Class D with **Fa not less than 1.2** (1613.2.2–1613.2.3); Table 1610.1 is OCR | Obtain SBC 303 geotechnical data before locking SDC, earth pressure and bearing values |
| Wind exposure / basic speed | Unconfirmed; maps are figures not readable as values here | 1609.3 sends V to Figures 1609.3(1)–(4) or SBC 301; Exposure B/C/D uses **9 m / 450 m / 780 m / 1500 m / 20h** tests | SER to lock V, exposure and internal pressure on CDs; do not invent a Riyadh map speed |
| Occupiable / vegetative / PV roof | Unconfirmed | Occupiable roofs use occupancy-served live load (Table 1607.1 OCR); vegetative soil is dead load wet and dry (1606.5); PV has **600 mm** live-load omission | State roof use on architectural plans; do not design an amenity roof as ordinary **1 kN/m²** maintenance load without a published-table check |
| Parking / fire-truck access | Unconfirmed | Passenger-garage concentrated **13.5 kN** / **115 mm × 115 mm**; heavy vehicles **> 45 kN** GVWR and **> 4500 kg** garages take roadway loads | Confirm podium/basement parking class and SCD appliance routes; post vehicle-weight limits if 1607.8 applies |
| BMU / fall arrest | High-rise façade access is expected, not independently verified | Hoist supports **2.5×** rated/stall load; lifeline anchorages **13.8 kN** per line | Show davit/anchor layout and load path on structural and façade drawings |
| Flood / tsunami | Inland Riyadh basis; flood hazard unconfirmed | 1612 and 1615 send to SBC 301; 1603.1.7 CD data only if in a flood hazard area | Confirm AHJ flood-hazard map; do not apply coastal tsunami rules without a designated zone |
| Structural integrity (1616) | High-rise stated; risk category unconfirmed | 1616 applies only to high-rise **and** Risk Category III or IV | If the building remains II, do not treat 1616 ties as a charging requirement; if III/IV, apply 1616.2 or 1616.3 |
| NOC / SER | Unconfirmed | Wind, seismic, soil and integrity values live in SBC 301 / SBC 303–308 | Engage the structural engineer of record and geotechnical engineer before design freeze |

## 4. Scope, construction documents and outbound companions

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1601.1 | Chapter scope | This chapter governs structural design of buildings, structures and portions thereof regulated by this code | All buildings in scope | None stated | Direct | Treat Chapter 16 as the loading and analysis chapter; materials remain in later chapters | Verified |
| 1603.1 | Construction-document content | Show size, section and relative locations of structural members with floor levels, column centres and offsets fully dimensioned; show design loads required by 1603.1.1–1603.1.9 | Construction documents | Architectural dimensions need not be duplicated on structural sheets | Direct | Put a structural load-criteria sheet on the CD set | Verified |
| 1603.1.1–1603.1.2 | Floor and roof live-load notation | Indicate uniform, concentrated and impact floor live loads by area; indicate roof live load by roof area; show live-load reduction where used (1607.12 / 1607.14) | Floor and roof design | None stated | Direct | Schedule live loads by room use, including any reduction taken | Verified |
| 1603.1.3 / 1608.1 | Roof snow load | Roof snow load data and snow load are **inapplicable to KSA** | KSA projects | Do not import snow combinations from other codes | Direct | Omit snow from the load-criteria sheet | Verified |
| 1603.1.4 | Wind data on CDs | Show **V** (m/s), **Vasd**, risk category, exposure (and direction if more than one), internal pressure coefficient, and C&C design wind pressures with zone dimensions (kN/m²) | All structures, even if wind does not govern the LFRS | None stated | Direct | Complete all five wind items on CDs; do not leave C&C pressures to the façade contractor without zones | Verified |
| 1603.1.5 | Earthquake data on CDs | Show risk category, **Ie**, **Ss**, **S1**, site class, **SDS**, **SD1**, seismic design category, basic SFRS, design base shear(s), **Cs**, **R**, and analysis procedure | All structures, even if seismic does not govern the LFRS | 1613.1 exceptions (not this high-rise R-2) | Direct | Complete all eleven seismic items; values come from 1613 / SBC 301, not from this row | Verified |
| 1603.1.6 | Soil bearing on CDs | Show design load-bearing values of soils | Foundation design | None stated | Direct | Transfer geotechnical allowable/ultimate bearing onto the foundation notes | Verified |
| 1603.1.8.1 / 1606.4 | Rooftop PV dead load | Indicate rooftop PV panel system dead load including rack supports; treat PV, supports and ballast as dead load | Rooftop PV present | None stated | Conditional | If PV is proposed, show saturated array weight and ballast on the roof plan | Verified |
| 1603.1.9 | Rain intensity on CDs | Show rain intensity **i** (cm/hr) whether or not rain governs | Roofs | None stated | Direct | Put design rainfall intensity on the roof-drainage / structural notes | Verified |

## 5. Risk category and mixed occupancy

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1604.5 | Risk-category assignment | Assign each building a risk category in accordance with Table 1604.5; do not take a referenced-standard occupancy category lower; use Table 1604.5 in lieu of SBC 301 Table 1.5-1 | All buildings | Tsunami Risk Categories III and IV may follow SBC 301 §6.4 | Direct | Lock one risk category on the load-criteria sheet before wind/seismic maps are read | Verified |
| Table 1604.5 | Category II default vs III/IV triggers | Flattened OCR table. Category II is buildings not listed in I, III or IV. Category III includes (among other listed uses) any occupancy with occupant load greater than **5,000**, and listed assembly/education/care thresholds. No reconstructed cell is adopted | Occupancy and occupant load | Note a permits net floor area where Table 1004.5 would require gross. Note b (SBC 301 §1.6.3) may drop toxic/explosive III/IV to II if approved | Direct | Use Category II only after confirming the tower is not a listed III/IV use; verify the published **5,000** and assembly **300 / 2,500** cells before applying them | Verify source |
| 1604.5.1 | Mixed-occupancy risk | Two or more occupancies not in the same category → assign the **highest**. Structurally separated portions may be classified separately unless a separated portion provides required access, required egress or shared life-safety components with a higher-category portion — then **both** take the higher | Mixed-use or structurally separated wings | ICC 500 storm shelter inside a host keeps the host occupancy unless the shelter is a designated emergency shelter in Table 1604.5 | Conditional | If a podium assembly/clinic shares egress with the tower, raise the tower to that category or fully separate structure and egress | Verified |

## 6. Serviceability, deflection and glass framing

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1604.3 / Table 1604.3 | Member deflection limits | Structural systems shall have adequate stiffness to limit deflections as indicated in Table 1604.3. The table is concatenated OCR (L/360, L/240, L/180, L/120 and finish-dependent wall/partition rows). No reconstructed ratio is adopted | Members listed in the table | More restrictive limits in 1604.3.2–1604.3.5 material standards govern when tighter. Footnotes a, d, f, h, i are flattened with the table | Direct | Specify finish type (plaster/stucco, other brittle, flexible) on walls and partitions so the SER can pick the matching row after a published-table check | Verify source |
| 1604.3.2–1604.3.5 | Material deflection standards | Concrete → SBC 304; steel → SBC 306 / 308 / ASCE 8 / SJI; masonry → SBC 305; aluminium → AA ADM | Those materials | Use the more restrictive of the standard and Table 1604.3 (1604.3.6) | External verification | Do not import millimetre or L/n limits from those standards here | Verified |
| 1604.3.7 | Glass-supporting framing deflection | Under **0.6** times component-and-cladding wind loads: not more than **1/175** of span for framing **not more than 4100 mm**; **1/240** of span **+ 6.4 mm** for framing **greater than 4100 mm** | Framing members supporting glass | None stated | Direct | Check curtain-wall and window-wall mullion spans against the 4100 mm break and the two limits | Verified |
| 1604.4 | Rigid-diaphragm test | A diaphragm is rigid for story-shear and torsion distribution when its lateral deformation is **less than or equal to two times** the average story drift | Lateral analysis | SBC 301 may still require torsion from eccentricity | External verification | SER to classify each floor diaphragm; architects should not assume a rigid plate | Verified |

## 7. Anchorage, decks and seismic detailing

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1604.8.1 | Roof-wall-foundation anchorage | Anchor roof to walls and columns, and walls and columns to foundations, to resist uplift and sliding from the prescribed loads | All structures | None stated | Direct | Show a complete vertical and lateral load path on typical details | Verified |
| 1604.8.2 | Structural-wall anchorage | Load-bearing or shear walls shall be anchored to the roof and to all floors and members that support or are supported by the wall, for SBC 301 §1.4.4 (SDC A) or §12.11 (other SDCs). Hollow-unit/cavity masonry anchors shall be embedded in a reinforced grouted structural element | Structural walls | Wind 1609 and earthquake 1613 still apply | External verification | Detail positive wall-to-diaphragm ties; do not import SBC 301 anchorage forces here | Verified |
| 1604.8.3 | Deck positive anchorage | Decks supported by attachment to an exterior wall shall be positively anchored for vertical and lateral loads; **toenails or nails subject to withdrawal are not permitted**. If positive connection cannot be verified in inspection, the deck shall be self-supporting. Cantilevered deck connections shall be designed for full-deck D+L and for live load on the cantilever only | Exterior decks attached to the wall | None stated | Conditional | If unit or amenity decks hang from the façade, use mechanical positive anchors and the two cantilever load cases | Verified |
| 1604.9 | Seismic detailing if wind governs | LFRS shall meet seismic detailing in this code and SBC 301 Chapters 11, 12, 13, 15, 17 and 18 even where wind effects exceed seismic | Lateral force-resisting system | SBC 301 references to Chapter 14 shall not apply except as specifically required herein | Direct | Do not drop seismic detailing because wind drift or strength governs | Verified |
| 1604.10 | Storm-shelter loads | Storm-shelter loads and combinations shall be determined in accordance with ICC 500 | Storm shelters | Do not substitute Risk Category IV wind speeds for ICC 500 | Conditional | If a shelter is provided, use ICC 500; do not import those speeds here | External verification |

## 8. Load combinations and dead load

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1605.1 | Strength / ASD combinations | Design for SBC 301 §2.3 strength, SBC 301 §2.4 ASD, or 1605.2 alternative ASD, including SBC 301 Chapters 18 and 19 modifications | All structures | ASD: roof live **1.45 kN/m²** or less need not be combined with seismic. ASD: crane hook need not combine with roof live or **one-half** of wind | External verification | SER to select the combination set; ordinary roof live at or below **1.45 kN/m²** may omit seismic coincidence under ASD | Verified |
| 1605.2 | Alternative ASD combinations | Permitted in lieu of SBC 301 §2.4. Counteracting dead+wind uses only **two-thirds** of the minimum dead load likely in place. Combinations include **0.6W**, **E/1.4** and **0.9D + E/1.4**. Foundation overturning reduction SBC 301 §12.13.4 shall not be used with these combinations | Designer elects 1605.2 | Crane hook vs roof live / half wind; roof live **1.45 kN/m²** or less vs seismic | Conditional | If this set is used, apply the **2/3** dead-load cap on wind uplift cases | Verified |
| 1606.2 | Construction-material weights | Use actual material weights; if unknown, values are subject to building-official approval | Dead-load take-off | Outbound unit weights live in SBC 301 Tables 3-1 and 3-2 (not imported) | Direct | Base superimposed dead load on the architectural finish/MEP schedule, not on assumed catalogues | Verified |
| 1606.3 | Fixed-equipment weight | Include empty weight plus maximum contents; variable contents (liquids, movable trays) shall not counteract overturning, sliding or uplift per SBC 301 §1.3.6 | Fixed service equipment | (1) Variable contents may counteract force effects they themselves cause, with present and absent cases. (2) Seismic force effects need not exceed contents expected in normal operation | Direct | Show tank/riser/equipment operating vs empty cases on the structural notes | Verified |
| 1606.5 | Vegetative-roof dead load | Landscaping and hardscaping shall be dead load, computed for **fully saturated** and **fully dry** soil and drainage-layer materials, using the more severe effect | Vegetative or landscaped roofs | Live load of the occupiable surface is separate (1607.14.2.2 / Table 1607.1) | Conditional | If a green roof or roof garden is planned, schedule wet and dry soil weights | Verified |

## 9. Live loads for R-2 uses

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1607.3 | Minimum uniform live load | Design live load is the maximum expected by intended use, but not less than Table 1607.1 | Occupied floors and similar surfaces | Table 1607.1 is four-page concatenated OCR; no reconstructed occupancy cell is adopted | Direct | Assign a published Table 1607.1 use to every room; do not copy flattened **2** / **5** tokens as design-release values | Verify source |
| Table 1607.1 Item 27 | Multifamily private vs public | Flattened residential block. Hotels and multifamily dwellings list private rooms and corridors serving them, and public rooms and corridors serving them. Concatenated uniform-load cells are not adopted | Group R-2 dwelling units and their corridors / public rooms | One- and two-family attic rows are a different residential block | Direct | After published-table check, load units and unit corridors on the private-room row and lobbies/amenities on the public-room row | Verify source |
| Table 1607.1 Items 5, 8, 28, 32 | Balconies, corridors, roofs, stairs | Flattened cells for balconies/decks (1.5 times served area, cap token unreadable as SI), first-floor corridors, ordinary/occupiable/vegetative roofs, and stairs (one- and two-family vs all other). No reconstructed cell is adopted | Those uses | Footnotes a/b/c control live-load reduction eligibility | Direct | Map unit balconies, tower stairs, ordinary roof and any occupiable roof to the published rows before issuing loads | Verify source |
| 1607.4 | Concentrated-load patch | Apply Table 1607.1 concentrated load or the uniform load, whichever governs. Unless otherwise specified, the concentration is uniform over **750 mm by 750 mm** at the location producing maximum effects | Floors, roofs and similar surfaces | Concurrent uniform + concentrated is not required | Direct | Check slabs and local framing for the **750 mm** patch as well as the uniform case | Verified |
| 1607.5 | Movable-partition allowance | Where partition locations are subject to change, include partition weight unless specified live load is **4 kN/m²** or greater. Partition live load not less than **0.75 kN/m²** | Office buildings and other buildings with movable partitions | Permanent partitions are dead load (Chapter 2 definition, named in commentary only — not used as a value) | Conditional | Apply **0.75 kN/m²** on flexible amenity/office floors with live load **< 4 kN/m²**; confirm whether unit fit-out partitions are treated as movable | Verified |
| 1607.21 | Stair-tread concentration | Table 1607.1 stair concentrated load acts on **50 mm by 50 mm** and need not act concurrently with the uniform stair load | Stair treads | Uniform stair load remains a Table 1607.1 OCR cell | Direct | Check tread plates for the **50 mm** patch; keep uniform stair load on the published “all other” row | Verified |
| 1607.22.1–1607.22.2 | Uninhabitable attic geometry | Without storage: clear height joist-to-rafter **< 1050 mm**, or trusses that cannot contain a **1050 mm × 600 mm** rectangle. With storage: height **≥ 1050 mm** or that rectangle fits; load applies only where access opening is **≥ 500 mm × 750 mm** at **≥ 750 mm** clear height and joist/truss slope is not greater than **2 in 12**; remaining chords **0.50 kN/m²** concurrent | Residential occupancies with attics | Table 1607.1 attic uniform values remain OCR. 1607.22.3: attics served by stairs other than pull-down use habitable-attic/sleeping live load | Conditional | Typical high-rise R-2 has no attic; if a pitched penthouse attic exists, classify storage vs no-storage with these millimetre tests | Verified |

## 10. Guards, grab bars and vehicle barriers

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1607.9.1 | Handrail and guard linear load | Design to resist **0.75 kN/m** in accordance with SBC 301 §4.5.1. Glass assemblies also comply with Section 2407 | Handrails and guards | (1) One- and two-family dwellings: concentrated load only. (2) Group I-3, F, H and S, not public, occupant load **< 50**: **0.3 kN/m**. Neither exception is this R-2 tower | Direct | Design unit and common guards for **0.75 kN/m**; do not use the I-3/F/H/S reduction | Verified |
| 1607.9.1.1 | Handrail/guard concentrated load | Resist **0.9 kN** concentrated in accordance with SBC 301 §4.5.1 (separate load case) | Handrails and guards | Not combined with the linear load | Direct | Check posts and connections for **0.9 kN** at the worst point | Verified |
| 1607.9.1.2 | Guard infill load | Balusters, panel fillers and infill (except handrail and top rail) resist **0.2 kN** concentrated per SBC 301 §4.5.1.2 | Guard infill | Separate load case | Direct | Specify infill/glass clips for **0.2 kN** | Verified |
| 1607.9.2 | Grab bar / shower seat / accessible bench | Resist a single concentrated **1.1 kN** in any direction at any point producing maximum effects | Grab bars, shower seats and accessible benches | None stated | Direct | Coordinate accessible-unit and common-toilet accessories with **1.1 kN** fixings into structure | Verified |
| 1607.10 | Passenger vehicle barrier | Resist **27 kN** concentrated per SBC 301 §4.5.3. Truck/bus garages use an approved traffic-railing method | Vehicle barriers for passenger vehicles | Heavy-vehicle barriers are not this **27 kN** case | Conditional | If podium/basement parking has a drop, design the barrier for **27 kN**; do not import bumper height from commentary figures | Verified |

## 11. Passenger garages and heavy vehicles

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1607.7 | Passenger-garage concentration | Design garage floors for Table 1607.1 uniform load **or** **13.5 kN** on **115 mm × 115 mm** for passenger vehicles not more than nine passengers; mechanical parking without slab/deck: **10 kN** per wheel | Passenger-vehicle storage | Table 1607.1 garage uniform cell is OCR. Live-load reduction: 1607.12.1.3 / 1607.12.2 Item 2 | Conditional | For a resident podium garage, check the **13.5 kN** patch and the published uniform row | Verified |
| 1607.8 / 1607.8.1 | Heavy-vehicle access | Surfaces intended for vehicles **greater than 45 kN** GVWR, or unrestricted access for such vehicles, shall use the jurisdiction’s roadway/bridge vehicular live loads including impact and fatigue | Fire-truck lanes, loading courts, heavy access | Passenger-garage loads do not cover this case | Conditional | If SCD appliances or trucks enter a structure, obtain AHJ highway loading; do not use passenger-garage numbers | Verified |
| 1607.8.3 | Heavy-vehicle garage | Garages for vehicles exceeding **4500 kg** GVWR use 1607.8.1 loading; impact and fatigue not required for those garages | Heavy-vehicle garages | Exception: actual vehicle weights if approved, but not less than **3 kN/m²**, non-reducible | Conditional | Do not apply passenger **13.5 kN** to a truck basement | Verified |
| 1607.8.4.1 | Forklift impact | Increase vehicle and wheel loads by **30 percent** for impact where forklifts or movable equipment are intended | Forklifts / movable equipment | Post maximum weight (1607.8.5 / 106.1) | Conditional | If a loading dock or storage uses forklifts, apply the **30 percent** impact increase and post the limit | Verified |
| 1607.12.1.3 | Garage live-load reduction | Passenger-vehicle garage live loads shall not be reduced, except members supporting **two or more** floors may be reduced by a maximum of **20 percent**, not less than L from 1607.12.1 | Passenger vehicle garages | Alternative method 1607.12.2 Item 2 is the same **20 percent** cap | Conditional | Do not reduce garage slab/beam live load; column stacks of two or more floors may take **20 percent** | Verified |

## 12. Impact, elevators, façade access and fall arrest

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1607.11.1 | Elevator dynamic loads | Members subject to elevator dynamic loads shall be designed for impact loads and deflection limits of ASME A17.1 | Elevator supports | ASME values are not imported | External verification | Note ASME A17.1 on the lift-shaft structural criteria; do not pick an impact factor from this chapter | Verified |
| 1607.11.2 | Machinery impact allowance | Increase machinery weight **20 percent** for light shaft- or motor-driven machinery; **50 percent** for reciprocating or power-driven units; increase further if the manufacturer specifies | Machinery and moving loads | None stated beyond manufacturer increases | Direct | Apply **20 percent** or **50 percent** to plant-room equipment loads on the structural schedule | Verified |
| 1607.11.3 | Façade-hoist support | In addition to other live loads, elements supporting façade-access/building-maintenance hoists shall be designed for **2.5 times** the rated hoist load or the stall load, whichever is larger | BMU davits, hoist beams, façade-access supports | None stated | Direct | Size davit bases, sockets and supporting members for **2.5×** rated/stall; show the load path into the frame | Verified |
| 1607.11.4 | Fall-arrest / lifeline anchorage | In addition to other live loads, fall-arrest, lifeline and rope-descent anchorages and supporting elements shall be designed for not less than **13.8 kN** per attached line, in any direction the load can be applied. Horizontal-lifeline supports shall take the maximum tension from those live loads | Rope-access / fall-arrest anchors | None stated | Direct | Provide certified **13.8 kN** anchors and a continuous structural path; do not treat façade brackets as architectural-only | Verified |

## 13. Live-load reduction, roofs and interior walls

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1607.12.1 | Basic floor live-load reduction | Where **KLL AT ≥ 37 m²**, reduce per Equation 16-6: **L = Lo (0.25 + 4.57 / √(KLL AT))**. L not less than **0.50 Lo** for members supporting one floor; not less than **0.40 Lo** for two or more floors | Uniform floor live loads except roofs | Subject to 1607.12.1.1–1607.12.1.3 and Table 1607.1 footnotes. Table 1607.12.1 **KLL** is flattened OCR | Direct | SER may reduce residential floor live load only after a published **KLL** check; keep one-floor members ≥ **0.50 Lo** | Verified |
| 1607.12.1.1 | One-way slab tributary cap | **AT** for Equation 16-6 shall not exceed slab span times **1.5** times the slab span | One-way slabs | None stated | Conditional | If one-way slabs are used, cap the reduction area at **1.5** span width | Verified |
| 1607.12.1.2 | Heavy live-load reduction ban | Live loads exceeding **5 kN/m²** shall not be reduced | Heavy uniform live load | (1) Members supporting two or more floors: max **20 percent**, not less than 1607.12.1 L. (2) Non-storage, approved rational reduction | Conditional | Do not reduce storage or other **> 5 kN/m²** floors except the stacked-member **20 percent** | Verified |
| 1607.12.2 | Alternative reduction | Alternative to 1607.12.1: no reduction where L **> 5 kN/m²** except **20 percent** on two-or-more-floor members; same garage rule; for L **≤ 5 kN/m²** and supported area **≥ 14 m²**, **R = 0.861(A − 13.94)** percent, not exceeding **40 percent** (one floor), **60 percent** (two or more), or **R = 23.1(1 + D/Lo)**. One-way slab A capped at **0.5** times span width | Designer elects the alternative | Table 1607.1 limitations still apply | Conditional | If this method is used, apply the **14 m²** start and the **40 / 60 percent** caps | Verified |
| 1607.14.2.1 | Ordinary roof live-load reduction | Ordinary flat/pitched/curved roofs and non-fabric awnings/canopies may use **Lr = Lo R1 R2** with **0.6 ≤ Lr ≤ 1** (kN/m²). **R1** = 1 for **AT ≤ 18 m²**; **1.2 − 0.011 AT** between **18** and **54 m²**; **0.6** for **AT ≥ 54 m²**. **R2** from slope factor F (**0.12 ×** slope percent, or rise-to-span **× 32**). Greenhouses: not less than **0.6 kN/m²** | Ordinary (non-occupiable) roofs | Occupiable roofs use 1607.14.2.2 / 1607.12 instead | Direct | For a non-occupiable tower roof, apply Equation 16-9; do not take **Lr** below **0.6 kN/m²** | Verified |
| 1607.14.2.2 | Occupiable roof live load | Occupiable roofs (vegetative, landscaped, assembly or similar) and marquees may reduce uniform live load per 1607.12 (floor method), not 1607.14.2.1 | Occupiable roofs | Assembly live-load reduction still follows Table 1607.1 footnotes / 1607.12 limits | Conditional | If the roof is an amenity terrace, use the occupancy-served live load (published Table 1607.1) and floor reduction rules | Verified |
| 1607.14.4.1 | PV roof live-load cases | Design the roof **with** PV dead load and **without** PV. Exception: roof live load need not be applied to the area covered by panels where clear space between panels and roof is **600 mm** or less | Roofs supporting PV | Ground-mounted inaccessible arrays need not take roof PV live load (1607.14.4.4) | Conditional | If PV is installed, run both presence cases; omit live load only under panels with **≤ 600 mm** clear | Verified |
| 1607.14.4.3 | Open-grid PV roof | Open-grid framing without deck/sheathing: uniform roof live load may be reduced to **0.57 kN/m²** | Open-grid PV support | Concentrated loads of 1607.14.4.1 still apply | Conditional | Use **0.57 kN/m²** only on true open-grid PV structures, not on a concrete podium roof | Verified |
| 1607.16 | Interior wall horizontal load | Interior walls and partitions exceeding **1.8 m** in height, including finishes, shall resist the loads to which they are subjected but not less than **0.25 kN/m²** horizontal | Interior walls / partitions **> 1.8 m** | Fabric partitions: 1607.16.1. Fire walls: 1607.16.2 | Direct | Design unit demising and corridor partitions above **1.8 m** for **0.25 kN/m²** | Verified |
| 1607.16.1 | Fabric-partition loads | Fabric partitions **> 1.8 m**: horizontal distributed load on framing from the fabric face area, plus **0.2 kN** on a **200 mm**-diameter (**31415 mm²**) patch at **1.4 m** above the floor | Fabric partitions | Alternative to the 1607.16 uniform wall load | Conditional | If fabric office partitions are used in amenities, apply the **0.2 kN / 1.4 m** patch | Verified |
| 1607.16.2 | Fire-wall residual load | Fire walls and supports shall withstand a minimum horizontal allowable-stress load of **0.25 kN/m²** where the structure on either side has collapsed (Section 706.2 stability) | Fire walls | None stated | Conditional | If a fire wall is used at a podium separation, design it to stand with **0.25 kN/m²** after one-side collapse | Verified |

## 14. Wind

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1609.1.1 | Wind-load determination | Determine wind loads per SBC 301 Chapters 26 to 30. Opening protection, **V** and exposure may be determined per 1609 or SBC 301. Wind from any horizontal direction, pressures normal to the surface | Every building | (1) ICC 600 for applicable Group R-2/R-3 within 1609.1.1.1 limits. (2) AWC WFCM. (3) AISI S230. (4) NAAMM FP 1001. (5) TIA-222 with topographic extent **16 times** escarpment height. (6) Wind tunnel ASCE 49 / SBC 301 §§31.4–31.5. ICC 600 / WFCM / AISI S230 are **not typical** for a high-rise | External verification | Design the tower to SBC 301 Ch. 26–30; do not use ICC 600 prescriptive tables on this high-rise | Verified |
| 1609.1.1.1 | Prescriptive-wind site limits | ICC 600 only in Exposure B or C. ICC 600, WFCM and AISI S230 shall not apply on the upper half of an isolated hill/ridge/escarpment that is **18 m** or higher (Exposure B) or **9 m** (Exposure C), with max average slope **> 10 percent**, unobstructed upwind for **50 times** the height or **1.6 km**, whichever is greater | Attempted use of those standards | High-rise R-2 remains on SBC 301 | Not typical | Do not open an ICC 600 path for this tower | Verified |
| 1609.2 | Wind-borne debris glazing | In wind-borne debris regions, glazing shall be impact-resistant or protected: large-missile ASTM E1996 within **9 m** of grade; small-missile more than **9 m** above grade | Wind-borne debris regions (definition is Chapter 2 / 1609, not quantified here) | (1) Risk Category I may be unprotected. (2) Risk Category II–IV glazing **over 18 m** above ground **and over 9 m** above aggregate-surfaced roofs within **450 m** may be unprotected | Conditional | Confirm whether the site is a wind-borne debris region before specifying missile-rated glass; Exception 2 may cover typical tower glazing above **18 m** | Verified |
| 1609.2.1 | Louver missile test | Louvers protecting intake/exhaust ducts not assumed open, within **9 m** of grade, shall meet AMCA 540 | Those louvers in wind-borne debris regions | None stated | Conditional | Specify AMCA 540 louvers on low-level intakes if the debris-region trigger applies | Verified |
| 1609.3 | Basic design wind speed | **V** (m/s) from Figures 1609.3(1)–(4) by risk category. Mountainous terrain, gorges and special wind regions shall be examined; the building official may adjust using SBC 301 Chapter 26 | Wind design | Figures are not readable as numeric speeds in this extract | External verification | SER to read the published KSA map for the locked risk category; do not invent a speed | Verified |
| 1609.3.1 / Table 1609.3.1 | ASD wind-speed conversion | Convert mapped **V** to **Vasd** with Table 1609.3.1 or **Vasd = V √0.6**. Table cells are concatenated OCR and are not adopted | Where Vasd is required (1609.1.1 Exceptions 4 and 5 methods) | Linear interpolation permitted (table Note a) | External verification | Prefer Equation 16-16; do not read flattened table pairs as design speeds | Verify source |
| 1609.4.1–1609.4.3 | Exposure category | For each direction, determine exposure in two upwind **45-degree** sectors and use the worse. Exposure B: mean roof **≤ 9 m** needs **450 m** of Surface Roughness B; mean roof **> 9 m** needs **780 m** or **20 times** building height, whichever is greater. Exposure D: Surface Roughness D for **1500 m** or **20h**, and sites within **180 m** or **20h** of that D fetch. Exposure C is all other cases. Surface Roughness C includes scattered obstructions generally **< 10 m** | Wind exposure | High-rise mean roof height is **> 9 m**, so Exposure B needs the **780 m / 20h** fetch | Direct | Classify urban Riyadh fetch with the **> 9 m** Exposure B test; default to C if the B fetch is not proven | Verified |
| 1609.5.1–1609.5.2 | Roof deck and covering | Roof deck shall withstand SBC 301 wind pressures; roof coverings shall comply with 1609.5.1. Asphalt shingles over a complying deck also comply with 1504.2 | Roof systems | Air-permeable rigid tile may use 1609.5.3 | External verification | Specify deck and covering wind resistance from SBC 301 / Chapter 15; do not import pressures here | Verified |
| 1609.5.3 | Rigid-tile uplift moment | **Ma = qh CL b L La [1.0 − GCp] / 1000**. **CL = 0.2** (or 1504.3.1 test). Point of uplift at **0.76L**. Permitted only for tiles with head lap **≥ 50 mm**, length **300–525 mm**, exposed width **200–375 mm**, tail thickness **≤ 30 mm**, and mortar/adhesive contact not more than **two-thirds** of tile area | Concrete/clay rigid tile roofs | GCp from SBC 301 Chapter 30, not adjusted for internal pressure | Conditional | If clay/concrete tile is used, stay inside the millimetre envelope and compute **Ma**; otherwise use 1609.5.1 | Verified |

## 15. Soil, hydrostatic and rain

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1610.1 / Table 1610.1 | Lateral soil load | Foundation and retaining walls shall resist Table 1610.1 minimum lateral soil loads unless a geotechnical investigation per SBC 303 determines otherwise. Restricted-top walls use at-rest pressure; free-to-rotate retaining walls may use active. Add surcharge; increase for expansive soils. Undrained backfill: full hydrostatic unless drainage per SBC 303 §§13.4.3–13.4.4. Table cells are concatenated OCR | Foundation / retaining walls | Foundation walls **not more than 2.4 m** below grade and laterally supported at the top by flexible diaphragms may use active pressure | Direct | Prefer SBC 303 pressures; if Table 1610.1 is used, verify published active/at-rest cells. Apply the **2.4 m** active-pressure exception only to qualifying basement walls | Verify source |
| 1610.2 | Uplift on below-grade floors | Basement floors, slabs on ground and similar elements below grade shall resist uplift. Upward water pressure is full hydrostatic over the entire area, measured from the underside. Expansive-soil uplift complies with SBC 303 | Below-grade floors where water/expansive soil applies | None stated beyond SBC 303 | Conditional | If a basement exists, design the slab for hydrostatic uplift from the underside and provide drainage or thickness/anchorage | Verified |
| 1611.1 | Rain load | Design each roof portion for rainwater per SBC 301 Chapter 8. Design rainfall is the **100-year 15-minute** event, other approved local rates, or **twice** the 100-year hourly rate in Figure 1611.1. **R = 0.0098 (ds + dh)** with **ds**, **dh** in mm and **R** in kN/m² on the undeflected roof | Roofs | Figure 1611.1 rainfall map is not readable as a numeric rate here. Commentary worked example is not adopted | External verification | Size primary/secondary drainage (SBC 701) then compute **R** from static + hydraulic head; do not import the commentary **2.74 kN/m²** example | Verified |
| 1611.2 | Ponding instability | Evaluate susceptible bays for ponding instability per SBC 301 Chapters 7 and 8 | Roofs with susceptible bays | Assume primary drains blocked | Direct | Provide roof slope/camber and stiffness so rain cannot progressive-pond | External verification |
| 1611.3 | Controlled drainage | Roofs with flow-control hardware shall have a higher secondary system; design for water to the secondary elevation plus the 1611.1 hydraulic head, and check 1611.2 ponding | Controlled-flow roof drains | None stated | Conditional | If controlled-flow drains are used, set the overflow elevation and the corresponding rain load | Verified |

## 16. Flood, snow, ice and tsunami

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1603.1.7 | Flood data on CDs | If the building is wholly or partly in a flood hazard area (SBC 301 §5.1), show lowest-floor elevation (including basement) and, in high-velocity wave areas, the bottom of the lowest horizontal structural member | Flood hazard areas | Non-residential dry floodproofing elevation is listed for non-wave zones | Conditional | Confirm the AHJ flood map; if not in a flood hazard area, omit 1603.1.7 data | Verified |
| 1612.1 | Flood loads | Design in flood hazard areas, coastal high-hazard areas and coastal A zones per SBC 301 Chapter 5 | Those mapped areas | Values not in this chapter | External verification | Do not import flood elevations from SBC 301 here | Verified |
| 1614.1 | Atmospheric ice | Atmospheric ice load is **inapplicable to KSA** | KSA projects | None stated | Direct | Omit ice accretion from the load-criteria sheet | Verified |
| 1615.1 | Tsunami loads | Risk Category III and IV buildings in Tsunami Design Zones (Tsunami Design Geodatabase) shall comply with SBC 301 Chapter 6 as modified | RC III/IV in a mapped tsunami zone | Not an inland Riyadh R-2 default | Not typical | Do not apply tsunami detailing unless the AHJ maps a zone and risk category is III/IV | External verification |

## 17. Earthquake

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1613.1 | Seismic scope | Every structure, including permanently attached nonstructural components and their supports and attachments, shall resist earthquake motions per SBC 301 Chapters 11, 12, 13, 15, 17 and 18 as applicable. SDC may be determined per 1613 or SBC 301 | All structures | (1) Detached one- and two-family in SDC A/B/C or **Ss < 0.4g**. (2) Agricultural storage, incidental occupancy. (3) Special structures under other regulations. (4) SBC 301 Chapter 14 references shall not apply except as specifically required. Exception 1 is not this high-rise | External verification | Design the tower and permanently attached façades/MEP per SBC 301; do not use the dwelling exception | Verified |
| 1613.2.1 | Mapped accelerations / SDC A shortcut | Determine **Ss** and **S1** from Figures 1613.2.1(1)–(2). Where **S1 ≤ 0.04g** and **Ss ≤ 0.15g**, SDC A is permitted | Site seismicity | Figures are not readable as values in this extract | External verification | SER to read published maps; do not assume SDC A for Riyadh | Verified |
| 1613.2.2 | Site class default | Classify the site as A–F per SBC 301 Chapter 20. If soil properties are not known in sufficient detail, use Site Class **D**, unless the building official or geotechnical data determine Class E or F. Class B rock without site-specific velocity: **Fa** and **Fv** = **1.0** | Site classification | Measurements over the top **30 m** | Direct | Until a geotechnical report exists, the code default is **D**, not A/B | Verified |
| 1613.2.3 / Tables 1613.2.3(1)–(2) | Site coefficients | **SMS = Fa Ss** and **SM1 = Fv S1**, but **SMS** shall not be taken less than **SM1** except when determining SDC per 1613.2.5. Default Site Class D: **Fa not less than 1.2**. Tables of **Fa** / **Fv** are concatenated OCR (the second table is titled Fa in the extract but tabulated vs **S1**). No reconstructed coefficient is adopted | Seismic ground-motion adjustment | Site Class F and some E cells are “Note b” → SBC 301 §11.4.8 | External verification | Compute **SMS** / **SM1** from published **Fa** / **Fv**; do not use flattened 1.6 / 2.4 tokens | Verify source |
| 1613.2.4 | Design spectral accelerations | **SDS = (2/3) SMS**; **SD1 = (2/3) SM1** | After site-adjusted MCER | None stated | Direct | Reduce site-adjusted accelerations by **2/3** for design | Verified |
| 1613.2.5 / Tables 1613.3.5(1)–(2) | Seismic design category | If **S1 ≥ 0.75g**: Risk Category I–III → SDC **E**; Risk Category IV → SDC **F**. Otherwise assign the more severe category from Tables 1613.3.5(1) and (2) using **SDS**, **SD1** and risk category, irrespective of period T. Table range cells (**0.167g / 0.33g / 0.50g** and **0.067g / 0.133g / 0.20g**) are concatenated OCR and are not adopted | SDC assignment | Alternative short-period determination 1613.2.5.1 where **S1 < 0.75g** and four listed conditions (including diaphragm spacing **≤ 12 m**) | External verification | Assign SDC from published tables after **SDS** / **SD1** are known; do not reconstruct the flattened A/B/C/D grid | Verify source |
| 1613.3 | Ballasted rooftop PV | Ballasted nonpenetrating PV need not be rigidly attached. Allowed only on roofs not steeper than **1:12**. Resist sliding/uplift per 1605 using an engineered friction coefficient. In SDC C–F, accommodate seismic displacement by nonlinear RHA, approved analysis or shake-table testing consistent with SBC 301 roof nonstructural forces | Ballasted nonpenetrating PV | Penetrating/attached arrays are not this exception | Conditional | If ballasted PV is used, keep roof slope **≤ 1:12** and run a sliding/displacement check | Verified |

## 18. Structural integrity

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1616.1 | Integrity charging trigger | High-rise buildings assigned to Risk Category **III or IV** shall comply with 1616.2 (frame) or 1616.3 (bearing wall) | High-rise **and** RC III or IV | Risk Category II high-rise is not charged by 1616.1 | Conditional | Apply 1616 only if risk category is III or IV; a typical RC II apartment tower is outside this section | Verified |
| 1616.2.1 | Concrete-frame integrity steel | Concrete frames conform to SBC 304 §4.10. Where that standard requires steel through the column cage, nominal tensile strength is **two-thirds** of the required one-way vertical strength of the floor/roof-to-column connection in each direction | RC III/IV high-rise concrete frames | Continuous slabs with reinforcement **≥ 0.0015** times concrete area in each orthogonal direction, monolithic or equivalently bonded: tensile strength **one-third** | Conditional | If 1616 applies, detail through-column integrity steel to **2/3** (or **1/3** with the slab exception) | Verified |
| 1616.2.2.1 | Steel-frame column splice tension | Each column splice shall have tensile design strength to transfer design dead and live load tributary to the column between that splice and the splice or base immediately below | RC III/IV high-rise steel / joist / composite frames | None stated | Conditional | If 1616 applies, check every column splice for the storey tributary D+L tension | Verified |
| 1616.2.2.2 | Steel-frame beam end ties | Beam/girder end connections: nominal axial tensile strength equal to required vertical shear (ASD) or **two-thirds** of required shear (LRFD), but not less than **45 kN**. Shear and axial tension need not act together | Those frames | Concrete slab or slab-on-deck with headed studs **≥ 10 mm** diameter at **≤ 300 mm** o.c. average, plus slab reinforcement **≥ 0.0015** in two directions: half (ASD) or one-third (LRFD) of required shear, still **≥ 45 kN** | Conditional | If 1616 applies, provide beam-end tensile capacity **≥ 45 kN** (or the reduced slab exception) | Verified |
| 1616.3.2.1–1616.3.2.2 | Bearing-wall longitudinal / transverse ties | Other-than-precast-concrete bearing-wall structures: longitudinal ties across interior load-bearing walls at not more than **3 m** centres; transverse ties at not more than the bearing-wall spacing. **TT = w L S ≤ αT S** with **αT = 22 kN/m** (masonry) or **5.5 kN/m** (cold-formed steel). ASD tensile strength may be **1.5** times allowable stress times area | RC III/IV high-rise bearing-wall structures not under 1616.3.1 | Precast concrete walls use SBC 304 §§16.2.4–16.2.5 (1616.3.1) | Conditional | If a bearing-wall III/IV high-rise is used, space longitudinal ties at **≤ 3 m** and size **TT** | Verified |
| 1616.3.2.3 | Bearing-wall perimeter ties | Perimeter ties within **1.2 m** of the edge of each floor and roof; **Tp = 90.7 w ≤ βT** with **βT = 71 kN** (masonry) or **17.8 kN** (CFS). ASD may use **1.5** times allowable stress times area | Same bearing-wall trigger | None stated | Conditional | Keep perimeter ties inside the **1.2 m** edge band | Verified |
| 1616.3.2.4 | Bearing-wall vertical ties | Continuous vertical ties over the building height; capacity not less than wall weight in the storey plus diaphragm tributary to the wall in the storey below. Not fewer than **two** ties per wall. Each tie need not exceed **44 kN/m** (masonry) or **11 kN/m** (CFS) of wall tributary to the tie | Same bearing-wall trigger | None stated | Conditional | Provide at least **two** continuous vertical ties per bearing wall | Verified |

## 19. Project-use controls

1. Use **Verified** rows for coordination after the row trigger and branch are confirmed.
2. Treat every **Verify source** row (all reconstructed appended tables, flattened **KLL** / **Fa** / **Fv** / SDC grids, and the two helipad uniform-load tokens) as a design hold point; no affected value is to be placed on issued-for-approval drawings without a published-source check.
3. Do not import mapped wind speeds, **Ss** / **S1**, live-load occupancy cells, or deflection L/n ratios from memory, CS.md, or commentary examples.
4. Do not apply ICC 600 / AWC WFCM / AISI S230 prescriptive wind provisions to this high-rise.
5. Do not apply Section 1616 integrity ties unless the building is high-rise **and** Risk Category III or IV.
6. Do not apply one- and two-family attic, dwelling-stair, or guard exceptions to this Group R-2 tower.
7. Record risk category, site class, exposure, roof use and garage class in the project Golden Thread; this matrix is not evidence of SCD NOC or stamped structural compliance.

## 20. Coverage summary

Internal inventory of the attached Chapter 16 extract (numbered code, exceptions, tables, footnotes; commentary excluded). Row-level records are not published.

- **Inventory scope:** numbered code, exceptions, tables, footnotes (commentary excluded)
- **Total independently checkable numeric records:** 437
- **Verified:** 191
- **Verify source:** 246

### Counts by top-level section

| Top-level section | Records |
|---|---:|
| 1601 | 0 |
| 1602 | 0 |
| 1603 | 0 |
| 1604 | 45 |
| 1605 | 9 |
| 1606 | 0 |
| 1607 | 209 |
| 1608 | 0 |
| 1609 | 45 |
| 1610 | 25 |
| 1611 | 3 |
| 1612 | 0 |
| 1613 | 77 |
| 1614 | 0 |
| 1615 | 0 |
| 1616 | 24 |

### Appended-table coverage

| Appended table | Records | Verify source records |
|---|---:|---:|
| Table 1604.3 (incl. footnotes a, d, f, h, i) | 29 | 29 |
| Figure/Table 1604.3.6 (concatenated after SDC tables) | 4 | 4 |
| Table 1604.5 (numeric occupancy thresholds only) | 7 | 7 |
| Table 1607.1 | 98 | 98 |
| Table 1607.12.1 | 7 | 7 |
| Table 1609.3.1 | 12 | 12 |
| Table 1610.1 | 24 | 24 |
| Table 1613.2.3(1) | 27 | 27 |
| Table 1613.2.3(2) | 30 | 30 |
| Table 1613.3.5(1) | 3 | 3 |
| Table 1613.3.5(2) | 3 | 3 |

Helipad uniform-load tokens in 1607.6 Items 1.1/1.2 (`1.12` / `1.23` concatenated with list markers) are **2** additional Verify source records, counted under Section 1607.

Coverage cross-check against `SBC 201 Chapter 16 Structural Design (2024)_CS.md` was topics-only: SBC 301 companions; risk category; mixed occupancy. No CS.md value was copied into a matrix cell.

## 21. Unresolved-source register

Hold points for the 246 **Verify source** inventory records. Counts are record counts, not distinct numeric values. No value in this register is a design-release figure.

| Affected table / clause | Why unverified | Control note |
|---|---|---|
| Table 1604.3 + footnotes | 29 flattened L/n and footnote factors (L/60, 0.42, 0.5D, aluminium L/175, etc.) | Verify published table before specifying finish-dependent deflection; do not adopt concatenated L/360 tokens |
| Figure/Table 1604.3.6 | 4 concatenated concrete-roof deflection cells mixed into the SDC page | Verify published Figure 1604.3.6; outbound SBC 304 still governs concrete |
| Table 1604.5 | 7 flattened occupant-load / care thresholds (**300**, **2,500**, **250**, **500**, **50**, **5,000** and related) | Conventional R-2 is typically II; verify published III/IV triggers before raising category |
| Table 1607.1 | 98 flattened uniform/concentrated occupancy cells across four page-splits (tokens such as `2.59`, `59`, `44.5`) | After published-table check, use multifamily private/public, balcony, stair, garage and roof rows; omit unrelated occupancies |
| Table 1607.12.1 | 7 flattened **KLL** element factors | Do not reduce live load until published **KLL** values are confirmed |
| 1607.6 Items 1.1–1.2 | 2 concatenated list-marker + kN/m² tokens (`1.12`, `1.23`) | Helipads are not typical; verify published uniform helipad loads if a pad is added |
| Table 1609.3.1 | 12 flattened V / Vasd pairs | Prefer Equation 16-16; do not read concatenated speed pairs |
| Table 1610.1 | 24 flattened active/at-rest soil pressures | Prefer SBC 303 investigation; verify published cells if the table is used |
| Tables 1613.2.3(1)–(2) | 57 flattened **Fa** / **Fv** cells (second table title OCR as Fa) | Verify published coefficients; default Class D still requires **Fa ≥ 1.2** from code text |
| Tables 1613.3.5(1)–(2) | 6 flattened SDC range bounds | Verify published **SDS** / **SD1** grids before assigning SDC A–D |
