# SBC 201 Chapter 11 Accessibility — Group R-1 High-Rise Dimensional Requirements Matrix (2024)

## 1. Document metadata and use limitation

- **Project basis:** Mixed-use tall building containing Group R-1 (hotel) with Group R-2 residential and Group B office/amenities sharing podium, parking and routes. An occupied floor is stated to be more than 23 m above the relevant reference level. This matrix filters Chapter 11 for the **Group R-1 hotel** portion.
- **Deliverable tier:** Project-use matrices in Sections 1–17 (design-check rows, not pasted inventory), plus a coverage summary and unresolved-source register. The full row inventory is not published.
- **Code/source basis:** SBC 201 (2024), Chapter 11, source file `Reference\SBC 201 2024\source_reference\Chapter_11 — ACCESSIBILITY.txt`.
- **Extraction audit:** Internal inventory: **276** independently checkable numeric records (**192** Verified, **84** Verify source). Unresolved OCR is listed in the register and is not a design-release value.
- **Model:** Cursor Grok 4.6.
- **Prepared:** 2026-08-28.
- **Status:** Source-only architectural advisory matrix for design coordination. It is not a stamped compliance statement, accessibility consultant report, SCD NOC, SBPS approval, legal opinion, or permission to construct.
- **Outbound-source rule:** No value in this matrix has been imported from ICC A117.1, Chapter 10, Chapter 9, Section 403, Chapter 30, SBC 701, SBC 901, HUD/FHAG, ADA, commentary examples, or the chapter summary. Where Chapter 11 sends the user elsewhere, this matrix records the dependency without supplying the outbound value.

### Scope and assumptions

1. Group R-1 and high-rise status are project statements, not independently verified classifications.
2. The mixed-use podium with Group R-2 and Group B is a project statement. Shared routes, parking, EV, recreation and public entrances must be assigned to an occupancy before a row is used as Direct.
3. The exact AHJ/permit pathway, project stage and SCD NOC status are unconfirmed; therefore this matrix does not conclude compliance.
4. Typical transient hotel path is **Section 1108.6.1.1** (Accessible units per Table 1108.6.1.1). Type B units apply only where units are **intended to be occupied as a residence** (1108.6.1.2).
5. Automatic sprinkler protection is not selected in this chapter extract. Chapter 11 does not branch hotel unit scoping on NFPA 13 versus 13R.
6. Guestroom count, parking counts/types, valet, banquet/F&B, recreation layouts and EV provision are unconfirmed.
7. Chapter 11 is **scoping**. Technical millimetre geometry for accessible routes, doors, toilets, kitchens and Accessible units is ICC A117.1. Charging **1102.1** names ICC A117.1 with **no edition year**. General Comments name 2009; later commentary discusses 2017 anthropometry. Neither commentary year is adopted as a charging substitution.
8. All eight appended tables are concatenated OCR. No reconstructed cell is adopted as a design-release value. Affected project-use rows are **Verify source**.
9. Group R-2 apartment Type A/B mix, R-2 2-percent parking, and the 1107.2 R-2 EV exemption are **not** applied to the hotel. See the companion R-2 High-Rise Chapter 11 matrix for the residential tower.

## 2. Legends

### Applicability

| Status | Meaning |
|---|---|
| **Direct** | Expected to govern the stated R-1 hotel basis, subject to confirmed geometry and design data. |
| **Conditional** | Governs only when the stated feature, use, occupant load, unit type or mixed-use/podium condition exists. |
| **Not typical** | Unrelated occupancy-only rule; omitted from this deliverable unless the gap register already opened that use. |
| **External verification** | Chapter 11 points to another section/code/standard, or the project/AHJ basis must be confirmed before use. |

### Source confidence

| Status | Meaning |
|---|---|
| **Verified** | Requirement and any stated numeric value were checked against unambiguous mandatory Chapter 11 source text. |
| **Verify source** | OCR, flattened table, page-split, or footnote attachment is unresolved. Not a design-release value. |

## 3. Project decision and gap register

