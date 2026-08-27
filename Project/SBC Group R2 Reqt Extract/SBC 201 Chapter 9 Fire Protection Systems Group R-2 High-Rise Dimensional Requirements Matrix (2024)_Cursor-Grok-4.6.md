# SBC 201 Chapter 9 Fire Protection Systems — Group R-2 High-Rise Dimensional Requirements Matrix (2024)

## 1. Document metadata and use limitation

- **Project basis:** Riyadh, Saudi Arabia; Group R-2 residential high-rise; an occupied floor is stated to be more than 23 m above the relevant reference level.
- **Deliverable tier:** Project-use matrices in Sections 4–18 (design-check rows, not pasted inventory), plus project-use controls, a coverage summary and an unresolved-source register. The full row inventory is not published.
- **Code/source basis:** SBC 201 (2024), Chapter 9, source file `Reference\SBC 201 2024\source_reference\Chapter_09 — FIRE PROTECTION SYSTEMS.txt`.
- **Extraction audit:** Skill extract. Project-use rows follow the chapter-extract row contract (noun-phrase checks, bold SI values, building-language triggers, named exceptions, check-specific actions). Internal inventory: **310** independently checkable numeric records (**251** Verified, **59** Verify source). Unresolved OCR and missing equations are listed in the register and are not design-release values.
- **Model:** Cursor Grok 4.6.
- **Prepared:** 2026-08-27.
- **Status:** Source-only architectural/fire-protection coordination advisory matrix. It is not a stamped fire-engineering report, SCD NOC, SBPS approval, legal opinion, or permission to construct.
- **Outbound-source rule:** No value in this matrix has been imported from Chapter 4 (including 403.3), Chapter 10, Chapter 11, Chapter 27, Chapter 30, SBC 501, SBC 701, SBC 801, NFPA 4/10/13/13R/13D/14/20/72, ICC A117.1, ASME A17.1, commentary examples, Figure 903.2, or the existing chapter summary. Where Chapter 9 sends the user elsewhere, this matrix records the dependency without supplying the outbound value.

### Scope and assumptions

1. Group R-2 and high-rise status are project statements, not independently verified classifications. Chapter 9 uses “high-rise” without restating a height trigger.
2. The exact Riyadh AHJ/permit pathway, project stage, fire-strategy status and SCD NOC status are unconfirmed; therefore this matrix does not conclude compliance.
3. NFPA 13 versus 13R is not assumed as a project choice. **903.3.1.2** eligibility (four stories or fewer and **9 m** above/below fire-department vehicle access) is tested first. For this occupied-floor-above-**23 m** basis, 13R is not a permitted installation path; remaining sprinkler geometry uses the **903.3.1.1 / NFPA 13** path.
4. Mixed-use podium, enclosed parking, amenity assembly, Type I cooking, landscaped roof, fuel-burning appliances and storey/FD-access datums are unconfirmed.
5. Table 906.3(1), Table 906.3(2) Extra-High row, Table 907.5.2.3.2, and the 909.6.2 / 909.10.1 / 910.3.3 equations are concatenated or cut off. Affected values are **Verify source**.
6. Figure 903.2 occupancy-threshold grid is a figure, not a value source. Table 903.2.11.6 names **403.3** as an outbound high-rise suppression pointer; Chapter 4 text is not imported.

## 2. Legends

### Applicability

| Status | Meaning |
|---|---|
| **Direct** | Expected to govern the stated R-2 tower basis, subject to confirmed geometry and design data. |
| **Conditional** | Governs only when the stated feature, mixed-use/podium condition, sprinkler branch or exception exists. |
| **Not typical** | Unrelated occupancy-only rule; omitted from this deliverable unless the gap register already opened that use. |
| **External verification** | Chapter 9 points to another section/code/standard, or the project/AHJ basis must be confirmed before use. |

### Source confidence

| Status | Meaning |
|---|---|
| **Verified** | Requirement and any stated numeric value were checked against unambiguous mandatory Chapter 9 source text. |
| **Verify source** | OCR, flattened table, page-split, missing heading, or footnote attachment is unresolved. Not a design-release value. |

## 3. Project decision and gap register

| Decision / gap | Current project basis | Why it controls Chapter 9 application | Required project action |
|---|---|---|---|
| Sprinkler installation standard | Unconfirmed; 13R eligibility is tested, not assumed | 903.3.1.2 permits NFPA 13R only at **four stories or fewer** and highest/lowest floor **9 m** of FD vehicle access. High-rise geometry fails that test | Fire engineer to lock **903.3.1.1 / NFPA 13** unless a published 13R path is proven; do not take 13-only trade-offs on a 13R system |
| Storeys and FD-access datum | Occupied floor stated above **23 m**; exact height, grade plane and vehicle-access level unconfirmed | Controls 13R eligibility, 903.2.11.3 **16.5 m / OL 30**, 905.3.1 **4 stories / 9 m**, 907.2.13.3 **36 m** multi-channel EVACS, and FSAE sprinkler omission | Issue a signed code datum sheet with grade plane, occupied-floor elevations, basements and lowest FD vehicle access |
| Mixed-use / podium | Unconfirmed | 903.2.8 sprinkles the **entire building** that contains a Group R fire area. Non-R fire areas may independently require NFPA 13 even if a 13R residential path existed | Freeze occupancy by fire area; do not apply residential 13R omissions to podium retail, parking or assembly |
| Enclosed / open parking | Unconfirmed | 903.2.10 enclosed garage **1115 m²** or beneath other groups; open garage **4460 m²**; commercial MV **465 m²** | Classify podium/basement parking as 406.5 vs 406.6 and dimension fire areas |
| Amenity assembly / occupied roof | Unconfirmed | 903.2.1 Group A thresholds and 903.2.1.6 occupied-roof OL **100 / 300** can add story-to-LED sprinkler coverage; 907.2.1 alarm thresholds are occupancy-specific | Classify each lounge, gym, pool deck and roof amenity by actual function and occupant load |
| Type I cooking | Unconfirmed | 904.2.2 / 904.13 require an extinguishing system for each required Type I hood (SBC 501 / SBC 801 §609) | Kitchen consultant to lock hood type; if Type I, apply 904.13 geometry |
| EVACS / FCC location | High-rise stated; AHJ approval unconfirmed | 907.2.13 requires EVACS; 911.1.1 location must be approved by the fire code official | Fire alarm designer and SCD consultant to lock FCC location, paging zones and cause-and-effect |
| Fuel-burning appliances | Unconfirmed all-electric vs gas | 915 requires CO detection in Group R where 915.1.2–915.1.6 conditions exist | MEP to state whether any fuel-burning appliance, fireplace, furnace or attached private garage exists |
| Landscaped roof / helipad | Unconfirmed | 905.3.8 extends standpipes to a landscaped roof; 905.3.6 sends heliports to SBC 801 | Confirm roof program before freeze of standpipe termination |
| NOC and fire strategy | SCD NOC and stamped fire-strategy status unconfirmed | Acceptance of NFPA 13 design, smokeproof method, FCC and radio coverage cannot be concluded from Chapter 9 alone | Engage the qualified local/fire consultant before design freeze |

