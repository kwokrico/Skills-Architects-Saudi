# SBC 201 Chapter 4 Special Detailed Requirements Based on Occupancy and Use — Group R-2 High-Rise Dimensional Requirements Matrix (2024)

## 1. Document metadata and use limitation

- **Project basis:** Riyadh, Saudi Arabia; Group R-2 residential high-rise; an occupied floor is stated to be more than 23 m above the relevant reference level.
- **Deliverable tier:** Project-use matrices in Sections 4–18 (design-check rows, not pasted inventory), plus a coverage summary and unresolved-source register. The full row inventory is not published.
- **Code/source basis:** SBC 201 (2024), Chapter 4, source file `Reference\SBC 201 2024\source_reference\Chapter_04 — SPECIAL DETAILED REQUIREMENTS BASED ON OCCUPANCY AND USE.txt`.
- **Extraction audit:** Skill extract. Project-use rows follow the chapter-extract row contract (noun-phrase checks, bold SI values, building-language triggers, named exceptions, check-specific actions). Internal inventory: **768** independently checkable numeric records (**403** Verified, **365** Verify source). Unresolved OCR and flattened appended tables are listed in the register and are not design-release values.
- **Model:** Cursor Grok 4.6.
- **Prepared:** 2026-08-27.
- **Status:** Source-only architectural advisory matrix for design coordination. It is not a stamped compliance statement, fire-engineering report, SCD NOC, SBPS approval, legal opinion, or permission to construct.
- **Outbound-source rule:** No value in this matrix has been imported from Chapter 2 (high-rise definition), Chapter 5 height/area tables, Table 601/602, Chapter 7 ratings, Chapter 9, Chapter 10, Chapter 11, Chapter 16, Chapter 30, SBC 501, SBC 801, ICC A117.1, commentary examples, or a chapter summary. Where Chapter 4 sends the user elsewhere, this matrix records the dependency without supplying the outbound value.

### Scope and assumptions

1. Group R-2 and high-rise status are project statements, not independently verified classifications. Section **403.1** does not restate the Chapter 2 occupied-floor height; smokeproof-stair **403.5.4** uses **23 m** above the lowest level of fire department vehicle access.
2. The exact Riyadh AHJ/permit pathway, project stage, fire-strategy status and SCD NOC status are unconfirmed; therefore this matrix does not conclude compliance.
3. Automatic sprinkler protection is not selected. **Section 403.3** requires a system throughout in accordance with **Section 903.3.1.1** (NFPA 13) for high-rise buildings. **NFPA 13R / Section 903.3.1.2** is **not** an equal 403.3 path. Section **420.4** still *points* to **903.2.8** for Group R; that outbound value is not imported.
4. Construction type, Risk Category, Seismic Design Category, building height versus **36 m** and **128 m**, podium garage type (open vs enclosed), atrium, and occupied basement depth versus **9 m** below lowest level of exit discharge are unconfirmed.
5. Mall, Group I, Group H, aircraft, stages, laboratories and other occupancy-only packages in this chapter are omitted from project-use tables. They remain in the internal inventory and coverage counts.
6. Table **406.5.4** and most other appended tables are flattened HTML. Affected cells are **Verify source**. Table **403.2.4** two-cell bond-strength values are readable and are treated as Verified.
7. Fire-partition / horizontal-assembly ratings in Section 708/711, fire-command-center construction in Section 911, smokeproof-enclosure construction in Section 909.20, fire-service-access elevator construction in Section 3007, and domestic-cooking rules in SBC 501 require separate verification.

## 2. Legends

### Applicability

| Status | Meaning |
|---|---|
| **Direct** | Expected to govern the stated R-2 tower basis, subject to confirmed geometry and design data. |
| **Conditional** | Governs only when the stated feature, height band, construction type, sprinkler branch, podium garage, atrium or basement exists. |
| **Not typical** | Unrelated occupancy-only rule; omitted from this deliverable unless the gap register already opened that use. |
| **External verification** | Chapter 4 points to another section/code/standard, or the project/AHJ basis must be confirmed before use. |

### Source confidence

| Status | Meaning |
|---|---|
| **Verified** | Requirement and any stated numeric value were checked against unambiguous mandatory Chapter 4 source text or an unambiguous table cell. |
| **Verify source** | OCR, flattened table, page-split, or footnote attachment is unresolved. Not a design-release value. |

## 3. Project decision and gap register

| Decision / gap | Current project basis | Why it controls Chapter 4 application | Required project action |
|---|---|---|---|
| High-rise datum | Occupied floor stated above 23 m; exact height, grade plane and lowest fire-department vehicle access unconfirmed | Selects 403 package; **36 m** fire-service-access elevators; **128 m** FRR-reduction stop, extra risers, dual mains, enclosure impact integrity |
| Sprinkler basis | Unconfirmed. High-rise **403.3** requires **903.3.1.1**; **420.4** points to **903.2.8** | 13R is not a 403.3 substitute. FRR reductions, fuel-line rating drop and shaft-rating drop all assume the 403.3 system |
| Construction type | Unconfirmed; high-rise R-2 typically Type I or II | 403.2.1.1 IA→IB and IB→IIA reductions; Type IV-A/IV-B **36 m** dual-main trigger |
| Height vs 128 m | Unconfirmed | Extra stair **does not apply** to R-2; riser redundancy, dual street mains, SFRM **48 kN/m²** and enclosure impact still may |
| Risk Category | Unconfirmed; conventional R-2 often II | 403.2.2 impact integrity applies to Risk Category III/IV at any high-rise height, and to all buildings **more than 128 m** |
| Seismic Design Category | Unconfirmed | 403.3.3 secondary on-site water (**30 minutes**) applies to SDC C, D, E or F |
| Podium / mixed use | Unconfirmed | Shared 403 systems still apply to the tower; garage uses **406**; mall **402** is not assumed |
| Parking garage | Unconfirmed: open vs enclosed, private vs public, basement depth | 406 geometry; 405 Exception 2 if a sprinklered garage would otherwise be an underground building |
| Atrium / lobby void | Unconfirmed | 404 smoke control, enclosure and glass-protection sprinklers if a connecting void is an atrium |
| Occupied basement | Unconfirmed vs **9 m** below lowest LED | 405 Type I, two exits, smokeproof stairs; **18 m** two-compartment split |
| EVACS / fire command / ERCES | Unconfirmed | 403.4.4–403.4.6 send to 907.5.2.2, 911 and SBC 801 §510; values not in this chapter |
| NOC and fire strategy | SCD NOC and stamped fire-strategy status unconfirmed | High-rise smoke removal, smokeproof stairs, FSAE and sprinkler zoning cannot be concluded from Chapter 4 alone |

