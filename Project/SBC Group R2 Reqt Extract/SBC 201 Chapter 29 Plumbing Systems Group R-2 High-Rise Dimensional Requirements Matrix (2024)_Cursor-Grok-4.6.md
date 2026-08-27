# SBC 201 Chapter 29 Plumbing Systems — Group R-2 High-Rise Dimensional Requirements Matrix (2024)

## 1. Document metadata and use limitation

- **Project basis:** Riyadh, Saudi Arabia; Group R-2 residential high-rise; an occupied floor is stated to be more than 23 m above the relevant reference level.
- **Deliverable tier:** Project-use matrices in Sections 1–11 (design-check rows, not pasted inventory), plus a coverage summary and unresolved-source register. The full row inventory is not published.
- **Code/source basis:** SBC 201 (2024), Chapter 29, source file `Reference\SBC 201 2024\source_reference\Chapter_29 — PLUMBING SYSTEMS.txt`.
- **Extraction audit:** Skill-finetune run. Project-use rows follow the chapter-extract row contract (noun-phrase checks, bold SI values, building-language triggers, named exceptions, check-specific actions). Internal inventory: **59** independently checkable numeric records (**37** Verified, **22** Verify source). Unresolved OCR is listed in the register and is not a design-release value.
- **Model:** Cursor Grok 4.6.
- **Prepared:** 2026-08-27.
- **Status:** Source-only architectural advisory matrix for design coordination. It is not a stamped compliance statement, plumbing design, SCD NOC, SBPS approval, legal opinion, or permission to construct.
- **Outbound-source rule:** No value in this matrix has been imported from SBC 701, SBC 702, SBC 801, the International Property Maintenance Code, SBC 901, Section 1210, Chapter 11 / Section 1110.2.1 / ICC A117.1, Chapter 10 occupant-load tables, ISPSC Section 609, commentary sample problems, Commentary Figures, or the existing chapter summary. Where Chapter 29 sends the user elsewhere, this matrix records the dependency without supplying the outbound value.

### Scope and assumptions

1. Group R-2 and high-rise status are project statements, not independently verified classifications.
2. The exact Riyadh AHJ/permit pathway, project stage and SCD NOC status are unconfirmed; therefore this matrix does not conclude compliance.
3. Automatic sprinkler protection is unconfirmed. Chapter 29 does not branch fixture counts or clearances on NFPA 13 versus 13R.
4. Building height, storey count, mixed-use podium, amenity program, food service, parking attendants, covered/open mall configuration and unit type (dwelling versus sleeping) are unconfirmed.
5. Table 2902.1 is concatenated OCR (`TABLE 29.21` / `TABLE 29.01.1`). **No fixture ratio is adopted**, including any apartment, hotel, mercantile or assembly token visible in the flattened string.
6. Fixture quality, urinal substitution, drinking-fountain substitution, accessible millimetres and toilet-room finishes are outbound and are not supplied here.

## 2. Legends

### Applicability

| Status | Meaning |
|---|---|
| **Direct** | Expected to govern the stated R-2 tower basis, subject to confirmed geometry and design data. |
| **Conditional** | Governs only when the stated feature, use, occupant load, public-utilization or mixed-use/podium condition exists. |
| **Not typical** | Unrelated occupancy-only rule; omitted from this deliverable unless the gap register already opened that use. |
| **External verification** | Chapter 29 points to another section/code/standard, or the project/AHJ basis must be confirmed before use. |

### Source confidence

| Status | Meaning |
|---|---|
| **Verified** | Requirement and any stated numeric value were checked against unambiguous mandatory Chapter 29 source text. |
| **Verify source** | OCR, flattened table, page-split, or footnote attachment is unresolved. Not a design-release value. |

## 3. Project decision and gap register

