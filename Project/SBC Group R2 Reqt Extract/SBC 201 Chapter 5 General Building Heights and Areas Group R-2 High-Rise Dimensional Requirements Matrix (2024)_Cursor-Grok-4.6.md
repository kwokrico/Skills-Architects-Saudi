# SBC 201 Chapter 5 General Building Heights and Areas — Group R-2 High-Rise Dimensional Requirements Matrix (2024)

## 1. Document metadata and use limitation

- **Project basis:** Riyadh, Saudi Arabia; Group R-2 residential high-rise; an occupied floor is stated to be more than 23 m above the relevant reference level.
- **Deliverable tier:** Project-use matrices in Sections 4–16 (design-check rows, not pasted inventory), plus a coverage summary and unresolved-source register. The full row inventory is not published.
- **Code/source basis:** SBC 201 (2024), Chapter 5, source file `Reference\SBC 201 2024\source_reference\Chapter_05 — GENERAL BUILDING HEIGHTS AND AREAS.txt`.
- **Extraction audit:** Skill extract. Project-use rows follow the chapter-extract row contract (noun-phrase checks, bold SI values, building-language triggers, named exceptions, check-specific actions). Internal inventory: **1425** independently checkable numeric records (**150** Verified, **1275** Verify source). Unresolved OCR is listed in the register and is not a design-release value.
- **Model:** Cursor Grok 4.6.
- **Prepared:** 2026-08-27.
- **Status:** Source-only architectural advisory matrix for design coordination. It is not a stamped compliance statement, height/area calculation package, SCD NOC, SBPS approval, legal opinion, or permission to construct.
- **Outbound-source rule:** No value in this matrix has been imported from Chapter 4, Chapter 6 / Table 601, Section 403, Section 406 / Table 406.5.4, Section 420, Section 706, Section 707 / Table 707.3.10, Section 716, Section 903, Section 907, Section 1511, SBC 401, SBC 501, SBC 801, SBC 901, NFPA 13/13R/13D manuals, commentary examples, or the existing chapter summary. Where Chapter 5 sends the user elsewhere, this matrix records the dependency without supplying the outbound value.

### Scope and assumptions

1. Group R-2 and high-rise status are project statements, not independently verified classifications. Chapter 5 does not restate the high-rise definition; Section 403 remains outbound.
2. The exact Riyadh AHJ/permit pathway, project stage, fire-strategy status and SCD NOC status are unconfirmed; therefore this matrix does not conclude compliance.
3. Type of construction is unconfirmed. Tables 504.3, 504.4 and 506.2 are concatenated OCR; type-specific metre, story and area cells are **Verify source** except the uniform Group R **S13R / S13D 18 m** strings.
4. Automatic sprinkler protection is not selected. **NFPA 13 / Section 903.3.1.1** (table tags NS / S / S1 / SM) and **NFPA 13R / Section 903.3.1.2** (S13R) are shown as separate branches. Note h to Tables 504.3 / 504.4 / 506.2 states new Group R occupancies shall be sprinklered per 903.2.8; NS cells are for SBC 901 existing-building evaluation.
5. Storey count, grade plane, fire walls, podium 510.2, mixed B/M/S-2/A, occupied roof, mezzanines and live/work units are unconfirmed.
6. Section 507 unlimited-area paths (F/S warehouses, malls, hangars, Group E, A-3 halls) are omitted from lead tables. Live/work (508.5) is omitted unless that program is opened in the gap register.
7. Table 504.4 is page-split after the A-1 start; **no R-2 story cells are present** in the extract.

## 2. Legends

### Applicability

| Status | Meaning |
|---|---|
| **Direct** | Expected to govern the stated R-2 tower basis, subject to confirmed geometry and design data. |
| **Conditional** | Governs only when the stated feature, construction type, sprinkler branch, mixed-use/podium condition or exception exists. |
| **Not typical** | Unrelated occupancy-only or low-rise-only rule; omitted from this deliverable unless the gap register already opened that use. |
| **External verification** | Chapter 5 points to another section/code/standard, or OCR/AHJ must be confirmed first. |

### Source confidence

| Status | Meaning |
|---|---|
| **Verified** | Requirement and any stated numeric value were checked against unambiguous mandatory Chapter 5 source text or an unambiguous table cell. |
| **Verify source** | OCR, flattened table, page-split, or footnote attachment is unresolved. Not a design-release value. |

## 3. Project decision and gap register