## 4. Scope, required systems and high-rise testing

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 901.1 | Chapter scope | This chapter specifies where fire protection and life safety systems are required and governs their design, installation and operation | All buildings in scope | Maintenance/testing live in SBC 801 (not imported) | Direct | Treat Chapter 9 as the charging chapter for sprinklers, standpipes, alarms, smoke control, FCC, FDC and fire pumps | Verified |
| 901.2 | Required-system status | Install, repair, operate and maintain systems per this code and SBC 801. Any system used to take an exception or reduction is a **required** system | Fire protection or life safety system | Voluntary systems still must meet this chapter | Direct | If a sprinkler or alarm trade-off is taken elsewhere, keep that system as required | Verified |
| 901.5 | Acceptance before occupancy | Do not occupy a portion of a structure until the required fire protection systems in that portion have been tested and approved | New work / partial occupancy | Tests in the presence of the building official where required | Direct | Sequence partial occupancy only after the serving systems are tested | Verified |
| 901.6 / 901.6.1 | Supervising-station monitoring | Where required, monitor fire protection systems at an approved supervising station per NFPA 72. Automatic sprinkler systems shall be so monitored | Required sprinkler systems | Exception 1: one- and two-family dwellings. Exception 2: limited-area systems per 903.3.8 | Direct | Show supervising-station monitoring on the sprinkler/alarm riser diagram | External verification |
| 901.6.2.1 | High-rise integrated testing | Integrated testing shall comply with NFPA 4, with a test before certificate of occupancy and at intervals not exceeding **10 years**, unless an NFPA 4 integrated-system test plan specifies otherwise | High-rise buildings | Repeat of the entire integrated test is not required after a repair except to verify functions initiated by replaced equipment | Direct | Put NFPA 4 integrated testing on the commissioning specification; do not import NFPA 4 procedures here | External verification |
| 901.6.2.2 | Smoke-control integrated testing | Where a fire alarm is integrated with a Section 909 smoke control system, integrated testing shall comply with NFPA 4 on the same **10-year** cadence | Fire alarm integrated with 909 smoke control | Same repair-repeat limitation as 901.6.2.1 | Conditional | If stair pressurization or another 909 system is provided, include it in the NFPA 4 test plan | External verification |
| 901.6.3 | Fire-alarm supervising station | Fire alarm systems required by 907.2 shall be monitored by an approved supervising station per 907.6.6 | Required 907.2 fire alarm | Exceptions: 907.2.11 smoke alarms; Group I-3 smoke detectors; one- and two-family sprinklers | Direct | Connect the tower fire alarm to a supervising station; keep unit smoke alarms off that path | Verified |
| 901.7 | Fire-area separation | To stay under a Chapter 9 protection threshold, divide fire areas with 706 fire walls, 707 fire barriers or 711 horizontal assemblies rated not less than Section 707.3.10 | Building subdivided to avoid a protection trigger | Rating values live in 707.3.10 (not imported) | Conditional | 903.2.8 already sprinkles any building with a Group R fire area; do not use fire areas to omit tower sprinklers | External verification |

## 5. Fire pump and riser rooms

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 902.1 | Pump/riser room working space | Size rooms for manufacturer clearances so equipment can be inspected, serviced, repaired or replaced without removing permanent construction or disabling a required fire-resistance-rated assembly; provide a door and unobstructed passageway for the largest piece of equipment | Fire pump room or sprinkler riser room is provided | This section does not itself require a room | Direct | Coordinate room size and a removal path with the fire-protection contractor before the core is frozen | Verified |
| 902.1.1 | Pump/riser access | Provide ready access to risers, fire pumps and controllers. A locked room door is permitted if the key is available at all times | Equipment in a pump or riser room | None stated | Direct | Show a 24-hour key location on the life-safety plan | Verified |
| 902.1.2 | Access-door lettering | Label access doors with an approved contrasting sign; letters minimum height **50 mm**, minimum stroke **10 mm** | Pump or riser room doors | None stated | Direct | Put **50 mm / 10 mm** lettering on the door schedule | Verified |
| 902.1.3 | Pump/riser room temperature | Maintain the room at not less than **4 °C**; heating units shall be permanently installed | Pump or riser room | None stated | Direct | Specify permanent heating to **4 °C** in the pump/riser room | Verified |
| 902.1.4 | Pump/riser room lighting | Provide permanently installed artificial illumination | Pump or riser room | None stated | Direct | Put permanent lighting on the electrical room data sheet | Verified |

## 6. Group R sprinkler charging

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 903.2 | Where sprinklers are required | Provide approved automatic sprinklers in new buildings in the locations in 903.2.1 through 903.2.12 | New buildings | Telecom equipment spaces with 907.2 smoke detection and **1-hour** barriers or **2-hour** horizontal assemblies, or both | Direct | Do not use the telecom exception for R-2 dwelling floors | Verified |
| 903.2.8 | Group R building sprinklers | Provide an automatic sprinkler system per 903.3 **throughout all buildings with a Group R fire area** | Any Group R fire area, including R-2 | 903.2.8.1–903.2.8.4 permit 13D/13R only for R-3, R-4 and small care dwellings — not this R-2 high-rise | Direct | Sprinkle the entire building that contains the R-2 fire area, including mixed-use stories | Verified |
| 903.2.11.3 | Height **16.5 m** sprinkler trigger | Sprinkle throughout buildings that have one or more stories with occupant load **30 or more** located **16.5 m or more** above the lowest level of fire department vehicle access, measured to the finished floor | Occupied story at that height and load | Group F-2 occupancies | Direct | Treat as a second independent trigger; 903.2.8 already covers this tower | Verified |
| Table 903.2.11.6 | Outbound high-rise suppression pointer | Additional required suppression systems include **403.3 High-rise buildings** among other outbound sections | Uses listed in the table | Concatenated OCR pointer table; no Chapter 4 value is adopted | External verification | Obtain published 403.3; do not import high-rise sprinkler text from Chapter 4 here | Verify source |