| Decision / gap | Current project basis | Why it controls Chapter 11 application | Required project action |
|---|---|---|---|
| ICC A117.1 edition | Charging 1102.1 has no year; General Comments name 2009; commentary discusses 2017 | Controls turning spaces, clear floor space, door manoeuvring, Accessible-unit interiors | AHJ/code consultant to lock the referenced edition; do not silently switch editions |
| Transient vs extended-stay | Unconfirmed | 1108.6.1.1 Accessible units always; 1108.6.1.2 Type B only if units are intended as a residence | Freeze hotel operating model (nightly vs corporate/extended stay) before unit typicals |
| Guestroom count and classes | Unconfirmed | Table 1108.6.1.1 quotas; **> 50** units per structure counted separately on a multi-building site; dispersion among classes | Issue a signed key schedule by class (standard, suite, kitchenette, executive) |
| Mixed-use Type B on the same structure | R-2 Type B units stated on the same building | 1104.1 vehicular-way exception does **not** apply to buildings containing or serving Type B units | Provide a pedestrian accessible route from every applicable arrival point; do not use a driveway-only exception |
| Mixed-use power doors | Table 1105.1.1 lists A-1–A-4, **B, M, R-1**; footnote uses most restrictive listed load | Hotel public entrances can be pulled in by Group B/A/M loads even if the hotel load alone is below the table | Sum listed mixed-use occupant loads after published-source check of the table |
| Parking facility split | Unconfirmed shared garage | R-1 uses **1106.3 Item 2 → Table 1106.2**, not the R-2 2-percent rule; calculate **each parking facility** separately (1106.2) | Produce a parking schedule by facility and occupancy served (hotel, residential, office) |
| Valet / porte-cochère | Unconfirmed | 1106.9.3 requires an accessible passenger loading zone at valet; 1106.9.1 spaces accessible zones at **≤ 30 m** | Confirm drop-off length and valet operation |
| Recreation serving which occupancy | Unconfirmed shared pool/gym | Hotel/office recreation uses **1111.3** (all facilities accessible). R-2 Type A/B uses **1111.2.2** (**25%** / ≥ 1). 1111.4.14 Ex. 3 water-entry waiver is **only** on the 1111.2.2/2.3 path | Map every recreational facility to the occupancies it serves |
| EV charging | Unconfirmed | 1107.2 exception is **R-2, R-3, R-4 only** — hotel EV is **not** exempt | If hotel or public chargers exist, apply 1107.2.1 / 1107.2.2 |
| Occupied roof / amenities | Unconfirmed | 1104.4 requires an accessible route to each accessible story, mezzanine and occupied roof; 1108.3 common rooms serving Accessible units must be accessible | Show an accessible route to lobby, F&B, banquet, gym, pool deck and any occupied roof serving the hotel |
| NOC / accessibility consultant | Unconfirmed | Technical A117.1 geometry, assisted-evacuation and SCD acceptance cannot be concluded from Chapter 11 scoping alone | Engage the qualified local accessibility/fire consultants before design freeze |

## 4. Scoping versus technical standard

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-1 hotel status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1101.1 | Chapter scope | This chapter controls design and construction of facilities for accessibility | All facilities in scope | None stated | Direct | Treat Chapter 11 as the scoping document for the hotel and the site elements that serve it | Verified |
| 1102.1 | ICC A117.1 | Accessible in accordance with this code **and ICC A117.1** (no year) | All required accessible facilities | None stated | External verification | Lock the A117.1 edition with the AHJ; do not import millimetre geometry here | Verified |
| 1108.2 | Unit interiors | Accessible / Type A / Type B units comply with applicable portions of **Chapter 11 of ICC A117.1**; higher unit types may substitute | Required unit types | Type A may be built as Accessible; Type B as Accessible or Type A | External verification | Produce Accessible-guestroom typicals from the referenced A117.1 chapter, not from commentary millimetres | Verified |
| 1110.1 Exception | Unit toilets/kitchens | Accessible, Type A and Type B units shall comply with **Chapter 10 of ICC A117.1** | Those unit types | 1110 otherwise still governs common/public features | External verification | Note the source names Chapter 10 here and Chapter 11 at 1108.2; verify the printed A117.1 mapping before detailing | Verified |
| 1108.3 | Common rooms serving units | Rooms and spaces available to the public or residents and serving Accessible, Type A or Type B units shall be accessible, including toilet/bathing, kitchen, living/dining and exterior patios/terraces/balconies | Amenities serving required units | 1108.4 story exemptions; 1111.2 recreation (R-2/R-3/R-4 path, not the hotel 1111.3 path) | Direct | Put lobby, restaurants, banquet, laundry, gym and pool deck on an accessible route serving Accessible guestrooms | Verified |

