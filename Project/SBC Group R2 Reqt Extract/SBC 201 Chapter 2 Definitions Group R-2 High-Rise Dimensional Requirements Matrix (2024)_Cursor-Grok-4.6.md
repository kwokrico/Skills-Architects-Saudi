# SBC 201 Chapter 2 Definitions — Group R-2 High-Rise Dimensional Requirements Matrix (2024)

## 1. Document metadata and use limitation

- **Project basis:** Riyadh, Saudi Arabia; Group R-2 residential high-rise; an occupied floor is stated to be more than 23 m above the relevant fire-department vehicle-access level.
- **Deliverable tier:** Project-use matrices in Sections 1–13 (design-check rows, not pasted inventory), plus a coverage summary and unresolved-source register. The full row inventory is not published.
- **Code/source basis:** SBC 201 (2024), Chapter 2, source file `Reference\SBC 201 2024\source_reference\Chapter_02 — DEFINITIONS.txt`.
- **Extraction audit:** Skill-finetune run. Project-use rows follow the chapter-extract row contract (noun-phrase checks, bold published tokens, building-language triggers, named exceptions, check-specific actions). Internal inventory: **208** independently checkable numeric records (**208** Verified, **0** Verify source). Commentary, bibliography and Chapter 2 figures were excluded. Unrelated occupancy/chemical classification thresholds were inventoried internally and omitted from lead tables.
- **Model:** Cursor Grok 4.6.
- **Prepared:** 2026-08-27.
- **Status:** Source-only architectural advisory matrix for design coordination. It is not a stamped compliance statement, occupancy classification, SCD NOC, SBPS approval, legal opinion, or permission to construct.
- **Outbound-source rule:** No value in this matrix has been imported from Chapter 3, 4, 5, 9, 10, 11, 15, 16, 403, 404, 505, 1031, ICC A117.1, SBC 601/602, SBC 801, SBC 901, SBC 1101/1102, commentary examples (including **36 m** / **126 m** high-rise commentary), figure captions, or the existing chapter summary. Where Chapter 2 sends the user elsewhere, this matrix records the dependency without supplying the outbound value.

### Scope and assumptions

1. Group R-2 and high-rise status are project statements. High-rise is defined here as an occupied floor more than **23 m** above the lowest level of fire department vehicle access; that measurement is not independently verified for this project.
2. The exact Riyadh AHJ/permit pathway, project stage and SCD NOC status are unconfirmed; therefore this matrix does not conclude compliance.
3. Automatic sprinkler protection, storey count, mixed-use podium, amenity/assembly program, atrium, mezzanine, penthouse use and unit type (apartment dwelling units versus sleeping/congregate/live-work) are unconfirmed.
4. Chapter 2 defines terms. It does not classify occupancy (Chapter 3), set height/area (Chapter 5), scope accessibility counts (Chapter 11), or publish egress millimetre geometry (Chapter 10).
5. Commentary after each definition, the chapter bibliography, and FIGURES OF CHAPTER 2 are not mandatory source text. Figure examples (including grade-plane sample elevations) are not adopted.

## 2. Legends

### Applicability

| Status | Meaning |
|---|---|
| **Direct** | Expected to govern the stated R-2 tower basis, subject to confirmed geometry and design data. |
| **Conditional** | Governs only when the stated feature, use, occupant load, sprinkler branch or exception exists. |
| **Not typical** | Unrelated occupancy-only rule; omitted from this deliverable unless the gap register already opened that use. |
| **External verification** | Chapter 2 points to another section/code/standard, or the project/AHJ basis must be confirmed before use. |

### Source confidence

| Status | Meaning |
|---|---|
| **Verified** | Requirement and any stated numeric value were checked against unambiguous mandatory Chapter 2 source text. |
| **Verify source** | OCR, flattened table, page-split, or footnote attachment is unresolved. Not a design-release value. |

## 3. Project decision and gap register

