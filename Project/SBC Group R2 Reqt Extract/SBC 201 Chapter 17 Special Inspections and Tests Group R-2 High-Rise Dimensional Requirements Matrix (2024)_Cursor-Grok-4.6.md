# SBC 201 Chapter 17 Special Inspections and Tests — Group R-2 High-Rise Dimensional Requirements Matrix (2024)

## 1. Document metadata and use limitation

- **Project basis:** Riyadh, Saudi Arabia; Group R-2 residential high-rise; an occupied floor is stated to be more than 23 m above the relevant reference level.
- **Deliverable tier:** Project-use matrices in Sections 1–15 (design-check rows, not pasted inventory), plus a coverage summary and unresolved-source register. The full row inventory is not published.
- **Code/source basis:** SBC 201 (2024), Chapter 17, source file `Reference\SBC 201 2024\source_reference\Chapter_17 — SPECIAL INSPECTIONS AND TESTS.txt`.
- **Extraction audit:** Skill-finetune run. Project-use rows follow the chapter-extract row contract (noun-phrase checks, bold SI values, building-language triggers, named exceptions, check-specific actions). Internal inventory: **156** independently checkable numeric records (**106** Verified, **50** Verify source). Unresolved OCR, flattened tables and page-splits are listed in the register and are not design-release values.
- **Model:** Cursor Grok 4.6.
- **Prepared:** 2026-08-27.
- **Status:** Source-only architectural advisory matrix for design coordination of special inspections, tests and structural observation. It is not a stamped compliance statement, structural-observation report, SCD NOC, SBPS approval, legal opinion, or permission to construct.
- **Outbound-source rule:** No value in this matrix has been imported from SBC 301–306, AISC 341, SDI QA/QC, AWS D1.4, ASTM inspection standards, Section 403, Section 704, Sections 714/715, Section 909, Chapter 16 wind/seismic maps, commentary examples, or the existing chapter summary. Where Chapter 17 sends the user elsewhere, this matrix records the dependency without supplying the outbound value.

### Scope and assumptions

1. Group R-2 and high-rise status are project statements, not independently verified classifications.
2. The exact Riyadh AHJ/permit pathway, project stage, fire-strategy status and SCD NOC status are unconfirmed; therefore this matrix does not conclude compliance.
3. Risk Category, Seismic Design Category, basic wind speed *V*, wind Exposure Category, construction type, geotechnical report status, foundation system, SFRM versus mastic/intumescent, smoke-control scope and EIFS use are unconfirmed.
4. Automatic sprinkler protection is not selected. Chapter 17 does not branch NFPA 13 versus 13R. Section 1705.13.6 Item 6 applies where automatic fire sprinkler systems are installed.
5. Building height, storey count, grade plane and mixed-use podium layout are unconfirmed beyond the stated high-rise occupied-floor datum.
6. Seven appended inspection tables are concatenated OCR. No reconstructed continuous/periodic cell or the Table 1705.3 “**7.8 mm**” fillet-weld token is adopted as a design-release value.
7. Commentary numbers are excluded, including fireplace-steel examples, restated **720 N/m²** cladding weight, isolator “two specimen” counts, and Section 403.2.3 SFRM bond (named only in commentary).

## 2. Legends

### Applicability

| Status | Meaning |
|---|---|
| **Direct** | Expected to govern the stated R-2 tower basis, subject to confirmed geometry and design data. |
| **Conditional** | Governs only when the stated feature, material, seismic/wind branch or exception exists. |
| **Not typical** | Unrelated occupancy-only rule; omitted from this deliverable unless the gap register already opened that use. |
| **External verification** | Chapter 17 points to another section/code/standard, or the project/AHJ basis must be confirmed before use. |

### Source confidence

| Status | Meaning |
|---|---|
| **Verified** | Requirement and any stated numeric value were checked against unambiguous mandatory Chapter 17 source text. |
| **Verify source** | OCR, flattened table, page-split, or footnote attachment is unresolved. Not a design-release value. |

## 3. Project decision and gap register

| Decision / gap | Current project basis | Why it controls Chapter 17 application | Required project action |
|---|---|---|---|
| High-rise confirmation | Occupied floor stated above 23 m; classification not independently verified | 1704.6.1 Item 2 structural observation and 1705.18 firestop SI both trigger on high-rise | Issue a signed height/storey datum; keep observation and firestop SI on the SSI until classification is locked |
| Risk Category | Unconfirmed (R-2 often II, not verified) | RC IV independently requires observation; RC III/IV independently require firestop SI; masonry veneer Level 2 is RC IV only | Structural RDP to assign Risk Category per Section 1604.5 (outbound); do not assume II |
| Seismic Design Category | Unconfirmed; values live in Chapter 16 / SBC 301 | 1705.13–1705.14 inspections and tests are SDC-gated; 1704.6.1 Item 3 is SDC E and **greater than two stories** | Lock SDC on the structural basis of design; show SDC branches on the SSI without importing Chapter 16 maps here |
| Wind *V* and exposure | Unconfirmed | Extra wind SI applies in Exposure B at **67 m/sec** or greater, or Exposure C/D at **62.5 m/sec** or greater | Wind consultant to publish *V* and exposure; until then retain the two Chapter 17 branches |
| Construction type | Unconfirmed (steel, concrete, masonry, wood, mass timber) | Selects 1705.2–1705.5 tables and outbound SBC 304/305/306 | Freeze primary structure and deck/truss systems on the SSI |
| Geotech / foundations | Unconfirmed | Soils table, deep-foundation tables, helical piles and 90-percent density exception | Issue approved geotechnical report and foundation type before SSI freeze |
| SFRM vs intumescent | Unconfirmed | 1705.15 sampling/thickness/density/bond versus 1705.16 AWCI 12-B | Fire-protection specification to name the listed system; high-rise 403.2.3 bond is outbound and not imported |
| Smoke control | Unconfirmed | 1705.19 special inspector if a smoke-control system is provided | Fire strategy to lock Section 909 / smokeproof-enclosure scope |
| EIFS | Unconfirmed | 1705.17 SI unless a listed drainage or masonry/concrete-substrate exception applies | Façade specification to confirm EIFS, WRB coating and substrate |
| Sprinkler presence | Unconfirmed; 13 vs 13R not a Chapter 17 branch | 1705.13.6 Item 6 sprinkler-clearance SI applies where automatic sprinklers are installed | Fire engineer to confirm sprinklers; use the 75 mm / flexible-hose branches, not a 13/13R choice |
| Podium mixed use / storage racks | Unconfirmed | Storage-rack SI is SDC D–F and **2400 mm** or greater; not a typical apartment fit-out | Open this branch only if warehouse/retail racks appear |
| NOC / SSI / observation | Unconfirmed | Statement of special inspections is a permit condition; observation does not waive Section 110 or 1705 | Engage the structural RDP and approved agencies; align SSI, SBPS and SCD comments before construction |

