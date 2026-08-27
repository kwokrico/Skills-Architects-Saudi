# SBC 201 Chapter 11 Accessibility — Group R-2 High-Rise Dimensional Requirements Matrix (2024)

## 1. Document metadata and use limitation

- **Project basis:** Riyadh, Saudi Arabia; Group R-2 residential high-rise; an occupied floor is stated to be more than 23 m above the relevant reference level.
- **Deliverable tier:** Project-use matrices in Sections 1–17 (design-check rows, not pasted inventory), plus a coverage summary and unresolved-source register. The full row inventory is not published.
- **Code/source basis:** SBC 201 (2024), Chapter 11, source file `Reference\SBC 201 2024\source_reference\Chapter_11 — ACCESSIBILITY.txt`.
- **Extraction audit:** Skill-finetune re-run. Project-use rows follow the chapter-extract row contract (noun-phrase checks, bold SI values, building-language triggers, named exceptions, check-specific actions). Internal inventory: **276** independently checkable numeric records (**192** Verified, **84** Verify source). Unresolved OCR is listed in the register and is not a design-release value. Pre-skill baseline retained as `…_Grok-4.6.md`.
- **Model:** Cursor Grok 4.6.
- **Prepared:** 2026-08-27.
- **Status:** Source-only architectural advisory matrix for design coordination. It is not a stamped compliance statement, accessibility consultant report, SCD NOC, SBPS approval, legal opinion, or permission to construct.
- **Outbound-source rule:** No value in this matrix has been imported from ICC A117.1, Chapter 10, Chapter 9, Section 403, Chapter 30, SBC 701, SBC 901, HUD/FHAG, ADA, commentary examples, or the existing chapter summary. Where Chapter 11 sends the user elsewhere, this matrix records the dependency without supplying the outbound value.

### Scope and assumptions

1. Group R-2 and high-rise status are project statements, not independently verified classifications.
2. The exact Riyadh AHJ/permit pathway, project stage and SCD NOC status are unconfirmed; therefore this matrix does not conclude compliance.
3. Unit type is unconfirmed. The lead apartment-house path is **Section 1108.6.2.2** (Type A + Type B). Table 1108.6.1.1 Accessible-unit quotas apply to Group R-1 and to Group R-2 **other than** live/work and apartment houses. They are not applied to a conventional apartment tower unless the unit type is congregate.
4. Automatic sprinkler protection is not selected in this chapter extract. Chapter 11 does not branch residential unit scoping on NFPA 13 versus 13R.
5. Building height, storey count, grade plane, occupied-roof configuration, parking counts/types, mixed-use podium, amenity/recreation layouts and EV provision are unconfirmed.
6. Chapter 11 is **scoping**. Technical millimetre geometry for accessible routes, doors, toilets, kitchens and Type A/B units is ICC A117.1. Charging **1102.1** names ICC A117.1 with **no edition year**. General Comments name 2009; later commentary discusses 2017 anthropometry. Neither commentary year is adopted as a charging substitution.
7. All eight appended tables are concatenated OCR. No reconstructed cell is adopted as a design-release value. Affected project-use rows are **Verify source**.

## 2. Legends

### Applicability