| Decision / gap | Current project basis | Why it controls Chapter 2 application | Required project action |
|---|---|---|---|
| High-rise confirmation | Stated; not measured here | **202** high-rise is occupied floor **> 23 m** above lowest fire-department vehicle access, not building height from grade plane | Survey FD access elevation and the lowest occupied floor; lock the **23 m** test before applying Section **403** |
| Additional high-rise tiers | Not in this chapter’s definition text | Commentary mentions further rules above **36 m** and **126 m**; those numbers are not 202 source values | Take additional high-rise thresholds from **Section 403**, not from this matrix |
| Unit type | Unconfirmed apartment dwelling units vs sleeping/congregate/live-work | Dwelling unit vs sleeping unit vs congregate living vs live/work changes Chapter 10/11 branches without changing this chapter’s definitions | Classify every unit on a signed schedule (kitchen + sanitation together = dwelling unit) |
| Transient vs nontransient | Assumed nontransient R-2 | **202** transient is occupancy of a dwelling/sleeping unit for **not more than 30 days** | Confirm lease/stay duration; stays ≤ **30 days** are transient (typically R-1), not this R-2 basis |
| Mixed-use / podium | Unconfirmed | Fire area, FSD, atrium story-count and public-way geometry still use these definitions | Freeze occupancy by space; measure FSD and atrium stories with the 202 methods |
| Atrium / mezzanine / penthouse | Unconfirmed | Atrium for this occupancy is a closed-top void connecting **three or more** stories; mezzanine geometry is **Section 505**; penthouse is unoccupied rooftop MEP/shafts | Identify every multi-storey void, intermediate level and rooftop enclosure before locking 404/505/1511 |
| Townhouse / SBC 1101-1102 product | Not assumed on this tower | Townhouse is **three or more** attached foundation-to-roof units with open space on at least two sides; the four-test 1101/1102 exception is commentary | Do not apply the townhouse definition unless that attached product is added |
| Grade plane / stories above grade | Unconfirmed site grades | **1.8 m** lot-line offset and **1.8 m** / **3.6 m** story-above-grade tests control height in stories (Chapter 5) | Produce a grade-plane diagram from finished ground, not from a single corner spot-height |
| Sprinkler / NOC / fire strategy | Unconfirmed | Chapter 2 does not select NFPA 13 vs 13R; commentary on sprinkler types is not adopted | Lock the sprinkler standard from Chapter 9 / the fire strategy, not from this glossary |
| Accessibility edition | Not published here | Accessible / Type A / Type B are labels pointing to Chapter 11 and ICC A117.1 | Keep millimetre unit geometry on the locked A117.1 edition |

## 4. Term application

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 201.1 | Chapter term meanings | Unless otherwise expressly stated, words and terms shall have the meanings shown in this chapter | All applications of this code | None stated | Direct | Put Chapter 2 on the code sheet as the glossary for defined terms used on the drawings | Verified |
| 201.2 | Tense gender number | Present tense includes the future; masculine includes feminine; singular includes plural and plural the singular | Reading any defined or undefined term | None stated | Direct | Do not treat singular “dwelling unit” or “exit” as limiting the count of those elements | Verified |
| 201.3 | Terms in other Saudi codes | Where terms are not defined in this code and are defined in other referenced Saudi codes, those meanings apply | Term absent from Chapter 2 | None stated | External verification | Look up the missing term in the named Saudi code; do not import that code’s numbers into this matrix | Verified |
| 201.4 | Terms not defined | Where terms are not defined through the methods authorized by this section, they have ordinarily accepted meanings as the context implies | Term absent from this code and other referenced Saudi codes | None stated | Direct | Use ordinary construction meaning; do not invent a Chapter 2 threshold | Verified |

