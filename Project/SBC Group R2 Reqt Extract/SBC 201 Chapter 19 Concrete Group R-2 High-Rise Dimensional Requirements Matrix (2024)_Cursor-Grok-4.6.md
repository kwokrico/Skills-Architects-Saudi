# SBC 201 Chapter 19 Concrete — Group R-2 High-Rise Dimensional Requirements Matrix (2024)

## 1. Document metadata and use limitation

- **Project basis:** Riyadh, Saudi Arabia; Group R-2 residential high-rise; an occupied floor is stated to be more than 23 m above the relevant reference level.
- **Deliverable tier:** Project-use matrices in Sections 1–12 (design-check rows, not pasted inventory), plus a coverage summary and unresolved-source register. The full row inventory is not published.
- **Code/source basis:** SBC 201 (2024), Chapter 19, source file `Reference\SBC 201 2024\source_reference\Chapter_19 — CONCRETE.txt`.
- **Extraction audit:** Skill-finetune re-run. Project-use rows follow the chapter-extract row contract (noun-phrase checks, bold SI values, building-language triggers, named exceptions, check-specific actions). Internal inventory: **33** independently checkable numeric records (**33** Verified, **0** Verify source). Non-numeric OCR hold points are listed in the register and are not design-release values. No pre-skill Chapter 19 baseline is published beside this file.
- **Model:** Cursor Grok 4.6.
- **Prepared:** 2026-08-27.
- **Status:** Source-only architectural advisory matrix for design coordination. It is not a stamped compliance statement, structural design, SCD NOC, SBPS approval, legal opinion, or permission to construct.
- **Outbound-source rule:** No value in this matrix has been imported from SBC 304, SBC 301, SBC 302, Chapter 17, Section 2206, Chapter 7 / Table 721.1(2), ACI 117, ACI ITG-7, ACI 506R, PCI MNL 128, ASTM E2634, commentary examples, or the existing chapter summary. Where Chapter 19 sends the user elsewhere, this matrix records the dependency without supplying the outbound value.

### Scope and assumptions

1. Group R-2 and high-rise status are project statements, not independently verified classifications.
2. The exact Riyadh AHJ/permit pathway, project stage, fire-strategy status and SCD NOC status are unconfirmed; therefore this matrix does not conclude compliance.
3. Seismic Design Category is unconfirmed. Item 11 of 1901.5 (slab-on-grade as a structural diaphragm) applies only if the structure is assigned to SDC **D, E or F**.
4. Automatic sprinkler protection is not selected in this chapter extract. Chapter 19 does not branch on NFPA 13 versus 13R.
5. Building height, storey count, grade plane, basement/podium construction, mixed use and whether any slab on grade transmits vertical loads or lateral forces are unconfirmed.
6. Structural concrete design, durability classes, anchoring, materials and most member sizes live in **SBC 304**, not in this chapter. Section 1905 states that appropriate modifications have been reflected in **SBC 304-24**; this extract does not reprint those modifications.
7. 1901.7.1 says cast-in-place tolerances shall be “in accordance with this section” but the attached extract does not publish millimetre tolerances or name ACI 117 in the **code** paragraph (ACI 117 appears only in commentary). No commentary millimetres are adopted.
8. There are no appended tables in this chapter extract.

## 2. Legends

### Applicability

| Status | Meaning |
|---|---|
| **Direct** | Expected to govern the stated R-2 tower basis, subject to confirmed geometry and design data. |
| **Conditional** | Governs only when the stated feature, load, sprinkler branch or exception exists. |
| **Not typical** | Unrelated occupancy-only rule; omitted from this deliverable unless the gap register already opened that use. |
| **External verification** | Chapter 19 points to another section/code/standard, or the project/AHJ basis must be confirmed before use. |

### Source confidence

| Status | Meaning |
|---|---|
| **Verified** | Requirement and any stated numeric value were checked against unambiguous mandatory Chapter 19 source text. |
| **Verify source** | OCR, flattened table, page-split, or footnote attachment is unresolved. Not a design-release value. |

## 3. Project decision and gap register