## 4. Employment, statement of special inspections and submittals

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1703.1 | Approved-agency accreditation | Approved agency shall meet Part III of **SBC 302** and shall be accredited | Agency performing tests or special inspections | Independence, equipment and personnel in 1703.1.1–1703.1.3; SBC 302 values are not imported | Direct | Name accredited agencies on the SSI; do not let the contractor employ the agency unless the contractor is also the owner | Verified |
| 1703.1.1 | Agency independence | Agency shall be objective, competent and independent from the contractor responsible for the inspected work, and shall disclose conflicts to the building official and the RDP in responsible charge | Approved agency | 1704.2 Exception 4 allows the contractor to employ the agency only where the contractor is also the owner | Direct | Keep the owner (not the GC) as the employing party on this tower | Verified |
| 1704.2 | Owner-employed special inspections | Owner or owner’s authorized agent, other than the contractor, shall employ approved agencies for Section 1705 work, in addition to Section 110 inspections | Permit application under Section 105 | 1. Minor work or jurisdiction-approved conditions. 2. Group U accessory to residential unless the building official requires SI. 3. Portions under 2211.1.2 CFS light-frame or 2308 conventional light-frame. 4. Contractor-as-owner employment | Direct | Place SI on the high-rise permit path; do not treat the tower as minor work or prescriptive light-frame | Verified |
| 1704.2.3 / 1704.3 | Statement of special inspections | Applicant shall submit an SSI as a permit condition; the RDP in responsible charge prepares it | Special inspections or tests required by 1705 | SSI not required for 2211.1.2 / 2308 portions; a qualified person approved by the building official may prepare the SSI only where the work was not designed by an RDP | Direct | Issue the SSI with the permit set; do not defer it to construction administration | Verified |
| 1704.3.1 | SSI content | Identify materials/systems/work requiring SI or tests; type and extent of each inspection and each test; extra seismic/wind items under 1705.12–1705.14; and whether each inspection is continuous, periodic, or per the referenced-standard notation | Every required SI/test | Wind and seismic identification in 1704.3.2–1704.3.3 when those sections apply | Direct | Schedule each tower SI scope as continuous, periodic or standard-notation on the SSI | Verified |
| 1704.2.4 | Inspection reports | Approved agencies keep records, report to the building official and the RDP, flag uncorrected discrepancies before phase completion, and submit a final report at a time agreed before start of work | SI and tests performed | None stated | Direct | Put report routing and the agreed final-report date in the CA/SSI kickoff | Verified |
| 1704.2.5 / 1704.2.5.1 | Fabricator special inspection | Shop fabrication of structural, load-bearing or lateral-load-resisting members requires SI during fabrication unless the fabricator is approved; approved fabricator submits a certificate of compliance | Off-site structural fabrication | Approval based on written procedures, QC manuals and periodic auditing | Conditional | Require SI or an approved-fabricator certificate for precast, steel and truss shops | Verified |
| 1704.4 | Contractor statement of responsibility | Each contractor for a listed main wind or seismic force-resisting system, designated seismic system, or wind/seismic component shall submit a written statement of responsibility before that work starts | Wind or seismic items listed on the SSI | Acknowledgement of the SSI special requirements only | Conditional | Collect contractor statements before steel/concrete/façade erection on those systems | Verified |
| 1704.5 Items 1–7 | Owner certificates and reports | Owner submits fabricator, seismic-qualification, designated-seismic, shotcrete, joist, weldability and SDC **B–F** mill-test certificates/reports listed in this section, in addition to 1704.2.4 agency reports | Applicable listed materials/systems | Item 7 mill tests apply to ASTM A615 bars used to resist earthquake flexure/axial force in special moment frames, special structural walls or coupling beams in SDC **B, C, D, E or F**; outbound SBC 304 clauses are not imported | Conditional | Schedule the listed certificates against actual materials; lock SDC before relying on Item 7 | Verified |

## 5. Structural observation

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1704.6 / 1704.6.1 Item 2 | High-rise structural observation | Owner shall employ a registered design professional to visually observe representative structural systems, details and load paths; observation does not waive Section 110 or 1705 | Structure is a high-rise building | Also required for Risk Category **IV**, or SDC **E** and **greater than two stories** above grade plane, or where the structural RDP or building official requires it | Direct | Appoint the structural observer, file frequency/extent before site visits, and file the close-out statement of unresolved deficiencies | Verified |
| 1704.6.1 Item 3 | SDC E multi-storey observation | Structural observation required where the structure is SDC **E** and **greater than two stories** above grade plane | SDC E and storey count | Independent of the high-rise trigger; this tower already meets Item 2 if high-rise is confirmed | Conditional | Retain Item 2 as the governing high-rise trigger; Item 3 is additional if SDC E is assigned | Verified |