## 5. Height, grade plane, story and high-rise

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 202 | Grade plane | Average of finished ground adjoining the building at exterior walls. Where ground slopes away, use the lowest points between the building and the lot line, or a point **1.8 m** from the building where the lot line is more than **1.8 m** away | Building height, stories above grade plane, basement classification | None stated | Direct | Draw grade plane from perimeter finished grades using the **1.8 m** offset; do not use a single corner elevation | Verified |
| 202 | Story | Portion of a building between the upper surface of a floor and the upper surface of the floor or roof next above, measured top-to-top of successive finished floors (or to ceiling joists/roof rafters at the top story) | Every building level | See basement, building height, grade plane and mezzanine | Direct | Count each stacked floor-to-floor volume as a story, including basements; treat a qualifying mezzanine as part of its story | Verified |
| 202 | Story above grade plane | Any story with finished floor entirely above grade plane, or in which the floor next above is more than **1.8 m** above grade plane, or more than **3.6 m** above finished ground at any point | Height in stories (Chapter 5) | A level that fails this test is a basement | Direct | Test every below-grade and hillside level against **1.8 m** and **3.6 m** before dropping it from the story count | Verified |
| 202 | Basement | A story that is not a story above grade plane | Levels that fail the story-above-grade-plane test | This basement definition does **not** apply to Section **1612** flood loads | Direct | Exclude true basements from Table 504 story limits; use the flood basement definition only if 1612 applies | Verified |
| 202 | Building height | Vertical distance from grade plane to the average height of the highest roof surface | Height in metres (Chapter 5) | None stated in this definition | Direct | Measure to the average of the highest roof, not to a penthouse that remains a 202 penthouse | Verified |
| 202 | High-rise building | Building with an occupied floor located more than **23 m** above the lowest level of fire department vehicle access | Occupied floor vs FD vehicle access | Not a measurement of building height from grade plane | Direct | Dimension FD access to the lowest occupied floor on the life-safety section; if **> 23 m**, apply **Section 403** without importing 403 values here | Verified |

## 6. Area, fire area and fire separation distance

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 202 | Building area | Area within surrounding exterior walls (or exterior walls and fire walls), exclusive of vent shafts and courts. Areas without surrounding walls count if they lie within the horizontal projection of the roof or floor above | Allowable area (Chapter 5) | Vent shafts and courts are excluded | Direct | Take the footprint inside exterior/fire walls; add projected open-sided area; keep courts and vent shafts out of the area takeoff | Verified |
| 202 | Gross floor area | Floor area within the inside perimeter of exterior walls, exclusive of vent shafts and courts, without deduction for corridors, stairways, ramps, closets, interior walls, columns or other features. Unwalled portions use usable area under the horizontal projection of the roof or floor above. Shafts with no openings and interior courts are excluded | Occupant-load and other gross-area applications | Shafts with no openings and interior courts omitted | Direct | Use inside-face exterior-wall takeoff for Table 1004.5 gross rows; do not net-out corridors | Verified |
| 202 | Net floor area | Actual occupied area, not including unoccupied accessory areas such as corridors, stairways, ramps, toilet rooms, mechanical rooms and closets | Occupant-load net-area applications | Accessory unoccupied rooms omitted | Direct | Use net area only for spaces Table 1004.5 assigns as net; keep toilets and corridors out of that takeoff | Verified |
| 202 | Fire area | Aggregate floor area enclosed and bounded by fire walls, fire barriers, exterior walls or horizontal assemblies. Unwalled areas count if they sit under the horizontal projection of the roof or floor next above | Sprinkler, alarm and other fire-area triggers (Chapter 9) | None stated | Direct | Sum every story (and any mezzanine area the later chapter includes) inside the bounding rated assemblies; do not import Chapter 9 thresholds here | Verified |
| 202 | Fire separation distance | Distance from the building face, measured at right angles from the wall, to: (1) the closest interior lot line; (2) the centerline of a street, alley or public way; or (3) an imaginary line between two buildings on the lot | Exterior-wall rating and opening limits (Chapter 7) | Designer locates the imaginary line, then it applies to both buildings | Direct | Dimension FSD perpendicular to each exterior face on the site plan; freeze any same-lot imaginary line before rating the walls | Verified |

