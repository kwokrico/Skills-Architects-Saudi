# SBC 201 Chapter 22 Steel — Group R-2 High-Rise Dimensional Requirements Matrix (2024)

## 1. Document metadata and use limitation

- **Project basis:** Riyadh, Saudi Arabia; Group R-2 residential high-rise; an occupied floor is stated to be more than 23 m above the relevant reference level.
- **Deliverable tier:** Project-use matrices in Sections 4–12 (design-check rows, not pasted inventory), plus a coverage summary and unresolved-source register. The full row inventory is not published.
- **Code/source basis:** SBC 201 (2024), Chapter 22, source file `Reference\SBC 201 2024\source_reference\Chapter_22 — STEEL.txt`.
- **Extraction audit:** Skill extract. Project-use rows follow the chapter-extract row contract (noun-phrase checks, bold SI values, building-language triggers, named exceptions, check-specific actions). Internal inventory: **5** independently checkable numeric records (**5** Verified, **0** Verify source). Non-numeric OCR hold points are listed in the register and are not design-release values.
- **Model:** Cursor Grok 4.6.
- **Prepared:** 2026-08-27.
- **Status:** Source-only architectural advisory matrix for design coordination. It is not a stamped compliance statement, structural design, SCD NOC, SBPS approval, legal opinion, or permission to construct.
- **Outbound-source rule:** No value in this matrix has been imported from SBC 306, SBC 308, SBC 309, SBC 304, SBC 301 (including Table 12.2-1 *R* values other than the **greater than 3** trigger published here), AISC 341, AISC 358, SJI 100, SJI 200, ASCE 8, ASCE 19, RMI ANSI/MH 16.1, RMI ANSI/MH 16.3, ANSI/SDI-NC1.0, ANSI/SDI-RD1.0, SDI-C, AISI S400, AISI S202, AISI S230, AISI S240, Chapter 7, Chapter 16, Chapter 17, commentary examples, bibliography edition years, Figure 2211.2, or the existing chapter summary. Where Chapter 22 sends the user elsewhere, this matrix records the dependency without supplying the outbound value.

### Scope and assumptions

1. Group R-2 and high-rise status are project statements, not independently verified classifications.
2. The exact Riyadh AHJ/permit pathway, project stage, fire-strategy status and SCD NOC status are unconfirmed; therefore this matrix does not conclude compliance.
3. Structural system (hot-rolled steel frame, CIP concrete with miscellaneous steel, composite steel-concrete, cold-formed decks) and Seismic Design Category are unconfirmed.
4. Automatic sprinkler protection, mixed-use podium and storey count are unconfirmed. Chapter 22 does not branch on NFPA 13 versus 13R or on occupancy group.
5. Fire-resistance of steel assemblies is Chapter 7, not this chapter. Special inspections named here send to Chapter 17; this extract has no SI frequency table.
6. AISI S230 prescriptive light-frame (**2211.1.2**, dwellings/townhouses **less than or equal to three stories**) is not this typology. It is counted in the internal inventory and parked in the gap register only.
7. There are no appended tables in this chapter extract. Bibliography years and Figure 2211.2 are not treated as numbered code.

## 2. Legends

### Applicability

| Status | Meaning |
|---|---|
| **Direct** | Expected to govern the stated R-2 tower basis, subject to confirmed geometry and design data. |
| **Conditional** | Governs only when the stated feature, load, sprinkler branch or exception exists. |
| **Not typical** | Unrelated occupancy-only rule; omitted from this deliverable unless the gap register already opened that use. |
| **External verification** | Chapter 22 points to another section/code/standard, or the project/AHJ basis must be confirmed before use. |

### Source confidence

| Status | Meaning |
|---|---|
| **Verified** | Requirement and any stated numeric value were checked against unambiguous mandatory Chapter 22 source text. |
| **Verify source** | OCR, flattened table, page-split, or footnote attachment is unresolved. Not a design-release value. |

## 3. Project decision and gap register