## 4. Chapter 4 application

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 401.1 | Chapter 4 supplemental scope | Occupancy and construction rules of this code still apply; this chapter adds the occupancy- and use-specific provisions described herein | Any occupancy or use listed in Chapter 4 | None stated | Direct | Read 403 and 420 with the rest of the code; do not treat Chapter 4 as a substitute for Chapters 5–10 | Verified |
| 402.1 Ex. 1 | Mall section not required for R-2 lobby | Foyers and lobbies of Group B, R-1 and R-2 occupancies are **not required** to comply with Section 402 | Residential foyer/lobby that is not a covered or open mall building | Buildings that fully comply with other code provisions also need not use 402 | Direct | Do not apply mall width, kiosk or plastic-sign rules to the tower lobby unless a true mall building is proposed | Verified |

## 5. High-rise applicability and height bands

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 403.1 | High-rise package trigger | High-rise buildings shall comply with Sections **403.2 through 403.6** | Building classified as high-rise (Chapter 2 definition is outbound) | Airport traffic-control towers 412.2; open parking garages 406.5; Group A-5 portion 303.6; special industrial 503.1.1; H-1; listed H-2/H-3 cases | Direct | Lock occupied-floor height vs lowest fire-department vehicle access on the code data sheet, then apply the 403 package | External verification |
| 403.5.4 | Smokeproof-stair height datum | Every required interior exit stairway serving floors **more than 23 m** above the lowest level of fire department vehicle access shall be a smokeproof enclosure | Required interior exit stair serving those floors | Construction of the enclosure is in **909.20** and **1023.12** (not imported) | Direct | Identify which stairs serve floors above the 23 m fire-access datum; do not smokeproof-label podium-only stairs that never serve those floors | Verified |
| 403.6.1 | Fire-service elevator height band | Occupied floor **more than 36 m** above the lowest level of fire department vehicle access requires fire-service-access elevators | Tower occupied floor above **36 m** fire-access datum | Capacity and 3007/3002.4 details are in that row | Conditional | Dimension the highest occupied floor vs fire-access grade; if above 36 m, reserve two FSAE cars | Verified |
| 403.2.1.1 / 403.3.1 / 403.5.2 | Super-high-rise 128 m band | Several 403 rules change at building height **greater than 128 m**: IA FRR reduction stops; extra sprinkler risers; dual street mains; R-2 extra-stair exemption still holds | Building height vs **128 m** | R-2 extra stair is independently excepted (Section 13) | Conditional | Put **128 m** on the height diagram even if the extra stair is not required for R-2 | Verified |

## 6. Construction and fire-resistance reductions

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 403.2.1 | FRR-reduction prerequisite | 403.2.1.1 and 403.2.1.2 reductions are allowed only where sprinkler control valves have supervisory initiating devices and water-flow initiating devices **for each floor** | Designer proposes a Table 601 rating reduction | No reduction without the per-floor valve/flow devices | Conditional | Show floor-control assemblies and addressable flow/tamper on the sprinkler schematic before taking a 403.2.1 reduction | Verified |
| 403.2.1.1 Item 1 | Type IA element-rating reduction | For buildings **not greater than 128 m** in building height, Type IA building-element ratings may be reduced to Type **IB** ratings | Type IA selected for height/area; height ≤ **128 m** | Columns supporting floors shall **not** be reduced | Conditional | Keep floor-supporting columns on the Type IA column rating; reduce only the other IA elements if this branch is used | Verified |
| 403.2.1.1 Item 2 | Type IB element-rating reduction | Type IB building-element ratings may be reduced to Type **IIA** ratings | Type IB selected; occupancy is other than F-1, H-2, H-3, H-5, M and S-1 | R-2 is not in the excluded list. Reduction still needs 403.2.1 devices | Conditional | If the tower is Type IB, document the IIA-equivalent element ratings on the construction-type sheet | Verified |
| 403.2.1.1 Item 3 | Height/area after reduction | Height and area limits remain those of the building **without** the rating reduction | Any 403.2.1.1 reduction taken | Construction type is not reclassified downward | Conditional | Keep Tables 504/506 on the original type; do not shrink allowable area because elements were reduced | Verified |
| 403.2.1.2 | Shaft-enclosure rating reduction | For height **not greater than 128 m**, fire barriers enclosing vertical shafts other than interior exit stairways and elevator hoistways may be reduced to **1 hour** where sprinklers are installed in the shafts at the **top** and at **alternate floor levels** | Secondary shafts (trash, MEP, linen) in a ≤ **128 m** high-rise | Does **not** apply to exit-stair or elevator-hoistway enclosures | Conditional | Detail shaft-head and alternate-floor sprinklers on every reduced-rating shaft; keep exit and lift shafts at their full rating | Verified |

## 7. Stair and elevator enclosure impact integrity

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 403.2.2 | Enclosure integrity trigger | Interior exit-stairway and elevator-hoistway enclosures shall comply with 403.2.2.1–403.2.2.4 for Risk Category **III or IV**, and for **all** buildings **more than 128 m** in building height | Risk Category III/IV high-rise, or any building > **128 m** | Typical Risk Category II R-2 below 128 m is outside this trigger | Conditional | Confirm Risk Category on the structural criteria sheet before specifying ordinary shaft board | Verified |
| 403.2.2.1 | Soft-body impact | Enclosure panels shall meet or exceed Soft Body Impact Classification **Level 2**, ASTM C1629/C1629M, tested from the **exterior** side of the enclosure | 403.2.2 applies | Concrete/masonry deemed to comply (403.2.2.3) | Conditional | Specify Level 2 soft-body shaft board (or concrete/masonry) on the core-wall type | Verified |
| 403.2.2.2 | Hard-body impact | Face **not** exposed to the interior of the enclosure: **two** layers of Hard Body **Level 2**, **or** **one** layer of Hard Body **Level 3**, **or** multiple layers tested in tandem to **Level 3** | 403.2.2 applies | Concrete/masonry deemed to comply (403.2.2.3) | Conditional | Note the chosen hard-body build-up on the corridor side of the shaft | Verified |
| 403.2.2.3–403.2.2.4 | Masonry or equivalent walls | Concrete or masonry walls satisfy 403.2.2.1 and 403.2.2.2. Other materials may be used if they provide equivalent Soft Body **Level 2** and Hard Body **Level 3** resistance, ASTM C1629/C1629M | Alternative shaft wall proposed | Hard-body Level 3 text is page-split after 403.2.2.4 heading; classification is completed on the next page | Conditional | Prefer concrete/masonry cores, or attach the C1629 report for a board system | Verified |