| Decision / gap | Current project basis | Why it controls Chapter 19 application | Required project action |
|---|---|---|---|
| Structural engineer / SBC 304 | Unconfirmed companion design | 1901.2 charges structural concrete to this chapter **and SBC 304** as amended in 1905; this extract has no member sizes, covers, mix classes or anchor capacities | Issue an SBC 304 structural package; do not size concrete from Chapter 19 alone |
| Seismic Design Category | Unconfirmed | 1901.5 Item 11 requires a statement whether slab on grade is a structural diaphragm for SDC **D, E or F**; 1902.1.1 design displacement is outbound to SBC 301 12.8.6 | Lock SDC on the code datum sheet; show diaphragm/non-diaphragm SOG on structural drawings |
| Slab on grade role | Unconfirmed: architectural wearing slab vs structural diaphragm / collector | Non-structural SOG is limited here to 1904 and 1907; a load-path SOG must comply with the full chapter and SBC 304 | Structural engineer to classify every ground-supported slab |
| 1906.1 light-frame footings | Not applicable to this R-2 high-rise | Plain-concrete footing **150 mm** / **100 mm** projection is only for Group **R-3** and other occupancies **less than two stories** of light-frame construction | Do not apply 1906.1 to tower or typical podium foundations |
| Shotcrete use | Unconfirmed | Section 1908 numeric locks apply only if shotcrete is specified | Confirm whether shotcrete is used (repair, basement, landscape); if none, park 1908 as unused |
| Vapor-retarder AHJ exception | Unconfirmed | 1907.1 Exception 2 waives the retarder where approved based on local site conditions | Do not omit the retarder under enclosed floors without AHJ approval |
| Special inspections | Outbound to Chapter 17 | 1901.6 and 1903.2 send concrete SI/tests to Chapter 17; this extract has no SI frequency table | Coordinate Chapter 17 SI schedule with the concrete specification |
| CIP tolerance standard | 1901.7.1 charging incomplete in the extract | Code does not name ACI 117; commentary does. No millimetre tolerances are published here | Verify the published 1901.7.1 text before specifying CIP tolerances |
| Mixed-use podium | Unconfirmed | Does not change 1907 SOG thickness; may add GFRC cladding (1903.3) or ICF walls (1903.4) | Freeze cladding and forming systems; import PCI MNL 128 / ASTM E2634 only if used |
| NOC / stamped structural | Unconfirmed | Concrete design, SCD acceptance and construction tolerances cannot be concluded from this chapter extract | Engage the structural engineer of record before design freeze |

## 4. Scope and SBC 304 companion

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1901.1 | Chapter concrete scope | This chapter governs materials, quality control, design and construction of concrete used in structures | Concrete in the structure | None stated | Direct | Treat Chapter 19 as the charging chapter; send member design to the SBC 304 package | Verified |
| 1901.2 | Structural concrete companion | Structural concrete shall be designed and constructed in accordance with this chapter **and SBC 304** as amended in 1905 | Structural concrete | Slabs on grade that do **not** transmit vertical loads or lateral forces are governed here only by 1904 and 1907 | Direct | Keep a live SBC 304 structural specification; classify each SOG as structural or non-structural | Verified |
| 1901.3 | Anchoring to concrete | Anchoring to concrete shall be in accordance with **SBC 304** as amended in 1905 | Cast-in, post-installed expansion, undercut, screw and adhesive anchors | None stated | External verification | Schedule all concrete anchors to the SBC 304 anchorage specification; do not invent capacities here | Verified |
| 1901.4 | Composite steel-concrete design | Systems of structural steel acting compositely with reinforced concrete shall be designed in accordance with **Section 2206** | Composite steel-concrete systems | None stated | External verification | If composite slabs or beams are used, design them under Section 2206, not from this chapter | Verified |
| 1905.1 | SBC 304-24 modifications | Appropriate modifications has been reflected in **SBC 304-24** | Structural concrete using SBC 304 | None stated | External verification | Use the SBC 304-24 text as modified; do not reconstruct 1905 amendments from this extract | Verified |