## 6. Steel, concrete, masonry and wood special inspections

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1705.2.1 | Structural steel SI | Special inspections and NDT of structural steel elements shall follow the quality-assurance inspection requirements of **SBC 306** | Structural steel in the building | Fabrication SI not required where the entire fabrication process has no welding, thermal cutting or heating, with stated material-control procedures; railing systems limited to weld inspection at cantilevered rail-post bases | Direct | List structural steel SI on the SSI as SBC 306 QA; do not import SBC 306 frequencies here | Verified |
| 1705.2.2 | Steel deck SI | Cold-formed steel floor and roof deck SI and welding-inspector qualification shall follow **SDI QA/QC** | Steel floor or roof deck | None stated in this section | Conditional | If metal deck is used, name SDI QA/QC on the SSI without importing that standard’s values | Verified |
| 1705.2.3 / Table 1705.2.3 | Open-web joist SI | Open-web steel joists and joist girders shall be specially inspected in accordance with Table 1705.2.3 | Joists/girders used | Table is concatenated OCR; continuous/periodic *X* marks are not adopted as design-release values; Note a also points to 1705.13 | Conditional | If joists are specified, verify the published table before assigning periodic vs continuous; keep joist certificates per 1704.5 Item 5 | Verify source |
| 1705.2.4 | Long-span CFS truss bracing | Where cold-formed steel truss **clear span is 18 m or greater**, the special inspector shall verify temporary installation restraint/bracing and permanent individual truss-member restraint/bracing against the approved truss submittal | CFS truss span ≥ 18 m | None stated | Conditional | Flag any CFS truss ≥ 18 m on framing plans and put bracing SI on the SSI | Verified |
| 1705.3 / Table 1705.3 | Concrete construction SI | Concrete SI and tests shall follow this section and Table 1705.3 | Concrete construction | Story-limited footing exceptions and on-grade slabs/patios in 1705.3; this high-rise fails the **three stories or less** gate. Table is concatenated OCR. Item 2b token “maximum **7.8 mm**” fillet weld is not adopted | Direct | Put concrete SI on the SSI; verify published Table 1705.3 frequencies before issuing hold-points; do not repair 7.8 mm from memory | Verify source |
| 1705.3 Ex. 1–2 | Low-rise footing SI waiver | Isolated spread footings, and continuous wall footings, of buildings **three stories or less** above grade plane fully supported on earth or rock may be waived as stated | Buildings three stories or less | Continuous-footing sub-items are flattened (items 3–5 appear un-nested; **17. MPa** OCR). Waiver does not describe this high-rise | Conditional | Do not apply the three-storey footing waiver to the tower; verify published exception nesting only if a separate low-rise U/podium structure is claimed | Verify source |
| 1705.3.1 | Rebar welding SI | Welding SI and inspector qualification for reinforcing bars shall be in accordance with **AWS D1.4** | Rebar is welded | Source repeats AWS D1.4 twice; AWS values are not imported | Conditional | If rebar welding is specified, name AWS D1.4 on the SSI and collect 1704.5 Item 6 weldability reports for non-A706 bars | Verified |
| 1705.4 | Masonry SI | Masonry SI and tests shall follow the quality-assurance program of **SBC 305** | Masonry construction | Empirically designed masonry, glass-unit masonry or masonry veneer in RC **I, II or III**; masonry fireplaces/heaters/chimneys per 2111–2113 | Conditional | If structural or veneer masonry is used, list SBC 305 QA; do not import SBC 305 levels except as 1705.4.1 states | Verified |
| 1705.4.1 | RC IV veneer Level 2 | Glass-unit masonry or masonry veneer in Risk Category **IV** shall be inspected to **SBC 305 Level 2** | RC IV structure with that masonry | Ordinary R-2 is not typically RC IV | Conditional | Apply Level 2 only if RC IV is assigned; otherwise keep 1705.4 | Verified |
| 1705.5.1 | High-load wood diaphragm SI | High-load diaphragms designed to 2306.2 require SI of panel grade/thickness, adjoining framing size, fastener diameter/length, fastener-line count and spacing/edge margins | 2306.2 high-load diaphragm | Prefabricated wood assemblies follow 1704.2.5 | Conditional | Typical concrete/steel R-2 towers omit this unless a wood diaphragm is specified | Verified |
| 1705.5.2 | Long-span wood truss bracing | Where metal-plate-connected wood truss **clear span is 18 m or greater**, verify temporary and permanent restraint/bracing against the approved truss submittal | Wood truss span ≥ 18 m | None stated | Conditional | Same 18 m gate as CFS; apply only if long-span wood trusses exist | Verified |
| 1705.5.3 / Table 1705.5.3 | Mass-timber SI | Mass timber in Types **IV-A, IV-B and IV-C** shall follow Table 1705.5.3 (source cite printed as **Table 1/705.5.3**) | Mass-timber construction types | Flattened table cells are not adopted | Conditional | Conventional R-2 high-rise is not mass timber unless that type is selected; verify published table if IV-A/B/C is used | Verify source |

