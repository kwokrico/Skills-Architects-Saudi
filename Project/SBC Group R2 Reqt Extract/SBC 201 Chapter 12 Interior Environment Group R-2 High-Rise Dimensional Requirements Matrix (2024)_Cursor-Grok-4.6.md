# SBC 201 Chapter 12 Interior Environment — Group R-2 High-Rise Dimensional Requirements Matrix (2024)

## 1. Document metadata and use limitation

- **Project basis:** Riyadh, Saudi Arabia; Group R-2 residential high-rise; an occupied floor is stated to be more than 23 m above the relevant reference level.
- **Deliverable tier:** Project-use matrices in Sections 1–16 (design-check rows, not pasted inventory), plus a coverage summary and unresolved-source register. The full row inventory is not published.
- **Code/source basis:** SBC 201 (2024), Chapter 12, source file `Reference\SBC 201 2024\source_reference\Chapter_12 — INTERIOR ENVIRONMENT.txt`.
- **Extraction audit:** Skill-finetune run. Project-use rows follow the chapter-extract row contract (noun-phrase checks, bold SI values, building-language triggers, named exceptions, check-specific actions). Internal inventory: **116** independently checkable numeric records (**108** Verified, **8** Verify source). Unresolved OCR is listed in the register and is not a design-release value.
- **Model:** Cursor Grok 4.6.
- **Prepared:** 2026-08-27.
- **Status:** Source-only architectural advisory matrix for design coordination. It is not a stamped compliance statement, mechanical/electrical/acoustic report, SCD NOC, SBPS approval, legal opinion, or permission to construct.
- **Outbound-source rule:** No value in this matrix has been imported from SBC 501, SBC 401 / NFPA 70, SBC 601 / SBC 602 / IECC, SBC 701, SBC 801, ASCE 24, TMS 302, Chapter 10 Section 1008, Chapter 29, Section 505.1, ICC A117.1 Section 808, commentary examples, Figure 1205.1, or the existing chapter summary. Where Chapter 12 sends the user elsewhere, this matrix records the dependency without supplying the outbound value.

### Scope and assumptions

1. Group R-2 and high-rise status are project statements, not independently verified classifications.
2. The exact Riyadh AHJ/permit pathway, project stage and SCD NOC status are unconfirmed; therefore this matrix does not conclude compliance.
3. Natural versus mechanical ventilation and natural versus artificial light are designer choices **per room**. Section 1205 yards and courts apply only where exterior openings provide required natural light or ventilation.
4. Climate zone for attic exceptions and Table 1202.3 is unconfirmed. Climate Zones 1–8 are shown as branches; a Riyadh zone is not assumed.
5. Automatic sprinkler protection is not selected in this chapter extract. Chapter 12 does not branch interior-environment dimensions on NFPA 13 versus 13R.
6. Building height, storey count above grade plane, basement versus crawl, mixed-use podium, amenity toilets and efficiency-unit mix are unconfirmed.
7. Table 1202.3 is concatenated OCR. No reconstructed climate-zone R-value is adopted as a design-release value.
8. Section 1207 enhanced classroom acoustics is Group E only and is omitted from project-use tables. The **565 m³** trigger is inventoried for coverage only.

## 2. Legends

### Applicability

| Status | Meaning |
|---|---|
| **Direct** | Expected to govern the stated R-2 tower basis, subject to confirmed geometry and design data. |
| **Conditional** | Governs only when the stated feature, use, climate-zone branch, natural-light/vent path or exception exists. |
| **Not typical** | Unrelated occupancy-only rule; omitted from this deliverable unless the gap register already opened that use. |
| **External verification** | Chapter 12 points to another section/code/standard, or the project/AHJ basis must be confirmed before use. |

### Source confidence

| Status | Meaning |
|---|---|
| **Verified** | Requirement and any stated numeric value were checked against unambiguous mandatory Chapter 12 source text. |
| **Verify source** | OCR, flattened table, page-split, or footnote attachment is unresolved. Not a design-release value. |

## 3. Project decision and gap register

