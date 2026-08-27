# SBC 201 Chapter 15 Roof Assembly — Group R-2 High-Rise Dimensional Requirements Matrix (2024)

## 1. Document metadata and use limitation

- **Project basis:** Riyadh, Saudi Arabia; Group R-2 residential high-rise; an occupied floor is stated to be more than 23 m above the relevant reference level.
- **Deliverable tier:** Project-use matrices in Sections 1–14 (design-check rows, not pasted inventory), plus a coverage summary and unresolved-source register. The full row inventory is not published.
- **Code/source basis:** SBC 201 (2024), Chapter 15, source file `Reference\SBC 201 2024\source_reference\Chapter_15 — ROOF ASSEMBLY.txt`.
- **Extraction audit:** Skill-finetune run. Project-use rows follow the chapter-extract row contract (noun-phrase checks, bold SI values, building-language triggers, named exceptions, check-specific actions). Internal inventory: **559** independently checkable numeric records (**234** Verified, **325** Verify source). Unresolved OCR is listed in the register and is not a design-release value.
- **Model:** Cursor Grok 4.6.
- **Prepared:** 2026-08-27.
- **Status:** Source-only architectural advisory matrix for design coordination. It is not a stamped compliance statement, roofing specification, SCD NOC, SBPS approval, legal opinion, or permission to construct.
- **Outbound-source rule:** No value in this matrix has been imported from Chapter 16, Section 1611, Section 705.11, Section 1202.2, Chapter 22, Chapter 24, Chapter 26, Table 601, SBC 701, SBC 801, SBC 301, ANSI/SPRI, UL/FM test criteria, commentary examples, or the existing chapter summary. Where Chapter 15 sends the user elsewhere, this matrix records the dependency without supplying the outbound value.

### Scope and assumptions

1. Group R-2 and high-rise status are project statements, not independently verified classifications.
2. The exact Riyadh AHJ/permit pathway, project stage, fire-strategy status and SCD NOC status are unconfirmed; therefore this matrix does not conclude compliance.
3. Type of construction, roof covering system, design slope, wind speed/exposure, parapet versus free-edge drainage, ballast/aggregate, occupied-roof/amenity program, penthouse use, cooling towers, PV and vegetative roofs are unconfirmed.
4. Ice-barrier and selected solid-sheathing clauses are printed **Not applicable in the Kingdom**; IBC ice-dam geometry is not filled in.
5. Table 1504.2, Table 1504.9, Table 1505.1, Tables 1507.1.1(1)/(2), Table 1507.3.7 and wood-exposure tables are concatenated OCR. No reconstructed cell is a design-release value.
6. Steep-slope wood, asphalt, slate and clay/concrete tile fastener inventories are omitted from lead tables unless a pavilion or steep roof is added (gap register).

## 2. Legends

### Applicability

| Status | Meaning |
|---|---|
| **Direct** | Expected to govern the stated R-2 tower basis, subject to confirmed geometry and design data. |
| **Conditional** | Governs only when the stated feature, covering, slope, construction type or rooftop structure exists. |
| **Not typical** | Unrelated occupancy-only or low-rise covering rule; omitted from this deliverable unless the gap register already opened that use. |
| **External verification** | Chapter 15 points to another section/code/standard, or OCR/AHJ must be confirmed before use. |

### Source confidence

| Status | Meaning |
|---|---|
| **Verified** | Requirement and any stated numeric value were checked against unambiguous mandatory Chapter 15 source text or an unambiguous table cell. |
| **Verify source** | OCR, flattened table, page-split, or footnote attachment is unresolved. Not a design-release value. |

## 3. Project decision and gap register

| Decision / gap | Current project basis | Why it controls Chapter 15 application | Required project action |
|---|---|---|---|
| Type of construction | Unconfirmed (high-rise R-2 often Type I, not verified here) | Locks Table 1505.1 class, penthouse height (unlimited on Type I vs **5500 mm** otherwise), equipment-screen combustible branches and 1511.2.4 fire-resistance exceptions | Issue a signed construction-type sheet before specifying roof class or penthouse walls |
| Roof covering and slope | Unconfirmed | Selects 1507.10–1507.14 low-slope membranes vs 1507.4 metal vs steep-slope 1507.2–1507.9; controls **2:12** edge-test and **1/4:12 (2-percent)** drainage slopes | Freeze covering system and design slope on the roof plan; do not mix steep-slope fastener tables into a membrane tower by default |
| Wind speed and exposure | Unconfirmed; Chapter 16 / SBC 301 not imported | Controls Table 1504.2 shingle class, Table 1504.9 aggregate parapets, 1507.1.1 underlayment wind branch and 1507.17.4.1 high-wind caps | Structural engineer to lock V, Vasd, exposure and mean roof height; verify published tables before using OCR cells |
| Parapet vs free edge | Unconfirmed | Secondary drains/scuppers apply where the perimeter can entrap water; aggregate roofs require Table 1504.9 parapets | Show primary and overflow drainage on every roof catchment; identify parapet/upstand vs dripping eaves |
| Ballast / aggregate | Unconfirmed | Triggers 1504.5 ANSI/SPRI RP-4, 1507.12.3 stone standards and Table 1504.9 parapet heights | State whether the membrane is adhered, mechanically attached or ballasted |
| Occupied roof / amenity | Unconfirmed | Weatherproofing, drainage, landscaped-roof fire design and rooftop-structure limits still apply; occupant-load/egress are outside this chapter | Coordinate occupied-roof finishes with 1507.15 / 1505.10 if landscaped; keep Chapter 10/11 geometry out of this matrix |
| Penthouse program | Unconfirmed | **One-third** deck-area cap, use limits (MEP/tanks/elevators/shafts only) and Type I FSD rating exceptions | Schedule enclosed rooftop area vs roof deck; do not program habitable amenity as a 1511.2 penthouse |
| Cooling towers / screens | Unconfirmed | Noncombustible trigger at **23 m²** / **4.6 m** / roof **> 15 m**; screens **5.5 m** (Type IA unlimited) | Roof MEP layout to flag tower base area and screen height vs construction type |
| PV / vegetative | Unconfirmed | 1505.8–1505.10 and 1507.15–1507.17 add listing and outbound SBC 801 / 1607.14.2.2 / Table 601 | Confirm PV and landscaped-roof scope before specifying fire class and structural fire resistance |
| New vs reroof | Assumed new construction | 1512 waives **2-percent** slope and 1502.2 overflow only for existing roofs that already drain | Treat 1512 as inactive unless an existing covering is being recovered or replaced |
| NOC / roof specification | Unconfirmed | Wind tests, listing and SCD acceptance cannot be concluded from Chapter 15 text alone | Engage the qualified local/roofing/fire consultants before design freeze |