## 7. Sprinkler installation standard (13 vs 13R)

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 903.3.1 | Default installation standard | Design and install sprinklers per 903.3.1.1 unless 903.3.1.2, 903.3.1.3 or another chapter permits otherwise | Required automatic sprinklers | 13R and 13D only where those sections are met | Direct | Start from NFPA 13 unless a numbered 13R/13D permission is proven | External verification |
| 903.3.1.2 | NFPA 13R eligibility | NFPA 13R is permitted in Group R only where **all** apply: **four stories or fewer** above grade plane; highest floor **9 m or less** above lowest FD vehicle access; lowest floor **9 m or less** below that access. Stories under 510.2 / 510.4 are measured from grade plane | Group R proposing 13R | Pedestal 510.2 / 510.4 does not restart the four-story / **9 m** tests from the podium roof | Direct | Record that this occupied-floor-above-**23 m** high-rise **fails** 13R eligibility; do not specify 13R | Verified |
| 903.3.1.1 | NFPA 13 throughout | Where the code requires a building or portion to be equipped throughout per this section, install sprinklers throughout per NFPA 13 except 903.3.1.1.1 and 903.3.1.1.2 | 13R/13D not permitted | Exempt locations and R bathrooms as numbered | Direct | Specify NFPA 13 for the tower; installation details live in NFPA 13 (not imported) | External verification |
| 903.3.1.3 | NFPA 13D scope | NFPA 13D is permitted in one- and two-family dwellings, Group R-3, Group R-4 Condition 1 and townhouses | Those occupancies only | Not a Group R-2 high-rise path | Not typical | Omit 13D from the tower specification | Verified |
| 903.3.2 | Quick-response / residential sprinklers | Where sprinklers are required, install quick-response or residential sprinklers in dwelling units and sleeping units in Group R occupancies (and other listed I-2/ambulatory/light-hazard locations) | R dwelling/sleeping units | Listings and 903.3.1 still apply | Direct | Specify QR or residential heads in units; keep other occupancies on their NFPA 13 hazard | Verified |

## 8. Sprinkler omissions, obstructions and high-rise floor valves

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 903.3.1.1.1 | NFPA 13 exempt rooms | Sprinklers may be omitted in listed rooms if an approved 907.2 automatic fire detection system is provided. Do not omit sprinklers merely because a room is damp, rated or contains electrical equipment. Item 3: generator/transformer rooms with **2-hour** walls and floor/ceiling or roof/ceiling assemblies. Items 5–6: fire-service-access and occupant-evacuation elevator machine/control rooms | Designer proposes an omission | FSAE/OEE rooms are Conditional on Chapters 4/30 requiring those elevators; those chapters are not imported | Conditional | Use omissions only with listed detection and the **2-hour** generator-room rating; keep unit and corridor sprinklers | Verified |
| 903.3.1.1.2 | Small R bathroom omission | In Group R, sprinklers are not required in bathrooms not exceeding **5 m²** in individual dwelling or sleeping units if walls and ceilings (including behind shower/tub) are noncombustible or limited-combustible with a **15-minute** thermal barrier | Unit bathrooms | Accessible bathrooms often exceed **5 m²** — then sprinkle | Conditional | Dimension each unit bathroom; sprinkle any bathroom over **5 m²** | Verified |
| 903.2.11.2 | Rubbish and linen chutes | Install sprinklers at the top of rubbish and linen chutes and in terminal rooms; additional heads at alternate floors and at the lowest intake. Recess and freeze-protect extension sprinklers; provide access for servicing | Rubbish or linen chutes | Heading is missing in the extract; body text follows 903.2.11.1.3 | Direct | Show chute sprinklers at top, terminal, lowest intake and alternate floors on the riser diagram | Verify source |
| 903.3.3 | Obstruction and pile clearance | Install sprinklers with regard to obstructions per the applicable standard. Sprinkle in or under covered kiosks, displays, booths, concession stands or equipment exceeding **1200 mm** in width. Maintain not less than **900 mm** clearance between sprinklers and the top of combustible-fiber piles | Obstructions or combustible-fiber storage | Kitchen equipment under a 904 exhaust hood is excepted | Conditional | Keep **1200 mm** kiosks sprinkled and **900 mm** above fiber storage in amenities/back-of-house | Verified |
| 903.3.8.1 | Limited-area sprinkler cap | Limited-area systems shall not exceed **six** sprinklers in any single fire area | Limited-area system proposed | Not a substitute for 903.2.8 throughout-building protection | Not typical | Do not use a six-head limited-area system to satisfy the R-2 building trigger | Verified |
| 903.4 | Electrical supervision | Electrically supervise valves, pumps, tanks, water levels and temperatures, critical air pressures and waterflow switches by a listed fire alarm control unit | Automatic sprinkler systems | Eight listed exceptions (13D dwellings, limited-area, some 13R combination supplies, sealed jockey/kitchen/fuel/trim valves, underground roadway valves) | Direct | Supervise floor and supply valves at the FACU; do not apply the 13R combination-supply exception to this 13 tower | Verified |
| 903.4.2 | Exterior waterflow alarm | Connect an approved exterior audible device, activated by flow equivalent to one smallest-orifice sprinkler. Where a fire alarm is installed, sprinkler actuation shall actuate the building fire alarm | Each automatic sprinkler system | None stated | Direct | Show the exterior waterflow bell and fire-alarm interconnection | Verified |
| 903.4.3 | High-rise floor control valves | Provide approved supervised indicating control valves at the point of connection to the riser **on each floor** in high-rise buildings | High-rise buildings | None stated | Direct | Put a supervised floor control valve at each story on the combined standpipe/sprinkler riser | Verified |

## 9. Commercial cooking and alternative extinguishing

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 903.1.1 / 904.2.1 | Alternative system vs sprinkler trade-offs | A 904 alternative extinguishing system may replace occupancy sprinklers where recognized and approved, but it shall **not** unlock sprinkler exceptions or reductions | Alternative agent proposed in lieu of 903 | Does not make the building “sprinklered throughout” for other chapters | Conditional | Do not take egress or rating reductions on a clean-agent or hood system | Verified |
| 904.2.2 | Type I hood extinguishing | Each required commercial kitchen exhaust hood and duct system required by SBC 801 §609 or SBC 501 Chapter 5 to have a Type I hood shall be protected with an approved automatic fire-extinguishing system | Type I hood required | Hood-type rules live in SBC 501 / SBC 801 (not imported) | Conditional | If a Type I amenity or staff kitchen exists, specify a 904.13 system | External verification |
| 904.13.1 | Hood manual actuator | Locate a manual actuation device at or near a cooking-area means of egress, not less than **3 m** and not more than **6 m** from the kitchen exhaust system; install not more than **1200 mm** and not less than **1050 mm** above the floor; maximum force **178 N** and maximum movement **350 mm** | 904.13 commercial cooking system | Automatic sprinkler systems need not have this manual means | Conditional | Dimension the pull station on the kitchen plan | Verified |
| 904.13.2 | Cooking fuel/power shutdown | Actuation shall automatically shut down fuel or electrical power to the cooking equipment; reset shall be manual | 904.13 system | None stated | Conditional | Show interlock to gas/electric cooking equipment | Verified |
| 904.14 | Domestic cooking in R-2 dormitories | Cooktops and ranges in Group R-2 college dormitories per 420.11 shall be protected per 904.14.1 (UL 300A hood system or 30-minute ignition-resistant burners) | R-2 college dormitory domestic cooking | Ordinary R-2 apartments are not this trigger | Conditional | Open only if the building is college/university staff or student housing with 420.11 cooking | External verification |