| Decision / gap | Current project basis | Why it controls Chapter 29 application | Required project action |
|---|---|---|---|
| Table 2902.1 fixture ratios | Attached table is concatenated OCR; no ratio adopted | Controls every water closet, lavatory, bathtub/shower, drinking fountain and service-sink count | Verify the published Table 2902.1 before any fixture schedule; do not reconstruct apartment or amenity ratios from memory, commentary samples or the chapter summary |
| Actual use vs Group R-2 label | Unconfirmed amenity, podium, lobby, food-service and parking uses | 2902.1 sizes fixtures by actual use of the space, which may differ from the Chapter 3 group | Freeze use-by-room on the fixture schedule; apply the published table row that matches the actual use |
| Occupant load | Unconfirmed for units, stories, amenities and outdoor terraces | 2902.1 takes occupant load from this code; 2902.1.1 splits, rounds and aggregates from that load | Produce the Chapter 10 occupant-load schedule first; do not invent loads here |
| Unit type | Unconfirmed: dwelling units versus sleeping units | 2902.2 Exception 1 relieves separate-sex facilities in both; Table 2902.1 still needs the matching published residential row | Classify every R-2 unit; do not transpose a hotel/motel row onto apartments |
| Public vs in-unit toilets | Unconfirmed which toilets serve the public, employees or only a unit | 2902.3, 2902.3.1–2902.3.6, 2903.1.2 and 2903.1.4–2903.1.5 apply to public/employee rooms, not to 2902.2 Exception 1 unit baths | Tag every toilet as in-unit, common/employee or public on the plumbing plans |
| Mixed-use / podium / mall | Unconfirmed | Business **25**, mercantile **100**, mall travel **90 m** and service-sink **91 m** branches apply only if those uses exist | Identify every non-residential tenant; do not apply mall travel to a conventional residential core |
| Food preparation | Unconfirmed commercial kitchen or F&B | 2902.3.1 and 2902.3.2 control public toilet access and doors into public food-prep rooms | If F&B is provided, route public toilets off the kitchen and keep toilet doors out of the prep room |
| Parking attendants | Unconfirmed | 2902.3 Exception 1 drops public toilets only for no-attendant garages; employees still need toilets | Confirm attended vs unattended parking; keep employee travel within 2902.3.3 |
| Family / assisted-use rooms | Unconfirmed; trigger lives in Chapter 11 | 2902.1.2 and 2902.2.1 allow those rooms to count, but 1110.2.1 decides when they are required | Accessibility consultant to lock family/assisted-use count from Chapter 11; do not import 1110 values here |
| SBC 701 / 1210 / A117.1 | Unconfirmed MEP and accessibility packages | Fixture quality, substitution, finishes and accessible millimetres are not published as Chapter 29 values | Plumbing, interiors and accessibility consultants to lock SBC 701, Section 1210 and Chapter 11 / ICC A117.1 separately |
| NOC / AHJ | Unconfirmed | Fixture counts and public-toilet access cannot be concluded as approved from this chapter alone | Engage the qualified local plumbing/code consultant before design freeze |

## 4. Scope and outbound charging

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 2901.1 | Chapter plumbing scope | This chapter **and SBC 701** govern design, construction, erection and installation of plumbing components, appliances, equipment and systems in buildings covered by this code | All plumbing in the tower | None stated | Direct | Place Chapter 29 and SBC 701 on the code sheet as the plumbing charging pair; do not import 701 fixture-design values here | Verified |
| 2901.1 | Toilet and bathing-room construction | Toilet and bathing rooms shall be constructed in accordance with **Section 1210** | Every toilet and bathing room | Commentary 1209 is not the charging section | External verification | Finish and privacy of toilet/bathing rooms from Section 1210; do not copy 1210 millimetres into this matrix | Verified |
| 2901.1 | Sewage, maintenance and alterations | Private sewage disposal shall conform to **SBC 702**. Use and maintenance: **SBC 801**, the International Property Maintenance Code and **SBC 701**. Alteration, repair, relocation, replacement and addition: **SBC 901** and **SBC 701** | Private sewage, occupied-building maintenance, or alteration work | None stated | External verification | Route those scopes to the named codes; keep their values off this matrix | Verified |

