# SBC 201 Chapter 7 Fire and Smoke Protection Features — Group R-2 High-Rise Dimensional Requirements Matrix (2024)

## 1. Document metadata and use limitation

- **Project basis:** Riyadh, Saudi Arabia; Group R-2 residential high-rise; an occupied floor is stated to be more than 23 m above the relevant reference level.
- **Deliverable tier:** Project-use matrices in Sections 4–20 (design-check rows, not pasted inventory), plus a coverage summary and unresolved-source register. The full row inventory is not published.
- **Code/source basis:** SBC 201 (2024), Chapter 7, source file `Reference\SBC 201 2024\source_reference\Chapter_07 — FIRE AND SMOKE PROTECTION FEATURES.txt`.
- **Extraction audit:** Skill extract. Project-use rows follow the chapter-extract row contract (noun-phrase checks, bold SI values, building-language triggers, named exceptions, check-specific actions). Internal inventory: **2863** independently checkable numeric records (**517** Verified, **2346** Verify source). The Verify-source majority is the OCR-destroyed Tables 721.1(1)–(3) and 722.* cell dump; those cells are not design-release values.
- **Model:** Cursor Grok 4.6.
- **Prepared:** 2026-08-27.
- **Status:** Source-only architectural advisory matrix for design coordination. It is not a stamped compliance statement, fire-engineering report, SCD NOC, SBPS approval, legal opinion, or permission to construct.
- **Outbound-source rule:** No value in this matrix has been imported from Tables 601 / 508.4 / 509.1 / 1020.2, Sections 403 / 404 / 414 / 420 / 510 / 1023 / 1024 / 1026, Chapter 9 sprinkler design, Chapter 10 corridor ratings, Chapter 14 cladding, NFPA 82, SBC 501 plenum limits, SBC 801 ESS enclosure ratings, commentary examples, or a chapter summary. Where Chapter 7 sends the user elsewhere, this matrix records the dependency without supplying the outbound value. No Chapter 7 `*_CS.md` was found.

### Scope and assumptions

1. Group R-2 and high-rise status are project statements, not independently verified classifications.
2. The exact Riyadh AHJ/permit pathway, project stage, fire-strategy status and SCD NOC status are unconfirmed; therefore this matrix does not conclude compliance.
3. Construction type is unconfirmed. A high-rise R-2 tower is typically Type I or II, not verified. Type V framed walls are not assumed for the tower shaft.
4. Automatic sprinkler protection is not selected. **NFPA 13 / Section 903.3.1.1** and **NFPA 13R / Section 903.3.1.2** are shown as separate branches. Table 705.8 `UP, S` is **903.3.1.1 only**.
5. Fire-separation distance by elevation, fire walls versus occupancy/fire-area barriers, podium mix, adjoining S-2 parking, storey count and shaft program are unconfirmed.
6. Tables 716.1(2) (flattened remainder), 716.1(3) (`>ch1` / exterior `1/2` token), Figure 705.7 *F*_eo, and all appended Tables 721.1(1)–(3) and 722.* are OCR-unresolved. Affected rows are **Verify source**.
7. Exterior-wall weather envelope and combustible cladding remain in Chapter 14. Structural FRR by construction type remains in Table 601. High-rise SFRM bond strength and the 403.2.1.2 shaft-hour reduction remain in Section 403.

## 2. Legends

### Applicability

| Status | Meaning |
|---|---|
| **Direct** | Expected to govern the stated R-2 tower basis, subject to confirmed geometry and design data. |
| **Conditional** | Governs only when the stated feature, construction type, sprinkler branch, FSD, mixed-use or exception exists. |
| **Not typical** | Unrelated occupancy-only or low-rise-only rule; omitted from this deliverable unless the gap register already opened that use. |
| **External verification** | Chapter 7 points to another section/code/standard, or the project/AHJ basis must be confirmed before use. |

### Source confidence

| Status | Meaning |
|---|---|
| **Verified** | Requirement and any stated numeric value were checked against unambiguous mandatory Chapter 7 source text or an unambiguous table cell. |
| **Verify source** | OCR, flattened table, page-split, missing figure, or footnote attachment is unresolved. Not a design-release value. |

## 3. Project decision and gap register

| Decision / gap | Current project basis | Why it controls Chapter 7 application | Required project action |
|---|---|---|---|
| Construction type | Unconfirmed; high-rise R-2 typically Type I or II, not verified | Table 705.5 Type I vs IIB/VB bands; 704 encasement; 708.3 / 711.2.4.3 half-hour unit-separation exception is Type IIB/IIIB/VB only; 718 combustible fireblocking is Type III–V | Freeze type of construction on the code data sheet before wall, shaft and SFRM schedules |
| Sprinkler basis | Unconfirmed: neither NFPA 13 nor 13R is assumed | Table 705.8 `UP, S` is **903.3.1.1 only**; 705.8.5 vertical opening skip allows 13 **or** 13R; 708.3 Exc 2 / 711.2.4.3 Exc are **903.3.1.1 only**; 717.5.3 Exc 2 smoke-damper skip is **903.3.1.1** | Fire engineer to lock Chapter 9 system; do not treat 13R as the Table 705.8 sprinklered opening branch |
| Fire-separation distance | Unconfirmed by elevation | Tables 705.2 / 705.5 / 705.8; 705.5 both-sides rating at FSD **≤ 3 m**; 705.2.3 projection protection within **1500 mm** | Dimension FSD on each elevation to the lot line or assumed lot line, not to the balcony edge |
| Storeys and height | Occupied floor stated above 23 m; exact storey count unconfirmed | Shafts connecting **4 or more** stories are **2 h** (713.4); 705.8.5 Exc 1 is **≤ 3** stories; 708.4.2 Exc 4 R-2 draftstop reduction is **≤ 4** stories and **≤ 18 m** | Issue a signed code datum sheet with storey count including basements, excluding mezzanines |
| Fire walls vs barriers | Unconfirmed whether a fire wall, occupancy separation or fire-area barrier is used | Table 706.4 R-2 fire wall **3 h** (2 h in Type II/V); Table 707.3.10 R fire area **2 h**; Table 508.4 mixed-occupancy hours not imported | Freeze the separation strategy on the life-safety plans; do not treat a fire barrier as a fire wall |
| Podium / mixed use / S-2 garage | Unconfirmed | 705.3 Exc 2 adjoining S-2/R-2 openings; 707.3.9 mixed occupancy; incidental uses Table 509.1 | Classify podium, parking and amenity occupancies; tag shared walls with all served groups |
| High-rise Section 403 | Unconfirmed beyond the 23 m project statement | Commentary (not code) cites 403.2.1.2 shaft-hour reduction and 403.2.3 SFRM bond; neither value is in Chapter 7 | Fire engineer to apply Section 403 separately; do not adopt 1-hour shaft reductions from commentary |
| Corridor rating | Unconfirmed | 708.1 / 708.3 send corridor walls to Table 1020.2; ½-hour corridor option is outbound | Use the Chapter 10 matrix for corridor hours; keep 708 construction rules here |
| Incidental uses | Unconfirmed (trash, linen, parking attendant, etc.) | 707.3.7 / 713.13.5 send hours to Table 509.1 | Schedule incidental rooms; do not import 509.1 hours into this matrix |
| NOC and fire strategy | SCD NOC and stamped fire-strategy status unconfirmed | Shaft pressurization, smoke control, damper exceptions and SCD acceptance cannot be concluded from Chapter 7 alone | Engage the qualified local/fire consultant before design freeze |