## 5. General applicability and surviving exceptions

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-1 hotel status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1103.1 | Default accessibility | Sites, buildings, structures, facilities, elements and spaces, temporary or permanent, shall be accessible | All construction | Only to the extent permitted by 1103.2 / 1104–1112 | Direct | Assume accessible unless a numbered exception is proven | Verified |
| 1103.2.2 | Employee work areas | Approach, enter and exit plus 907.5.2.3.1, 1009 and 1104.3.1 only | Employee work areas | Portions **< 28 m²** and **≥ 175 mm** essential level change exempt from all requirements (not courtroom stations) | Conditional | Apply to BOH, kitchens, housekeeping and security desks; keep visible alarm and accessible MOE outbound | Verified |
| 1103.2.9 | Equipment spaces | Spaces frequented only by service personnel for maintenance, repair or occasional monitoring of equipment are not required to comply with this chapter | Service-only equipment spaces | None stated | Direct | Do not force an accessible route into elevator pits, penthouses or typical MEP rooms | Verified |
| 1103.2.14 | Walk-in coolers | Walk-in cooler and freezer equipment accessed only from employee work areas is not required to comply with this chapter | BOH coolers | Public-facing coolers still need operable parts / display on the public side (1110.10.2, 1110.15) | Conditional | Exempt kitchen walk-ins; keep front-of-house display coolers in the operable-parts package | Verified |
| 1104.3.1 Ex. 1 | Small work-area path | Common-use circulation paths in employee work areas **< 100 m²** defined by permanent partitions/furnishings need not be accessible routes | Employee work areas | Equipment-integral and weather-exposed exterior path exceptions also stated | Conditional | Keep an accessible route **to** the work area; the path through a small defined workstation may be exempt | Verified |

## 6. Accessible routes and stories

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-1 hotel status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1104.1 | Site arrival route | At least **one** accessible route from transit, accessible parking, accessible loading, streets/sidewalks to the accessible entrance | Site arrival points | Vehicular-way-only exception **does not apply** to buildings containing or serving Type B units (R-2 on this mixed-use structure) | Direct | Provide a pedestrian accessible route from every applicable arrival point | Verified |
| 1104.2 | On-site connections | At least **one** accessible route connecting accessible buildings, facilities, elements and spaces on the same site | Multiple accessible elements on one site | Vehicular-way-only; recreation only as 1111 | Direct | Connect podium, parking, lobby, F&B and recreation to the same accessible network | Verified |
| 1104.3 | Connected spaces | At least **one** accessible route to each required accessible portion, to accessible entrances connecting accessible walkways, and to the public way | Building required to be accessible | 1104.4 story skips; assembly levels without wheelchair spaces; courtroom workstations; 1111 recreation | Direct | Trace the accessible route from public way through lobby, lifts, guest floors with Accessible units, and amenity floors | Verified |
| 1104.4 | Multistory / occupied roof | At least **one** accessible route shall connect each accessible story, mezzanine and occupied roofs | Multilevel buildings | Exception 1 (**≤ 279 m²** aggregate) does not apply to this elevator high-rise. Exception 2: stories with no 1108/1109 accessible elements need not be served | Direct | Serve every story that contains Accessible units, public use or common use serving those units, including occupied roof | Verified |
| 1104.5 | Route coincidence | Accessible routes shall coincide with or be in the same area as general circulation; interior circulation requires an interior accessible route; a single accessible route shall not pass through kitchens, storage, restrooms, closets or similar | Accessible routes | 2. A single route may pass through a kitchen or storage room **inside** an Accessible, Type A or Type B unit | Direct | Keep common accessible routes in public circulation, not through service rooms | Verified |
| 1108.4 | Route to units | At least **one** accessible route shall connect accessible building entrances with the primary entrance of each Accessible, Type A and Type B unit and with interior/exterior spaces serving the units | Required units | 5. In Group R-1, a route is **not** required to connect stories **within** an individual unit if the accessible level is an Accessible unit **and** provides sleeping for **two** persons minimum **and** a toilet on that level. 7. Type B stories exempted by 1108.7 | Direct | Serve every Accessible guestroom entrance from an accessible building entrance. Do not use Exception 5 to skip hotel stories | Verified |
| 1104.6 | Security barriers | Security barriers shall not obstruct a required accessible route or accessible means of egress | Bollards, checkpoints | Adjacent route permitted around devices that cannot comply (metal detectors), with visual contact of personal items | Conditional | If a lobby security line exists, provide an adjacent accessible path that keeps bags in view | Verified |