## 10. Standpipe systems

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 905.2 | Standpipe standard | Install standpipes per this section and NFPA 14; FDCs per 912 | Required standpipe | Hydraulic criteria live in NFPA 14 (not imported) | Direct | Specify NFPA 14; do not import residual-pressure values from memory | External verification |
| 905.3.1 | Height-based Class III standpipe | Install Class III standpipes throughout where any apply: **four or more** stories above or below grade plane; highest floor more than **9 m** above lowest FD vehicle access; lowest floor more than **9 m** below highest FD vehicle access | Building height vs FD access | Exception 1: Class I allowed if sprinkled per 903.3.1.1 or 903.3.1.2. Exceptions 2–5: Class I in B/E, parking, sprinkled basements, or where occupant hose will not be used. Exception 6: ignore recessed docks ≤ **four** vehicles and impractical topography | Direct | Provide at least Class I (sprinklered-building exception) on a combined riser; lock wet vs manual with NFPA 14 and the high-rise status | Verified |
| 905.3.8 | Landscaped-roof standpipe | If the building has a standpipe and a landscaped roof, extend the standpipe to that roof level | Landscaped roof present | None stated | Conditional | Terminate a hose valve at the landscaped roof | Verified |
| 905.4 | Class I hose-connection locations | Provide Class I hose connections: in every required interior exit stairway at each story (main floor landing unless otherwise approved); each side of a horizontal-exit wall; every exit passageway entrance; roof with slope less than **4:12 (33.3-percent)** at the roof or highest stair landing with 1011.12 access; additional locations if remote floor portion exceeds **45 m** (nonsprinklered) or **60 m** (sprinklered) from a hose connection | Class I standpipe | Single connection permitted in an open corridor/breezeway between open stairs not greater than **23 m** apart. Horizontal-exit / exit-passageway valves may be omitted if the floor is reachable by a **9 m** hose stream from a nozzle on **30 m** of hose | Direct | Place a hose valve at each stair floor landing; add extra valves if travel exceeds **60 m** on this sprinkled tower | Verified |
| 905.4.1 | Standpipe riser protection | Protect Class I risers and laterals not in an interior exit stairway to the same fire resistance as required vertical enclosures | Combined riser outside a stair | In a fully sprinkled building, laterals outside a stair need not be in rated construction | Direct | Keep the main riser in the exit stair; if a lateral leaves the stair, apply the sprinkled-building lateral exception or match shaft rating | Verified |
| 905.4.2 | Interconnection | Where more than one standpipe is provided, interconnect per NFPA 14 | Multiple standpipes | None stated | Direct | Interconnect risers; do not import NFPA 14 supply sizes here | External verification |
| 905.7.1 | Cabinet lettering | Identify cabinets with a permanently attached contrasting sign, letters not less than **50 mm** high | Fire-fighting equipment cabinets | Pictogram if the door is too small; glass-panel doors need not be marked | Conditional | If hose/extinguisher cabinets are used, apply **50 mm** lettering | Verified |

## 11. Portable fire extinguishers

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 906.1 | R-2 extinguisher locations | Install portable extinguishers in Group R-2 occupancies. Exception 1: if each dwelling unit has a minimum **1-A:10-B:C** extinguisher, common-area extinguishers are required only in Items 2–6 (cooking **9 m**, flammable liquids, construction, Table 906.1, special-hazard rooms) | Group R-2 | Item 2 cooking **9 m** also names R-2 college dormitories separately | Direct | Either distribute NFPA 10 extinguishers in common areas or put a **1-A:10-B:C** unit in every dwelling and still cover Items 2–6 | Verified |
| 906.3.1 / Table 906.3(1) | Class A distribution | Size and distribute Class A extinguishers per Table 906.3(1). Concatenated OCR: Light/Ordinary/Extra minimum ratings, **280 / 140 / 100 m²** per unit of A, **1,045 m²** max area, travel **23 m**. No reconstructed cell is adopted | Class A hazard occupancy | Footnote a: two **9.5 Liter** water-type = one 4-A. Footnote c: two 1-A water-type = one 2-A in Light Hazard | Direct | Verify the published table before locking rating and **23 m** travel; do not copy flattened **280 / 140 / 100** tokens as design-release values | Verify source |
| 906.3.2 / Table 906.3(2) | Class B shallow-liquid distribution | For flammable/combustible liquids **≤ 6.5 mm** deep, use Table 906.3(2). Extra-High row is concatenated `20-B1540-B980-B15`. No reconstructed rating/travel pair is adopted | Class B hazard with shallow liquid | Deeper liquids go to NFPA 10 (not imported) | Conditional | If a shallow Class B hazard exists, verify the published Extra-High row before specifying 20-B / 40-B / 80-B travel | Verify source |
| 906.9.1–906.9.3 | Extinguisher mounting | Gross weight **≤ 18 kg**: top not more than **1500 mm** above the floor. Gross weight **> 18 kg**: top not more than **1000 mm**. Bottom clearance not less than **100 mm** | Hand-held extinguishers | Wheeled units follow 906.10 | Direct | Put mounting heights on the interior-detail sheet | Verified |

## 12. Group R-2 fire alarm and unit smoke alarms

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 907.2.9.1 | R-2 manual fire alarm | Install a manual fire alarm that activates 907.5 occupant notification where any apply: a dwelling/sleeping unit is **three or more** stories above the lowest LED; a unit is more than **one** story below the highest LED of its exits; the building contains more than **16** dwelling or sleeping units | Group R-2 | Exception 1: ≤ **two** stories with **1-hour** partitions and each unit exiting directly to a public way/court/yard. Exception 2: omit manual boxes if sprinkled per 903.3.1.1 or 903.3.1.2 and waterflow activates occupant notification throughout the zones. Exception 3: omit the fire alarm in sprinkled buildings with no interior corridors and direct/open-ended-corridor egress | Direct | This high-rise trips the three-story and likely the 16-unit tests. Exception 2 may omit pull stations but does **not** delete the 907.2.13 high-rise alarm/EVACS | Verified |
| 907.2.9.2 / 907.2.11.2 | Unit smoke-alarm locations | Install listed UL 217 single- or multiple-station smoke alarms regardless of occupant load: on the ceiling or wall outside each separate sleeping area in the immediate vicinity of bedrooms; in each sleeping room; on each story within the dwelling unit including basements (not crawl spaces or uninhabitable attics). Split levels without an intervening door may share the upper-level alarm if the lower level is less than one full story below | R-2 dwelling/sleeping units | 907.2.11.7 fire-alarm smoke detectors may substitute with in-unit-only notification | Direct | Show three-location smoke alarms on every unit typical | Verified |
| 907.2.11.3 | Smoke alarms near cooking | Do not install ionization alarms less than **6 m** horizontally from a permanent cooking appliance; ionization with a silence switch less than **3 m**; photoelectric less than **1.8 m**, unless that would prevent a required 907.2.11.2 location | Cooking appliance in or adjacent to a required alarm location | Required-location override is stated | Direct | Dimension kitchen/living smoke alarms off the cooktop | Verified |
| 907.2.11.4 | Smoke alarms near bathrooms | Install smoke alarms not less than **900 mm** horizontally from a bathroom door/opening with a bathtub or shower unless that would prevent a required location | Bathroom with tub/shower | Required-location override is stated | Direct | Keep bedroom alarms **900 mm** from the bath door | Verified |
| 907.2.11.5 | In-unit interconnection | Where more than one smoke alarm is required in a unit, activation of one shall activate all in that unit. Listed wireless interconnection is permitted. The alarm shall be clearly audible in all bedrooms with intervening doors closed | Group R units | Physical wiring not required for listed wireless | Direct | Specify interconnect (wired or listed wireless) on the unit electrical typical | Verified |
| 907.2.11.6 | Smoke-alarm power | Primary power from building wiring on a commercial source, with battery backup. Integral-strobe alarms without battery backup shall use Section 2702 emergency power. Permanent wiring; no disconnect other than overcurrent protection | New construction | Battery backup not required if connected to a 2702 emergency system | Direct | Circuit unit smoke alarms from house power with battery backup | External verification |
| 907.2.9.3 | College/university R-2 detection | Automatic smoke detection activating 907.5 is required in college/university student or staff housing in common spaces, laundry/mechanical/storage rooms, and interior corridors serving units, with unit smoke alarms interconnected to the fire alarm per NFPA 72 | R-2 operated by a college or university for student or staff housing | Exception: no interior corridors and each unit opens to exterior exit access or directly to an exit | Conditional | Open only if the occupancy is campus housing; do not apply to a market apartment tower | External verification |