| Decision / gap | Current project basis | Why it controls Chapter 12 application | Required project action |
|---|---|---|---|
| Natural vs mechanical ventilation | Unconfirmed per room | Selects 1202.5 openable-area / borrowed-vent rules versus SBC 501 rates; also switches Section 1205 on or off | Issue a room-by-room environmental schedule (natural, mechanical, or mixed) before freezing window and court sizes |
| Tight-dwelling ACH | Unconfirmed; high-rise envelopes are typically below **5** ACH at **50 Pa** | 1202.1 requires mechanical ventilation per SBC 501 Section 403 when the dwelling-unit test is below that threshold | Energy consultant to record blower-door results; until then treat units as mechanically ventilated and do not import Section 403 rates |
| Natural vs artificial light | Unconfirmed per room | Selects 1204.2 **8 percent** glazing and 1205 yards/courts versus 1204.3 **107 lux** | Lock daylight versus electric light per habitable room on the same environmental schedule |
| Climate zone | Unconfirmed | Controls 1202.2.1 **1/300** attic exception (Zones **6–8**), 1202.3 Item 4 (Zones **5–8**), Item 5.2 (Zones **1–3**) and Table 1202.3 R-values | Energy consultant / AHJ to lock the SBC climate zone; do not assume a Riyadh zone from memory |
| Roof / attic type | Unconfirmed: vented attic, unvented attic, or no concealed roof space | 1202.2 versus 1202.3; concrete roofs without attics do not take 1202.2.1 net-free area | Mark each roof assembly as vented, unvented (1202.3 items complete) or solid (no concealed space) |
| Storey count above grade plane | Occupied floor stated above 23 m; exact storeys unconfirmed | 1205.2 / 1205.3 grow yard/court width and court length per storey, capped at **14** stories, only if natural light/vent is used | Issue a signed datum sheet (grade plane, storeys, occupied-floor elevations) before sizing any required yard or court |
| Foundation type | Unconfirmed; high-rise typically basement/cellar | 1202.4 under-floor ventilation excepts spaces occupied by basements or cellars | Confirm crawl versus basement; skip 1202.4 if the tower sits on a basement |
| Unit type | Unconfirmed: standard dwelling vs efficiency; Accessible / Type A / Type B mix | 1208.3 areas versus 1208.4 **17.7 m²** living room and **750 mm** kitchen working space | Classify every unit; apply 1208.4 only to efficiency dwellings |
| Amenity / podium toilets | Unconfirmed | 1210.2.1 floor/base and 1210.3 privacy apply to spaces **other than** dwelling units and to public restrooms | Freeze which toilets are public/employee versus in-unit |
| Mixed-use / Group E | Unconfirmed | 1207 classroom acoustics and 1203 Exception 2 (F, H, S, U) are not R-2 dwelling rules | Do not apply Group E **565 m³** classroom criteria or F/H/S/U heating exceptions to apartments |
| NOC / consultants | Unconfirmed | SBC 501 rates, acoustic laboratory ratings and SCD acceptance cannot be concluded from Chapter 12 alone | Engage mechanical, acoustic and local code consultants before design freeze |

## 4. Scope and outbound controls

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1201.1 | Chapter scope | This chapter governs ventilation, temperature control, lighting, yards and courts, sound transmission, room dimensions, surrounding materials and rodent proofing of interior spaces | Interior spaces of buildings | None stated | Direct | Treat Chapter 12 as the interior-environment document for units, common rooms and roof spaces | Verified |
| 1202.5.2.1 | Bathroom mechanical exhaust | Rooms containing bathtubs, showers, spas and similar bathing fixtures shall be mechanically ventilated in accordance with **SBC 501** | Bathing rooms | None stated | External verification | Provide mechanical exhaust for every unit and amenity bath; rates from SBC 501 | Verified |
| 1202.5.2 / 1202.6 | Contaminant and hazard exhaust | Contaminant sources, flammable or combustible hazards and other sources covered in **SBC 501** or **SBC 801** shall be exhausted as required by both codes | Naturally ventilated or other spaces with those sources | None stated | External verification | Identify parking, commercial kitchen and chemical rooms and exhaust per those codes | Verified |
| 1204.5 | Means-of-egress lighting | Means of egress illuminated in accordance with **Section 1008.1** | Means of egress | None stated | External verification | Use the Chapter 10 matrix for egress illumination; do not copy 1008 values here | Verified |
| 1205.3.3 | Court drainage | Bottom of every court graded and drained to a public sewer or other approved disposal complying with **SBC 701** | Every court | None stated | External verification | Detail court drainage to SBC 701; do not import drainage sizes here | Verified |
| 1209.3 | Appliance access | Access to mechanical appliances in under-floor areas, attics, roofs or elevated structures in accordance with **SBC 501** | Appliances in those locations | None stated | External verification | Size appliance access from SBC 501 | Verified |
| 1210.1 | Plumbing fixture count | Number and type of plumbing fixtures in any occupancy shall comply with **Chapter 29** | Any occupancy | None stated | External verification | Count fixtures from Chapter 29 | Verified |

