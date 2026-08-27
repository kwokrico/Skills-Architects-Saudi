# SBC 201 Chapter 10 Means of Egress — Group R-2 High-Rise Dimensional Requirements Matrix (2024)

## 1. Document metadata and use limitation

- **Project basis:** Riyadh, Saudi Arabia; Group R-2 residential high-rise; an occupied floor is stated to be more than 23 m above the relevant reference level.
- **Deliverable tier:** Project-use matrices in Sections 1–20 (design-check rows, not pasted inventory), plus a coverage summary and unresolved-source register. The full row inventory is not published.
- **Code/source basis:** SBC 201 (2024), Chapter 10, source file `Reference\SBC 201 2024\source_reference\Chapter_10 — MEANS OF EGRESS.txt`.
- **Extraction audit:** Skill-finetune re-run. Project-use rows follow the chapter-extract row contract (noun-phrase checks, bold SI values, building-language triggers, named exceptions, check-specific actions). Internal inventory: **645** independently checkable numeric records (**557** Verified, **88** Verify source). Unresolved OCR is listed in the register and is not a design-release value. Pre-skill baseline retained as `…_Cursor-Grok-4.6-pre-skill.md`.
- **Model:** Cursor Grok 4.6.
- **Prepared:** 2026-08-27.
- **Status:** Source-only architectural advisory matrix for design coordination. It is not a stamped compliance statement, fire-engineering report, SCD NOC, SBPS approval, legal opinion, or permission to construct.
- **Outbound-source rule:** No value in this matrix has been imported from an outbound code, standard, commentary example, or the existing chapter summary. Where Chapter 10 sends the user elsewhere, this matrix records the dependency without supplying the outbound value.

### Scope and assumptions

1. Group R-2 and high-rise status are project statements, not independently verified classifications.
2. The exact Riyadh AHJ/permit pathway, project stage, fire-strategy status and SCD NOC status are unconfirmed; therefore this matrix does not conclude compliance.
3. Automatic sprinkler protection is not selected. **NFPA 13 / Section 903.3.1.1** and **NFPA 13R / Section 903.3.1.2** are shown as separate branches wherever Chapter 10 differentiates or jointly recognizes them.
4. Emergency voice/alarm communication system (EVACS) compliance with Section 907.5.2.2 is unconfirmed.
5. Building height, storey count, grade plane, accessible floors and occupied-roof configuration, level(s) of exit discharge, unit type, occupant loads, mixed uses and amenity layouts are unconfirmed.
6. Table 1004.5 Residential, Table 1006.2.1, Tables 1006.3.4(1)/(2), Table 1017.2 and both OCR-labelled Table 1020.2 extracts contain source segmentation or footnote uncertainty. Their affected rows are marked **Verify source** and are not design release values.
7. Accessibility technical geometry cross-referenced to Chapter 11/ICC A117.1, fire-protection systems in Chapter 9, high-rise provisions in Section 403, smokeproof-enclosure systems in Section 909.20, and other outbound standards require separate verification.

## 2. Legends

### Applicability

| Status | Meaning |
|---|---|
| **Direct** | Expected to govern the stated R-2 tower basis, subject to confirmed geometry and design data. |
| **Conditional** | Governs only when the stated feature, use, occupant load, sprinkler branch or exception exists. |
| **Not typical** | Not expected in a conventional R-2 tower, but retain if the feature appears in podium, amenity, roof or mixed-use areas. |
| **External verification** | Chapter 10 points to another section/code/standard, or the project/AHJ basis must be confirmed before use. |

### Source confidence

| Status | Meaning |
|---|---|
| **Verified** | Requirement and any stated numeric value were checked against unambiguous mandatory Chapter 10 source text or an unambiguous table cell. |
| **Verify source** | OCR, flattened table, page-split, or footnote attachment is unresolved. Not a design-release value. |

## 3. Project decision and gap register

| Decision / gap | Current project basis | Why it controls Chapter 10 application | Required project action |
|---|---|---|---|
| Sprinkler basis | Unconfirmed: neither NFPA 13 nor NFPA 13R is assumed | Controls capacity reductions, separation, common path, travel-distance table branch, dead ends, accessible-egress exceptions and corridor table branch | Fire engineer and code consultant to lock the Chapter 9 system and record whether Section 903.3.1.1 or 903.3.1.2 applies; verify high-rise permissibility outside Chapter 10 |
| EVACS | Unconfirmed | Reduced stair capacity factor requires both qualifying sprinklers and Section 907.5.2.2 EVACS | Fire alarm designer to confirm EVACS scope and cause/effect; until then retain base capacity factors |
| Storeys and height | Occupied floor stated above 23 m; exact height, grade plane and storey count unconfirmed | Controls high-rise outbound provisions, accessible-egress elevator trigger, enclosure rating, roof access and stair signs | Issue a signed code datum sheet with grade plane, building height, occupied-floor elevations, basements, mezzanines and storey count |
| Per-storey occupant load | Unconfirmed | Controls number of exits/accesses to exits and cumulative stair/discharge sizing | Produce a storey-by-storey occupant-load and egress-routing schedule |
| Per-space occupant load | Unconfirmed | Controls one-door logic, common path, door swing, panic hardware and assembly rules | Produce a room/space load schedule using actual function, net/gross basis and layout |
| Unit type | Unconfirmed: dwelling units versus sleeping units | Controls Tables 1006.3.4(1)/(2), internal door exceptions and single-exit logic | Classify every R-2 unit type and show the applicable table branch on life-safety plans |
| Podium and mixed uses | Detailed uses unconfirmed | Shared egress must satisfy the most stringent served occupancy; residential rules cannot be applied to retail, parking, business or assembly by default | Freeze occupancy/use by room and fire area; identify every shared egress component |
| Amenity assembly | Configuration, fixed seating and occupant load unconfirmed | Triggers Table 1004.5 assembly factors, Section 1030 aisle/seating rules, possible main-exit provisions and occupant-load posting | Classify each lounge, multipurpose room, gym, pool deck, cinema and roof amenity by actual function and seating arrangement |
| Accessible floors and occupied roof | Unconfirmed | Controls number and components of accessible means of egress and the four-storey elevator trigger | Accessibility consultant to map all required accessible floors/roof and the complete route to a public way |
| Level of exit discharge | Unconfirmed, including possible multiple discharge levels | Controls elevator trigger datum, stair termination, discharge exceptions, accessible discharge and convergence | Mark each level of exit discharge in section and trace every exit independently to the public way |
| NOC and fire strategy | SCD NOC and stamped fire-strategy status unconfirmed | Authority acceptance, smoke control, active systems, assisted evacuation and high-rise strategy cannot be concluded from Chapter 10 alone | Engage the qualified local/fire consultant; align life-safety drawings, fire strategy, SBPS submission and SCD comments before design freeze |

## 4. General egress baseline

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1003.2 | General egress ceiling height | Means of egress ceiling height **not less than 2300 mm** above finished floor | All egress components | Dwelling/sleeping-unit ceilings, stair headroom, door height, ramp headroom and other listed cases are separately controlled | Direct | Coordinate reflected ceilings, services and signage to preserve the applicable clear height | Verified |
| 1003.3.1 | Protruding-object headroom | Minimum headroom **2000 mm** over circulation paths; not more than **50%** of the egress ceiling area may be reduced | Protrusions below the general ceiling height | Door closers and stops may reduce headroom only to **2000 mm** | Direct | Model clear headroom along all walking lines, not only corridor centerlines | Verified |
| 1003.3.1 | Low-headroom barrier | Barrier required where clearance is less than **2000 mm**; leading edge **700 mm maximum** above floor | Any low-clearance circulation path | No numeric branch stated | Direct | Detail cane-detectable protection below stairs and services | Verified |
| 1003.3.2–1003.3.3 | Protruding objects | Post-mounted overhang maximum **100 mm** where leading edge is over **700 mm** and under **2000 mm**; where post spacing exceeds **300 mm**, obstruction bottom is **700 mm maximum or 2000 mm minimum**; horizontal projection maximum **100 mm** between **700–2000 mm** high | Object projects into a circulation path | Handrail exception permits **115 mm** projection; sloping handrail portions between stair/ramp endpoints are excepted as stated | Direct | Audit wall- and post-mounted signs, cabinets and equipment against cane/head zones | Verified |
| 1003.5 | Elevation changes | Changes under **300 mm** use a sloped surface; slopes over **1:20 (5%)** use a 1012 ramp; change **150 mm or less** requires handrails or contrasting floor finish | Elevation change in means of egress | Listed nonaccessible exceptions include a single riser or two risers with **325 mm minimum tread** and at least one handrail within **750 mm** of travel centerline | Direct | Eliminate isolated steps from common egress; document any exact exception | Verified |
| 1003.6 | Egress continuity | Path shall not be interrupted; minimum width or required capacity shall not diminish along travel | Entire exit access, exit and exit discharge | Only Chapter 10 permitted projections/components | Direct | Trace the controlling width continuously to the public way | Verified |