## 5. Construction documents and inspections

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1901.5 | Concrete construction-document contents | Construction documents for structural concrete shall include the 1901.5 strength, grade, geometry, prestress, splice, joint and outbound **SBC 301** / **SBC 304 Chapter 26** information | Structural concrete construction documents | Item 11 is a separate SDC **D, E or F** statement | Direct | Put the 1901.5 checklist on the structural issue set | Verified |
| 1901.5 Item 11 | SDC slab-diaphragm statement | For structures assigned to Seismic Design Category **D, E or F**, the documents shall include a statement if slab on grade is designed as a structural diaphragm | SDC D, E or F | Not required by this item outside SDC D, E or F | Conditional | Once SDC is locked, state on the foundation drawings whether each SOG is a diaphragm | Verified |
| 1901.6 | Concrete special inspections | Special inspections and tests of concrete elements and concreting operations shall be as required by **Chapter 17** | Concrete elements and concreting operations | None stated in this chapter | External verification | Attach the Chapter 17 SI schedule to the concrete specification; do not invent frequencies here | Verified |
| 1903.2 | Materials special inspections | Where required, special inspections and tests shall be in accordance with **Chapter 17** | Concrete materials and testing where SI is required | None stated in this chapter | External verification | Align material testing with the same Chapter 17 programme as 1901.6 | Verified |

## 6. Tolerances

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1901.7 | Default structural tolerances | Where not indicated in construction documents, structural tolerances for concrete structural elements shall be in accordance with 1901.7 | Concrete structural elements without stated tolerances | None stated | Direct | State CIP and precast tolerances on the drawings so 1901.7 is not an unspoken default | Verified |
| 1901.7.1 | Cast-in-place concrete tolerances | Structural tolerances for cast-in-place concrete structural elements shall be in accordance with this section; the attached extract publishes **no millimetre limits** and does **not** name ACI 117 in the code paragraph | Cast-in-place concrete structural elements | Group R-3 detached one- or two-family dwellings; shotcrete | External verification | Verify the published 1901.7.1 text before specifying CIP tolerances; do not import ACI 117 millimetres from commentary | Verify source |
| 1901.7.2 | Precast concrete tolerances | Structural tolerances for precast concrete structural elements shall be in accordance with **ACI ITG-7** | Precast concrete structural elements | Group R-3 detached one- or two-family dwellings are not required to comply | External verification | If precast is used, specify ACI ITG-7; do not copy ITG-7 values into this matrix | Verified |

## 7. Terminology and special structural walls

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1902.1.1 | Design-displacement definition | Design displacement at each level shall be the total lateral deflection at that level calculated for the design earthquake using **Section 12.8.6 of SBC 301** | Seismic design displacement | None stated | External verification | Take storey displacements from the SBC 301 analysis; do not invent millimetres here | Verified |
| 1902.1.2 | Special structural wall | Special structural walls of cast-in-place or precast concrete shall comply with **SBC 304** Sections **18.2.4 through 18.2.8**, **18.10** and **18.11**, as applicable, in addition to ordinary wall requirements; where SBC 301 says “special reinforced concrete shear wall,” it means “special structural wall” | Special structural walls | Ordinary wall requirements still apply as applicable | External verification | Match wall type labels on structural drawings to SBC 304 special-wall clauses; do not import those clause values here | Verified |

## 8. Materials, GFRC and ICF

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1903.1 | Concrete materials and tests | Materials used to produce concrete, concrete itself and testing thereof shall comply with the applicable standards listed in **SBC 304** | Concrete materials and testing | None stated | External verification | Specify cements, aggregates, water, reinforcement and admixtures from the SBC 304 list | Verified |
| 1903.3 | GFRC materials standard | Glass fiber-reinforced concrete (GFRC) and the materials used in such concrete shall be in accordance with **PCI MNL 128** | GFRC | None stated | Conditional | If GFRC cladding or panels are used, specify PCI MNL 128; do not take fire ratings from this chapter | Verified |
| 1903.4 | Flat-wall ICF material | Insulating concrete form material used for forming flat concrete walls shall conform to **ASTM E 2634** | Flat-wall ICF systems | None stated | Conditional | If ICF walls are proposed, require ASTM E 2634 forms; typical R-2 high-rise CIP/precast does not use ICF | Verified |

## 9. Durability

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1904.1 | Structural concrete durability | Structural concrete shall conform to the durability requirements of **SBC 304** | Structural concrete | None stated | External verification | Assign SBC 304 exposure classes on the mix schedule; do not invent cover or w/c limits here | Verified |
| 1904.2 | Nonstructural concrete durability | The registered design professional shall assign appropriate durability requirements for nonstructural concrete | Nonstructural concrete | None stated | Direct | State durability for toppings, non-structural SOG and similar work on the specification, even though SBC 304 does not assign them here | Verified |