| Decision / gap | Current project basis | Why it controls Chapter 22 application | Required project action |
|---|---|---|---|
| Structural system | Unconfirmed: hot-rolled frame vs CIP with miscellaneous steel vs composite | 2205 charges structural steel to **SBC 306**; 2206 charges composite to **SBC 306** and **SBC 304**; 2210 charges CFS members and decks to **SBC 308** / SDI | Structural engineer of record to freeze the gravity and lateral systems before steel specifications are issued |
| Seismic Design Category | Unconfirmed | 2205.2.1.1 vs 2205.2.1.2, 2205.2.2, 2209.3 and 2211.1.1 branch on SDC B/C vs D/E/F | Lock SDC on the code datum / load-criteria sheet from Chapter 16 / SBC 301 |
| Response modification *R* | Unconfirmed | SDC B/C steel SFRS using Table 12.2-1 *R* must follow **SBC 306 Chapter 12** unless the named “not specifically detailed” exception applies; collectors need Chapter 12 where **R greater than 3** | State the SFRS and *R* on structural drawings; do not adopt commentary *R* = 3 as a code cell |
| Steel joists | Unconfirmed | 2207 applies only if open-web joists or joist girders are specified | Confirm podium, amenity-roof or parking joist use; if none, park Section 2207 |
| Steel cables | Unconfirmed | 2208.1 charges cable structures to **ASCE 19** | Confirm whether any architectural or structural cables exist |
| Storage racks | Unconfirmed | 2209 applies to pallet/cantilever racks; **2400 mm** certificate is SDC D/E/F only | Confirm basement, parking or amenity racking height and SDC |
| CFS decks / light-frame | Unconfirmed | Composite metal deck is common on steel or composite floors (2210.1.1); CFS light-frame SFRS (2211.1) is unusual for this tower | Classify every metal deck and every CFS wall as structural vs nonstructural |
| AISI S230 prescriptive path | Not applicable to this R-2 high-rise | **2211.1.2** permits AISI S230 only for detached one- and two-family dwellings and townhouses **less than or equal to three stories** above grade plane | Do not apply AISI S230 or three-storey light-frame rules to the tower |
| Special inspections | Outbound to Chapter 17 | 2204.1–2204.2, 2211.1.3.2 and 2211.1.3.3 send welding, high-strength bolts and long trusses to **1705.2** / **1704.2.5** | Coordinate the Chapter 17 SI schedule with the steel specification; do not invent frequencies here |
| Fire protection of steel | Outbound to Chapter 7 | This chapter has no fire-resistance periods, spray thicknesses or unprotected-steel tables | Take steel fire ratings from Chapter 7 / the listed assembly, not from Chapter 22 |
| NOC / stamped structural | Unconfirmed | SBC 306/308/309 member design, AISC seismic prequalification and SCD acceptance cannot be concluded from this extract | Engage the structural engineer of record before design freeze |

## 4. Scope, identification and protection

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 2201.1 | Chapter steel scope | This chapter governs quality, design, fabrication and erection of steel construction | Steel quality, design, fabrication or erection on the building | None stated | Direct | List steel work packages on the drawing index and route each system through 2202–2211 | Verified |
| 2202.1 | Structural steel identification | Identify structural steel elements per **SBC 306**; cold-formed members per **SBC 308**; cold-formed light-frame also per **SBC 309** as applicable; other structural load-carrying steel per the specified ASTM or other specification and this chapter. Where grade is not readily identifiable from marking and test records, test the steel to verify conformity | Structural, cold-formed or other load-carrying steel | None stated | External verification | Require mill certificates and piece marks on the steel specification; hold unidentified members for testing before erection | Verified |
| 2203.1 | Steel painting and corrosion protection | Paint structural steel elements per **SBC 306**. Paint open-web steel joists and joint girders per **SJI 100** and **SJI 200**. Protect individual members and assembled panels of cold-formed steel per **SBC 308**; protect cold-formed light-frame per **SBC 309** as applicable | Structural steel, open-web joists, or cold-formed steel exposed to the protection rules of this section | None stated | External verification | Put the matching painting/corrosion specification on each steel package; do not import coating dry-film thicknesses from those standards into this matrix | Verified |

## 5. Connections

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 2204.1 | Welding design and inspection | Welding design, workmanship, technique and personnel qualification shall follow the specifications listed in **2205, 2206, 2207, 2208, 2210 and 2211**. Special inspection of welding: **Section 1705.2** | Welded steel work under those sections | None stated | External verification | Name the applicable AWS/SJI welding specification on the weld procedure sheet and attach the Chapter 17 welding SI item; do not import weld sizes here | Verified |
| 2204.2 | Bolting design and inspection | Bolt design, installation and inspection shall follow **2205, 2206, 2207, 2210 and 2211**. Special inspection of high-strength bolt installation: **Section 1705.2** | Bolted steel work under those sections | None stated | External verification | Schedule high-strength bolts to the Chapter 17 SI programme; do not import pretension or snug-tight values here | Verified |
| 2204.3 | Anchor-rod thread engagement | Set anchor rods to the approved construction documents. Threaded-end protrusion through the connected material shall fully engage the nut threads and shall not be greater than the bolt thread length | Cast-in or similar anchor rods connecting steel | None stated | Direct | Dimension stick-through and thread length on the base-plate / foundation-anchor detail so the nut is fully engaged without exceeding the threaded length | Verified |