## 4. Fire tests, identification and multiple-use assemblies

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 702.1 | Multiple-use fire assemblies | An assembly serving more than one fire purpose shall comply with **all** applicable requirements for each purpose | Wall, floor, door or damper serving two or more listed roles | None stated | Direct | Tag corridor/shaft/lobby walls with every applicable 707/708/709/716/717 rule | Verified |
| 703.2 | Fire-resistance without sprinklers | FRR of elements, components or assemblies is determined by 703.2.1 or 703.2.2 **without** automatic sprinklers or other suppression in the test, or by 703.2.3 | Required fire-resistance rating | Alternative method under 104.11 | Direct | Specify tested/analytical listings; do not take credit for building sprinklers in the E119/UL 263 rating | Verified |
| 703.2.1.1 | Nonsymmetrical interior walls | Test both faces; assigned rating is the **shortest** duration | Interior walls and partitions of nonsymmetrical construction | One-face test only if evidence shows the least-resistant face was exposed (building official acceptance); exterior walls follow 705.5 | Direct | Use symmetrical shaft/corridor assemblies or document the weaker-face listing | Verified |
| 703.3.1 Exc | Composite noncombustible surfacing | Structural base noncombustible (ASTM E136 or E2652 with E136 criteria) plus surfacing **not more than 3.18 mm** with flame-spread index **not greater than 50** (ASTM E84 or UL 723) | Materials required to be noncombustible | None stated | Direct | Keep thin finishes on noncombustible substrates within the thickness and FSI limits | Verified |
| 703.5 | Rated-wall marking in concealed space | Permanent signs or stenciling within **4.5 m** of each wall end and at intervals **not exceeding 9 m**; lettering **not less than 75 mm** high with **minimum 10 mm** stroke | Accessible concealed floor, floor-ceiling or attic at fire walls, fire barriers, fire partitions, smoke barriers, smoke partitions or other walls requiring protected openings | None stated | Direct | Show barrier identification on reflected-ceiling and attic plans | Verified |
| 703.6 | Mass-timber protection time | Contribution minutes = Test Assembly 2 time minus unprotected Test Assembly 1 time, same ASTM E119 / UL 263 structural-failure criteria | Types IV-A / IV-B / IV-C noncombustible protection | Table 722.7.1(1) deemed-to-comply times are **Verify source** | Conditional | Do not use Type IV unless mass timber is specified; verify published 722.7 tables before assigning minutes | Verified |

## 5. Structural member protection and SFRM

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 704.1 | Structural FRR floor | Member FRR not less than the rated assemblies it supports, and not less than Table 601 | Columns, beams and other required-rated members | Fire barriers, fire partitions, smoke barriers and horizontal assemblies as provided in 707.5, 708.4, 709.4 and 711.2 | External verification | Take hours from Table 601 and from the supported assembly; do not import Table 601 here | Verified |
| 704.2 | Column individual encasement | Protect the entire column on all sides for the full height, including connections, through the ceiling space to the top of the column | Columns required to have protection to achieve an FRR | Light-frame integral studs/columns per 704.4.1 | Direct | Continue SFRM or board encasement through the ceiling plenum; do not stop at the ceiling membrane | Verified |
| 704.3 | Primary-frame individual encasement | Individual encasement on all sides for the full length, including connections | Primary frame other than columns that supports **more than two floors**, or **one floor and a roof**, or a load-bearing wall, or a nonload-bearing wall **more than two stories** high | Exposed-sides-only where the tested extent satisfies 703 | Direct | Encase transfer girders and multi-storey primary beams individually, not by floor membrane alone | Verified |
| 704.6–704.6.1 | Attachment remaining cover | Lug/bracket/rivet/bolt edges may extend to within **25 mm** of the fire-protection surface; secondary steel attachments receive the same material and thickness for **not less than 300 mm**, or the full length if shorter than **300 mm**; hollow open-end attachments protected inside and out | Primary or secondary structural steel requiring fire protection | None stated | Direct | Extend SFRM onto hangers, braces and erection lugs; close open hollow stubs | Verified |
| 704.7 | Reinforcement cover measurement | Protection thickness measured to the outside of reinforcement; stirrups and spiral ties may project **not more than 12.5 mm** into the protection | Concrete or masonry members with required cover | None stated | Direct | Check cover to main bars, not to stirrup outer face | Verified |
| 704.9 | Impact protection height | Corner guards or a substantial noncombustible jacket to a height adequate for full protection, **not less than 1.5 m** above the finished floor | Fire-protective covering subject to vehicle, merchandise or other impact | Concrete columns in parking garages | Conditional | Protect SFRM columns in the podium garage and loading bay to at least **1.5 m** | Verified |
| 704.10 | Exterior load-bearing member FRR | Highest of Table 601 for the element, Table 601 for exterior bearing walls, and Table 705.5 based on FSD | Load-bearing members in exterior walls or outside the building | None stated | External verification | Coordinate column FRR with FSD and construction type; do not import Table 601 hours | Verified |
| 704.11 | Unprotected lintel bottom flange | Fire protection not required at the bottom flange of lintels, shelf angles and plates spanning **not more than 2 m** (primary frame or not), and at bottom flanges not part of the structural frame regardless of span | Lintels, shelf angles and plates | None stated | Conditional | Leave short masonry lintel soffits unprotected only within the **2 m** primary-frame limit | Verified |
| 704.13.3.2 | SFRM over unlisted primer | Field ASTM E736: **not fewer than five** bond tests; average bond **not less than 80%** and individual **not less than 50%** of SFRM on clean uncoated **3.2 mm** plate; beam flange **≤ 300 mm**, column flange **≤ 400 mm**, web depth **≤ 400 mm** | SFRM over primers, paints or encapsulants other than those in the listing | Do not use this path outside the size limits | Conditional | Prefer listed primers; if painted steel is unavoidable, run the five-test E736 protocol before spraying | Verified |
| 704.13.4 | SFRM application temperature | Ambient and substrate **not less than 4.5°C** during application and for **not fewer than 24 hours** after | SFRM application | Manufacturer's instructions may allow otherwise | Direct | Hold winter/night pours and spray until the **4.5°C / 24 h** condition is met | Verified |
| 704.13 / 403.2.3 | High-rise SFRM bond | Chapter 7 requires listing-consistent thickness, density and substrate; **bond-strength values are in Section 403.2.3**, not here | High-rise steel frame with SFRM | None stated in Chapter 7 | External verification | Specify 1705.14 special inspection and Section 403 bond; do not invent kPa values | Verified |