## 5. Occupied-space ventilation

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1202.1 | Occupied-space ventilation choice | Natural ventilation in accordance with Section 1202.5, **or** mechanical ventilation in accordance with **SBC 501** | Buildings | Bathroom mechanical exhaust still required by 1202.5.2.1; tight dwelling units: SBC 501 Section 403; I-2 / ambulatory care: SBC 501 Section 407 (not this occupancy) | Direct | Lock natural versus mechanical per room on the environmental schedule; do not import SBC 501 rates | Verified |
| 1202.1 | Tight-dwelling mechanical ventilation | Dwelling unit with infiltration **less than 5** air changes per hour when tested at **50 Pa** (IECC residential provisions Section 402.4.1.2 or equivalent in **SBC 602**) shall be ventilated by mechanical means in accordance with **Section 403 of SBC 501** | Dwelling units at that tightness | Ambulatory care and Group I-2 use SBC 501 Section 407, not this R-2 path | Direct | Treat sealed high-rise units as mechanically ventilated until blower-door results prove otherwise; do not import Section 403 rates | Verified |
| 1202.5 | Occupant-controlled openings | Natural ventilation through windows, doors, louvres or other openings to the outdoors, with operating mechanisms readily accessible and controllable by occupants | Occupied spaces using the natural path | None stated | Conditional | If a room is natural-vent, keep operators accessible to occupants | Verified |
| 1202.5.1 | Openable ventilation area | Openable area of openings to the outdoors **not less than 4 percent** of the floor area being ventilated | Occupied spaces using natural ventilation | None stated | Conditional | Schedule openable area at least 4 percent of each naturally ventilated room | Verified |
| 1202.5.1.1 | Borrowed ventilation opening | Unobstructed opening to the adjoining room **not less than 8 percent** of the interior-room floor area and **not less than 2.3 m²**; outdoor openable area based on the **total** floor area being ventilated | Interior room without outdoor openings, ventilated through an adjoining room | Sunroom with thermal isolation or patio cover: opening **not less than 8 percent** and **not less than 1.86 m²** | Conditional | Do not put a door in a borrowed-vent opening; size the outer-room openable area on the combined floor area | Verified |
| 1202.5.1.2 | Below-grade vent well | Outside horizontal clear space measured perpendicular to the opening shall be **one and one-half times** the depth of the opening (depth from average adjoining ground to the bottom of the opening) | Required natural-ventilation openings below grade | None stated | Conditional | Size window wells at 1.5 times opening depth if basement rooms are naturally ventilated | Verified |
| 1202.5.3 | Vent openings onto yards | Where natural ventilation is provided by openings onto yards or courts, those yards or courts shall comply with Section 1205 | Natural ventilation onto a yard or court | None stated | Conditional | Apply Section 10 of this matrix only to rooms that take outdoor air from a yard or court | Verified |

