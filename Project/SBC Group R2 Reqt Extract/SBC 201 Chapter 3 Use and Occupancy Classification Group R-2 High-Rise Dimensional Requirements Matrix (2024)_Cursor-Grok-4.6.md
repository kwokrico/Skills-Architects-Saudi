# SBC 201 Chapter 3 Use and Occupancy Classification — Group R-2 High-Rise Dimensional Requirements Matrix (2024)

## 1. Document metadata and use limitation

- **Project basis:** Riyadh, Saudi Arabia; Group R-2 residential high-rise as a project statement. Chapter 3 does not define high-rise; occupied-floor height is not a value in this chapter.
- **Deliverable tier:** Project-use matrices in Sections 4–10 (design-check rows, not pasted inventory), plus project-use controls, a coverage summary and an unresolved-source register. The full row inventory is not published.
- **Code/source basis:** SBC 201 (2024), Chapter 3, source file `Reference\SBC 201 2024\source_reference\Chapter_03 — USE AND OCCUPANCY CLASSIFICATION.txt`.
- **Extraction audit:** Skill extract. Project-use rows follow the chapter-extract row contract (noun-phrase checks, bold SI values, building-language triggers, named exceptions, check-specific actions). Internal inventory: **450** independently checkable numeric records (**60** Verified, **390** Verify source). Unresolved OCR is listed in the register and is not a design-release value.
- **Model:** Cursor Grok 4.6.
- **Prepared:** 2026-08-27.
- **Status:** Source-only architectural advisory matrix for design coordination. It is not a stamped occupancy classification, fire-strategy, SCD NOC, SBPS approval, legal opinion, or permission to construct.
- **Outbound-source rule:** No value in this matrix has been imported from Chapter 2, Chapter 4, Chapter 5, Section 403, 406, 414, 415, 419, 420, 508, 509, SBC 801, SBC 1101/1102, commentary examples, Figure 308.1, or bibliography years. Where Chapter 3 sends the user elsewhere, this matrix records the dependency without supplying the outbound value.

### Scope and assumptions

1. Group R-2 and high-rise status are project statements, not independently verified classifications.
2. The exact Riyadh AHJ/permit pathway, project stage and SCD NOC status are unconfirmed; therefore this matrix does not conclude compliance.
3. Automatic sprinkler protection is not selected. Chapter 3 classification of Group R-2 does not branch on NFPA 13 versus 13R. Sprinkler notes on Tables 307.1(1)–(2) are MAQ-increase branches only and are OCR-unresolved.
4. Mixed-use podium, amenity assembly, parking, occupied roof, live/work, unit type and care uses are unconfirmed. Those branches are shown, not assumed.
5. Commentary numbers are not adopted, including a 30-day transient stay, `0.45 m²` per person, `10 percent` mixed-occupancy, and the `67.5 m²` assembly example.
6. Tables 307.1(1) and 307.1(2) are concatenated OCR. No reconstructed MAQ is adopted as a design-release value.

## 2. Legends

### Applicability

| Status | Meaning |
|---|---|
| **Direct** | Expected to govern the stated R-2 tower basis, subject to confirmed geometry and design data. |
| **Conditional** | Governs only when the stated feature, use, occupant load, mixed-use/podium condition or exception exists. |
| **Not typical** | Unrelated occupancy-only rule; omitted from this deliverable unless the gap register already opened that use. |
| **External verification** | Chapter 3 points to another section/code/standard, or the project/AHJ basis must be confirmed before use. |

### Source confidence

| Status | Meaning |
|---|---|
| **Verified** | Requirement and any stated numeric value were checked against unambiguous mandatory Chapter 3 source text. |
| **Verify source** | OCR, flattened table, page-split, or footnote attachment is unresolved. Not a design-release value. |

## 3. Project decision and gap register