## 5. Fixture-count method

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 2902.1 | Actual-use fixture basis | Provide plumbing fixtures in the minimum number shown in Table 2902.1 based on the **actual use** of the building or space; occupant load is determined by this code | Every building or space that requires fixtures | Uses not shown in Table 2902.1 are considered individually by the building official | Direct | Schedule fixtures from actual room use and the Chapter 10 occupant load, not from the R-2 group label alone | Verified |
| Table 2902.1 | Minimum fixture ratios | Fixture-ratio cells cannot be recovered from the attached extract (concatenated OCR). **No ratio is adopted.** | Actual use of the building or space | Uses not shown are considered individually by the building official; table footnotes are not readable in this extract | External verification | Open the published Table 2902.1 before counting any water closet, lavatory, bathtub/shower, drinking fountain or service sink | Verify source |
| 2902.1.1 | Sex-split fixture calculation | Divide the total occupant load **in half** for each sex; apply Table 2902.1 ratios to that sex load; round fractions **up** to the next whole number; for multiple occupancies, **sum fractions first, then round up** | Fixture counts that use sex-distributed Table 2902.1 ratios | Exception 1: approved statistical split other than **50 percent** each sex. Exception 2: all-gender multiple-user rooms use **100 percent** of total load. Exception 3: sex distribution is not required where single-user water closets and bathing-room fixtures follow 2902.1.2 | Conditional | Use this method on common, amenity and podium fixture schedules; do not sex-split in-unit baths that follow 2902.2 Exception 1 | Verified |
| 2902.1.1 Ex. 2 | All-gender multiple-user count | Calculate the minimum fixture count at **100 percent** of total occupant load; each fixture type shall be in accordance with **ICC A117.1**; each urinal provided shall be located in a stall | Multiple-user facilities designed to serve all genders | ICC A117.1 geometry is outbound and is not supplied here | Conditional | If an all-gender amenity toilet is proposed, size on full load, put every urinal in a stall, and take accessible fixture geometry from ICC A117.1 | Verified |
| 2902.1.3 | Lavatory-to-water-closet distribution | Where **two or more** toilet rooms are provided for each sex, distribute the required lavatories proportionately to the required water closets | More than one toilet room per sex in the same building or tenant space | None stated | Conditional | Where amenity or podium toilets are split across several rooms per sex, proportion lavatories to each room’s water-closet count | Verified |

## 6. Unit-level facilities

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 2902.2 Ex. 1 | In-unit separate-sex relief | Separate facilities for each sex shall not be required for dwelling units and sleeping units | Plumbing fixtures required inside an R-2 dwelling or sleeping unit | 2902.2 still requires separate-sex facilities where this exception does not apply | Direct | Do not provide male/female pairs inside apartments; keep unit baths as single-household rooms | Verified |
| 2902.1.2 | Single-user fixture contribution | Plumbing fixtures in single-user toilet and bathing rooms, including family or assisted-use rooms required by **Section 1110.2.1**, shall contribute toward the building or tenant-space total and shall be identified as available to all persons regardless of sex. The total may be based on separate facilities or on the aggregate of single-user and separate facilities | Single-user or family/assisted-use rooms provided | Section 1110.2.1 decides when family/assisted-use rooms are required; those counts are not imported here | Conditional | Credit each single-user/family room once toward the building total; label the door for all persons; do not double-count one room as both sexes | Verified |
| 2902.1.1 Ex. 3 | Single-user sex-split relief | Distribution of the sexes is not required where single-user water closets and bathing-room fixtures are provided in accordance with 2902.1.2 | Single-user water closets and bathing rooms used to meet the count | Does not delete Table 2902.1; it only drops the 50/50 split | Conditional | Where common toilets are all single-user rooms, count fixtures without a male/female split | Verified |

