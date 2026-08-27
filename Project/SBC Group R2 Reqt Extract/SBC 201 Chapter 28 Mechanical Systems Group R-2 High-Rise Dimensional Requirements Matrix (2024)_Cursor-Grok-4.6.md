# SBC 201 Chapter 28 Mechanical Systems — Group R-2 High-Rise Dimensional Requirements Matrix (2024)

## 1. Document metadata and use limitation

- **Project basis:** Riyadh, Saudi Arabia; Group R-2 residential high-rise.
- **Deliverable tier:** Project-use matrices in Sections 1–5 (design-check rows, not pasted inventory), plus a coverage summary and unresolved-source register. The full row inventory is not published.
- **Code/source basis:** SBC 201 (2024), Chapter 28, source file `Reference\SBC 201 2024\source_reference\Chapter_28 — MECHANICAL SYSTEMS.txt`.
- **Extraction audit:** Skill extract. Project-use rows follow the chapter-extract row contract (noun-phrase checks, bold published tokens, building-language triggers, named exceptions, check-specific actions). Internal inventory: **0** independently checkable numeric records (**0** Verified, **0** Verify source). Chapter 28 has no tables, exceptions, footnotes, or numeric cells.
- **Model:** Cursor Grok 4.6.
- **Prepared:** 2026-08-27.
- **Status:** Source-only architectural advisory matrix for design coordination. It is not a stamped compliance statement, mechanical design, SCD NOC, SBPS approval, legal opinion, or permission to construct.
- **Outbound-source rule:** No value in this matrix has been imported from SBC 501, SBC 1201, SBC 801, SBC 901, the International Property Maintenance Code, Chapter 21, commentary examples, Figure 2801.1, or the existing chapter summary. Where Chapter 28 sends the user elsewhere, this matrix records the dependency without supplying the outbound value.

### Scope and assumptions

1. Group R-2 and high-rise status are project statements, not independently verified classifications.
2. The exact Riyadh AHJ/permit pathway, project stage and SCD NOC status are unconfirmed; therefore this matrix does not conclude compliance.
3. Chapter 28 names **SBC 501** and **SBC 1201** together for design, construction, erection and installation. It does not assign either volume by occupancy and does not state whether fuel gas is present.
4. Automatic sprinkler protection, storey count, mixed-use podium and amenity program are unconfirmed. Chapter 28 itself does not branch on those facts; any such branching lives in the outbound mechanical, fuel-gas, fire-prevention or existing-building codes and is not reconstructed here.
5. Duct sizes, ventilation rates, combustion air, kitchen hoods, shafts, plant-room geometry, gas piping, chimney millimetres, listing/labeling criteria and maintenance intervals are not published in this chapter.

## 2. Legends

### Applicability

| Status | Meaning |
|---|---|
| **Direct** | Expected to govern the stated R-2 tower basis, subject to confirmed geometry and design data. |
| **Conditional** | Governs only when the stated feature, use, occupant load, sprinkler branch or exception exists. |
| **Not typical** | Unrelated occupancy-only rule; omitted from this deliverable unless the gap register already opened that use. |
| **External verification** | Chapter 28 points to another section/code/standard, or the project/AHJ basis must be confirmed before use. |

### Source confidence

| Status | Meaning |
|---|---|
| **Verified** | Requirement and any stated numeric value were checked against unambiguous mandatory Chapter 28 source text or an unambiguous table cell. |
| **Verify source** | OCR, flattened table, page-split, or footnote attachment is unresolved. Not a design-release value. |

## 3. Project decision and gap register

| Decision / gap | Current project basis | Why it controls Chapter 28 application | Required project action |
|---|---|---|---|
| SBC 501 versus SBC 1201 | Unconfirmed whether fuel-gas piping or gas appliances are provided | 2801.1 charges design-install to this chapter, **SBC 501** and **SBC 1201** together; fuel-gas work is not scoped by occupancy in this chapter | MEP consultant to lock the mechanical volume and, if gas is present, the fuel-gas volume; do not drop **SBC 1201** from the code sheet until gas is confirmed absent |
| Masonry chimney, fireplace or barbecue | Unconfirmed; amenity barbecue possible, dwelling masonry not typical of this typology | 2801.1 sends those features to **SBC 501** and **Chapter 21** | Freeze amenity/unit fireplace and barbecue program; if any masonry chimney, fireplace or barbecue exists, charge it to 501 and Chapter 21 — do not import hearth or flue dimensions here |
| New construction versus existing-building mechanical work | Tower treated as new construction unless the project states otherwise | Alteration, repair, relocation, replacement and addition are charged to **SBC 901** with **SBC 501** and **SBC 1201** | Keep first-fit tower mechanical work on the design-install charging row; use the 901 branch only for confirmed existing-building mechanical work |
| HVAC, ventilation, duct, appliance and gas criteria | Not published in Chapter 28 | There are no millimetre, air-change, hood, shaft or pipe-size checks in this chapter | Produce the mechanical and fuel-gas packages from **SBC 501** and **SBC 1201**; keep those values off this matrix |
| Sprinkler / mixed use / storeys | Unconfirmed | Chapter 28 has no occupancy, sprinkler or storey branch | Do not wait on NFPA 13 versus 13R to apply 2801.1; those decisions do not change this chapter |
| MEP consultant / SCD pathway | Unconfirmed | Chapter 28 is a charging pointer only; it cannot evidence mechanical or fire-strategy acceptance | Engage the qualified local MEP consultant and align SCD comments before design freeze |

