# SBC 201 Chapter 14 Exterior Walls — Group R-2 High-Rise Dimensional Requirements Matrix (2024)

## 1. Document metadata and use limitation

- **Project basis:** Riyadh, Saudi Arabia; Group R-2 residential high-rise; an occupied floor is stated to be more than 23 m above the relevant reference level.
- **Deliverable tier:** Project-use matrices in Sections 4–15 (design-check rows, not pasted inventory), plus a coverage summary and unresolved-source register. The full row inventory is not published.
- **Code/source basis:** SBC 201 (2024), Chapter 14, source file `Reference\SBC 201 2024\source_reference\Chapter_14 — EXTERIOR WALLS.txt`.
- **Extraction audit:** Skill extract. Project-use rows follow the chapter-extract row contract (noun-phrase checks, bold SI values, building-language triggers, named exceptions, check-specific actions). Internal inventory: **225** independently checkable numeric records (**213** Verified, **12** Verify source). Unresolved OCR and the missing ignition table are listed in the register and are not design-release values.
- **Model:** Cursor Grok 4.6.
- **Prepared:** 2026-08-27.
- **Status:** Source-only architectural advisory matrix for design coordination. It is not a stamped compliance statement, facade-engineering report, SCD NOC, SBPS approval, legal opinion, or permission to construct.
- **Outbound-source rule:** No value in this matrix has been imported from Chapter 7, Chapter 16, Chapter 26, Tables 601/602/705.8, SBC 305, SBC 601/SBC 602, IECC climate maps, NFPA 268/275/285 acceptance criteria beyond the numeric triggers stated in this chapter, commentary examples, or the existing chapter summary. Where Chapter 14 sends the user elsewhere, this matrix records the dependency without supplying the outbound value.

### Scope and assumptions

1. Group R-2 and high-rise status are project statements, not independently verified classifications.
2. The exact Riyadh AHJ/permit pathway, project stage, fire-strategy status and SCD NOC status are unconfirmed; therefore this matrix does not conclude compliance.
3. Construction type is unconfirmed. An occupied floor above **23 m** is treated as putting combustible WRB, combustible cladding, MCM and HPL onto the Type I–IV **greater than 12 m** path **if** the tower walls are Type I, II, III or IV. Type V framed walls are not assumed for the tower shaft.
4. Automatic sprinkler protection is not selected. Chapter 14 does not branch the cladding numeric limits on NFPA 13 versus 13R.
5. Cladding system, combustible WRB, foam plastic in the envelope, fire separation distance, climate zone and podium mix are unconfirmed.
6. Table 1404.2 stucco coat thicknesses, Table 1404.2 note e, Table 1404.3(3) Zone 8, Table 1404.3(4) and Table 1405.1.1.1.2 are OCR-unresolved or missing from the extract. Affected rows are **Verify source**.
7. Exterior-wall fire-resistance ratings, unprotected opening percentages, foam-plastic NFPA 285 assemblies, veneer design in SBC 305, climate zone from SBC 601/602, and window/door structural tests in Section 1705.9 require separate verification.

## 2. Legends

### Applicability

| Status | Meaning |
|---|---|
| **Direct** | Expected to govern the stated R-2 tower basis, subject to confirmed geometry and design data. |
| **Conditional** | Governs only when the stated feature, cladding system, construction type, climate-zone branch or exception exists. |
| **Not typical** | Unrelated occupancy-only or Type V-only rule; omitted from this deliverable unless the gap register already opened that use. |
| **External verification** | Chapter 14 points to another section/code/standard, or the project/AHJ basis must be confirmed before use. |

### Source confidence

| Status | Meaning |
|---|---|
| **Verified** | Requirement and any stated numeric value were checked against unambiguous mandatory Chapter 14 source text or an unambiguous table cell. |
| **Verify source** | OCR, flattened table, page-split, missing table, or footnote attachment is unresolved. Not a design-release value. |

## 3. Project decision and gap register

| Decision / gap | Current project basis | Why it controls Chapter 14 application | Required project action |
|---|---|---|---|
| Construction type | Unconfirmed; high-rise R-2 typically Type I or II, not verified | 1402.5, 1404.5, 1405.1.1, 1406.10 and 1408.10 apply to Types I–IV; 1406.11 / 1408.12 / 1407.4.1 Type V paths are different | Freeze type of construction on the code data sheet before cladding specification |
| Cladding system | Unconfirmed: masonry, metal, MCM, HPL, EIFS, wood, vinyl/fiber-cement/PP at podium are all open | Selects which 1404 install rules, 1405 combustible limits, 1406 MCM, 1407 EIFS or 1408 HPL matrix applies | Issue a wall-type schedule by elevation and height above grade plane |
| Combustible WRB | Unconfirmed | Type I–IV walls **greater than 12 m** with a combustible WRB require NFPA 285 unless a listed exception is proven | Identify every WRB as combustible or noncombustible per 703.3; do not treat fenestration flashing as the WRB |
| Foam plastic in the envelope | Unconfirmed | 1403.13 and 1406.12 / 1408.13 send foam to Chapter 26; attachment through foam sheathing sends to 2603.11–2603.13 | Facade and energy consultants to confirm whether foam is in the wall; do not import 2603 values here |
| Climate zone | Unconfirmed; IECC / SBC 601/SBC 602 not imported | Tables 1404.3(2)–(4) interior vapor-retarder class and continuous-insulation R-values vary by zone | Lock the SBC 601/602 climate zone for the site; do not assume a zone from maps in this extract |
| Fire separation distance | Unconfirmed by wall | 1405.1.1 **10%** cap at FSD **1500 mm**; NFPA 268 / Table 1405.1.1.1.2; HPL alternate 1408.11; polypropylene **3 m** | Dimension FSD on each elevation; keep Table 1405.1.1.1.2 as a hold point |
| Combustible cladding height | Occupied floor stated above 23 m; cladding height by material unconfirmed | Types I–IV combustible covering **12 m** (FRTW **18 m**); MCM/HPL above **12 m** need NFPA 285 | Mark cladding material versus height above grade plane on every elevation |
| Podium / Type V framed walls | Unconfirmed | 1407.4.1 drainage EIFS is required on Type V framed Group R walls; vinyl/PP/wood siding is a low-height product class | Freeze podium construction type and rainscreen materials separately from the tower shaft |
| Windows and doors | Unconfirmed products | 1404.13 sends performance to Section 1705.9; flashing still follows 1404.4 | Structural/fenestration schedule to cite 1705.9 tests; wall sections to show 1404.4 flashing |
| Flood hazard | Unconfirmed | 1402.6 / 1402.7 apply only in flood hazard / coastal A / coastal high-hazard areas | Civil/flood consultant to confirm 1612 designation before detailing breakaway walls |
| NOC and fire strategy | SCD NOC and stamped fire-strategy status unconfirmed | NFPA 285 wall listings, combustible cladding and SCD acceptance cannot be concluded from Chapter 14 alone | Engage the qualified local/fire/facade consultants before design freeze |