## 13. High-rise detection, EVACS and fire-department communications

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 907.2.13 | High-rise alarm package | Provide an automatic smoke detection system per 907.2.13.1, a fire-department communication system per 907.2.13.2, and an emergency voice/alarm communication system per 907.5.2.2 | High-rise buildings | Airport towers, open parking, A-5, low-hazard special occupancies, H-1/H-2/H-3; I-1/I-2 staff-attended private mode | Direct | Include detection, FD communications and EVACS on the fire-alarm riser; R-2 is not a listed exception | Verified |
| 907.2.13.1.1 | High-rise area smoke detection | Connect smoke detectors to the automatic fire alarm; activation shall start EVACS. In addition to 907.2.1–907.2.9: detectors in each unsprinklered mechanical/electrical/transformer/telephone or similar room, and in each elevator machine room, machinery space, control room, control space **and elevator lobbies** | High-rise | Elevator rooms and lobbies require detectors even if sprinkled | Direct | Show lobby and elevator-machine-room detectors on every typical floor | Verified |
| 907.2.13.1.2 | High-rise duct smoke detection | Duct detectors per 907.3.1: in the main return/exhaust plenum of each air-conditioning system greater than **940 liters per second**, downstream of the last inlet; and at each connection to a vertical duct/riser serving **two or more** stories. In Group R-2, a smoke detector is allowed in each return-air riser carrying not more than **2360 liters per second** and serving not more than **10** air-inlet openings | HVAC capacity and risers | R-2 riser alternative is optional | Direct | Coordinate duct detectors with mechanical; use the R-2 **2360 L/s / 10-inlet** alternative only where those limits are met | Verified |
| 907.2.13.2 | Wired FD communication alternative | Where a wired communication system is approved in lieu of in-building two-way emergency-responder coverage per SBC 801 §510, install it per NFPA 72 between the 911 fire command center, elevators, elevator lobbies, emergency/standby power rooms, fire-pump rooms, areas of refuge and interior exit stairways, with a device at each stair floor | Wired system approved in lieu of radio coverage | Default path is SBC 801 §510 radio coverage (918.1) | Conditional | Prefer 918.1 radio coverage; if a wired substitute is approved, put jacks at the listed rooms and each stair floor | External verification |
| 907.2.13.3 | Multi-channel voice evacuation | In buildings with an occupied floor more than **36 m** above the lowest level of fire department vehicle access, high-rise voice evacuation shall be multiple-channel | Occupied floor **> 36 m** above FD access | Occupied floor stated above **23 m** but **36 m** is unconfirmed | Conditional | If the occupied floor exceeds **36 m**, specify a multi-channel EVACS | Verified |
| 907.5.2.2 | EVACS operation and paging zones | Design EVACS per NFPA 72. Automatic detector, waterflow or manual box shall sound an alert tone then voice instructions. In high-rise buildings the system shall operate on at least the alarming floor, the floor above and the floor below. Provide speakers throughout by paging zones, minimum: elevator groups; interior exit stairways; each floor; areas of refuge | Required EVACS | Group I-1/I-2 constantly attended / overhead page | Direct | Zone EVACS by floor ±1, stairs, elevator groups and any area of refuge | External verification |
| 907.5.2.2.1–907.5.2.2.3 | EVACS override and live voice | Provide manual override on a selective and all-call basis; live voice by paging zone; other announcements allowed if fire-alarm use takes precedence | EVACS | None stated | Direct | Show selective/all-call microphones at the FCC | Verified |
| 907.5.2.2.5 | EVACS standby power | Provide standby power per Section 2702 | EVACS | 2702 values are not imported | Direct | Put EVACS on the standby-power schedule | External verification |