| Decision / gap | Current project basis | Why it controls Chapter 5 application | Required project action |
|---|---|---|---|
| Construction type | Unconfirmed; high-rise R-2 often Type I, not verified here | Tables 504.3 / 504.4 / 506.2 and 510 specials are type-specific; type-to-cell mapping is OCR-unresolved | Freeze type of construction on the code data sheet; read published tables before locking height, stories or area |
| Sprinkler basis | Unconfirmed: neither NFPA 13 nor 13R is assumed | Selects S vs S13R rows; S13R height in this extract is **18 m** for every construction type — below the stated occupied floor **> 23 m** | Fire engineer to lock 903.3.1.1 vs 903.3.1.2; do not use the S13R height row for a >23 m occupied floor without a published-table check |
| Storeys and grade plane | Occupied floor stated above 23 m; exact height, grade plane and storey count unconfirmed | Independent tests in 503.1; Table 504.4 R-2 cells are missing; Eq. 5-2 applies above three stories | Issue a signed datum sheet with grade plane, roof height, basements, mezzanines and storey count |
| Fire walls vs one building | Unconfirmed | 503.1 treats each 706 fire-wall portion as a separate building for height, stories, area and type | Show fire walls on the life-safety plan if the massing exceeds one tabular building; do not import 706 ratings here |
| Podium / 510.2 | Unconfirmed mixed parking/retail below | 3-hour Type IA plate can split area/stories/type; overall metres still from grade plane; Item 7 unit token is OCR | Freeze whether 510.2 is used; detail the 3-hour assembly, Type IA below, and shaft ratings |
| Mixed B / M / S-2 / A | Unconfirmed podium and amenity program | 508.3 uses the most restrictive height/area; 508.4 uses Table 508.4 hours (flattened) and area ratios ≤ **1** | Classify every room; choose accessory / nonseparated / separated / 510 and show it on the code sheet |
| Occupied roof | Unconfirmed | 503.1.4 occupancy vs story-below; enclosure **1200 mm**; penthouses outbound to 1511 | State occupied-roof uses and enclosure heights; do not count complying occupied roofs as area or a story |
| Mezzanines | Unconfirmed | **2.1 m** clear; aggregate **one-third** (dwelling-unit **one-half** branch) | Identify every mezzanine vs story; keep loft units on the 505.2.1 Exception 3 path if used |
| Live/work units | Not opened | 508.5 would classify the unit as R-2 with **280 m² / 50% / five** workers | Omit 508.5 from lead tables unless a live/work program is added |
| NOC and fire strategy | SCD NOC and stamped fire-strategy status unconfirmed | High-rise 403, sprinklers 903 and fire-wall 706 cannot be concluded from Chapter 5 alone | Engage the qualified local/fire consultant before design freeze |

## 4. Scope and independent limits

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 501.1 | Chapter height/area scope | This chapter controls the height and area of structures hereafter erected and additions to existing structures | New buildings and additions | None stated | Direct | Evaluate the entire enlarged building against Chapter 5 when an addition is not fire-wall separated | Verified |
| 503.1 | Independent height, stories and area | Building height, number of stories and building area shall not exceed Sections 504 and 506 based on Section 602 type and Section 302 occupancy, except as modified in Chapter 4 and this chapter. Apply the three tests independently | Every building and fire-wall portion | Chapter 4 and this chapter modifications, including 507 and 510 | Direct | Record type, occupancy, sprinkler tag, height, stories and area as three separate code-sheet lines | Verified |
| 503.1 | Fire-wall separate buildings | Each portion separated by one or more fire walls complying with Section 706 is a separate building for area, height, stories and type of construction | Structure divided by fire walls | 706 construction is outbound; do not import ratings | Conditional | Stop fire-wall height/area takeoff at each 706 line; verify 706 separately | External verification |
| 503.1.2 | Buildings on the same lot | Two or more buildings on the same lot are separate buildings, or may be treated as portions of one building where each building’s height and stories and the aggregate area are within Sections 504 and 506 | More than one building on the lot | Treating them as one building applies the aggregate-building provisions to each | Conditional | Either assume an imaginary lot line (705.3 outbound) or prove the aggregate still fits 504/506 | Verified |
| 503.1.3 | Type I unlimited tabular buildings | Type I buildings permitted unlimited tabular height and area are not required to use 507, 503.1.1, 504.3 unlimited-height options, or other-type increases | Type I with unlimited Table 504/506 cells | This is not a release from high-rise 403.3 sprinklers | Conditional | If Type I unlimited cells are confirmed from the published tables, do not add 507 yard conditions as a substitute | External verification |

## 5. Address identification

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 502.1 | Address character size | Approved address identification, legible and visible from the street or road fronting the property; characters contrast with the background; Arabic numbers or letters, not spelled-out numbers; each character **minimum 100 mm** high with **minimum 12.5 mm** stroke width; maintain the identification | New and existing buildings | Fire code official may require additional locations; private-road sites use a monument, pole or other approved means where the address cannot be viewed from the public way | Direct | Place contrasting 100 mm / 12.5 mm address characters on the street elevation and any fire-official extra locations | Verified |