## 4. Mechanical charging

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 2801.1 | Mechanical design-install charging | This chapter, **SBC 501** and **SBC 1201** govern the design, construction, erection and installation of mechanical appliances, equipment and systems | Mechanical appliances, equipment and systems on buildings covered by this code | None stated | Direct | Place Chapter 28, SBC 501 and SBC 1201 on the mechanical code sheet; do not adopt duct, ventilation, combustion-air or appliance values from this chapter | Verified |
| 2801.1 | Masonry chimney fireplace barbecue | Masonry chimneys, fireplaces and barbecues shall comply with **SBC 501** and **Chapter 21** | Masonry chimney, fireplace or barbecue on the building | None stated | Conditional | If a masonry chimney, fireplace or barbecue is programmed, name SBC 501 and Chapter 21 on those drawings; do not import flue, hearth or barbecue dimensions here | Verified |
| 2801.1 | Mechanical use and maintenance | **SBC 801**, the **International Property Maintenance Code**, **SBC 501** and **SBC 1201** govern the use and maintenance of mechanical components, appliances, equipment and systems | In-service use and maintenance of mechanical systems | None stated | External verification | Name SBC 801, IPMC, SBC 501 and SBC 1201 for mechanical O&M; do not import maintenance intervals or fire-prevention criteria from this chapter | Verified |
| 2801.1 | Mechanical alteration repair addition | **SBC 901**, **SBC 501** and **SBC 1201** govern the alteration, repair, relocation, replacement and addition of mechanical components, appliances, equipment and systems | Alteration, repair, relocation, replacement or addition to existing mechanical systems | None stated | Conditional | Charge existing-building mechanical work to SBC 901 with SBC 501 and SBC 1201; keep new-tower first installation on the design-install row | Verified |

## 5. Project-use controls

1. Use **Verified** rows for initial scoping after the row trigger and branch are confirmed.
2. There is no **Verify source** row in this deliverable. Do not treat the absence of numeric cells as permission to fill values from memory, commentary, Figure 2801.1 or the chapter summary.
3. Do not import SBC 501, SBC 1201, SBC 801, SBC 901, IPMC or Chapter 21 duct, ventilation, combustion-air, hood, shaft, plant-room, gas-piping, chimney or maintenance figures into drawings from this matrix.
4. Do not treat General Comments, listing/labeling commentary, SBC 501 Chapter 2 definitions, Section 703.5.2 noncombustible commentary, or Figure 2801.1 example labels as numbered code cells.
5. Record the locked mechanical volume(s), fuel-gas presence, fireplace/barbecue program and new-versus-existing mechanical scope in the project Golden Thread; this matrix is not evidence of SCD NOC, SBPS approval or stamped mechanical compliance.

## 6. Coverage summary

Internal inventory of the attached Chapter 28 extract (numbered code, exceptions, tables, footnotes; commentary excluded). Row-level records are not published.

- **Inventory scope:** numbered code, exceptions, tables, footnotes (commentary excluded)
- **Total independently checkable numeric records:** 0
- **Verified:** 0
- **Verify source:** 0

### Counts by top-level section

| Top-level section | Records |
|---|---:|
| 2801 | 0 |

Coverage cross-check against `SBC 201 Chapter 28 Mechanical Systems (2024)_CS.md` was topics-only: Chapter 28 is a charging pointer to **SBC 501** and **SBC 1201**; masonry chimneys, fireplaces and barbecues to **SBC 501** and **Chapter 21**; use and maintenance to **SBC 801**, IPMC, **SBC 501** and **SBC 1201**; alterations to **SBC 901**, **SBC 501** and **SBC 1201**. It is not a shaft, plant-room or kitchen-hood chapter. No CS.md value was copied into a matrix cell.

## 7. Unresolved-source register

No OCR, flattened-table, page-split or footnote hold point. Mandatory text is unambiguous. Numeric mechanical, fuel-gas, chimney and existing-building criteria are outbound and are not adopted from this chapter.

| Affected table / clause | Why unverified | Control note |
|---|---|---|
| — | No independently checkable numeric cell, table or footnote in the attached extract | Do not reconstruct SBC 501, SBC 1201, SBC 801, SBC 901, IPMC or Chapter 21 values here; lock those criteria from the outbound codes |