## 5. Occupant load and capacity

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1004.2.1 | Cumulative load through intervening spaces | Capacity is based on the combined occupant load of interconnected accessory/intervening spaces to each point along the path | Occupants egress through another room/area/space | Do not double-count occupants with independent routes | Direct | Build a cumulative load tree for lobbies, corridors and discharge paths | Verified |
| 1004.2.3 | Loads from adjacent stories | Occupant loads from separate stories are **not added**, except for convergence under 1005.6 | Vertical egress sizing by story | Mezzanine loads and convergence follow their own rules | Direct | Size story egress separately, then test convergence | Verified |
| 1004.3 | Multiple functions in one area | Calculate each function independently using its applicable occupant-load factor | Mixed-function amenity or podium space | Net areas are removed before applying a gross-area factor to the balance | Conditional | Zone each actual function on the occupant-load plan | Verified |
| 1004.4 | Multiple occupancies | Apply means-of-egress rules to each occupancy portion; shared components meet the most stringent requirement of occupancies served | Podium or mixed-use tower | No residential default for shared paths | Conditional | Tag shared corridors, stairs and discharge with all served occupancies | Verified |
| 1004.7 | Outdoor areas and occupied roofs | Building official assigns occupant load from anticipated use. Where additional persons use a yard, patio, occupied roof, court or similar area and its egress passes through the building, building egress is based on the **sum of building and outdoor-area occupant loads** | Outdoor area accessible to and usable by building occupants | The aggregation rule does not apply to outdoor areas associated with an individual Group R-2 dwelling unit; service-only outdoor areas need only one means | Conditional | Include shared roof/terrace amenity loads in the cumulative route; keep private unit balconies/patios on the stated exception branch | Verified |
| Table 1004.5 | Areas without fixed seating | Occupant load is not less than floor area divided by the factor for the function of space | Every non-fixed-seat space | Building official may approve actual load lower than calculated; approval is required | Direct | Record factor, net/gross basis, area and rounded load per space | Verified |
| Table 1004.5 | Residential factor | Residential row exists, but numeric factor and gross/net basis cannot be unambiguously segmented from the OCR table | R-2 dwelling/sleeping areas | No numeric value is adopted in this tier | External verification | Verify published Table 1004.5 before calculating residential loads | Verify source |
| Table 1004.5 | Likely tower support functions | Business **14 m² gross/person**; commercial kitchen **19 m² gross/person**; exercise room **4.6 m² gross/person**; parking garage **19 m² gross/person**; accessory storage/mechanical **28 m² gross/person** | Where those actual functions occur | Use actual function, not the overall R-2 group label | Conditional | Apply only to mapped rooms with matching functions | Verified |
| Table 1004.5 | Assembly amenity factors | Standing **0.46 m² net/person**; concentrated chairs only **0.65 m² net/person**; unconcentrated tables/chairs **1.4 m² net/person** | Amenity used for assembly without fixed seating | Pools/decks rows remain OCR-unresolved and are not supplied here | Conditional | Test every intended furniture/event layout and use the governing load | Verified |
| 1004.5.1 | Increased occupant load | Modified load permitted if all other code requirements use it and density does not exceed **1 person per 0.65 m²** of occupiable floor space | Designer/owner proposes higher load | All affected provisions must use modified load | Conditional | Record the approved design load consistently across all disciplines | Verified |
| 1004.6 | Fixed seating | Without dividing arms: **1 person per 450 mm** of seating length; booths: **1 person per 600 mm** measured at backrest | Fixed seating in amenity/assembly areas | Wheelchair and companion spaces each count as one occupant | Conditional | Count seats and continuous benches from the actual seating plan | Verified |
| 1004.8 | Concentrated business | Approved actual load, but not less than **1 person per 4.65 m² gross** | Call centres, trading floors, data-processing centres and similar dense business uses | Building-official approval required | Conditional | Apply only if such a podium/management use is confirmed | Verified |
| 1005.3.1 | Base stair capacity | Stair capacity = served occupant load × **7.6 mm/person** | All stairs unless an exception is proven | Assembly seating has separate listed branches | Direct | Retain base factor until sprinkler and EVACS evidence is locked | Verified |
| 1005.3.1 Ex. 1 | Reduced stair capacity | **5.08 mm/person** | Other than H/I-2, and building throughout has Section 903.3.1.1 **or** 903.3.1.2 sprinklers **and** Section 907.5.2.2 EVACS | NFPA 13 and NFPA 13R both satisfy the Chapter 10 sprinkler wording; EVACS is additionally mandatory | Conditional | Do not use reduced factor unless both system conditions are documented | Verified |
| 1005.3.2 | Base non-stair capacity | Other egress component capacity = served load × **5.08 mm/person** | Doors, corridors, ramps and other non-stair components | Reduced-factor Exception 1 is OCR-corrupted | Direct | Use **5.08 mm/person**; do not infer a reduced value | Verified |
| 1005.3.2 Ex. 1 | Reduced non-stair capacity | Mandatory OCR is corrupted; numeric factor is not recoverable from the supplied extract | Proposed reduced non-stair factor | No value adopted from commentary or outbound source | External verification | Verify the published clause before any reduction | Verify source |
| 1005.6 | Egress convergence | After convergence from stories above/below, provide the larger of the largest minimum width or the sum of required capacities for the two adjacent stories | Stairs/ramps converge at an intermediate level | Limited to the two adjacent stories described | Conditional | Check podium/ground convergence before fixing lobby width | Verified |
| 1005.7 / 1005.7.1–1005.7.3 | Encroachments and projections | Fully opened door reduces required width by maximum **175 mm**; door in any position by maximum **one-half**; other trim/decorative projection maximum **40 mm each side**; protruding objects comply with 1003.3 | Door, hardware or projection enters required egress width | Surface latch hardware exception requires mounting **850–1200 mm** high and stated orientation; door-swing restriction does not apply inside individual R-2 dwelling/sleeping units | Direct | Overlay all door swings and wall projections on net-width plans | Verified |

## 6. Exit counts and loss-of-exit capacity

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1006.2.1 | Space-level two-way-out trigger | Provide **two exits or exit access doorways from a space** where occupant load or common path exceeds Table 1006.2.1 | Applied to each room/space | Mechanical penthouse common-path measurement and other listed exceptions | Direct | Check each unit, amenity, plant and tenant space independently | Verified |
| 1006.2.1.1 | Large-space exit count | Space load **501–1,000: 3** exits/access doorways; **greater than 1,000: 4** | Individual space exceeds 500 occupants | Separate from story-level Table 1006.3.3 | Conditional | Apply to large podium/amenity spaces if present | Verified |
| 1006.3 / 1006.3.1 | Stories and occupied roofs | Number of separate and distinct exits/accesses is based on aggregate load served; where stairs serve multiple stories or a story and occupied roof, use each story or occupied-roof load **individually** to calculate its required exits/accesses | Every story and occupied roof | Mezzanine and convergence rules remain separate | Direct | Add each occupied roof as its own line in the exit-count schedule | Verified |
| Table 1006.3.3 | Story/occupied-roof exit count | Load **1–500: 2**; **501–1,000: 3**; **more than 1,000: 4** exits or accesses to exits | Each story **and occupied roof** | Single-exit permissions under 1006.3.4 are separate exceptions; required count is maintained to exit discharge/public way | Direct | Schedule roof and story counts independently from every space/unit check | Verified |
| 1006.3.4 Item 5 | Unit-level one-door logic | An individual single- or multistorey dwelling unit may have a single exit/access if it complies with 1006.2.1 and, outside the unit entrance, access is to at least **two approved independent exits**, unless the unit exit discharges directly outside at the level of discharge | Individual dwelling unit | This permission does **not** reduce the required number of exits from the story | Conditional | Show one unit entrance door and two independent story exits as separate checks | Verified |
| Table 1006.2.1 | R-2 one-door space limit | OCR/inventory reads maximum **20 occupants** and sprinklered common path **38 m**; unsprinklered branch reads Not Permitted | R-2 room/space with one exit access doorway | Table note recognizes Section 903.3.1.1 or 903.3.1.2; table segmentation requires published-source check | Conditional | Treat as a hold point; verify table before relying on a one-door unit/space | Verify source |
| Table 1006.3.4(1) | Single-exit R-2 dwelling story | OCR/inventory reads basement through third story above grade: maximum **4 dwelling units** and **38 m** travel | R-2 consisting of dwelling units | Requires Section 903.3.1.1 or 903.3.1.2 sprinklers and Section 1031 EEROs; fourth story and higher reads Not Permitted | Conditional | High-rise residential floors should retain multiple story exits; verify low podium/residential levels separately | Verify source |
| Table 1006.3.4(2) | R-2 sleeping-unit story branch | Table is for R-2 sleeping units; inventory rows are flattened and upper stories read single exit Not Permitted from the third story and higher | R-2 consisting of sleeping units | Exact row/occupancy attachment requires published-source check | Conditional | Confirm unit type; do not transpose dwelling-unit limits to sleeping units | Verify source |
| 1005.5 | Exit-loss check | Remaining capacity/width after loss of one exit must be at least **50%** required | Any floor/space requiring multiple exits | Applies alongside exit-count minimums | Direct | Distribute capacity so one oversized/critical exit does not fail the system | Verified |