## 6. Roof and attic ventilation

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1202.2 | Roof ventilation path | Roof assemblies shall be ventilated in accordance with this section **or** shall comply with Section 1202.3 | Roof assemblies | None stated | Conditional | Pick vented or unvented attic on the roof section; do not mix the two in one concealed space | Verified |
| 1202.2.1 | Vented attic airspace and NFVA | Cross ventilation of each enclosed attic or rafter space; airspace **not less than 25 mm** between insulation and roof sheathing; net free ventilating area **not less than 1/150** of the space ventilated | Enclosed attics and rafter spaces with ceiling applied to the underside of roof framing | Exception: net free area **1/300** where **both** Climate Zones **6, 7 or 8** with Class I or II vapor retarder on the warm-in-winter side of the ceiling **and** at least **40 percent** and not more than **50 percent** of required venting in the upper portion, upper vents **not more than 900 mm** below the ridge (framing conflict may place them lower) | Conditional | On vented roofs keep a 25 mm ventilation path and size net-free vents at 1/150 unless both exception conditions are proven | Verified |
| 1202.2.2 | Attic vent opening protection | Vent openings with a least dimension **not less than 1.6 mm** and **not more than 6.4 mm** are permitted; openings larger than **6.4 mm** shall be screened with corrosion-resistant material having openings **1.6 mm to 6.4 mm** | Exterior openings into an attic of a building intended for human occupancy | Combustion air from an attic: Chapter 7 of SBC 501 (no values imported) | Direct | Specify insect and rodent screens on every attic vent | Verified |
| 1202.3 | Unvented attic envelope | Unvented attic and unvented enclosed rafter assemblies permitted only where Items 1–5 are met, including the attic completely within the building thermal envelope and **no** interior Class I vapor retarder on the attic floor | Unvented attic or unvented enclosed rafter assembly | 1. Special-use enclosures (swimming pool, data processing, hospital, art gallery). 2. Climate Zones **5 through 8** humidified **beyond 35 percent** during the three coldest months | Conditional | Do not claim 1202.3 unless every listed item is on the roof detail | Verified |
| 1202.3 Item 3 | Wood-shingle drying space | Where wood shingles or shakes are used, vented airspace **not less than 6.4 mm** between the shingles or shakes and the roofing underlayment above the structural sheathing | Unvented attic with wood shingles or shakes | None stated | Conditional | Keep a 6.4 mm drying space under wood roofs even if the attic is unvented | Verified |
| 1202.3 Item 4 | Cold-climate vapor retarder | In Climate Zones **5, 6, 7 and 8**, any air-impermeable insulation shall be a Class II vapor retarder or shall have a Class II vapor retarder coating or covering in direct contact with the underside of the insulation | Unvented attic in those climate zones | Riyadh climate zone is unconfirmed | Conditional | Apply only after the energy consultant locks the climate zone | Verified |
| 1202.3 Item 5.1.4 | Sheathing temperature method | Sufficient rigid board or sheet insulation above the structural roof sheathing to keep the monthly average underside temperature **above 7°C**, assuming interior air **20°C** and exterior air equal to the monthly average of the **three** coldest months | Alternative to Table 1202.3 R-values under Item 5.1 | None stated | Conditional | Document the three-month average outdoor temperatures; do not use commentary examples | Verified |
| 1202.3 Item 5.2 | Climate 1–3 vapor-diffusion port | In Climate Zones **1, 2 and 3**, air-permeable insulation in unvented attics: vapor-diffusion port **not more than 300 mm** below the highest roof point; port area **not less than 1/600** of the ceiling area; membrane **not less than 20 perms** (ASTM E96 Procedure A); **not less than 50 mm** between blocking and roof sheathing; roof slope **not less than 3:12**; where only air-permeable insulation is used directly below the sheathing, supply air **not less than 23.6 L/s per 100 m²** of ceiling | Unvented attic using Item 5.2 | Item 5.3: air supplied from occupiable-space ductwork or a supply fan while the conditioning system operates | Conditional | Use this package only if the climate zone is 1–3 | Verified |
| Table 1202.3 | Unvented-attic R-value | Flattened OCR table; no reconstructed climate-zone R-value is adopted | Items 5.1.2 and 5.1.3 condensation control | Footnote a points to IECC Section C402.2.1 or equivalent in SBC 601 / SBC 602 (no value imported) | Conditional | Hold the insulation R-value until a published Table 1202.3 is checked | Verify source |