## 7. Soils and deep foundations

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1705.6 / Table 1705.6 | Soils SI and tests | Existing site soils, fill placement and load-bearing requirements shall be inspected and tested per this section and Table 1705.6, using the approved geotechnical report and construction documents | Shallow foundations / compacted fill | Table is concatenated OCR. Where SBC 303 does not require fill-placement reporting, in-place dry density shall be **not less than 90 percent** of maximum dry density at optimum moisture (ASTM D1557) | Direct | Put soils SI on the SSI; use the 90-percent density check only on the SBC 303 non-reporting branch; do not import commentary 300 mm fill limits | Verify source |
| 1705.7 / Table 1705.7 | Driven deep-foundation SI | Driven elements shall be inspected and tested per Table 1705.7 against the geotechnical report and documents | Driven piles | Flattened continuous *X* marks are not design-release; steel/concrete/specialty rows point back to 1705.2 / 1705.3 / the SSI | Conditional | If driven piles are selected, verify the published table and keep driving records per element | Verify source |
| 1705.8 / Table 1705.8 | Cast-in-place deep-foundation SI | Cast-in-place elements shall be inspected and tested per Table 1705.8 | Bored piles / caissons | Flattened table; concrete row points to 1705.3 | Conditional | If CIP piles are selected, verify the published table and record diameters, lengths and grout/concrete volumes | Verify source |
| 1705.9 | Helical-pile SI | **Continuous** special inspections during helical-pile installation, recording equipment, pile dimensions, tip elevations, final depth, final installation torque and RDP-required data | Helical piles | Geotechnical report and documents govern compliance | Conditional | Use only if helical piles are specified; keep continuous field logs | Verified |
| 1705.10 | Deep-foundation integrity tests | Where structural integrity is reasonably in doubt, an engineering assessment with defect tests per ASTM D4945, D5882, D6760 or D7949, or other approved method, is required | Doubt as to element integrity | Test method values are not imported | Conditional | Trigger integrity testing from driving/drilling records, not as a default extra on every pile | Verified |

## 8. Wind-resistance special inspections

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1705.12 | Wind SI geographic gate | Extra wind-resistance SI in 1705.12.1–1705.12.3 is required in Exposure **B** where *V* is **67 m/sec or greater**, and in Exposure **C or D** where *V* is **62.5 m/sec or greater**, unless 1704.2 exceptions apply | Wind speed and exposure from the structural basis of design | Do not assume Riyadh *V* or exposure in this chapter | Conditional | Publish *V* and exposure; if either gate is met, identify MWFRS and cladding on the SSI per 1704.3.3 | Verified |
| 1705.12.1 | Wood MWFRS wind SI | Continuous SI during field gluing of MWFRS elements; periodic SI of nailing, bolting, anchoring and other fastening of wood MWFRS elements | 1705.12 wind gate and wood MWFRS | Not required where lateral resistance is structural sheathing and specified panel-edge fastener spacing is **more than 100 mm** on center | Conditional | Typical concrete/steel R-2 omits wood MWFRS; if used, apply the 100 mm spacing exception only where documented | Verified |
| 1705.12.2 | CFS light-frame wind SI | Periodic SI of MWFRS welding and of screw, bolt, anchor and other fastening | 1705.12 wind gate and CFS MWFRS | Not required for gypsum/fiberboard sheathing, or wood-panel/steel-sheet sheathing on only one side with panel-edge spacing **more than 100 mm** o.c. | Conditional | Apply only to CFS lateral systems under the wind gate | Verified |
| 1705.12.3 | Cladding and roof wind SI | Periodic SI of fastening of roof covering/deck/framing connections, and of exterior wall covering and wall connections to roof and floor diaphragms and framing | 1705.12 wind gate | None stated beyond 1704.2 | Conditional | If the *V*/exposure gate is met, add façade and roof-fastening SI to the envelope specification | Verified |