## 6. Occupied roofs

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 503.1.4 | Occupied-roof occupancy | A roof level or portion may be an occupied roof if that occupancy is permitted by Table 504.4 for the story immediately below. Occupied-roof area is **not** building area under 506. An occupied roof is **not** included in building height or number of stories under 504 where penthouses and other enclosed rooftop structures comply with Section 1511 | Occupied roof proposed | Exception 1: occupancy on the roof is not limited to the story below where the building is sprinklered throughout per 903.3.1.1 or 903.3.1.2 **and** occupant notification per 907.5.2.1 and 907.5.2.3 is provided on the occupied roof; EVACS per 907.5.2.2 is also required on that roof where such a system is required elsewhere in the building. Exception 2: assembly on roofs of Type I or II open parking per the exception to 903.2.1.6 | Conditional | Classify the roof use; keep penthouses on 1511; do not add complying occupied-roof area to Table 506.2 takeoff | Verified |
| 503.1.4.1 | Occupied-roof enclosure height | Elements or structures enclosing the occupied roof shall **not extend more than 1200 mm** above the occupied-roof surface | Enclosures around an occupied roof | Exception: penthouses per 1511.2 and towers, domes, spires and cupolas per 1511.5. Mechanical screens and bulkheads are not in that exception | Conditional | Limit guard walls, windscreens and similar enclosures to 1200 mm unless a listed 1511 penthouse/tower path is used | Verified |

## 7. Height in metres

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 504.1 | Height attributes | Height in metres and number of stories are determined from type of construction, occupancy and whether an automatic sprinkler system is installed throughout | Every building | Exception: one-story aircraft hangars / paint hangars / aircraft manufacturing with Chapter 9 suppression and yards/public ways **not less than one and one-half times** the building height — not a conventional R-2 path | Direct | Lock occupancy, type and sprinkler tag before reading Table 504.3 | Verified |
| 504.2 | Mixed-occupancy height | In a mixed-occupancy building per 508, no individual occupancy shall exceed this section’s height and story limits for that occupancy | Mixed occupancy | Actual building height depends on 508.3 vs 508.4 | Conditional | Check each occupancy against 504; do not let a more restrictive podium occupancy sit above its own story cap | Verified |
| 504.3 | Tabular height in metres | Maximum building height in metres shall not exceed Table 504.3 | All buildings | Rooftop exception below. Table cells are concatenated; construction-type headers are garbled | Direct | Use Table 504.3 only after the published grid is verified; do not reconstruct type columns from memory | Verify source |
| 504.3 Exception | Combustible rooftop structures | Towers, spires, steeples and other rooftop structures shall match the building’s required type except where 1511.2.4 permits otherwise; not for habitation or storage. Noncombustible such structures are unlimited in height; combustible such structures shall **not extend more than 6 m** above the allowable building height | Rooftop towers/spires/steeples | Habitation or storage makes the structure a story | Conditional | Keep combustible architectural rooftop elements within 6 m of the Table 504.3 cap; send penthouse geometry to 1511 | Verified |
| Table 504.3 | Group R S13R/S13D height | Group R **S13R** and **S13D** rows in the extract are twelve consecutive **18** values, so **18 m** above grade plane for every listed construction type on those sprinkler tags | Group R with 903.3.1.2 (S13R) or 903.3.1.3 (S13D) throughout | S13D is not the typical R-2 high-rise system. NS and S (903.3.1.1) type-specific metre cells remain unmapped | Direct | Do not place an occupied floor above **23 m** on the S13R **18 m** row. Confirm S (NFPA 13) type-specific metres from the published table | Verified |
| Table 504.3 note h | New Group R sprinklers | New Group R occupancies shall be protected by an automatic sprinkler system in accordance with Section 903.2.8 | New Group R | NS values are only for existing-building height evaluation per SBC 901 (note d) | Direct | Design new R-2 on an S or S13R row, not NS; verify 903.2.8 separately | Verified |

## 8. Number of stories

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 504.4 | Tabular stories | Maximum number of stories above grade plane shall not exceed Table 504.4 | All buildings | Table starts at A-1 then page-splits; **no R-2 story cells are in the extract** | Direct | Hold storey count until the published Table 504.4 Group R row is read; do not invent R-2 story limits | Verify source |
| Table 504.4 note h | New Group R sprinklers | New Group R occupancies shall be protected by an automatic sprinkler system in accordance with Section 903.2.8 | New Group R | NS for existing buildings per SBC 901 (note d) | Direct | Same sprinkler lock as Table 504.3 note h; do not reuse an NS story cell for new R-2 | Verified |