## 4. Envelope performance

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1401.1 | Chapter scope | This chapter sets minimum requirements for exterior walls, wall coverings, openings, windows and doors, and architectural trim | All exterior walls and coverings | None stated | Direct | Treat Chapter 14 as the weather-envelope and combustible-cladding chapter, not the rating/openings chapter | Verified |
| 1402.2 | Weather-resistant envelope | Provide a weather-resistant envelope with flashing per 1404.4, a water-resistive barrier behind the veneer per 1403.2, a means of draining water to the exterior, and condensation protection per 1404.3 | Exterior walls | Exception 1: not required over concrete or masonry walls designed to Chapters 19 and 21. Exception 2: ASTM E331 barrier path. Exception 3: EIFS complying with 1407.4.1 | Direct | Show WRB, drainage plane and flashing on typical wall sections unless a numbered exception is demonstrated | Verified |
| 1402.2 Ex. 2.1–2.4 | ASTM E331 barrier-wall test | Test assembly not less than **1.2 m by 2.4 m**, minimum differential pressure **0.3 kN/m²**, minimum duration **2 hours**, with not fewer than **one** opening, **one** control joint, **one** wall/eave interface and **one** wall sill; water shall not penetrate those joints | Barrier envelope proposed in lieu of drainage, 1403.2 and 1404.4 | Pass/fail is no water at control joints, opening perimeters or dissimilar-material terminations | Conditional | Use only if a tested barrier wall is specified; match tested opening and joint details on shop drawings | Verified |
| 1403.2 | Water-resistive barrier | Not fewer than **one** layer of WRB attached to studs or sheathing, flashed per 1404.4, continuous behind the exterior wall veneer. Comply with **No. 15** felt ASTM D226 Type 1; ASTM E2556 Type I or II; ASTM E331 per 1402.2; or other approved materials | WRB required by 1402.2 | Concrete/masonry and tested-barrier exceptions under 1402.2 | Direct | Specify the WRB product standard on the wall-type schedule and lap it with 1404.4 flashing | Verified |
| 1402.2 Ex. 3 | EIFS envelope branch | EIFS complying with Section 1407.4.1 may be used in lieu of the 1402.2 drainage/WRB/flashing prescription | EIFS specified as the exterior envelope | Numeric drainage efficiency is in 1407.4.1, not here | Conditional | Do not treat a barrier-coat EIFS as satisfying 1402.2 unless 1407.4.1 is also met | Verified |

## 5. Combustible water-resistive barriers

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1402.5 | Combustible WRB NFPA 285 | Type I, II, III or IV exterior walls **greater than 12 m** above grade plane that contain a combustible WRB shall be tested to and comply with NFPA 285. Combustibility per 703.3. Fenestration products, fenestration flashing, WRB flashing and through-wall flashings are **not** part of the WRB for this section | Type I–IV walls taller than **12 m** with a combustible WRB | Exception 1: WRB is the only combustible component and covering is brick, concrete, stone, terra cotta, stucco or steel at Table 1404.2 minimum thickness. Exception 2: WRB is the only combustible component and meets 1402.5 Exception 2.1 and 2.2 | Direct | Require an NFPA 285 listed wall assembly for any combustible WRB on the tower shaft, or document a numbered exception | Verified |
| 1402.5 Ex. 2.1 | Low-heat WRB cone calorimeter | Peak heat release rate less than **150 kW/m²**, total heat release less than **20 MJ/m²**, effective heat of combustion less than **18 MJ/kg**, ASTM E1354 horizontal, incident flux **50 kW/m²**, thickness intended for use | Exception 2 path; WRB is the only combustible component | Must be used together with Exception 2.2 | Conditional | Accept this exception only with a complete E1354 report at the installed thickness | Verified |
| 1402.5 Ex. 2.2 | Low-heat WRB surface burning | Flame spread index **25** or less and smoke-developed index **450** or less, ASTM E84 or UL 723, specimen mounting ASTM E2404 | Exception 2 path; WRB is the only combustible component | Must be used together with Exception 2.1 | Conditional | Do not claim Exception 2 from E84/UL 723 alone | Verified |