## 6. Structural steel and seismic

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 2205.1 | Structural steel design standard | Design, fabrication and erection of structural steel elements in buildings, structures and portions thereof shall be in accordance with **SBC 306** | Structural steel elements | None stated | External verification | Specify structural steel to SBC 306; do not import member sizes, Fy or connection values into this matrix | Verified |
| 2205.2.1.1 | SDC B or C steel SFRS | SDC **B or C** structures may use any construction permitted in 2205. Where *R* from **SBC 301 Table 12.2-1** is used, design and detail to **SBC 306 Chapter 12** | Structural steel seismic force-resisting system in SDC B or C | *R* designated for “Steel systems not specifically detailed for seismic resistance, excluding cantilever column systems” in SBC 301 Table 12.2-1 may use **SBC 306** without **AISC 341** | External verification | Once SDC and *R* are locked, either detail the SFRS to SBC 306 Chapter 12 or document the named Table 12.2-1 exception; do not write commentary *R* = 3 on the drawings from this extract | Verified |
| 2205.2.1.2 | SDC D E or F steel SFRS | SDC **D, E or F** structures shall be designed and detailed to **SBC 306 Chapter 12**, except as permitted in **SBC 301 Table 15.4-1** | Structural steel seismic force-resisting system in SDC D, E or F | Nonbuilding-structure permission in SBC 301 Table 15.4-1 | External verification | If SDC is D, E or F, require SBC 306 Chapter 12 detailing on the steel SFRS; do not import Table 15.4-1 rows here | Verified |
| 2205.2.1.1–2205.2.1.2 | SMF and IMF moment-connection prequalification | Beam-to-column moment connections in special moment frames and intermediate moment frames shall be prequalified per **AISC 341 Section K1**, qualified by testing per **AISC 341 Section K2**, or prequalified per **AISC 358** | SMF or IMF beam-to-column moment connections | None stated | External verification | If SMF/IMF is selected, name K1 / K2 / AISC 358 on the moment-connection typical; do not copy tested connection geometry into this matrix | Verified |
| 2205.2.2 Item 1 | Collectors in SDC D E or F | Struts, collectors, chords and foundation elements in seismic force-resisting systems other than 2205.2.1 shall follow **SBC 306 Chapter 12** where the structure is SDC **D, E or F**, except as permitted in SBC 301 Table as published **15.41** | Collectors, struts, chords or steel foundation elements resisting seismic force in SDC D, E or F | Exception as permitted in the cited SBC 301 table | External verification | Verify the published SBC 301 table identifier before relying on any exception; otherwise detail those elements to SBC 306 Chapter 12 | Verify source |
| 2205.2.2 Item 2 | Collectors where R exceeds 3 | The same non-SFRS steel elements shall follow **SBC 306 Chapter 12** where **R greater than 3** from SBC 301 Table 12.2-1 is used for an SDC **B or C** structure | Collectors, struts, chords or steel foundation elements on an SDC B or C building designed with *R* **greater than 3** | Item 1 (SDC D, E or F) is a separate trigger | External verification | If SDC B/C *R* is **greater than 3**, detail collectors and chords to SBC 306 Chapter 12 even when they are not the primary SFRS | Verified |

## 7. Composite steel-concrete

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 2206.1 | Composite steel-concrete design | Systems of structural steel elements acting compositely with reinforced concrete shall be designed in accordance with **SBC 306** and **SBC 304**, excluding **SBC 304 Chapter 14** | Composite steel-concrete members or systems | SBC 304 Chapter 14 is excluded | External verification | If composite beams or slabs are used, issue a joint SBC 306 / SBC 304 specification and do not apply SBC 304 Chapter 14 from this extract | Verified |
| 2206.2.1 | Composite seismic detailing | Where *R* from **SBC 301 Table 12.2-1** is used for structural steel acting compositely with reinforced concrete, design and detail to **SBC 306 Chapter 12** | Composite SFRS using a Table 12.2-1 *R* | None stated in this chapter | External verification | Lock composite *R* with the SER; send seismic detailing to SBC 306 Chapter 12 and do not import those clause values here | Verified |