## 9. Mezzanines and equipment platforms

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 505.2 | Mezzanine story/area treatment | A complying mezzanine is a portion of the story below; it does **not** contribute to building area or number of stories under 503.1. Include mezzanine area in the fire area. Clear height above and below the mezzanine floor **not less than 2.1 m** | Mezzanine proposed | Means of egress follows Chapter 10 (outbound) | Conditional | Keep 2.1 m clear both sides; do not add a complying mezzanine to Table 506.2 area or Table 504.4 stories | Verified |
| 505.2.1 | Mezzanine aggregate area | Aggregate mezzanine area within a room **not greater than one-third** of that room’s floor area. Enclosed portions of the room are excluded from the room area. Mezzanine area is not included in the room area for this check | Mezzanine in a room | Exception 1: Type I/II special industrial 503.1.1 — **two-thirds** (not typical). Exception 2: Type I or II throughout with 903.3.1.1 **and** 907.5.2.2 EVACS — **one-half**. Exception 3: mezzanine in a dwelling unit in a 903.3.1.1 or 903.3.1.2 building — **one-half**, if open except bathrooms/closets, opening unobstructed except walls **not more than 1050 mm**, columns and posts, and 505.2.3 exceptions are not used | Conditional | Use one-third for amenity mezzanines unless Exception 2 is proven; use the 1050 mm dwelling-unit path only for loft units | Verified |
| 505.2.3 | Mezzanine openness | Mezzanine shall be open and unobstructed to the room except for walls **not more than 1 m** in height, columns and posts | Mezzanine | Exception 1: enclosed occupant load **not greater than 10**. Exception 2: two or more exits or access to exits. Exception 3: enclosed area **not greater than 10 percent** of the mezzanine. Exception 4: industrial control glazing. Exception 5: other than Groups H and I, **no more than two stories**, 903.3.1.1 throughout, two or more exits — not a high-rise path | Conditional | Keep common-area mezzanines open above 1 m unless a numbered exception is documented | Verified |
| 505.2.1.1–505.3.1 | Mezzanine plus equipment platform | Where a room contains both, aggregate area of mezzanines and equipment platforms **not greater than two-thirds** of the room; mezzanine still limited by 505.2.1. Equipment platforms alone **not greater than two-thirds** of the room. Platforms are not a story or building area and are not in the 903 fire area | Equipment platform, or both in one room | Platform access shall not serve building egress. Guards per 1015.2 (outbound) | Conditional | Limit plant platforms to two-thirds of the plant room; sprinkle above and below where 903.3 requires (505.3.2) | Verified |

## 10. Allowable area method

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 506.1.3 | Basement area exclusion | Basements need not be included in the total allowable floor area provided the total basement area does **not exceed** the area permitted for a one-story-above-grade-plane building | Basements present | Multiple basements are aggregated against that one-story allowable | Conditional | Compare aggregate basement area to the one-story allowable (including 506.3 frontage); count basements in the building total if they exceed it | Verified |
| 506.1.3.1 | Full-site basement | One or more basement floors covering the entire land area are permissible provided public-safety, ventilation, groundwater drainage and sewage requirements of the relevant executive regulations and environmental requirements are met | Basement proposed under the full site | Technical/architectural/structural requirements are not quantified here | Conditional | Coordinate full-site basement with those executive/environmental rules; do not treat this clause as extra Table 506.2 area | Verified |
| 506.2.1 | Single-occupancy area equations | Allowable area of each story: \(A_a=[A_t+(NS \times I_f)]\) (Equation 5-1). Total allowable area of a building **more than three stories** above grade plane: that quantity times \(S_a\) (Equation 5-2), where \(S_a=3\), or \(S_a=4\) where the building is equipped throughout per **903.3.1.2**. No individual story shall exceed Equation 5-1 | Single-occupancy building | \(A_t\) and NS come from Table 506.2 (OCR). Frontage \(I_f\) from 506.3 | Direct | Run 5-1 per story and 5-2 for the tower total; do not use \(S_a=4\) unless 13R is actually installed | Verified |
| 506.2.2 | Mixed-occupancy area ratios | Each story follows 508.3.2 or 508.4.2 as applicable. For buildings **more than three stories**, the aggregate sum of (actual story area / allowable story area) using Equation 5-3 shall **not exceed three** | Mixed occupancy, more than three stories | Exception: separated occupancies per 508.4 **and** sprinklers throughout per 903.3.1.2 — the ratio sum shall **not exceed four** | Conditional | Sum story ratios and keep the total ≤ 3 (or ≤ 4 only on a proven 13R separated mixed building) | Verified |
| Table 506.2 | Group R-2 tabular \(A_t\) | Table 506.2 supplies NS, S1, SM, S13R and S13D area factors in square metres. The R-2h block is concatenated; construction-type assignment is unresolved | R-2 area takeoff | Note h: new Group R sprinklers per 903.2.8. Note d: NS for SBC 901 existing buildings. Note i (Group U greenhouse **435 m²**) is not an R-2 factor | Direct | Do not adopt R-2 \(A_t\) cells from the flattened grid; verify the published R-2 row before area calculations | Verify source |