## 8. Sprayed fire-resistant materials

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 403.2.3 / Table 403.2.4 | SFRM bond strength | SFRM installed throughout the building shall have minimum bond strength **21 kN/m²** for height **up to 128 m**, and **48 kN/m²** for height **greater than 128 m**, measured above the lowest level of fire department vehicle access (Table note a) | High-rise with sprayed fire-resistant materials | Table is concatenated HTML; the two cells are readable. Do not use commentary **7.2 kN/m²** | Direct | Put the governing bond-strength value on the fireproofing specification and mock-up | Verified |

## 9. High-rise sprinklers, risers, water and pumps

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 403.3 | High-rise sprinkler standard | Building shall be equipped throughout with an automatic sprinkler system in accordance with **Section 903.3.1.1** and a secondary water supply where required by 403.3.3 | High-rise building under 403 | Telecommunications-equipment spaces: detection per 907.2 plus **1-hour** fire barriers or **2-hour** horizontal assemblies, or both. **903.3.1.2 / NFPA 13R is not listed** | Direct | Specify NFPA 13 / 903.3.1.1 throughout the tower; do not use a 13R-only high-rise design | Verified |
| 403.3.1 | Extra sprinkler risers | Each sprinkler zone in buildings **more than 128 m** in building height shall be supplied by **not fewer than two** risers. Each riser supplies sprinklers on **alternate** floors. If more than two risers serve a zone, adjacent floors shall not be supplied from the same riser | Building height > **128 m** | Does not apply at or below 128 m | Conditional | Draw two remote risers per zone and alternate-floor take-offs on the riser diagram | Verified |
| 403.3.1.1 | Riser location | Sprinkler risers shall be placed in interior exit stairways and ramps remotely located in accordance with **Section 1007.1** | Risers required | 1007.1 separation values are not imported | Direct | Route risers in remote exit stairs; coordinate with 403.5.1 enclosure remoteness | External verification |
| 403.3.2 | Dual street mains | Required fire pumps shall be supplied from **not fewer than two** water mains in **different streets**, with separate supply piping, where the building is **more than 128 m** high, **or** Type **IV-A / IV-B** and **more than 36 m** high | Those height/construction cases | Two connections to the **same** main are permitted if the main is valved so an interruption can be isolated and supply continues through **not fewer than one** connection | Conditional | Confirm street-main layout with civil; Type IV-A/IV-B towers hit this at 36 m, not 128 m | Verified |
| 403.3.3 | Secondary on-site water | Automatic secondary **on-site** water supply, capacity not less than the hydraulically calculated sprinkler demand including hose stream, duration **not less than 30 minutes** per NFPA 13 occupancy-hazard classification, for high-rise buildings in Seismic Design Category **C, D, E or F** | SDC C–F high-rise | Extra fire pump for the secondary supply only if needed for intake pressure. NFPA 13 demand figures are not imported | Conditional | Lock SDC from Chapter 16; size the on-site tank from the NFPA 13 calculation, not from this matrix | Verified |
| 403.3.4 | Fire-pump room | Fire pumps shall be located in rooms protected in accordance with **Section 913.2.1** | Fire pump provided | 913.2.1 ratings are not imported | Direct | Show the pump room on the life-safety plan and cite 913.2.1 for the enclosure | External verification |

## 10. Detection, alarm, standpipe, communications and fire command

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 403.4.1 | High-rise smoke detection | Smoke detection in accordance with **Section 907.2.13.1** | High-rise building | Detector locations are not in this chapter | Direct | Carry 907.2.13.1 into the fire-alarm scope; do not invent device counts here | External verification |
| 403.4.2 | High-rise fire alarm | Fire alarm system in accordance with **Section 907.2.13** | High-rise building | Outbound | Direct | Show a high-rise fire-alarm system on the cause-and-effect matrix citing 907.2.13 | External verification |
| 403.4.3 | High-rise standpipe | Standpipe system as required by **Section 905.3** | High-rise building | Class and locations are in Chapter 9 | Direct | Coordinate standpipe stairs with 403.5 remoteness; do not copy 905 numbers here | External verification |
| 403.4.4 | Emergency voice/alarm | Emergency voice/alarm communication system in accordance with **Section 907.5.2.2** | High-rise building | EVACS details are outbound | Direct | Include EVACS in the fire-alarm specification; this chapter does not size speakers | External verification |
| 403.4.5 | Emergency responder coverage | In-building two-way emergency responder communication coverage in accordance with **Section 510 of SBC 801** | High-rise building | SBC 801 §510 exceptions are not imported | Direct | Flag ERCES/DAS as a fire-strategy item for SCD; do not design radio coverage from this extract | External verification |
| 403.4.6 | Fire command center | Fire command center complying with **Section 911**, in a location approved by the fire code official | High-rise building | 911 room size and equipment list are not imported | Direct | Locate a fire command center at an SCD-agreed entry and cite Section 911 for fit-out | External verification |