## 7. Common path, exit access travel and exit separation

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| Table 1006.2.1 | R-2 common path | OCR/inventory reads **38 m** with qualifying sprinklers and Not Permitted without | One-door R-2 space branch | Note a recognizes Section 903.3.1.1 or 903.3.1.2; table OCR requires verification | Conditional | Verify published table and measure from the most remote point to choice of two routes | Verify source |
| Table 1017.2 | Group R exit access travel | Flattened OCR row for A/E/F-1/I-1/M/R/S-1 reads **“60° / 75°”**; limits/footnote markers are unresolved | Total exit access travel for Group R | Sprinkler footnote references Section 903.3.1.1 or 903.3.1.2 | External verification | Do not use 60/75 as released design criteria until published table is checked | Verify source |
| 1017.3 | Measurement to exit | Where more than one exit is required, measure travel distance to the nearest exit | Multiple exits required | Listed special measurement exceptions | Direct | Show measured travel paths, not straight-line radii | Verified |
| 1007.1.1 | Two-exit remoteness — base | Separation at least **one-half** the maximum overall diagonal of the building/area served | Two exits/access doorways/stairs/ramps required | Straight-line measurement unless corridor method applies | Direct | Dimension the governing diagonal and exit separation on each plan | Verified |
| 1007.1.1 | Two-exit remoteness — sprinkler branch | Separation may be at least **one-third** the maximum overall diagonal | Building throughout sprinklered under 903.3.1.1 **or** 903.3.1.2 | No selection between NFPA 13 and 13R within this Chapter 10 clause | Conditional | Use one-third only after sprinkler basis is formally fixed | Verified |
| 1007.1.1 | Interconnected/scissor stairs | Interlocking or scissor stairways count as **one exit stairway** | Scissor/interlocking core proposed | Does not supply two required exits by itself | Conditional | Do not count two flights in one scissor enclosure as two exits | Verified |
| 1007.1.1 | Corridor separation measurement | For stairs/ramps interconnected by a **1-hour** corridor complying with 1020, measure along the shortest direct line within the corridor | Rated interconnecting corridor arrangement | Corridor must satisfy the stated protection | Conditional | Identify exact measurement method in fire strategy | Verified |
| 1007.1.2 | Three-or-more exits | At least two of three or more required exits/access doorways must satisfy 1007.1.1 remoteness | Story/space requires 3 or 4 exits | Remaining exits still must be arranged to remain available | Conditional | Flag the remote pair in the egress schedule | Verified |
| 1020.5 | Dead end — base | Where more than one exit/access doorway is required, dead-end corridor maximum **6 m** | Multiple-exit condition | Geometric exception where dead end is less than **2.5 ×** least corridor width | Direct | Use 6 m unless a listed exception is demonstrated | Verified |
| 1020.5 Ex. 2 | Dead end — NFPA 13 branch | Group R-2 dead-end corridor maximum **15 m** | Building throughout sprinklered under **903.3.1.1 only** | NFPA 13R / 903.3.1.2 is not listed in this exception | Conditional | Keep separate 13 and 13R plan checks; do not give 13R the 15 m allowance | Verified |
| 1017.2.1 | Exterior egress balcony increase | Table 1017.2 travel may increase by up to **30 m** where the last portion occurs on a 1021-compliant exterior egress balcony | Exterior egress balcony used | Base Table 1017.2 value still requires verification | Conditional | Treat only as a documented alternative after balcony compliance and base limit are verified | Verified |

## 8. Accessible means of egress

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1009.1 | Minimum accessible means | Accessible spaces require at least **one accessible means of egress** | Any required accessible space | Accessible mezzanine and assembly exceptions listed | Direct | Map a continuous accessible egress path to the public way | Verified |
| 1009.1 | Multiple accessible means | Where more than one means of egress is required from an accessible space, each accessible portion requires at least **two accessible means of egress** | 1006.2/1006.3 requires multiple means | Assembly ramped/stepped-aisle exception may allow one when common path is accessible and satisfies 1030.8 | Direct | Identify the two independent accessible options on every applicable floor | Verified |
| 1009.2 | Permitted components | Components include accessible routes, compliant interior/exterior/exit-access stairs, elevators, platform lifts, horizontal exits, ramps, areas of refuge and exterior assisted-rescue areas | Building the complete accessible route | Each component must satisfy its cited section and outbound accessibility scoping | Direct | Create a component-by-component accessible egress diagram | Verified |
| 1009.2.1 | Elevator trigger | Where a required accessible floor or occupied roof is **four or more stories above or below** a level of exit discharge, at least **one required accessible means** shall be a 1009.4 elevator | Four-storey vertical separation | OCR duplicated wording in one exception; base requirement is clear but inventory remains flagged | Conditional | Reserve an accessible-egress elevator strategy unless an exception is proven | Verify source |
| 1009.2.1 Ex. 1 | Elevator exception — horizontal exit | Elevator not required on floors at/above discharge that have a horizontal exit | Building throughout sprinklered under 903.3.1.1 **or** 903.3.1.2 | Does not apply to floors below discharge | Conditional | Demonstrate horizontal-exit refuge, capacity and discharge before using exception | Verify source |
| 1009.2.1 Ex. 2 | Elevator exception — ramp | Elevator not required on floors provided with a 1012-compliant ramp | Building throughout sprinklered under 903.3.1.1 **or** 903.3.1.2 | Ramp must serve the applicable levels | Conditional | Apply only to an actual continuous ramp solution | Verify source |
| 1009.3.2 | Accessible-egress stair width | Clear width **1200 mm minimum between handrails** | Stair used as accessible means of egress | Width not required with 903.3.1.1 or 903.3.1.2 sprinklers, or from refuge area with horizontal exit | Conditional | Check clear width between handrails separately from nominal stair width | Verified |
| 1009.3.3 Ex. 5 | R-2 stair area of refuge | **Areas of refuge are not required at stairways in Group R-2 occupancies** | Stair forms part of an accessible means of egress in R-2 | This is only an area-of-refuge exception; it does **not** remove the accessible-means-of-egress requirement or the accessible route to the stair/elevator | Conditional | Continue to provide the required accessible means, stair access and other applicable communication/elevator components | Verified |
| 1009.6.3 | Area-of-refuge wheelchair spaces | One **750 × 1300 mm** wheelchair space per **200 occupants or portion** served | Area of refuge provided/required | Other protection and communication provisions also apply | Conditional | Lay out spaces without reducing egress width | Verified |
| 1009.7.2–1009.7.4 | Exterior assisted-rescue area | Separation **1 hour**; rated wall extends **3000 mm** vertically and **3 m** horizontally each side, or **1200 mm** perpendicular alternative; other sides at least **50% open**; stair **1200 mm** clear between handrails | Exterior assisted-rescue option at level of discharge | Rating/width exceptions where throughout sprinklered under 903.3.1.1 or 903.3.1.2 | Conditional | Coordinate façade exposure, opening protection and landing geometry | Verified |
| 1009.8 | Two-way communication | Provide at each elevator/bank landing on each accessible floor **one or more stories above or below** discharge | Accessible elevator landings | Areas of refuge, ramps, service/freight/private residence elevators and listed institutional cases have exceptions | Conditional | Include devices, signage, monitoring location and power/interface in fire strategy | Verified |