| Decision / gap | Current project basis | Why it controls Chapter 3 application | Required project action |
|---|---|---|---|
| Unit type | Unconfirmed: dwelling units vs sleeping units | 310.3 charges R-2 as sleeping units **or more than two** dwelling units; dwelling vs sleeping also selects later Chapter 4/11 paths | Freeze a unit schedule (apartment dwelling vs congregate sleeping) on the code data sheet |
| Transient vs permanent stay | Unconfirmed; serviced apartments / short-stay product not locked | 310.2 is primarily transient; 310.3 is primarily permanent. A dual-purpose product must satisfy both (302.1) | Confirm the marketed length of stay; if both transient and permanent uses exist, classify for both R-1 and R-2 |
| Mixed-use podium | Unconfirmed: retail, offices, parking, dining | 302.1 sends multiple occupancy groups to **Section 508**; do not import 508 percentages here | Occupancy-by-room schedule for podium, amenities and parking |
| Amenity assembly | Unconfirmed: gym, prayer hall, indoor pool, party room, dining | 303.1.1 / 303.1.2 reclassify small assembly; larger accessory rooms stay Group A and become mixed occupancy | Calculate occupant load and floor area for every amenity room before locking Group A vs B vs R-2 |
| Occupied roof | Unconfirmed | 302.1 classifies occupied roofs by the occupancy they most nearly resemble and sends geometry to **503.1.4** | Name the roof use (assembly, residential amenity, or unoccupied) on the roof plan |
| Live/work | Unconfirmed | 310.3 lists live/work units as Group R-2; 302.2 sends certain uses to **Chapter 4** without naming Section 419 in the Chapter 3 code text | Confirm whether any unit includes a tenant-operated nonresidential use |
| In-unit day care / custodial care | Unconfirmed | 305.2.2 keeps **five or fewer** children as the primary occupancy; 305.2.3 is Group R-3 for dwelling-unit day care; 308.5.4 is R-3 / SBC 1101/1102 | Confirm whether any unit or amenity is a care facility; do not assume R-3 for an R-2 apartment |
| Building-level nursery / kindergarten | Unconfirmed | 308.5.2 / 308.5.2.1 locate nursery/kindergarten on the ground floor, with a **1:12** / **1.5 m** ramp branch to the first floor | If a nursery or kindergarten is added, apply 308.5.2; otherwise omit that geometry |
| Parking / repair | Unconfirmed public or private parking | Open/enclosed public parking is Group S-2 (311.3) and is sent to **406**; repair garages are S-1 and sent to **406.8** | Classify parking as public S-2 or private (312.2 / 406.3); keep repair out of the residential garage |
| Hazardous materials | Unconfirmed: pool chemicals, generator fuel, cleaning stores | 307.1 is Group H only when MAQ in Tables 307.1(1)–(2) is exceeded in a control area per **414** | Produce a control-area / chemical inventory; do not adopt OCR MAQ cells |
| Sprinkler / MAQ notes | Unconfirmed NFPA 13 vs 13R | Table 307.1 notes d/e/f/g increase or unlimited MAQ only on the **903.3.1.1** path; OCR unresolved | Do not use reconstructed MAQ multipliers; lock sprinkler standard with the fire engineer |
| NOC / fire strategy | Unconfirmed | Mixed occupancy, high-rise and H/MAQ cannot be concluded from Chapter 3 alone | Engage the qualified local code/fire consultants before design freeze |