## 7. Entrances

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-1 hotel status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1105.1 | Public entrances | At least **60 percent** of all public entrances shall be accessible, in addition to 1105.1.2–1105.1.8 | Public entrances | Areas not required to be accessible; loading/service entrances that are not the only tenant entrance | Direct | Count public doors (not egress-only doors) and make ≥ 60% accessible | Verified |
| 1105.1.1 / Table 1105.1.1 | Power-operated public entrance | One full-power or low-energy power-operated door at each required accessible public entrance when occupancy and building occupant load exceed the table; vestibule: one leaf in and one leaf out | Table lists Groups **A-1–A-4** and **B, M, R-1**. Mixed-use uses the most restrictive listed load | Flattened OCR occupant-load cells are not adopted | Direct | Power-operate accessible hotel public entrances once the published R-1/B/M/A load is confirmed; mixed-use may use the most restrictive listed load | Verify source |
| 1105.1.2 | Parking-garage entrance | Direct pedestrian access from parking structures to building/facility entrances shall be accessible | Direct garage-to-building pedestrian access | None stated | Direct | Provide an accessible pedestrian door from the parking structure into the hotel lobby | Verified |
| 1105.1.3 | Tunnel / walkway entrance | At least **one** accessible entrance from each pedestrian tunnel or elevated walkway | Direct pedestrian access from those links | None stated | Conditional | If a podium link bridge exists, make at least one door from it accessible | Verified |
| 1105.1.4 | Restricted entrance | At least **one** restricted entrance shall be accessible | Restricted (security-controlled) entrances | Key-card staff doors that are not “restricted entrances” are not this section | Conditional | If a members-only or staff-secure hotel entry exists, make at least one of that type accessible | Verified |
| 1105.1.7 | Tenant entrance | At least **one** accessible entrance to each tenant in a facility | Multi-tenant facility | Self-service storage not required to be accessible | Conditional | If podium tenancies exist, give each tenant an accessible entrance in addition to the 60% building count | Verified |
| 1105.1.8 | Unit entrance | At least **one** accessible entrance to each dwelling/sleeping unit | Dwelling and sleeping units | Not required to units that are not Accessible, Type A or Type B | Direct | Every Accessible guestroom gets an accessible entrance; shared lobby doors still count toward 60% | Verified |

## 8. Parking, vans and passenger loading

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-1 hotel status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1106.3 Item 2 | R-1 accessible parking | In Group I-1 and R-1 occupancies, accessible parking shall be provided in accordance with **Table 1106.2** | R-1 parking | Table 1106.2 is flattened OCR. Do **not** use the R-2 **2 percent** rule (Item 1) | Direct | Size hotel accessible stalls from the published Table 1106.2 after source check; calculate each parking facility separately (1106.2) | Verify source |
| Table 1106.2 | General parking table | Flattened OCR table; no reconstructed stall-count cell is adopted | Parking facilities using 1106.2 | R-1 uses this table via 1106.3 Item 2 | Direct | Hold stall counts until the published table is verified; do not reconstruct concatenated cells | Verify source |
| 1106.3 Item 3 | 1:1 parking vs Accessible units | Where at least one parking space is provided for each dwelling/sleeping unit, at least **one** accessible parking space shall be provided for **each Accessible and Type A unit** | Parking provided at ≥ 1 space per unit | Code does not state that Item 2 and Item 3 are additive | Conditional | If assigned 1:1 hotel parking exists, provide an accessible stall for every Accessible guestroom and compare with Table 1106.2 | Verified |
| 1106.3 Item 4 | In-building parking | Where parking is within or beneath a building, accessible parking shall also be within or beneath the building | Parking in/under the building | None stated | Direct | Put accessible stalls in the podium/basement garage, not only on the surface lot | Verified |
| 1106.6 | Van spaces | For every **six** or fraction of six accessible parking spaces, at least **one** shall be van-accessible | Accessible parking provided | **2100 mm** van-height reduction is Group U private garages serving **R-2 and R-3 only** — not R-1 | Direct | Provide 1-in-6 vans; do not use the 2100 mm R-2/R-3 garage exception for hotel stalls | Verified |
| 1106.7 Ex. 1 | Van-space level | In multilevel parking structures, van-accessible parking spaces are permitted on **one** level | Multilevel parking | Accessible spaces still dispersed; van-height millimetres are A117.1 (not imported) | Direct | Concentrate van stalls on the level that can provide the A117.1 van clearance | Verified |
| 1106.9.1 | Continuous loading zone | One accessible passenger loading zone in every continuous **30 m** maximum | Passenger loading zones provided | None stated | Conditional | If a porte-cochère exists, space accessible zones at ≤ 30 m | Verified |
| 1106.9.3 | Valet loading zone | A passenger loading zone shall be provided at valet parking services | Valet parking | Valet does not delete accessible parking | Conditional | If valet is offered, provide an accessible drop-off; still provide 1106 parking | Verified |
| 1112.1 Item 2 | Hotel stall identification | Accessible parking required by 1106.3 shall be identified by the ISA | 1106.3 accessible spaces | Assigned-stall identification exception is **I-1, R-2, R-3, R-4 only** — **not R-1** | Direct | Sign every required hotel accessible stall; do not use the R-2 assigned-space signage exception | Verified |