## 9. Illumination and signs

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1008.2 | Illumination while occupied | Means of egress serving a room/space is illuminated whenever occupied | Occupied room or space | **Dwelling units and sleeping units in Group R-2 are excepted** from this continuous-illumination rule; the exception does not extend to required common egress outside the unit | Direct | Separate in-unit lighting controls from continuously available common egress lighting | Verified |
| 1008.2.1 | Normal common-egress illumination | At least **11 lux** at walking surface | Required common means of egress outside the excepted R-2 dwelling/sleeping unit | Assembly performance exception is separate | Direct | Put 11-lux minimum on common corridors, exits and discharge criteria | Verified |
| 1008.2.1 | Common stair illumination | At least **110 lux** at walking surface on exit-access stairs, exit stairs and required landings when in use | Required common stairs outside the excepted R-2 dwelling/sleeping unit | Assembly performance reduction may reach **2.2 lux** only with automatic restoration and listed conditions | Direct | Coordinate normal controls so common stairs meet 110 lux when used | Verified |
| 1008.3.2 | Emergency-illuminated components | Emergency system automatically illuminates interior exit-access stairs/ramps, interior/exterior exit stairs/ramps, exit passageways, discharge vestibules/areas and exterior exit landings | Building requires two or more exits/accesses | Listed component scope is cumulative | Direct | Include the complete route, not only stairs and exit signs | Verified |
| 1008.3.3 Item 5 | Large public-restroom emergency lighting | Public restrooms over **28 m²** are automatically illuminated by the emergency electrical system upon power failure | Public restroom area exceeds 28 m² | Other listed emergency-response rooms have no dimensional trigger in this clause | Conditional | Add qualifying public restrooms to emergency-lighting schedules and calculations | Verified |
| 1008.3.4 | Emergency duration | Emergency power for at least **90 minutes** | Emergency egress lighting | Batteries, unit equipment or on-site generator permitted | Direct | Coordinate 90-minute basis with electrical schedule | Verified |
| 1008.3.5 | Initial emergency level | Average at least **11 lux**, minimum at any point **1 lux** at floor level along path | Emergency power starts | No project-specific reduction | Direct | Verify average and point minimum by calculation | Verified |
| 1008.3.5 | End-of-duration level | May decline to average **6 lux**, point minimum **0.6 lux** at end of duration | At 90-minute endpoint | Applies only at end of emergency-lighting duration | Direct | Include depreciation/end-duration check | Verified |
| 1013.1 | Exit-sign spacing | No point in exit-access corridor or exit passageway more than **30 m** or listed viewing distance, whichever is less, from visible sign | Direction to exit not readily apparent | Signs not required inside individual R-2 sleeping/dwelling units; one-exit rooms and obvious approved main exterior exits also listed | Direct | Prepare sign visibility/spacing plan outside units | Verified |
| 1013.6.1–1013.6.3 | Exit-sign graphics and power | Letters at least **150 mm** high with **20 mm** strokes; “EXIT” letter width at least **50 mm** except I, spacing at least **10 mm**; externally lit face at least **55 lux**; backup at least **90 minutes** | Exit/directional sign required | Approved self-powered sign may satisfy stated 90-minute exception | Direct | Coordinate sign schedule and photometrics | Verified |
| 1023.9–1023.9.1 | Stair identification sign | Required at each landing when stair/ramp connects more than **3 stories**; bottom at least **1500 mm** above landing; sign at least **450 × 300 mm**, stair ID **40 mm**, floor number **125 mm**, other text **25 mm** | High-rise interior exit stair/ramp | Tactile sign requirements are separately cross-referenced | Direct | Issue a consistent stair-sign family and location detail | Verified |

## 10. Doors, gates and turnstiles

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1010.1.1 | Door clear opening | Capacity-sized and at least **800 mm clear width**; minimum clear height **2000 mm** | Required egress door | R-2 internal nonaccessible-unit exceptions exist; Type B user-passage doors remain **800 mm** | Direct | Schedule clear opening, not nominal leaf size | Verified |
| 1010.1.1 | Swing-door measurement | Measure between door face and stop with door at **90 degrees**; one leaf of a pair without mullion must provide **800 mm** clear | Swinging/pair doors | Listed special doors have separate provisions | Direct | Dimension clear width at 90 degrees in door details | Verified |
| 1010.1.2.1 | Direction of swing | Door swings in egress direction for room/area load **50 or more**, or Group H | Threshold met | Unit entrance below threshold is not automatically required by this clause to swing out | Conditional | Link each door swing to served room load | Verified |
| 1010.1.3 | Door operating forces | Push/pull unlatching maximum **67 N**; rotational unlatching maximum **3.15 N-m**; manually operated interior swinging non-fire-rated egress door opening maximum **22 N**; other, sliding, folding and fire-rated doors maximum **133 N** to set in motion and **67 N** to full-open | Manually operated egress door | Power-operated doors are addressed separately; forces are applied at latch side under 1010.1.3.1 | Direct | Put force criteria in hardware specification and commissioning checks | Verified |
| 1010.1.5 | Door landing | Landing length in travel direction at least **1100 mm**; fully open door may reduce required dimension by no more than **175 mm** | Egress door landing | Within individual R-2 units, landing length need not exceed **900 mm** | Direct | Check both open and closed door positions | Verified |
| 1010.1.6 | Threshold — base | Sliding doors serving dwelling units maximum **20 mm**; other doors maximum **12.5 mm**; changes over **6 mm** bevel no steeper than **1:2 (50%)** | Doorway threshold | Exceptions below are narrowly scoped | Direct | Use the base limits for required egress and accessible doors | Verified |
| 1010.1.6 Ex. 1 | R-2 exterior threshold | Sliding or side-hinged exterior threshold may be up to **200 mm** only where the door is **not** part of required egress, **not** part of a Chapter 11 accessible route, and **not** part of an Accessible, Type A or Type B unit | Group R-2 or R-3 exterior door meeting all three conditions | Failure of any condition returns the door to the base limits | Conditional | Identify the nonrequired, nonaccessible door and unit type before using 200 mm | Verified |
| 1010.1.6 Ex. 2 | Type B exterior-side threshold | Where 1010.1.4 Ex. 5 permits a **100 mm** exterior level change, exterior-side threshold maximum is **120 mm** above deck/patio/balcony for sliding doors and **115 mm** for other doors | Exterior door of Type B unit under the cited level-change exception | These are exterior-side measurements; base interior-side limits and beveling still apply | Conditional | Detail both interior and exterior threshold datums | Verified |
| Unnumbered — commentary indicates 1010.1.7 | Doors in series / vestibule | Space between two doors in series is **1200 mm minimum plus the width of a door swinging into the space**; doors swing in the same direction or away from the intervening space | Successive doors/vestibule on an egress path | Horizontal sliding power doors: **1200 mm** minimum; R-2/R-3 unit storm/screen doors need not be spaced 1200 mm; doors within R-2/R-3 dwelling units are excepted **other than within Type A dwelling units** | Conditional | Dimension vestibules beyond the full door swing; apply unit exceptions only at their exact scope | Verify source |
| 1010.2.1 | Unlatching | Not more than **one motion** in one linear/rotational direction to release latching/locking devices | Egress side of doors | Group R unit security devices are a listed exception under 1010.2.4 Item 5 | Direct | Coordinate hardware sets for single-action egress | Verified |
| 1010.2.3 | Hardware height | Operating devices **850–1200 mm** above finished floor | Egress doors/gates | Pool/spa barrier latch exception up to **1350 mm** under stated conditions | Direct | Put range in hardware specification | Verified |
| 1010.2.4 Item 5 | R-unit security | Group R dwelling/sleeping-unit doors serving load **10 or less** may have night latch, dead bolt or security chain if openable inside without key/tool | Individual unit | Does not waive one-motion/safe-egress intent beyond stated permission | Conditional | Confirm unit occupant load and free-egress operation | Verified |
| 1010.2.9 | Panic hardware | Group A/E rooms/spaces with load **50 or more** require panic/fire-exit hardware; Group H also listed | Assembly amenity or mixed-use trigger | Main-exit and electrical locking exceptions are listed | Conditional | Check amenity and podium doors by actual occupancy/load | Verified |
| 1010.2.11 Item 2 | Hardware-released electric lock | Door-mounted release hardware is operable with **one hand** and complies with 1010.2.1 | Door-hardware release electric locking system, except Group H | All listed release and power-loss criteria remain cumulative | Conditional | Coordinate the hardware set and single-hand operation with the electrical lock release | Verified |
| 1010.2.12 | Sensor-released lock | Manual release at **1000–1200 mm** high and within **1500 mm** of secured doors; direct power interruption; unlock at least **30 seconds** | Sensor-released electrically locked egress door | Fire alarm, sprinkler/detection and power-loss release conditions also required | Conditional | Coordinate access control with fire alarm and emergency lighting | Verified |
| 1010.2.13 / 1010.2.13.1 | Delayed egress | General path maximum **one delayed-egress system**; irreversible release within **15 seconds** after no more than **3 seconds** applied effort; approved delay may be **30 seconds** | Delayed-egress locking system serving Group R or another listed occupancy with required sprinkler/detection prerequisite | Institutional two-device exceptions are NOT_TYPICAL and capped at **30 seconds combined** | Conditional | Treat delayed egress as a fire-alarm, access-control, emergency-lighting and signage package; obtain approval for any 30-second branch | Verified |
| 1010.2.13.1 Item 6 | Delayed-egress sign | Sign above and within **300 mm** of exit hardware; PUSH/PULL legend states opening in **15 [30] seconds** according to door swing | Delayed-egress door | Group I sign omission is a separate clinical exception | Conditional | Put exact legend, location and approved delay on the door/hardware schedule | Verified |
| 1010.3.1 | Revolving door | Breakout aggregate width at least **900 mm**; side-hinged 1010.1 door in same wall within **3000 mm**; revolving door not on accessible route | Revolving entrance proposed | Egress credit limited to **50%** and **50 persons** per door under 1010.3.1.1 | Conditional | Prefer compliant side-hinged egress doors as the dependable route | Verified |
| 1010.5.1 | Conventional turnstile | Credit maximum **50 persons** and no more than **50%** required capacity; device max **990 mm** high; clear width **420 mm** up to 990 mm high and **550 mm** above | Turnstile used for egress credit | Must free-turn on power loss/manual release | Conditional | Keep at least half capacity independent of turnstiles | Verified |
| 1010.5.1.1 | Accessible-route turnstile | Clear width at least **900 mm** at/below **850 mm** high and at least **800 mm** between **850–2000 mm**; mechanism is not revolving | Turnstile lies on an accessible route | Accessibility geometry and approach remain separately controlled | Conditional | Provide a compliant nonrevolving accessible lane and dimension both height branches | Verified |
| 1010.5.2 | Security access turnstile | Lane minimum **550 mm**; lane under **800 mm** credited maximum **50 persons**; lane **800 mm or more** sized under Section 1005 | Approved supervised 903.3.1.1 sprinklered building and listed release conditions | Requires automatic unobstructed opening on specified events | Conditional | Use only with NFPA 13 branch and coordinated fail-safe release | Verified |
| 1010.5.4 | Turnstile companion door | For served load over **300**, side-hinged compliant door within **15 m** | Nonportable turnstile | Exception for compliant 1010.5.2 security turnstiles | Conditional | Include companion door in lobby planning if trigger is met | Verified |