## 6. Exterior walls — projections, FSD ratings and openings

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| Table 705.2 | Projection setback from FSD line | FSD **0 to < 600 mm**: projections **not permitted**; **600 to < 900 mm**: **≥ 600 mm**; **900 to < 1500 mm**: **≥ two-thirds of FSD**; **≥ 1500 mm**: **≥ 1000 mm** | Cornices, eaves, balconies and similar projections | 705.3 same-lot buildings treated as one building | Direct | Measure FSD to the wall, then check balcony/eave edge against Table 705.2 | Verified |
| 705.2.3 | Projection protection near lot line | Projections within **1500 mm** of the FSD line shall be noncombustible, **≥ 1-hour** combustible, heavy timber 2304.11, FRTW, or 705.2.3.1 | Projections extending toward the FSD line | Type VB Group R-3/U with FSD **≥ 1.5 m** (not this tower) | Conditional | Fire-rate or make noncombustible any balcony/eave that enters the **1500 mm** zone | Verified |
| 705.2.3.1 | Combustible balcony length | Aggregate length **not more than 50 percent** of the building perimeter on each floor; combustible construction other than FRTW shall match Table 601 floor FRR or be heavy timber | Combustible balconies and similar projections | Exc 4: sprinklers extended to the balcony → length not limited. Exc 2: untreated wood/plastic-composite pickets **≤ 1050 mm**. Exc 1: FRTW on Types I/II **≤ 3** stories (not this tower) | Conditional | Either sprinkler every balcony or keep combustible balcony length ≤ **50%** of that floor perimeter | Verified |
| 705.3 Exc 2 | Adjoining S-2 / R-2 openings | Where an S-2 parking garage of Type I or IIA has **no** FSD to a Group R-2 building, occupant-use openings are permitted per 706.8; opening protectives **not less than 1½ hour** are required **only in the S-2 wall**, not in the R-2 wall | S-2 garage erected on the same lot as Group R-2 with zero FSD | Protectives only on the garage side | Conditional | If podium parking shares a wall with the tower, rate the garage openings **1½ h** and keep the residential openings unprotected on that interface | Verified |
| 705.5 | Exterior-wall fire exposure | Walls with FSD **≤ 3 m** rated from **both sides**; FSD **> 3 m** rated from the **inside only** | Exterior walls required to have an FRR | None stated | Direct | Use two-sided listings on close lot-line walls; interior-only listings only where FSD exceeds **3 m** | Verified |
| Table 705.5 | Group R exterior-wall FRR | Group R column: FSD **< 1.5 m** all types **1 h**; **1.5 ≤ FSD < 3 m** **1 h**; **3 ≤ FSD < 9 m** Type IA/IB/IVA/IVB **1 h** (note c), Type IIB/VB **0 h**, other types **1 h**; FSD **≥ 9 m** all types **0 h**. Load-bearing walls also comply with Table 601 (not imported). Note g: **0 h** where Table 705.8 permits unlimited unprotected openings on nonbearing walls | Exterior walls, FSD measured to the story | Notes b, c, g, h, i; Group H / F-1 / M / S-1 columns omitted from this row | Direct | For a Type I tower, schedule **1 h** exterior walls where FSD **< 9 m**, then overlay Table 601 if the wall is load-bearing | Verified |
| Table 705.8 | Exterior opening area per story | Percentage of exterior-wall area per story. **UP, NS** / **UP, S (903.3.1.1 only)** / **Protected**: FSD **0–<0.9 m** Not Permitted / Not Permitted / Not Permitted; **0.9–<1.5 m** NP / **15%** / **15%**; **1.5–<3 m** **10%** / **25%** / **25%**; **3–<4.5 m** **15%** / **45%** / **45%**; **4.5–<6 m** **25%** / **75%** / **75%**; **6–<7.5 m** **45%** / No Limit / No Limit; **7.5–<9 m** **70%** / No Limit / No Limit; **≥ 9 m** No Limit all degrees | Exterior wall openings, each story | Note k → 705.3 Exc 2 for S-2/R-2. Notes d/f are Group R-3 only. Note g: open parking FSD **≥ 3 m** unlimited. **Do not treat 13R as UP, S** | Direct | Calculate opening % by FSD and story; until NFPA 13 is locked, use the **UP, NS** column as the conservative branch | Verified |
| 705.8.1 Exc 1 | First-story unlimited unprotected | Street-facing first story with FSD **> 4.5 m** to street centreline, or facing **≥ 9 m** unoccupied space with fire-lane access | First story above grade plane; other than Group H | Does not unlock upper-storey openings | Conditional | Apply only to the ground-storey street elevation | Verified |
| 705.8.4 | Mixed protected and unprotected openings | \((A_p/a_p)+(A_u/a_u) \leq 1\) (Equation 7-2) | Both opening types in the same story exterior wall | \(A_e\) from 705.7 may replace \(A_p\) | Direct | Do not add protected and unprotected percentages independently | Verified |
| Figure 705.7 | Equivalent opening factor \(F_{eo}\) | Figure lookup required for Equation 7-1; **no numeric table in the extract** | Protected openings where unexposed-temperature criterion is waived | Do not guess \(F_{eo}\) | External verification | Verify the published figure before using equivalent protected area | Verify source |
| 705.8.5 | Adjacent-story opening separation | Where openings in adjacent stories are within **1.5 m** horizontally and the lower opening is not a **≥ ¾-hour** protective: provide **≥ 900 mm** of **≥ 1-hour** both-sides spandrel, **or** a **≥ 1-hour** flame barrier projecting **≥ 750 mm** | Exterior openings in adjacent stories | Exc 1: **≤ 3** stories. Exc 2: sprinklers throughout **903.3.1.1 or 903.3.1.2**. Exc 3: open parking | Conditional | If 13 or 13R is locked throughout, document Exc 2 and omit the spandrel; otherwise detail the **900 mm / 750 mm** option | Verified |
| 705.8.6 | Same-lot vertical roof exposure | Opening **< 4.5 m** vertically above an adjacent roof, with FSD to the imaginary line **< 4.5 m** each side, shall be a **≥ ¾-hour** protective | Buildings on the same lot | Exc 1: **≥ 1-hour** roof for **≥ 3 m** from the facing wall, including supports | Conditional | Protect low podium-roof windows facing a higher tower wall, or rate the lower roof | Verified |
| 705.11 / 705.11.1 | Parapet height | Required parapets **≥ 750 mm** above the roof/wall intersection; uppermost **450 mm** on the roof side noncombustible including counterflashing/coping. Roof slope **> 2:12 (16.7-percent)** toward the parapet: extend to the height of any roof within an FSD that requires opening protection | Parapet required by 705.11 | Exc 4: **1-hour** wall to underside of roof with Group R parallel framing **≥ 1.2 m** and roof openings **≥ 1.5 m**. Exc 6: Table 705.8 permits **≥ 25%** unprotected. Exc 2: floor area **≤ 100 m²** | Conditional | Provide **750 mm** parapets on close FSD walls unless a numbered exception is demonstrated | Verified |

## 7. Fire walls

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| Table 706.4 | R-2 fire-wall rating | Groups A, B, E, H-4, I, **R-1, R-2**, U: **3 hours**. Note a: Type II or V walls **permitted to be 2 hours** | Fire wall used to create separate buildings | H-1/H-2 **4 h**; F-2/S-2/R-3/R-4 **2 h** (not this occupancy row) | Conditional | If a fire wall is used, schedule **3 h** unless both sides are Type II or V | Verified |
| 706.5 | Horizontal fire-wall extension | Extend **≥ 450 mm** beyond the exterior surface | Fire wall, exterior wall to exterior wall | Exc 1–2: terminate at interior of sheathing with **≥ 1.2 m** of **≥ 1-hour** exterior each side and **≥ ¾-hour** openings | Conditional | Carry the fire wall through the facade or document the 1.2 m rated-skin exception | Verified |
| 706.5.1 | Exterior walls at fire-wall intersection | **1-hour** exterior walls with **¾-hour** openings for **≥ 1.2 m** each side, unless the angle is **≥ 180 degrees** | Fire wall meets an exterior wall | Imaginary-lot-line protection also skipped at **≥ 180 degrees** | Conditional | Detail the re-entrant corner or prove a straight **180-degree** facade | Verified |
| 706.5.2 | Projecting elements near fire wall | Fire wall extends to the outer edge of any balcony, overhang, canopy, marquee or similar projection **≤ 1.2 m** from the wall | Horizontal projections beside a fire wall | Listed 1-hour / ¾-hour opening exceptions 1–3 | Conditional | Stop balconies short of **1.2 m** or extend the fire wall through the projection | Verified |
| 706.6 | Fire wall above roofs | Terminate **≥ 750 mm** above both adjacent roofs | Fire walls | Exc 2: **2-hour** wall may stop at roof deck with **1-hour** roof within **1.2 m** and openings **≥ 1.2 m**. Exc 5: walls above a **3-hour** 510.2 podium assembly may start at the top of that assembly (510 hours not imported) | Conditional | Parapet the fire wall **750 mm** unless a numbered roof-termination exception is proven | Verified |
| 706.6.1 | Stepped-building fire wall | Terminate **≥ 750 mm** above the lower roof; exterior wall extending **> 750 mm** above the lower roof is **≥ 1 hour** both sides with **≥ ¾-hour** openings; portion **> 4.5 m** above the lower roof need not be rated unless other provisions apply | Fire wall also serving as exterior wall at different roof levels | Exception: **1-hour** lower roof within **3 m**, supports **1 hour**, no openings within **3 m** | Conditional | Section the podium/tower step and apply the **750 mm / 4.5 m** stations | Verified |
| 706.6.2 | Sloped roof at interior fire wall | Where slope toward the fire wall is **> 2:12**, wall height equals roof height at **1200 mm** from the wall **plus 750 mm**, and not less than **750 mm** | Interior fire wall with sloping roofs | None stated | Conditional | Raise the fire-wall parapet on the uphill side of a sloped roof | Verified |
| 706.7 | Combustible members into masonry fire wall | Opposite-side embedded ends **≥ 100 mm** apart; hollow walls filled solid **≥ 100 mm** above, below and between members | Combustible members bearing into a concrete or masonry fire wall | None stated | Conditional | Offset timber/joist pockets through the fire wall | Verified |
| 706.8 | Fire-wall openings | Each opening **≤ 15 m²**; aggregate width **≤ 25%** of the wall length at any floor | Openings through a fire wall | Exc 1: party walls — no openings. Exc 2: both buildings sprinklered 903.3.1 throughout — **15 m²** not limited; **25% still applies** | Conditional | Size fire-wall doors to the **15 m² / 25%** cap | Verified |