## 14. Occupant notification, zoning and R-2 visible capability

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 907.4.2.1 | Manual-box location | Locate manual fire alarm boxes not more than **1500 mm** from each exit entrance. In buildings not sprinkled per 903.3.1.1 or 903.3.1.2, additional boxes so travel does not exceed **60 m** | Manual fire alarm required | 907.2.9.1 Exception 2 may omit boxes if waterflow notifies | Direct | If pull stations remain, place them within **1500 mm** of each exit; the **60 m** extra-box rule does not apply to this 13-sprinkled tower | Verified |
| 907.4.2.2 | Manual-box height | Activating handle/lever not less than **1000 mm** and not more than **1200 mm** above the floor | Manual boxes provided | None stated | Conditional | Put **1000–1200 mm** on the device height typical | Verified |
| 907.5.2.1.1–907.5.2.1.2 | Audible sound pressure | Provide **15 dBA** above average ambient or **5 dBA** above the maximum sound lasting not less than **60 seconds**, whichever is greater, in every occupiable space. Combined level shall not exceed **110 dBA**; if average ambient exceeds **105 dBA**, visible appliances per NFPA 72 replace audible | Occupant notification | I-2 critical-care exceptions are not this occupancy | Direct | Have the fire-alarm designer prove **15 / 5 / 110 dBA** in units, corridors and amenities | Verified |
| 907.5.2.1.3.1–907.5.2.1.3.2 | 520 Hz sleeping-room signals | In R-2 sleeping rooms, the fire-alarm audible signal shall be a **520-Hz** low-frequency signal per NFPA 72. Where 907.2.9 requires a fire alarm, unit smoke-alarm signals in sleeping rooms shall also be **520 Hz**, or a listed 520 Hz appliance/detector shall provide it | R-2 sleeping rooms | Applies because 907.2.9 / 907.2.13 require a fire alarm | Direct | Specify **520 Hz** bases or sounders in bedrooms | External verification |
| 907.5.2.3.1 | Visible alarms in common areas | Provide visible alarm notification appliances in public-use and common-use areas | Required fire alarm | Employee work areas with audible coverage: circuits initially designed with not less than **20-percent** spare capacity for future visibles | Direct | Put strobes in lobbies, corridors, amenities and other common-use rooms | Verified |
| 907.5.2.3.3 | R-2 future visible capability | In Group R-2 required by Section 907 to have a fire alarm, each story containing dwelling or sleeping units shall support future visible appliances per ICC A117.1 Chapter 11 (wired or wireless) | R-2 with a required fire alarm | A117.1 geometry is not imported | Direct | Show spare capacity / access points per 907.5.2.3.3.1; obtain A117.1 Chapter 11 separately | External verification |
| 907.5.2.3.3.1 | Wired future-visible capacity | Wired path: replacement with combination appliances, or future extension from unit smoke-alarm locations, **or** fire-alarm power supply and circuits with not less than **5-percent** excess capacity and a single access point on every story (circuits need not extend beyond that point). Document on 907.1.2 shop drawings | Wired future-visible option | Wireless equipment is an alternative under 907.5.2.3.3 | Conditional | If wired, show **5-percent** spare and one access point per residential story | Verified |
| 907.6.3 | Initiating-device identification | Identify specific device address, location, type, floor and status (normal/alarm/trouble/supervisory) | Fire alarm system | Exceptions include single-story buildings **< 2100 m²**, systems with only pull stations + waterflow + not more than **10** additional devices, devices that cannot support IDs, and replacements | Direct | Specify addressable identification; the small-building exceptions do not fit this high-rise | Verified |
| 907.6.4 | Alarm zoning | Zone each floor separately; a zone shall not exceed **2100 m²** and shall not exceed **90 m** in any direction | Fire alarm system | Sprinkler zones may follow NFPA 13 area limits | Direct | Split large floor plates so no alarm zone exceeds **2100 m² / 90 m** | Verified |
| 907.6.4.2 | High-rise separate initiating zones | In high-rise buildings, provide a separate zone by floor for smoke detectors, sprinkler waterflow devices, manual boxes and other approved automatic fire-protection systems, where provided | High-rise | None stated | Direct | Annunciate detectors, waterflow and pull stations as separate floor zones at the FCC | Verified |
| 907.6.6 | Fire-alarm monitoring | Required fire-alarm systems shall be monitored (source text is OCR-repeated). Exceptions in the remnant include Group I-3 smoke detectors and one- and two-family sprinklers | Required fire alarm | Confirm published 907.6.6 wording | Direct | Monitor the system at a supervising station per 901.6.3; verify published 907.6.6 before specification freeze | Verify source |

## 15. Smokeproof enclosures (Chapter 9 geometry)

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 909.20 | Smokeproof-enclosure trigger | Where required by Section 1023.12, construct a smokeproof enclosure per this section (stair/ramp plus open balcony, ventilated vestibule, or pressurized stair and vestibule). Roof access required by SBC 801 shall be from the smokeproof enclosure | 1023.12 requires a smokeproof enclosure | 1023.12 values are not imported | External verification | Confirm Chapter 10 whether high-rise interior exit stairs must be smokeproof; then pick one 909.20 method | External verification |
| 909.20.1 | Vestibule size | Access by vestibule or open exterior balcony. Vestibule minimum dimension not less than the required corridor width, and not less than **1.1 m** wide and **1.8 m** long in the direction of egress travel | Vestibule method | Pressurization alternative 909.20.5 may omit the vestibule | Conditional | If a vestibule is used, plan **1.1 m × 1.8 m** clear | Verified |
| 909.20.3.2–909.20.3.3 | Natural-ventilation vestibule | Vestibule-to-stair door not less than a **20-minute** fire-protection rating. Each vestibule: minimum net **1.5 m²** opening facing an outer court, yard or public way not less than **6 m** wide | Natural-ventilation alternative | Building-to-vestibule door is a Section 716 fire door | Conditional | Use only where an outdoor court **≥ 6 m** can take the **1.5 m²** opening | Verified |
| 909.20.4.2 | Mechanical-vestibule ventilation | Not less than **one** air change per minute; exhaust not less than **150 percent** of supply; supply within **150 mm** of the floor; exhaust register top not more than **150 mm** down from the top of the smoke trap | Mechanical-ventilation alternative | Engineered path 909.20.4.2.1: **90** air changes per hour, sized for **three** vestibules | Conditional | If this method is selected, show supply/exhaust registers and the smoke trap on the stair detail | Verified |
| 909.20.4.3 | Vestibule smoke trap | Vestibule ceiling not less than **500 mm** higher than the door opening into the vestibule | Mechanical-ventilation alternative | Height may be decreased if approved and justified by design and test | Conditional | Keep a **500 mm** ceiling step at the vestibule door | Verified |
| 909.20.4.4 | Shaft pressure vs vestibule | Maintain minimum **25 Pa** positive in the shaft relative to the vestibule with all doors closed | Mechanical-ventilation alternative | None stated | Conditional | Commission **25 Pa** shaft-to-vestibule | Verified |
| 909.20.5 | Stair pressurization without vestibule | Where sprinkled throughout per 903.3.1.1, the vestibule is not required if each interior exit stair/ramp is pressurized to not less than **25 Pa** and not more than **85 Pa** relative to the building, all doors closed, under maximum stack and wind | NFPA 13 building electing pressurization-only | This is the usual high-rise 13 path | Conditional | If vestibules are omitted, design **25–85 Pa** stair pressurization | Verified |
| 909.20.6.2–909.20.6.3 | Pressurized stair and vestibule | Stair **≥ 12.50 Pa** positive vs vestibule; vestibule **≥ 12.50 Pa** positive vs the fire floor; door-opening force not more than **133 N**. Relief vent not less than **1180 liters per second** at the design pressure difference | Pressurized stair + vestibule alternative | Door assemblies as 909.20.6.1 | Conditional | If this method is selected, meet the two **12.50 Pa** differentials and the **1180 L/s** relief | Verified |
| 909.20.7.1 | Independent ventilation protection | Smokeproof ventilation shall be independent of other building ventilation. Equipment, control wiring, power wiring and ductwork: exterior; or inside the enclosure; or inside the building behind **2-hour** barriers/horizontal assemblies | Mechanical 909.20.4/5/6 methods | Wiring outside the **2-hour** enclosure: UL 2196 **2-hour** cable, **50 mm** concrete encasement, or **2-hour** electrical circuit protective system | Conditional | Keep pressurization plant on a **2-hour** path or listed **2-hour** wiring | Verified |
| 909.20.7.2 | Smokeproof standby power | Mechanical vestibule/shaft ventilation and automatic fire detection shall have standby power per Section 2702 | Mechanical smokeproof methods | 2702 values are not imported | Conditional | Put smokeproof fans and detectors on standby power | External verification |
| 909.21.1 | Elevator hoistway pressurization | Where hoistway pressurization is used in lieu of required enclosed elevator lobbies: **25 Pa** minimum and **65 Pa** maximum vs adjacent occupied space, measured at mid-door with cars at recall. Outside air intake not less than **6 m** from any exhaust | Pressurization in lieu of 3006 lobbies | Exception 1: on floors containing only Group R, measure vs a dwelling/sleeping unit. FSAE/OEE enclosed lobbies are not replaced by pressurization (named in commentary — not used as a value) | Conditional | Use only if Chapter 30 allows this substitute; commission **25–65 Pa** and a **6 m** intake offset | Verified |