**Door-arrangement numbering hold point:** the supplied Chapter 10 text omits the section number before “Door arrangement”; its commentary identifies **1010.1.7**. The mandatory values are retained under the citation **Unnumbered — commentary indicates 1010.1.7**, and the published section number remains a verification hold point.

## 11. Stairs

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1011.2 | Minimum width | Capacity-sized under 1005 and at least **1100 mm** | General stair | Stair serving fewer than **50** occupants may be **900 mm**; accessible-egress clear width is separate | Direct | Use the larger of capacity, 1100 mm and accessible-egress requirement | Verified |
| 1011.3 | Headroom | At least **2100 mm** vertically from nosing line, continuous to one tread beyond bottom riser | General stair | Spiral stair **2000 mm**; limited R-2 in-unit projection exception **120 mm** | Direct | Check soffits, landings and underside of flights in section | Verified |
| 1011.5.2 | Public/common riser and tread | Riser **100–175 mm**; rectangular tread at least **275 mm** | Common/public tower stairs | Assembly stepped aisles and listed special stairs separate | Direct | Apply to exit stairs and common circulation stairs | Verified |
| 1011.5.2 Ex. 3 | Inside individual R-2 dwelling | Riser maximum **200 mm**; tread and winder walkline at least **250 mm**; minimum winder depth **150 mm**; solid-riser nosing **20–32 mm** where tread below 275 mm | Stair wholly within individual dwelling unit | Not for common/exit stair | Conditional | Label in-unit stairs distinctly so exception is not propagated to core stairs | Verified |
| 1011.5.4 | Uniformity | Largest-smallest riser or tread variation maximum **10 mm** in a flight | All flights | Listed stepped-aisle and consistent-winder branches | Direct | Add construction tolerance requirement | Verified |
| 1011.6 | Landing depth and door | Landing depth equals stair width or **1200 mm**, whichever is less; fully open door projects no more than **175 mm**; open door cannot reduce landing below **one-half** required width | Stair landing | Listed transition/curved landing exceptions | Direct | Overlay door swings on clear landing diagrams | Verified |
| 1011.7.1 | Stair walking-surface slope | Maximum **1:48 (2%)** in any direction | Treads and landings | Opening-size exceptions for industrial uses | Direct | Coordinate drainage without exceeding cross slope | Verified |
| 1011.8 | Maximum flight rise | **3600 mm** maximum vertical rise between landings | Stair flight | Technical-production spiral exception | Direct | Insert intermediate landing where floor-to-floor geometry requires | Verified |
| 1011.12 | Roof stair | In buildings **4 or more stories**, one stair extends to roof unless roof slope exceeds **4:12 (33%)** | Tower roof | Unoccupied-roof access alternatives listed except where 1011.12.1 requires otherwise | Conditional | Confirm occupied/unoccupied roof and coordinate one core to roof | Verified |
| 1011.12.2 | Unoccupied-roof hatch | Hatch permitted at least **1.5 m²**, minimum dimension **600 mm** | Building without occupied roof | Applies only under stated roof-access exception | Conditional | Coordinate hatch, ladder/device and roof safety | Verified |
| 1011.13 | Roof-edge guard near hatch | Guard roof hatch/access or roof edge where opening is within **3000 mm** of roof edge | Roof access near edge | Guard must satisfy 1015 | Conditional | Keep hatch farther from edge or detail compliant guard | Verified |

## 12. Ramps

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1012.2 | Means-of-egress ramp slope | Maximum **1:12 (8.3%)** | Ramp forms part of means of egress | Other pedestrian ramps may be **1:8 (12.5%)**, but accessible route may be more restrictive outbound | Conditional | Use 1:12 for egress/accessible planning unless verified otherwise | Verified |
| 1012.3 | Ramp cross slope | Maximum **1:48 (2%)** | All ramps | No numeric branch stated | Conditional | Coordinate drainage falls | Verified |
| 1012.4 | Rise per run | Maximum **750 mm** | Each ramp run | No numeric branch stated | Conditional | Set landing frequency from rise | Verified |
| 1012.5.1 | Ramp clear width | At least **900 mm** between handrails/projections and sized for capacity | Egress ramp | Accessible route and served load may require more | Conditional | Check clear width after handrails | Verified |
| 1012.5.2 | Ramp headroom | At least **2000 mm** over runs and intermediate landings | Egress ramp | No stated numeric exception | Conditional | Coordinate structure/services in section | Verified |
| 1012.6.3–1012.6.4 | Ramp landings | Length at least **1500 mm**; direction-change landing **1500 × 1500 mm** | Ramp landing | Nonaccessible R-2 individual units may use **900 mm** landing / **900 × 900 mm** turn; nonaccessible ramp length need not exceed 1200 mm | Conditional | Apply accessibility/unit classification before selecting exception | Verified |
| 1012.8 | Ramp handrails | Both sides where rise exceeds **150 mm** | Ramp run | No general numeric exception in record | Conditional | Detail continuous handrails and extensions | Verified |
| 1012.10.1–1012.10.2 | Edge protection | Curb at least **100 mm**, or qualifying barrier; extended floor/ground at least **300 mm** beyond inside face of handrail | Ramp/landing edge protection required | Listed flared-side/adjoining-run/minor-drop exceptions | Conditional | Select and detail one compliant edge-protection method | Verified |

## 13. Handrails and guards

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1014.2 | Handrail height | Uniform **850–950 mm** above stair nosings or ramp surface | Required handrails | Alternating tread/ship ladder **750–850 mm**; fitting transitions listed | Direct | Dimension from correct datum, not finished landing | Verified |
| 1014.3.1 | Type I graspability | Circular outside diameter **32–50 mm**; noncircular perimeter **100–160 mm**, max cross-section **60 mm**, min **25 mm** | Type I handrail | Edge radius at least **0.25 mm** | Direct | Put profile limits in metalwork/joinery details | Verified |
| 1014.6 | Extensions | Ramp extensions **300 mm** horizontally beyond top/bottom; stair top **300 mm**, bottom slopes one tread depth | Handrails not continuous between runs/flights | Nonaccessible dwelling-unit and assembly-aisle exceptions | Direct | Resolve extensions against doors and circulation | Verified |
| 1014.7 | Wall clearance | At least **38 mm** clear between handrail and wall/surface | Wall-mounted handrail | No numeric branch stated | Direct | Coordinate brackets and finishes | Verified |
| 1014.8 | Projection | Handrail projections into required aisle/stair/ramp width maximum **115 mm** each side; accessible ramp clear between rails at least **900 mm** | Handrails project into egress width | Intermediate-pair rule applies where gap over **150 mm** | Direct | Calculate capacity on net clear width | Verified |
| 1014.9 | Intermediate handrails | All portions of stair minimum width/required capacity within **750 mm** of a handrail | Wide stair | No stated numeric exception | Conditional | Add intermediate rails to wide stairs | Verified |
| 1015.2 | Guard trigger | Guard open-sided walking surfaces where drop exceeds **750 mm** at a point within **900 mm** horizontally of edge | Mezzanine, balcony, stair, ramp, landing, roof edge | Listed stage/loading/service exceptions | Direct | Survey every edge and adjacent level | Verified |
| 1015.3 | General guard height | At least **1100 mm** | Required guards | R-2 in-unit stair guards may be **850 mm**; top-as-handrail **850–950 mm**; low-rise in-unit 900 mm exception does not describe this high-rise tower generally | Direct | Use 1100 mm for common areas and document any in-unit exception | Verified |
| 1015.4 | Guard openings | General guard rejects **100 mm** sphere; in R-2 unit open stair, **110 mm** sphere; triangular stair opening **150 mm** | Required guard | Other listed industrial/assembly branches | Direct | Specify opening limits by location | Verified |
| 1015.6–1015.7 | Roof service/access guards | Guards where service component or hatch is within **3000 mm / 3 m** of edge and edge drop exceeds **750 mm**; service guard extends **750 mm** beyond component/hatch | Roof equipment/access near edge | Fall-arrest/restraint anchorage exception under stated standard | Conditional | Coordinate roof plant zones, access path and fall protection | Verified |
| 1015.8 | R-2 operable-window trigger | In Group R-2/R-3 buildings including dwelling units, comply with one of four controls where bottom of clear operable opening is **less than 900 mm** above interior floor and exterior drop is **more than 1800 mm** to grade/surface below | Both sill/drop conditions occur | Raising bottom of clear opening to at least 900 mm avoids this trigger; an EERO must also satisfy 1031 | Direct | Audit every operable residential window against interior sill and exterior drop | Verified |
| 1015.8 Items 1–3 | Window fall-prevention branches | (1) Where **top of sill is more than 23 m** above exterior grade/surface, provide ASTM F2006 device; or (2) largest open position rejects a **100 mm-diameter sphere**; or (3) provide ASTM F2090 fall-prevention device | Triggered R-2/R-3 operable window | ASTM F2006 branch is expressly tied to the more-than-23 m top-of-sill condition; select one listed branch | Direct | Coordinate façade hardware and identify any window also serving as EERO | Verified |
| 1015.8 Item 4 / 1015.8.1 | Window opening-control device | Opening-control device complies with ASTM F2090 and, after release for full opening, does not reduce net clear opening below Section 1031.3.1 | Triggered window uses opening-control-device branch | Section 1031.3.1 criterion matters where the window is an EERO | Conditional | Obtain listed device data and verify released EERO clear area where applicable | Verified |