## 4. Classification mechanics

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 301.1 | Chapter classification scope | This chapter controls classification of all buildings and structures as to occupancy and use | Every building and structure | None stated | Direct | Put occupancy group(s) on the code data sheet from this chapter, not from a later chapter’s title | Verified |
| 302.1 | Occupancy group assignment | Classify the structure into one or more occupancy groups in this section based on hazards and risks associated with the intended purpose | Every structure or portion | Unlisted purpose: classify as the occupancy it most nearly resembles | Direct | Assign Group R-2 to the residential tower once 310.3 is confirmed; do not leave floors unclassified | Verified |
| 302.1 | Multipurpose space | An area, room or space occupied at different times for different purposes shall comply with all applicable requirements associated with each purpose | Rooms with more than one programmed use | None stated | Conditional | If a lounge is also used as a banquet or prayer hall, apply every matching occupancy, not the lighter one only | Verified |
| 302.1 | Mixed occupancy groups | Structures containing multiple occupancy groups shall comply with **Section 508** | More than one occupancy group in the structure | Accessory assembly rooms that 303.1.2 keeps out of Group A are not classified as Assembly; 508 values are not in this chapter | External verification | Send podium, parking and over-threshold amenities to the Section 508 mixed-occupancy analysis; do not import 508 limits here | Verified |
| 302.1 | Occupied-roof classification | Occupied roofs shall be classified in the group the occupancy most nearly resembles, according to fire safety and relative hazard, and shall comply with **Section 503.1.4** | Occupied roofs | None stated | Conditional | Classify the roof terrace as the use it actually hosts; take occupied-roof construction limits from 503.1.4 | Verified |
| 302.2 | Use designation / Chapter 4 | Occupancy groups contain subordinate uses; certain uses require specific limitations and controls in **Chapter 4** and elsewhere | Uses listed in 302.1 group descriptions | None stated | External verification | After the group is locked, apply the matching Chapter 4 special-occupancy section named by this chapter (for example 420 at 310.1, 406 at 311.3.1); do not import those values here | Verified |

## 5. Group R-2 charging

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 310.1 | Residential Group R | Group R is a building or portion used for sleeping purposes when not classified as Institutional Group I and when not regulated by **SBC 1101/1102** | Sleeping accommodation not Group I and not under SBC 1101/1102 | 310.4.1 and 310.4.2 SBC 1101/1102 options apply to R-3 care/lodging, not this tower | Direct | Keep the tower on SBC 201 Group R; do not apply the one- and two-family code to a high-rise apartment building | Verified |
| 310.1 | Group R Section 420 | Group R occupancies not constructed in accordance with SBC 1101/1102 as permitted by 310.4.1 and 310.4.2 shall comply with **Section 420** | Group R not on the SBC 1101/1102 path | None stated | External verification | Send dwelling/sleeping-unit separation, sprinklers and alarms to Section 420; do not copy 420 ratings here | Verified |
| 310.3 | Group R-2 definition | Group R-2 occupancies containing sleeping units **or more than two** dwelling units where the occupants are primarily permanent in nature | Permanent residential occupancy of that form | Listed R-2 uses below; congregate living is R-2 only with **more than 16** occupants | Direct | Confirm more than two dwelling units (or sleeping units) and primarily permanent occupancy on the code data sheet | Verified |
| 310.3 | Apartment-house classification | Apartment houses are included in Group R-2 | Apartment houses with primarily permanent occupants | None stated in 310.3 | Direct | Classify conventional apartment floors as Group R-2 | Verified |
| 310.3 | Congregate living R-2 | Congregate living facilities (non-transient) with **more than 16** occupants are Group R-2 | Non-transient congregate living | **16 or fewer** occupants is Group R-3 (310.4), not this tower’s default | Conditional | If staff housing or boarding is congregate, count occupants; over 16 stays R-2, 16 or fewer is not R-2 | Verified |
| 310.3 | Other listed R-2 uses | Boarding houses (non-transient), dormitories, hotels (non-transient), motels (non-transient) and vacation timeshare properties are included in Group R-2 | Those uses with primarily permanent occupants | Transient hotels/motels are Group R-1 (310.2) | Conditional | Reclassify only if the product is dormitory, non-transient hotel/motel, boarding or timeshare rather than apartments | Verified |
| 310.3 | Live/work units | Live/work units are included in Group R-2 | Dwelling or sleeping unit with a tenant-operated nonresidential portion | None stated in 310.3; 302.2 still sends certain uses to Chapter 4 | Conditional | If any unit is live/work, classify it Group R-2; take Chapter 4 live/work controls from that chapter, not from commentary | Verified |