## 8. Fire barriers

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 707.3.1 / 713.4 | Shaft barrier rating | Use 713.4 (in this chapter): **≥ 2 h** connecting **4 or more** stories; **≥ 1 h** connecting fewer than 4; not less than the floor penetrated; need not exceed **2 h** | Fire barrier enclosing a shaft | Interior exit stairs follow 1023.1 (hours not imported) | Direct | Schedule **2-hour** shaft walls for the tower; do not import 403.2.1.2 reductions from commentary | Verified |
| 707.3.2–707.3.5 | Exit-enclosure ratings | Interior exit stair/ramp → 1023.1; exit passageway → 1024.3; horizontal exit → 1026.1; exit-access stair enclosure → 713.4 | Fire barriers for those exits | Values not filled from Chapter 10 | External verification | Coordinate exit-enclosure hours with the Chapter 10 matrix | Verified |
| 707.3.7 | Incidental-use barrier | FRR not less than Table 509.1 | Incidental uses | Sprinkler-in-lieu walls that only resist smoke are not fire barriers | External verification | Do not import Table 509.1 hours; list trash, linen and similar rooms on the incidental-use schedule | Verified |
| 707.3.9 | Mixed-occupancy barrier | FRR not less than Table 508.4 | Separated mixed occupancies | Also apply 707.3.10 if the wall separates fire areas | External verification | Do not import Table 508.4; tag podium retail/parking separations for a Chapter 5 check | Verified |
| Table 707.3.10 | Fire-area separation rating | Group **R** (with A, B, E, F-2, H-4, H-5, I, M, S-2): **2 hours**. Mixed-occupancy fire areas: **highest** table value. H-1/H-2 **4 h**; F-1/H-3/S-1 **3 h**; U **1 h** | Fire barriers, fire walls or horizontals separating fire areas | Do not use this table as occupancy-separation (that is Table 508.4) | Direct | If fire areas are used, separate R fire areas with **2-hour** barriers or horizontals | Verified |
| 707.5 / 707.5.1 | Fire-barrier continuity and support | Continuous from foundation or floor/ceiling below through concealed space to the underside of the floor/roof sheathing, deck or slab; supporting construction FRR **≥** the barrier; hollow vertical spaces fireblocked at every floor | Fire barriers | Incidental-use **≤ 1 h** support unrated in Type IIB/IIIB/VB (Table 509.1 hours not filled). Exit-passageway top may match 1024.3 | Direct | Run shaft and occupancy-separation walls through the ceiling; fireblock stud cavities at each floor | Verified |
| 707.6 | Fire-barrier opening limits | Aggregate opening width **≤ 25%** of wall length; each opening **≤ 15 m²** | Openings in a fire barrier | Exc 1: **15 m²** waived where adjoining floors have 903.3.1.1 (**25% remains**). Exc 2: both limits waived for fire doors serving exit-access or interior-exit stair/ramp enclosures. Exc 3: E119/UL 263 protective with FRR ≥ wall. Exc 4: 25% waived for atrium fire windows. Exc 5: both waived for stair-to-passageway doors | Direct | Keep incidental and occupancy-separation openings within **25% / 15 m²** unless a numbered exception applies | Verified |

## 9. Fire partitions — dwelling units and corridors

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 708.1 | Fire-partition applications | Includes Group R unit separations (420.2), corridor walls (1020.3), elevator lobby (3006.3), egress balconies (1021.2), R-1/R-2 dwelling/sleeping separations (907.2.8.1 / 907.2.9.1), vestibules (1028.2) | Walls listed in 708.1 | Mall tenant and ambulatory walls omitted unless podium mix is opened | Direct | Classify unit demising, corridor and lobby walls as fire partitions, not fire barriers | Verified |
| 708.3 | Fire-partition rating | **Not less than 1 hour** | Fire partitions | Exc 1: corridor **½ hour** only where Table 1020.2 permits (table not imported). Exc 2: DU/SU separations **≥ ½ hour** in Type IIB/IIIB/VB with **903.3.1.1 throughout** (not 13R) | Direct | Schedule **1-hour** unit and corridor partitions for a Type I/II tower; do not use the ½-hour unit exception on Type I | Verified |
| 708.4 | Fire-partition continuity | From top of foundation or floor/ceiling below to underside of sheathing/deck/slab **or** to a floor/roof-ceiling assembly with FRR **≥** the partition | Fire partitions | Exc 1: crawl with floor above **≥ 1 h**. Exc 2: corridor wall may stop at corridor ceiling membrane if membrane matches the wall and (2.1) room-side membrane continues, or (2.2) 13 **or** 13R throughout **including the interstitial**. Exc 3: tunnel corridor with rated ceiling | Direct | Prefer deck-to-deck unit walls; if using a corridor membrane termination, document Exc 2.1 or 2.2 | Verified |
| 708.4.1 | Supporting construction | FRR **≥** the supported partition | Fire-partition support | Type IIB/IIIB/VB: support rating not required for DU/SU, corridors, mall tenants, ambulatory, R-1/R-2 unit walls, vestibules | Direct | On Type I/II, keep floors supporting 1-hour partitions at least 1 hour (Table 601 still governs) | Verified |
| 708.4.2 | Combustible interstitial fireblock/draftstop | Where partitions do not reach the deck, fireblock (718.2.1) or draftstop (718.3.1 / 718.4.1) on the partition line | Combustible construction | Exc 1: 903.3.1.1 throughout, or 903.3.1.2 with interstitial protection as for 13. Exc 2: corridor that also separates units — draftstop above **one** wall only. Exc 3: R-2 **< 4** dwelling units. Exc 4: R-2 **≤ 4** stories and **≤ 18 m** — attic draftstop **≤ 280 m²** or every **2** units, whichever smaller | Conditional | High-rise exceeds Exc 3–4; if combustible concealed space exists, fireblock/draftstop unless Exc 1 is proven | Verified |

## 10. Smoke barriers and smoke partitions

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 709.3 | Smoke-barrier rating | **1-hour** fire-resistance rating | Smoke barriers | Group I-3 **≥ 2.5 mm** steel (not this occupancy) | Conditional | Rate AOR, elevator-lobby and 909 smoke-barrier walls **1 hour** when those features exist | Verified |
| 709.4 | Smoke-barrier continuity | Effective membrane from foundation or floor/ceiling below to underside of sheathing/deck/slab, including concealed and interstitial spaces; supporting construction rated except Type IIB/IIIB/VB | Smoke barriers | Interstitial exception where ceiling/exterior wall provides equivalent fire and smoke resistance. Horizontal continuity: 709.4.1 compartments vs 709.4.2 AOR/lobby | Conditional | Run smoke barriers through the ceiling void; do not stop at a lay-in ceiling unless the exception is demonstrated | Verified |
| 709.4.2 | AOR / elevator-lobby enclosure stop | Terminate at a **≥ 1-hour** fire barrier, another smoke barrier, or an outside wall | Smoke barriers enclosing an area of refuge (1009.6.4) or elevator lobby (405.4.3, 3007.6.2, 3008.6.2) | Smoke/draft door not required at the hoistway door or the AOR-to-exit door | Conditional | Close the lobby/AOR smoke enclosure to a rated barrier or the exterior | Verified |
| 710.5.2.2 | Smoke-partition door leakage | **≤ 0.015 m³/s per m²** of door at **25 Pa**, ambient and elevated temperature (UL 1784; NFPA 105 installation) | Where smoke-and-draft-control doors are required in smoke partitions | None stated | Conditional | Specify UL 1784 doors if I-2-style smoke partitions or 710 doors appear | Verified |

I-2/I-3 smoke-compartment walls, 20 mm cross-corridor undercuts and I-2 pass-throughs are omitted (Not typical).

## 11. Horizontal assemblies

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 711.2.3 | Horizontal supporting construction | Protect supporting construction to the FRR of the horizontal assembly | Rated floors and roofs | Type IIB/IIIB/VB: incidental **≤ 1 h**, DU/SU 420.3, and 709 smoke-barrier horizontals may have unrated support | Direct | Encase primary members supporting rated floors (see also 704.3) | Verified |
| 711.2.4 | Floor/roof FRR floor | Not less than type of construction (Table 601, not imported), and not less than 711.2.4.1–711.2.4.6 | Horizontal assemblies | Mixed occupancy → 508.4; fire area → Table 707.3.10; incidental → 509 | External verification | Overlay Table 601 hours with unit-separation and fire-area hours | Verified |
| 711.2.4.3 | Dwelling/sleeping-unit floor rating | Horizontal assemblies serving as DU/SU separations per 420.3: **not less than 1 hour** | Floors between dwelling or sleeping units | **≥ ½ hour** in Type IIB/IIIB/VB with 903.3.1.1 throughout | Direct | Keep unit-to-unit floors **1 hour** on Type I/II; do not use the ½-hour exception | Verified |
| 711.2.5 | Lay-in ceiling uplift | Lay-in panels in a rated floor/roof-ceiling shall resist **48 Pa** upward, or hold-downs shall be installed | Lay-in acoustical panels in rated assemblies | None stated | Conditional | Specify hold-down clips or a tested **48 Pa** panel | Verified |
| 711.2.6 | Unusable crawl or attic membrane | **1-hour** floor/ceiling over an unusable crawl: ceiling membrane may be omitted. **1-hour** roof over an unusable attic: floor membrane may be omitted | Unusable crawl or attic | Usable storage attics are not this exception | Conditional | Omit the unused membrane only where the space is documented as unusable | Verified |