## 7. Under-floor and crawl-space ventilation

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1202.4 | Under-floor ventilation | Space between the bottom of the floor joists and the earth shall be ventilated in accordance with 1202.4.1, 1202.4.2 or 1202.4.3 | Under-floor space | Spaces occupied by basements or cellars are excepted | Conditional | If the tower sits on a basement, skip this section; if a true crawl exists, pick one of the three methods | Verified |
| 1202.4.1 | Crawl vent covers | Cross-ventilation openings through foundation walls; covering least dimension **not greater than 6.4 mm**; listed covers include perforated plate **not less than 1.8 mm** thick, expanded plate **not less than 1.2 mm** thick, hardware cloth of **0.90 mm** wire or heavier, and mesh with least dimension **not greater than 3.2 mm** | Natural crawl ventilation | Operable louvres only where ventilation is per 1202.4.1.2 | Conditional | Specify a listed cover with openings not greater than 6.4 mm | Verified |
| 1202.4.1.1 | Open-earth crawl vents | Net area of ventilation openings **not less than 0.67 m² for each 100 m²** of crawl-space area | Crawl with uncovered earth floor | None stated | Conditional | Size foundation vents at 0.67 m² per 100 m² of crawl area | Verified |
| 1202.4.1.2 | Covered-earth crawl vents | Net area of ventilation openings **not less than 0.67 m² for each 1000 m²** of crawl-space area | Ground covered with a Class I vapor retarder | None stated | Conditional | With a Class I ground cover, size vents at 0.67 m² per 1000 m² | Verified |
| 1202.4.3.1 | Mechanical crawl ventilation | Continuously operated mechanical ventilation at **1.02 L/s for each 10 m²** of crawl-space ground surface, with the ground covered by a Class I vapor retarder | Mechanically ventilated crawl | Alternative: condition the crawl in accordance with SBC 501 and insulate walls per IECC or equivalent in SBC 601 or 602 (1202.4.3.2) | Conditional | If using fans instead of vents, provide 1.02 L/s per 10 m² and a Class I ground cover | Verified |
| 1202.4.4 | Flood openings | Under-floor ventilation openings deemed to meet ASCE 24 flood-opening requirements only where designed and installed **in accordance with ASCE 24** | Buildings in flood hazard areas | No ASCE 24 values imported | External verification | If the site is in a flood hazard area, coordinate flood openings with ASCE 24 separately | Verified |

## 8. Temperature control

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1203.1 | Occupied-space heating | Active or passive space heating capable of maintaining an indoor temperature of **not less than 20°C** at a point **900 mm** above the floor on the design heating day | Interior spaces intended for human occupancy | 1. Spaces whose primary purpose is not associated with human comfort. 2. Group F, H, S or U occupancies | Direct | Show heating capacity for units, corridors and amenity rooms; outdoor design temperatures are named as SBC 701 Appendix D and are not imported | Verified |

## 9. Lighting

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1204.1 | Occupied-space lighting choice | Natural light by exterior glazed openings in accordance with 1204.2 **or** artificial light in accordance with 1204.3; required glazed openings shall open onto a public way, yard or court in accordance with 1205 | Every space intended for human occupancy | None stated | Direct | Lock natural versus artificial light per room; Section 1205 applies only to rooms that take required natural light | Verified |
| 1204.2 | Natural glazed area | Minimum net glazed area **not less than 8 percent** of the floor area of the room served | Spaces using natural light | None stated | Conditional | Schedule glazed area at least 8 percent of each naturally lit room | Verified |
| 1204.2.1 | Borrowed natural light | Interior room permitted as a portion of an adjoining room where **one-half** of the common wall is open and unobstructed and the opening is **not less than one-tenth** of the interior-room floor area or **2.3 m²**, whichever is greater | Interior room without its own required glazing | Sunroom with thermal isolation or patio cover: glazed common-wall area **not less than one-tenth** of the interior-room floor area or **1.86 m²**, whichever is greater | Conditional | Keep borrowed-light openings at least half the wall and at least 2.3 m² (or 1.86 m² for a sunroom); size outer glazing on the combined floor area | Verified |
| 1204.2.2 | Natural-light exterior opening | Required 1204.2 openings shall open directly onto a public way, yard or court as set forth in Section 1205 | Required natural-light openings | 1. Roofed porch abutting a public way, yard or court, with ceiling height **not less than 2.1 m** and longer side **at least 65 percent** open and unobstructed. 2. Skylights need not open directly onto a public way, yard or court | Conditional | Do not count a glazed opening onto an enclosed balcony unless the porch exception is met | Verified |
| 1204.3 | Artificial illumination | Average illumination of **107 lux** over the area of the room at a height of **750 mm** above the floor | Spaces using artificial light instead of 1204.2 | None stated | Direct | Specify 107 lux at 750 mm in interior rooms without qualifying natural light | Verified |
| 1204.4 | Dwelling-unit stair illumination | Stairways within dwelling units and exterior stairways serving a dwelling unit shall have **not less than 11 lux** on tread runs | Those stairways | Stairways in other occupancies are governed by Chapter 10 (no values imported). Controls: **NFPA 70** or equivalent in **SBC 401** (1204.4.1) | Direct | Light in-unit and unit-serving exterior stairs to 11 lux on treads; locate switches per the electrical code; common egress stairs follow Chapter 10 | Verified |