## 8. Open-web steel joists

Apply this section only if open-web steel joists or joist girders are specified.

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 2207.1–2207.1.1 | Joist design standard | Design, manufacture and use of open-web steel joists and joist girders shall follow **SJI 100** or **SJI 200** as applicable. Where required, seismic design of the building shall also follow **2205.2** or **2211.1.1** | Open-web steel joists or joist girders | None stated | Conditional | Name SJI 100 or SJI 200 on the joist specification; send seismic load path to the steel or CFS SFRS section, not to a joist-only calculation | Verified |
| 2207.2 | Joist construction-document contents | The registered design professional shall show SJI designations plus joist/girder design, layout, end supports, anchorage, non-SJI bridging, bridging termination, and bearing connections for uplift and lateral load, including special loads (concentrated, nonuniform, net uplift, axial, end moments, connection forces), special profiles/openings/extended ends, and non-SJI live/total-load deflection criteria | Open-web joists or joist girders on the structural set | Bridging that already matches the SJI specification need not be rewritten as a “difference” | Conditional | Put the 2207.2 load and layout checklist on the joist plan before manufacturer design starts | Verified |
| 2207.3–2207.4 | Joist calculations and placement plans | The manufacturer shall design joists and girders to SJI and 2207.2 loads. The RDP may require sealed manufacturer calculations, including non-SJI bridging, non-SJI connections, field splices and joist headers. Placement plans shall show those loads, special profiles, support and splice connections, bridging size/location, deflection criteria and joist headers. Placement plans do not require the manufacturer’s RDP seal | Open-web joists or joist girders released for fabrication | Sealed calculations only where the project RDP requests them | Conditional | Require placement plans for field erection; request sealed calcs when bridging, splices or headers differ from SJI defaults | Verified |
| 2207.5 | Joist certificate of compliance | At completion of manufacture, the joist manufacturer shall submit a certificate of compliance to the owner or owner’s agent for submittal to the building official as specified in **Section 1704.5**, stating work met the approved construction documents and the SJI specification in 2207.1 | Open-web joists or joist girders manufactured for the project | None stated | Conditional | Add the 1704.5 joist certificate to the closeout list before joists ship | Verified |

## 9. Steel cables

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 2208.1 | Steel-cable structures | Design, fabrication and erection of steel cables for buildings, including related connections and protective coatings, shall be in accordance with **ASCE 19** | Steel cables used as building structure or listed cable construction | None stated. Section heading in the extract reads “STEEL STRUCTURES”; the numbered paragraph is cables / ASCE 19 | Conditional | If any structural or architectural cables are used, specify ASCE 19 and do not import cable diameters or pretension from that standard into this matrix | Verified |

## 10. Storage racks

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 2209.1–2209.2 | Storage-rack design standards | Pallet/selective racks of cold-formed or hot-rolled steel: **RMI ANSI/MH 16.1**. Cantilevered storage racks: **RMI ANSI/MH 16.3**. Where required by SBC 301, seismic design of either type shall follow **SBC 301 Section 15.5.3** | Steel storage racks or steel cantilevered storage racks | None stated in this chapter | Conditional | If basement, parking or amenity racking is used, name MH 16.1 or 16.3 and send seismic rack design to SBC 301 15.5.3; do not import bay loads here | Verified |
| 2209.3 | Tall-rack SDC D-F certificate | For rack storage **2400 mm** in height or greater to the top load level and assigned to SDC **D, E or F**, submit a certificate of compliance to the owner or owner’s agent at completion of installation stating the work met the approved construction documents | Racks **2400 mm** or taller to the top load level in SDC D, E or F | Shorter racks, or SDC A/B/C, are not charged by this certificate clause | Conditional | Once rack height and SDC are known, add the installation certificate to the closeout list for racks meeting both triggers | Verified |