## 11. Post-fire smoke removal

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 403.4.7 Item 1 | Natural smoke-removal openings | Manually operable windows or panels around the perimeter of **each floor** at **not more than 15 m** intervals; operable area **not less than 4 m² per 15 m** of perimeter | Natural-ventilation smoke-removal option | Exception 1 (**0.2 m²** per sleeping unit) is **Group R-1 only** — do not use for R-2. Exception 2: fixed glazing permitted if fire fighters can clear it | Direct | Schedule panel size and spacing per floor, or use tempered/clearable glass agreed with civil defence | Verified |
| 403.4.7 Item 2 | Mechanical smoke-removal rate | Mechanical air-handling providing **one exhaust air change every 15 minutes** for the area involved; return and exhaust moved directly outside with **no recirculation** | Mechanical smoke-removal option | This is post-fire salvage/overhaul ventilation, not Section 909 atrium smoke control | Conditional | If mechanical removal is chosen, show 4 ACH equivalent (one change / 15 min) as a dedicated exhaust mode | Verified |
| 403.4.7 Item 3 | Alternative smoke removal | Any other approved design that will produce equivalent results | Designer proposes a non-prescriptive system | Building-official approval required | Conditional | Use only with a documented equivalent and AHJ acceptance | Verified |

## 12. Standby and emergency power

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 403.4.8 | Standby and emergency power | Standby power per **2702** and **3003** for 403.4.8.3 loads. Emergency power per **2702** for 403.4.8.4 loads | High-rise building | Load lists below; durations in Chapter 27 are not imported | Direct | Split standby vs emergency bus on the generator schedule using the two lists | External verification |
| 403.4.8.1 | Generator room enclosure | Indoor generator set in a separate room enclosed with **2-hour** fire barriers (Section 707) or horizontal assemblies (Section 711), or both. Manual start and transfer at the fire command center | Generator inside the building | Group I-2 Condition 2 critical-branch start/transfer need not be at the fire command center — not an R-2 exception | Direct | Draw a 2-hour generator room and duplicate start/transfer at the fire command center | Verified |
| 403.4.8.2 Item 1 | UL 1489 fuel-line protection | Fuel lines serving an indoor generator, outside the generator room, protected by a UL 1489 system rated **not less than 2 hours**; reduced to **1 hour** where the building is sprinklered throughout per **903.3.1.1** | Fuel-fired indoor generator | High-rise 403.3 already requires 903.3.1.1, so the **1-hour** reduction is available on that branch | Conditional | Specify 1-hour UL 1489 wrap if NFPA 13 throughout is documented | Verified |
| 403.4.8.2 Item 2 | Rated assembly around fuel lines | Assembly fire-resistance **not less than 2 hours**, reduced to **1 hour** where sprinklered throughout per **903.3.1.1 or 903.3.1.2** | Fuel-fired indoor generator; rated shaft/chase used instead of UL 1489 | Item 2 is the only 403 fuel-line clause that also names 903.3.1.2. Item 3: other approved methods | Conditional | Prefer the 903.3.1.1 / 1-hour chase consistent with 403.3; do not switch the whole tower to 13R to take this drop | Verified |
| 403.4.8.3 | Standby power loads | Standby loads: (1) smokeproof-enclosure ventilation and automatic fire detection; (2) elevators; (3) additional standby rules in **1009.4, 3007 or 3008** where elevators serve accessible egress, fire-service access or occupant self-evacuation | High-rise standby generator | 3003/3007/3008 kW figures are not imported | Direct | Include smokeproof fans and all elevators on the standby schedule; add FSAE/OEE extra load if those elevators exist | External verification |
| 403.4.8.4 | Emergency power loads | Emergency loads: exit signs and egress illumination (Chapter 10); elevator car lighting; EVACS; automatic fire detection; fire alarm; electrically powered fire pumps; fire-command-center power and lighting | High-rise emergency generator | Pickup times are in Chapter 27, not here | Direct | Put these seven loads on the emergency bus, including fire-command lighting | External verification |

## 13. High-rise means of egress

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 403.5.1 | Interior exit-stair remoteness | Separate required interior exit stairways by **not less than 10 m** **or** **one-fourth** of the maximum overall diagonal of the building or area served, **whichever is less**. Measure in a straight line between nearest points of the **enclosures**. Where **three or more** interior exit stairways exist, **not fewer than two** shall comply. Interlocking or scissor stairways count as **one** | High-rise required interior exit stairs | Also meet Chapter 10 Section 1007 (values not imported). Do **not** use commentary **9 m** | Direct | Dimension enclosure-to-enclosure clearance on each typical floor; treat scissors as one stair | Verified |
| 403.5.2 | Additional stair — R-2 exemption | One additional interior exit stairway is required for buildings **other than Group R-2 and their ancillary spaces** that are **more than 128 m** in building height, plus remaining-capacity-with-one-stair-removed. Scissor stairs shall not be that additional stair | Building height > **128 m** in a **non-R-2** occupancy | Exception 1: occupant-evacuation elevators per 3008. Exception 2: portions with highest occupiable floor **less than 128 m**. **R-2 and ancillary amenity spaces are exempt from the extra stair** | Direct | Do not add a third stair solely for 403.5.2 on an R-2 tower; still size stairs to Chapter 10 and 403.5.1 | Verified |
| 403.5.3 | Stair re-entry unlocking | Stairway doors other than exit-discharge doors may be locked from the stair side if they can be unlocked **simultaneously without unlatching** on a signal from the fire command center | Stair doors locked against re-entry | Unlocking shall not defeat the latch | Conditional | If security locks stairs, show a fire-command unlock circuit that leaves latching intact | Verified |
| 403.5.3.1 | Locked-stair communication | Telephone or other two-way communications to an approved constantly attended station at **not less than every fifth floor** in each stairway where doors are locked | 403.5.3 locking used | None stated in the numbered code sentence | Conditional | Place a two-way device at least every fifth locked-stair landing | Verified |
| 403.5.4 | Smokeproof interior exit stairs | Every required interior exit stairway serving floors **more than 23 m** above the lowest level of fire department vehicle access shall be a smokeproof enclosure in accordance with **909.20** and **1023.12** | Those stairs | Vestibule vs pressurization methods are in 909.20, not imported | Direct | Designate tower exit stairs as smokeproof and send the system design to 909.20 | External verification |
| 403.5.5 | Luminous egress path markings | Luminous egress path markings shall be provided in accordance with **Section 1025** | High-rise building under 403 | This chapter does **not** list occupancy groups. Do not import a commentary A/B/E/I/M/R-1 list | Direct | Apply 1025 to the exit enclosures; verify occupancy scope in Chapter 10, not from this matrix | External verification |