| Status | Meaning |
|---|---|
| **Direct** | Expected to govern the stated R-2 tower basis, subject to confirmed geometry and design data. |
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
| ICC A117.1 edition | Charging 1102.1 has no year; General Comments name 2009; commentary discusses 2017 | Controls turning spaces, clear floor space, door manoeuvring, Type A/B unit interiors | AHJ/code consultant to lock the referenced edition; do not silently switch editions |
| Unit type | Unconfirmed: apartment dwelling units vs sleeping units vs congregate bedrooms | Selects 1108.6.2.2 (Type A/B) versus 1108.6.2.3 + Table 1108.6.1.1 (Accessible units) | Classify every R-2 unit type and show the applicable branch on accessibility plans |
| Site unit count | Unconfirmed; typical tower exceeds 20 units | Type A trigger is **more than 20** dwelling/sleeping units **on the site** | Issue a signed unit schedule for the site, excluding existing structures per 1108.6.2.2.1 Exception 2 |
| Elevator service | High-rise implies elevator service, not independently verified | 1108.7 nonelevator reductions do not apply to a true elevator building except 1108.7.3 limited-elevator branch | Confirm passenger-elevator service to all stories containing units; if a lift serves only the lowest unit story, re-test 1108.7.3 |
| Parking count and type | Unconfirmed | 1106.3 Item 1 (**2%** of each type) versus Item 3 (one accessible space per Accessible/Type A unit where parking is 1:1); Item 4 if parking is in/under the building | Produce a parking schedule by facility and type (resident, visitor, accessible, van, EV) |
| Mixed-use podium | Unconfirmed | Shared routes, **60%** public entrances, Table 1105.1.1 power doors (A/B/M/R-1 only), family toilets, assembly seating | Freeze occupancy by room; do not apply R-1 power-door loads to R-2 |
| Recreation / pool | Unconfirmed | 1111.2.2 **25%** of each type for Type A/B; 1111.4.14 Exception 3 waives water-entry for Type A/B pools but not for Accessible-unit recreation | Map every recreational facility type serving the tower |
| EV charging | Unconfirmed | 1107.2 exception for EV serving R-2; **5%** / **3300 mm** / **1500 mm** apply only if the exception does not cover the installation | Confirm whether chargers serve R-2 residents only or a public/commercial facility |
| Occupied roof / amenities | Unconfirmed | 1104.4 Exception 1 **does not apply** to structures with **4 or more** dwelling units; common rooms serving Type B units must be accessible (1108.3) | Show an accessible route to every required accessible story, mezzanine and occupied roof |
| NOC / accessibility consultant | Unconfirmed | Technical A117.1 geometry, assisted-evacuation and SCD acceptance cannot be concluded from Chapter 11 scoping alone | Engage the qualified local accessibility/fire consultants before design freeze |

## 4. Scoping versus technical standard

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1101.1 | Chapter scope | This chapter controls design and construction of facilities for accessibility | All facilities in scope | None stated | Direct | Treat Chapter 11 as the scoping document for the tower and site | Verified |
| 1102.1 | ICC A117.1 | Accessible in accordance with this code **and ICC A117.1** (no year) | All required accessible facilities | None stated | External verification | Lock the A117.1 edition with the AHJ; do not import millimetre geometry here | Verified |
| 1108.2 | Unit interiors | Accessible / Type A / Type B units comply with applicable portions of **Chapter 11 of ICC A117.1**; higher unit types may substitute | Required unit types | Type A may be built as Accessible; Type B as Accessible or Type A | External verification | Produce unit-type typical details from the referenced A117.1 chapter, not from commentary millimetres | Verified |
| 1110.1 Exception | Unit toilets/kitchens | Accessible, Type A and Type B units shall comply with **Chapter 10 of ICC A117.1** | Those unit types | 1110 otherwise still governs common/public features | External verification | Note the source names Chapter 10 here and Chapter 11 at 1108.2; verify the printed A117.1 mapping before detailing | Verified |
| 1108.3 | Common rooms serving units | Rooms and spaces available to the public or residents and serving Accessible, Type A or Type B units shall be accessible, including toilet/bathing, kitchen, living/dining and exterior patios/terraces/balconies | Amenities serving required units | 1108.4 story exemptions; 1111.2 recreation; Type B impervious balcony step-down **100 mm maximum** | Direct | Put lobby, mail, laundry, refuse, shared toilets, gym and roof terrace on an accessible route | Verified |

## 5. General applicability and surviving exceptions

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1103.1 | Default accessibility | Sites, buildings, structures, facilities, elements and spaces, temporary or permanent, shall be accessible | All construction | Only to the extent permitted by 1103.2 / 1104–1112 | Direct | Assume accessible unless a numbered exception is proven | Verified |
| 1103.2.2 | Employee work areas | Approach, enter and exit plus 907.5.2.3.1, 1009 and 1104.3.1 only | Employee work areas | Portions **< 28 m²** and **≥ 175 mm** essential level change exempt from all requirements (not courtroom stations) | Conditional | Apply to BOH, security desks and plant-adjacent workstations; keep visible alarm and accessible MOE outbound | Verified |
| 1103.2.9 | Equipment spaces | Spaces frequented only by service personnel for maintenance, repair or occasional monitoring of equipment are not required to comply with this chapter | Service-only equipment spaces | None stated | Direct | Do not force an accessible route into elevator pits, penthouses or typical MEP rooms | Verified |
| 1104.3.1 Ex. 1 | Small work-area path | Common-use circulation paths in employee work areas **< 100 m²** defined by permanent partitions/furnishings need not be accessible routes | Employee work areas | Equipment-integral and weather-exposed exterior path exceptions also stated | Conditional | Keep an accessible route **to** the work area; the path through a small defined workstation may be exempt | Verified |