## 11. Cold-formed steel and decks

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 2210.1 | Cold-formed member design | Cold-formed carbon and low-alloy steel structural members: **SBC 308**. Cold-formed stainless-steel structural members: **ASCE 8**. Cold-formed light-frame construction shall also comply with **2211**. Where required, seismic design of CFS structures shall follow **2210.2** | Cold-formed structural steel members | None stated | External verification | Specify carbon/low-alloy CFS to SBC 308 and stainless CFS to ASCE 8; do not import thicknesses or Fy from those standards | Verified |
| 2210.1.1.1–2210.1.1.3 | Cold-formed steel decks | Noncomposite steel floor decks may be designed to **ANSI/SDI-NC1.0**. Steel roof decks may be designed to **ANSI/SDI-RD1.0**. Composite slabs of concrete and steel deck may be designed to **SDI-C** | Cold-formed steel floor, roof or composite deck | Each SDI path is permissive for its deck type | Conditional | Name the matching SDI standard on the deck specification; do not import gauges, rib depths or composite-slab thicknesses here | Verified |
| 2210.2 | Cold-formed seismic detailing | Where *R* from **SBC 301 Table 12.2-1** is used for cold-formed steel structures, design and detail to **SBC 308**, **ASCE 8**, or, for cold-formed steel special-bolted moment frames, **AISI S400** | CFS SFRS using a Table 12.2-1 *R* | Special-bolted moment frames use AISI S400 rather than SBC 308 / ASCE 8 | External verification | If a CFS SFRS is used, lock the standard (SBC 308, ASCE 8 or AISI S400) to the selected system; do not import AISI S400 heights or *E*mh from commentary | Verified |

## 12. Light-frame, trusses and nonstructural

Cold-formed **structural** light-frame (2211.1) is unusual for this R-2 high-rise. Apply those rows only if CFS floors, structural walls, shear/strap walls or trusses are specified. **2211.1.2** AISI S230 is omitted from the table (see gap register). Nonstructural CFS (2211.2) is the typical partition path.

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 2211.1 | CFS light-frame structural systems | Floor and roof systems; structural walls; shear walls, strap-braced walls and in-plane diaphragms; and trusses, including members and connections, shall follow **SBC 309** and 2211.1.1 through 2211.1.3 as applicable | Cold-formed steel light-frame used as those structural systems | None stated | Conditional | If CFS is a structural system rather than a partition, specify SBC 309 and do not treat it as architectural stud framing | Verified |
| 2211.1.1.1 | Light-frame SDC B or C SFRS | Where *R* from **SBC 301 Table 12.2-1** is used for CFS light-frame in SDC **B or C**, the SFRS shall be designed and detailed to **AISI S400** | CFS light-frame SFRS in SDC B or C using Table 12.2-1 *R* | *R* designated for “Steel systems not specifically detailed for seismic resistance, excluding cantilever column systems” in SBC 301 Table 12.2-1 may use **SBC 309** without AISI S400 | External verification | Document either AISI S400 detailing or the named Table 12.2-1 exception; do not adopt commentary *R* = 3 | Verified |
| 2211.1.1.2 | Light-frame SDC D through F SFRS | CFS light-frame assigned to SDC **D, E or F** shall have the SFRS designed and detailed in accordance with **AISI S400** | CFS light-frame SFRS in SDC D, E or F | None stated | External verification | If SDC is D–F and CFS light-frame resists seismic force, require AISI S400; do not import AISI S400 values here | Verified |
| 2211.1.3.1 | CFS truss design drawings | Truss design drawings shall conform to **AISI S202 Section I1**, shall ship with the trusses, and shall include permanent individual truss member restraint/bracing details per **AISI S202 Section I1.6** where those methods provide the restraint/bracing | Cold-formed steel trusses | I1.6 bracing details only where that method is used | Conditional | Require AISI S202 drawings in the truss shipment; do not import I1 content into this matrix | Verified |
| 2211.1.3.2 | Long-span CFS truss bracing and SI | Owner or owner’s agent shall contract a registered design professional for temporary installation restraint/bracing and permanent individual truss member restraint/bracing where clear spans are **18 m** or greater. Special inspection of trusses **over 18 m** in length shall follow **Section 1705.2** | CFS trusses with clear span **18 m** or greater, or length **over 18 m** | Shorter trusses are not charged by this clause | Conditional | If any CFS truss reaches **18 m**, assign an RDP for temp and permanent bracing and add 1705.2 SI to the steel inspection list | Verified |
| 2211.1.3.3 | CFS truss quality assurance | Trusses that are not part of a manufacturing process with third-party quality control per **AISI S240 Chapter D** shall be fabricated in compliance with **Sections 1704.2.5 and 1705.2** as applicable | CFS trusses fabricated outside an AISI S240 Chapter D QC process | Factory process meeting AISI S240 Chapter D is outside this fabrication path | Conditional | State whether each truss supplier is under AISI S240 Chapter D; if not, put 1704.2.5 / 1705.2 on the fabrication SI list | Verified |
| 2211.2 | Nonstructural CFS members | Design and installation of nonstructural members and connections in cold-formed steel light-frame construction shall be in accordance with **SBC 308** and **SBC 309** | Nonstructural CFS (typical partition studs and similar) | None stated | External verification | Specify interior CFS studs to SBC 308/309; do not import stud gauges or spacing from those standards into this matrix | Verified |