## 4. Drainage and overflow

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1502.1 | Roof drainage design | Roof drainage design and installation shall comply with this section, **Section 1611** and **Chapter 11 of SBC 701** | All roof assemblies | No numeric drain sizing is stated in this chapter | External verification | Size primary drains from 1611 and SBC 701; do not invent millimetre or rainfall values here | Verified |
| 1502.2 | Secondary overflow drainage | Where roof drains are required, secondary (emergency overflow) drains or scuppers are required where perimeter construction can entrap water if primary drains back up; install and size overflow to **Section 1611** and **SBC 701 Chapter 11** | Roof perimeter can pond | Overflow is not required where the roof cannot pond (free-draining edge) | Direct | Provide a second drain path at every parapet or upstand catchment; keep 1611 ponding depth on the structural drawing | Verified |
| 1502.3 | Scupper opening | Scuppers sized so ponding does not exceed the **1611.1** design depth; opening dimension **not less than 100 mm**; ignore primary-system flow when locating and sizing | Scuppers used as secondary drainage | No other numeric opening stated | Direct | Detail scupper width/height ≥ **100 mm** and set inlet elevation from the structural ponding limit, not from the primary drain | Verified |
| 1502.4 | External gutters and leaders | Gutters and leaders on the outside of the building shall be noncombustible or minimum **Schedule 40** plastic pipe | External gutters/leaders | Group R-3, private garages and Type V construction are excepted | Direct | Specify noncombustible or Schedule 40 plastic leaders on the tower; do not use the R-3/Type V branch | Verified |

## 5. Weather protection and parapet copings

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1503.1 | Roof covering required | Roof decks shall be covered with approved roof coverings secured per this chapter, this code and the manufacturer's approved instructions | All roof decks | None stated | Direct | Show a listed covering on every deck, including canopies and low roofs | Verified |
| 1503.2–1503.2.1 | Flashing locations and metal | Flash to prevent water entry at copings, permeable materials, parapet intersections and penetrations; flash wall/roof intersections, gutters, slope/direction changes and openings. Metal flashing: corrosion-resistant, thickness **not less than 0.48 mm** (No. 26 galvanized) | Discontinuities in the roof plane | None stated | Direct | Schedule corrosion-resistant metal flashing ≥ **0.48 mm** at every roof/wall, gutter, change-of-slope and penetration | Verified |
| 1503.3–1503.3.2 | Parapet coping | Cope or cover parapets so the top surface provides positive drainage. Weatherproof covering width **not less than** the parapet thickness; rated parapets required by **705.11** shall not have their fire-resistance rating decreased | Parapet walls | 1503.3.2 covers parapets that meet a 705.11 exception; still require full-width coping | Direct | Slope the coping to the roof and keep the cap width ≥ wall thickness; coordinate rating with 705.11 without importing that section's heights | Verified |
| 1503.4 | Attic and rafter vents | Intake and exhaust vents per **Section 1202.2** and the vent manufacturer's instructions | Attic or rafter cavity requiring ventilation | No vent area is stated in this chapter | External verification | Size vents from Chapter 12; do not copy 1202.2 ratios into this matrix | Verified |
| 1503.5 | Cricket or saddle | Cricket or saddle on the ridge side of any chimney or penetration **greater than 760 mm** wide measured perpendicular to the slope; covering of sheet metal or the same material as the roof covering | Penetration or chimney > **760 mm** across slope | Unit skylights installed per **2405.5** and flashed per manufacturer may omit the cricket | Conditional | Provide a cricket upslope of wide chimneys, shafts and equipment curbs; record the skylight exception only for listed unit skylights | Verified |