## 9. Seismic-resistance special inspections and testing

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1705.13 Exception | Low-seismic SI waiver | 1705.13.1–1705.13.9 SI is not required for light-frame with *S_DS* **not more than 0.5** and height **not more than 10.5 m**; or reinforced masonry/concrete with *S_DS* **not more than 0.5** and height **not more than 7.5 m**; or detached one- or two-family dwellings **not exceeding two stories** without listed SBC 301 12.3 irregularities | Structures meeting a listed exception | A high-rise exceeds both **10.5 m** and **7.5 m** height limits; the dwelling exception is not this occupancy | Conditional | Do not apply the 1705.13 height waivers to this tower; still lock SDC/*S_DS* on the structural basis of design | Verified |
| 1705.13.1.1 | Steel SFRS seismic SI | Structural steel seismic force-resisting systems in SDC **B, C, D, E or F** shall be inspected to **AISC 341** quality assurance | Steel SFRS and SDC B–F | SDC **B or C** where the SBC 301 Table 12.2-1 “steel systems not specifically detailed for seismic resistance, excluding cantilever column systems” *R* row is used; SDC **D, E or F** where SBC 306 detailing is permitted by SBC 301 Table 15.4-1. Do not take *R* = 3 from commentary | Conditional | After SDC is locked, list AISC 341 SI unless a stated exception is demonstrated; do not import AISC 341 frequencies | Verified |
| 1705.13.1.2 | Steel collector/chord SI | Structural steel elements in the SFRS other than 1705.13.1.1 (struts, collectors, chords, foundation elements) in SDC **B–F** follow AISC 341 QA | Those steel elements | SDC **B or C** with *R* of **3 or less**; SDC **D, E or F** where detailing other than AISC 341 is permitted by SBC 301 Table 15.4-1 | Conditional | Identify collectors/chords on the SSI separately from the main steel SFRS | Verified |
| Unnumbered — page-split after 1705.13.1.2 | Wood SFRS seismic SI | For SFRS of structures assigned to SDC **C, D, E or F**: continuous SI during field gluing; periodic SI of nailing, bolting, anchoring and other fastening of wood SFRS elements | Wood SFRS in SDC C–F | Not required where lateral resistance is structural sheathing and panel-edge spacing is **more than 100 mm** on center. Published subsection number is missing in the extract | Conditional | Verify the printed 1705.13.2 number; apply only if a wood SFRS exists | Verify source |
| 1705.13.3 | CFS SFRS seismic SI | Periodic SI of SFRS welding and of screw/bolt/anchor/other fastening in SDC **C, D, E or F** | CFS light-frame SFRS | Gypsum/fiberboard sheathing; or one-sided wood-panel/steel-sheet sheathing with edge spacing **more than 100 mm** o.c. | Conditional | Apply only to CFS lateral systems in SDC C–F | Verified |
| 1705.13.4 | Designated seismic systems | In SDC **C, D, E or F**, the special inspector shall examine designated seismic systems requiring qualification under SBC 301 13.2.2 and verify label, anchorage and mounting against the certificate of compliance | Designated seismic systems | SBC 301 qualification criteria are not imported | Conditional | List designated seismic equipment on the SSI and collect 1704.5 Item 3 certificates | Verified |
| 1705.13.8 | Seismic isolation SI | Periodic SI during fabrication and installation of isolator units and energy-dissipation devices in seismically isolated structures in SDC **B–F** | Seismic isolation used | None stated | Conditional | Typical R-2 does not use isolation; open only if specified | Verified |
| 1705.13.9 | CFS special bolted moment frames | Periodic SI of CFS special bolted moment-frame installation in the SFRS of SDC **D, E or F** | That SFRS in SDC D–F | None stated | Conditional | Apply only if that system is selected | Verified |
| 1705.14.1.1–1705.14.1.2 | Steel seismic NDT | NDT of steel SFRS and of other steel SFRS elements in SDC **B–F** follows AISC 341 QA | Steel SFRS / steel SFRS elements | Same SDC/*R*/SBC 306 exception pattern as 1705.13.1.1–1705.13.1.2, including *R* of **3 or less** on elements in SDC B or C | Conditional | Pair NDT with the matching SI exception branch; do not import AISC 341 NDT rates | Verified |
| 1705.14.2 | Nonstructural seismic qualification | In SDC **B–F**, where SBC 301 13.2.1 Item 2 seismic qualification is used, the RDP shall specify qualification requirements on the construction documents and certificates of compliance shall be submitted per 1704.5 | Qualification path chosen instead of project-specific design | SBC 301 / AC 156 values are not imported | Conditional | If qualification (not design) is chosen, put the parameters on drawings and collect certificates | Verified |
| 1705.14.3 | Designated-system seismic tests | 1704.5 Item 3 requires certificates of compliance for designated seismic systems in accordance with Section 1705.14.3; that subsection is **not present** in the supplied extract (1705.14.2 is followed by 1705.14.4) | Designated seismic systems | No value is adopted from commentary or outbound SBC 301 | External verification | Verify published 1705.14.3 before specifying designated-system tests | Verify source |
| 1705.14.4 | Isolation-system tests | Seismic isolation systems in SDC **B–F** shall be tested in accordance with Section 17.8 of **SBC 301** | Seismically isolated structures | Commentary “two specimens” is not adopted | Conditional | Name SBC 301 17.8 on the SSI if isolation is used; do not import specimen counts | Verified |

## 10. Architectural and MEP seismic components

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1705.13.5 | Cladding and veneer SI | Periodic SI of erection and fastening of exterior cladding, interior and exterior nonbearing walls, and interior and exterior veneer in SDC **D, E or F** | Those components in SDC D–F | 1. Height **9 m or less** above grade or walking surface. 2. Exterior cladding and interior/exterior veneer **250 N/m² or less**. 3. Interior nonbearing walls **750 N/m² or less**. Commentary **720 N/m²** is not used | Conditional | After SDC is locked, SI tower façades above 9 m unless a weight exception is documented; use **750 N/m²** for interior walls | Verified |
| 1705.13.5.1 | Access-floor anchorage SI | Periodic SI of access-floor anchorage in SDC **D, E or F** | Raised access floors | None stated | Conditional | Apply to podium IT/MEP access floors if SDC D–F | Verified |
| 1705.13.6 Items 1–4 | Emergency power and hazardous MEP SI | Periodic SI of: emergency/standby electrical-equipment anchorage in SDC **C–F**; other electrical-equipment anchorage in SDC **E or F**; hazardous-material piping and associated mechanical units in SDC **C–F**; hazardous-material ductwork in SDC **C–F** | Those MEP systems and SDC | None stated beyond 1704.2 | Conditional | Put life-safety electrical gear and any hazardous MEP on the SSI once SDC is known | Verified |
| 1705.13.6 Item 5 | Vibration-isolation clearance SI | Periodic SI of vibration-isolation systems in SDC **C–F** where documents require a nominal clearance of **7 mm or less** between equipment support frame and restraint | Tight isolation clearance specified | Not required where the 7 mm clearance is not specified | Conditional | If isolated plant uses the reduced clearance, add SI; do not import SBC 301 force reductions | Verified |
| 1705.13.6 Item 6 | Sprinkler seismic clearance | Where automatic sprinklers are installed in SDC **C–F**, periodic SI shall verify either SBC 301 13.2.3 clearances (not imported) or a nominal clearance of **not less than 75 mm** between sprinkler drops/sprigs and non-supporting structure, attached equipment and other piping | Automatic sprinklers present | Flexible sprinkler hose fittings: clearance SI not required. Chapter 17 does not choose NFPA 13 vs 13R | Conditional | Coordinate sprinkler drops with structure and MEP; use the 75 mm branch or flexible hose; do not assume 13 vs 13R here | Verified |
| 1705.13.7 / Table 1705.13.7 | Storage-rack SI | Steel storage racks and steel cantilevered racks **2400 mm or greater** in height in SDC **D, E or F** shall have periodic SI per Table 1705.13.7 | Tall racks in SDC D–F | Flattened table cells are not adopted; not a typical apartment fit-out | Conditional | Open only if podium warehouse/retail racks meet the height and SDC gates; then verify the published table | Verify source |