## 10. Yards and courts

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1205.1 | Yard and court applicability | This section applies to yards and courts adjacent to exterior openings that provide natural light or ventilation; such yards and courts shall be on the same lot as the building | Those openings | Does not apply where the facing rooms use mechanical ventilation and artificial light | Conditional | Skip this section for mechanically ventilated, artificially lit rooms | Verified |
| 1205.2 | Yard width | Yards **not less than 900 mm** in width for buildings **two stories or less** above grade plane; for buildings more than two stories, increased at **300 mm** for each additional story; buildings **exceeding 14 stories** computed on the basis of **14 stories** | Yards serving required natural light or ventilation openings | None stated | Conditional | Compute yard width from storey count above grade plane; do not use Figure 1205.1 commentary millimetres | Verified |
| 1205.3 | Court width and length | Courts **not less than 900 mm** in width (**1800 mm** where windows open on opposite sides); length **not less than 3000 mm** unless bounded on one end by a public way or yard; more than two stories: increase **300 mm** in width and **600 mm** in length for each additional story; buildings **exceeding 14 stories** computed on **14 stories** | Courts serving required natural light or ventilation openings | None stated | Conditional | Size the court from storey count; do not copy commentary five-storey examples | Verified |
| 1205.3.1–1205.3.2 | Court access and air intake | Access shall be provided to the bottom of courts for cleaning; courts **more than two stories** in height shall have a horizontal air intake at the bottom **not less than 1.0 m²** leading to the exterior unless abutting a yard or public way | Courts as 1205.3 | Air intake not required if the court abuts a yard or public way | Conditional | Provide a 1.0 m² low-level intake on fully bounded courts taller than two stories | Verified |

## 11. Sound transmission

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1206.1 | Sound-transmission scope | Common interior walls, partitions and floor/ceiling assemblies between adjacent dwelling units and sleeping units, or between those units and adjacent public areas | R-2 units and public or service areas | None stated | Direct | Apply this section to every demising wall and every unit-to-corridor or lobby floor | Verified |
| 1206.2 | Airborne sound rating | STC **not less than 50** where tested in accordance with ASTM E90, or field NNIC **not less than 45** in accordance with ASTM E336; penetrations treated to maintain the required ratings | Separations in 1206.1 | Entrance doors are not required to meet the STC/NNIC number but shall be tight fitting to the frame and sill; masonry STC may be calculated per TMS 302 or tested per ASTM E90 | Direct | Specify STC 50 (or NNIC 45 field) wall and floor-ceiling types; keep unit entry doors tight-fitting | Verified |
| 1206.3 | Impact sound rating | Floor-ceiling assemblies shall have IIC **not less than 50** where tested in accordance with ASTM E492, or field NISR **not less than 45** in accordance with ASTM E1007 | Floor-ceilings between units, or between a unit and a public or service area | Engineering analysis comparison to ASTM E492 assemblies is permitted | Direct | Specify IIC 50 (or NISR 45 field) on every unit-to-unit and unit-to-corridor floor | Verified |

## 12. Interior room dimensions

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1208.1 | Habitable room plan dimension | Habitable spaces other than a kitchen **not less than 2100 mm** in any plan dimension; kitchens shall have a clear passageway **not less than 900 mm** between counter fronts and appliances or counter fronts and walls | Habitable spaces and kitchens | Kitchens are exempt from the 2100 mm plan-dimension rule | Direct | Keep bedrooms, living and dining as a 2100 mm plan cylinder; keep 900 mm kitchen passage | Verified |
| 1208.2 | Occupiable ceiling height | Occupiable spaces, habitable spaces and corridors: ceiling height **not less than 2250 mm** above the finished floor; bathrooms, toilet rooms, kitchens, storage rooms and laundry rooms: **not less than 2100 mm** | Those rooms | 2. Sloped ceiling: prescribed height in **one-half** the area; portions **less than 1500 mm** AFF excluded from 1208.3 area. 3. Mezzanines: Section 505.1 (no value imported). 4. Corridors contained within a Group R dwelling or sleeping unit: **not less than 2100 mm**. Exception 1 (one- and two-family beams) is not this occupancy | Direct | Hold 2250 mm in units, common rooms and public corridors; 2100 mm in baths, kitchens, stores, laundry and in-unit corridors | Verified |
| 1208.2.1 | Lowered ceiling area | Any room with a lowered ceiling shall have the minimum ceiling height in **two-thirds** of the area thereof; the lowered ceiling shall be **not less than 2100 mm** | Rooms required to have the 1208.2 minimum ceiling height | Section title is OCR-damaged (`Faturated` / `fumed`); the two-thirds and 2100 mm figures are unambiguous in the charging sentence | Direct | If a bulkhead or dropped ceiling is used, keep the full minimum height over at least two-thirds of the room and never drop below 2100 mm | Verified |
| 1208.3 | Dwelling-unit room area | Every dwelling unit shall have **no fewer than one** room of **not less than 11.2 m²** net floor area; other habitable rooms **not less than 6.5 m²** net | Dwelling units | Kitchens are not required to be of a minimum floor area | Direct | Show at least one 11.2 m² room per unit; keep other habitable rooms at least 6.5 m² | Verified |