## 6. Wind, edge and impact performance

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1504.1 | Wind resistance of roofs | Roof decks and coverings shall be designed for wind loads in accordance with **Chapter 16** and 1504.2–1504.5 | All roof decks and coverings | No Chapter 16 pressures are stated here | External verification | Put component-and-cladding uplift on the structural/roofing spec; do not import 1609 values | Verified |
| 1504.3.1.3 | Clay/concrete tile lift coefficient | Lift coefficient for concrete and clay tile shall be **0.2**, or determined per SBCCI SSTD 11 or ASTM C1570 | Clay or concrete roof tile | Used only if tile is selected | Conditional | If tile appears on a pavilion, adopt **0.2** or a tested coefficient; not a default tower membrane check | Verified |
| 1504.4 | Mechanically attached or adhered covering | Coverings under 1507 that are mechanically attached or adhered shall resist design wind load pressures for components and cladding per **1609.5.2**; allowable stress design wind load is permitted | Non-ballasted 1507 covering | Structural metal panels follow 1504.4.2 (ASTM E1592 / FM 4474 / UL 580) with cold-formed steel and aluminium design exceptions to **2210.1** / **2002.1** | Direct | Require listed wind-uplift tests on the membrane or metal-panel specification; keep 1609 calculation outbound | Verified |
| 1504.5 | Ballasted low-slope single-ply | Ballasted low-slope (roof slope **< 2:12**) single-ply coverings installed per 1507.12 shall be designed per **ANSI/SPRI RP-4** | Ballasted single-ply, slope < **2:12** | No RP-4 ballast weights are stated here | Conditional | If stone ballast is used, design to RP-4; do not invent bag or stone weights | Verified |
| 1504.6–1504.6.1 | Low-slope edge and gutter tests | Metal edge systems (except gutters and counterflashing) on BUR, modified bitumen and single-ply with slope **less than 2:12** shall be designed for Chapter 16 wind and tested to ANSI/SPRI ES-1 RE-1, RE-2 and RE-3 (V from Figures 1609.3(1)–(4)). Gutters that secure the membrane edge on the same low-slope systems: Section 1609 plus SPRI GT-1 G-1 and G-2 | Low-slope membrane roofs < **2:12** | Gutters and counterflashing are excluded from the ES-1 edge-system sentence; GT-1 applies only where the gutter secures the membrane | Direct | Specify ES-1 tested copings/fascia and GT-1 tested gutters on the typical membrane tower edge | Verified |
| 1504.7 | Low-slope weathering | Low-slope coverings (slope **< 2:12**) per 1507 shall demonstrate physical integrity based on **2,000 hours** accelerated weathering (ASTM G152, G154 or G155) | Low-slope 1507 covering | Cyclical flexural membranes must not show significant tensile/breaking-strength loss | Direct | Require the **2,000-hour** weathering listing on the membrane submittal | Verified |
| 1504.8 | Low-slope impact | Low-slope coverings (slope **< 2:12**) shall resist impact per ASTM D3746, ASTM D4272 or FM 4470 foot-traffic | Low-slope 1507 covering | No impact energy is stated in this chapter | Direct | Require an impact-test listing on the membrane spec; do not import commentary dart masses | Verified |
| 1504.9 | Aggregate-surfaced parapet | Parapets shall be provided for aggregate-surfaced roofs and shall comply with Table 1504.9 | Aggregate-surfaced roofs | Table grid is concatenated OCR — no millimetre row adopted | Conditional | If gravel/slag surfacing is used, provide a parapet and verify the published table before setting height | Verified |
| Table 1504.9 notes c–d | Gravel stop and Exposure D | Where the table height is **50 mm**, a gravel stop ≥ **50 mm** from the roof surface and ≥ aggregate height is permitted. Exposure D: add **200 mm** to Exposure C height, and not less than **300 mm** | Aggregate roofs using Table 1504.9 | Interpolation of height and wind is permitted (note a); V and exposure from **1609** (note b) | Conditional | Use these footnote rules only after the published table cell is verified; do not reconstruct the OCR grid | Verified |
| Table 1504.2 | Steep-slope shingle wind class | Classification vs maximum basic / allowable-stress wind speed cannot be unambiguously segmented from the concatenated table | Asphalt, metal or PV shingles tested to ASTM D3161 / D7158 / UL 7103 | Footnote a: ASTM D7158 calculations assume Exposure B or C and building height **18 m or less**; additional calculations outside those assumptions | External verification | Verify the published table before assigning a D/G/H or A/D/F class; high-rise height typically exceeds the **18 m** footnote assumption | Verify source |
| Table 1504.9 | Aggregate parapet height grid | Minimum parapet height (mm) vs aggregate size, mean roof height and wind cannot be read from the flattened HTML | Aggregate-surfaced roofs | Notes c–d above remain usable once the cell is known | External verification | Hold all millimetre grid values until a published Table 1504.9 is checked | Verify source |

## 7. Fire classification

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1505.1 | Roof-assembly class test | Class A, B and C assemblies required to be listed shall be tested to ASTM E108 or UL 790; fire-retardant-treated wood roof coverings also ASTM D2898. Minimum covering class per Table 1505.1 by construction type | Roof assemblies | Skylights and sloped glazing complying with **Chapter 24** or **Section 2610** are excepted from this fire classification | Direct | Specify a listed Class A/B/C assembly matching construction type; keep skylight fire rules on Ch. 24 / 2610 | Verified |
| 1505.2 | Class A use and deemed-to-comply | Class A assemblies are effective against severe fire-test exposure, shall be listed/identified Class A, and are permitted on **all types of construction**. Exceptions (no listing required): brick, masonry or exposed concrete; ferrous/copper/metal sheets and shingles, clay/concrete tile or slate on noncombustible decks (or metal sheets without a deck on noncombustible framing); copper sheets **minimum 4.9 kg/m²** over combustible decks; slate over ASTM D226 Type II over combustible decks | Class A covering | Exceptions 1–4 are deemed Class A without ASTM E108 listing | Direct | Prefer a listed Class A membrane on the tower; if using copper over combustible deck, schedule **≥ 4.9 kg/m²** | Verified |
| 1505.3–1505.5 | Class B, C and nonclassified | Class B: moderate exposure, listed Class B. Class C: light exposure, listed Class C. Nonclassified: approved material not listed as A, B or C | Coverings other than Class A | Table 1505.1 (not commentary) sets the minimum class by construction type | Direct | Do not assume Class C is available on a high-rise Type I plate; verify Table 1505.1 | Verified |
| Table 1505.1 | Minimum class by construction type | Appended table is concatenated (`IA…VB` with `BBBC°BC°BBC°` tokens). No construction-type class letter is adopted | All buildings | Notes below are readable; Urban Wildland / Appendix D may impose a stricter class | External verification | Verify the published Table 1505.1 against the locked construction type before specifying Class B vs C | Verify source |
| Table 1505.1 notes | Nonclassified and cedar-shake limits | Nonclassified coverings permitted on Group **R-3** and **U** with fire-separation distance **≥ 1.8 m** from the leading edge of the roof. Cedar/redwood No. 1 shakes/shingles per 1505.7: not more than **two stories**, projected roof **≤ 560 m²**, FSD **≥ 3.0 m** to lot lines except street/public way | Those limited buildings only | Not a Group R-2 high-rise path | Not typical | Do not apply R-3/U nonclassified or two-storey cedar notes to this tower | Verified |
| 1505.7 | Special-purpose wood underlayment | Underlayment of **16 mm** Type X water-resistant gypsum backing board or gypsum sheathing under minimum nominal **12.5 mm** wood structural panel solid sheathing or **25 mm** nominal spaced sheathing | Special-purpose wood shingle/shake roofs per 1507.8 / 1507.9 | Buildings permitted to use this construction are those in Table 1505.1 note (two-storey / **560 m²**) | Not typical | Omit from the tower covering spec unless a qualifying special-purpose wood roof is added | Verified |