## 6. Transient, R-3 and R-4 branches

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 310.2 | Group R-1 transient | Group R-1 occupancies contain sleeping units where the occupants are primarily transient in nature, including hotels and motels (transient) | Primarily transient sleeping units | Boarding/congregate (transient) with **more than 10** occupants are also R-1; **10 or fewer** is R-3 | Conditional | If the tower sells short-stay/hotel rooms, classify those units R-1, or both R-1 and R-2 where 302.1 multipurpose applies | Verified |
| 310.2 | Transient congregate threshold | Boarding houses (transient) and congregate living facilities (transient) with **more than 10** occupants are Group R-1 | Transient congregate / boarding | **10 or fewer** occupants is Group R-3 (310.4) | Conditional | Do not use the R-1 congregate threshold for a permanent apartment house | Verified |
| 310.4 | Two-dwelling-unit R-3 | Buildings that do not contain **more than two** dwelling units are Group R-3 when not classified as R-1, R-2, R-4 or I | One- or two-dwelling buildings | High-rise apartment houses exceed two dwelling units and stay R-2 | Direct | Do not reclassify the tower as R-3; the two-dwelling cap is a different building type | Verified |
| 310.4 | Nontransient congregate R-3 | Congregate living facilities (nontransient) with **16 or fewer** occupants are Group R-3 | Small nontransient congregate living | **More than 16** occupants is R-2 (310.3) | Conditional | Use this branch only for a small staff-house or similar; not for the apartment tower | Verified |
| 310.5 | Group R-4 custodial care | Group R-4 is **more than five** but **not more than 16** persons, excluding staff, residing on a 24-hour basis in a supervised residential environment and receiving custodial care | Supervised custodial care at that count | Construction as defined for Group R-3 except as otherwise provided; Conditions 1 and 2 in 310.5.1–310.5.2 | Conditional | Classify assisted-living / group-home wings as R-4 or I-1, not R-2 apartments | Verified |

## 7. Amenity and assembly spaces

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 303.1 | Assembly Group A | Group A is gathering for civic, social or religious functions; recreation; food or drink consumption; or awaiting transportation | Assembly purpose | Small-building and small-space reclassifications in 303.1.1–303.1.2; Group E association in 303.1.3 | Conditional | Test every amenity against 303.1 before calling it residential accessory | Verified |
| 303.1.1 | Small assembly tenant | A building or tenant space used for assembly purposes with occupant load **less than 50** persons shall be classified as Group B | Entire building or tenant space used for assembly | None stated | Conditional | Classify a small café tenant as Group B when occupant load is below 50; at 50 or more it is Group A | Verified |
| 303.1.2 | Accessory assembly occupant load | A room or space used for assembly purposes with occupant load **less than 50** persons and accessory to another occupancy shall be classified as Group B **or** as part of that occupancy | Accessory assembly room | Either this occupant-load path **or** the 303.1.2 area path may be used; 303.1.3 is Group E only | Conditional | For each amenity, compute occupant load; below 50 and accessory, keep it Group B or R-2 | Verified |
| 303.1.2 | Accessory assembly floor area | A room or space used for assembly purposes that is **less than 70 m²** in area and accessory to another occupancy shall be classified as Group B **or** as part of that occupancy | Accessory assembly room | Independent of the occupant-load item; either threshold is sufficient | Conditional | If occupant load is 50 or more, still test floor area; under **70 m²** and accessory, keep Group B or R-2 | Verified |
| 303.3 | Food and drink assembly | Group A-2 includes banquet halls, gaming areas, and restaurants, cafeterias and similar dining facilities including associated commercial kitchens | Food and/or drink consumption | Occupant load **less than 50** for a whole tenant is Group B (303.1.1); accessory small rooms use 303.1.2 | Conditional | Classify residents’ dining, banquet and commercial kitchens as A-2 unless a 303.1.1 / 303.1.2 threshold is met | Verified |
| 303.4 | Recreation and worship assembly | Group A-3 includes, among others, gymnasiums (without spectator seating), indoor swimming pools (without spectator seating), and mosques / prayer halls | Worship, recreation or amusement not classified in A-1, A-2, A-4 or A-5 | Spectator seating at an indoor pool or gym is Group A-4 (303.5); 303.1.2 may keep a small accessory room out of Group A | Conditional | Classify gym, prayer hall and indoor pool without spectators as A-3 unless 303.1.2 applies; add A-4 if spectator seating is provided | Verified |
| 303.5 | Indoor spectator assembly | Group A-4 is indoor sporting events and activities **with spectator seating**, including swimming pools | Indoor sport with a defined seating area | Without spectator seating the same pool or gym is A-3 (303.4) | Conditional | If the amenity pool or gym has spectator seating, classify A-4 and send the mix to Section 508 | Verified |
| 303.1.5 | Special amusement | Special amusement areas shall comply with **Section 411** | Special amusement areas | None stated | Conditional | If a puzzle room or special amusement is added, use Section 411; do not import 411 values here | Verified |