## 6. Weather covering thicknesses

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1404.2 | Minimum covering thickness | Exterior walls shall provide weather protection. Materials at the minimum nominal thickness in Table 1404.2 are acceptable as approved weather coverings | Exterior weather coverings | Note a: wood siding thinner than **12.5 mm** only over sheathing conforming to 2304.6. Note b: thickness is the narrowest solid thickness exclusive of texture. Note d: copper mass **4.88 kg/m²** (cold-rolled and lead-coated) or **3.66 kg/m²** (shingles, high-yield and lead-coated high-yield) | Direct | Put the specified covering and Table 1404.2 thickness on the wall-type schedule | Verified |
| Table 1404.2 | Masonry and stone coverings | Adhered masonry veneer **6.35 mm**; anchored natural stone **50.4 mm**; architectural cast stone **62.5 mm**; other anchored masonry veneer **66.67 mm**; marble slabs **25.4 mm**; terra cotta anchored **12.7 mm**; terra cotta adhered **9.525 mm** | Those coverings specified | Note b exclusive of texture | Conditional | Confirm unit thickness on material submittals against the tabulated minimum | Verified |
| Table 1404.2 | Metal, glass and panel coverings | Aluminum siding **0.48 mm**; steel (approved corrosion resistant) **0.37 mm**; structural glass **8.73 mm**; glass-fiber reinforced concrete panels **9.525 mm**; porcelain tile **3.125 mm** | Those coverings specified | Aluminum siding also AAMA 1402 per 1403.5.1; metal veneer running text uses **0.4 mm** sheet steel in 1404.11 | Conditional | Coordinate Table 1404.2 thickness with 1404.11 metal-veneer and 1404.12 glass-veneer install rules | Verified |
| Table 1404.2 | Vinyl siding thickness | Vinyl siding **0.88 mm** | Vinyl siding specified | None stated in the table row | Conditional | Use only if vinyl is confirmed at podium or low walls; still apply 1404.14 wind limits | Verified |
| Table 1404.2 | Fiber-cement siding thickness | Fiber-cement lap siding **6.35 mm**; fiber-cement panel siding **6.35 mm** | Fiber-cement siding specified | Note e is referenced on both rows but the note text is missing from the extract | Conditional | Verify published note e before relying on the fiber-cement thickness rows | Verify source |
| Table 1404.2 | Stucco coat thicknesses | Three-coat and two-coat stucco/exterior cement plaster rows are concatenated; coat thicknesses over metal plaster base, unit masonry and concrete are not recoverable | Stucco or exterior cement plaster specified | Do not invent coat thicknesses | Conditional | Verify the published Table 1404.2 stucco rows before specifying plaster coats; Chapter 25 still governs cement plaster | Verify source |

## 7. Vapor retarders

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1404.3 | Interior vapor retarder | Classify materials per Table 1404.3(1). Provide an interior-side vapor retarder on frame walls per Tables 1404.3(2) and 1404.3(3), or an approved hygrothermal design. Climate zone from IECC Chapter 3 (SBC 601/SBC 602). Class I interior plus Class I exterior requires an approved design | Frame walls | Exception 1: basement walls. Exception 2: below-grade portion of any wall. Exception 3: construction where moisture accumulation/condensation/freezing will not damage materials. Exception 4: Class I and II retarders with vapor permeance greater than **1 perm** (ASTM E96 Procedure B) permitted on the interior of any frame wall in all climate zones | Conditional | Apply to framed exterior walls; concrete/masonry backup may fall under Exception 3 only if demonstrated | Verified |
| 1404.3 | Class II with exterior foam | Where a Class II interior retarder is combined with foam plastic insulating sheathing as continuous insulation on the exterior, the CI shall comply with Table 1404.3(4) and the Class II retarder shall have vapor permeance greater than **1 perm** (ASTM E96 Procedure B) | Class II interior + exterior foam CI on frame walls | Table 1404.3(4) R-values are OCR-destroyed and are not adopted | Conditional | Do not issue CI R-values from Table 1404.3(4) until the published table is checked | Verify source |
| Table 1404.3(1) | Vapor-retarder classes | Class I: perm rating **less than or equal to 0.1**. Class II: **greater than 0.1 and less than or equal to 1.0**. Class III: **greater than 1.0 and less than or equal to 10** | Vapor-retarder classification | Listed deemed-to-comply materials (polyethylene/foil; kraft-faced batts/paint; latex/enamel paint) as tabled | Direct | Identify the interior finish/retarder class on the wall assembly schedule | Verified |
| Table 1404.3(2) | Interior class by climate zone | Zones **1 and 2**: Class I not permitted, Class II not permitted, Class III permitted. Zone **3**: Class I not permitted, Class II permitted, Class III permitted. Zone **4** except Marine 4: Class I not permitted, Class II permitted, Class III per Table 1404.3(3). Marine **4** and Zones **5–8**: Class I permitted, Class II permitted, Class III per Table 1404.3(3) | Interior vapor retarder on frame walls | Footnote a also points to 1404.3.1 and 1404.3.2 | Conditional | Select the row only after the SBC 601/602 climate zone is locked | Verified |
| Table 1404.3(3) | Class III continuous insulation | Zone **4**: CI **R ≥ 0.44** over **50 mm × 100 mm** wall or **R ≥ 0.66** over **50 mm × 150 mm**, or listed vented cladding. Zone **5**: **R ≥ 0.88** / **R ≥ 1.32**. Zone **6**: **R ≥ 0.88** / **R ≥ 1.32**. Zone **7**: **R ≥ 1.32** / **R ≥ 1.32**. R-values are **K·m²/W** | Class III interior retarder in those zones | Vented cladding includes vinyl lap, polypropylene, horizontal aluminum, brick veneer with airspace, and other approved vented claddings. Insulation for this table does not supersede SBC 601/602 thermal envelope | Conditional | Use vented-cladding or CI branch on framed walls only; do not treat these R-values as the energy-code minimum | Verified |
| Table 1404.3(3) | Zone 8 Class III CI | Zone 8 CI cells both read **R ≥ 2.64** over **50 mm × 100 mm**; the **50 mm × 150 mm** pairing is unresolved | Class III in Zone 8 | Not a design-release value | Conditional | Verify published Zone 8 cells before any Class III CI in that zone | Verify source |
| 1404.3.1–1404.3.2 | Spray-foam Class III moisture control | Spray foam with maximum permeance **1.5 perms** at installed thickness on the interior cavity side of WSP, fiberboard, insulating sheathing or gypsum may satisfy Table 1404.3(3) CI where its R-value meets or exceeds the tabulated CI. Combined spray-foam and CI R-values may be counted toward that CI requirement | Class III compliance via cavity spray foam | Does not replace SBC 601/602 thermal checks | Conditional | Record spray-foam perm and R-value on the assembly data sheet if this hybrid path is used | Verified |