## 14. High-rise elevators

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 403.6 | Elevator charging | Elevator installation and operation shall comply with **Chapter 30** and 403.6.1–403.6.2 | High-rise building | Chapter 30 car sizes and hoistway protection are not imported | Direct | Send the lift package to Chapter 30; use 403.6.1–403.6.2 for the high-rise extras | External verification |
| 403.6.1 | Fire-service-access elevators | Occupied floor **more than 36 m** above the lowest level of fire department vehicle access: **not fewer than two** fire-service-access elevators, **or all elevators, whichever is less**, in accordance with **Section 3007**. Each FSAE capacity **not less than 1600 kg**, and comply with **Section 3002.4** | Occupied floor above the **36 m** fire-access datum | 3007 lobby, standpipe-stair adjacency and 3002.4 stretcher dimensions are not imported | Conditional | Provide two 1600 kg FSAE cars (or every car if fewer than two exist) and a 3007 lobby at each FSAE | Verified |
| 403.6.2 | Occupant-evacuation elevators | Passenger elevators for general public use **may** be used for occupant self-evacuation where installed in accordance with **Section 3008** | Designer elects OEE | Optional for R-2; not a substitute for R-2 extra-stair (that stair is already exempt) | Conditional | If OEE is offered, apply 3008 to **all** public passenger lifts; do not import 3008 geometry here | External verification |

## 15. Group R unit separations and domestic cooking

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 420.1 | Group R charging | Groups I-1, R-1, R-2, R-3 and R-4 shall comply with 420.1 through 420.5 and other applicable provisions | Group R-2 building | 420.6–420.9 are I-1 only and are omitted here | Direct | Apply unit separations, 420.4/420.5 pointers and 420.10 cooking on every R-2 floor | Verified |
| 420.2 | Dwelling/sleeping-unit walls | Walls separating dwelling units, separating sleeping units, and separating dwelling or sleeping units from other contiguous occupancies shall be **fire partitions** in accordance with **Section 708** | R-2 units in the same building | 708 ratings (including any sprinkler reduction) are not imported | Direct | Draw unit-demising and unit-to-corridor/other-occupancy walls as 708 fire partitions; read the hour rating from Chapter 7 | External verification |
| 420.3 | Dwelling/sleeping-unit floors | Floor assemblies separating dwelling units, separating sleeping units, and separating dwelling or sleeping units from other contiguous occupancies shall be **horizontal assemblies** in accordance with **Section 711** | R-2 stacked units | 711 ratings are not imported | Direct | Rate unit-to-unit and unit-to-podium floors as 711 horizontal assemblies | External verification |
| 420.4 | Group R sprinkler pointer | Group R occupancies shall be equipped throughout in accordance with **Section 903.2.8**. Quick-response or residential sprinklers per **903.3.2** | Group R | High-rise **403.3** already requires **903.3.1.1**. Do not import a 13R option from 903.2.8 into the tower | Direct | Keep the tower on NFPA 13 / 903.3.1.1; use 903.3.2 for residential/QR heads where Chapter 9 requires them | External verification |
| 420.5 | R-2 alarm and smoke-alarm pointer | Fire alarm and smoke alarms for R-2 in accordance with **Section 907.2.9**. Single- or multiple-station smoke alarms for R-2 in accordance with **Section 907.2.11** | Group R-2 | Device locations and interconnection are in Chapter 9 | Direct | Include 907.2.9 system and 907.2.11 unit smoke alarms in the fire-alarm specification | External verification |
| 420.10 | Group R domestic cooking | Cooking appliances used for domestic cooking operations in Group R shall be in accordance with **Section 917.2 of SBC 501** | Dwelling-unit kitchens and similar domestic cooking | Hotel restaurants / commercial cooking are outside this pointer. Dormitory 420.11 is omitted unless a college-dorm program is opened | Direct | Specify dwelling kitchens to SBC 501 §917.2; do not use I-1 420.8–420.9 rules on apartments | External verification |