## 8. Podium, storage and parking

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 304.1 | Business Group B | Group B is office, professional or service-type transactions, including storage of records and accounts | Office / professional / service use | Training and skill development is Group B where not classified as Group A | Conditional | Classify management offices, clinics and tutoring rooms as Group B unless occupant load pushes the room to Group A | Verified |
| 304.1 | Small dining as Group B | Dining facilities **not more than 230 m²** in area are included in Group B | Dining not associated with the A-2 restaurant list in 303.3 | Food processing / commercial kitchens **more than 230 m²** and not associated with restaurants are Group F-1 (306.2) | Conditional | Size a non-restaurant dining room against **230 m²**; larger associated restaurant dining stays on the 303.3 / 303.1.1 path | Verified |
| 306.2 | Large commercial kitchen | Food processing establishments and commercial kitchens not associated with restaurants, cafeterias and similar dining facilities **more than 230 m²** in area are Group F-1 | Detached or non-restaurant food processing above that area | Associated A-2 kitchens follow 303.3 | Conditional | Do not classify a restaurant kitchen as F-1; use F-1 only for a standalone kitchen/plant over **230 m²** | Verified |
| 309.1 | Mercantile Group M | Group M is display and sale of merchandise with stocks of goods accessible to the public | Retail / wholesale sales | Accessory storage may remain with the principal occupancy (311.1.1) | Conditional | Classify podium retail as Group M and send the R-2 / M mix to Section 508 | Verified |
| 309.2 | Mercantile hazardous display | Aggregate quantity of nonflammable solid and nonflammable or noncombustible liquid hazardous materials stored or displayed in a single control area of Group M shall not exceed **Table 414.2.5(1)** | Group M control areas | Table 414.2.5(1) is not in this chapter | External verification | If podium retail sells pool chemicals or similar, take display limits from Table 414.2.5(1), not from OCR Table 307.1 | Verified |
| 309.3 | Motor-fuel dispensing | Motor fuel-dispensing facilities shall comply with **Section 406.7** | Fuel-dispensing facilities | None stated | Conditional | If a filling station is on the plot, use 406.7; do not import those values here | Verified |
| 311.1.1 | Accessory storage | A room or space used for storage purposes that is accessory to another occupancy shall be classified as part of that occupancy | Accessory storage | Independent storage is Group S and mixed occupancy under 508 | Direct | Classify typical residential stores, bin rooms and house tanks that serve the apartments as Group R-2, not S-1 | Verified |
| 311.1.2 | Combustible storage | High-piled stock or rack storage, or attic, under-floor and concealed spaces used for storage of combustible materials, shall be in accordance with **Section 413** | Those storage conditions | None stated | Conditional | If combustible storage is high-piled or in concealed spaces, use Section 413; do not import 413 values here | Verified |
| 311.3 | Public parking Group S-2 | Public parking garages, open or enclosed, are included in Group S-2 | Public parking without repair-garage operations | Repair garages are Group S-1 (311.2) and shall comply with **406.8** (311.2.2) | Conditional | Classify podium/public parking as S-2; keep vehicle repair out of that garage | Verified |
| 311.3.1 | Parking garage construction | Public parking garages shall comply with **Section 406.4** and with **406.5** (open) or **406.6** (enclosed) | Public parking garages | None stated | External verification | Detail open versus enclosed parking from Section 406; do not copy 406 openings or area figures here | Verified |
| 312.2 | Private garage / carport | Private garages and carports shall comply with **Section 406.3** | Private garages and carports | Public parking is 311.3.1, not this path | Conditional | Use 406.3 only for private residential garages, not a public podium garage | Verified |
| 312.1 | Small communications structure | Communication equipment structures with a gross floor area of **less than 140 m²** are included in Group U | Small communications buildings | Larger occupied equipment buildings follow the occupancy they most nearly resemble | Conditional | Classify a small site telecom hut under **140 m²** as Group U | Verified |
| 312.1 | Tall fence | Fences **more than 2.1 m** in height are included in Group U | Fences above that height | None stated | Conditional | Show site fences over **2.1 m** as Group U structures on the plot classification | Verified |