## 8. Flashing, weeps and adhered veneer base

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1404.4 | Flashing locations | Install flashing to prevent moisture entering the wall or to redirect it to the finish or to a 1403.2 WRB that is part of 1402.2 drainage. Required at door and window perimeters, penetrations and terminations, wall/roof intersections, chimneys, porches, decks, balconies and similar projections, and built-in gutters. Projecting-flange flashing on both sides and ends of copings, under sills and continuously above projecting trim. Self-adhered fenestration flashings: AAMA 711. Fluid-applied opening flashings: AAMA 714 | Exterior wall openings, penetrations and terminations | Tested 1402.2 Exception 2 barrier details may substitute where that path is used | Direct | Detail flashing at every listed condition on wall sections, window/door types and balcony/roof junctions | Verified |
| 1404.4.2 | Anchored-veneer weeps | Flashing and weep holes in 1404.6 anchored veneer not more than **250 mm** above finished ground level above the foundation wall or slab. At other supports (structural floors, shelf angles, lintels), flashing and weeps in the first course of masonry above the support | Anchored masonry veneer | None stated | Conditional | Dimension foundation weeps and every shelf-angle/lintel flashing course on masonry elevations | Verified |
| 1404.10.1.2.1 | Adhered-veneer foundation screed | Corrosion-resistant screed or flashing minimum **0.5 mm** or **26 gage** galvanized or plastic, minimum vertical attachment flange **90 mm**, extending not less than **25 mm** below the foundation plate line on exterior stud walls. WRB lapped over the exterior of the attachment flange | Adhered masonry veneer on exterior stud walls | Also comply with 1404.4 | Conditional | Show weep-screed gage, flange and extension on the base-of-wall detail | Verified |
| 1404.10.1.3 | Adhered-veneer clearances | On exterior stud walls, adhered masonry veneer not less than **100 mm** above earth, **50 mm** above paved areas, or **12.5 mm** above exterior walking surfaces supported by the same foundation as the wall | Adhered masonry veneer on stud walls | None stated | Conditional | Dimension veneer-to-grade and veneer-to-paving clearances on base details | Verified |
| 1404.10.1.4.2–1404.10.1.4.3 | Adhered lath and mortar beds | Nominal **12.5 mm** scratch coat encapsulating lath, scored horizontally. Nominal **12.5 mm** setting bed worked to a nominal **9 mm** bed after units are applied. Mortar per 2103 and 2512.2 | Adhered masonry veneer installed with lath and mortar | Direct-to-masonry/concrete path per 1404.10.1.5 / 2510.7 | Conditional | Specify scratch and setting-bed thicknesses on the adhered-veneer specification | Verified |
| 1404.10.2 | Exterior porcelain tile limits | Units weighing more than **0.17 kN/m²**: maximum **1200 mm** any face dimension, **0.8 m²** face area, and not more than **0.30 kN/m²**. Units **0.17 kN/m²** or less: maximum **1800 mm** any face dimension and **1.6 m²** face area. Adhere to an approved backing system | Exterior adhered porcelain tile | None stated | Conditional | Check unit weight, edge length and area on the tile schedule before facade use | Verified |

## 9. Combustible cladding on Types I–IV

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1405.1.1 | Combustible covering area and height | Combustible exterior wall coverings shall not exceed **10 percent** of an exterior wall surface area where fire separation distance is **1500 mm** or less, and shall be limited to **12 m** in height above grade plane | Types I, II, III and IV construction | Plastics complying with Chapter 26 are excepted from 1405.1. FRTW complying with 2303.2 for exterior installation is not limited in wall area where FSD is **1500 mm** or less and is permitted up to **18 m** above grade plane regardless of FSD. Wood veneers also comply with 1404.5 | Direct | Keep combustible cladding (other than qualifying FRTW) off the tower shaft above **12 m**; map FSD versus combustible percentage on each elevation | Verified |
| 1405.1.1.1 | NFPA 268 ignition | Where 1405.1.1 permits combustible exterior wall coverings, test in accordance with NFPA 268 | Combustible covering on Types I–IV | Exception 1: wood or wood-based products. Exception 2: other combustible materials covered with an exterior weather covering, other than vinyl sidings, included in and complying with Table 1404.2 thicknesses. Exception 3: aluminum minimum thickness **0.5 mm** | Conditional | Require NFPA 268 for combustible finishes that are not wood, Table 1404.2-covered (non-vinyl), or **0.5 mm** aluminum | Verified |
| 1405.1.1.1.1 | Close-range ignition | Where FSD is **1.5 m** or less, combustible exterior wall coverings shall not exhibit sustained flaming as defined in NFPA 268 | Combustible covering at FSD **1.5 m** or less | None stated beyond 1405.1.1.1 exceptions | Conditional | Record the NFPA 268 no-sustained-flaming result on close FSD elevations | Verified |
| 1405.1.1.1.2 | Reduced-flux ignition table | For FSD greater than **1.5 m**, covering permitted if exposed to a reduced incident radiant heat flux per NFPA 268 without sustained flaming. Minimum FSD from Table 1405.1.1.1.2 based on the maximum tolerable flux that does not cause sustained flaming | Combustible covering at FSD greater than **1.5 m** | Table 1405.1.1.1.2 is not present in the attached extract. Commentary flux/distance examples are not adopted | External verification | Do not adopt a flux-versus-FSD pair until the published table is verified | Verify source |
| 1405.1.2 | Combustible covering at wall top | Combustible exterior wall coverings along the top of exterior walls shall be completely backed up by the exterior wall and shall not extend over or above the top of the exterior wall | Combustible covering at parapet/wall top | None stated | Direct | Stop combustible cladding at the wall top; do not project it as an unbacked cornice above the wall | Verified |
| 1405.1.3 | Furred combustible cavity | Where combustible covering is furred out and forms a solid surface, the distance between the back of the covering and the exterior wall shall not exceed **41 mm**. The concealed space shall be fireblocked per Section 718 | Furred combustible covering forming a solid surface | Distance may exceed **41 mm** where the concealed space is not required to be fireblocked by Section 718. Section 718 values are not imported | Conditional | Limit rainscreen cavity behind combustible cladding to **41 mm** unless a 718 exception is documented | Verified |