## 12. Vertical openings

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 712.1.2 | In-unit unconcealed opening | Opening **≤ 4** stories, totally within one dwelling unit, unconcealed | Private unit stair or void | None stated | Conditional | Limit duplex/triplex voids to **4** stories and keep them unconcealed | Verified |
| 712.1.3.1–712.1.3.2 | Escalator opening | Opening **≤ 2×** escalator projected area; **≤ 4** stories other than Groups B and M; 903.3.1.1 plus draft curtain and NFPA 13 sprinklers. Alternative: **≥ 1.5-hour** noncombustible shutters, closing **≤ 150 mm/s**, smoke-detector actuated | Escalators penetrating floors | B/M storey cap does not apply | Conditional | If an amenity escalator is added, use the draft-curtain path or listed **1.5 h** shutters | Verified |
| 712.1.7 | Atrium story threshold | Other than I-2/I-3: atrium where the floor opening connects **3 or more** stories (Section 404). I-2/I-3: **2 or more** stories | Vertical opening treated as an atrium | A-1/A-4/A-5 balconies and 505 mezzanines are not a story | Conditional | If a lobby void connects **3+** stories, apply Section 404; do not import 404.6 hours | Verified |
| 712.1.9 | Two-story opening | Opening connecting **not more than 2** stories, other than I-2/I-3, not otherwise listed | Unenclosed two-story void | Not through a fire-area or smoke barrier; not concealed; **not open to a Group I or R corridor**; not open to a corridor on nonsprinklered floors; separated from other floor openings by shaft construction | Conditional | Do not open a two-story amenity void into an R corridor | Verified |
| 712.1.13.1 | Horizontal fire door | FRR **≥** the assembly penetrated; NFPA 288; labeled | Floor fire doors in rated horizontals | None stated | Conditional | Match hatch ratings to the floor | Verified |
| 712.1.15 | Skylights in rated roofs | Unprotected skylights **not permitted** where the roof must be rated per 705.8.6 | Skylights and roof penetrations in a roof required to be rated by 705.8.6 | Supporting construction still rated | External verification | Protect or omit skylights on roofs that 705.8.6 requires to be rated | Verified |

## 13. Shaft enclosures and chutes

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 713.4 | Shaft fire-resistance rating | **Not less than 2 hours** where connecting **four stories or more**; **not less than 1 hour** where connecting **less than four stories**. Story count **includes basements**, **excludes mezzanines**. Rating **not less than** the floor penetrated and **need not exceed 2 hours**. Nonsymmetrical walls per 703.2.1.1 | Shafts protecting floor/roof openings (not interior exit stairs — those are 1023) | Commentary 403.2.1.2 1-hour reduction is **not** Chapter 7 code and is not adopted | Direct | Specify **2-hour** elevator, MEP and refuse shafts for the high-rise; count basements | Verified |
| 713.6 | Exterior wall as shaft | Exterior wall that is part of a shaft complies with 705; shaft FRR does **not** apply to that wall | Exterior wall forming part of a required shaft | Overlay still required for 1021.2 / 1023.7 / 1027.6 (hours not imported) | Conditional | Do not add shaft hours onto an exterior wall that only needs Table 705.5 | Verified |
| 713.7 | Shaft openings | Protect as fire-barrier openings (716); doors self- or automatic-closing by smoke detection (716.2.6.6) | Openings in a shaft enclosure | Openings other than those necessary for the shaft are prohibited (713.7.1) | Direct | Use smoke-activated shaft doors; do not put borrowed lights into shafts except as required for the shaft purpose | Verified |
| 713.11 | Shaft bottom | Enclose at the lowest level with FRR **≥** the lowest floor penetrated **and ≥** the shaft; **or** terminate in a related-use room with FRR and protectives **≥** the shaft; **or** listed fire dampers at the lowest floor | Shaft that does not extend to the bottom of the building | Exc 1: bottom-only openings plus draftstop or sprinklers. Exc 2: waste/linen → 713.13.4. Exc 3: no combustibles and no interior openings | Conditional | Close elevator/MEP shafts at transfer levels with a 2-hour soffit or a rated equipment room | Verified |
| 713.12 | Shaft top | Extend to roof sheathing/deck/slab with Table 601 roof construction; **or** close below the roof with FRR **≥** topmost floor penetrated **and ≥** the shaft; **or** extend past the roof per 1511 | Top of every shaft | 713.12.1: no fire/smoke damper required where the shaft goes through the roof into a 1511 rooftop structure with ducts connected directly to HVAC | Direct | Cap shafts at a 2-hour lid or carry them to the roof assembly | Verified |
| 713.13.3 | Chute access room | **≥ 1-hour** fire barriers and/or horizontals; openings **≥ ¾-hour**; doors self- or automatic-closing on smoke; room configured so the room door latches with the chute panel in any position | Waste, recycling or linen chute access | In-unit chute serving and contained in **one** dwelling unit is exempt (713.13 Exc) | Conditional | Provide a 1-hour chute vestibule; do not open chutes directly to corridors (713.13.1) | Verified |
| 713.13.4 | Chute discharge room | Enclosure FRR **not less than** the shaft; opening protectives equal to the shaft protection; smoke-activated closing; waste chute shall **not** terminate in an incinerator room | Chute discharge | Collection rooms **without** chutes → Table 509.1 (not imported) | Conditional | Match the discharge-room rating to the **2-hour** chute shaft | Verified |
| 713.13.6 | Chute sprinklers | Approved automatic sprinklers per 903.2.11.2 | Waste, recycle and linen chutes | Design density not in this chapter | External verification | Show chute sprinklers on the fire-protection drawings; do not import 903.2.11.2 spacing | Verified |
| 713.14 | Elevator hoistways | Construct per 712, 713 and Chapter 30 | Elevator, dumbwaiter and other hoistways | Chapter 30 lobby/opening rules not imported | External verification | Keep hoistway construction on 713.4; resolve lobbies in Chapter 30 | Verified |

## 14. Penetrations

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 714.4.1.2 | Wall through-penetration firestop | ASTM E814 / UL 1479 at **not less than 2.49 Pa**; **F** rating **≥** wall FRR | Through penetrations of fire-resistance-rated walls | T rating not required for walls in this clause. Metallic concrete/masonry path: max **150 mm** diameter and **0.1 m²** opening with grout full thickness | Direct | Specify F-rated firestop systems matching the wall hour | Verified |
| 714.4.2 Exc 1 | Unlisted steel electrical boxes | Each box **≤ 0.01 m²**; aggregate **≤ 0.065 m² in any 10 m²** of wall; annular space **≤ 3.2 mm**; opposite-side boxes separated **≥ 600 mm** horizontally (or by cavity depth / fireblock / putty pads / listing) | Membrane penetrations of walls/partitions **max 2 hours** | Listed boxes, putty pads, or Exc 6 for oversized boxes. **Do not use commentary 9 m²** | Direct | Limit back-to-back boxes; keep the **10 m²** aggregate, not the commentary 9 m² | Verified |
| 714.5.1.2 | Floor through-penetration firestop | Pressure **≥ 2.49 Pa**; **F** and **T** ratings **≥ 1 hour** and **≥** floor FRR | Horizontal through penetrations | T not required in a wall cavity; drains in concealed horizontals; metal conduit **≤ 100 mm** into metal-enclosed switchgear | Direct | Use F/T firestops through unit and corridor floors | Verified |
| 714.5.1 Exc 1 | Multi-floor metallic penetrant | Diameter **≤ 150 mm** and aggregate **≤ 92,900 mm² per 10 m²** of floor | Steel/ferrous/copper/concrete/masonry through a single rated floor, unlimited floors if both limits met | Concrete-floor grout path similar with **≤ 92,900 mm²** per floor | Conditional | Cap unlisted metallic stacks at the aggregate area | Verified |
| 714.5.2 Exc 1–2 | Ceiling membrane penetrations | Metallic/concrete/masonry aggregate **≤ 64,500 mm² per 10 m²** of ceiling. Steel electrical boxes **≤ 10,300 mm²** each, aggregate **≤ 64,500 mm² per 10 m²**, annular **≤ 3.2 mm**, in **max 2-hour** horizontals | Membrane penetrations of rated floor/roof-ceiling assemblies tested without penetrations | Listed boxes and firestop exceptions | Direct | Coordinate downlights and boxes with the **64,500 mm² / 10 m²** ceiling cap | Verified |
| 714.5.4 | Smoke-barrier penetration leakage | UL 1479 air leakage at **75 Pa**: **≤ 1.5 m³/min per m²** of opening, **or** cumulative **≤ 25 L/s per 9 m²** of wall or floor | Penetrations in smoke barriers | Ambient and elevated tests | Conditional | Require L-rated firestops on AOR/lobby smoke barriers | Verified |
| 714.6.1–714.6.2 | Nonrated floor penetrations | Noncombustible penetrants connecting **max 5 stories** with noncombustible or classified fill; any penetrants connecting **max 2 stories** with approved annular fill | Non-fire-resistance-rated floors | None stated | Conditional | Shaft nonrated transfer floors still need annular fill or a 713 enclosure | Verified |