## 14. Corridors, aisles and exterior egress balconies

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1016.2 | Intervening spaces | Exit access cannot pass through a lockable room; dwelling/sleeping-area egress cannot lead through another sleeping area, toilet or bathroom; egress generally cannot pass through kitchens/storage/closets | Exit route passes through another space | Kitchen serving adjoining rooms in same dwelling/sleeping unit is a listed exception | Direct | Trace unit and shared routes against room locking and use | Verified |
| 1016.2 | Elevator lobby route | If two or more exits are required, at least one required exit must be accessible without travel through the enclosed elevator lobby required by Section 3006 | Enclosed elevator lobby lies on exit access | Lobby protection need not extend to exit unless another section requires direct access | Conditional | Preserve one independent route around lobby | Verified |
| 1016.2.1 | Multiple tenants/units | Each tenant space, dwelling unit and sleeping unit gets access to required exits without passing through adjacent tenant/unit | More than one tenant/unit on floor | Smaller-tenant exception is less than **10%** of larger adjoining space and has other conditions | Direct | Keep residential units independently connected to common egress | Verified |
| 1018.3 / 1018.5 | Nonassembly aisles | Nonpublic aisle serving fewer than **50** and not required accessible may be **700 mm** | B/M or other nonassembly work/stock aisle | Public/accessible aisle must satisfy applicable width/capacity | Conditional | Apply only to genuinely nonpublic support aisles | Verified |
| Table 1020.2 | R corridor rating | For Group R corridor serving more than **10**, OCR reads unsprinklered Not Permitted and sprinklered **“0.5/1 hours”**; rating/footnote attachment unresolved | Common R corridor | Table recognizes 903.3.1.1 or 903.3.1.2 where allowed; in-unit R corridor rating exception exists | External verification | Obtain published table/footnote before selecting corridor rating | Verify source |
| Table 1020.2 | Corridor width | OCR table contains **1100 mm** general and **900 mm** small-load/within-unit values, but row attachment is unresolved | Corridor width selection | Capacity under Section 1005 can govern above table minimum | External verification | Verify published table before issue; provisionally coordinate common corridor no narrower than capacity and verified minimum | Verify source |
| 1021.3 | Balcony openness | Long side at least **50% open**, distributed to minimize smoke/toxic-gas accumulation | Exterior egress balcony | Wall separation and opening protection also apply | Conditional | Demonstrate permanent openness, not operable glazing | Verified |
| 1021.4 | Balcony location | Fire separation distance at least **3000 mm** from lot line, other building portions and same-lot buildings unless protected as stated | Exterior egress balcony | Section 705 protection branch | Conditional | Coordinate façade returns and adjacent masses | Verified |

Dead-end corridor limits (base **6 m**; **15 m** only with Section 903.3.1.1 sprinklers) and the **30 m** exterior-balcony travel increase are tabulated once in Section 7.

## 15. Interior exit stairs/ramps, exit passageways and horizontal exits

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1023.1 | Exit enclosure continuity | Interior exit stair/ramp enclosed and leads directly outside or extends outside through 1024 exit passageway; used only for egress and circulation | Interior exit stair/ramp | Limited discharge alternatives under 1028.2 | Direct | Keep storage, plant and non-egress uses out of enclosure | Verified |
| 1023.2 | Enclosure rating | **2 hours** where connecting **4 stories or more**; **1 hour** where fewer; basements count, mezzanines do not | Interior exit enclosure | Rating not less than penetrated floor and need not exceed 2 hours; listed special exceptions | Direct | Tower core should be coordinated to 2-hour branch, subject to full code review | Verified |
| 1023.4 | Openings | Openings limited to required exit access and egress; **elevators shall not open into** interior exit stairways/ramps | Exit enclosure | Unprotected exterior openings handled separately | Direct | Eliminate service-room and elevator openings into stairs | Verified |
| 1023.7 | Exposed exterior wall | At angle below **180°**, building wall within **3000 mm** requires at least **1 hour**; protection extends to **3000 mm** above top landing/roof line; openings at least **3/4 hour** | Stair exterior wall exposed by building return | Applies to affected exposure zone | Conditional | Check façade returns around discharge and roof | Verified |
| 1023.10 / 1023.9.1 Items 4–6 | Elevator-lobby identification | At an interior-exit-stair landing where **two or more doors lead to the floor**, any door directly accessing an enclosed elevator lobby is marked **“Elevator Lobby”** on or directly adjacent to the door; lettering/numbers at least **25 mm**, nonglare and contrasting | Two-or-more-door stair landing with direct enclosed-lobby door | If the building/sign is subject to Section 1025, use the same material required by 1025.4; R-2 alone is not a listed 1025.1 group | Conditional | Add the lobby-door sign to stair-core door/sign schedules without importing Section 403 elevator assumptions | Verified |
| 1024.2 | Exit-passageway width | Capacity-sized; minimum **1100 mm**, or **900 mm** when serving fewer than **50** occupants | Exit passageway used | Permitted encroachments under 1005.7 | Conditional | Size for cumulative stair load, not only local floor | Verified |
| 1024.3 | Exit-passageway rating | At least **1 hour** and not less than connected stair/ramp requirement | Exit passageway extends protected exit | Connected 2-hour tower stair therefore controls at not less than that rating | Conditional | Match passageway protection to connected enclosure | Verified |
| 1026.1 | Horizontal-exit share | Cannot be sole exit; with multiple exits, no more than **one-half** total number or width/capacity may be horizontal exits | Horizontal exit proposed | I-2/I-3 exceptions not typical for R-2 | Conditional | Retain independent vertical/outdoor exits for remaining required share | Verified |
| 1026.2 | Horizontal-exit separation | Minimum **2-hour** separation, extending vertically unless floors are at least 2 hours with no unprotected openings | Horizontal exit proposed | Pedestrian-walkway exception only under stated conditions | Conditional | Align barrier continuity through tower/podium | Verified |
| 1026.4.1 | Refuge capacity | Net **0.28 m²/person** accommodated | Horizontal-exit refuge area | Separate from 1009 wheelchair-space geometry | Conditional | Calculate both total refuge area and accessible spaces | Verified |
| 1026.4.2 | Refuge exit | At least **one refuge-area exit** leads directly outside or to interior exit stair/ramp | Horizontal-exit refuge | Listed adjoining-compartment exception | Conditional | Show onward route without return through fire-origin compartment | Verified |