## 10. Selected veneers

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1404.5 | Wood veneer on Types I–IV | Not less than **25 mm** nominal thickness, **10 mm** exterior hardwood siding, or **9 mm** exterior-type wood structural panels or particleboard. Height not more than **12 m** above grade (**18 m** where fire-retardant-treated wood is used). Attached to or furred from noncombustible backing with the required fire-resistance rating. Open or spaced wood veneers without concealed spaces shall not project more than **600 mm** | Wood veneer on Type I, II, III or IV walls | None stated beyond the FRTW height increase | Conditional | Confine wood veneer to the stated height band and show projection and noncombustible backing on details | Verified |
| 1404.6–1404.6.2 | Anchored masonry veneer | Comply with 1404.6 through 1404.9 and SBC 305 Sections 12.1 and 12.2. Chapter 14 anchored veneers are not required to meet SBC 305 Article 3.3 F1 tolerances. Seismic Design Category C, D, E or F: SBC 305 Section 12.2.2.11 | Anchored masonry veneer | SBC 305 numeric detailing is not imported | Conditional | Note SBC 305 as the veneer design standard; keep Chapter 14 flashing/weep and thickness checks on the drawings | Verified |
| 1404.7 Item 1 | Stone veneer on masonry/concrete | Units not exceeding **250 mm** thick. Ties not less than **2.7 mm** wire; loop legs not less than **150 mm**; eyes **300 mm** maximum on center both ways; **2.7 mm** wire tie for every **0.2 m²**; tie legs not less than **375 mm** with last **50 mm** bent; **25 mm** minimum cement grout between backing and veneer | Anchored stone veneer on concrete or masonry backing | None stated | Conditional | Put tie size, spacing, grout thickness and unit cap thickness on the stone-veneer typical | Verified |
| 1404.7 Items 2–3 | Stone veneer on studs | **50 by 50 mm**, **1.6 mm** mesh; **two** WRB layers; studs not more than **400 mm** on center; mesh fasteners **100 mm** on center and **200 mm** into plates/tracks; wood: **50 mm** nails with **30 mm** penetration; steel: #8 screws with not fewer than **three** exposed threads; **2.7 mm** tie every **0.2 m²** with **375 mm** legs and **50 mm** bends; **25 mm** grout; steel studs minimum bare thickness **1 mm** | Anchored stone veneer on wood or cold-formed steel studs | Page split after “minimum 30” continues as **30 mm** penetration | Conditional | Use the stud-backing typical only if stone is on framed walls; show two WRB layers and grout thickness | Verified |
| 1404.8 | Slab-type stone veneer | Units not exceeding **50 mm** thick; dowels in the middle third of edges, not more than **600 mm** apart around the periphery, not fewer than **four** ties per unit; unit area not more than **2 m²**. Loose dowel holes not more than **1.6 mm** oversize, countersink diameter and depth equal to **twice** the dowel diameter. Ties resist **two times** the veneer weight; sheet-metal ties not smaller than **0.853 by 25 mm**; wire not smaller than **3.70 mm** | Anchored slab marble, travertine, granite or similar | None stated | Conditional | Limit slab size and show four-edge dowel spacing on each unit type | Verified |
| 1404.9 | Terra cotta veneer | Units not less than **40 mm** thick; dovetail webs approximately **200 mm** on center. Anchors not less than No. **8** gage at the top of each piece in bed joints not less than **300 mm** nor more than **450 mm** on center, secured to **6 mm** pencil rods. Facing set not less than **50 mm** from backing, solid-filled with Portland cement grout and pea gravel. Ties support the full weight of the veneer in tension | Anchored terra cotta or ceramic units | None stated | Conditional | Show **50 mm** grouted cavity, web spacing and bed-joint anchor spacing on the terra-cotta typical | Verified |
| 1404.11–1404.11.1 | Metal veneer | Sheet steel not less than **0.4 mm** nominal thickness. Fastenings or ties not more than **600 mm** vertically or horizontally; units exceeding **0.4 m²** have not fewer than **four** attachments per unit. Attachments not less than W **1.7** wire. Design attachments for Chapter 16 / SBC 301 wind (outbound) | Exterior metal veneer | Corrosion-resistant or porcelain-enamel protection required | Conditional | Dimension fastener grid and panel area on metal-panel shop drawings | Verified |
| 1404.12–1404.12.2 | Glass veneer size | Single section not more than **1.0 m²** where not more than **4500 mm** above sidewalk/grade, and not more than **0.56 m²** where more than **4500 mm** above that level. Length or height not more than **1200 mm**. Thickness not less than **8 mm** | Thin exterior structural glass veneer | None stated | Conditional | Check each glass-veneer unit area, edge and thickness against height above grade | Verified |
| 1404.12.3–1404.12.6 | Glass veneer support | At least **50 percent** of each unit bonded by mastic **6 mm** to **16 mm** thick. At sidewalk: metal molding, glass **6 mm** above highest sidewalk point. Above bulkhead or more than **900 mm** above sidewalk: nonferrous shelf angles not less than **1 mm** thick and **50 mm** long, not fewer than **two** per unit. Horizontal joints not less than **1.6 mm**; expansion joints not less than **6 mm** where abutting nonresilient material. Above show-window heads or more than **3600 mm** above sidewalk: mechanical fastenings at each edge or four corners in addition to mastic and shelf angles | Thin exterior structural glass veneer | Building official may approve other jointing | Conditional | Combine mastic thickness, shelf angles and mechanical fixings on the glass-veneer section by height zone | Verified |