## 15. Joints and voids

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 715.3 | Fire-resistant joint system | Duration **≥** the assembly FRR (ASTM E1966 / UL 2079 as applicable) | Joints in or between rated walls, floors and roofs | Ten listed location exceptions; control joints **≤ 16 mm** tested as part of E119/UL 263 | Direct | Specify listed joint systems at floor/wall and wall/wall intersections | Verified |
| 715.3.1 Exc | Exterior joint fire exposure | Where FSD **> 3000 mm**, test from the interior only | Nonsymmetrical wall joints | Else both faces; shortest duration | Conditional | Two-sided joint listings on close lot-line walls | Verified |
| 715.4 | Curtain-wall perimeter containment | ASTM E2307 **F** rating **≥** floor FRR | Void between a curtain wall and a rated floor | Vision glass extending to the finished floor: approved material, **2.5 Pa**, time **≥** floor FRR | Direct | Provide an E2307 safing line at every curtain-wall floor edge | Verified |
| 715.8 | Smoke-barrier joint leakage | **≤ 7.75 L/s per m** at **75 Pa**, ambient and elevated (UL 2079) | Joints in smoke barriers and curtain-wall/horizontal smoke-barrier voids | None stated | Conditional | Specify L-rated joints on smoke-barrier lines | Verified |

## 16. Opening protectives

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 716.2.2.1 | Corridor / smoke-barrier fire door | **Minimum 20 minutes**; NFPA 252 / UL 10C **without** hose stream | Table 716.1(2) 20-minute doors in corridor or smoke-barrier walls | Viewport **≤ 25 mm** diameter with **≥ 6 mm** glass disc in a holder that will not melt at **927°C** | Direct | Specify 20-minute smoke-and-draft corridor doors; hose-stream not required on this path | Verified |
| 716.2.2.1.1 | Smoke and draft control | Leakage **≤ 15 L/s per m²** at **25 Pa** (UL 1784); louvers prohibited | Corridor and smoke-barrier fire doors | Terminated stops prohibited where cited | Direct | Put UL 1784 / “S” label on corridor unit-entry and lobby doors | Verified |
| 716.2.2.2 | Other 0.5-hour partition doors | **Minimum 20 minutes with hose stream** (NFPA 252 / UL 10B / UL 10C) | Fire partitions **0.5 hour** other than corridors | Type I/II unit walls are 1 hour, so this row is the ½-hour exception path | Conditional | If ½-hour unit walls are used (Type IIB/IIIB/VB + 13), test those doors **with** hose stream | Verified |
| 716.2.2.3 | Exit-door temperature rise | Maximum transmitted temperature rise **not more than 250°C** above ambient at **30 minutes** | Fire doors in interior exit stairways, ramps and exit passageways | Not required where sprinklers throughout are **903.3.1.1 or 903.3.1.2** | Conditional | Use **250°C** from the code text (not commentary **232°C**) unless the sprinkler exception is locked; Table 716.1(1) “T” mark is **232°C / 30 min** | Verified |
| 716.2.2.3.1 | Exit-door vision panel | Fire-protection-rated glazing **> 0.065 m²** **not permitted**; larger panels only if fire-resistance-rated and meeting 716.2.2.3 temperature rise | Glazing in those exit doors | None stated | Direct | Keep stair-door vision panels **≤ 0.065 m²** unless W-rated glazing is listed for the door | Verified |
| Table 716.1(2) | Fire-wall / >1 h fire-barrier doors | Wall **4 h** → door **3 h**, sidelights NP, **W-240**; wall **3 h** → door **3 h** (note d: two **1½ h** doors ≡ one **3 h**), **W-180**; wall **2 h** → door **1½ h**, vision **64,500 mm²** (≤ **D-H-90**, > **D-H-W-90**), sidelights NP, **W-120**; wall **1½ h** → door **1½ h**, same vision split, **W-90** | Fire walls and fire barriers with required FRR **greater than 1 hour** | Remainder of the table (shafts, 1 h barriers, partitions, corridors) is flattened — **do not reconstruct from memory** | Conditional | Use this block for 2-hour shafts/fire areas; hold all other Table 716.1(2) rows as Verify source | Verified |
| Table 716.1(2) cont. | Exterior-wall and smoke-barrier doors | Exterior: wall **3 h** → door **1½ h**, vision **64,500 mm²** **D-H-90**, SL NP, **W-180**; wall **2 h** → door **1½ h**, max size tested, **D-H-90 or D-H-W-90**; wall **1 h** → door **¾ h**, **D-H-45**. Smoke barrier: wall **1 h** → door **⅓ h**, max size tested, **D-20** | Exterior walls and smoke barriers | Note h: fire-protection-rated glazing not permitted in SBC 801 §1207 ESS barriers | Conditional | Match exterior opening-protective hours to Table 705.5 wall hours | Verified |
| Table 716.1(2) remainder | Shaft, 1 h barrier, partition, corridor door ratings | Flattened repeat of `21164,500 mm² D-H-90` after the double-fire-wall `321½` token | Other assembly types in Table 716.1(2) | Do not fill from IBC memory | External verification | Verify the published table for 1-hour shaft, corridor and unit-entry door hours before issuing the door schedule | Verify source |
| Table 716.1(3) | Fire-window ratings | Fire walls: NP. Fire barriers **1 h**: NP (general). Atrium / incidental / mixed (707.3.6 / 707.3.7 / 707.3.9): wall **1 h** → window **¾ h**, **OH-45 or W-60**. Fire partitions **0.5 h**: **⅓ h**, **OH-20 or W-30**. Smoke barriers **1 h**: **¾ h**, **OH-45 or W-60**. Exterior **1 h**: **¾ h**; exterior **0.5 h**: **⅓ h**. Party walls: NP | Fire-protection-rated windows | Fire-barrier `>ch1` token and exterior `>1` → `1/2` window hour are OCR holds | Conditional | Prefer W-rated glazing in 2-hour shafts; use OH-45 only where the 1-hour mixed/incidental/atrium row applies | Verified |
| Table 716.1(3) OCR | Fire-barrier >1 h and exterior >1 h windows | Wall token **`>ch1`**: NP. Exterior **`>1`** window **`1/2`** (1½ vs ½ unresolved) | Those table rows | Do not adopt **½ hour** from the flattened exterior cell | External verification | Verify the published Table 716.1(3) before specifying windows in >1-hour exterior walls | Verify source |
| 716.2.6.6 | Smoke-activated closing delay | Closing shall begin **not more than 10 s** after smoke-detector actuation | Hold-open automatic-closing doors at listed locations | None stated | Conditional | Set hold-open release delay **≤ 10 s** | Verified |
| 716.3.2.1.2 | Interior fire-window area | Fire-protection-rated window assemblies **≤ 25%** of the common wall with any room | Interior fire-protection-rated windows | Fire barriers also limited by 707.6 length | Conditional | Cap borrowed-light fire windows at **25%** of the room’s common wall | Verified |
| 716.3.4 | Unrated exterior protected openings | **≥ ¾-hour** fire-protection rating | Non-FRR exterior walls that still require protected openings under 705.3 / 705.8 / 705.8.5 / 705.8.6 | 0.5-hour partitions may use **0.33-hour** fire-protection glazing | Conditional | Where Table 705.8 requires protected openings in a 0-hour wall, specify **¾-hour** protectives | Verified |