## 6. Accessible routes and stories

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1104.1 | Site arrival route | At least **one** accessible route from transit, accessible parking, accessible loading, streets/sidewalks to the accessible entrance | Site arrival points | Vehicular-way-only exception **does not apply** to buildings containing or serving Type B units | Direct | Provide a pedestrian accessible route from every applicable arrival point; do not rely on a driveway-only exception | Verified |
| 1104.2 | On-site connections | At least **one** accessible route connecting accessible buildings, facilities, elements and spaces on the same site | Multiple accessible elements on one site | Vehicular-way-only; recreation only as 1111 | Direct | Connect podium, parking, lobby and recreation to the same accessible network | Verified |
| 1104.3 | Connected spaces | At least **one** accessible route to each required accessible portion, to accessible entrances connecting accessible walkways, and to the public way | Building required to be accessible | 1104.4 story skips; assembly levels without wheelchair spaces; courtroom workstations; 1111 recreation | Direct | Trace the accessible route from public way through lobby, lifts and common floors | Verified |
| 1104.4 | Multistory / occupied roof | At least **one** accessible route shall connect each accessible story, mezzanine and occupied roofs | Multilevel buildings | Exception 1 (**≤ 279 m²** aggregate above+below) **shall not apply** to structures with **4 or more dwelling units** | Direct | Do not use the 279 m² story-skip on this R-2 tower; serve every required accessible level including occupied roof | Verified |
| 1104.5 | Route coincidence | Accessible routes shall coincide with or be in the same area as general circulation; interior circulation requires an interior accessible route; a single accessible route shall not pass through kitchens, storage, restrooms, closets or similar | Accessible routes | 1. Garage-to-Type B routes need not be interior. 2. A single route may pass through a kitchen or storage room **inside** an Accessible, Type A or Type B unit | Direct | Keep common accessible routes in public circulation, not through service rooms | Verified |
| 1108.4 | Route to units | At least **one** accessible route shall connect accessible building entrances with the primary entrance of each Accessible, Type A and Type B unit and with interior/exterior spaces serving the units | Required units | 1. **1:12** / legal-barrier vehicular substitute. 3. R-2 with Type A units: stories need not connect where Type A units, their common use and all public use are already on an accessible route. 7. Type B stories exempted by 1108.7 | Direct | For an elevator high-rise, serve every Type A and Type B unit entrance from an accessible building entrance | Verified |
| 1108.3 Ex. 3 | Type B balcony step | Type B unit impervious decks/patios/balconies not more than **100 mm** below adjacent interior finished floor | Type B unit private outdoor space | Community/public decks are not this exception | Direct | Limit unit balcony step-down to 100 mm where the walking surface is impervious; keep community terraces fully accessible | Verified |

## 7. Entrances

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1105.1 | Public entrances | At least **60 percent** of all public entrances shall be accessible, in addition to 1105.1.2–1105.1.8 | Public entrances | Areas not required to be accessible; loading/service entrances that are not the only tenant entrance | Direct | Count public doors (not egress-only doors) and make ≥ 60% accessible | Verified |
| 1105.1.1 / Table 1105.1.1 | Power-operated public entrance | One full-power or low-energy power-operated door at each required accessible public entrance when occupancy and building occupant load exceed the table; vestibule: one leaf in and one leaf out | Table lists Groups **A-1–A-4** and **B, M, R-1**; mixed-use uses the most restrictive listed load | **Group R-2 is not listed.** Flattened OCR occupant-load cells are not adopted | Conditional | Do not apply an R-1 occupant trigger to R-2. If a podium A/B/M/R-1 load exceeds the published table, power-operate those occupancies’ accessible public entrances after source check | Verify source |
| 1105.1.2 | Parking-garage entrance | Direct pedestrian access from parking structures to building/facility entrances shall be accessible | Direct garage-to-building pedestrian access | None stated | Direct | Provide an accessible pedestrian door from the parking structure into the tower | Verified |
| 1105.1.7 | Tenant entrance | At least **one** accessible entrance to each tenant in a facility | Multi-tenant facility | Self-service storage not required to be accessible | Conditional | If podium tenancies exist, give each tenant an accessible entrance in addition to the 60% building count | Verified |
| 1105.1.8 | Unit entrance | At least **one** accessible entrance to each dwelling/sleeping unit | Dwelling and sleeping units | Not required to units that are not Accessible, Type A or Type B | Direct | Every Type A and Type B unit gets an accessible entrance; shared lobby doors still count toward 60% | Verified |