## 11. Light cladding at podium

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1404.14 | Vinyl siding wind pressure | Vinyl siding ASTM D3679 permitted where design wind pressure per 1609 does not exceed **1.45 kN/m²**. Where pressure exceeds **1.45 kN/m²**, tests or calculations indicating Chapter 16 compliance shall be submitted | Vinyl siding specified | Manufacturer instructions may control fasteners | Conditional | Do not use the **1.45 kN/m²** deemed-to-comply path on a high-rise wind exposure without Chapter 16 evidence | Verified |
| 1404.14.1.1–1404.14.1.3 | Vinyl siding fasteners | Corrosion-resistant nails, head not less than **7.9 mm**, shank not less than **3.18 mm**, penetration not less than **32 mm** into nailable substrate. Cold-formed steel: not fewer than **three** exposed threads. Spacing not greater than **400 mm** for horizontal siding and **300 mm** for vertical siding, fasteners in the middle third of nail-hem slots | Vinyl siding on wood or CFS | Approved manufacturer instructions may specify otherwise | Conditional | Put fastener size, penetration and spacing on the vinyl typical if used at podium | Verified |
| 1404.16–1404.16.2 | Fiber-cement siding | ASTM C1186 Type A minimum Grade II (or ISO 8336 Category A minimum Class 2). Wood stud nails penetrate not less than **25 mm**. CFS screws not fewer than **three** exposed full threads. Lap siding maximum width **300 mm**, lapped minimum **32 mm** | Fiber-cement panel or lap siding | Manufacturer instructions may specify otherwise | Conditional | Show lap, joint protection and fastener penetration on fiber-cement details | Verified |
| 1403.12.2 | Polypropylene siding FSD | Fire separation distance between a building with polypropylene siding and the adjacent building not less than **3 m** | Polypropylene siding used | Flame-spread specimen must remain in position during ASTM E84 or UL 723 per 1403.12.1 | Conditional | Do not place PP siding on walls with FSD under **3 m** | Verified |
| 1404.18 | Polypropylene siding wind/height | Limited to areas where Chapter 16 wind speed does not exceed **45 m/s** and building height is less than or equal to **12 m** in Exposure C. Where wind exceeds **45 m/s** or height exceeds **12 m**, tests or calculations indicating Chapter 16 compliance shall be submitted | Polypropylene siding specified | Manufacturer installation instructions still apply | Conditional | Treat PP siding as a low-height product; the tower shaft exceeds the **12 m** deemed-to-comply height | Verified |

## 12. Metal composite materials (MCM)

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1406.9 | General MCM surface burning | Unless otherwise specified, MCM flame spread index **75** or less and smoke-developed index **450** or less, ASTM E84 or UL 723, maximum thickness intended for use | MCM used | Types I–IV use the stricter 1406.10.1 indices | Conditional | Record E84/UL 723 indices at the installed thickness on the MCM specification | Verified |
| 1406.10 | MCM height split | Types I–IV: comply with 1406.10.1 and 1406.10.2 for installations up to **12 m** above grade plane. Comply with 1406.10.1 through 1406.10.3 for installations greater than **12 m** above grade plane | MCM on Type I, II, III or IV | Type V permission in 1406.11 is omitted here as not typical for the tower shaft | Direct | Treat tower MCM as the greater-than-**12 m** path, including NFPA 285 | Verified |
| 1406.10.1 | Types I–IV MCM surface burning | Flame spread index not more than **25** and smoke-developed index not more than **450**, maximum thickness intended for use, ASTM E84 or UL 723 | MCM on Types I–IV | None stated | Direct | Specify FSI **25** / SDI **450** for tower MCM, not the general **75** / **450** pair | Verified |
| 1406.10.2 | MCM thermal barrier | Separate MCM from the interior by **12.5 mm** gypsum wallboard or a material meeting both NFPA 275 Temperature Transmission and Integrity Fire Tests | MCM on Types I–IV | Exception 1: MCM system specifically approved from NFPA 286 with 803.1.1.1 criteria, UL 1040 or UL 1715, maximum thickness, with typical seams/joints. Exception 2: MCM as balcony/projection elements, architectural trim or embellishments | Direct | Show the **12.5 mm** thermal barrier or a listed exception on the MCM wall section | Verified |
| 1406.10.3 | MCM NFPA 285 | MCM system tested to and complying with NFPA 285, MCM in the maximum thickness intended for use | Types I–IV MCM greater than **12 m** above grade plane | None stated in this section | Direct | Require an NFPA 285 listing for the full MCM wall assembly at maximum thickness | Verified |
| 1406.8 | MCM on rated walls | Where MCM is used on exterior walls required to have a fire-resistance rating per Section 705, submit evidence that the required rating is maintained | MCM on a fire-resistance-rated exterior wall | Exception: MCM without foam plastic, on the outer surface, attachments not penetrating through the entire exterior wall assembly | Conditional | Coordinate rated-wall listings with Chapter 7; do not import Table 705 values here | Verified |
| 1406.12 | MCM with foam | Where MCM systems are in an exterior wall envelope containing foam plastic insulation, the envelope shall also comply with Section 2603 | Foam and MCM in the same envelope | Chapter 26 values are not imported | Conditional | Flag any foam + MCM wall as a Chapter 26 assembly, not MCM-only | Verified |