## 11. Frontage increase

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 506.3.1 | Frontage perimeter threshold | To qualify for a frontage area-factor increase, **not less than 25 percent** of the building perimeter shall be on a public way or open space. The open space shall be on the same lot or dedicated for public use and accessed from a street or approved fire lane | Frontage increase claimed | Fire-wall edges are perimeter, not open frontage | Direct | Measure open perimeter including fire-lane access; do not count inaccessible yards | Verified |
| 506.3.2 | Minimum open-space width | Public way or open space used for the increase shall have a **minimum distance of 6 m** measured at right angles from the building face to the closest interior lot line, the entire width of a street/alley/public way, or the exterior face of an adjacent building on the same property. The increase uses the smallest qualifying width that is **6 m or greater** and the percentage of perimeter that has at least **6 m** | Frontage increase claimed | Width is the full space between buildings on the same lot, not fire-separation distance to an imaginary line | Direct | Dimension perpendicular yards/streets on the site plan; take \(I_f\) from the smallest ≥6 m side | Verified |
| Table 506.3.3 | Frontage increase factor | \(I_f\) is taken from Table 506.3.3. Interpolation within the table is permitted | Building qualifies under 506.3.1–506.3.2 | Table is flattened (percent × open-space columns concatenated) | Direct | Verify published 506.3.3 factors before applying \(I_f\) in Equations 5-1 / 5-2 / 5-3 | Verify source |
| Table 506.3.3.1 | Near-unlimited-area frontage | Where a building meets Section 507 except the **18 m** public-way/yard width, \(I_f\) is taken from Table 506.3.3.1 | Failed 507 yard width only | Not a typical R-2 high-rise path. Table is flattened | Conditional | Do not use 506.3.3.1 unless a 507 configuration is actually proposed | Verify source |

## 12. Mixed occupancy

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 508.1 | Mixed-use options | Each portion is classified per 302.1. Where more than one occupancy group exists, comply with 508.2, 508.3, 508.4, 508.5 or a combination | More than one occupancy group | Exception 1: occupancies separated per 510. Exception 2: Table 415.6.5 detached Group H-1/H-2/H-3 | Conditional | State accessory / nonseparated / separated / 510 on the code sheet; do not mix methods silently | Verified |
| 508.2.3 | Accessory occupancy area | Building allowable area is per 506 for the **main** occupancy. Aggregate accessory occupancies shall **not occupy more than 10 percent** of the floor area of the story and shall not exceed Table 506.2 **nonsprinklered** tabular values for each accessory occupancy | Accessory occupancies ancillary to the main use | Height/stories follow 504 for the main occupancy (508.2.2). No separation required except 508.2.4 exceptions | Conditional | Keep amenity/accessory fire areas ≤ 10% of the story and ≤ the NS tabular cap for that accessory group | Verified |
| 508.2.4 Ex. 2 | Dwelling-unit accessory separation | Group I-1, R-1, R-2 and R-3 dwelling units and sleeping units shall be separated from other dwelling/sleeping units and from accessory occupancies contiguous to them per Section 420 | Accessory space contiguous to an R-2 unit | Exception 1: Group H-2 through H-5 still need 508.4 separation | Direct | Do not waive 420 unit separations because a lounge or office is “accessory” | External verification |
| 508.3.2 | Nonseparated height and area | Allowable building area, height and stories of the nonseparated portion are the **most restrictive** allowances of the occupancy groups under consideration for the building’s type, per 503.1 | Nonseparated mixed occupancy | Most restrictive Chapter 9 applies throughout the nonseparated area (508.3.1). High-rise: most restrictive 403 of those occupancies applies throughout (508.3.1.1) | Conditional | Size the nonseparated volume to the worst occupancy’s 504/506 row; apply 403/Chapter 9 on that same volume | Verified |
| 508.3.3 Ex. 2 | Nonseparated dwelling-unit separation | R-2 dwelling/sleeping units still separate from other units and contiguous occupancies per Section 420 | Nonseparated mixed building with R-2 units | Group H-2 through H-5 still need 508.4 | Direct | Keep 420 unit and occupancy separations even on the nonseparated path | External verification |
| 508.4.2 | Separated occupancy area ratios | In each story, the sum of (actual area of each separated occupancy / allowable area of that occupancy) shall **not exceed 1** | Separated mixed occupancy | Frontage increase uses the **entire building** perimeter | Conditional | Tabulate occupancy areas and allowables per story; keep the ratio sum ≤ 1 | Verified |
| 508.4.3 | Separated occupancy height | Each separated occupancy shall comply with 503.1 height and story limits for the building’s type of construction | Separated mixed occupancy | Exception: Section 510 specials | Conditional | Park each occupancy only on stories Table 504.4 allows for that group | External verification |
| Table 508.4 | Occupancy separation hours | Required fire-barrier / horizontal-assembly hours between occupancies, S vs NS columns. **S** means 903.3.1.1 throughout; **NS** includes buildings with 13R or 13D. **N** = no separation; **NP** = not permitted | Separated occupancies | Note a: Section 420. Note b: private/pleasure-vehicle areas reduced **1 hour** but **not less than 1 hour**. Note f: fire-area separations also meet 707.3.10 / Table 707.3.10. Table is flattened | Conditional | Verify published R vs B/M/S-2/A hours before rating podium separations; do not adopt concatenated 1/2/3 hour cells | Verify source |
| 508.4.4.1 | Mass-timber occupancy thermal barrier | Required occupancy separations shall be 707 fire barriers or 711 horizontal assemblies, or both. In Type IV-B or IV-C, mass-timber elements serving those separations shall have an approved thermal barrier of gypsum board **not less than 12.5 mm** thick, or a material meeting both NFPA 275 Temperature Transmission and Integrity tests, toward the interior | Type IV-B/IV-C occupancy separations | Not applicable unless mass timber is the construction type | Conditional | Specify 12.5 mm gypsum or NFPA 275 thermal barrier on the interior face of mass-timber occupancy separations | Verified |