## 8. Parking, vans and passenger loading

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1106.3 Item 1 | R-2 accessible parking | At least **2 percent**, but not less than **one**, of **each type** of parking space provided shall be accessible | R-2 required to have Accessible, Type A or Type B units | Table 1106.2 is the I-1/R-1 path (Item 2), not the R-2 default | Direct | Count resident, visitor and any other parking **types** separately and take 2% (≥ 1) of each | Verified |
| 1106.3 Item 3 | 1:1 parking vs Type A | Where at least one parking space is provided for each dwelling/sleeping unit, at least **one** accessible parking space shall be provided for **each Accessible and Type A unit** | Parking provided at ≥ 1 space per unit | Code does not state that Item 1 and Item 3 are additive | Conditional | If assigned 1:1 parking exists, provide an accessible stall for every Type A (and Accessible) unit and compare with Item 1 | Verified |
| 1106.3 Item 4 | In-building parking | Where parking is within or beneath a building, accessible parking shall also be within or beneath the building | Parking in/under the building | None stated | Direct | Put accessible stalls in the podium/basement garage, not only on the surface lot | Verified |
| 1106.6 | Van spaces | For every **six** or fraction of six accessible parking spaces, at least **one** shall be van-accessible | Accessible parking provided | Group U private garages serving R-2/R-3: van routes/spaces/aisles permitted **2100 mm** minimum vertical clearance | Direct | Provide 1-in-6 vans; use 2100 mm only for qualifying Group U private garages — do not import A117.1 van height from commentary | Verified |
| 1106.7 Ex. 1 | Van-space level | In multilevel parking structures, van-accessible parking spaces are permitted on **one** level | Multilevel parking | Accessible spaces still dispersed; van-height millimetres are A117.1 (not imported) | Direct | Concentrate van stalls on the level that can provide the A117.1 van clearance | Verified |
| Table 1106.2 | General parking table | Flattened OCR table; no reconstructed stall-count cell is adopted | Parking facilities using 1106.2 | R-2 residential parking uses 1106.3 first | Conditional | Use only for non-residential facilities or I-1/R-1 after published-source check | Verify source |
| 1106.9.1 | Continuous loading zone | One accessible passenger loading zone in every continuous **30 m** maximum | Passenger loading zones provided | None stated | Conditional | If a porte-cochère or kerbside drop-off exists, space accessible zones at ≤ 30 m | Verified |
| 1112.1 Item 2 Ex. | Assigned-stall signage | In Group R-2, where parking is assigned to specific units, identification of accessible parking spaces is **not required** | 1106.3 accessible spaces that are assigned | Identification exception only; stalls still required | Conditional | Keep stall geometry; ISA signs may be omitted only for assigned unit spaces | Verified |

## 9. Electrical vehicle charging

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1107.2 Exception | R-2 EV exemption | EV charging stations provided to serve Groups R-2, R-3 and R-4 are **not required** to comply with Section 1107.2 | EV serving those occupancies | Public/commercial EV on the same site is not this exception | Direct | Resident-assigned R-2 chargers are not scoped by 1107.2; still provide an accessible route to required accessible parking | Verified |
| 1107.2.1 | Accessible EV count | Not less than **5 percent** of vehicle spaces served by EV systems, but not fewer than **one of each type**, shall be accessible | EV systems not covered by the R-2 serving exception | None stated beyond 1107.2 | Conditional | If podium/public chargers exist, reserve 5% (≥ 1 of each charger type) | Verified |
| 1107.2.2 | Accessible EV stall size | **3300 mm** minimum vehicle-space width with adjoining access aisle **1500 mm** minimum | Accessible EV spaces required by 1107.2.1 | R-2 serving exception | Conditional | Do not substitute a narrower A117.1 van option; this section specifies 3300 + 1500 | Verified |