## 7. Common, public and employee toilets

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 2902.2 | Separate-sex common facilities | Where plumbing fixtures are required, provide separate facilities for each sex | Required fixtures outside 2902.2 Exception 1 dwelling/sleeping units | Exception 1: dwelling and sleeping units. Exception 2: total occupant load, including employees and customers, of **15 or fewer**. Exception 3: mercantile occupancies with maximum occupant load **100 or fewer**. Exception 4: business occupancies with maximum occupant load **25 or fewer** | Direct | Provide separate male and female toilets for lobby, amenity and other common required facilities unless a listed exception is demonstrated | Verified |
| 2902.2 Ex. 2 | Small-occupancy one-toilet permission | Separate facilities shall not be required where the total occupant load, including employees and customers, is **15 or fewer** | Structure or tenant space at that load | Does not delete the requirement to provide fixtures | Conditional | Apply only to a mapped small tenant or amenity whose combined load is 15 or fewer | Verified |
| 2902.2 Ex. 3 | Small mercantile one-toilet permission | Separate facilities shall not be required in mercantile occupancies in which the maximum occupant load is **100 or fewer** | Mercantile occupancy or tenant at that load | Business Exception 4 (**25 or fewer**) is a separate podium-B branch | Conditional | Apply only if a podium/retail mercantile space is confirmed at that load | Verified |
| 2902.2 Ex. 4 | Small business one-toilet permission | Separate facilities shall not be required in business occupancies with maximum occupant load **25 or fewer** | Business occupancy or tenant at that load | Mercantile Exception 3 (**100 or fewer**) is a separate podium-M branch | Conditional | Apply only if a podium/management business space is confirmed at that load | Verified |
| 2902.2.1 | Family rooms as the two required toilets | Where a building or tenant space requires a separate toilet facility for each sex and each facility is required to have only **one** water closet, **two** family or assisted-use toilet facilities may serve as the required separate facilities | Each required sex facility has only one water closet | Those family/assisted-use rooms shall not be required to be identified for exclusive use by either sex under 2902.4 | Conditional | If each sex is at one water closet, two family/assisted-use rooms may replace the male/female pair; leave the sex pictogram off those two doors | Verified |
| 2902.3 | Public and employee toilets | Structures and tenant spaces intended for public utilization shall provide public toilet facilities for customers, patrons and visitors. Employees shall be provided with toilet facilities. Fixture numbers follow Section 2902 for all users. Employee toilets may be separate or combined with public toilets | Public-utilization portions and all employee areas | Exception 1: public toilets not required for parking garages with no parking attendants. Exception 2: public toilets not required for quick-transaction structures/tenant spaces with public access area **30 m² or less** | Conditional | Provide public toilets for lobby, amenities and any public tenant; always provide employee toilets; combine them only where the plan shows shared use | Verified |
| 2902.3 Ex. 1 | No-attendant parking public-toilet relief | Public toilet facilities shall not be required for parking garages where there are no parking attendants | Unattended parking garage | Employees still require toilet facilities under 2902.3 | Conditional | Omit public toilets from an unattended podium garage; still show employee toilets within the 2902.3.3 travel limit | Verified |
| 2902.3 Ex. 2 | Quick-transaction public-toilet relief | Public toilet facilities shall not be required for structures and tenant spaces intended for quick transactions, including takeout, pickup and drop-off, having a public access area **less than or equal to 30 m²** | Quick-transaction public access at that area | Employees still require toilet facilities | Conditional | Apply only to a mapped pickup/drop-off lobby at or under 30 m²; do not use it for seated F&B or amenity lounges | Verified |
| 2902.3.5 | Pay-facility surplus | Where pay facilities are installed, they shall be in excess of the required minimum facilities. Required facilities shall be free of charge | Any pay toilet or bathing room | None stated | Conditional | If a pay amenity toilet is proposed, keep the required free count in addition | Verified |
| 2902.3.6 | Multi-occupant toilet door lock | Where a toilet room is provided for the use of multiple occupants, the egress door shall not be lockable from the inside of the room | Multi-occupant toilet room | Does not apply to family or assisted-use toilet rooms | Conditional | Specify non-lockable inside hardware on amenity gang toilets; allow an inside lock only on family/assisted-use rooms | Verified |

