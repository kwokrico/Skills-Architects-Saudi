# SBC 201 Chapter 13 Energy Efficiency — Group R-2 High-Rise Dimensional Requirements Matrix (2024)

## 1. Document metadata and use limitation

- **Project basis:** Riyadh, Saudi Arabia; Group R-2 residential high-rise.
- **Deliverable tier:** Project-use matrices in Sections 1–5 (design-check rows, not pasted inventory), plus a coverage summary and unresolved-source register. The full row inventory is not published.
- **Code/source basis:** SBC 201 (2024), Chapter 13, source file `Reference\SBC 201 2024\source_reference\Chapter_13 — ENERGY EFFICIENCY.txt`.
- **Extraction audit:** Skill-finetune run. Project-use rows follow the chapter-extract row contract (noun-phrase checks, bold published tokens, building-language triggers, named exceptions, check-specific actions). Internal inventory: **0** independently checkable numeric records (**0** Verified, **0** Verify source). Chapter 13 has no tables, exceptions, footnotes, or numeric cells.
- **Model:** Cursor Grok 4.6.
- **Prepared:** 2026-08-27.
- **Status:** Source-only architectural advisory matrix for design coordination. It is not a stamped compliance statement, energy-modelling report, SCD NOC, SBPS approval, legal opinion, or permission to construct.
- **Outbound-source rule:** No value in this matrix has been imported from SBC 601, SBC 602, climate-zone tables, envelope/HVAC/lighting criteria, commentary examples, or the existing chapter summary. Where Chapter 13 sends the user elsewhere, this matrix records the dependency without supplying the outbound value.

### Scope and assumptions

1. Group R-2 and high-rise status are project statements, not independently verified classifications.
2. The exact Riyadh AHJ/permit pathway, project stage and SCD NOC status are unconfirmed; therefore this matrix does not conclude compliance.
3. Chapter 13 does not assign **SBC 601** versus **SBC 602** to this occupancy. Both volumes are named; neither is selected here.
4. Automatic sprinkler protection, storey count, mixed-use podium and amenity program are unconfirmed. Chapter 13 itself does not branch on those facts; any such branching lives in the outbound energy codes and is not reconstructed here.
5. Climate zone, thermal envelope, air leakage, mechanical, service-water heating, electrical distribution and illumination criteria are not published in this chapter.

## 2. Legends

### Applicability

| Status | Meaning |
|---|---|
| **Direct** | Expected to govern the stated R-2 tower basis, subject to confirmed geometry and design data. |
| **Conditional** | Governs only when the stated feature, use, occupant load, sprinkler branch or exception exists. |
| **Not typical** | Unrelated occupancy-only rule; omitted from this deliverable unless the gap register already opened that use. |
| **External verification** | Chapter 13 points to another section/code/standard, or the project/AHJ basis must be confirmed before use. |

### Source confidence

| Status | Meaning |
|---|---|
| **Verified** | Requirement and any stated numeric value were checked against unambiguous mandatory Chapter 13 source text or an unambiguous table cell. |
| **Verify source** | OCR, flattened table, page-split, or footnote attachment is unresolved. Not a design-release value. |

## 3. Project decision and gap register

| Decision / gap | Current project basis | Why it controls Chapter 13 application | Required project action |
|---|---|---|---|
| SBC 601 versus SBC 602 | Unconfirmed; Chapter 13 names both and does not assign either volume to Group R-2 high-rise | Controls which energy-conservation volume demonstrates compliance for the tower and any mixed-use portions | Energy/MEP consultant and AHJ to lock the applicable volume(s); do not infer the selection from this chapter |
| Climate zone | Not published in Chapter 13 | Envelope, HVAC and related criteria in the outbound codes are climate-dependent | Establish the project climate zone from the locked SBC 601/602 documents, not from this matrix |
| Envelope, HVAC, service water, electrical and illumination criteria | Not published in Chapter 13 | There are no R-values, SHGC, LPD, equipment-efficiency or similar numeric checks in this chapter | Produce the energy-compliance package from SBC 601 and/or SBC 602; keep those values off this matrix |
| Mixed-use / podium program | Unconfirmed | Shared or non-residential portions, if present, are still demonstrated under the outbound energy codes, not under a Chapter 13 occupancy table | Freeze occupancy/use by space; apply the locked 601/602 scoping to each portion |
| Energy consultant / AHJ pathway | Unconfirmed | Chapter 13 is a charging pointer only; it cannot evidence energy-code acceptance | Engage the qualified local energy/MEP consultant before design freeze |

## 4. Energy-efficiency charging

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1301.1 | Chapter energy-efficiency scope | This chapter governs the design and construction of buildings for energy efficiency | All buildings in Chapter 13 scope | None stated | Direct | Place Chapter 13 on the code sheet as the charging energy-efficiency chapter | Verified |
| 1301.1.1 | SBC 601/602 compliance | Buildings shall be designed and constructed in accordance with the Saudi Energy Conservation Code (**SBC 601** and **SBC 602**) | All buildings governed by this chapter | None stated | External verification | Demonstrate energy-efficiency compliance through SBC 601 and SBC 602; do not adopt envelope, HVAC, lighting or climate-zone values from this chapter | Verified |

## 5. Project-use controls

1. Use **Verified** rows for initial scoping after the row trigger and branch are confirmed.
2. There is no **Verify source** row in this deliverable. Do not treat the absence of numeric cells as permission to fill values from memory, commentary or the chapter summary.
3. Do not import SBC 601 or SBC 602 envelope, HVAC, service-water, electrical-distribution, illumination or climate-zone figures into drawings from this matrix.
4. Do not treat Chapter 13 as assigning **SBC 601** or **SBC 602** to Group R-2 high-rise.
5. Record the locked energy-code volume(s), climate zone and compliance path in the project Golden Thread; this matrix is not evidence of SCD NOC, SBPS approval or stamped energy compliance.

## 6. Coverage summary

Internal inventory of the attached Chapter 13 extract (numbered code, exceptions, tables, footnotes; commentary excluded). Row-level records are not published.

- **Inventory scope:** numbered code, exceptions, tables, footnotes (commentary excluded)
- **Total independently checkable numeric records:** 0
- **Verified:** 0
- **Verify source:** 0

### Counts by top-level section

| Top-level section | Records |
|---|---:|
| 1301 | 0 |

Coverage cross-check against `SBC 201 Chapter 13 Energy Efficiency (2024)_CS.md` was topics-only: Chapter 13 is a charging pointer to **SBC 601** and **SBC 602**; it is not a thermal-envelope or lighting-power chapter. No CS.md value was copied into a matrix cell.

## 7. Unresolved-source register

No OCR, flattened-table, page-split or footnote hold point. Mandatory text is unambiguous. Numeric energy criteria are outbound and are not adopted from this chapter.

| Affected table / clause | Why unverified | Control note |
|---|---|---|
| — | No independently checkable numeric cell, table or footnote in the attached extract | Do not reconstruct SBC 601/602 values here; lock those criteria from the outbound codes |