## 11. Sprayed fire-resistant materials and intumescent coatings

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1705.15 (heading number page-split) | SFRM SI timing and sample cap | SFRM on floor/roof/wall assemblies and structural members shall be inspected and tested to 1705.15.1–1705.15.6 during construction, with an additional visual inspection after rough electrical, sprinkler, mechanical, plumbing and ceiling-suspension installation and before concealment; required sample size shall **not exceed 110 percent** of the referenced-standard sample in 1705.15.4.1–1705.15.4.9 | SFRM used for the fire-resistance design | Charging heading number is missing; 1705.15.1–1705.15.6 follow. Section 403.2.3 high-rise bond named only in commentary is not imported | Direct | If steel fireproofing is SFRM, schedule in-progress and post-rough visual SI and cap extra samples at 110 percent | Verified |
| 1705.15.1 | SFRM verification items | SI and tests shall include substrate condition, thickness, density in kg/m³, bond strength adhesion/cohesion, and finished-application condition | SFRM application | Listing and fire-resistance rating govern; kg/m³ is the published density unit, not a numeric limit | Direct | Put the five checks in the fireproofing specification | Verified |
| 1705.15.4 | SFRM thickness tolerance | **Not more than 10 percent** of thickness measurements may be less than the approved fire-resistance design thickness, and none shall be less than 1705.15.4.1 | SFRM thickness survey | 1705.15.4.1 floors apply to individual readings | Direct | Reject lots that miss design thickness on more than 10 percent of readings or that violate the individual floor | Verified |
| 1705.15.4.1 | Individual thickness floor | For design thickness **25 mm or greater**, minimum individual thickness is design thickness **minus 6.4 mm**. For design thickness **less than 25 mm**, minimum individual thickness is design thickness **minus 25 percent**. Determine thickness per ASTM E605 | Individual SFRM readings | Sampling locations in 1705.15.4.2–1705.15.4.3 | Direct | State both floors in the fireproofing QA sheet; do not import ASTM E605 sample rates except as this chapter modifies them | Verified |
| 1705.15.4.2 | Assembly thickness sampling | **Not less than four** measurements for each **93 m²** of sprayed area, or portion thereof, in each story, per ASTM E605 | Floor, roof and wall SFRM | None stated | Direct | Sample every 93 m² per story, not the larger ASTM default | Verified |
| 1705.15.4.3–1705.15.4.4 | Deck thickness patch | Thickness from a **300 mm by 300 mm** square; **not fewer than four** measurements, located symmetrically; fluted decks include valley, crest and sides and report the average | Cellular or fluted deck SFRM | None stated | Conditional | Use the 300 mm patch on metal-deck fireproofing | Verified |
| 1705.15.4.5–1705.15.4.9 | Member thickness sampling | Thickness testing on **not less than 25 percent** of structural members on each floor; measurements at each end of a **300 mm** length: beams/girders **nine** locations, joists/trusses **seven**, wide-flanged columns **12**, HSS/pipe columns **not fewer than four** | SFRM on structural members | None stated | Direct | Put member-type location counts in the QA procedure | Verified |
| 1705.15.5 | SFRM density sampling | Density **not less than** the approved fire-resistance design; ASTM E605; **not less than one** sample per **230 m²** (or portion) of sprayed assembly area in each story, and **not less than one** sample of each structural-member type per **230 m²** of floor area (or portion) in each story | SFRM density | None stated | Direct | Sample density on the 230 m² grid, separate from thickness patches | Verified |
| 1705.15.6 / 1705.15.6.1–1705.15.6.2 | SFRM bond strength | Cohesive/adhesive bond **not less than 7.2 kN/m²** by ASTM E736 field test; **not less than one** sample per **230 m²** of sprayed assembly area per story, and **not less than one** sample of each member type per **230 m²** of floor area per story | Cured SFRM | Primer/paint/encapsulant bond tests in 1705.15.6.3 where listing has not established bond. Do not import Section 403.2.3 high-rise bond from commentary | Direct | Specify 7.2 kN/m² as the Chapter 17 floor; ask the fire engineer whether 403 imposes a stricter outbound value | Verified |
| 1705.16 | Mastic and intumescent SI | SI and tests of mastic and intumescent fire-resistant coatings on structural elements and decks shall follow **AWCI 12-B**, based on the listed fire-resistance design, during construction, with additional visual inspection after rough MEP/sprinkler and before concealment | Intumescent/mastic fireproofing | AWCI 12-B values are not imported | Conditional | If intumescent is used instead of SFRM, name AWCI 12-B on the SSI | Verified |