General Section 909 atrium/assembly smoke-control equations, 910 smoke-and-heat vents (Group F-1/S-1 **4650 m²**), and Group I corridor-door rules are omitted from project-use unless mixed-use opens those features in the gap register.

## 16. Fire command center

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 911.1 | Fire command center required | Provide a fire command center in buildings classified as high-rise, and in F-1/S-1 occupancies with footprint over **46450 m²** | High-rise classification | F-1/S-1 footprint trigger is not this occupancy | Direct | Provide an FCC; do not use the **9 m²** F-1/S-1 size | Verified |
| 911.1.1 | FCC location | Location and accessibility shall be approved by the fire code official | Required FCC | None stated | Direct | Obtain fire-code-official approval of FCC location, typically at the main fire-department entry | Verified |
| 911.1.2 | FCC separation | Separate from the remainder of the building by not less than a **1-hour** fire barrier (707) or horizontal assembly (711), or both | Required FCC | None stated | Direct | Draw a **1-hour** FCC enclosure with listed opening protectives | Verified |
| 911.1.3 | FCC size | Not less than **0.015 percent** of the total building area served or **20 m²**, whichever is greater, with minimum dimension **0.7** times the square root of the room area or **3 m**, whichever is greater | High-rise FCC | F-1/S-1 footprint **> 46500 m²** may use **9 m² / 2.4 m** where approved — not this tower. Do not use commentary **18.35 m²** | Direct | Plan the FCC at least **20 m²** with minimum dimension **3 m**, and increase if **0.015 percent** of building area is greater | Verified |
| 911.1.5 | FCC storage ban | Storage unrelated to FCC operation is prohibited | Required FCC | None stated | Direct | Keep the FCC off the furniture/storage inventory | Verified |
| 911.1.6 | FCC required features | Comply with NFPA 72 and provide the listed controls and information: EVACS control unit; FD communications; fire-alarm annunciator; elevator status; air-distribution status/controls; 909.16 firefighter’s smoke-control panel where smoke control is installed; simultaneous interior-exit-stair unlock; sprinkler valve/waterflow display; emergency/standby power status; FD telephone; fire-pump status; schematic plans; Building Information Card (13.1–13.7); work table; generator supervision/start/transfer; public-address where required elsewhere; elevator fire-recall switch (ASME A17.1); elevator emergency/standby power selector where provided | Required FCC | NFPA 72 layout and ASME A17.1 switch details are not imported | Direct | Freeze an approved 911.1.4 layout that includes every listed feature; do not treat the work table as optional | External verification |
| 911.1.7 | FCC identification | Permanent easily visible sign on the door reading `FIRE COMMAND CENTER` | Required FCC | None stated | Direct | Put the exact legend on the door schedule | Verified |

## 17. Fire department connections, fire pumps and shaft markings

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 912.2–912.2.1 | FDC location | Locate FDCs so connected apparatus and hose will not obstruct access for other apparatus; location approved by the fire code official. Place on the street side or facing approved fire-apparatus access roads, fully visible and recognizable, unless otherwise approved | Sprinkler and standpipe FDCs | Existing-building sign path is 912.2.2 | Direct | Coordinate FDC location with SCD access; keep it visible from the approach road | Verified |
| 912.2.2 | Existing FDC sign | Where an existing FDC is not visible, provide an approved sign with letters `FDC` not less than **150 mm** high and other words or an arrow not less than **50 mm** high | Existing building, FDC not visible | New-build FDCs should be visible per 912.2.1 | Conditional | Use only on existing-building alterations | Verified |
| 912.4.2 | FDC working space | Maintain not less than **900 mm** width, **900 mm** depth and **1.95 m** height in front of and to the sides of wall-mounted FDCs and around free-standing FDCs, unless otherwise required or approved | Wall-mounted or free-standing FDC | Fire-code-official may modify | Direct | Keep a **900 × 900 × 1.95 m** clear box at the FDC | Verified |
| 912.5 | FDC identification sign | Metal sign with raised letters not less than **25 mm**: AUTOMATIC SPRINKLERS, STANDPIPES, TEST CONNECTION, or a combination; identify served portions if the FDC does not serve the entire building | Sprinkler, standpipe or fire-pump FDC | None stated | Direct | Specify a **25 mm** raised-letter metal FDC sign | Verified |
| 913.1 | Fire-pump standard | Where provided, install fire pumps per this section and NFPA 20 | Fire pump provided | Exception: 13D / SBC 1101–1102 pumps | Direct | A high-rise 13 system will typically need a pump; design to NFPA 20 (not imported) | External verification |
| 913.2.1 | Fire-pump room rating | Locate fire pumps in rooms separated by **2-hour** fire barriers or **2-hour** horizontal assemblies, or both | Fire pump in the building | Exception 1 (**1-hour** in a fully sprinkled non-high-rise) does **not** apply to high-rise. Exception 2: physical separation per NFPA 20 | Direct | Enclose the pump room **2 hours**; do not take the 1-hour non-high-rise exception | Verified |
| 913.2.2 | Fire-pump circuit survivability | Protect cables for survivability of circuits supplying fire pumps by UL 2196 **1-hour** listed cable, a **1-hour** electrical circuit protective system, **1-hour** construction, or encasement in not less than **50 mm** of concrete | Fire-pump supply circuits | Exception: cables inside a fire-pump or generator room that is already fire-resistance separated | Direct | Show a **1-hour** survivability method from the source to the pump room | Verified |
| 913.3 | Pump-room temperature | Maintain the pump room or pump house above **5 °C** | Pump room/house where required | Engine manufacturer’s minimum may be higher (913.3.1) | Direct | Heat the pump room above **5 °C** (and above **4 °C** per 902.1.3) | Verified |
| 914.1.1–914.1.2 | Shaftway markings | Mark outside openings onto a multi-story hoistway/shaftway, and interior door/window openings onto a shaftway, with `SHAFTWAY` in red letters not less than **150 mm** high on a white background | Openings onto communicating shafts | Interior markings not required where the opening is readily discernible as a shaftway by construction | Direct | Put **150 mm** SHAFTWAY signs on exterior shaft openings and on non-obvious interior shaft doors | Verified |