## 13. Exterior insulation and finish systems (EIFS)

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1407.2–1407.4 | EIFS performance | Construct EIFS to ASTM E2568. Framing/substrate resist Chapter 16 loads. EIFS complies with 1402 weather resistance and manufacturer instructions | EIFS specified | Special inspections per 1704.2 and 1705.17 | Conditional | List ASTM E2568 and Chapter 17 special inspections on the EIFS specification | Verified |
| 1407.4.1 | EIFS with drainage | Average minimum drainage efficiency **90 percent** per ASTM E2273. Required on framed walls of Type V construction, Group R-1, R-2, R-3 and R-4 occupancies | Type V framed walls in Group R, or EIFS with drainage otherwise specified | WRB for drainage EIFS: 1403.2 or ASTM E2570 | Conditional | If any Type V framed R-2 wall exists (podium/townhouse-style), specify drainage EIFS at **90 percent**; do not assume Type V for the tower shaft | Verified |

## 14. High-pressure laminates (HPL)

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1408.9 | General HPL surface burning | Unless otherwise specified, HPL flame spread index **75** or less and smoke-developed index **450** or less, ASTM E84 or UL 723, minimum and maximum thicknesses intended for use | HPL used | Types I–IV use 1408.10 or the 1408.11 alternate | Conditional | Record min-and-max thickness burns on the HPL specification | Verified |
| 1408.10–1408.10.1 | Types I–IV HPL surface burning | Comply with 1408.10.1 through 1408.10.4, or with 1408.11. HPL flame spread index not more than **25** and smoke-developed index not more than **450**, min and max thicknesses, ASTM E84 or UL 723 | HPL on Type I, II, III or IV | 1408.11 alternate is a separate height/area path | Direct | Default the tower to 1408.10 (including NFPA 285), not the **12 m** alternate | Verified |
| 1408.10.2–1408.10.3 | HPL thermal barrier | Separate HPL from the interior by **12.5 mm** gypsum wallboard or NFPA 275 (both tests). Thermal barrier not required where the HPL system is approved from NFPA 286 with 803.1.1.1, UL 1040 or UL 1715 (min and max thicknesses, typical details), or where HPL is balcony/projection, trim or embellishment | HPL on Types I–IV | Listed large-scale tests or trim/balcony use | Direct | Show the **12.5 mm** barrier or a documented 1408.10.3 exception | Verified |
| 1408.10.4 | HPL NFPA 285 | HPL system tested to and complying with NFPA 285, HPL in the minimum and maximum thicknesses intended for use | Types I–IV HPL on the 1408.10 path | 1408.11 alternate may omit 1408.10.1–1408.10.4 if its limits are met | Direct | Require NFPA 285 at both min and max HPL thickness for tower installations | Verified |
| 1408.11–1408.11.1.2 | HPL 12 m alternate | HPL not required to comply with 1408.10.1–1408.10.4 where installed up to **12 m** above grade plane and: FSD **1.5 m** or less, HPL area not more than **10 percent** of the exterior wall surface; or FSD greater than **1.5 m**, no HPL area limit | Alternate to full 1408.10 on Types I–IV | Height still capped at **12 m** on this path. Type V permission in 1408.12 omitted as not typical for the tower shaft | Conditional | Use the alternate only for HPL that stays at or below **12 m**; tower elevations above that remain on 1408.10 | Verified |
| 1408.8 | HPL on rated walls | Where HPL is used on exterior walls required to have a fire-resistance rating per Section 705, submit evidence that the required rating is maintained | HPL on a fire-resistance-rated exterior wall | Exception: HPL without foam plastic, outer surface, attachments not through the entire wall | Conditional | Coordinate rated-wall evidence with Chapter 7 | Verified |
| 1408.13 | HPL with foam | HPL systems containing foam plastic insulation shall also comply with Section 2603 | Foam in the HPL system/envelope | Chapter 26 values are not imported | Conditional | Flag foam-cored HPL as a Chapter 26 assembly | Verified |

## 15. Outbound controls

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1402.3 | Structural loads | Exterior walls and associated openings shall resist superimposed loads required by Chapter 16 | All exterior walls and openings | No Chapter 16 values imported | External verification | Size cladding, anchors and openings from Chapter 16 / SBC 301, not from this matrix | Verified |
| 1402.4 | Fire resistance and openings | Exterior walls fire-resistance rated as required by other sections, with opening protection as required by Chapter 7 | Exterior walls | Commentary names Tables 601, 602 and 705.8; those values are not in this chapter’s code text and are not adopted | External verification | Pull ratings and unprotected-opening percentages from Chapters 6 and 7 | Verified |
| 1402.6–1402.7 | Flood resistance | In flood hazard areas, exterior walls below the 1612 elevation use flood-damage-resistant materials. In coastal high-hazard areas and coastal A zones, electrical, mechanical and plumbing components shall not be mounted on or penetrate breakaway exterior walls | Flood hazard / coastal A / coastal high-hazard designation | Section 1612 elevations and ASCE 24 are not imported | Conditional | Confirm 1612 flood designation before detailing below-elevation walls | Verified |
| 1403.3–1403.8 | Material chapters | Wood walls: Chapter 23. Masonry: Chapter 21. Steel: Chapter 22. Aluminum: Chapter 20. Concrete: Chapter 19. Glass-unit masonry: Chapter 21. Plastic panels: Chapter 26 plus Chapter 16 wind | Those materials used | No outbound chapter values imported | External verification | Keep material design in the named chapters; use Chapter 14 for covering, WRB and combustible-cladding checks | Verified |
| 1403.13–1403.14 | Foam plastic and through-foam attachment | Foam plastic insulation in exterior wall covering assemblies shall comply with Chapter 26. Coverings attached through foam plastic insulating sheathing shall comply with 2603.11, 2603.12 or 2603.13 | Foam in the wall or cladding fastened through foam sheathing | Chapter 26 numeric attachment/NFPA 285 rules are not imported | External verification | Route foam walls and through-foam fasteners to Chapter 26 | Verified |
| 1404.13–1404.13.1 | Exterior windows and doors | Windows and doors in exterior walls conform to testing and performance in Section 1705.9. Install per approved manufacturer instructions; fastener size and spacing from those instructions based on maximum loads and spacing used in the tests | Exterior fenestration | No 1705.9 pressures imported | External verification | Put 1705.9 test reports on the fenestration schedule; keep 1404.4 flashing in the wall details | Verified |
| 1404.15 | Cement plaster | Exterior cement plaster conforms to Chapter 25 | Stucco / cement plaster | Gypsum plaster is not an exterior covering in this clause | External verification | Detail stucco coats from Chapter 25 after verifying Table 1404.2 stucco rows | Verified |
| 1404.17 | Weatherboard fastening | Secure weather boarding and wall coverings with approved corrosion-resistant fasteners per Table 2304.10.2 or approved manufacturer instructions, except where wood sheathing is not less than **25 mm** nominal thickness | Weather boarding / wall coverings | Table 2304.10.2 nail schedules are not imported | External verification | Use Chapter 23 nailing tables for wood coverings | Verified |
| 1409.1 | Plastic composite decking | Exterior deck boards, stair treads, handrails and guards of plastic composites, including plastic lumber, shall comply with Section 2612 | Plastic composite decking, treads, handrails or guards | Section 2612 values are not imported | Conditional | Route balcony deck boards and composite guards to 2612 | Verified |