## 13. Incidental uses

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 509.1 | Incidental-use scope | Incidental uses in Table 509.1 shall comply with this section. They are ancillary functions limited to that table | Listed incidental room or system | Exception: incidental uses **within and serving a dwelling unit** need not comply | Direct | Apply Table 509.1 to common-building plant/laundry/waste; not to in-unit laundry | Verified |
| 509.2 | Incidental occupancy class | Incidental uses are **not** individually classified per 302.1; they take the building occupancy in which they are located | Incidental use present | They do not create a mixed occupancy by themselves | Direct | Keep laundry/waste/plant rooms as R-2 for occupancy classification | Verified |
| 509.3 | Incidental area cap | Incidental uses shall **not occupy more than 10 percent** of the building area of the story in which they are located | Incidental uses on a story | None stated | Direct | Limit each story’s Table 509.1 rooms to 10% of that story | Verified |
| Table 509.1 | Furnace and boiler rooms | Furnace room where any piece of equipment is over **117 kW** per hour input: **1 hour** or an automatic sprinkler system. Rooms with any boiler over **103.5 kPa** and **7.5 kW**: **1 hour** or an automatic sprinkler system | Those equipment rooms outside dwelling units | Sprinkler need only protect the incidental room (509.4.2.1 / note a) | Conditional | Rate or sprinkle furnace/boiler rooms at those thresholds; show smoke-resisting enclosure if the sprinkler-only path is used (509.4.2) | Verified |
| Table 509.1 | Laundry and waste rooms | Laundry rooms over **9 m²**: **1 hour** or an automatic sprinkler system. Waste and linen collection rooms over **9 m²** (other than ambulatory care and Group I-2): **1 hour** or an automatic sprinkler system | Common laundry or waste rooms over 9 m² | I-2 / ambulatory rows are a different (stricter) branch. Dwelling-unit exception under 509.1 | Direct | Provide 1-hour enclosure or room sprinklers for common laundry and waste rooms larger than 9 m² | Verified |
| Table 509.1 | Hydrogen rooms in Group R | Hydrogen fuel gas rooms not classified as Group H: **1 hour** in Groups B, F, H, M, S and U; **2 hours** in Groups A, E, I and **R** | Hydrogen fuel gas room in an R occupancy | Not classified as Group H | Conditional | If a hydrogen room is provided in the R-2 building, use the 2-hour Group R rating | Verified |
| 509.4.1.1 | Mass-timber incidental thermal barrier | Where Table 509.1 requires a rated separation, mass-timber fire barriers or horizontal assemblies in Type IV-B or IV-C shall have gypsum **not less than 12.5 mm** or NFPA 275 thermal barrier toward the interior of the incidental use | Type IV-B/IV-C incidental separations | None stated | Conditional | Same thermal-barrier detail as 508.4.4.1, on the incidental-use face | Verified |