## 9. Electrical vehicle charging

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-1 hotel status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1107.2 Exception | R-2 EV exemption (not R-1) | EV charging stations provided to serve Groups **R-2, R-3 and R-4** are not required to comply with 1107.2 | EV serving those occupancies | **Group R-1 is not listed** | Direct | Do not apply the residential EV exemption to hotel or public chargers | Verified |
| 1107.2.1 | Accessible EV count | Not less than **5 percent** of vehicle spaces served by EV systems, but not fewer than **one of each type**, shall be accessible | EV systems not covered by the R-2/R-3/R-4 serving exception | None stated beyond 1107.2 | Conditional | If hotel or podium/public chargers exist, reserve 5% (≥ 1 of each charger type) | Verified |
| 1107.2.2 | Accessible EV stall size | **3300 mm** minimum vehicle-space width with adjoining access aisle **1500 mm** minimum | Accessible EV spaces required by 1107.2.1 | None stated | Conditional | Do not substitute a narrower A117.1 van option; this section specifies 3300 + 1500 | Verified |

## 10. Sleeping-unit mix (Accessible / Type B)

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-1 hotel status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1108.6.1.1 | Accessible-unit site vs structure | Accessible units per Table 1108.6.1.1. Multi-building site: structures **> 50** units counted **per structure**; structures **≤ 50** units counted **site-wide**. Disperse among classes of units | Group R-1 dwelling/sleeping units | 1103.2.11 (≤ **five** sleeping units + proprietor residence) is not this tall hotel | Direct | Count guestrooms on the signed key schedule; use the 50-unit split if more than one hotel structure exists | Verified |
| Table 1108.6.1.1 | Accessible-unit quotas | Flattened OCR table (without roll-in / with roll-in / total). No reconstructed cell is adopted | Group R-1 Accessible units | Applies also to congregate R-2 (not this hotel path) | Direct | Provide Accessible guestrooms, including the published roll-in-shower split, only after source check of the table | Verify source |
| 1108.6.1.2 | Type B extended stay | In structures with **four or more** dwelling/sleeping units intended to be occupied as a residence, **every** such unit shall be Type B | Units intended as a residence | Reduction permitted per 1108.7. Typical transient hotel is not this trigger | Conditional | If corporate/extended-stay product is intended as a residence, make every such unit Type B (Accessible units already exceed Type B) | Verified |
| 1108.7.3 | Elevator only to lowest unit story | Where elevator service provides an accessible route **only** to the lowest story containing residence units, only units on **that story** need be Type B | Elevator limited to the lowest unit story | Applies to Type B reductions, not Accessible-unit quotas | Conditional | If Type B is triggered and the lift core serves all hotel floors, this exception is not available | Verified |