## 16. Podium and parking garage

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 406.2.2 | Garage clear height | Clear height of each floor level in vehicle and pedestrian traffic areas **not less than 2100 mm** | Parking garage present | Mechanical-access open-parking tier may be lower where approved. Accessible van height is in Chapter 11, not here. Fuel-canopy height is 406.7.2 | Conditional | Set typical garage storey height to preserve **2100 mm** clear under beams, signs and sprinklers | Verified |
| 406.2.4 | Garage floor surface | Concrete or similar approved noncombustible, nonabsorbent floor; parking area sloped to a drain or the main vehicle entry | Parking garage | Exception 1: asphalt at **ground level** for public garages and private carports. Exception 2 (repair-garage CRF **0.45 W/cm²**) is not a typical R-2 podium finish | Conditional | Slope basement/upper garage slabs to drains; limit asphalt to grade-level if used | Verified |
| 406.2.5 | Garage/sleeping openings | Openings between a motor-vehicle-related occupancy and a room used for **sleeping purposes** shall **not** be permitted | Any garage adjoining sleeping rooms | Applies to public and private garages | Conditional | Eliminate windows/doors from garage into bedrooms; use a non-sleeping lobby if a unit adjoins the garage | Verified |
| 406.2.7 | EV charging listing | EV charging equipment listed to **UL 2202**; EV supply equipment listed to **UL 2594**; electrical per NFPA 70 / SBC 401; accessibility per **Section 1107** | EV charging provided in the garage | Accessible EVCS geometry is in Chapter 11 / A117.1, not imported | Conditional | Put UL 2202/2594 on the EVCS specification and send accessible stalls to Chapter 11 | External verification |
| 406.2.9.1 | Ignition-source elevation | Ignition sources in garages elevated **not less than 450 mm** above the floor on which the appliance rests | Fuel-fired or sparking equipment in the garage | Not required for appliances listed flammable-vapor-ignition-resistant. Rooms communicating with a private garage are treated as part of that garage | Conditional | Mount water heaters, dryers and similar equipment ≥ **450 mm** or use FVIR-listed units | Verified |
| 406.2.9.1.1 | Fuel-fired appliance vestibule | Connection of a parking garage to a room with a fuel-fired appliance shall be by a **two-doorway** vestibule, unless ignition sources are elevated per 406.2.9 | Public/parking garage next to a plant room | Single door permitted with the elevation option. 406.2.9.2 / 406.2.9.3 installations are excepted | Conditional | Provide a vestibule to boiler/generator rooms opening to the garage, or elevate the ignition source | Verified |
| 406.2.9.2 | Public-garage appliance height | Appliances in public garages **not less than 2400 mm** above the floor; if vehicles can pass under, **not less than 300 mm** higher than the tallest vehicle door opening | Public parking garage | Exception: impact-protected appliances installed per 406.2.9.1 and NFPA 30A | Conditional | Hang garage heaters/AHUs at **2400 mm** or behind vehicle-impact protection | Verified |
| 406.3.1 | Private-garage area cap | Each private garage **not greater than 100 m²**; multiple private garages separated by **1-hour** fire barriers (707) or **1-hour** horizontal assemblies (711), or both | Private (Group U) garages rather than public S-2 | A typical podium public garage is 406.4, not this cap | Conditional | Use 406.4/406.5/406.6 for a shared podium garage; apply 100 m² only to true private garages | Verified |
| 406.3.2.1 | Private garage / dwelling separation | **12.5 mm** gypsum on the garage side; garage beneath habitable rooms: **16 mm** Type X (or equivalent) plus **12.5 mm** on supporting structure. Doors: solid wood or honeycomb steel **not less than 35 mm**, or **20-minute** 716.2.2.1 doors; self-closing and self-latching | Private garage adjacent to a dwelling unit | Not a substitute for 420.2/420.3 in the tower. 406.2.5 still bans openings into sleeping rooms | Conditional | Use this build-up only for townhouse-style private garages, not for the public podium | Verified |
| 406.4.2 | Vehicle barriers | Vehicle barriers **not less than 850 mm** high where the drop from drive lane or parking space to the surface below is **greater than 300 mm**; loading per **Section 1607.10** | Public parking garage with edge drop > **300 mm** | Not required in mechanical-access vehicle storage compartments. 1607.10 kN value is not imported | Conditional | Show 850 mm vehicle barriers at every garage edge and ramp drop; send loads to the structural engineer | Verified |
| 406.4.3 | Parking-ramp slope | Vehicle ramps used for vertical circulation **and** parking shall **not exceed 1:15 (6.67 percent)**. Vehicle ramps are not required exits unless pedestrian facilities are provided | Parking on the ramp | Steeper ramps cannot be the pedestrian exit | Conditional | Keep parked ramps at **1:15** or flatter; provide separate pedestrian exits | Verified |
| 406.5.2 | Open-garage ventilation openings | Openings on **two or more** sides; opening area **not less than 20 percent** of each tier’s perimeter wall area; aggregate opening length **not less than 40 percent** of the tier perimeter; interior walls **not less than 20 percent** open | Open parking garage classification | Exception: 40 percent perimeter distribution not required where openings are uniformly distributed on **two opposing** sides (20 percent area still applies) | Conditional | If claiming “open” garage, calculate opening area and length per tier before dropping mechanical ventilation | Verified |
| 406.5.2.1 | Below-grade open-garage well | Where below-grade openings provide the required natural ventilation, outside horizontal clear space shall be **one and one-half** times the depth of the opening, maintained from grade to the lowest required opening | Open garage with openings below surrounding grade | Depth-to-well ratio is the check | Conditional | Size light-well width ≥ **1.5 ×** opening depth | Verified |
| 406.5.4.1 | Single-use open garage / spiral tier | Exclusive parking use may use **Table 406.5.4**. Grade-level office/waiting/toilets **not more than 100 m²** need not be separated. Continuous spiral floor: each **2900 mm** of height (or portion) is a tier | Stand-alone open garage, not mixed with the tower | Table 406.5.4 cells are flattened — **Verify source**. Mixed podium garages stay on Chapter 5 via 406.5.4 | Conditional | Do not use Table 406.5.4 for a mixed R-2 podium; verify the published table only for a single-use open garage | Verify source |
| 406.5.5 | Open-garage area/height increases | Sides open on **three-fourths** of the perimeter: **25 percent** area increase and **one** extra tier. Entire perimeter open: **50 percent** area and **one** extra tier. “Open” side: openings **not less than 50 percent** of interior side area, height used in the calculation **not more than 2.15 m** | Single-use open garage seeking Table 406.5.4 increases | Type II all-sides-open unlimited-area branch (height **not exceed 23 m**; portions within **6 m** of openings; courts **60 m**) is page-split — treat those two distance tokens as **Verify source** | Conditional | Apply 25/50 percent increases only after opening-area diagrams; verify the Type II 6 m / 60 m page-split before using unlimited area | Verify source |
| 406.5.7 | Attendant-only garage stairs | Where persons **other than parking attendants** are not permitted: **not fewer than two** exit stairways, each **not less than 900 mm** wide | Attendant-only / mechanical-access open garage | Public-use garages use Chapter 10 (not imported) | Conditional | For a public podium garage, size stairs from Chapter 10, not the 900 mm attendant branch | Verified |
| 406.6.2 | Enclosed-garage ventilation | Mechanical ventilation and exhaust in accordance with **Chapters 4 and 5 of SBC 501** | Enclosed public parking garage | Exception: accessory to one- and two-family dwellings | Conditional | Send enclosed-podium ventilation rates to SBC 501; do not invent ACH here | External verification |
| 406.6.3 | Enclosed-garage sprinklers | Enclosed parking garage sprinklered in accordance with **Section 903.2.10** | Enclosed public garage | 903.2.10 fire-area thresholds are not imported. High-rise 403.3 already requires 13 throughout the building | Conditional | Keep enclosed podium parking on the building NFPA 13 system; confirm 903.2.10 still met | External verification |
| 406.6.4.1–406.6.4.3 | Mechanical-access enclosed garage | **2-hour** separation from other occupancies; mechanical smoke removal per **910.4**; fire-control room **not less than 4.65 m²** with exterior fire-service access | Mechanical-access enclosed (rack) garage | Typical ramp podium is 406.6, not 406.6.4 | Conditional | If a puzzle/rack garage is added, apply 2-hour box, 910.4 exhaust and a 4.65 m² fire-control room | Verified |