## 13. Efficiency dwelling units

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1208.4 Item 1 | Efficiency living-room area | Living room of **not less than 17.7 m²** of floor area | Efficiency dwelling units | Efficiency units conforming to 1208.4 are not required to comply with 1208.3 minimum areas | Conditional | If studios are efficiency units, give the living room 17.7 m²; do not use the commentary 17.5 m² figure | Verified |
| 1208.4 Items 2 and 4 | Efficiency closet and bathroom | Separate closet; separate bathroom containing a water closet, lavatory and bathtub or shower | Efficiency dwelling units | None stated | Conditional | Plan a separate closet and a full bathroom; fixture clearances named as SBC 701 are not imported | Verified |
| 1208.4 Item 3 | Efficiency kitchen working space | Kitchen sink, cooking appliance and refrigerator each having a clear working space of **not less than 750 mm** in front; light and ventilation conforming to this chapter | Efficiency dwelling units other than Accessible, Type A and Type B | Accessible, Type A and Type B units follow those unit standards instead of the 750 mm working-space rule | Conditional | Keep 750 mm in front of sink, cooktop and fridge unless the unit is Accessible, Type A or Type B | Verified |

## 14. Access to unoccupied spaces

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1209.1 | Crawl access opening | **Not fewer than one** access opening **not less than 450 mm by 600 mm** | Crawl spaces | None stated | Conditional | Provide a 450 × 600 mm crawl hatch if a crawl exists | Verified |
| 1209.2 | Attic access opening | Opening **not less than 560 mm by 760 mm** to any attic area having a clear height of **over 760 mm**; clear headroom **not less than 760 mm** in the attic at or above the access opening | Attics exceeding 760 mm clear height | None stated | Direct | Provide a 560 × 760 mm attic hatch with 760 mm headroom at the opening | Verified |

## 15. Toilet and bathroom finishes and privacy

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1210.2.1 | Non-dwelling wet-room floor | In other than dwelling units, toilet, bathing and shower-room floors shall have a smooth, hard, non-absorbent surface; wall base **not less than 100 mm** | Common and amenity toilet and bathing rooms | Dwelling-unit bathrooms are outside this floor and base rule | Conditional | Use a 100 mm non-absorbent base in lobby, gym and podium toilets; do not use the commentary 150 mm figure | Verified |
| 1210.2.2 | Splash-zone wall finish | Walls and partitions within **600 mm** of service sinks, urinals and water closets shall have a smooth, hard, non-absorbent surface to a height of **not less than 1200 mm** above the floor; accessories sealed to protect structural elements from moisture | Those fixtures | 1. Dwelling units and sleeping units. 2. Toilet rooms not accessible to the public and having **not more than one** water closet | Conditional | Tile or equivalent to 1200 mm within 600 mm of amenity water closets, urinals and service sinks | Verified |
| 1210.2.3–1210.2.4 | Shower surround and tub joint | Shower compartments and walls above bathtubs with installed shower heads finished with a smooth non-absorbent surface to a height **not less than 1800 mm** above the drain inlet; built-in tubs with showers shall have waterproof joints between the tub and adjacent wall | Showers and tubs with shower heads | None stated | Direct | Take wet-area finishes to 1800 mm above the drain in unit and amenity showers; seal tub-to-wall joints | Verified |
| 1210.3 | Public restroom visual screening | Public restrooms shall be visually screened from outside entry or exit doorways, including where mirrors would compromise personal privacy | Public restrooms | Visual screening not required for single-occupant toilet rooms with a lockable door | Conditional | Offset or screen amenity toilet entries so the room is not visible from the door | Verified |
| 1210.3.1 | Water-closet compartments | Each water closet utilized by the public or employees shall occupy a separate compartment with walls or partitions and a door | Public or employee water closets | 1. Single-occupant toilet room with a lockable door. 2. Child day-care toilet rooms with two or more water closets may omit one compartment (not typical). 3. Group I-3 housing areas (not typical) | Conditional | Enclose every amenity and employee water closet unless it is a lockable single-occupant room | Verified |
| 1210.3.2 | Urinal partitions | Partitions shall begin at a height **not more than 300 mm** from the finished floor and extend **not less than 1500 mm** above the finished floor; they shall extend from the wall **not less than 450 mm** or to a point **not less than 150 mm** beyond the outermost front lip of the urinal, whichever is greater | Urinals used by the public or employees | 1. Single-occupant or family/assisted-use toilet room with a lockable door. 2. Child day-care toilet rooms with two or more urinals may omit partitions at one urinal (not typical) | Conditional | If amenity urinals exist, provide partitions from not more than 300 mm to at least 1500 mm AFF and at least 450 mm deep, or 150 mm beyond the lip | Verified |