## 10. Slabs on grade

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1907.1 | Ground-supported slab and vapor retarder | Concrete floor slabs supported directly on the ground shall be **not less than 90 mm** thick, with a **150 microns (0.15 mm)** polyethylene vapor retarder, joints lapped **not less than 150 mm**, between base/subgrade and slab, or other approved equivalent methods or materials | Concrete floor slabs on the ground | Vapor retarder is not required for driveways, walks, patios and other flatwork that will not be enclosed later; or where approved based on local site conditions. Thickness has no stated exception | Direct | Show **90 mm** SOG with **150-micron** retarder and **150 mm** laps on enclosed ground-floor, basement and parking details | Verified |

## 11. Shotcrete

Apply this section only if shotcrete is specified. Except as modified here, shotcrete shall conform to this chapter for plain or reinforced concrete (1908.1). Do not adopt commentary millimetres (ACI 506R **50 mm** WWF, **750 mm** / **75 mm** preconstruction panels, **300 mm** joint taper, **66°C** steam, **5°C** curing).

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1908.1–1908.2 | Shotcrete proportions and strength | Shotcrete is mortar or concrete pneumatically projected at high velocity onto a surface; proportions shall allow suitable placement with the selected equipment and shall result in finished in-place hardened shotcrete meeting the strength requirements of this code | Shotcrete work | 1908 modifies this chapter; otherwise plain/reinforced concrete rules apply | Conditional | If shotcrete is used, submit a mix that meets the specified strength under 1908.10 testing | Verified |
| 1908.3–1908.4.3 | Shotcrete aggregate and reinforcement | Coarse aggregate, if used, shall **not exceed 19 mm**. Maximum reinforcement size is **Dia 16** bars unless preconstruction tests demonstrate adequate encasement of larger bars. **Dia 16** or smaller: minimum clearance between parallel bars **65 mm**. Larger bars where permitted: minimum clearance **six diameters**. Two curtains: nearer-nozzle curtain **12 bar diameters**, remaining curtain **six bar diameters**. Lap splices shall be noncontact with **50 mm** minimum clearance between bars | Shotcrete reinforcement placement | Building official may reduce required clearances where preconstruction tests show adequate encasement. Contact lap splices for support are permitted when approved from satisfactory preconstruction tests and the splice plane is perpendicular to the shotcrete surface | Conditional | Dimension bar size, parallel clearance and noncontact laps on the shotcrete placing drawing | Verified |
| 1908.4.4 | Shotcrete spirally tied columns | Shotcrete shall **not** be applied to spirally tied columns | Spirally tied columns | None stated | Conditional | Keep spiral columns as CIP or another permitted method; do not gun them | Verified |
| 1908.5 | Shotcrete preconstruction tests | Where required by 1908.4, a test panel shall be shot, cured, cored or sawn, examined and tested before the project starts; the panel shall reproduce the thickest and most congested area, shot at the same angle with the same nozzle, mix and equipment unless substitutes are approved; reports to the building official as specified in **Section 1704.5** | Preconstruction tests required by 1908.4 | Substitute equipment only if approved by the building official | Conditional | Do not import commentary **750 mm** / **75 mm** panel sizes; follow 1908.5 as written and 1704.5 for reporting | Verified |
| 1908.6–1908.8 | Shotcrete placement and joints | Rebound or accumulated loose aggregate shall be removed before placing initial or succeeding layers; rebound shall not be used as aggregate. Unfinished work shall not stand for more than **30 minutes** unless edges are sloped to a thin edge. Square joints are permitted for structural elements that will be under compression and for construction joints shown on the approved construction documents. Sloping and square edges shall be cleaned and wetted before placing additional material. In-place shotcrete with sags, sloughs, segregation, honeycombing, sand pockets or other obvious defects shall be removed and replaced; shotcrete above sags and sloughs shall be removed and replaced while still plastic | Shotcrete placement | Square joints only where 1908.7 permits them | Conditional | Limit cold joints to **30 minutes** or a sloped thin edge; do not reuse rebound; replace defective shotcrete. The extract’s “Before placing additional material are permitted” sentence is OCR-garbled — do not invent missing words | Verified |
| 1908.9–1908.9.2 | Shotcrete curing | During the curing periods specified, shotcrete shall be maintained **above 4°C** and in moist condition. Initial curing: continuously moist for **24 hours** after shotcreting is complete, or sealed with an approved curing compound. Final curing shall continue for **seven days** after shotcreting, or for **three days** if high-early-strength cement is used, or until the specified strength is obtained, using the initial-curing process or an approved moisture-retaining cover | Shotcrete curing | **Three-day** final-curing branch only with high-early-strength cement, or stop when specified strength is obtained | Conditional | Put **4°C**, **24 hours** and **seven days** / **three days** on the shotcrete curing specification; do not substitute commentary **5°C** or **66°C** | Verified |
| 1908.10–1908.10.3 | Shotcrete strength tests | Approved-agency tests on representative specimens water-soaked at least **24 hours** before testing. Maximum-size aggregate **larger than 9.5 mm**: not less than **three 75 mm** cores or **75 mm** cubes; test panels minimum **450 mm by 450 mm**. Aggregate **9.5 mm or smaller**: not less than **50 mm** cores or **50 mm** cubes; test panels minimum **300 mm by 300 mm**. Sampling at least **once each shift**, but not less than **one for each 40 m³**. Average of **three** cores **≥ 0.85f'c** with no single core **< 0.75f'c**; average of **three** cubes **≥ f'c** with no individual cube **< 0.88f'c**; retest erratic locations | Shotcrete strength acceptance | Specimens from in-place work or test panels. Panels shot in the same position, during the work, by the nozzlemen doing the work, and cured as the work | Conditional | Write the **9.5 mm** specimen/panel split, soak, frequency and **0.85f'c** / **0.75f'c** / **0.88f'c** acceptance into the QA specification | Verified |