## 12. Fire-resistant penetrations and joints

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1705.18 | Firestop and joint SI trigger | In high-rise buildings, in buildings assigned to Risk Category **III or IV**, or in fire areas containing Group R occupancies with occupant load **greater than 250**, SI is required for through-penetrations, membrane-penetration firestops, fire-resistant joint systems and perimeter fire-containment systems tested and listed to 714.4.1.2, 714.5.1.2, 715.3.1 and 715.4 | High-rise, or RC III/IV, or Group R fire area OL > 250 | The three triggers are independent. Commentary that concatenates “high-rise assigned to RC III or IV” is not used | Direct | Put firestop/joint/perimeter-containment SI on the SSI because the building is stated as high-rise; the OL > 250 branch is additional, not a substitute | Verified |
| 1705.18.1 | Penetration firestop inspection standard | Listed penetration firestops under 714.4.1.2 and 714.5.2 shall be inspected by an approved agency in accordance with **ASTM E2174** | 1705.18 trigger met | ASTM E2174 procedures/values are not imported | Direct | Name ASTM E2174 on the SSI and keep listed-system IDs on the firestop schedule | Verified |
| 1705.18.2 | Joint and perimeter inspection standard | Listed fire-resistant joint systems under 715.3.1 and 715.4 shall be inspected by an approved agency in accordance with **ASTM E2393** | 1705.18 trigger met | Includes curtain-wall/floor void systems discussed in the clause; ASTM E2393 values are not imported | Direct | Name ASTM E2393 for joints and perimeter containment; coordinate curtain-wall head-of-wall details | Verified |

## 13. Smoke-control testing

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1705.19 / 1705.19.1 | Smoke-control special inspector | Smoke-control systems shall be tested by a special inspector: (1) during duct erection and before concealment for leakage testing and device-location records; (2) prior to occupancy after sufficient completion for pressure-difference testing, flow measurements and detection/control verification | Smoke-control system provided | Section 909 quantitative leakage/pressure values are not imported | Conditional | If the fire strategy includes smoke control or smokeproof enclosures, appoint the 1705.19 inspector at the two stated stages | Verified |
| 1705.19.2 | Smoke-control inspector competence | Approved agencies for smoke-control testing shall have expertise in fire-protection engineering, mechanical engineering and certification as air balancers | 1705.19 testing | None stated | Conditional | Check agency CVs for all three competences before appointment | Verified |

## 14. EIFS, load tests and exterior window/door assemblies

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1705.17 | EIFS special inspection | Special inspections are required for all EIFS applications | EIFS used | 1. EIFS over a water-resistive barrier with a means of draining moisture to the exterior. 2. EIFS over masonry or concrete walls | Conditional | If barrier EIFS on stud walls is used, keep SI; drained EIFS or masonry/concrete substrate may take the exception | Verified |
| 1705.17.1 | WRB coating SI | A water-resistive barrier coating complying with ASTM E2570 requires SI of that coating when installed over a sheathing substrate | E2570 coating on sheathing | None stated | Conditional | If the Chapter 14 drainage EIFS option uses an E2570 coating, add coating SI | Verified |
| 1705.20 | Mass-timber sealant SI | Periodic SI of sealants or adhesives required by Section 703.7 applied to mass-timber elements designated on the approved construction documents | Mass timber with 703.7 sealant | 703.7 values are not imported | Conditional | Apply only on IV-A/B/C mass-timber projects | Verified |
| 1708.2.2 | Unspecified in-situ load test | Where no referenced load-test procedure exists: test load at least the specified factored design loads (non-SFRS); static load left **24 hours**; recovery **not less than 75 percent** of maximum deflection **within 24 hours** after removal; no evidence of failure; deflection not beyond 1604.3 (outbound) | In-situ test of existing/doubtful construction | Duration-sensitive materials adjusted; dynamic components held for a period consistent with function | Conditional | Use only if capacity is in doubt and no material-standard test applies; do not import 1604.3 limits | Verified |
| 1709.3.1 | Unspecified preconstruction load test | Superimposed test load **not less than two times** the superimposed design load, held **24 hours**; recovery **not less than 75 percent** within **24 hours** after removal; then reload to failure or **two and one-half times** the deflection-limit load or **two and one-half times** the superimposed design load; allowable load is the least of the deflection-limit load, failure load **divided by 2.5**, and maximum applied load **divided by 2.5** | Construction not designable by approved analysis / no standard test | 1709.3.2 sends deflection limits to 1604.3 (not imported) | Conditional | Use only for non-standard assemblies; keep the 2× / 2.5× / 75 percent / 24-hour sequence | Verified |
| 1709.5 | Window/door ASD conversion | For exterior windows and doors tested under 1709.5.1 or 1709.5.2, required design wind pressures from SBC 301 may be converted to allowable stress design by multiplying by **0.6** | Window/door wind-pressure rating | Alternate-size analysis/testing exception under AAMA 2502; SBC 301 pressures are not imported | Direct | Convert strength-level façade pressures by 0.6 only for these assembly tests; do not invent *V* | Verified |
| Unnumbered — following 1709.5 (commentary indicates 1709.5.1) | Labeled window/door assemblies | Exterior windows and sliding doors tested and labeled to AAMA/WDMA/CSA 101/I.S.2/A440; side-hinged doors labeled to that standard or 1709.5.2; labeled products not subject to 2403.2 and 2403.3 | Exterior windows and doors | Published 1709.5.1 heading is missing in the extract | Direct | Specify labeled AAMA/WDMA/CSA assemblies; verify the printed subsection number | Verify source |
| 1709.5.2 | ASTM E330 assembly test | Assemblies not under 1709.5.1 shall be tested to ASTM E330; glass complies with 2403; each assembly tested for **10 seconds** at **1.5 times** the Chapter 16 design pressure | Non-AAMA labeled path | Chapter 24 glass thickness not imported | Conditional | If the ASTM path is used, put 10 s / 1.5× in the test specification | Verified |
| 1709.5.2.1 | Garage and rolling doors | Tested to ASTM E330 or ANSI/DASMA 108 and meeting DASMA 108 pass/fail; permanent label with manufacturer, model, positive/negative design wind pressure, installation-drawing reference and test standard | Garage/rolling doors | Typical R-2 podium parking doors | Conditional | Require labeled DASMA/E330 doors on parking entries | Verified |
| 1709.5.3.1 | Windborne-debris shutters | Impact-protective systems tested to ASTM E1886 and E1996 for impact and ASTM E330 for design wind pressure; SBC 301 pressures multiplied by **0.6** for this section; permanent label per 1703.5.4 | Buildings in windborne-debris regions (1609.2, outbound) | Riyadh debris-region status is not determined in this chapter | Conditional | Open only if 1609.2 places the site in a debris region; then use the 0.6 conversion and labeled shutters | Verified |