## 14. Podium and parking specials

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 510.2 | Horizontal building separation | Upper and lower volumes are separate buildings for area, fire-wall continuity, stories and type where all listed conditions are met: **3-hour** horizontal assembly (vertical offsets and their supports also **3 hours**); building below, including the assembly, is Type IA; shafts/stair/ramp/escalator enclosures through the assembly **not less than 2 hours** with 716 protectives; occupancies above limited to Group A uses each with occupant load **less than 300**, or Groups B, M, R or S; building below sprinklered throughout per **903.3.1.1** and not Group H | 510.2 podium/pedestal elected | Item 3 exception: **3-hour** enclosure below and **1-hour** above where the building above is not required to be Type I, the enclosure connects **fewer than four stories**, and opening protectives above are **not less than 1 hour**. Item 4: combustible interior exit stairs in the Type IA building only if the building above is Type III, IV or V **and** the stair in the Type IA building is in **3-hour** construction | Conditional | Detail the 3-hour Type IA plate, 2-hour shafts, occupancy list and NFPA 13 below; count upper stories from the plate | Verified |
| 510.2 Item 7 | Podium overall height unit | Maximum building height in **mm** shall not exceed Section 504.3 for the building having the smaller allowable height, measured from the grade plane | 510.2 podium | The printed unit is **mm** in the extract; do not treat it as millimetres and do not silently convert | Conditional | Verify the published unit for Item 7 before locking overall podium height from grade plane | Verify source |
| 510.4 | Parking beneath Group R | Where a maximum **one story** above grade plane Group S-2 parking garage (enclosed or open, or combination), of Type I construction or open of Type IV, with grade entrance, is provided under Group R, the number of stories used to determine minimum type is measured from the floor above that parking. The floor assembly shall comply with the parking garage’s type **and** with Table 508.4 mixed-occupancy separation | One-story S-2 parking under R | Table 504.3 height in metres is **not** increased. Table 508.4 hours are OCR | Conditional | If this path is used, start the R story count above the garage; keep the metre cap from Table 504.3 | Verified |
| 510.9 | Multiple buildings on a pedestal | Where two or more buildings sit above the horizontal assembly under 510.2, 510.3 or 510.8, those upper buildings are separate from each other and comply as distinct buildings | Multiple towers or fire-wall-split buildings on one plate | None stated | Conditional | Treat each upper building’s type, height and area independently on the 510.2 plate | Verified |

## 15. Alternate R-2 height paths

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 510.5 | Type IIIA R-2 height increase | For Type IIIA Groups R-1 and R-2, Table 504.3 height shall be increased by **3 m** and Table 504.4 stories increased by **one** where the first-floor assembly above the basement is **not less than 3 hours** and floor area is subdivided by **2-hour** fire walls into areas of **not more than 279 m²** | Type IIIA R-2 using this increase | Base Table 504.3/504.4 cells remain OCR. High-rise 403 is still outbound | Conditional | Use only on Type IIIA; show 3-hour first floor, 2-hour fire walls and 279 m² compartments | Verified |
| 510.6 | Type IIA R-2 height increase | Height limitation for Type IIA Groups R-1 and R-2 shall be increased to **nine stories** and **30 m** where the building is separated by **not less than 15 m** from any other building on the lot and from lot lines, exits are segregated in an area enclosed by a **2-hour** fire wall, and the first-floor assembly is **not less than 1½ hours** | Type IIA R-2 using this increase | A building at 30 m may be high-rise; Section 403 is outbound and not waived here | Conditional | Use only on Type IIA with 15 m yards, 2-hour exit fire walls and 1½-hour first floor; still run 403 if high-rise | Verified |

## 16. Open-parking mixed

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 510.7 | Open parking beneath Group R | Open parking garages under Groups A, I, B, M and R shall not exceed height and area permitted under Section 406.5. The portion above shall not exceed Section 503 for the upper occupancy. Height in metres **and** stories of the upper portion is measured from grade plane **and includes** the open parking garage | Open S-2 parking under R | Table 406.5.4 values are not imported | Conditional | Measure R height and stories from grade through the garage; verify 406.5 separately | External verification |
| 510.7.1 | Open-parking / R separation and egress | Fire barriers or horizontal assemblies between parking and the upper occupancy shall match Table 508.4. Type applies to each occupancy individually, except structural members including main bracing in the garage that support the upper occupancy take the more restrictive Table 601 rating. Means of egress for the upper occupancy shall be separated from parking by fire barriers or horizontal assemblies having **not less than a 2-hour** fire-resistance rating, with self-closing 716 doors | 510.7 configuration | Table 508.4 and Table 601 are outbound/OCR. Parking egress follows 406.5 | Conditional | Enclose R exits through the garage in 2-hour construction; do not import 601 or 508.4 hours from this extract | Verified |
| 510.8 | B or M under open parking | Group B or M below a lesser-type Group S-2 open parking garage are separate buildings for type where listed conditions are met, including a **not less than 2-hour** horizontal assembly, Type IA below (exception: Type IB or II, not less than the garage type, where the building below is **not greater than one story** above grade plane), and garage exits discharging at grade in **2-hour** fire barriers or horizontal assemblies | Open parking above B/M podium | Not an R-above path. 406.5 still governs the garage including the height of the building below | Conditional | Use only if retail/office sits under open parking; keep R residential on 510.2 / 510.4 / 510.7 instead | Verified |

## 17. Project-use controls