## 8. Low-slope coverings typical of towers

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1507.10.1 | Built-up roof slope | Design slope **not less than one-fourth unit vertical in 12 units horizontal (2-percent slope)**, except coal-tar built-up **not less than one-eighth unit vertical in 12 units horizontal (1-percent slope)** | Built-up roofs | Coal-tar branch is the only lower-slope exception in this clause | Direct | Set BUR drainage slope to **2-percent** unless a coal-tar specification is locked at **1-percent** | Verified |
| 1507.10.2 | Built-up materials | BUR materials shall comply with Table 1507.10.2 or UL 55A | Built-up roofs | Table 1507.10.2 is a standards list (no dimensional cells) | Direct | Call the applicable ASTM/UL 55A standard on the BUR spec | Verified |
| 1507.11.1–1507.11.2 | Modified-bitumen slope and materials | Design slope **not less than one-fourth unit vertical in 12 units horizontal (2-percent slope)**. Materials: ASTM D6162, D6163, D6164, D6222, D6223, D6298 or D6509. Base sheet may be 1507.11.2, ASTM D1970 or ASTM D4601 | Modified-bitumen roofs | None stated | Direct | Set mod-bit slope to **2-percent** and list a named ASTM product | Verified |
| 1507.12.1–1507.12.2 | Single-ply slope and materials | Design slope **not less than 1/4 unit vertical in 12 units horizontal (2-percent slope)**. Materials per Table 1507.12.2 (CSPE/PIB, EPDM, KEE, PVC, TPO) | Single-ply roofs | None stated | Direct | Set single-ply slope to **2-percent** and name the ASTM membrane | Verified |
| 1507.12.3 | Ballasted stone | Ballasted low-slope roofs (slope **< 2:12**) installed per this section and 1504.5; stone ballast ASTM D448 or ASTM D7655 | Ballasted single-ply < **2:12** | RP-4 design remains outbound | Conditional | If ballast is used, specify ASTM D448/D7655 stone and the 1504.5 RP-4 design | Verified |
| 1507.13.1–1507.13.4 | SPF slope, coating window and foam | SPF design slope **not less than one-fourth unit vertical in 12 units horizontal (2-percent slope)**. Foam ASTM C1029 Type III or IV or ASTM D7425. Liquid-applied protective coating per Table 1507.13.3 applied **not less than 2 hours nor more than 72 hours** after foam. Foam plastics also **Chapter 26** | Sprayed polyurethane foam roofs | Chapter 26 values are not imported | Conditional | If SPF is used, hold **2-percent** slope and the **2–72 hour** coating window on the application spec | Verified |
| 1507.14.1–1507.14.2 | Liquid-applied slope | Liquid-applied roofing design slope **not less than one-fourth unit vertical in 12 units horizontal (2-percent slope)**; ASTM C836, C957 or D3468 | Liquid-applied roofs | None stated | Conditional | If liquid-applied, set slope to **2-percent** and name the ASTM coating | Verified |
| 1507.4.2 | Metal panel minimum slope | Lapped non-soldered seams without lap sealant: **three units vertical in 12 (25-percent slope)**. With approved lap sealant: **one-half unit vertical in 12 (4-percent slope)**. Standing-seam: **one-quarter unit vertical in 12 (2-percent slope)** | Metal roof panels | Deck may be spaced supports where the covering is so designed (1507.4.1) | Conditional | If metal panels are used, pick the matching slope branch; standing-seam at **2-percent** is the low-slope tower option | Verified |
| 1507.4.3 | Metal covering standards | Metal-sheet systems with supporting members: **Chapter 22**. Coverings over structural decking: Table 1507.4.3(1); corrosion resistance Table 1507.4.3(2) | Metal-sheet roof coverings | Table 1507.4.3(1) copper masses `0.0416 kg/m²` / `0.0312 kg/m²` are treated as OCR-suspect | Conditional | Use readable aluminium **0.61 mm** / **0.48 mm**, zinc **0.7 mm** and lead masses from the table; verify copper masses against the published table | Verify source |
| 1506.3 | Product identification | Roof-covering materials delivered in packages bearing manufacturer marks and approved-agency labels required by 1505; bulk shipments by certificate or bill of lading | All 1506/1507 materials | None stated | Direct | Require labeled bundles/rolls on site and in the submittal | Verified |

## 9. Insulation, coatings and radiant barriers

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1508.1 | Above-deck insulation fire test | Above-deck thermal insulation permitted where covered with an approved roof covering and the assembly passes **NFPA 276** or **UL 1256** | Above-deck insulation | (1) Foam plastic per **Chapter 26**. (2) Concrete or composite metal-and-concrete deck with approved covering — NFPA 276/UL 1256 not required for that non-foam case | Direct | Require NFPA 276 or UL 1256 on steel-deck insulation assemblies; send foam to Chapter 26; document the concrete-deck exception if used | Verified |
| 1508.2 | Insulation material standards | Above-deck thermal insulation board shall comply with Table 1508.2 | Above-deck insulation board | Table is a standards list | Direct | Name the ASTM C552 / C578 / C1289 (etc.) product on the insulation spec | Verified |
| 1509.1–1509.2 | Roof coatings | Installing a roof coating on a covering shall comply with 1505 and this section; materials per Table 1509.2 | Roof coatings | Coatings still need a 1505 fire class where required | Conditional | If recoating, list ASTM D6083 / D1227 / D2823 / D4479 / D2824 / D6694 / D6947 as applicable and keep 1505 class | Verified |
| 1510.2–1510.4 | Above-deck radiant barrier | Permitted where covered with an approved covering and the radiant-barrier-plus-covering system complies with **FM 4550** or **UL 1256**. Low-emittance surface shall face the continuous airspace between barrier and covering. Material: ASTM C1313/1313M | Radiant barrier above the deck | None stated | Conditional | If used, orient the low-e face to the airspace and require FM 4550 or UL 1256 on the combined system | Verified |