## 9. Care uses in or with the tower

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 305.2 | Group E day care | Group E day care is **more than five** children **older than 2.5** years receiving educational, supervision or personal care for **fewer than 24** hours per day | Day care of that size, age and duration | 305.2.2 and 305.2.3 reduce small facilities; infants **2.5** years or less are I-4 unless 308.5.1 applies | Conditional | If a commercial day care is in the podium, classify E or I-4 from headcount, age and hours; do not call it R-2 amenity | Verified |
| 305.2.2 | Five-or-fewer day care | A facility having **five or fewer** children receiving such day care shall be classified as part of the primary occupancy | Day care at that headcount | 305.2.3 dwelling-unit path is Group R-3 | Conditional | Five or fewer children in an R-2 amenity or unit stay with the primary occupancy (R-2) | Verified |
| 305.2.3 | Dwelling-unit day care | A facility as above within a dwelling unit and having **five or fewer** children receiving such day care shall be classified as Group R-3 | Day care inside a dwelling unit | Commentary discusses R-2 multifamily as 305.2.2; that commentary number/path is not adopted as a substitution | Conditional | Do not silently convert an R-2 apartment to R-3 for in-unit day care; lock the path with the AHJ | Verified |
| 308.2.3 | Custodial care as R-4 | A facility housing **not fewer than six** and **not more than 16** persons receiving custodial care shall be classified as Group R-4 | 24-hour custodial care at that count | **More than 16** is Group I-1 (308.2); **five or fewer** is R-3 / SBC 1101/1102 (308.2.4) | Conditional | Assisted-living counts of 6–16 are R-4, not R-2 | Verified |
| 308.3.2 | Small medical care | A facility with **five or fewer** persons receiving medical care shall be classified as Group R-3 or shall comply with SBC 1101/1102 if sprinklered per 903.3.1.3 or SBC 1101/1102 Section 2904 | Medical care at that headcount | **More than five** incapable of self-preservation on a 24-hour basis is Group I-2 (308.3) | Conditional | A small in-home medical-care use is not Group R-2; it is R-3 or I-2 depending on headcount | Verified |
| 308.5.3 | Small I-4 as primary occupancy | A facility having **five or fewer** persons receiving custodial care shall be classified as part of the primary occupancy | Custodial care fewer than 24 hours, not in a dwelling unit | 308.5.4 dwelling-unit path is R-3 / SBC 1101/1102 | Conditional | Five or fewer day-care recipients in a common room stay with the primary occupancy | Verified |
| 308.5.2–308.5.2.1 | Nursery / kindergarten location | Classrooms and facilities for nursery and kindergarten stages (children **under 6** years) shall be on the ground floor; first-floor location is permitted only with a ramp of maximum slope **1:12**, minimum clear width **1.5 meters**, and two handrails suitable for children | Nursery or kindergarten classrooms | Ground-floor location needs no ramp branch | Conditional | If a nursery/kindergarten is added above ground floor, provide the 308.5.2.1 ramp; otherwise omit | Verified |
| 308.5.1 | Infant day care as Group E | Child day care for **more than five** but **not more than 100** children **2.5** years or less of age may be Group E where care rooms are on a level of exit discharge serving those rooms and each care room has an exit door directly to the exterior | Infant/toddler day care at that count | Otherwise Group I-4 (308.5) | Conditional | Do not use this Group E relief unless every infant room has a direct exterior exit on the discharge level | Verified |