## 10. Dwelling-unit mix (Accessible / Type A / Type B)

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1108.6.2.2.1 | Type A apartments | In Group R-2 containing **more than 20** dwelling/sleeping units, at least **2 percent** but not less than **one** shall be Type A; **all Group R-2 units on a site** counted; disperse among classes | Apartment houses / condominiums | 1. Reduction only as permitted by 1108.7. 2. Existing structures do not contribute to the site count | Direct | For a typical tower > 20 units, provide ≥ 2% Type A, dispersed by bedroom class, calculated on the **site** | Verified |
| 1108.6.2.2.2 | Type B apartments | Where **four or more** dwelling/sleeping units intended to be occupied as a residence are in a **single structure**, **every** such unit shall be Type B | Apartment/condo structure | Reduction permitted per 1108.7 | Direct | Treat the high-rise as one structure; all residence units are Type B (Type A already exceeds Type B) | Verified |
| 1108.6.2.3.1 / Table 1108.6.1.1 | Accessible units (congregate) | Accessible units per Table 1108.6.1.1, including without/with roll-in shower split; only **one** bedroom in a grouped unit counts toward required Accessible units | R-2 **other than** live/work and apartment houses | Flattened OCR table cells are not adopted | Conditional | Do not apply hotel/dorm Accessible-unit quotas to conventional apartments; verify published table if congregate bedrooms exist | Verify source |
| 1108.6.2.1 | Live/work units | Nonresidential portion accessible; residential portion Type B if **four or more** live/work units intended as residence | Section 419 live/work | 1108.7 Type B reductions | Conditional | If live/work appears in the podium, split residential vs work accessibility | Verified |

## 11. Section 1108.7 reductions (elevator high-rise)

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1108.7.3 | Elevator only to lowest unit story | Where elevator service provides an accessible route **only** to the lowest story containing residence units, only units on **that story** need be Type B | Elevator limited to the lowest unit story | Upper unit stories then not Type B under this exception | Conditional | If the lift core serves all residential floors, this exception is not available | Verified |
| 1108.7.2 | Multistory units | A multistory unit without elevator service is not required to be Type B; with external elevator to only one floor, that floor is the primary entry, shall be Type B, and shall contain living, kitchen and toilet where those are provided in the unit | Multistory dwelling/sleeping units | None stated for Type A | Conditional | Typical stacked apartments are single-story units; apply only to duplex/townhouse products | Verified |

## 12. Common toilets, kitchens, drinking fountains and lifts

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1110.2 | Toilet/bathing rooms | Each toilet room and bathing room shall be accessible; at least **one** of each type of fixture/element/control/dispenser accessible | Toilet/bathing rooms | Ex. 2: rooms serving dwelling/sleeping units **not required to be accessible by 1108**. Ex. 3: clustered single-user rooms **≥ 50%** (≥ 1 of each use). Do not locate the **only** toilets on a non-accessible floor | Direct | Make lobby, amenity and podium public toilets accessible; unit bathrooms follow A117.1 by unit type | Verified |
| 1110.2.1 | Family/assisted-use toilet | Required in assembly and mercantile where aggregate male+female water closets **≥ 6**; travel **≤ 150 m** and **≤ one story** from separate-sex rooms | Assembly/mercantile fixture count | Mixed occupancy: count only A/M water closets | Conditional | If podium retail/assembly hits six WCs, add a family room on an accessible route | Verified |
| 1110.2.4 | Compartments | **≥ 5%** of compartments wheelchair-accessible; if compartments+urinals **≥ 6**, **≥ 5%** ambulatory-accessible **in addition** | Multi-compartment toilets | Unit bathrooms excepted via 1110.2 Ex. 2 | Conditional | Size amenity toilets with a wheelchair stall; add ambulatory stall when the room is large | Verified |
| 1110.2.5 | Lavatories | **≥ 5%** (≥ 1) accessible; extra accessible lavatory if the only one is inside the accessible stall; **≥ 6** lavatories → one enhanced-reach | Lavatories provided | Enhanced reach per A117.1 (not imported) | Conditional | Do not hide the only accessible lavatory inside the accessible stall | Verified |
| 1110.4 | Kitchens and kitchenettes | Kitchens and kitchenettes in accessible spaces or rooms shall be accessible | Common kitchens / kitchenettes | Unit kitchens follow 1110.1 Exception / A117.1 (not imported) | Direct | Detail lobby pantry, resident lounge kitchen and staff break kitchenettes as accessible | Verified |
| 1110.5.1 | Drinking fountains | No fewer than **two**: one wheelchair, one standing (or dual-spout substitute) | Drinking fountains provided on a floor/site/secured area | Children’s standing spout **760 mm minimum** | Conditional | If fountains are provided, install hi-lo; do not import SBC 701 fixture counts | Verified |
| 1110.8 | Elevators | Passenger elevators on an accessible route shall be accessible and comply with **Chapter 30** | Passenger elevators on an accessible route | Freight/construction elevators not this section | External verification | All passenger cars on the accessible route are accessible; stretcher/FSAE sizes live in Chapter 30 / 403, not here | Verified |
| 1110.9 Item 4 | Platform lifts in units | Platform lifts permitted on a required accessible route **within** an individual Accessible, Type A or Type B unit | New construction | ASME A18.1 (not imported) | Conditional | Use a lift inside a multi-level Type A unit only if chosen; it does not replace building elevators | Verified |