## 11. Common toilets, kitchens, drinking fountains and lifts

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-1 hotel status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1110.2 | Toilet/bathing rooms | Each toilet room and bathing room shall be accessible; at least **one** of each type of fixture/element/control/dispenser accessible | Toilet/bathing rooms | Ex. 2: rooms serving dwelling/sleeping units **not required to be accessible by 1108**. Ex. 3: clustered single-user rooms **≥ 50%** (≥ 1 of each use). Do not locate the **only** toilets on a non-accessible floor | Direct | Make lobby, F&B and banquet toilets accessible; Accessible-guestroom bathrooms follow A117.1 | Verified |
| 1110.2.1 | Family/assisted-use toilet | Required in assembly and mercantile where aggregate male+female water closets **≥ 6**; travel **≤ 150 m** and **≤ one story** from separate-sex rooms | Assembly/mercantile fixture count | Mixed occupancy: count only A/M water closets. Family bathing room required where separate-sex bathing rooms are provided in recreational facilities | Conditional | If banquet/F&B/retail hits six WCs, add a family room on an accessible route | Verified |
| 1110.2.4 | Compartments | **≥ 5%** of compartments wheelchair-accessible; if compartments+urinals **≥ 6**, **≥ 5%** ambulatory-accessible **in addition** | Multi-compartment toilets | Unit bathrooms excepted via 1110.2 Ex. 2 | Conditional | Size lobby/F&B toilets with a wheelchair stall; add ambulatory stall when the room is large | Verified |
| 1110.2.5 | Lavatories | **≥ 5%** (≥ 1) accessible; extra accessible lavatory if the only one is inside the accessible stall; **≥ 6** lavatories → one enhanced-reach | Lavatories provided | Enhanced reach per A117.1 (not imported) | Conditional | Do not hide the only accessible lavatory inside the accessible stall | Verified |
| 1110.4 | Kitchens and kitchenettes | Kitchens and kitchenettes in accessible spaces or rooms shall be accessible | Common kitchens / kitchenettes | Unit kitchens follow 1110.1 Exception / A117.1 (not imported) | Direct | Detail lobby pantry, club lounge kitchen and staff break kitchenettes as accessible | Verified |
| 1110.5.1 | Drinking fountains | No fewer than **two**: one wheelchair, one standing (or dual-spout substitute) | Drinking fountains provided on a floor/site/secured area | Children’s standing spout **760 mm minimum** | Conditional | If fountains are provided, install hi-lo; do not import SBC 701 fixture counts | Verified |
| 1110.8 | Elevators | Passenger elevators on an accessible route shall be accessible and comply with **Chapter 30** | Passenger elevators on an accessible route | Freight/construction elevators not this section | External verification | All passenger cars on the accessible route are accessible; stretcher/FSAE sizes live in Chapter 30 / 403, not here | Verified |
| 1110.9 Item 4 | Platform lifts in units | Platform lifts permitted on a required accessible route **within** an individual Accessible, Type A or Type B unit | New construction | ASME A18.1 (not imported) | Conditional | Use a lift inside a split-level Accessible suite only if chosen; it does not replace building elevators | Verified |
| 1110.13.2 | Sales and service counters | At least **one of each type** of sales or service counter/window shall be accessible; disperse if the counters are dispersed | Reception, F&B, retail counters | Not a check-out-aisle table | Direct | Lower at least one reception/check-in and one of each F&B/retail service counter type | Verified |
| 1110.13.3 | Food-service lines | Food service lines shall be accessible; **≥ 50%** (≥ 1) of each type of self-service shelf accessible | Food-service lines provided | None stated | Conditional | If a buffet or cafeteria line exists, put the line and ≥ 50% of each shelf type on the accessible route | Verified |

## 12. Recreational facilities

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-1 hotel status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1111.3 | Recreation other than R-2/R-3/R-4 | Recreational facilities not falling within 1111.2 shall be **accessible** | Hotel, office and other occupancies outside 1111.2 | Shared facilities that also serve R-2 Type A/B still cannot drop below 1111.3 where they serve the hotel | Direct | Make **every** hotel-serving pool, gym, court and spa accessible — do not use the R-2 **25%** rule | Verified |
| 1111.4.14 | Pool water entry | Swimming pools, wading pools, cold baths, hot tubs and spas shall be accessible and on an accessible route | Those water features provided | Ex. 1 catch-pool/slide terminus. Ex. 2 clustered spas **5%** (≥ 1 of each type). Ex. 3 water-entry waiver is **only** for 1111.2.2 / 1111.2.3 (Type A/B) — **not** 1111.3 | Direct | Provide an accessible route **to and into** hotel pools/spas; do not use the Type A/B water-entry waiver | Verified |
| 1111.4.10 | Exercise machines | At least **one of each type** of exercise machine and equipment shall be on an accessible route | Exercise machines provided | Operable-part heights are A117.1 (not imported) | Conditional | Put at least one of each gym machine type on the accessible route | Verified |
| 1111.4.2 | Player seating | At least **one** wheelchair space in team/player seating serving areas of sport activity | Team/player seating provided | Bowling-lane exception | Conditional | If a court has player benches, provide one wheelchair space | Verified |
| 1111.4.4 | Court sides | At least **one** accessible route shall directly connect both sides of the court | Court sports | None stated | Conditional | If tennis/padel/basketball courts exist, connect both sides without leaving the court area | Verified |
| 1111.2.2 | R-2 Type A/B recreation (companion) | **25 percent**, but not less than **one**, of each type where recreation serves a single building containing Type A or Type B units | Recreation serving R-2 Type A/B | Does **not** govern hotel-only facilities; mixed shared rec still meets 1111.3 for the hotel | Conditional | If a pool is hotel-only, ignore this row. If shared with R-2, the hotel 1111.3 100% path governs the hotel share | Verified |