## 17. Ducts and air-transfer openings

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| Table 717.3.2.1 | Fire-damper rating | Assemblies **< 3 hours**: damper **≥ 1.5 hours**. Assemblies **3 hours or greater**: damper **≥ 3 hours** | Fire dampers (and combination dampers per 717.3.2.3) | None stated | Direct | Use **1.5-hour** dampers in 1- and 2-hour walls; **3-hour** dampers only in 3-hour fire walls | Verified |
| 717.3.2.2 | Smoke-damper class | Class **I or II**; elevated-temperature rating **≥ 121°C** | Smoke dampers | None stated | Direct | Specify Class I or II smoke dampers at **≥ 121°C** | Verified |
| 717.3.3.1 | Fire-damper actuation | Operating temperature ≈ **10°C** above normal duct temperature, **not less than 71°C**; **not more than 177°C** if in a Section 909 smoke-control system | Primary heat-responsive device | None stated | Direct | Select fusible links at **≥ 71°C** | Verified |
| 717.3.3.2 | Smoke-detector distance | In-duct detector or sampling tubes **within 1500 mm** of the damper, no inlets/outlets between; transfer-opening spot detector **within 1500 mm** horizontally | Smoke-damper actuation | Corridor detection or area detection alternatives 4–5 | Direct | Place duct detectors within **1500 mm** of each smoke damper | Verified |
| 717.4.1–717.4.2 | Damper access | Access door **not less than 300 mm** square, or a removable duct section, where fusible links or internal operators exist; permanent label letters **not less than 12.5 mm** (“FIRE/SMOKE DAMPER”, “SMOKE DAMPER” or “FIRE DAMPER”) | Fire and smoke dampers | Remote inspection per NFPA 80/105 where access is restricted | Direct | Show 300 mm access doors and labels on MEP drawings | Verified |
| 717.5.2 | Fire-barrier duct dampers | Listed fire dampers | Ducts and air-transfer openings in fire barriers | Do not penetrate exit enclosures except as 1023.5 / 1024.6 permit. Exc 3: omit FD where wall **≤ 1 h**, steel **≥ 0.47 mm**, 13 **or** 13R, not Group H, fully ducted HVAC | Direct | Provide fire dampers at 2-hour occupancy/fire-area barriers unless a numbered exception applies | Verified |
| 717.5.3 | Shaft fire and smoke dampers | Listed **fire and smoke** dampers at permitted shaft penetrations | Shaft ducts and air-transfer openings | Exc 1.1: omit FD for steel subducts **≥ 0.47 mm** extending **≥ 550 mm** with continuous 909.11 exhaust. Exc 2 (Group **B and R**, **903.3.1.1** throughout): omit **smoke** dampers on kitchen/dryer/bath/toilet exhaust with the same subduct/**550 mm**/continuous fan. Exc 1.4 / 3: garage shafts separated **≥ 2 h**. Exc 5: FD prohibited on kitchen/dryer exhaust per SBC 501 | Direct | Combine Exc 1.1 and Exc 2 to omit both dampers on R toilet/kitchen exhaust **only if NFPA 13** (not 13R) is locked | Verified |
| 717.5.4 | Fire-partition duct dampers | Listed fire dampers | Fire-partition penetrations, other than Group H | Exc 4: omit FD for ducted HVAC, wall **≤ 1 h**, steel **≥ 0.47 mm**, 13 **or** 13R. Corridor dampers per 717.5.4.1 | Direct | Provide fire or corridor dampers at unit/corridor walls unless the ducted-HVAC exception is documented | Verified |
| 717.5.5 | Smoke-barrier duct dampers | Listed smoke damper in each duct or air-transfer opening | Smoke barriers | Steel ducts opening to **one** smoke compartment only; I-2 Condition 2 QR-sprinkler exception | Conditional | Smoke-damp AOR and elevator-lobby smoke-barrier ducts | Verified |
| 717.6.1 Exc | Three-floor residential duct | **Max 3 floors**; steel **≥ 0.47 mm** in a wall cavity; contained in **one** dwelling/sleeping unit; diameter **≤ 100 mm**; aggregate **≤ 0.065 m² per 9 m²** of floor; **2.5 Pa** annular; ceiling-radiation dampers at rated-ceiling grilles | Dwelling-unit ducts without a fire damper at each floor | This **9 m²** token is CODE (unlike 714.4.2 **10 m²**) | Conditional | Use only for in-unit stacks of three floors or fewer | Verified |

## 18. Concealed spaces, plaster and insulation

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 718.2.1–718.2.2 | Combustible-wall fireblocking | Materials include **50 mm** nominal lumber, two **25 mm**, **18 mm** WSP backed **18 mm**, **20 mm** particleboard backed **20 mm**, **12.5 mm** gypsum, **6 mm** cement millboard, or mineral wool; horizontal intervals **not more than 3000 mm**; unfaced fiberglass fill **≥ 400 mm** high | Combustible concealed stud, furred or staggered walls | Type I/II combustible concealed uses limited by 718.5 | Conditional | Fireblock combustible podium or Type III–V walls at **3 m** horizontally and at every floor | Verified |
| 718.2.6 | Combustible exterior-covering fireblock | Intervals **not more than 6000 mm** either way; concealed area **not more than 9 m²**; noncontinuous closed ends **≥ 100 mm** apart | Combustible exterior coverings/frames (Section 1405) | Metal covering skip: aluminium **≥ 0.5 mm** or steel **≥ 0.4 mm** on noncombustible framing, or NFPA 285 covering | Conditional | Fireblock rainscreen cavities at **6 m / 9 m²** unless a metal/NFPA 285 exception applies | Verified |
| 718.3 | Non-R floor draftstopping | Subdivide combustible floor/ceiling areas **not more than 100 m²** | Occupancies **other than Group R** | Group R follows **708.4.2**. Omit if 903.3.1.1 throughout | Not typical | R floors use 708.4.2, not this **100 m²** cap | Verified |
| 718.4 | Non-R attic draftstopping | Subdivide combustible attic/roof concealed areas **not more than 280 m²** | Occupancies **other than Group R** | Group R follows **708.4.2**. Omit if 903.3.1.1. Ventilate 1202.2.1 | Not typical | R attics use 708.4.2; the high-rise **≤ 18 m / 4-storey** reduction does not apply | Verified |
| 718.3.1 | Draftstop materials | **≥ 12.5 mm** gypsum, **≥ 10 mm** wood structural panel, **≥ 10 mm** particleboard, **≥ 25 mm** nominal lumber, or listed mineral/glass fibre | Floor draftstops | Attic materials 718.4.1 | Conditional | Specify gypsum or wood-panel draftstops where 708.4.2 requires them | Verified |
| 719.2–719.5 | Plaster fire-resistance equivalents | **12.5 mm** unsanded gypsum ≡ **20 mm** 1:3 gypsum-sand ≡ **25 mm** portland-cement sand. Plaster **> 25 mm** needs extra lath **≥ 20 mm** from the outer surface. **12.5 mm** plaster may replace **12.5 mm** concrete cover if **≥ 10 mm** concrete remains on floors and **≥ 25 mm** on columns | Plaster used for fire resistance | None stated | Conditional | Do not substitute finish plaster for tested SFRM on steel | Verified |
| 720.2–720.3 | Insulation flame spread | Concealed or exposed: flame-spread index **≤ 25** and smoke-developed index **≤ 450** (ASTM E84 or UL 723) | Thermal- and sound-insulating materials | Cellulosic loose-fill: no FS limit if SD **≤ 450** by CAN/ULC S102.2 (720.6). Foam → Chapter 26. Plenums → SBC 501 | Direct | Specify FS **25** / SD **450** insulation in walls, floors and attics | Verified |
| 720.3.1 | Exposed attic-floor insulation | Critical radiant flux **not less than 1200 W/m²** (ASTM E970) | Exposed insulation on attic floors | None stated | Conditional | If attic-floor insulation is left exposed, require the E970 flux | Verified |
| 720.7 | Pipe insulation | Flame-spread **≤ 25**, smoke-developed **≤ 450** | Pipe and tubing insulation and covering | Plenums comply with SBC 501 (values not imported) | Direct | Keep pipe lagging on the FS 25 / SD 450 path except in plenums | Verified |