## 7. Residential occupancy and unit types

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 202 | Dwelling unit | Single unit with complete independent living facilities for one or more persons, including permanent provisions for living, sleeping, eating, cooking **and** sanitation | Conventional apartment with a full kitchen and bathroom | Distinguished from sleeping unit | Direct | Schedule every apartment with permanent cooking **and** sanitation as a dwelling unit on the unit matrix | Verified |
| 202 | Efficiency dwelling unit | Dwelling unit where all permanent provisions for living, sleeping, eating and cooking are contained in a single room | Studio / efficiency apartment | Still a dwelling unit | Direct | Treat studios with permanent cooking as dwelling units, not sleeping units, for Chapter 10/11 scoping | Verified |
| 202 | Sleeping unit | Rooms/spaces for one or more persons with permanent sleeping; may include living, eating and **either** sanitation **or** kitchen, but not both. Spaces that are also part of a dwelling unit are not sleeping units | Hotel-style rooms, congregate bedrooms, kitchenette-only studios | Spaces inside a dwelling unit are not sleeping units | Conditional | If a unit has a kitchenette **or** a bathroom but not both, classify it as a sleeping unit and switch the 1108/1006 branch | Verified |
| 202 | Congregate living facilities | Building or part thereof that contains sleeping units where residents share bathroom or kitchen facilities, or both | Shared-bath or shared-kitchen housing | Occupant-count classification is Chapter 3, not this definition | Conditional | If bathrooms or kitchens are shared, label the product congregate living; do not import the commentary 10/16-person splits | Verified |
| 202 | Live/work unit | Dwelling unit or sleeping unit in which a significant portion of the space includes a nonresidential use operated by the tenant | Combined living and tenant-operated work | None stated | Conditional | If live/work is programmed, tag those units and apply the live/work sections of later chapters without importing their numbers here | Verified |
| 202 | Multistory unit | Dwelling unit or sleeping unit with habitable space on more than one story | Maisonette / duplex apartment | None stated | Conditional | Flag every split-level unit for the Chapter 11 multistory-unit accessibility branch | Verified |
| 202 | Transient occupancy | Occupancy of a dwelling unit or sleeping unit for **not more than 30 days** | Stay-duration test for R-1 vs R-2 | None stated | Direct | Confirm residential stays exceed **30 days**; if any block is ≤ **30 days**, reclassify that block as transient | Verified |
| 202 | Intended as a residence | Dwelling unit or sleeping unit that can or will be used all or part of the time as the occupant’s place of abode | Type B / Fair-Housing-style scoping in Chapter 11 | None stated | Direct | Treat the apartments as places of abode for Chapter 11 Type B intent; keep A117.1 millimetres outbound | Verified |

## 8. Accessibility unit labels

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 202 | Accessible | Site, building, facility or portion thereof that complies with **Chapter 11** | Any claim that a route or space is accessible | Technical millimetres are not in this chapter | External verification | Show Chapter 11 scoping on the accessibility sheet; do not copy ICC A117.1 geometry into this matrix | Verified |
| 202 | Accessible route | Continuous, unobstructed path that complies with **Chapter 11** | Accessible approach, entry and circulation | None stated | External verification | Draw the Chapter 11 accessible route; keep A117.1 clearances on that standard | Verified |
| 202 | Accessible means of egress | Continuous and unobstructed way of egress travel from any accessible point in a building or facility to a public way | Accessible egress (Section 1009) | Ingress route may differ (1104/1105) | External verification | Coordinate accessible egress to 1009; do not import area-of-refuge sizes from Chapter 10 | Verified |
| 202 | Accessible unit | Dwelling or sleeping unit that complies with this code and Accessible units in **ICC A117.1** | Units scoped as Accessible (capital A) | Counts are Chapter 11, not this definition | External verification | Use this label only for units Chapter 11 actually assigns as Accessible; keep A117.1 interiors outbound | Verified |
| 202 | Type A unit | Dwelling or sleeping unit designed and constructed for accessibility in accordance with this code and Type A units in **ICC A117.1** | Units scoped as Type A | Counts are Chapter 11 | External verification | Apply the Type A label to the Chapter 11 apartment-house quota; do not import A117.1 millimetres | Verified |
| 202 | Type B unit | Dwelling or sleeping unit designed and constructed for accessibility in accordance with this code and Type B units in **ICC A117.1** | Units intended to be occupied as a residence | Counts and exceptions are Chapter 11 | External verification | Label the remaining residential units Type B per Chapter 11; keep technical criteria on A117.1 | Verified |