## 15. Project-use controls

1. Use **Verified** rows for initial SSI and specification scoping after the row trigger and branch are confirmed.
2. Treat every **Verify source** row (flattened tables, 7.8 mm weld token, **17. MPa** OCR, missing 1705.13.2 / 1705.14.3 / 1709.5.1 headings) as a design hold point; no affected value is to be placed in issued-for-approval documents without a published-source check.
3. Do not apply the 1705.3 **three stories or less** concrete-footing waivers, or the 1705.13 **10.5 m / 7.5 m** seismic-SI waivers, to this high-rise.
4. Do not follow commentary that merges 1705.18 high-rise with Risk Category III/IV, or that restates interior-wall weight as **720 N/m²**.
5. Do not import SBC 304/305/306, AISC 341, ASTM E2174/E2393/E605, Section 909, Section 403.2.3 or Chapter 16 *V*/SDC values.
6. Record AHJ, SDC, wind, construction-type and fire-strategy decisions in the project Golden Thread; this matrix is not evidence of SCD NOC, structural observation close-out, or stamped compliance.

## 16. Coverage summary

Internal inventory of the attached Chapter 17 extract (numbered code, exceptions, tables, footnotes; commentary excluded). Row-level records are not published.

- **Inventory scope:** numbered code, exceptions, tables, footnotes (commentary excluded)
- **Total independently checkable numeric records:** 156
- **Verified:** 106
- **Verify source:** 50
- **Numeric records in Sections 1701, 1702, 1703, 1706 and 1707:** 0

### Counts by top-level section

| Top-level section | Records |
|---|---:|
| 1701 | 0 |
| 1702 | 0 |
| 1703 | 0 |
| 1704 | 4 |
| 1705 (body, excluding appended tables) | 87 |
| 1706 | 0 |
| 1707 | 0 |
| 1708 | 3 |
| 1709 | 13 |

### Appended-table coverage

| Appended table | Records | Verify source records |
|---|---:|---:|
| Table 1705.2.3 | 3 | 3 |
| Table 1705.3 | 22 | 22 |
| Table 1705.5.3 | 9 | 9 |
| Table 1705.6 | 5 | 5 |
| Table 1705.7 | 4 | 4 |
| Table 1705.8 | 2 | 2 |
| Table 1705.13.7 | 4 | 4 |

Coverage cross-check against `SBC 201 Chapter 17 Special Inspections and Tests (2024)_CS.md` was topics-only: owner-employed SI and SSI; high-rise structural observation; concrete/steel SI; firestop SI in high-rise / RC III–IV / Group R OL > 250. No CS.md value was copied into a matrix cell.

## 17. Unresolved-source register

Hold points for the 50 **Verify source** inventory records. Counts are record counts, not distinct numeric values. No value in this register is a design-release figure.

| Affected table / clause | Why unverified | Control note |
|---|---|---|
| 1705.3 Exception items 2–5 | Flattened list; items 3–5 appear un-nested; *f'c* printed as **17. MPa** | High-rise fails the three-storey gate; do not reconstruct IBC 2.1/2.2/2.3 numbering from memory; verify published exception if a separate low-rise structure is claimed |
| Table 1705.2.3 | 3 concatenated continuous/periodic cells | Verify published joist table before assigning periodic SI |
| Table 1705.3 | 20 concatenated C/P marks, Item 11 SDC text, and Item 2b “maximum **7.8 mm**” fillet-weld token | Do not repair 7.8 mm to another millimetre; verify published table before SSI frequencies |
| Table 1705.5.3 (cite also printed Table 1/705.5.3) | 9 concatenated C/P cells | Mass timber only; verify published table if Types IV-A/B/C are used |
| Table 1705.6 | 5 concatenated C/P cells | Use 1705.6 charging text and the **90 percent** density exception; verify table frequencies |
| Table 1705.7 | 4 concatenated continuous marks (items 1–4) | Verify published driven-pile table if that system is selected |
| Table 1705.8 | 2 concatenated continuous marks | Verify published CIP-pile table if that system is selected |
| Table 1705.13.7 | 4 concatenated periodic marks | Verify published rack table only if **2400 mm** racks in SDC D–F exist |
| Unnumbered wood SFRS SI (after 1705.13.1.2) | Subsection heading missing at page 1596 split | Mandatory SDC **C–F** / **100 mm** values retained; verify printed 1705.13.2 number |
| 1705.14.3 | Subsection absent (1705.14.2 jumps to 1705.14.4) while 1704.5 Item 3 cites it | No designated-system test values adopted |
| 1705.15 charging heading | Section number missing before “Sprayed fire-resistant materials” | 1705.15.1–1705.15.6 values retained; verify printed 1705.15 number |
| Unnumbered AAMA window labeling (after 1709.5) | 1709.5.1 heading missing | Labeling rule retained; verify printed subsection number |