## 17. Atriums

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 404.1 | Atrium charging | Sections 404.1–404.11 apply to buildings containing atriums. Atriums are not permitted in Group H | Connecting vertical void treated as an atrium | Vertical openings that comply with 712.1.1–712.1.3 and 712.1.9–712.1.14 need not use 404 | Conditional | Decide atrium vs 712 opening on the lobby section; do not skip 404 if 712.1.7 (atrium) is the chosen path | Verified |
| 404.3 | Atrium building sprinklers | Approved automatic sprinkler system throughout the **entire building** | Atrium present | Exception 1: adjacent/above areas separated by **2-hour** barriers/horizontal assemblies. Exception 2: atrium ceiling **more than 16 m** above the floor — ceiling sprinklers not required (do not use commentary 16.5 m) | Conditional | Sprinkler the whole building if an atrium is used; omit only the high ceiling or 2-hour-separated wings | Verified |
| 404.5 | Atrium smoke control | Smoke control in accordance with **Section 909** | Atrium connecting stories | Exception 1: smoke control not required for a **two-story** atrium other than I-2 / I-1 Condition 2. Exception 2: more than two stories if only the **two lowest** stories are open and floors above are shaft-separated per 713.4 | Conditional | Provide 909 smoke control unless the two-story or shafted-upper-floor exception is demonstrated | External verification |
| 404.6 | Atrium enclosure | Separate atrium from adjacent spaces by a **1-hour** fire barrier (707) or horizontal assembly (711), or both | Atrium present | Glass-wall exception: sprinklers **100–300 mm** from glass, spacing **not greater than 1800 mm**, both sides (or room side only if no atrium walkway). Glass-block **3/4-hour**. Up to **three** floors may be open if included in the smoke-control design. No enclosure where 404.5 smoke control is not required | Conditional | Default to 1-hour atrium walls, or detail the 100–300 mm glass sprinkler grid | Verified |
| 404.8 | Atrium interior finish | Walls and ceilings of the atrium **not less than Class B**; sprinklers shall **not** reduce the class | Atrium surfaces | Table 803.13 reductions are not allowed here | Conditional | Specify Class B (or better) atrium wall/ceiling finish with no sprinkler trade-down | Verified |
| 404.10 | Exit stair in the atrium | Entry is the closest riser; access from **minimum of two** directions; remoteness to an enclosed 1023.2 stair per 1007.1.1; travel measured to the closest riser; **not more than 50 percent** of exit stairways in the same atrium | Interior exit stair placed in the atrium | 1007.1.1 distances not imported | Conditional | If a feature stair is an exit, keep at least half the exits in enclosed stairs and show two-way approach to the first riser | Verified |
| 404.4 / 404.7 / 404.9 / 404.11 | Atrium outbound pointers | Fire alarm **907.2.14**; smoke-control standby power **909.11**; travel distance **1017**; discharge through atrium **1028** | Atrium present | Values in those sections are not imported | Conditional | List 907.2.14, 909.11, 1017 and 1028 as atrium coordination items | External verification |

## 18. Underground buildings

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 405.1 | Underground-building trigger | 405.2–405.9 apply where a floor used for **human occupancy** is **more than 9 m** below the finished floor of the lowest level of exit discharge | Occupied basement / below-grade amenity | Exception 2: **parking garages** with sprinklers per 405.3. Also 1–2 family 903.3.1.3; transit; assembly seating; lowest storey ≤ **140 m²** and occupant load **less than 10**; limited-use plant rooms | Conditional | Measure occupied-floor depth vs LED. Sprinklered parking alone does not make the building a 405 underground building | Verified |
| 405.2 | Underground construction type | Underground portion shall be **Type I** construction | 405 applies | Above-grade portion follows Chapters 5/6 | Conditional | Set below-grade occupied structure to Type I | Verified |
| 405.3 | Underground sprinklers | Highest level of exit discharge serving the underground portions, and all levels below, sprinklered per **903.3.1.1**; water-flow and control valves supervised per **903.4** | 405 applies | Consistent with high-rise 403.3 NFPA 13 | Conditional | Extend NFPA 13 from LED down through all below-grade occupied levels | External verification |
| 405.4.1 | Deep-level two-compartment split | Floor **more than 18 m** below lowest LED: divide into **not fewer than two** compartments of approximately equal size, from LED down | Occupied floor > **18 m** below LED | Lowest storey need not be compartmented if area **not greater than 140 m²** and occupant load **less than 10** | Conditional | If a deep occupied basement exists, split it with a smoke barrier into two roughly equal compartments | Verified |
| 405.4.2–405.4.3 | Compartment independence | Smoke barrier per **709**; penetrations limited to plumbing/electrical with **714** firestopping; doors 716, smoke-activated, NFPA 105. Independent air supply/exhaust per compartment. Each compartment has direct elevator access, or a smoke-barrier lobby if the elevator serves more than one compartment | 405.4.1 compartmentation required | 709/714/716 values not imported | Conditional | Give each deep compartment its own HVAC and either its own lift or a 709 elevator lobby | External verification |
| 405.5 / 405.6 | Underground smoke control and alarm | Smoke control per **909**; where compartmented, each compartment has an independent automatically activated, manually operable system. Fire alarm where required by **907.2.18** and **907.2.19** | 405 applies | 909 design criteria not imported | Conditional | Add below-grade 909 smoke control and the 907.2.18/19 alarm scope | External verification |
| 405.7.1 | Underground exit count | Each floor: **not fewer than two** exits. Where 405.4 compartmentation is required: **not fewer than one** exit **and** **not fewer than one** exit-access doorway into the adjoining compartment | 405 applies | Chapter 10 may require more | Conditional | Put an exit in each deep compartment plus a cross-door to the other compartment | Verified |
| 405.7.2 | Underground smokeproof stairs | Every required stair serving floors **more than 9 m** below the finished floor of its LED shall be a smokeproof enclosure per **1023.12** | Those stairs | 909.20 construction not imported | Conditional | Smokeproof any stair that climbs more than 9 m from a below-grade occupied floor to its LED | External verification |
| 405.8 / 405.9 | Underground power and standpipe | Standby: smoke control; smokeproof ventilation/detection; elevators per 3003. Emergency: EVACS, fire alarm, detection, car lighting, egress/exit-sign lighting, fire pumps. Standpipe throughout per **905** | 405 applies | May overlap 403.4.8 loads in a high-rise with a deep basement | Conditional | Combine 403 and 405 load lists on the generator schedule; extend standpipe to the lowest occupied level | External verification |