## 16. Exit discharge and egress courts

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1028.1 / 1028.5 | Discharge destination | Exits discharge directly outside; exit discharge provides direct, unobstructed access to public way | Every exit | Limited 1028.2 discharge-through-area/vestibule/horizontal-exit branches | Direct | Trace every stair/exit independently to public way | Verified |
| 1028.2 Ex. 1 | Discharge through level area | No more than **50%** of number and width/capacity of interior exit stairs/ramps may egress through discharge-level areas | Lobby/atrium discharge proposed | Requires visible unobstructed exterior door and separation below; egress path is sprinkler-protected, and portions with access to it are either sprinklered throughout under **903.3.1.1 or 903.3.1.2** or separated as an interior-exit enclosure | Conditional | Keep at least half direct and document the NFPA 13 or NFPA 13R discharge-lobby protection branch | Verified |
| 1028.2 Ex. 1.4 | Stair termination separation | Exit-access stair/ramp termination and interior-exit discharge door separated by at least **9 m** or **one-fourth** building diagonal, whichever is less | Both terminate at same discharge level | Straight-line measurement | Conditional | Dimension conflict separation in lobby plan | Verified |
| 1028.2 Ex. 2 | Vestibule discharge | No more than **50%** of number and width/capacity may discharge through vestibule | Vestibule alternative | Depth from exterior max **3000 mm**, length max **9 m**; protected and used only for egress | Conditional | Detail enclosure, dimensions and direct outside door | Verified |
| 1028.2 | Combined exceptions | Combined use of area and vestibule exceptions cannot exceed **50%** of required exits and width/capacity | Both exceptions used | Aggregate cap, not 50% each | Conditional | Include combined schedule | Verified |
| 1028.5 | Safe dispersal | If public-way access cannot be provided: at least **0.46 m²/person**, on same lot at least **15 m** from building, permanently maintained/identified, with safe unobstructed path | Safe-dispersal alternative | Only when direct public-way access cannot be provided | Conditional | Coordinate site/fire-appliance/landscape plans and capacity | Verified |
| 1029.2 | Egress-court width/headroom | Capacity-sized; minimum **1100 mm**; unobstructed to **2.1 m** high | Egress court forms discharge | R-3/U 900 mm exception does not apply to R-2 tower | Conditional | Protect net width from gates, planting and services | Verified |
| 1029.3 | Narrow egress court | Where court is under **3000 mm** wide, walls at least **1 hour** for **3000 mm** above court floor; openings at least **3/4 hour** | Narrow court | Exceptions for load under 10 and R-3, not general R-2 | Conditional | Coordinate wall/opening ratings along court | Verified |

## 17. Assembly amenity conditions

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| Table 1004.5 | Unfixed amenity seating/load | Standing **0.46 m² net/person**; chairs only **0.65 m² net/person**; tables/chairs **1.4 m² net/person** | Assembly amenity without fixed seats | Select by actual configuration; pool/deck factors unresolved | Conditional | Calculate each operating/event layout | Verified |
| 1004.9 | Occupant-load posting | Every assembly room/space posts approved load conspicuously near main exit/access doorway in permanent, maintained form | Space is assembly occupancy | Intended configurations must be represented | Conditional | Add placard to signage schedule | Verified |
| 1030.2 | Main exit over 300 | If assembly load is greater than **300** and a main exit is provided, main exit accommodates at least **one-half** load and at least total capacity leading to it | Large assembly amenity | If no well-defined main exit/multiple main exits, perimeter distribution may provide **100%** capacity | Conditional | Test ballroom/cinema/club layouts if load crosses 300 | Verified |
| 1030.2 | Group A frontage | Group A main exit fronts a street or at least **3000 mm** unoccupied space adjoining street/public way | Building/space classified Group A and main exit used | Occupancy classification is outbound from Chapter 10 | Conditional | Confirm whether amenity is Group A and coordinate frontage | Verified |
| 1030.3 | Other exits over 300 | In addition to main exit, each level with load over **300** gets additional egress capacity for at least **one-half** total load served, complying with 1007.1 | Large assembly with main exit | Distributed-main-exit alternative separately addressed | Conditional | Provide remote additional exits and capacity split | Verified |
| 1030.5 | Balcony/gallery | Seating capacity **50 or more** requires at least **two means of egress**, one from each side | Interior assembly balcony/gallery/press box | Under 50 follows other applicable rules | Conditional | Avoid single-ended amenity mezzanine seating at trigger | Verified |
| 1030.8 | Assembly common path | Base maximum **9 m** from seat to choice of two routes; area serving fewer than **50** may use **23 m** | Assembly seating | Smoke-protected/open-air branch **15 m** | Conditional | Measure from worst seat under every furniture plan | Verified |
| 1030.9.1 | Assembly aisle widths | Stepped, seating both sides **1200 mm**; one side **900 mm**; level/ramped both sides **1100 mm**; one side **900 mm** | Assembly seating aisle | Listed reductions to 900/750/600 mm depend on seat count, accessibility and handrail arrangement | Conditional | Size from served seats and accessible route | Verified |
| 1030.13.1 | Seating at tables datum | Required clear width measured to line **480 mm** from and parallel to table/counter edge | Loose seating at tables/counters | Fixed-seat measurement from back of seat | Conditional | Draw chair occupancy envelope in egress plans | Verified |
| 1030.13.1.1 | Table aisle access-way | At least **300 mm** plus **12.5 mm** per additional 300 mm/fraction beyond **3600 mm** length | Seating at tables/counters | Portion not over **1800 mm** serving max **4 persons** excepted | Conditional | Check deep banquettes and private dining layouts | Verified |
| 1030.13.1.2 | Table access travel | Maximum **9 m** from any seat to choice of two or more separate-exit paths | Seating at tables | No numeric branch stated | Conditional | Test farthest chair, not table edge | Verified |
| 1030.14.1 | Ramped assembly aisle | Over **1:20 (5%)** is a ramped aisle; accessible route max **1:12 (8%)**; other ramped aisle max **1:8 (12.5%)** | Sloped amenity seating aisle | Cross slope max **1:48 (2%)** | Conditional | Coordinate sightlines with accessible slope | Verified |
| 1030.14.2 | Stepped assembly aisle | Slope over **1:8 (12.5%)** uses full-width risers/treads; tread at least **275 mm**; riser generally **100–200 mm** | Stepped seating aisle | Sightline exception permits riser to **225 mm** with stated marking/tolerance controls | Conditional | Use dedicated stepped-aisle detail, not ordinary stair detail | Verified |
| 1030.16 | Assembly aisle handrails | Ramped aisle over **1:15 (6.7%)** and stepped aisle require handrails; wide one-sided stepped aisle **1850 mm or more** requires two; one rail within **750 mm** | Assembly aisles | Listed seating/guard and extension exceptions | Conditional | Coordinate mid-aisle rails with seat access | Verified |

## 18. Emergency escape and rescue openings

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1031.2 / Table 1006.3.4 | R-2 scope | Group R-2 is subject to 1031.2 only when located in a story with **one exit or access to one exit** as permitted by Tables 1006.3.4(1)/(2) | Project relies on a permitted single-exit R-2 story | General multiexit R-2 floors are not independently brought into 1031.2 by the R-2 listing | Conditional | Keep EEROs within the complete, source-verified single-exit package | Verified |
| 1031.2 | Location rule by listed occupancy | Within the listed occupancy scope, basements and sleeping rooms **below the fourth story above grade plane** require at least one EERO; each basement sleeping room requires one and adjoining basement areas do not | R-3/R-4 generally; R-2 **only within the single-exit scope above** | Opening leads directly to public way or a yard/court opening to public way; listed exceptions follow | Conditional | Do not apply the general R-3/R-4 trigger to ordinary multiexit R-2 tower floors | Verified |
| 1031.2 Ex. 5 | Sprinklered basement sleeping rooms | In an individual R-2/R-3 dwelling or sleeping unit, basement sleeping-room EEROs may be omitted where building is throughout sprinklered under 903.3.1.1, .1.2 or .1.3 and basement has either **one means of egress plus one EERO**, or **two means of egress** | R-3 generally; R-2 only where 1031.2 already applies through the permitted single-exit-story scope | Exception changes basement sleeping-room distribution; it does not expand 1031.2 to general multiexit R-2 | Conditional | Confirm the parent 1031.2 scope before using Exception 5 | Verified |
| 1031.3.1 | Net clear area | Minimum **0.53 m²**; grade-floor opening minimum **0.46 m²** | EERO required | Grade-floor exception only | Conditional | Schedule net clear area in open position | Verified |
| 1031.3.2 | Minimum dimensions | Clear height at least **600 mm** and clear width at least **500 mm** | EERO required | Both dimensions apply alongside area | Conditional | Verify proprietary window free opening, not frame size | Verified |
| 1031.3.3 | Sill height | Bottom of clear opening maximum **1100 mm** above floor | EERO required | No numeric branch stated | Conditional | Coordinate furniture and façade module | Verified |
| 1031.5.1 | Area well | Minimum horizontal area **0.84 m²**, projection and width at least **900 mm** | EERO opens into area well | Ladder/steps may encroach maximum **150 mm** | Conditional | Coordinate structure, drainage and usable clear opening | Verified |
| 1031.5.2 | Deep well ladder/steps | Well deeper than **1100 mm** requires permanently fixed ladder or steps | Deep area well | Must not obstruct opening operation | Conditional | Detail access and opening swing together | Verified |
| 1031.5.2.1–.2 | Well ladder/step geometry | Ladder inside width at least **300 mm**, projection at least **75 mm**, vertical spacing max **450 mm**; steps inside width at least **350 mm**, tread over **125 mm**, riser max **450 mm** | Ladder/steps provided | Use the applicable device branch | Conditional | Include complete dimensional detail | Verified |