1. Use **Verified** rows for schematic height/area scoping after the row trigger and sprinkler/type branch are confirmed.
2. Treat every **Verify source** row (flattened Tables 504.3 type-specific cells, all of Table 504.4 including missing R-2 stories, Table 506.2 \(A_t\), Tables 506.3.3 / 506.3.3.1, Table 508.4 hours, 510.2 Item 7 **mm** token) as a design hold point. No affected value is to be placed in issued-for-approval documents without a published-source check.
3. Do not reconstruct Table 504.3 / 504.4 / 506.2 construction-type columns from IBC memory. The canonical failure is adopting a type-specific metre or area from a concatenated string.
4. Do not assume NFPA 13 versus 13R. The extract’s Group R S13R height is **18 m** for all types — incompatible with a stated occupied floor **> 23 m** unless the published table is shown to differ.
5. Do not import Section 403 high-rise, Section 420 unit separation, Table 601, Section 706 fire-wall, Table 406.5.4, 903, 907 or 1511 values.
6. Do not use Section 507 unlimited-area yards, hangar 1.5× height, or 508.5 live/work limits unless those programs are opened in the gap register.
7. Record construction type, sprinkler standard, grade plane, podium election and mixed-use method in the project Golden Thread. This matrix is not evidence of SCD NOC, SBPS approval, or stamped compliance.

## 18. Coverage summary

Internal inventory of the attached Chapter 5 extract (numbered code, exceptions, tables, footnotes; commentary excluded). Row-level records are not published.

- **Inventory scope:** numbered code, exceptions, tables, footnotes (commentary excluded)
- **Total independently checkable numeric records:** 1425
- **Verified:** 150
- **Verify source:** 1275

### Counts by top-level section

| Top-level section | Records |
|---|---:|
| 501 | 0 |
| 502 | 2 |
| 503 | 1 |
| 504 | 218 |
| 505 | 13 |
| 506 | 914 |
| 507 | 32 |
| 508 | 188 |
| 509 | 28 |
| 510 | 29 |

### Appended-table coverage

| Appended table | Records | Verify source records |
|---|---:|---:|
| Table 504.3 | 192 | 168 |
| Table 504.4 | 24 | 24 |
| Table 506.2 | 862 | 861 |
| Table 506.3.3 | 16 | 16 |
| Table 506.3.3.1 | 24 | 24 |
| Table 508.4 | 180 | 180 |
| Table 509.1 | 26 | 0 |

Coverage cross-check against `SBC 201 Chapter 5 General Building Heights and Areas (2024)_CS.md` was topics-only: independent H/S/A tests; occupied roofs; sprinkler-row tags; mezzanines; frontage; mixed occupancy; incidental uses; podium 510.2. No CS.md value was copied into a matrix cell. Commentary figures and worked examples (Type VB office metres/stories, motel area, accessory 1000 m² sketches) were not inventoried.

Table 504.4 remainder after the A-1 start, including every Group R story cell, is absent from the extract and is not counted as invented cells. Table 506.2 page 1 occupancy blocks after A-1 are OCR-cloned; I-1 / I-2 / I-3 / H-5 area rows are not in the continuation table.

## 19. Unresolved-source register

Hold points for the **1275** **Verify source** inventory records. Counts are record counts, not distinct numeric values. No value in this register is a design-release figure.

| Affected table / clause | Why unverified | Control note |
|---|---|---|
| Table 504.3 type-specific cells (168) | One collapsed HTML row; headers garbled (`TYPE IVTYPE VABABABABCHTAB`); NS and S (903.3.1.1) metre values cannot be assigned to IA–VB without reconstruction | Adopt only the uniform Group R S13R/S13D **18 m** strings. Verify published type columns before locking tower height |
| Table 504.4 (24 visible + remainder missing) | Table starts at A-1 NS/S then page-splits to footnotes; **no R-2 story cells** | Do not invent R-2 story limits. Read the published table before freeze |
| Table 506.2 (861) | Two concatenated pages; page 1 occupancy blocks after A-1 are cloned; R-2h block exists but columns unmapped; I-1/I-2/I-3/H-5 rows missing | Do not use flattened \(A_t\) in Equations 5-1 / 5-2 / 5-3 |
| Tables 506.3.3 and 506.3.3.1 (40) | Percent × open-space factor grids concatenated; 506.3.3.1 title OCR-labelled “SECTION 507 BUILDINGS” | Keep 25% / **6 m** from 506.3 prose; verify published \(I_f\) cells |
| Table 508.4 (180) | S/NS hour matrix flattened (`122NP`, `34232` digit runs) | Verify published R vs B/M/S-2/A hours; note b **1-hour** floor remains usable as text |
| 510.2 Item 7 | Prints height in **mm** | Do not treat as millimetres and do not convert to metres from memory |
| 507.10 yard width (1) | “18 m in width than one and one-half times the building height” is garbled | Unlimited-area hangar path omitted from lead tables; not an R-2 check |