## 13. Recreational facilities

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1111.2.1 | Recreation serving Accessible units | Every recreational facility of each type serving Accessible units shall be accessible | R-2/R-4 where recreation serves Accessible units | Applies if 1108.6.2.3 Accessible units exist | Conditional | Conventional apartments without Accessible units do not use this 100% rule | Verified |
| 1111.2.2 | Recreation serving Type A/B (single building) | **25 percent**, but not less than **one**, of each type of recreational facility shall be accessible | Recreation serving a single building containing Type A or Type B units | Count every facility of each type on the site to determine the number | Direct | For one tower, make ≥ 25% (≥ 1) of each pool, court, gym, playground type accessible | Verified |
| 1111.4.14 Ex. 3 | Pool water entry | Pools/spas required to be accessible **only** by 1111.2.2 / 1111.2.3 are **not required** to provide accessible means of entry into the water | Type A/B recreation scoping | Does not apply where 1111.2.1 requires every facility serving Accessible units | Direct | Provide an accessible route **to** the pool; water-entry equipment is not scoped by 1111.2.2/2.3. Technical entry methods remain in A117.1 if otherwise required | Verified |
| 1111.4.10 | Exercise machines | At least **one of each type** of exercise machine and equipment shall be on an accessible route | Exercise machines provided | Operable-part heights are A117.1 (not imported) | Conditional | Put at least one of each gym machine type on the accessible route | Verified |
| 1111.4.2 | Player seating | At least **one** wheelchair space in team/player seating serving areas of sport activity | Team/player seating provided | Bowling-lane exception | Conditional | If a court has player benches, provide one wheelchair space | Verified |
| 1111.4.4 | Court sides | At least **one** accessible route shall directly connect both sides of the court | Court sports | None stated | Conditional | If tennis/padel/basketball courts exist, connect both sides without leaving the court area | Verified |

## 14. Signage

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1112.1 Items 4–7 | Partial-access identification | Identify accessible toilets, entrances, check-out aisles and dressing/locker rooms **where not all** are accessible | Mixed accessible/non-accessible sets | None stated | Direct | Sign the accessible lobby entrance if any public entrance remains inaccessible | Verified |
| 1112.1 Items 8–9 | Accessible MOE signs | Accessible areas of refuge and exterior areas for assisted rescue in accordance with **Section 1009.9** | Those elements provided | Values not in Chapter 11 | External verification | Coordinate ISA with the Chapter 10 accessible-egress package | Verified |
| 1112.3 | Directional signs | Directional ISA signage at inaccessible entrances, toilets, elevators not on an accessible route, family-toilet locations, exits not providing approved accessible MOE (**1009.10**), and split hi-lo fountains | Those conditions | Visual characters per A117.1 (not imported) | Direct | Place directional copy at every inaccessible public entrance | Verified |