## 9. Vertical space, mezzanine and penthouse

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 202 | Atrium | Vertical space closed at the top, connecting **two or more** stories in Group I-2 and I-3 or **three or more** stories in all other occupancies | Multi-storey enclosed void | I-2/I-3 use the two-story branch; this R-2 tower uses **three or more** stories. Open-to-sky courts are courts, not atria | Conditional | If a closed-top void links **three or more** stories, call it an atrium and take enclosure from **Section 404.6** without importing 404 values | Verified |
| 202 | Mezzanine | Intermediate level or levels between the floor and ceiling of any story and in accordance with **Section 505** | Intermediate loft within a story | Numeric area fraction is not in this definition | External verification | Size every intermediate level from **Section 505**; do not adopt commentary “one-third” as a Chapter 2 value | Verified |
| 202 | Penthouse | Enclosed, unoccupied roof-top structure used for sheltering mechanical and electrical equipment, tanks, elevators and related machinery, and vertical shaft openings | Rooftop MEP / shaft enclosure | Habitable or occupied rooftop program is not a 202 penthouse | Conditional | Keep penthouses unoccupied and MEP/shaft-only; occupied amenity rooms are stories, not penthouses. Geometry is **Section 1511** | Verified |
| 202 | Attic | Space between the ceiling framing of the top story and the underside of the roof | Roof void above the top ceiling | None stated | Conditional | If a framed ceiling creates an attic, apply Chapter 12 ventilation and Chapter 7 draftstop rules from those chapters, not from this glossary | Verified |
| 202 | Court | Open, uncovered space, unobstructed to the sky, bounded on three or more sides by exterior building walls or other enclosing devices | Light well / enclosed yard open at the top | Not an atrium (atrium is closed at the top) | Conditional | Label open-to-sky wells as courts; do not apply atrium (404) rules to an uncovered court | Verified |
| 202 | Yard | Open space, other than a court, unobstructed from the ground to the sky, except where specifically provided by this code, on the lot on which a building is situated | On-lot open space | Distinct from a court | Direct | Show yards on the site plan as open-to-sky lot space that is not a three-sided court | Verified |

## 10. Space types and public way

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 202 | Habitable space | Space in a building for living, sleeping, eating or cooking. Bathrooms, toilet rooms, closets, halls, storage or utility spaces and similar areas are not habitable spaces | Unit interior rooms | Bathrooms, halls, closets and utilities are not habitable | Direct | Apply Chapter 12 habitable-room light/ventilation only to living/sleeping/eating/cooking rooms | Verified |
| 202 | Occupiable space | Room or enclosed space designed for human occupancy in which individuals congregate for amusement, educational or similar purposes or in which occupants are engaged at labor, and which is equipped with means of egress and light and ventilation meeting this code | Occupied rooms, including residential | Crawl spaces, attics, penthouses and equipment platforms are identified elsewhere as unoccupied | Direct | Provide egress, light and ventilation for every occupiable room; do not treat penthouses or attics as occupiable | Verified |
| 202 | Common use | Interior or exterior circulation paths, rooms, spaces or elements that are not for public use and are made available for the shared use of two or more people | Resident corridors, shared lounges, shared toilets | Not public-use | Direct | Tag resident-only shared rooms as common use for Chapter 11; do not treat them as public-use areas | Verified |
| 202 | Public-use areas | Interior or exterior rooms or spaces made available to the general public | Lobbies or amenities open to the public | Distinct from common use | Conditional | If a lobby or amenity is open to the general public, label it public-use and apply the Chapter 11 public-use branch | Verified |
| 202 | Public way | Street, alley or other parcel of land open to the outside air leading to a street, deeded/dedicated/appropriated to the public, with clear width **and** height of **not less than 3 m** | Exit-discharge destination; FSD to public way | None stated | Direct | Confirm the discharge street/alley is ≥ **3 m** wide and ≥ **3 m** high before calling it a public way | Verified |
| 202 | Lot line | Line dividing one lot from another, or from a street or any public place | FSD and yard measurement | Condominium ownership lines are not lot lines (commentary not adopted as a substitute) | Direct | Measure FSD to recorded lot lines, not to unit-demise lines | Verified |