## 8. Access, travel and location

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 2902.3.1 | Public-toilet access route | The route to public toilet facilities required by 2902.3 shall not pass through kitchens, storage rooms or closets. Access shall be from within the building or from the exterior. The public shall have access at all times the building is occupied | Public toilet facilities required | None stated | Conditional | Route lobby and amenity public toilets on a public corridor; keep the rooms available during occupancy | Verified |
| 2902.3.2 | Toilet door into food-prep | Toilet rooms shall not open directly into a room used for the preparation of food for service to the public | Toilet adjacent to public food preparation | None stated | Conditional | If F&B is provided, interpose a lobby, corridor or other room between the toilet door and the prep room | Verified |
| 2902.3.3 | Non-mall toilet travel | Required public and employee toilet facilities shall be located **not more than one story** above or below the space served, and the path of travel shall **not exceed 150 m** | Occupancies other than covered and open mall buildings | Factory and industrial employee travel may exceed this section where the location and distance are approved | Direct | Measure common and employee toilet travel on each tower and podium floor; keep the room within one story and 150 m | Verified |
| 2902.3.4 | Mall toilet travel | Required public and employee toilet facilities shall be located **not more than one story** above or below the space served, and the path of travel shall **not exceed 90 m**. Facilities are based on total square metres within the covered mall or within the open-mall perimeter line, installed in each store or in a central toilet area. Central-toilet travel is measured from the store or tenant main entrance; where employees have no in-store toilet, measure from the employees’ work area | Covered or open mall building | None stated | Conditional | Use the 90 m / one-story mall branch only if a covered or open mall is confirmed; do not apply it to a conventional residential core | Verified |
| 2902.4 | Sex designation signs | Required public facilities shall have signs that designate the sex as required by 2902.2. Signs shall be readily visible and located near the entrance to each toilet facility | Required public toilet facilities | 2902.2.1 family/assisted-use rooms used as the two required facilities need not be identified for exclusive use by either sex | Conditional | Place a sex designation at each required public toilet door unless 2902.2.1 applies; accessible sign geometry remains Chapter 11 | Verified |
| 2902.4.1 | Public-toilet directional sign | Post directional signage indicating the route to required public toilet facilities in a lobby, corridor, aisle or similar space so the sign can be readily seen from the main entrance to the building or tenant space | Required public toilet facilities | None stated | Conditional | Put a restroom directional sign in the main lobby sightline from the principal entrance | Verified |

## 9. Drinking fountains and service sinks

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 2902.5 | Drinking-fountain travel | Drinking fountains need not be located in individual tenant spaces where public drinking fountains are within **150 m** of the most remote location in the tenant space and **not more than one story** above or below. In a covered or open mall that distance shall **not exceed 90 m**. Drinking fountains shall be located on an accessible route | Tenant spaces that require drinking fountains under Table 2902.1 | Table 2902.1 still decides whether a fountain is required; 2902.6 may omit fountains at small occupant load | Conditional | Place common drinking fountains on an accessible route within 150 m and one story of served tenants; use 90 m only in a confirmed mall | Verified |
| 2902.6 | Small-occupancy fountain relief | Drinking fountains shall not be required for an occupant load of **15 or fewer** | Occupant load 15 or fewer | Does not prohibit providing a fountain | Conditional | Omit required drinking fountains only for mapped spaces at that load; keep amenity/lobby loads on the Table 2902.1 check | Verified |
| 2902.7 | Mall service-sink travel | Service sinks need not be located in individual covered-mall tenant spaces where service sinks are within **91 m** of the most remote location in the tenant space and **not more than one story** above or below. Service sinks shall be located on an accessible route | Covered-mall tenant spaces | Published travel is **91 m**; do not substitute a 90 m commentary figure | Conditional | If a covered mall exists, place the janitor sink on an accessible route within 91 m and one story of the farthest tenant | Verified |

## 10. Fixture installation and privacy

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 2903.1 | Fixture level and alignment | Fixtures shall be set level and in proper alignment with reference to adjacent walls | All plumbing fixtures | None stated | Direct | Specify level-set fixtures on unit and amenity toilet details; do not follow out-of-plumb walls | Verified |
| 2903.1.1 | Fixture clearances and compartments | Water closet, urinal, lavatory or bidet: center **not closer than 375 mm** to any side wall, partition, vanity or other obstruction; adjacent unseparated fixtures **not closer than 750 mm** center to center; clearance in front **not less than 525 mm** to any wall, fixture or door. Water-closet compartments **not less than 750 mm** wide and **1500 mm** deep (floor-mounted) or **750 mm** wide and **1400 mm** deep (wall-hung) | Those fixture types in unit or common toilets | Accessible children’s water-closet centerline exception is not applied to this occupancy. Accessible fixture geometry is outbound to Chapter 11 / ICC A117.1 and is not supplied here | Direct | Dimension unit baths and amenity toilets to these minima on the fixture layout; increase clearances where Chapter 11 governs the accessible fixture | Verified |
| 2903.1.2 | Public lavatory in same room | In employee and public toilet rooms, the required lavatory shall be located in the same room as the required water closet | Employee and public toilet rooms | Does not apply to dwelling-unit baths under 2902.2 Exception 1 | Conditional | Keep the amenity/employee lavatory in the toilet room with the water closet; do not put handwash behind a second door | Verified |
| 2903.1.3 | Fixture clearance at egress openings | Piping, fixtures or equipment shall not interfere with the normal operation of windows, doors or other means of egress openings | Fixtures or piping near those openings | None stated | Direct | Overlay fixture and pipe locations on door swings and egress openings in every toilet room | Verified |
| 2903.1.4 | Public water-closet compartments | Each water closet utilized by the public or employees shall occupy a separate compartment with walls or partitions and a door enclosing the fixture | Public or employee water closets | Exception 1: compartments are not required in a single-occupant toilet room with a lockable door. Child day-care and Group I-3 exceptions are not typical for this occupancy | Conditional | Provide full compartments in amenity gang toilets; a lockable single-occupant amenity room satisfies Exception 1 without a stall | Verified |
| 2903.1.5 | Urinal privacy partitions | Each urinal utilized by the public or employees shall occupy a separate area with walls or partitions. Horizontal dimension between walls or partitions at each urinal **not less than 750 mm**. Partitions begin at a height **not greater than 300 mm** from and extend **not less than 1500 mm** above the finished floor, and extend from the wall at each side **not less than 450 mm** or **not less than 150 mm** beyond the outermost front lip measured from the finished back wall, whichever is greater | Public or employee urinals | Exception 1: partitions are not required in a single-occupant or family/assisted-use toilet room with a lockable door. Child day-care Exception 2 is not typical for this occupancy | Conditional | If amenity urinals are provided, draw the partition envelope to these limits; skip partitions only in a lockable single-occupant or family room | Verified |