## 19. High-rise and outbound dependencies

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1023.12 | Smokeproof enclosure dependency | “Where required by Section 403.5.4, 405.7.2 or 412.2.2.1,” interior exit stairs/ramps are smokeproof enclosures under 909.20 | High-rise statement points toward 403.5.4 review | Chapter 10 does not fully define the high-rise trigger, exceptions or 909.20 system | External verification | Verify Section 403 applicability/exceptions and engineer the 909.20 system; do not claim Chapter 10 alone proves smokeproof stairs | Verified |
| 1009.2.1 / 1009.4 | Accessible-egress elevator | Four-or-more-storey trigger is in Chapter 10; elevator must comply with 1009.4 | Required accessible floor/roof at trigger | 1009.4 then cross-references elevator systems/standby power and other requirements | External verification | Coordinate accessibility, vertical transport, fire alarm and fire strategy | Verified |
| Section 403 / Ch. 30 | High-rise/fire-service/occupant elevators | Chapter 10 commentary/cross-references identify high-rise elevator interfaces, but Chapter 10 does not fully define Section 403 elevator triggers or values | High-rise tower | Requirements and exceptions lie outside Chapter 10 | External verification | Do not claim high-rise elevator quantities/features from this matrix; verify Sections 403, 3007 and 3008 as applicable | Verified |
| 1025.1 | Luminous egress path markings | Listed high-rise groups are **A, B, E, I-1, M and R-1** | High-rise building in a listed group | **R-2 is not included in the listed groups**; mixed-use listed occupancy portions may still require analysis | Not typical | Do not impose Section 1025 solely because the tower is R-2 high-rise; review any listed podium/mixed use separately | Verified |
| 1005.3.1 Ex. 1 | Reduced stair factor systems | **5.08 mm/person** only with 903.3.1.1 or .1.2 sprinklers plus 907.5.2.2 EVACS | Capacity reduction proposed | High-rise sprinkler/EVACS requirements themselves are outside this clause | External verification | Keep **7.6 mm/person** until fire engineer confirms both systems and AHJ acceptance | Verified |
| Table 1017.2 | Travel-distance dependency | Group R row OCR reads **“60° / 75°”**, unresolved | Travel design | Published table/footnotes and sprinkler basis need verification | External verification | Resolve before schematic egress freeze | Verify source |
| Table 1020.2 | Corridor dependency | Group R sprinklered rating OCR reads **“0.5/1 hours”**, unresolved | Common R corridor serving load over 10 | Published table and footnote attachment required | External verification | Do not release partition rating from this extract | Verify source |
| 1002.1–1002.2 | Operations and plans | Means of egress maintenance and required fire-safety/evacuation plans are directed to SBC 801 | Occupancy/operation | Chapter 10 does not define the full operational plan | External verification | Integrate assisted evacuation, phased strategy and management procedures into approved fire strategy/SBC 801 plan | Verified |
| Chapter 11 / ICC A117.1 | Accessibility geometry | Chapter 10 establishes accessible-egress scoping but cross-references technical accessibility requirements | Accessible routes, doors, signs, ramps and communication | Exact technical geometry outside the Chapter 10 source-only matrix | External verification | Complete separate SBC accessibility review | Verified |
| Chapters 7 and 9 / SBC 501 | Passive and active fire protection | Chapter 10 relies on fire barriers, opening protectives, sprinklers, alarm and smoke-control provisions elsewhere | All protected egress systems | Ratings and system design are not fully specified by Chapter 10 alone | External verification | Align architectural egress matrix with fire engineer’s code basis and SCD NOC package | Verified |
| SCD / SBPS | Authority acceptance | No Chapter 10 value constitutes authority approval | Riyadh permit/NOC pathway | AHJ identity, submission stage and comments unconfirmed | External verification | Qualified local consultant to confirm authority pathway and close decision register before issue for approval | Verified |

## 20. Project-use controls

1. Use the **Verified** rows for initial dimensional coordination only after the row trigger and branch are confirmed.
2. Treat every **Verify source** row as a design hold point; no affected value is to be placed in issued-for-approval drawings without a published-source check.
3. Maintain separate NFPA 13 and NFPA 13R life-safety diagrams until the fire strategy selects one. In particular, the Section 1020.5 **15 m** R-2 dead-end allowance is NFPA 13 only.
4. Calculate occupant load by actual room function, then test in sequence: room/space exit-access doors, story exits, remoteness, capacity, loss of one exit, travel/common path, accessible egress, discharge and public-way continuity.
5. Record all fire-strategy and authority decisions in the project Golden Thread; this matrix is not evidence of SCD NOC or stamped compliance.

## 21. Coverage summary

Internal inventory of the attached Chapter 10 extract (numbered code, exceptions, tables, footnotes; commentary excluded). Row-level records are not published.

- **Total independently checkable numeric records:** 645
- **Verified:** 557
- **Verify source:** 88
- **Numeric records in Sections 1001 and 1002:** 0

### Counts by top-level section

| Top-level section | Records |
|---|---:|
| 1001 | 0 |
| 1002 | 0 |
| 1003 | 15 |
| 1004 | 47 |
| 1005 | 11 |
| 1006 | 49 |
| 1007 | 7 |
| 1008 | 12 |
| 1009 | 15 |
| 1010 | 116 |
| 1011 | 55 |
| 1012 | 17 |
| 1013 | 10 |
| 1014 | 18 |
| 1015 | 24 |
| 1016 | 5 |
| 1017 | 16 |
| 1018 | 7 |
| 1019 | 1 |
| 1020 | 21 |
| 1021 | 3 |
| 1022 | 1 |
| 1023 | 14 |
| 1024 | 6 |
| 1025 | 20 |
| 1026 | 8 |
| 1027 | 10 |
| 1028 | 7 |
| 1029 | 5 |
| 1030 | 109 |
| 1031 | 16 |

### Appended-table coverage

| Appended table | Records | Verify source records |
|---|---:|---:|
| Table 1004.5 | 38 | 6 |
| Table 1006.2.1 | 14 | 14 |
| Table 1006.3.3 | 3 | 0 |
| Table 1006.3.4(1) | 1 | 1 |
| Table 1006.3.4(2) | 8 | 8 |
| Table 1010.3.1(1) | 5 | 0 |
| Table 1010.3.1(2) | 12 | 12 |
| Table 1017.2 | 11 | 11 |
| Table 1020.2 — corridor rating | 7 | 7 |
| Table 1020.2 — minimum width | 7 | 7 |
| Table 1030.6.2 | 5 | 0 |
| Table 1030.13.2.1 | 8 | 8 |

## 22. Unresolved-source register

Hold points for the 88 **Verify source** inventory records. Counts are record counts, not distinct numeric values. No value in this register is a design-release figure.

| Affected table / clause | Why unverified | Control note |
|---|---|---|
| Table 1004.5 | 6 flattened/unresolved rows | Verify published table; empty values not adopted |
| Section 1005.3.2 | Exception 1 OCR corrupted | No reduced non-stair factor inferred |
| Table 1006.2.1 | 14 flattened rows; footnote attachment unresolved | Verify published table before one-door / common-path use |
| Section 1006.2.2.2 | Page-split continuation | Verify published clause |
| Table 1006.3.4(1) | Flattened single-exit dwelling-unit row | Verify published table |
| Table 1006.3.4(2) | 8 flattened single-exit rows | Verify published table; do not transpose dwelling/sleeping branches |
| Section 1008.2.2 | Grammatical fragment in mandatory OCR | Verify published clause |
| Section 1009.2.1 | Duplicated wording in Exception 2 | Base four-storey elevator trigger is used; exception wording needs published check |
| Unnumbered — commentary indicates 1010.1.7 | Source omits section number | Door-arrangement values retained under this citation |
| Table 1010.3.1(2) | 12 concatenated diameter/speed cells | Verify published table |
| Section 1011.2 | Exception 3 crosses pages | Verify published clause |
| Table 1017.2 | Damaged header / degree-symbol cells (`60° / 75°`) | Do not treat as metres |
| Table 1020.2 — corridor rating | Duplicate OCR table; Group R `0.5/1` unresolved | Do not release partition rating from this extract |
| Table 1020.2 — minimum width | Duplicate OCR table; row/footnote attachment unresolved | Verify published table before issue |
| Section 1025.2.6.1 | OCR/source ambiguity | Verify published clause |
| Section 1025.4 | Corrupted luminance units in OCR | Raw text retained; no silent correction |
| Section 1027.6 | Exception item 8 crosses pages | Verify published clause |
| Table 1030.13.2.1 | 8 concatenated row cells | Seat counts pending verification |
| Section 1030.17.3 | OCR/source ambiguity | Verify published clause |
| Section 1030.17.4 | OCR/source ambiguity | Verify published clause |