## 16. Project-use controls

1. Use **Verified** rows for initial facade coordination after the row trigger, construction type and cladding system are confirmed.
2. Treat every **Verify source** row as a design hold point. No affected value is to be placed in issued-for-approval drawings without a published-source check.
3. Do not import Chapter 7 opening percentages, Chapter 16 wind pressures, Chapter 26 foam/NFPA 285 acceptance criteria, SBC 305 veneer tables, or SBC 601/602 climate-zone assignments.
4. Do not treat the occupied-floor height above **23 m** as permission to run combustible cladding, vinyl, or polypropylene up the tower shaft. Types I–IV combustible covering remains capped at **12 m** (**18 m** FRTW) unless a different Chapter 14 path (MCM/HPL NFPA 285) is documented.
5. Do not use Table 1404.3(4) R-values or Table 1405.1.1.1.2 flux/FSD pairs from commentary or memory.
6. Record construction type, cladding, WRB combustibility, foam, climate zone and FSD in the project Golden Thread. This matrix is not evidence of SCD NOC or stamped compliance.

## 17. Coverage summary

Internal inventory of the attached Chapter 14 extract (numbered code, exceptions, tables, footnotes; commentary excluded). Row-level records are not published.

- **Inventory scope:** numbered code, exceptions, tables, footnotes (commentary excluded)
- **Total independently checkable numeric records:** 225
- **Verified:** 213
- **Verify source:** 12
- **Numeric records in Section 1401:** 0
- **Numeric records in Section 1409:** 0 (outbound to 2612 only)

### Counts by top-level section

| Top-level section | Records |
|---|---:|
| 1401 | 0 |
| 1402 | 15 |
| 1403 | 3 |
| 1404 | 180 |
| 1405 | 10 |
| 1406 | 7 |
| 1407 | 1 |
| 1408 | 9 |
| 1409 | 0 |

### Appended-table coverage

| Appended table | Records | Verify source records |
|---|---:|---:|
| Table 1404.2 | 36 | 8 |
| Table 1404.3(1) | 5 | 0 |
| Table 1404.3(2) | 0 | 0 |
| Table 1404.3(3) | 10 | 2 |
| Table 1404.3(4) | 1 | 1 |
| Table 1405.1.1.1.2 | 1 | 1 |

Coverage cross-check against `SBC 201 Chapter 14 Exterior Walls (2024)_CS.md` was topics-only: weather envelope and WRB; vapor retarders; combustible cladding on Types I–IV; MCM/HPL/EIFS/foam. No CS.md value was copied into a matrix cell. Figure 1404.3(1) climate maps, Figure 1404.3(2) IECC thermal definitions, and other commentary figures were not inventoried.

## 18. Unresolved-source register

Hold points for the 12 **Verify source** inventory records. Counts are record counts, not distinct numeric values. No value in this register is a design-release figure.

| Affected table / clause | Why unverified | Control note |
|---|---|---|
| Table 1404.2 stucco rows | 5 three-coat/two-coat thickness cells concatenated; coat thicknesses over metal plaster base, unit masonry and concrete not recoverable | Verify published plaster-coat thicknesses; do not invent coats. Chapter 25 still governs cement plaster |
| Table 1404.2 note e | 3 products (fiber-cement lap, fiber-cement panel, hardboard) cite note e; note e text is absent from the extract | Verify published note e before using those thickness rows as complete |
| 1404.3 / Table 1404.3(4) | Entire continuous-insulation + Class II table is OCR-destroyed (`R-value ≥` loop); no cell adopted | Do not reconstruct CI R-values. Lock climate zone from SBC 601/602, then read the published table |
| Table 1404.3(3) Zone 8 | 2 CI cells both print **R ≥ 2.64** over **50 mm × 100 mm**; **50 mm × 150 mm** pairing unresolved | Verify published Zone 8 row before Class III CI in that zone |
| Table 1405.1.1.1.2 | Table cited by 1405.1.1.1.2 is not in the extract; commentary **9.5 kW/m² → 30 m** example is not adopted | Verify published flux-versus-FSD table before any reduced-flux NFPA 268 placement |