## 11. Project-use controls

1. Use **Verified** rows for initial coordination after the row trigger and branch are confirmed.
2. Treat every **Verify source** row as a hold point. Table 2902.1 ratios in this matrix are not design-release values.
3. Do not reconstruct apartment, hotel, mercantile or assembly fixture ratios from the flattened OCR string, commentary Sample Problems 1–4, IBC memory or the chapter summary.
4. Do not import SBC 701 fixture quality, urinal substitution percentages, bottled-water substitution, Section 1210 finishes, or Chapter 11 / ICC A117.1 millimetres into drawings from this matrix.
5. Keep the published **91 m** service-sink token in 2902.7; do not replace it with commentary **90 m**.
6. Separate in-unit baths (2902.2 Exception 1) from common/public/employee toilets before applying travel, signage, compartment and urinal-partition checks.
7. Record the locked fixture schedule, actual-use map and published Table 2902.1 row selections in the project Golden Thread. This matrix is not evidence of SCD NOC, SBPS approval or stamped plumbing compliance.

## 12. Coverage summary

Internal inventory of the attached Chapter 29 extract (numbered code, exceptions, tables, footnotes; commentary excluded). Row-level records are not published.

- **Inventory scope:** numbered code, exceptions, tables, footnotes (commentary excluded)
- **Total independently checkable numeric records:** 59
- **Verified:** 37
- **Verify source:** 22

### Counts by top-level section

| Top-level section | Records |
|---|---:|
| 2901 | 0 |
| 2902 | 22 |
| 2903 | 15 |

### Appended-table coverage

| Appended table | Records | Verify source records |
|---|---:|---:|
| Table 2902.1 | 22 | 22 |

Coverage cross-check against `SBC 201 Chapter 29 Plumbing Systems (2024)_CS.md` was topics-only: actual-use Table 2902.1 charging; 50/50 and all-gender calculation; separate-sex exceptions; public/employee toilets and travel; drinking fountains; fixture clearances. No CS.md value was copied into a matrix cell. Commentary-only quantities (Sample Problems 1–4 fixture maths, commentary 90 m service-sink figure, SBC 701 §421.4.2 **450 mm** shower entry, accessible urinal **900 mm**) were not inventoried as code records.

## 13. Unresolved-source register

Hold points for the 22 **Verify source** inventory records. Counts are record counts, not distinct numeric values. No value in this register is a design-release figure.

| Affected table / clause | Why unverified | Control note |
|---|---|---|
| Table 2902.1 | 22 flattened records: unreadable classification blocks on pages 1891–1892 plus concatenated ratio tokens on the continuation page (`TABLE 29.21` / `TABLE 29.01.1`, `Apartment houses1 per 101 per 101 per 8`). Footnotes are not independently readable | Verify the published table before any fixture count. Do not adopt apartment, hotel, mercantile or assembly ratios from the OCR string, commentary samples or memory |