## 11. Egress term locks

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 202 | Means of egress | Continuous and unobstructed path of vertical and horizontal egress travel from any occupied portion of a building or structure to a public way, consisting of exit access, exit and exit discharge | Entire occupant escape path | None stated | Direct | Show the three-part egress path to a qualifying public way on the life-safety plan; keep Chapter 10 widths outbound | Verified |
| 202 | Exit | Portion of the means of egress between the exit access and the exit discharge or public way. Components: exterior exit doors at the level of exit discharge, interior exit stairways and ramps, exit passageways, exterior exit stairways and ramps, and horizontal exits | Protected egress after exit access | None stated | Direct | Tag only those components as exits; unenclosed stairs remain exit access | Verified |
| 202 | Exit access | Portion of the means of egress that leads from any occupied portion of a building or structure to an exit | Rooms, corridors, exit-access stairs/ramps | Crawl spaces and concealed attics are not exit access | Direct | Measure travel distance in the exit-access portion only; do not import 1017 limits here | Verified |
| 202 | Common path of egress travel | Exit-access travel from the most remote point of each room, area or space to the point where occupants have separate and distinct access to two exits or exit-access doorways | Rooms or units with a single direction of travel | Part of overall exit-access travel distance | Direct | Dimension the one-way path inside each apartment to the two-way choice; keep 1006 mm limits on Chapter 10 | Verified |
| 202 | Area of refuge | Area where persons unable to use stairways can remain temporarily to await instructions or assistance during emergency evacuation | Accessible egress waiting area | Required locations are Section 1009 | External verification | Provide 1009 areas of refuge where that section requires them; do not invent sizes from this definition | Verified |
| 202 | Open-ended corridor | Interior corridor open on each end and connecting to an exterior stairway or ramp at each end with no intervening doors or separation from the corridor | Breezeway / open corridor | Exterior-stair rules are Section 1027 | Conditional | If a breezeway is used, keep both ends open to exterior stairs with no doors; take 1027 geometry from Chapter 10 | Verified |
| 202 | Grade-floor emergency escape opening | Emergency escape and rescue opening whose clear-opening bottom is **not more than 1100 mm** above or below the finished ground level adjacent to the opening | Grade-level EERO classification (Section 1031) | Window/door still must meet 1031 size and location | Conditional | If a unit EERO is claimed as grade-floor, keep the sill within **1100 mm** of adjacent grade; keep 1031 opening size outbound | Verified |
| 202 | Interior exit stairway | Exit component that meets one or more means of egress design requirements (number of exits or exit-access travel distance) and provides a protected path to the exit discharge or public way | Enclosed exit stairs | Unenclosed stairs are exit access | Direct | Enclose tower stairs as interior exit stairways; measure travel to the enclosure door, not down the stair | Verified |
| 202 | Smokeproof enclosure | Exit stairway or ramp designed and constructed so that movement of products of combustion into the enclosure is limited | High-rise / underground exit stairs (later chapters) | Construction details are not in this definition | External verification | Flag high-rise exit stairs for the smokeproof-enclosure provisions of Chapter 10 / 403; do not invent vestibule sizes here | Verified |