## 13. Signage

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-1 hotel status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1112.1 Items 4–7 | Partial-access identification | Identify accessible toilets, entrances, check-out aisles and dressing/locker rooms **where not all** are accessible | Mixed accessible/non-accessible sets | None stated | Direct | Sign the accessible lobby entrance if any public entrance remains inaccessible | Verified |
| 1112.1 Items 8–9 | Accessible MOE signs | Accessible areas of refuge and exterior areas for assisted rescue in accordance with **Section 1009.9** | Those elements provided | Values not in Chapter 11 | External verification | Coordinate ISA with the Chapter 10 accessible-egress package | Verified |
| 1112.3 | Directional signs | Directional ISA signage at inaccessible entrances, toilets, elevators not on an accessible route, family-toilet locations, exits not providing approved accessible MOE (**1009.10**), and split hi-lo fountains | Those conditions | Visual characters per A117.1 (not imported) | Direct | Place directional copy at every inaccessible public entrance | Verified |
| 1112.4 Item 1 | ALS availability sign | Assembly areas required to comply with 1109.2.7 shall notify patrons of assistive listening systems, with the hearing-loss symbol | Assembly with ALS | Signs at each ticket window may substitute for signs in each assembly room | Conditional | If a banquet hall has a PA, post ALS availability at the door or ticket point | Verified |

## 14. Podium, amenity and assembly (conditional)

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-1 hotel status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| Table 1109.2.2.1 | Wheelchair spaces | Flattened OCR table; no reconstructed seating-capacity cell is adopted | Assembly with fixed seating | Companion seat per 1109.2.3 (**one** per wheelchair space); **5%** designated aisle seats | Conditional | If a banquet hall, cinema or lecture room has fixed seats, apply the published table after source check | Verify source |
| 1109.2.5 | Designated aisle seats | **≥ 5%** (≥ 1) of aisle seats, closest to accessible routes | Aisle seats provided | Not required in team/player seating | Conditional | Mark aisle seats nearest the accessible route in amenity auditoria | Verified |
| 1109.2.9.1 | Dining surfaces | **≥ 5%** (≥ 1) of dining surfaces for seating and standing spaces accessible, distributed, on an accessible level | Dining surfaces provided | Mezzanine **< 25%** dining area exception (1109.2.9 Ex. 2) | Conditional | Provide wheelchair dining in hotel restaurants and bars | Verified |
| Table 1109.2.7.1 | ALS receivers | Flattened OCR table; asterisks unresolved; no reconstructed receiver-count cell is adopted | Assembly where audible communication is integral | Not required (except courtrooms) where there is no audio amplification; induction-loop HAC exception | Conditional | If a banquet hall has a PA, provide receivers after published-source check of the table | Verify source |
| 1110.14 | Locker / fitting rooms | **≥ 5%** (≥ 1) of each type of use in each cluster shall be accessible | Dressing, fitting or locker rooms provided | None stated | Conditional | If spa/gym lockers exist, make ≥ 5% of each cluster accessible | Verified |

## 15. High-rise and outbound controls

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-1 hotel status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1009 (named) | Accessible means of egress | Chapter 11 repeatedly sends accessible egress to Section 1009 | Accessible floors and occupied roofs | No 1009 values imported | External verification | Use the Chapter 10 matrix for AMOE; do not copy those numbers here | Verified |
| 1110.8 / Ch. 30 / 403 | Elevators | Passenger elevators on the accessible route: accessible + Chapter 30. Commentary also names stretcher, 1009.2.1 and 36 m FSAE — commentary numbers are **not adopted** | Elevators / high-rise | Charging 1110.8 does not itself state 36 m or four-storey triggers | External verification | Coordinate stretcher, FSAE and occupant-evacuation elevators from Chapter 30 / 403, not from Chapter 11 commentary | Verified |
| SBC 901 §306 | Existing buildings | Named in General Comments only | Existing buildings | Not quantified in this chapter’s code paragraphs | External verification | Alterations are outside this new-construction extract | Verified |