## 10. Rooftop structures

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1511.1.1 | Enclosed rooftop area | Aggregate area of penthouses and other enclosed rooftop structures **shall not exceed one-third** the area of the supporting roof deck. Such structures need not be included in building area or storey count per **503.1**, nor in the **901.7** fire area | Penthouses and enclosed rooftop structures | Exceeding one-third means the enclosure is treated as an additional storey (per the code's penthouse definition path in 1511.2) | Direct | Schedule enclosed roof area vs deck area and keep the sum ≤ **one-third** | Verified |
| 1511.2–1511.2.2 | Penthouse height and use | Penthouses complying with 1511.2.1–1511.2.4 are a portion of the storey below; others are an additional storey. Height above roof deck, measured to average penthouse roof: **not more than 5500 mm** except on **Type I** (unlimited). Use limited to shelter of mechanical/electrical equipment, tanks, elevators and related machinery, or vertical shaft openings, including ancillary access to elevators and stairways | Penthouses | Exception: tanks or elevators that travel to the roof — maximum **8500 mm** on non-Type I | Direct | On a Type I tower, height is unlimited but use remains MEP/shafts only; do not occupy a 1511.2 penthouse as amenity | Verified |
| 1511.2.3 | Penthouse weather protection | Louvers, louver blades or flashing shall protect mechanical/electrical equipment and the building interior from the elements | Penthouses with openings | None stated | Direct | Detail weatherproof louver/flashing at penthouse intakes and doors | Verified |
| 1511.2.4 Ex. 1 | Type I penthouse rating vs FSD | Type I penthouses: exterior walls and roofs with fire separation distance **> 1.5 m and < 6 m** may have **not less than a 1-hour** rating; FSD **6 m or greater** — no fire-resistance rating required | Type I construction penthouses | Base rule: penthouses constructed as required for the building's construction type | Conditional | Apply the **1.5 m / 6 m / 1-hour** branch only after construction type and FSD are locked | Verified |
| 1511.2.4 Ex. 2 | Low Type I or Type II penthouse FRT | On Type I **two stories or less** above grade plane, or Type II: FSD **> 1.5 m and < 6 m** — **not less than 1-hour** (or lesser per Table 705.5) and FRT wood permitted; FSD **≥ 6 m** — FRT wood, no rating; interior framing/walls may be FRT wood | Type I ≤ 2 stories or Type II | Not the high-rise Type I path | Not typical | Do not use the two-storey/Type II FRT branch on a high-rise Type I tower | Verified |
| 1511.2.4 Ex. 3 | Type III/IV/V penthouse walls | Exception 3 text is OCR-repeated and page-split; remaining limits are not adopted | Type III, IV or V penthouses | Not readable | External verification | Verify published 1511.2.4 Exception 3 before any Type III–V penthouse wall rating | Verify source |
| 1511.3–1511.3.2 | Roof tanks | Clauses 1511.3, 1511.3.1 and 1511.3.2 are missing after the page 1487–1488 split (next numbered code is 1511.3.3) | Roof tanks | Commentary about tanks over stairs/elevators is **not adopted** | External verification | Verify published 1511.3–1511.3.2 before locating tanks; do not use commentary as the requirement | Verify source |
| 1511.3.3 | Unenclosed tank cover | Unenclosed roof tanks shall have covers sloping toward the perimeter of the tanks | Unenclosed roof tanks | None stated | Conditional | Slope the tank cover to shed rain at the perimeter | Verified |
| 1511.4 | Cooling-tower construction | Cooling towers on the roof with base area **> 23 m²** or height **> 4.6 m** above the roof, where the roof is **> 15 m** above grade plane, shall be noncombustible. Base area **shall not exceed one-third** of the supporting roof deck | Roof cooling towers meeting the size/height/roof-height triggers | Exception: drip boards and enclosing construction may be wood **not less than 25 mm** nominal if covered on the exterior with noncombustible material | Conditional | If a tower exceeds **23 m²** or **4.6 m** on a roof **> 15 m**, specify noncombustible construction and keep base area ≤ **one-third** | Verified |
| 1511.5 | Towers, spires, domes, cupolas | Construction type fire-resistance not less than the building. If **> 26 m** above grade plane to the highest point **and** either **> 18.6 m²** horizontal area **or** used for other than a minaret or architectural embellishment: construct of and support on Type I or II | Towers/spires/domes/cupolas | Minaret / architectural-embellishment use avoids the Type I/II trigger when the area/height pair is not met | Conditional | Classify rooftop minarets vs occupied towers; if both **26 m** and **18.6 m²**/non-embellishment apply, require Type I or II | Verified |
| 1511.5.1 | Noncombustible tower separation | Greater than **18 m** above roof contact, or **> 18.6 m²** at any horizontal section, or used other than minaret/embellishment, or on a building **> 1.5 m** in building height: noncombustible construction and support, separated by **not less than 1.5 hours** with openings per **711**. On a building **> 15 m** in building height: supported by noncombustible construction | Qualifying towers/spires/domes/cupolas | The **1.5 m** building-height token sits beside a **15 m** token in the same paragraph and is treated as unresolved OCR | Conditional | Use **18 m**, **18.6 m²**, **1.5-hour** and **15 m** as printed; verify the **1.5 m** building-height trigger against the published clause | Verify source |
| 1511.6–1511.6.1 | Mechanical equipment screens | Screens constructed of exterior-wall materials for the building's construction type. FSD **> 1.5 m**: fire-resistance rating not required. Height **not more than 5.5 m** above the roof deck, except unlimited on **Type IA** | Mechanical equipment screens | Fences (1511.7.4) use the same rules | Direct | Limit screen height to **5.5 m** unless Type IA; drop the rating when FSD **> 1.5 m** | Verified |
| 1511.6.2 | Combustible screens on I–IV | On Type I, II, III or IV roofs, combustible screens permitted if any one of: (1) FSD **≥ 6 m** and height **≤ 1200 mm**; (2) FSD **≥ 6 m** and FRT wood for exterior installation; (3) panels flame spread index **25 or less** (ASTM E84 or UL 723, each face) and NFPA 285 as tested | Combustible screen on Type I–IV | Item 3 requires installation as tested | Conditional | If a combustible screen is proposed on the tower, pick one numbered limitation and show FSD/height/FRT/NFPA 285 on the detail | Verified |
| 1511.6.3 | Type V screen height | Type V screens may exceed maximum building height where FSD **> 1500 mm** and one of: FSD **≥ 6 m** with **1200 mm** extra height; noncombustible; FRT wood; or FSD **≥ 6 m** with flame spread **25 or less** | Type V buildings | Not the typical high-rise construction type | Not typical | Do not apply Type V height increases to a Type I tower | Verified |
| 1511.7.1 | Aerial supports | Aerial supports shall be noncombustible, except combustible permitted where height **not greater than 3650 mm** from roof deck to the highest point | Aerial supports | Height exception as stated | Conditional | Keep aerials noncombustible, or limit combustible supports to **≤ 3650 mm** | Verified |
| 1511.7.2 | Bulkheads | Bulkheads sheltering MEP or shaft openings comply as penthouses (1511.2); any other purpose is an additional storey | Bulkheads | None stated | Conditional | Treat stair/MEP bulkheads as 1511.2 penthouses | Verified |
| 1511.7.5 | Flagpoles | Flagpoles and similar structures need not be noncombustible and are not limited in height or number | Flagpoles | None stated | Conditional | Flagpoles are exempt from 1511 height/combustibility caps | Verified |
| 1511.8 | Roof supporting rooftop structures | Structural frame and roof construction supporting rooftop-structure loads shall comply with **Table 601**. The fire-resistance reduction in Table 601 Note a **shall not apply** to roofs containing rooftop structures | Any rooftop structure on the roof | Table 601 hours are not imported | External verification | Tell the structural/fire pack that Note a reduction is off; verify Table 601 hours outside this chapter | Verified |

## 11. PV, BIPV and landscaped roofs

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1505.8 | BIPV fire class | BIPV products installed as the roof covering shall be tested, listed and labeled for fire classification per 1505.1 | BIPV as covering | ASTM E108 / UL 790 path via 1505.1 | Conditional | If BIPV is the covering, require a 1505.1 fire-class listing | Verified |
| 1505.9 | Rooftop PV fire class | Rooftop-mounted PV panel systems tested, listed and identified with a fire classification per **UL 2703**; install per listing and manufacturer. Fire classification shall comply with Table 1505.1 | Rooftop-mounted PV | Table 1505.1 cells remain Verify source | Conditional | Require UL 2703 class matching the verified Table 1505.1 construction-type minimum | Verified |
| 1505.10 | Landscaped-roof fire design | Landscaped roofs shall comply with 1505.1 and 1507.15 and be installed per **ANSI/SPRI VF-1** | Landscaped roofs | VF-1 criteria are not imported | Conditional | If a roof garden is provided, specify ANSI/SPRI VF-1 and 1505.1 class | Verified |
| 1507.15–1507.15.1 | Vegetative / landscaped roof | Vegetative and landscaped roofs shall comply with this chapter, **Section 1607.14.2.2** and **SBC 801**. Supporting frame and roof construction shall comply with **Table 601** | Vegetative or landscaped roofs | No live-load or 801 values imported | Conditional | Coordinate structural live load (1607.14.2.2), SBC 801 and Table 601 without copying those numbers here | Verified |
| 1507.16.2 / 1507.16.5 | Photovoltaic shingles | Install on slopes **not less than two units vertical in 12 (2:12)**. Fasteners: galvanized, stainless, aluminium or copper roofing nails, minimum 12-gage (**2.67 mm**) shank, **9 mm** minimum head, penetrating **not less than 19 mm** into sheathing (through-sheathing if thinner) | Photovoltaic shingles | Ice barrier not applicable in the Kingdom | Conditional | If PV shingles are used, hold **2:12** slope and the **2.67 mm / 9 mm / 19 mm** nail rule | Verified |
| 1507.16.8 | PV shingle wind class | Photovoltaic shingles shall comply with Table 1504.2 for the appropriate maximum nominal design wind speed | Photovoltaic shingles | Table 1504.2 is concatenated OCR | External verification | Verify published Table 1504.2 before assigning the shingle class | Verify source |
| 1507.17.2–1507.17.4.1 | BIPV panel slope and high-wind underlayment | BIPV panels only on slopes **two units vertical in 12 (2:12) or greater**. Underlayment shingle-fashion from the eave, lapped **50 mm**. Where Vad **> 49 m/s**: overlap fasteners **not more than 900 mm** oc. Where Vad **≥ 54 m/s**: ASTM D226 Type III, D4869 Type IV or D6757; grid **300 mm** with **150 mm** at side laps; all laps **not less than 100 mm**; cap nails/staples with head **≥ 25 mm**, metal cap **≥ 0.25 mm**, plastic cap edge **≥ 0.89 mm**, ring-shank **≥ 2.11 mm**, smooth-shank **≥ 2.31 mm**, staple **≥ 21 gage (0.81 mm)**, penetration through sheathing or **≥ 19 mm** | BIPV roof panels | Adhered underlayment ASTM D1970 is an alternative. Ice barrier not applicable in the Kingdom | Conditional | If BIPV panels are used, lock **2:12** and apply the Vad **49 / 54 m/s** underlayment branch from Chapter 16 Vasd | Verified |

## 12. Kingdom deletions and reroofing

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1507.1.2 and siblings | Ice barrier | Printed **Not applicable in the Kingdom** (1507.1.2, 1507.2.7, 1507.5.4, 1507.6.4, 1507.7.4, 1507.8.4, 1507.9.4, 1507.16.4, 1507.17.4.2) | Steep-slope underlayment ice-dam clauses | Do not import IBC ice-barrier millimetres | Direct | Omit ice-barrier strips from KSA specifications; do not fill IBC eave-ice geometry | Verified |
| 1507.8.1.1 / 1507.9.1.1 | Solid sheathing for ice | Printed **Not applicable in the Kingdom** | Wood shingle/shake ice-area solid sheathing | None | Direct | Do not require the IBC ice-area solid-sheathing extra | Verified |
| Table 1507.3.7 note b | Tile attachment climate note | Printed **Not applicable to KSA** | Clay/concrete tile Table 1507.3.7 | Remainder of the table is flattened OCR | Conditional | If tile is used, verify the published table; do not apply note b | Verified |
| 1512.1 Ex. 1 | Existing low-slope recover slope | Roof replacement or recover of existing low-slope coverings need not meet the **one-quarter in 12 (2-percent slope)** in 1507 where the roof provides positive roof drainage | Existing low-slope reroof | New construction still uses 1507 slopes | Conditional | Use only on existing covers that already drain; do not waive **2-percent** on new tower roofs | Verified |
| 1512.1 Ex. 2 | Existing overflow waiver | Recovering or replacing an existing covering need not meet 1502.2 secondary drains/scuppers where the roof provides positive drainage; existing required overflow shall not be removed unless replaced to 1502.2 | Existing reroof with positive drainage | New construction still needs 1502.2 where the perimeter can entrap water | Conditional | Do not delete existing overflow on a reroof unless a 1502.2 replacement is installed | Verified |
| 1512.2 | Roof replacement | Roof replacement shall include removal of all existing layers of roof assembly materials down to the roof deck | Roof replacement | Exception printed **Not applicable in the Kingdom** | Conditional | Tear off to deck on replacement; do not use a Kingdom-deleted remaining-layer exception | Verified |
| 1512.2.1.1 | Recover prohibited | Roof recover not permitted where the existing roof is water-soaked/deteriorated, is slate/clay/cement/asbestos-cement tile, or has **two or more** applications of any covering | Proposed recover | 1512.2.1 lists conditions where recover is otherwise permitted | Conditional | If recovering, confirm fewer than two existing coverings and a sound, dry substrate | Verified |

## 13. Steep-slope coverings (only if used)

Steep-slope asphalt, tile, metal shingle, mineral-surfaced roll, slate, wood shingle and wood shake systems are not typical of a Group R-2 high-rise membrane roof. The following rows apply only if the gap register opens a pavilion, canopy or steep roof. Fastener-count tables and weather-exposure grids that are OCR-flattened are not dumped here.

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1507.2.2 | Asphalt shingle slope | Asphalt shingles only on slopes **2:12 (17-percent)** or greater; **2:12 to 4:12 (33-percent)** requires double underlayment per 1507.1.1 | Asphalt shingles | Underlayment tables 1507.1.1(1)–(2) are flattened OCR | Conditional | If asphalt is used, hold **2:12** minimum and double underlayment below **4:12**; verify published underlayment tables | Verified |
| 1507.2.5–1507.2.6 | Asphalt fasteners | Nails: 12-gage (**2.7 mm**) shank, **9.5 mm** minimum head, **19 mm** into sheathing (through if thinner). Not fewer than **four** fasteners per strip shingle or **two** per individual shingle; slopes exceeding **21:12** per manufacturer | Asphalt shingles | Manufacturer may require more fasteners, not fewer | Conditional | Put **four**/strip and **19 mm** penetration on the asphalt detail | Verified |
| 1507.2.8.3 | Asphalt drip edge | Drip edge at eaves and rakes; adjacent segments lapped **not less than 50 mm**; vertical leg **not less than 38 mm** and **not less than 6.5 mm** below sheathing; back on the roof **not less than 50 mm**; fastened **not greater than 300 mm** oc. Underlayment over drip edge at eaves; drip edge over underlayment at rakes | Asphalt shingle eaves and rakes | None stated | Conditional | Detail the **50 / 38 / 6.5 / 50 / 300 mm** drip-edge geometry | Verified |
| 1507.3.2 | Clay/concrete tile slope | Tile on slopes **2-1/2:12 (21-percent)** or greater; **2-1/2:12 to 4:12 (33-percent)** requires double underlayment | Clay or concrete tile | Solid sheathing required except spaced lumber in SDC A, B and C (1507.3.1) | Conditional | If tile is used, hold **2½:12** and double underlayment below **4:12** | Verified |
| 1507.3.6 | Tile fasteners and perimeter | Corrosion-resistant fasteners, not less than 11-gage, **8.0 mm** head, penetrating the deck **not less than 19 mm** or through, whichever is less. Attaching wire **not smaller than 2.1 mm**. Perimeter fastening: three tile courses but **not less than 900 mm** from hips, ridges, eaves and gable rakes | Clay or concrete tile | Table 1507.3.7 fastening schedule is flattened OCR | Conditional | Use the **8.0 mm / 19 mm / 2.1 mm / 900 mm** prose rules; verify published Table 1507.3.7 before wind-speed fastening | Verified |
| 1507.5.2 / 1507.5.7 | Metal shingle slope and valley | Metal shingles not below **3:12 (25-percent slope)**. Valley flashing **at least 200 mm** each way from centreline, splash rib **not less than 19 mm**, end lap **not less than 100 mm**; cement underlayment or self-adhered sheet for slopes under **7:12 (58-percent)** | Metal roof shingles | None stated | Conditional | If metal shingles are used, hold **3:12** and the **200 / 19 / 100 mm** valley | Verified |
| 1507.6.2 | Mineral-surfaced roll slope | Not applied on slopes below **one-unit vertical in 12 (8-percent slope)** | Mineral-surfaced roll roofing | None stated | Conditional | If roll roofing is used, hold **8-percent** minimum slope | Verified |
| 1507.7.2 / 1507.7.6 | Slate slope and headlap | Slate only on slopes **4:12** or greater; **two** fasteners per slate; headlap per Table 1507.7.6 (**100 mm** / **75 mm** / **50 mm** by slope band) | Slate shingles | Table 1507.7.6 slope/headlap tokens are readable | Conditional | If slate is used, hold **4:12**, two fasteners, and the table headlap | Verified |
| 1507.8.2 / 1507.8.7 | Wood shingle slope and spacing | Wood shingles on slopes **not less than 3:12 (25-percent)**. Side lap **not less than 40 mm**; spacing **6 to 9 mm**; weather exposure not more than Table 1507.8.7 | Wood shingles | Table 1507.8.7 is rowspan-concatenated OCR; table spacing **6.4 to 9.5 mm** conflicts with the clause | Conditional | Use clause **6 to 9 mm** and **40 mm** side lap; verify published Table 1507.8.7 before exposure | Verify source |
| 1507.9.2 / 1507.9.8 | Wood shake slope and spacing | Wood shakes on slopes **not less than 4:12 (33-percent)**. Side lap **not less than 40 mm**; spacing **9 to 16 mm** (naturally durable) or **6 to 9 mm** (preservative taper sawn); exposure per Table 1507.9.8 | Wood shakes | Table 1507.9.8 is concatenated OCR | Conditional | Use the clause spacing limits; verify published Table 1507.9.8 before exposure | Verify source |
| Tables 1507.1.1(1)–(2) | Underlayment type and application | Type/application vs covering and V **62.5 m/s** cannot be unambiguously read (headers show both V > and V ≥ **62.5 m/s**; cells concatenated) | Steep-slope underlayment | 1507.1.1 Exception 2 grid **300 mm** / **150 mm** / laps **100 mm** / offset **1800 mm** remains readable in the exception prose | External verification | Prefer the 1507.1.1 exception prose for cap-nail underlayment; verify published Tables 1507.1.1(1)–(2) | Verify source |

## 14. Project-use controls

1. Use **Verified** rows for initial coordination after the row trigger and branch are confirmed.
2. Treat every **Verify source** row as a design hold point; no affected OCR table cell is to be placed in issued-for-approval drawings without a published-source check.
3. Do not reconstruct Table 1505.1 class letters or Table 1504.9 millimetre grids from commentary, CS.md or memory.
4. Do not import Section 1611 rainfall, SBC 701 drain sizing, 705.11 parapet fire heights, 1202.2 vent ratios, Chapter 16 pressures, Table 601 hours, or SBC 801 landscaped-roof values.
5. Do not apply R-3/U nonclassified roofs, two-storey cedar-shake notes, Type V screen-height increases, or ice-barrier geometry to this R-2 high-rise.
6. Record covering system, construction type, wind and rooftop-structure decisions in the project Golden Thread; this matrix is not evidence of SCD NOC or stamped compliance.

## 15. Coverage summary

Internal inventory of the attached Chapter 15 extract (numbered code, exceptions, tables, footnotes; commentary excluded). Row-level records are not published.

- **Inventory scope:** numbered code, exceptions, tables, footnotes (commentary excluded)
- **Total independently checkable numeric records:** 559
- **Verified:** 234
- **Verify source:** 325
- **Numeric records in Sections 1501, 1506, 1508, 1509 and 1510:** 0 (1508–1510 name tests/standards without independent SI limits)

### Counts by top-level section

| Top-level section | Records |
|---|---:|
| 1501 | 0 |
| 1502 | 2 |
| 1503 | 2 |
| 1504 | 211 |
| 1505 | 17 |
| 1506 | 0 |
| 1507 | 288 |
| 1508 | 0 |
| 1509 | 0 |
| 1510 | 0 |
| 1511 | 37 |
| 1512 | 2 |

### Appended-table coverage

| Appended table | Records | Verify source records |
|---|---:|---:|
| Table 1504.2 | 33 | 32 |
| Table 1504.9 | 171 | 168 |
| Table 1505.1 | 13 | 9 |
| Table 1507.1.1(1) | 1 | 1 |
| Table 1507.1.1(2) | 36 | 36 |
| Table 1507.1.1(3) | 2 | 0 |
| Table 1507.2.8.2 | 16 | 0 |
| Table 1507.3.7 | 48 | 35 |
| Table 1507.4.3(1) | 17 | 5 |
| Table 1507.4.3(2) | 1 | 1 |
| Table 1507.7.6 | 3 | 0 |
| Table 1507.8 (spacing conflict) | 2 | 2 |
| Table 1507.8.7 | 18 | 18 |
| Table 1507.9.8 | 15 | 12 |
| Tables 1507.10.2 / 1507.12.2 / 1507.13.3 / 1508.2 / 1509.2 | 0 | 0 |

Coverage cross-check against `SBC 201 Chapter 15 Roof Assembly (2024)_CS.md` was topics-only: roof class, parapets, drainage/scuppers, outbound 1611 / SBC 701 / 705.11. No CS.md value was copied into a matrix cell.

## 16. Unresolved-source register

Hold points for the 325 **Verify source** inventory records. Counts are record counts, not distinct numeric values. No value in this register is a design-release figure.

| Affected table / clause | Why unverified | Control note |
|---|---|---|
| Table 1504.2 | 32 concatenated wind-speed / classification cells (`STREWS`, merged D/G/H classes) | Verify published table before shingle or PV-shingle class; footnote **18 m** height assumption is readable and typically exceeded on a high-rise |
| Table 1504.9 | 168 flattened parapet-height cells (6 mean-height rows × 2 aggregate sizes × 14 wind columns as marked in the extract HTML) | Do not reconstruct millimetre rows; footnotes c–d (**50 mm** gravel stop, Exposure D **+ 200 mm** / **≥ 300 mm**) may be used only after the published cell is known |
| Table 1505.1 | 9 concatenated construction-type class tokens including degree-symbol `C°` | Do not adopt CS.md/commentary Class C mapping; verify the published table against construction type |
| 1507.1.1 Exception 2 | 1 thickness token `0.25` with no unit | Verify published cap-thickness unit before specifying power-driven metal caps from the exception |
| Table 1507.1.1(1) | 1 wind-speed header (V > **62.5 m/s** and V ≥ **62.5 m/s** both printed) | Verify which column is the low-wind vs high-wind type list |
| Table 1507.1.1(2) | 36 flattened underlayment-application numbers with OCR (`not forever than`, slope-band mix-ups) | Prefer 1507.1.1 exception prose; verify published application table if steep-slope is added |
| Table 1507.3.7 | 35 concatenated tile-fastening cells | Use 1507.3.6 prose fasteners; verify published table before wind-speed nailing |
| Table 1507.4.3(1) | 5 copper mass cells (`0.0416` / `0.0312` kg/m²) inconsistent with 1505.2 **4.9 kg/m²** copper | Verify published copper masses; aluminium **0.61 / 0.48 mm** and zinc **0.7 mm** remain usable |
| Table 1507.4.3(2) | 1 coating-row OCR (`505%` vs 5% aluminium-alloy) | Verify published corrosion-resistance row |
| Table 1507.8 | 2 spacing tokens (**6.4 to 9.5 mm**) that conflict with 1507.8.7 **6 to 9 mm** | Use the clause spacing; verify the published installation table |
| Table 1507.8.7 | 18 rowspan-concatenated weather-exposure cells | Verify published shingle exposure before cutting shingles |
| Table 1507.9.8 | 12 concatenated shake-exposure cells | Verify published shake exposure; footnote a (**600 mm** × **9.5 mm**, **190 mm**) is readable |
| 1511.2.4 Exception 3 | 4 unreadable Type III/IV/V penthouse-wall limits (repeated OCR, page split) | Verify published Exception 3; do not use Type I Exception 1 as a substitute for III–V |
| 1511.3–1511.3.2 | Page-split: tank clauses missing after Exception 3 OCR; no numeric tank limits recovered from the extract | Verify published 1511.3–1511.3.2; do not promote commentary about tanks over stairs/elevators |
| 1511.5.1 | 1 building-height token **1.5 m** adjacent to **15 m** in the same paragraph | Verify published trigger; keep **18 m**, **18.6 m²**, **1.5-hour** and **15 m** as printed elsewhere in the clause |