## 15. Podium, amenity and assembly (conditional)

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| Table 1109.2.2.1 | Wheelchair spaces | Flattened OCR table; no reconstructed seating-capacity cell is adopted | Assembly with fixed seating | Companion seat per 1109.2.3; **5%** designated aisle seats | Conditional | If a cinema, mosque hall or lecture room has fixed seats, apply the published table after source check | Verify source |
| 1109.2.5 | Designated aisle seats | **≥ 5%** (≥ 1) of aisle seats, closest to accessible routes | Aisle seats provided | Not required in team/player seating | Conditional | Mark aisle seats nearest the accessible route in amenity auditoria | Verified |
| 1109.2.9.1 | Dining surfaces | **≥ 5%** (≥ 1) of dining surfaces for seating and standing spaces accessible, distributed, on an accessible level | Dining surfaces provided | Mezzanine **< 25%** dining area exception | Conditional | Provide wheelchair dining in café/amenity restaurant | Verified |
| Table 1109.2.7.1 | ALS receivers | Flattened OCR table; asterisks unresolved; no reconstructed receiver-count cell is adopted | Assembly where audible communication is integral | Not required (except courtrooms) where there is no audio amplification; induction-loop HAC exception | Conditional | If an amenity hall has a PA, provide receivers after published-source check of the table | Verify source |

## 16. High-rise and outbound controls

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1009 (named) | Accessible means of egress | Chapter 11 repeatedly sends accessible egress to Section 1009 | Accessible floors and occupied roofs | No 1009 values imported | External verification | Use the Chapter 10 R-2 matrix for AMOE; do not copy those numbers here | Verified |
| 1110.8 / Ch. 30 / 403 | Elevators | Passenger elevators on the accessible route: accessible + Chapter 30. Commentary also names stretcher, 1009.2.1 and 36 m FSAE — commentary numbers are **not adopted** | Elevators / high-rise | Charging 1110.8 does not itself state 36 m or four-storey triggers | External verification | Coordinate stretcher, FSAE and occupant-evacuation elevators from Chapter 30 / 403, not from Chapter 11 commentary | Verified |
| SBC 901 §306 | Existing buildings | Named in General Comments only | Existing buildings | Not quantified in this chapter’s code paragraphs | External verification | Alterations are outside this new-construction extract | Verified |

## 17. Project-use controls

1. Use **Verified** rows for initial scoping after the row trigger and branch are confirmed.
2. Treat every **Verify source** row (all reconstructed appended tables) as a design hold point; no affected value is to be placed in issued-for-approval drawings without a published-source check.
3. Do not apply Table 1108.6.1.1 Accessible-unit quotas to conventional R-2 apartments.
4. Do not apply Table 1105.1.1 power-door occupant loads to Group R-2.
5. Do not import ICC A117.1 millimetres, Chapter 10 AMOE dimensions, or commentary examples (810 mm doors, 2500 mm van height, 2050 mm vs 2100 mm, 50°C shower temperature).
6. Record AHJ, unit-type, parking and recreation decisions in the project Golden Thread; this matrix is not evidence of SCD NOC or stamped compliance.

## 18. Coverage summary

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

## 19. Unresolved-source register

Hold points for the 84 **Verify source** inventory records. Counts are record counts, not distinct numeric values. No value in this register is a design-release figure.

| Affected table / clause | Why unverified | Control note |
|---|---|---|
| Table 1105.1.1 | 2 flattened occupancy/load cells | Verify published table; do not apply reconstructed A/B/M/R-1 occupant loads to Group R-2 |
| Table 1106.2 | 11 flattened stall-count rows | R-2 residential parking uses 1106.3 first; verify published table before any 1106.2 use |
| Table 1108.6.1.1 | 33 flattened Accessible-unit cells (without / with roll-in / total) | Applies to R-1 and congregate R-2, not conventional apartment houses; verify published table if congregate bedrooms exist |
| Table 1109.2.2.1 | 7 flattened wheelchair-space rows | Verify published table before amenity/assembly seating |
| Table 1109.2.7.1 | 12 flattened receiver/HAC cells; asterisks unresolved | Verify published table before ALS receiver counts |
| Table 1109.3 | 2 flattened self-storage rows | Not typical for this R-2 tower; verify published table only if self-storage is added |
| Table 1110.13.1 | 4 flattened check-out-aisle rows | Not typical unless podium retail check-out aisles exist; verify published table |
| TABLE 111.4.9.1 (OCR title as printed) | 13 flattened boat-slip rows | Title OCR; not typical for this R-2 tower; verify published Table 1111.4.9.1 if a marina is added |