## 13. Project-use controls

1. Use **Verified** rows for initial scoping after the row trigger is confirmed (the steel system actually exists on the project).
2. Treat **Verify source** rows as hold points. The only project-use **Verify source** cell is **2205.2.2 Item 1** (SBC 301 table identifier published as `15.41`). Do not use that exception until the published table number is confirmed.
3. Do not import SBC 306/308/309 member sizes, AISC/SJI/SDI/AISI connection or deck values, Chapter 7 fire ratings, or Chapter 17 inspection frequencies into issued drawings from this matrix.
4. Do not adopt bibliography years (AISC 341-10, AISI S100-12, and similar) as charging editions, and do not adopt commentary *R* = 3, CFS-SBMF **10.5 m**, or SI **2.4 m** restatements.
5. Do not apply **2211.1.2** AISI S230 / **three stories** prescriptive framing to this R-2 high-rise.
6. Record SFRS, SDC, *R*, deck type and rack-height decisions in the project Golden Thread; this matrix is not evidence of SCD NOC or stamped compliance.

## 14. Coverage summary

Internal inventory of the attached Chapter 22 extract (numbered code, exceptions, tables, footnotes; commentary excluded). Row-level records are not published.

- **Inventory scope:** numbered code, exceptions, tables, footnotes (commentary excluded)
- **Total independently checkable numeric records:** 5
- **Verified:** 5
- **Verify source:** 0

### Counts by top-level section

| Top-level section | Records |
|---|---:|
| 2201 | 0 |
| 2202 | 0 |
| 2203 | 0 |
| 2204 | 0 |
| 2205 | 1 |
| 2206 | 0 |
| 2207 | 0 |
| 2208 | 0 |
| 2209 | 1 |
| 2210 | 0 |
| 2211 | 3 |

Numeric records: **2205.2.2 Item 2** (*R* **greater than 3**); **2209.3** (**2400 mm**); **2211.1.2** (**three stories**, inventory only — omitted from project-use tables); **2211.1.3.2** (**18 m** clear-span RDP; **over 18 m** SI).

No appended tables in the attached extract.

Coverage cross-check against `SBC 201 Chapter 22 Steel (2024)_CS.md` was topics-only: chapter as a companion-standard roadmap; identification/protection; welding/bolting SI to 1705.2; SBC 306 / 304 / 308 / 309 / SJI / ASCE 19 / RMI / SDI / AISI map; SDC and *R* seismic branches; **2400 mm** rack certificate; **18 m** truss bracing/SI; AISI S230 three-storey dwellings. No CS.md value was copied into a matrix cell. CS.md note that **SBC 307 is not cited** matches the attached extract.

## 15. Unresolved-source register

| Affected table / clause | Why unverified | Control note |
|---|---|---|
| 2205.2.2 Item 1 | Table identifier published as `15.41`; sibling **2205.2.1.2** publishes `Table 15.4-1` | Do not adopt either identifier as a repaired citation. No exception from that table is a design-release value until the published SBC 301 table is confirmed. Project-use row is **Verify source**. |
| 2208 section heading | Heading reads `STEEL STRUCTURES`; numbered **2208.1** is steel cables / **ASCE 19** | Use 2208.1 as published. Do not treat the heading as a second charging scope. |
| 2203.1 | Token `joint girders` in the painting sentence; 2207 uses `joist girders` | Keep the 2203.1 token as published. SJI 100 / SJI 200 charging is unambiguous; the row is **Verified**. |
| 2211.1.1 charging sentence | Body cites `Section 2211.1.1 or 2211.1.1.2` | Do not insert a missing `.1` from memory. Apply the SDC rules in **2211.1.1.1** and **2211.1.1.2**, which are complete. |
| 2207.2 / 2211.1.1.1 Exception | Page-split after “designations from” and after “SBC 309” | Continuation text is complete on the following page. No value was taken from the gap; both project-use rows remain **Verified**. |