## 16. Project-use controls

1. Use **Verified** rows for initial scoping after the row trigger and branch are confirmed.
2. Treat every **Verify source** row (Table 1202.3) as a design hold point; no affected value is to be placed in issued-for-approval drawings without a published-source check.
3. Do not apply Section 1205 yard and court growth to rooms that are mechanically ventilated and artificially lit.
4. Do not apply Group E Section 1207 classroom acoustics, one- and two-family 1208.2 Exception 1 beam projections, or F/H/S/U heating exceptions to this R-2 tower.
5. Do not import SBC 501 ventilation rates, SBC 701 Appendix D outdoor design temperatures, ICC A117.1 Section 808 criteria, Chapter 10 Section 1008 lux values, Chapter 29 fixture counts, commentary 150 mm wall bases, commentary 17.5 m² efficiency rooms, or Figure 1205.1 millimetres.
6. Record AHJ, climate-zone, ventilation-path and unit-type decisions in the project Golden Thread; this matrix is not evidence of SCD NOC or stamped compliance.

## 17. Coverage summary

Internal inventory of the attached Chapter 12 extract (numbered code, exceptions, tables, footnotes; commentary excluded). Row-level records are not published.

- **Inventory scope:** numbered code, exceptions, tables, footnotes (commentary excluded)
- **Total independently checkable numeric records:** 116
- **Verified:** 108
- **Verify source:** 8
- **Numeric records in Section 1201:** 0

### Counts by top-level section

| Top-level section | Records |
|---|---:|
| 1201 | 0 |
| 1202 | 50 |
| 1203 | 2 |
| 1204 | 11 |
| 1205 | 13 |
| 1206 | 4 |
| 1207 | 1 |
| 1208 | 15 |
| 1209 | 7 |
| 1210 | 13 |

### Appended-table coverage

| Appended table | Records | Verify source records |
|---|---:|---:|
| Table 1202.3 | 8 | 8 |

Coverage cross-check against `SBC 201 Chapter 12 Interior Environment (2024)_CS.md` was topics-only: ventilation path and ACH trigger; attic/crawl; heating and light; yards/courts; STC/IIC; room dimensions; toilet finishes. No CS.md value was copied into a matrix cell. Commentary-only quantities (attic worked example 0.67 m², 150 mm wall base, 17.5 m² efficiency living room, Figure 1205.1 yard millimetres) were not inventoried as code records.

## 18. Unresolved-source register

Hold points for the 8 **Verify source** inventory records. Counts are record counts, not distinct numeric values. No value in this register is a design-release figure.

| Affected table / clause | Why unverified | Control note |
|---|---|---|
| Table 1202.3 | 8 flattened climate-zone / R-value cells (`CLIMATE ZONEMINIMUM R-VALUE…R-54R-10…`) | Verify the published table before specifying unvented-attic rigid insulation under Items 5.1.2 and 5.1.3; do not reconstruct R-values from memory |