## 10. Hazardous materials and Group H

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 307.1 | Group H MAQ trigger | Group H is manufacturing, processing, generation or storage of physical or health-hazard materials in quantities **in excess of** those allowed in control areas complying with **Section 414**, based on MAQ in **Table 307.1(1)** and **Table 307.1(2)** | Hazardous materials in the building | Roof/canopy storage is outdoor storage per SBC 801; 307.1.1 lists uses that are not Group H | Conditional | Inventory pool chemicals, fuel and cleaners against control areas; if MAQ is exceeded, classify H and use **415** / SBC 801 | Verify source |
| 307.1.1 | Uses not Group H | Occupancies in the 16 listed items shall not be classified as Group H, but as the occupancy they most nearly resemble | Listed processes and storage arrangements | Closed piping for machinery; refrigeration systems; stationary batteries; fuel cells; and other listed items still follow Section 414 / SBC 801 as applicable | Conditional | Apply the matching 307.1.1 item (generator fuel piping, batteries, cleaning solvents) before calling a room Group H | Verified |
| 307.1.1 Item 4 | Closed-system cleaning | Cleaning establishments using combustible liquid solvents with flash point of **60°C** or higher in listed closed systems, separated by **1-hour** fire barriers (707) and/or **1-hour** horizontal assemblies (711), shall not be Group H | That cleaning process | Item 5: solvent flash point **90°C** or higher | Conditional | If a dry-cleaning tenant is added, lock flash point and 1-hour separation; do not default to Group H | Verified |
| 307.2 | Hazardous materials any quantity | Hazardous materials in any quantity shall conform to this code, including **Section 414**, and **SBC 801** | Any quantity of hazardous materials | Group H buildings also meet Section 415 | External verification | Even below MAQ, specify 414 / SBC 801 controls; do not import those quantities here | Verified |
| 307.4–307.5 | Flammable-liquid pressure split | Class I, II or IIIA flammable or combustible liquids in normally open containers/systems, or closed systems pressurized at **more than 103.5 kPa**, are Group H-2 when MAQ is exceeded; the same liquids in normally closed containers/systems at **103.5 kPa or less** are Group H-3 | Those liquids when Group H applies | Oxidizer Class 3 uses the same **103.5 kPa** open/closed split | Conditional | For fuel rooms that become Group H, use the 103.5 kPa open/closed test to pick H-2 vs H-3 | Verified |
| Tables 307.1(1)–307.1(2) | Control-area MAQ cells | Maximum allowable quantity per control area for physical-hazard and health-hazard materials | Control areas storing or using listed materials | Notes include sprinkler and cabinet increases (903.3.1.1), **50 percent** / **5 liters** consumer-product relief, and **90 kg** / **75 liters** Class 3 oxidizer maintenance allowance; cells and most notes are flattened OCR | External verification | Do not enter any reconstructed kilogram, litre or cubic-metre MAQ on drawings; verify the published tables | Verify source |