## 12. Fire-protection and roof term locks

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 202 | Class I standpipe | System providing **65 mm** hose connections for fire departments and those trained in handling heavy fire streams | FD-use standpipe | Class selection is Chapter 9 / NFPA 14 | Direct | Show **65 mm** FD hose valves on the standpipe schematic; do not size residual pressure from this definition | Verified |
| 202 | Class II standpipe | System providing **40 mm** hose stations primarily for building occupants or FD initial response | Occupant-use hose stations | Often omitted where a Class I system is used | Conditional | Provide **40 mm** occupant hose stations only if a Class II or III system is selected in Chapter 9 | Verified |
| 202 | Class III standpipe | System providing **40 mm** hose stations for occupants **and** **65 mm** hose connections for the fire department | Combined occupant and FD use | None stated | Conditional | If Class III is selected, schedule both **40 mm** stations and **65 mm** connections | Verified |
| 202 | Steep slope | Roof slope **2** units vertical in **12** units horizontal (**17-percent** slope) or greater | Roof-covering classification | Material-specific slopes are Chapter 15 | Conditional | If any roof equals or exceeds **2:12 (17-percent)**, treat it as steep-slope in the Chapter 15 covering tables | Verified |
| 202 | Positive roof drainage | Design that accounts for deflections from all design loads and has sufficient additional slope so drainage occurs within **48 hours** of precipitation | Roof drainage design | None stated | Direct | Coordinate structure and roof slope so water leaves within **48 hours**; keep 1502 / 1611 drain sizes outbound | Verified |
| 202 | Metal roof panel | Interlocking metal sheet having a minimum installed weather exposure of **0.28 m²** per sheet | Metal-panel roof covering | None stated | Conditional | If metal panels are used, confirm each sheet’s exposed area is ≥ **0.28 m²**; keep Chapter 15 slopes outbound | Verified |

## 13. Project-use controls

1. Use **Verified** rows for initial scoping after the row trigger and branch are confirmed.
2. There is no **Verify source** row in this deliverable. The attached Chapter 2 extract has no appended dimensional tables. A stray parenthesis on the grade-plane **1.8 m** token was read as **1.8 m** and is treated as Verified.
3. Do not import Chapter 3 occupancy counts, Chapter 5 height/area tables, Chapter 9 sprinkler thresholds, Chapter 10 egress millimetres, Chapter 11 unit quotas, Section 403 high-rise extras, Section 505 mezzanine fractions, or ICC A117.1 geometry from this matrix.
4. Do not adopt commentary numbers (**36 m** / **126 m** high-rise, mezzanine “one-third”, townhouse four-test 1101/1102 path, NFPA 13 vs 13R) as Chapter 2 requirements.
5. Do not apply Group H chemical thresholds, flood/coastal definitions, agricultural, aircraft-hangar or similar unrelated occupancy locks to this R-2 tower unless the gap register is reopened for that use.
6. Record grade plane, FD-access height, unit type and public-way confirmation in the project Golden Thread; this matrix is not evidence of SCD NOC, SBPS approval or stamped compliance.

## 14. Coverage summary

Internal inventory of the attached Chapter 2 extract (numbered code, definition text, numbered list items in definitions; commentary, bibliography and figures excluded). Row-level records are not published.

- **Inventory scope:** numbered code, exceptions, tables, footnotes (commentary excluded)
- **Total independently checkable numeric records:** 208
- **Verified:** 208
- **Verify source:** 0

### Counts by top-level section

| Top-level section | Records |
|---|---:|
| 201 | 0 |
| 202 | 208 |

Coverage cross-check against `SBC 201 Chapter 2 Definitions (2024)_CS.md` was topics-only: grade plane / story above grade plane / high-rise **23 m**, dwelling vs sleeping unit, atrium story count, and Accessible / Type A / Type B labels. No CS.md value was copied into a matrix cell. Commentary **36 m** / **126 m** high-rise tiers in the CS.md were not adopted.

H-occupancy chemical, flood, masonry-unit, aerosol, explosive and similar classification thresholds are included in the **208** internal count and are omitted from Sections 4–12 as **Not typical** for this occupancy.

## 15. Unresolved-source register

No OCR, flattened-table or unreadable-footnote hold point remains in mandatory Chapter 2 text used for project-use rows. Page-split definition sentences (including grade-floor EERO and toxic LD50 item 2) join unambiguously. Figures were not used as source.

| Affected table / clause | Why unverified | Control note |
|---|---|---|
| — | No independently checkable numeric cell left unverified in the attached extract | Do not reconstruct outbound Chapter 3/5/9/10/11/403/505 or A117.1 values here; lock those from their own extracts |