## 19. Project-use controls

1. Use **Verified** rows for drawing and specification checks after the row trigger is confirmed (high-rise, garage type, atrium, occupied depth).
2. Treat **Verify source** rows (flattened Table 406.5.4, 406.5.5 page-split distances) as hold points. They are not design-release values.
3. Do not import 708/711 hours, 907 device layouts, 909.20 vestibule sizes, 911 fire-command dimensions, 1025 marking details, 3007 lobby size, or SBC 501 cooking clearances into issued drawings from this matrix.
4. Keep **NFPA 13 / 903.3.1.1** as the high-rise sprinkler path (403.3). Do not treat 13R as satisfying 403.3 even though 420.4 points at 903.2.8.
5. Do not apply 403.5.2’s extra stair to Group R-2 or its ancillary amenity spaces.
6. Do not give R-2 the 403.4.7 Exception 1 **0.2 m²** hotel venting allowance.
7. Do not use commentary **9 m** in place of code **10 m** for 403.5.1, or commentary **7.2 kN/m²** in place of Table 403.2.4.
8. Omit mall (402), I-2/I-3, H, aircraft, stages, laboratories, dormitory cooking (420.11) and I-1 smoke-compartment cooking unless the gap register is later opened for those uses.
9. Record high-rise height bands, sprinkler standard, garage type and atrium/basement decisions in the project Golden Thread; this matrix is not evidence of SCD NOC or stamped compliance.

## 20. Coverage summary

Internal inventory of the attached Chapter 4 extract (numbered code, exceptions, tables, footnotes; commentary excluded). Row-level records are not published.

- **Inventory scope:** numbered code, exceptions, tables, footnotes (commentary excluded)
- **Total independently checkable numeric records:** 768
- **Verified:** 403
- **Verify source:** 365

### Counts by top-level section

| Top-level section | Records |
|---|---:|
| 401 | 0 |
| 402 | 42 |
| 403 | 43 |
| 404 | 12 |
| 405 | 11 |
| 406 | 73 |
| 407 | 29 |
| 408 | 23 |
| 409 | 6 |
| 410 | 26 |
| 411 | 4 |
| 412 | 141 |
| 413 | 2 |
| 414 | 116 |
| 415 | 131 |
| 416 | 1 |
| 417 | 3 |
| 418 | 3 |
| 419 | 3 |
| 420 | 10 |
| 421 | 0 |
| 422 | 7 |
| 423 | 6 |
| 424 | 15 |
| 425 | 0 |
| 426 | 13 |
| 427 | 15 |
| 428 | 33 |

### Appended-table coverage

| Appended table | Records | Verify source records |
|---|---:|---:|
| Table 403.2.4 | 2 | 0 |
| Table 406.5.4 | 20 | 20 |
| Table 412.2.1.1 | 5 | 5 |
| Table 412.3.6 | 81 | 81 |
| Table 412.6 | 24 | 24 |
| Table 414.2.2 | 36 | 36 |
| Table 414.2.5(1) | 40 | 40 |
| Table 414.2.5(2) | 20 | 20 |
| Table 414.5.1 | 15 | 15 |
| Table 415.6.5 | 26 | 26 |
| Table 415.11.1.1.1 (incl. continuation) | 66 | 66 |
| Table 428.3 | 30 | 30 |

No CS.md exists for this chapter. Commentary figures (including Figure 403.5.1’s **9 m** example) were not inventoried and were not used as values.

## 21. Unresolved-source register

Hold points for the 365 **Verify source** inventory records. Counts are record counts, not distinct numeric values. No value in this register is a design-release figure.

| Affected table / clause | Why unverified | Control note |
|---|---|---|
| 402.8.2.2 OLF range | Code text reads occupant-load factor **not less than 30** and **shall not exceed 50**; SI mall practice and the following commentary use **2.8 / 4.65**. Not adopted | Mall 402 is omitted from project-use. If a mall is later added, verify the published SI OLF bounds before using Equation 4-1 |
| Table 406.5.4 | Flattened HTML; 20 area/tier cells not safely segmented | Mixed R-2 podiums use Chapter 5 via 406.5.4, not this table. Verify published cells only for a single-use open garage |
| 406.5.5 Type II unlimited-area distances | Page-split after **2.15 m**; published continuation gives **6 m** horizontal and **60 m** courts, which conflict with the commentary figures on the same pages | Do not release Type II unlimited-area open-garage geometry until the published distances are checked |
| Table 412.2.1.1 | Concatenated control-tower heights | Aircraft occupancy omitted from project-use |
| Table 412.3.6 | Flattened hangar fire-area / construction grid plus **8.5 m** door-height note | Aircraft occupancy omitted |
| Table 412.6 | Flattened aircraft-manufacturing travel-distance grid | Aircraft occupancy omitted |
| Table 414.2.2 | Flattened control-area floor / percentage / rating grid | Hazardous-material control areas omitted unless an H use is added |
| Table 414.2.5(1) | Flattened MAQ indoor/outdoor cells and sprinkler-cabinet increase notes | Do not reconstruct kg/L MAQs from concatenated HTML |
| Table 414.2.5(2) | Concatenated flammable-liquid MAQ columns and density footnotes | Verify published litres and Ordinary Hazard densities before any retail MAQ |
| Table 414.5.1 | Flattened explosion-control Required/Not Required grid | H occupancy omitted |
| Table 415.6.5 | Flattened detached-building quantity triggers | H occupancy omitted |
| Table 415.11.1.1.1 (both pages) | Flattened H-5 fabrication density cells; footnote **255 m³** NTP | H-5 omitted |
| Table 428.3 | Flattened laboratory-suite percentage / count / rating grid | Higher-education laboratories omitted |