## 19. Prescriptive and calculated fire resistance

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 721.1 | Prescriptive assemblies | Materials in Tables 721.1(1), 721.1(2) and 721.1(3) are assumed to have the tabulated FRR; added heat-dissipation-changing materials need data that the rating is not reduced | Alternative to a tested listing | Tables are OCR-destroyed — **no cell adopted** | External verification | Prefer UL/GA listings. Do not reconstruct brick, gypsum or deck thicknesses from memory | Verify source |
| 721.1.3 | Cast-in-place column ties | Wire **not less than 4.5 mm** diameter, spiral pitch **not more than 200 mm**, or equivalent | Cast-in-place concrete protection of steel columns | None stated | Conditional | If using 721.1(1) column encasement, detail the spiral ties | Verified |
| 721.1.5 | Variable tendon cover | Average cover not less than Table 721.1(1); no tendon less than **one-half** of the table; absolute minimum **20 mm** slabs / **25 mm** beams; reduced-cover tendons contribute **≤ 50%** of required \(M_u\) if member **< 0.23 m²**, **≤ 65%** if larger | Prestressed members with unequal cover | Table 721.1(1) cover values themselves are Verify source | Conditional | Verify published Table 721.1(1) before using calculated tendon cover | Verified |
| 722.2–722.6 | Calculated concrete, masonry, steel, wood | Code-text limits that are readable include foam insulation **< 25 mm** disregarded / **≥ 25 mm** \(R_n = 5\) minutes; exterior one-sided fire FSD **> 1500 mm** (concrete/masonry) or **> 3000 mm** (wood); column \(f'_c\) **> 83 MPa** min dimension **600 mm**; R/C column cover **25 mm × hours** cap **50 mm**; substitute-beam SFRM thickness **≥ 10 mm**; calculated wood assemblies **not more than 1 hour** | Calculated fire resistance in lieu of a test | Equations 7-3/7-5, 7-12, 7-14 \(R_o\), 7-16 and 7-17 \(h_1\) are OCR-unresolved. All 722.* tables are Verify source | External verification | Do not run 722 calculations from this extract; use a published ACI 216.1 / AISI / AWC reference after source check | Verified |
| 722.7.2.1 | Interior mass-timber gypsum fastening | Type S screws penetrate **≥ 25 mm** into mass timber; base and subsequent layers **300 mm** o.c. both ways; subsequent layer offset **100 mm**; panel edges offset **450 mm**; edge screws **25 mm min / 50 mm max**; **32 mm** corner bead at 602.4.2.2 junctions | Type IV-A/B/C interior noncombustible protection | Third layer may use **25 mm** No. 6 Type S to AISI S220 furring. Table 722.7.1(1)/(2) contribution minutes concatenated (`1402803`, `12.5 mm / 16 mm`) — **not adopted** | Conditional | If mass timber is specified, use these fastening rules and verify published protection minutes | Verified |
| 722.7.2.2 | Exterior mass-timber gypsum fastening | Field **300 mm** o.c. each way; joints/ends **150 mm** o.c.; edge fasteners **25–50 mm**; nails min **12 gage**, **11 mm** head, penetrate **≥ 25 mm**; screws ASTM C1002 penetrate **≥ 25 mm** | Exterior side of mass timber | None stated | Conditional | Detail exterior gypsum on mass timber to these spacings | Verified |

## 20. Project-use controls

1. Use **Verified** rows for coordination after the row trigger and branch are confirmed.
2. Treat every **Verify source** row (Figure 705.7, flattened Table 716.1(2) remainder, Table 716.1(3) OCR tokens, and all Tables 721.1 / 722.*) as a design hold point; no affected value is to be placed on issued-for-approval drawings without a published-source check.
3. Do not import Table 601, 508.4, 509.1, 1020.2, 403.2.1.2, 403.2.3, Chapter 9 densities, Chapter 10 corridor hours, Chapter 14 cladding limits, NFPA 82, or SBC 501 plenum values from memory, CS.md, or commentary.
4. Do not treat NFPA 13R as the Table 705.8 `UP, S` branch or as 708.3 Exc 2 / 711.2.4.3 Exc / 717.5.3 Exc 2.
5. Do not apply Group R-3 / U opening, parapet or projection exceptions, I-2/I-3 smoke-compartment walls, mall tenant partitions, or the R-2 **≤ 4** storey / **≤ 18 m** attic-draftstop reduction to this high-rise.
6. Keep CODE **250°C** (716.2.2.3) distinct from Table 716.1(1) **232°C** “T” marking and from commentary 232°C. Keep 714.4.2 aggregate **10 m²**, not commentary **9 m²**.
7. Record construction type, FSD by elevation, sprinkler standard, fire-wall vs fire-area strategy, and shaft storey counts in the project Golden Thread; this matrix is not evidence of SCD NOC or stamped fire-protection compliance.

## 21. Coverage summary

Internal inventory of the attached Chapter 7 extract (numbered code, exceptions, tables, footnotes; commentary excluded). Row-level records are not published.

- **Inventory scope:** numbered code, exceptions, tables, footnotes (commentary excluded)
- **Total independently checkable numeric records:** 2863
- **Verified:** 517
- **Verify source:** 2346

### Counts by top-level section

| Top-level section | Records |
|---|---:|
| 701 | 0 |
| 702 | 0 |
| 703 | 7 |
| 704 | 19 |
| 705 | 102 |
| 706 | 54 |
| 707 | 28 |
| 708 | 17 |
| 709 | 4 |
| 710 | 5 |
| 711 | 12 |
| 712 | 14 |
| 713 | 25 |
| 714 | 31 |
| 715 | 6 |
| 716 | 48 |
| 717 | 30 |
| 718 | 18 |
| 719 | 5 |
| 720 | 6 |
| 721 | 1288 |
| 722 | 1144 |

Section 721 = 8 readable code-text records + ~1280 Verify-source cells in Tables 721.1(1)–(3). Section 722 = 88 readable code-text records + 6 OCR-unresolved equations + ~1050 Verify-source cells in Tables 722.*. Table-cell counts for 721/722 are estimates of independently checkable cells that cannot be adopted.

### Appended-table coverage

| Appended table | Records | Verify source records |
|---|---:|---:|
| Table 705.2 | 4 | 0 |
| Table 705.5 + numeric notes | 24 | 0 |
| Table 705.8 + numeric notes | 29 | 0 |
| Table 706.4 + note a | 5 | 0 |
| Table 707.3.10 | 4 | 0 |
| Table 716.1(1) | 1 | 0 |
| Table 716.1(2) | 14 | 2 |
| Table 716.1(3) | 10 | 2 |
| Table 717.3.2.1 | 2 | 0 |
| Figure 705.7 \(F_{eo}\) | 1 | 1 |
| Tables 721.1(1)–(3) | 1280 | 1280 |
| Tables 722.2 through 722.7 (printed titles include `22.5.1(6)`, `72.5.1(10)`, `72.6.2(*)`, `72.7.1(*)`) | 1050 | 1050 |

No Chapter 7 `*_CS.md` was found. Commentary figures and commentary calculations (ASTM E136 furnace temperatures, 9 m² outlet-box commentary, 232°C commentary vs 250°C code, 403.2.1.2 128 m shaft reduction) were not inventoried as requirements.

## 22. Unresolved-source register

Hold points for the **2346** Verify-source inventory records. Counts are record counts, not distinct numeric values. No value in this register is a design-release figure.

| Affected table / clause | Why unverified | Control note |
|---|---|---|
| Figure 705.7 \(F_{eo}\) | Normative figure; no numeric lookup table in the extract | Do not compute equivalent protected area (Eq. 7-1) until the published figure is read |
| Table 716.1(2) remainder | After the unique 4/3/2/1½-hour fire-wall/fire-barrier block, cells repeat `21164,500 mm² D-H-90`; double-wall row OCR `321½` | Verify published shaft, 1-hour barrier, partition and corridor door hours before issuing the door schedule |
| Table 716.1(3) fire-barrier `>ch1` | Wall-rating token unreadable | Treat general fire-barrier windows as NP until the published >1-hour row is confirmed |
| Table 716.1(3) exterior `>1` → `1/2` | Likely **1½-hour** window OCR as **½** | Do not specify ½-hour fire windows in >1-hour exterior walls from this extract |
| Tables 721.1(1), 721.1(2), 721.1(3) | Concatenated HTML; titles OCR as `7.1.12(a)`, `7.12(2)`, `7.1.13`, `21.13`; thickness cells unreadable (~1280 records) | Do not reconstruct prescriptive assembly thicknesses. Use tested listings |
| Tables 722.2.1.1 through 722.7.1(2) | Flattened W/D, cover, equivalent-thickness and mass-timber-minute grids; titles OCR as `22.5.1(6)`, `72.5.1(10)`, `72.6.2`, `72.7.1` (~1050 records) | Do not adopt concatenated `1402803` or `12.5/16 mm` Type X minutes. Verify published 722 tables if calculated FRR is used |
| Equations 7-3/7-5, 7-12, 7-14 \(R_o\), 7-16, 7-17 | Formula parentheses and \(h_1\) multiplier destroyed in OCR (6 records) | Do not run those calculations from this extract |