## 12. Project-use controls

1. Use **Verified** rows for initial scoping after the row trigger and branch are confirmed.
2. Treat every **Verify source** row as a design hold point; no affected value is to be placed in issued-for-approval drawings without a published-source check.
3. Do not apply 1906.1 **150 mm** / **100 mm** plain-concrete footings to this R-2 high-rise.
4. Do not import SBC 304 covers, mix classes, anchor capacities, ACI 117 millimetres, ACI ITG-7 values, PCI MNL 128 details, ASTM E2634 tests, Chapter 17 SI frequencies, or commentary examples (**750 mm** panels, **50 mm** WWF, **300 mm** tapers, **66°C**, **5°C**).
5. Keep the published tokens **150 microns (0.15 mm)**, **4°C**, **Dia 16**, **0.85f'c**, **0.75f'c** and **0.88f'c** intact.
6. Record SDC, SOG structural role, shotcrete use and vapor-retarder AHJ decisions in the project Golden Thread; this matrix is not evidence of SCD NOC or stamped compliance.

## 13. Coverage summary

Internal inventory of the attached Chapter 19 extract (numbered code, exceptions, tables, footnotes; commentary excluded). Row-level records are not published.

- **Inventory scope:** numbered code, exceptions, tables, footnotes (commentary excluded)
- **Total independently checkable numeric records:** 33
- **Verified:** 33
- **Verify source:** 0
- **Appended tables:** none

### Counts by top-level section

| Top-level section | Records |
|---|---:|
| 1901 | 0 |
| 1902 | 0 |
| 1903 | 0 |
| 1904 | 0 |
| 1905 | 0 |
| 1906 | 3 |
| 1907 | 3 |
| 1908 | 27 |

Coverage cross-check against `SBC 201 Chapter 19 Concrete (2024)_CS.md` was topics-only: SBC 304 companion; SOG 1904/1907 versus structural SOG; 1906 light-frame footings not applied to R-2 high-rise; 1907 **90 mm** / **150 microns** / **150 mm** lap; GFRC fire ratings are not this chapter. No CS.md value was copied into a matrix cell.

## 14. Unresolved-source register

Hold points for project-use **Verify source** rows and OCR clauses that must not be repaired from memory. No value in this register is a design-release figure. Numeric inventory **Verify source** count remains **0**.

| Affected table / clause | Why unverified | Control note |
|---|---|---|
| 1901.7.1 | Code says CIP tolerances shall be “in accordance with this section” but the extract publishes no millimetre values and does not name ACI 117 in the code paragraph; ACI 117 appears only in commentary | Verify the published 1901.7.1 text. Do not import ACI 117 millimetres from commentary or memory |
| 1908.7 | After the square-joint permission, the extract repeats a garbled “Before placing additional material are permitted” before the clean-and-wet sentence | **30 minutes** and square-joint permission remain Verified. Do not invent the missing words or adopt commentary **300 mm** taper |