## 16. Project-use controls

1. Use **Verified** rows for initial scoping after the row trigger and branch are confirmed.
2. Treat every **Verify source** row (all reconstructed appended tables) as a design hold point; no affected value is to be placed in issued-for-approval drawings without a published-source check.
3. Do not apply Table 1108.6.1.1 reconstructed cells; wait for the published table.
4. Do not apply the R-2 **2 percent** parking rule, the R-2 assigned-stall signage exception, the 1107.2 R-2 EV exemption, or the 1111.2.2 **25%** recreation rule to hotel-serving facilities.
5. Do not import ICC A117.1 millimetres, Chapter 10 AMOE dimensions, or commentary examples (810 mm doors, 2500 mm van height, 50°C shower temperature).
6. Record AHJ, guestroom-count, parking, recreation-ownership and extended-stay decisions in the project Golden Thread; this matrix is not evidence of SCD NOC or stamped compliance.

## 17. Coverage summary

Internal inventory of the attached Chapter 11 extract (numbered code, exceptions, tables, footnotes; commentary excluded). Row-level records are not published.

- **Inventory scope:** numbered code, exceptions, tables, footnotes (commentary excluded)
- **Total independently checkable numeric records:** 276
- **Verified:** 192
- **Verify source:** 84
- **Numeric records in Sections 1101 and 1102:** 0

### Counts by top-level section

| Top-level section | Records |
|---|---:|
| 1101 | 0 |
| 1102 | 0 |
| 1103 | 3 |
| 1104 | 12 |
| 1105 | 9 |
| 1106 | 12 |
| 1107 | 4 |
| 1108 | 51 |
| 1109 | 16 |
| 1110 | 62 |
| 1111 | 22 |
| 1112 | 1 |

### Appended-table coverage

| Appended table | Records | Verify source records |
|---|---:|---:|
| Table 1105.1.1 | 2 | 2 |
| Table 1106.2 | 11 | 11 |
| Table 1108.6.1.1 | 33 | 33 |
| Table 1109.2.2.1 | 7 | 7 |
| Table 1109.2.7.1 | 12 | 12 |
| Table 1109.3 | 2 | 2 |
| Table 1110.13.1 | 4 | 4 |
| TABLE 111.4.9.1 (OCR title) | 13 | 13 |

Coverage cross-check against `SBC 201 Chapter 11 Accessibility (2024)_CS.md` was topics-only: scoping vs ICC A117.1; 1103.2 exceptions; routes and stories; entrances and power doors; parking/vans; EV charging; dwelling-unit mix; assembly seating and toilets. No CS.md value was copied into a matrix cell.

## 18. Unresolved-source register

Hold points for the 84 **Verify source** inventory records. Counts are record counts, not distinct numeric values. No value in this register is a design-release figure.

| Affected table / clause | Why unverified | Control note |
|---|---|---|
| Table 1105.1.1 | 2 flattened occupancy/load cells | Verify published table; R-1 is listed. Mixed-use footnote uses the most restrictive listed occupant load |
| Table 1106.2 | 11 flattened stall-count rows | R-1 parking uses this table via 1106.3 Item 2; verify published table before stall counts |
| Table 1108.6.1.1 | 33 flattened Accessible-unit cells (without / with roll-in / total) | Direct for Group R-1; verify published table before guestroom mix. 50-unit site/structure rule in 1108.6.1.1 text is Verified |
| Table 1109.2.2.1 | 7 flattened wheelchair-space rows | Verify published table before banquet/assembly seating |
| Table 1109.2.7.1 | 12 flattened receiver/HAC cells; asterisks unresolved | Verify published table before ALS receiver counts |
| Table 1109.3 | 2 flattened self-storage rows | Not typical for this hotel; verify published table only if self-storage is added |
| Table 1110.13.1 | 4 flattened check-out-aisle rows | Not typical unless podium retail check-out aisles exist; verify published table |
| TABLE 111.4.9.1 (OCR title as printed) | 13 flattened boat-slip rows | Title OCR; not typical for this hotel; verify published Table 1111.4.9.1 if a marina is added |