## 18. Carbon monoxide detection and emergency responder radio

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 915.1.1 | Group R CO detection | Provide carbon monoxide detection in Group R occupancies in 915.2 locations where any 915.1.2–915.1.6 condition exists | Group R with a listed fuel-burning or garage condition | Open/enclosed parking garages per 406.5/406.6 are not “private garages” (915.1.6) | Conditional | If the tower is all-electric with no fireplace, furnace or attached private garage, CO detection is not charged by this section | Verified |
| 915.1.2–915.1.4 | Fuel-burning CO triggers | Detect in units that contain a fuel-burning appliance or fireplace; units served by a fuel-burning forced-air furnace; and units in buildings that contain fuel-burning appliances/fireplaces | Those fuel-burning conditions | 915.1.3: detector in the first room served by each main duct with alarm to an approved location. 915.1.4: no communicating openings, or listed remote-detector locations | Conditional | Map every gas appliance; apply the communicating-opening exceptions only where proven | Verified |
| 915.1.5 | Attached private-garage CO | Provide CO detection in units in buildings with attached private garages | Attached private garage | No communicating openings; units more than one story above or below; open-ended-corridor connection; detector between garage openings and units. 915.1.6: 406.5/406.6 parking is not a private garage | Conditional | Typical podium parking is 406.5/406.6, not a private garage; apply only to true attached private garages | Verified |
| 915.2.1 | Dwelling-unit CO location | Install outside each separate sleeping area in the immediate vicinity of the bedrooms; if a fuel-burning appliance is in a bedroom or its attached bathroom, install within the bedroom | Required dwelling-unit CO | Sleeping-unit path is 915.2.2 | Conditional | Place CO alarms at bedroom halls, and in bedrooms that contain fuel-burning equipment | Verified |
| 915.4.1 | CO-alarm power | Primary power from commercial building wiring; battery on primary-power loss; permanent wiring without a disconnect other than overcurrent protection | CO alarms (UL 2034) | Buildings without commercial power may use battery-only alarms | Conditional | Circuit CO alarms like smoke alarms | Verified |
| 918.1 | Emergency responder radio | Provide emergency responder radio coverage in **all new buildings** in accordance with SBC 801 Section 510 | New buildings | Wired 907.2.13.2 substitute only where approved in lieu of SBC 801 §510 | Direct | Design in-building radio coverage to SBC 801 §510; do not import those signal-strength values here | External verification |

## 19. Project-use controls

1. Use **Verified** rows for initial life-safety and fire-protection scoping after the row trigger and branch are confirmed.
2. Treat every **Verify source** row (flattened extinguisher tables, visible-alarm Table 907.5.2.3.2, 907.6.6 OCR, missing 903.2.11.2 heading, cut-off 909/910 equations) as a design hold point. No affected value is to be placed in issued-for-approval documents without a published-source check.
3. Do not specify NFPA 13R for this high-rise. Do not take 13-only code reductions on any residual 13R or 13D hypothesis.
4. Do not import 403.3, 1023.12, ICC A117.1, SBC 501, SBC 801 §510, NFPA 13/14/20/72 or commentary **18.35 m²** FCC area.
5. Do not apply Group A/E/F/H/I/M/S occupancy-threshold rows, mall/stage/amusement rules, or Table 907.5.2.3.2 R-1 visible counts to this R-2 tower unless the gap register already opened that use.
6. Record sprinkler standard, FD-access datum, mixed-use, FCC location and SCD NOC decisions in the project Golden Thread; this matrix is not evidence of SCD NOC or stamped compliance.

## 20. Coverage summary

Internal inventory of the attached Chapter 9 extract (numbered code, exceptions, tables, footnotes; commentary and figures excluded). Row-level records are not published.

- **Inventory scope:** numbered code, exceptions, tables, footnotes (commentary excluded)
- **Total independently checkable numeric records:** 310
- **Verified:** 251
- **Verify source:** 59

### Counts by top-level section

| Section | Records |
|---|---:|
| 901 | 2 |
| 902 | 3 |
| 903 | 76 |
| 904 | 12 |
| 905 | 22 |
| 906 | 37 |
| 907 | 76 |
| 908 | 0 |
| 909 | 40 |
| 910 | 10 |
| 911 | 6 |
| 912 | 9 |
| 913 | 5 |
| 914 | 4 |
| 915 | 3 |
| 916 | 4 |
| 917 | 1 |
| 918 | 0 |

### Appended-table coverage

| Appended table | Records | Verify source records |
|---|---:|---:|
| Table 903.2.5.2 (H-5 hazard names; no SI cells) | 0 | 0 |
| Table 903.2.11.6 (outbound section pointer) | 0 | pointer OCR hold (non-numeric) |
| Table 906.1 (SBC 801 pointer) | 0 | pointer OCR hold (non-numeric) |
| Table 906.3(1) Class A distribution | 12 | 12 |
| Table 906.3(1) footnotes a, c | 4 | 0 |
| Table 906.3(2) Class B distribution | 10 | 10 |
| Table 907.5.2.3.2 visible alarms (I-1/R-1) | 34 | 34 |

Coverage cross-check against `SBC 201 Chapter 9 Fire Protection Systems (2024)_CS.md` was topics-only: Group R sprinkler-throughout; 13R four-story / **9 m** limit; high-rise EVACS/FCC; standpipe height. No CS.md value was copied into a matrix cell.

## 21. Unresolved-source register

Hold points for the 59 **Verify source** inventory records, plus two non-numeric OCR/heading holds (903.2.11.2, 907.6.6). Counts are record counts, not distinct numeric values. No value in this register is a design-release figure.

| Affected table / clause | Why unverified | Control note |
|---|---|---|
| Table 903.2.11.6 | Concatenated section/subject pointer, including **403.3 High-rise buildings** | Record the outbound pointer only; obtain published Chapter 4 / 403.3 before using high-rise suppression text |
| Table 906.1 | Concatenated SBC 801 section list | Do not reconstruct extinguisher locations from flattened 801 cites |
| Table 906.3(1) | 12 concatenated Light/Ordinary/Extra cells (**2-A / 4-A**, **280 / 140 / 100 m²**, **1,045 m²**, **23 m**) | Verify the published table before locking Class A rating and travel; footnotes a/c (**9.5 Liters**, 1-A/2-A/4-A equivalents) are readable |
| Table 906.3(2) | Extra-High row concatenated `20-B1540-B980-B15`; remaining cells flattened | Do not reconstruct 20-B / 40-B / 80-B travel; verify the published table if a Class B hazard exists |
| Table 907.5.2.3.2 | Concatenated I-1/R-1 visible-alarm counts | Omit from R-2 project-use; do not use reconstructed sleeping-unit percentages |
| 903.2.11.2 | Code heading missing; chute-sprinkler body is attached after 903.2.11.1.3 | Confirm published heading and alternate-floor / lowest-intake placement before issuing the chute detail |
| 907.6.6 | Source text OCR-repeats “monitored by this chapter or by SBC 801” | Use 901.6.3 for supervising-station intent; verify published 907.6.6 wording |
| 909.6.2 | Door-opening-force equation cut off after “determined by:” | Do not invent the force equation; use 909.20.5 / 909.20.6.2 numeric caps where those methods apply |
| 909.10.1 | Exhaust-fan temperature-rise equation cut off after “computed by:” | Do not invent the temperature-rise formula; keep fans as 909.10 performance |
| 910.3.3 | Smoke-and-heat vent area formula cut off after “calculated as follows:” | Group F-1/S-1 vents are not typical; verify the published formula if 910 is opened |