## 11. Project-use controls

1. Use **Verified** rows for initial occupancy scoping after the row trigger is confirmed on the project (apartment house, amenity present, podium retail, parking type).
2. Treat every **Verify source** row as a hold point. Tables 307.1(1) and 307.1(2) are not design-release values.
3. Do not import mixed-occupancy percentages, incidental-use ratings, high-rise triggers, live/work area caps, parking-garage openings, or MAQ from Chapter 2, 4, 5, 9, 403, 406, 414, 419, 420, 508, 509, SBC 801 or SBC 1101/1102.
4. Do not adopt commentary as a requirement: 30-day stay, `0.45 m²` per person, `10 percent` of story, or the `67.5 m²` assembly example.
5. Show sprinkler/MAQ branches until the fire engineer locks NFPA 13 versus 13R; do not assume a multiplier from notes d/e/f.
6. Record occupancy-by-room decisions in the project Golden Thread; this matrix is not evidence of SCD NOC or stamped compliance.

## 12. Coverage summary

Internal inventory of the attached Chapter 3 extract (numbered code, exceptions, tables, footnotes; commentary excluded). Row-level records are not published. Figures, including Figure 308.1, were not inventoried.

- **Inventory scope:** numbered code, exceptions, tables, footnotes (commentary excluded)
- **Total independently checkable numeric records:** 450
- **Verified:** 60
- **Verify source:** 390

### Counts by top-level section

| Top-level section | Records |
|---|---:|
| 301 | 0 |
| 302 | 0 |
| 303 | 3 |
| 304 | 1 |
| 305 | 6 |
| 306 | 1 |
| 307 | 8 |
| 308 | 20 |
| 309 | 0 |
| 310 | 14 |
| 311 | 0 |
| 312 | 2 |

### Appended-table coverage

| Appended table | Records | Verify source records |
|---|---:|---:|
| Table 307.1(1) quantity cells | 360 | 360 |
| Table 307.1(1) flattened notes c, d, e, k | 6 | 6 |
| Table 307.1(1) note l | 1 | 0 |
| Table 307.1(2) quantity cells | 24 | 24 |
| Table 307.1(2) notes c, d, e | 4 | 0 |

No Chapter 3 `*_CS.md` was present for a coverage cross-check. No CS.md value was copied into a matrix cell.

## 13. Unresolved-source register

Hold points for the 390 **Verify source** inventory records. Counts are record counts, not distinct numeric values. No value in this register is a design-release figure.

| Affected table / clause | Why unverified | Control note |
|---|---|---|
| Table 307.1(1) | 360 flattened physical-hazard MAQ cells across pages 0235–0236; concatenated storage/use columns; values such as `3455` / `10.45` are unreadable cell joins | Do not reconstruct kilograms, litres or cubic metres from memory or from IBC recall; verify the published table before any H vs non-H decision |
| Table 307.1(1) notes c, d, e, k | 6 numeric footnote tokens (`50 percent`, `5 liters`, two `100 percent` increases, `90 kg`, `75 liters`) trapped in the same flattened HTML | Confirm consumer-product, sprinkler/cabinet and oxidizer-maintenance notes on the printed table; do not apply OCR multipliers |
| Table 307.1(2) | 24 flattened health-hazard MAQ cells; gaseous/liquefied pairs concatenated (`2501`, `450375`) | Verify corrosive / highly toxic / toxic MAQ on the published table; do not use OCR tokens |
| 307.1 project-use row | Group H trigger depends on the unverified tables | Keep the 307.1 row as **Verify source** until the published MAQ is confirmed |
| 303.6 heading | Group A-5 use list appears after 303.5 without a numbered heading (page 0204) | A-5 outdoor assembly is not typical for this tower; if an outdoor stadium is added, verify the printed 303.6 heading before citing |
