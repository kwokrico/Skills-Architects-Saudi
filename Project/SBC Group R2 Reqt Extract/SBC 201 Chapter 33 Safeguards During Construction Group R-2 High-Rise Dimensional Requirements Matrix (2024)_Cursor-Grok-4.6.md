# SBC 201 Chapter 33 Safeguards During Construction — Group R-2 High-Rise Dimensional Requirements Matrix (2024)

## 1. Document metadata and use limitation

- **Project basis:** Riyadh, Saudi Arabia; Group R-2 residential high-rise; an occupied floor is stated to be more than 23 m above the relevant reference level.
- **Deliverable tier:** Project-use matrices in Sections 4–12 (design-check rows, not pasted inventory), plus a coverage summary and unresolved-source register. The full row inventory is not published.
- **Code/source basis:** SBC 201 (2024), Chapter 33, source file `Reference\SBC 201 2024\source_reference\Chapter_33 — SAFEGUARDS DURING CONSTRUCTION.txt`.
- **Extraction audit:** Skill extract. Project-use rows follow the chapter-extract row contract (noun-phrase checks, bold SI values, building-language triggers, named exceptions, check-specific actions). Internal inventory: **60** independently checkable numeric records (**54** Verified, **6** Verify source). Flattened Table 3306.1 is listed in the register and is not a design-release value.
- **Model:** Cursor Grok 4.6.
- **Prepared:** 2026-08-27.
- **Status:** Source-only architectural advisory matrix for design coordination. It is not a stamped compliance statement, construction-safety plan, SCD NOC, SBPS approval, legal opinion, or permission to construct.
- **Outbound-source rule:** No value in this matrix has been imported from Chapter 9, 11, 16 or 18, Section 905, 906 or 111.3, SBC 303, 701 or 801 (including SBC 801 Chapter 33 and Appendix B), commentary examples, bibliography years, or the existing chapter summary. Where Chapter 33 sends the user elsewhere, this matrix records the dependency without supplying the outbound value.

### Scope and assumptions

1. Group R-2 and high-rise status are project statements, not independently verified classifications.
2. The exact Riyadh AHJ/permit pathway, project stage, fire-strategy status and SCD NOC status are unconfirmed; therefore this matrix does not conclude compliance.
3. Automatic sprinkler protection, mixed-use podium, storey count and construction type are unconfirmed. Chapter 33 does not branch on NFPA 13 versus 13R. Type I or II is treated as the expected tower path for 3313.4; Type III/IV/V fire-flow bands stay Conditional.
4. Occupied-building phasing, demolition of an existing structure, and combustible materials delivered to site are unconfirmed. Those branches select 3302, 3303, 3310.2, 3311.2 and 3313.2.
5. Table 3306.1 in the attached extract is concatenated HTML with a conflicting last-band protection type. No table cell is adopted. Numbered walkway, railing, barrier and covered-walkway dimensions in 3306.2–3306.7 remain usable once the table (or the AHJ) selects the protection type.
6. Commentary conversions (7200 Pa, 6 m, 3785 L/m) and commentary pointers (Section 1011, SBC 801 Appendix B, Appendix J) are not treated as code cells.

## 2. Legends

### Applicability

| Status | Meaning |
|---|---|
| **Direct** | Expected to govern the stated R-2 tower basis, subject to confirmed geometry and design data. |
| **Conditional** | Governs only when the stated feature, construction type, occupied-phasing, demolition or exception exists. |
| **Not typical** | Unrelated occupancy-only or two-story light-frame rule; omitted from this deliverable unless the gap register already opened that use. |
| **External verification** | Chapter 33 points to another section/code/standard, or OCR/AHJ must be confirmed first. |

### Source confidence

| Status | Meaning |
|---|---|
| **Verified** | Requirement and any stated numeric value were checked against unambiguous mandatory Chapter 33 source text. |
| **Verify source** | OCR, flattened table, page-split, or footnote attachment is unresolved. Not a design-release value. |

## 3. Project decision and gap register

| Decision / gap | Current project basis | Why it controls Chapter 33 application | Required project action |
|---|---|---|---|
| Occupied vs vacant construction | Unconfirmed whether any existing R-2, podium or neighbouring occupied structure stays occupied during work | 3302.1 and 3310.2 keep exits, structure, fire protection and sanitary safeguards live unless a numbered exception applies | Freeze a phasing drawing: occupied floors, substitute exits, and which fire systems remain in service |
| Construction type | Unconfirmed; high-rise R-2 typically Type I or II, not verified | 3313.4 is the Type I/II water-supply path; 3313.3.1–3313.3.3 apply only to Type III, IV or V using combustible materials | Lock type of construction before sizing construction-phase hydrants beyond 3313.2 / 3313.5 |
| Combustible materials on site | Unconfirmed cladding, formwork, packaging and finish stores | 3313.2 requires **1900 L/m** within **152 m** as soon as combustible building materials arrive, including on Type I/II sites | Plot material laydown versus hydrants on the construction logistics plan |
| Fire separation distance | Unconfirmed by lot line | Selects the Type III/IV/V fire-flow band if that construction type is used | Dimension FSD on the site plan before relying on 3313.3 |
| Standpipe / 905.3.1 | High-rise expected to need standpipes; Chapter 9 values not imported | 3311.1 and 3313.5 time the first standpipe and a **1900 L/m** hydrant within **30 m** of the FDC once construction exceeds **12 m** | Coordinate the construction standpipe with the 3310.1 stair and the FDC hydrant |
| Table 3306.1 protection type | Flattened HTML; last band lists both Barrier and None | Chooses construction railings (3306.4), site barriers (3306.5) and/or covered walkways (3306.7) | Verify the published table before freezing hoarding; do not reconstruct from IBC memory |
| Demolition | Unconfirmed whether an existing building is demolished | 3303, 3311.2 and demolition fire safety to SBC 801 Chapter 33 apply only if demolition occurs | Confirm demolition scope; do not drop vacant-lot, utility-cap or demolition-standpipe rows until that is closed |
| Excavation / adjoining buildings | Unconfirmed basement, shoring and neighbour setbacks | 3304 slopes, 3306.9 street-line barriers, 3307 notice and retention-system design lock the plot | Civil/structural to issue excavation, retention and 10-day neighbour-notice programme |
| Sprinkler / mixed use / storeys | Occupied floor stated above 23 m; sprinkler basis unconfirmed | 3312.1 blocks occupancy until a required sprinkler is tested and approved except as Section 111.3 allows | Fire engineer to lock Chapter 9; do not occupy on a temporary certificate without the 111.3 path |
| NOC / construction fire plan | SCD NOC and SBC 801 Chapter 33 operations unconfirmed | 3302.3, 3303.7 and 3309.2 send construction/demolition fire operations to SBC 801 | Engage the fire consultant for the construction fire-safety plan; do not import 801 values here |

## 4. Scope and occupied-building safeguards

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 3301.1 | Chapter construction-safety scope | This chapter governs safety during construction and protection of adjacent public and private properties | Construction or demolition of the building and adjoining property | None stated | Direct | Put Chapter 33 on the construction logistics and hoarding drawings, not only on the completed-building code sheet | Verified |
| 3301.2 | Equipment and material placement | Store and place construction equipment and materials so as not to endanger the public, workers or adjoining property for the duration of the project | Construction equipment or materials on or next to the plot | None stated | Direct | Show laydown, crane and skip locations clear of public ways, exits and adjoining structures | Verified |
| 3301.2.1 | Roof construction loads | Structural roof components shall support the roof-covering system and the material and equipment loads encountered during installation | Roof covering or reroofing installation | None stated | Conditional | Have the structural engineer confirm staging loads before stacking roof materials or equipment | Verified |
| 3302.1 | Occupied-building life-safety hold | Required exits, existing structural elements, fire protection devices and sanitary safeguards shall be maintained at all times during alterations, repairs or additions | Alteration, repair or addition while the building or a portion remains in use | Exception 1: adequate substitute provisions where the required element is itself being altered or repaired. Exception 2: maintenance not required where the existing building is not occupied | Conditional | On occupied-phasing drawings, keep each required exit and fire/sanitary device live or show the approved substitute | Verified |
| 3302.2 | Waste removal method | Remove waste so as to prevent injury or damage to persons, adjoining properties and public rights-of-way | Construction or demolition waste leaving the site | None stated | Direct | Specify enclosed chutes, covered skips and approved haul routes on the logistics plan | Verified |
| 3302.3 | Construction fire-safety companion | Fire safety during construction shall comply with this code and Chapter 33 of **SBC 801** | Construction operations | Numeric 801 criteria are not in this chapter | External verification | Name SBC 801 Chapter 33 on the construction fire plan; do not copy 801 values into this matrix | Verified |
| 3305.1 | Construction sanitary facilities | Provide sanitary facilities during construction, remodeling or demolition in accordance with **SBC 701** | Construction, remodeling or demolition activities | Numeric 701 fixture counts are not in this chapter | External verification | Show welfare facilities on the site plan and size them from SBC 701, not from this chapter | Verified |

## 5. Demolition

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 3303.1 | Demolition documents and schedule | Submit construction documents and a demolition schedule where the building official requires them. Do not start work until those documents or the schedule, or both, are approved | Demolition where the building official requires submittals | None stated | Conditional | Issue a demolition method statement and programme before site start if the AHJ asks for them | Verified |
| 3303.2 | Demolition pedestrian protection | Do not commence demolishing any building until pedestrian protection required by this chapter is in place | Demolition of any building | Protection type still depends on Table 3306.1, which is unresolved | Conditional | Install the verified hoarding/walkway before the first demolition activity | Verified |
| 3303.3 | Horizontal-exit substitution | Do not destroy a horizontal exit unless and until a substitute means of egress has been provided and approved | Demolition affecting a horizontal exit | Substitute egress requires building-official approval | Conditional | Keep party-wall exits usable, or obtain approval of the replacement route, before taking the wall down | Verified |
| 3303.4 | Vacant-lot restoration | Where a structure has been demolished or removed, fill and maintain the vacant lot to the existing grade or in accordance with the ordinances of the jurisdiction | Structure demolished or removed with no immediate rebuild occupying the grade | AHJ ordinances may set a different grade | Conditional | Restore grade to match adjoining ground unless the municipality states another profile | Verified |
| 3303.5 | Demolition water accumulation | Prevent accumulation of water or damage to any foundations on the premises or the adjoining property | Vacant or open demolition site | None stated | Conditional | Grade and drain the demolition plot so water cannot pond against this or neighbouring foundations | Verified |
| 3303.6 | Utility disconnection | Discontinue and cap service utility connections in accordance with approved rules and the applicable governing authority | Demolition of a served structure | Temporary retained services need separate AHJ permits (not quantified here) | Conditional | Coordinate cap-off certificates with each utility before demolition | Verified |
| 3303.7 | Demolition fire-safety companion | Fire safety during demolition shall comply with this code and Chapter 33 of **SBC 801** | Demolition operations | Numeric 801 criteria are not in this chapter | External verification | Add SBC 801 Chapter 33 to the demolition fire plan; do not import 801 blasting or demolition figures | Verified |

## 6. Site work, excavation and fill

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 3304.1 | Stump, root and formwork removal | Remove stumps and roots to not less than **300 mm** below the ground surface in the building footprint. Remove in-ground or sill-to-ground wood forms before occupancy or use. Remove loose or casual wood from direct contact with the ground under the building before completion | Excavation or fill for the building | None stated | Direct | Note the **300 mm** grubbing depth and formwork strip on foundation and completion checklists | Verified |
| 3304.1.1 | Permanent cut and fill slopes | Permanent fill and permanent excavation cut slopes shall be not steeper than **one unit vertical in two units horizontal (50-percent slope)** | Permanent fill or permanent excavation around the building | Cut slopes may be steeper only with a soil investigation report acceptable to the building official. The report path is not stated for fill | Direct | Draw finished and excavation slopes at **1:2** or flatter unless an accepted soils report justifies a steeper cut | Verified |
| 3304.1.2 | Surcharge and adjacent footings | Place no fill or other surcharge adjacent to a building unless that building can take the additional load. Underpin or otherwise protect existing footings or foundations affected by excavation against settlement and lateral movement | Fill, surcharge or excavation next to an existing structure | None stated | Direct | Keep stockpiles and plant off neighbouring foundations unless the structural engineer designs protection or underpinning | Verified |
| 3304.1.3 | Footings on adjacent slopes | For footings on adjacent slopes, see **Chapter 18** | Footings on or next to slopes | Chapter 18 values are not in this chapter | External verification | Send slope-footing geometry to the Chapter 18 structural criteria; do not invent setbacks here | Verified |
| 3304.1.4 | Fill supporting foundations | Fill used to support foundations shall comply with **SBC 303**. Special inspection of compacted fill shall be in accordance with **Section 1705.6** | Structural fill under foundations | Compaction criteria are not published in this chapter | External verification | Specify SBC 303 fill and 1705.6 inspection on the geotechnical notes; do not copy those values here | Verified |

## 7. Pedestrian protection trigger

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 3306.1 | Pedestrian protection and signs | Protect pedestrians during construction, remodeling and demolition as required by this chapter and Table 3306.1. Provide signs to direct pedestrian traffic | Construction, remodeling or demolition affecting pedestrians | Table 3306.1 cell values are not adopted from this extract | External verification | Provide directional signs; hold the protection *type* until the published table is verified | Verified |
| Table 3306.1 | Pedestrian protection type | No value adopted. Flattened HTML concatenates height of building, distance from construction to lot line and type of protection. Apparent bands include **2.4 m**, **1500 mm**, one-fourth / one-half of construction height, and types named construction railings, barrier, barrier and covered walkway, or none. The last “exceeding one-half the height” token lists both **Barrier** and **None** | Construction next to a lot line / public pedestrian route | Row pairing is unresolved; `rowspan` and the duplicated last band conflict | External verification | Do not select railing, barrier or covered walkway from this extract or from IBC memory; check the published table | Verify source |
| 3306.3 | Street directional barricade | Protect pedestrian traffic with a directional barricade where the walkway extends into the street, sized and built to direct vehicles away from the pedestrian path | Walkway projecting into the street | None stated | Conditional | Add a vehicle-facing barricade and traffic diversion where the temporary walkway occupies carriageway | Verified |
| 3306.8 | Pedestrian protection duration | Maintain required pedestrian protection in good order for as long as pedestrians are endangered. On completion, immediately remove walkways, debris and other obstructions and restore public property | Pedestrian protection required by this chapter | None stated | Direct | Keep hoarding on the programme until handover, then restore the public way | Verified |

## 8. Walkway, railing, barrier and excavation enclosure

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 3306.2 | Pedestrian walkway width and load | Provide a walkway in front of every construction and demolition site, and from an occupied-structure entrance or exit to a public way, of sufficient width but not less than **1.2 m**, with a durable surface, accessible per **Chapter 11**, designed for all imposed loads, live load not less than **7.2 kN/m²** | Construction or demolition frontage, or occupied building needing a route to a public way | Governing authority may authorise the sidewalk to be fenced or closed. Chapter 11 geometry is not imported | Direct | Dimension a **≥ 1.2 m** accessible temporary walkway at **7.2 kN/m²** on the hoarding plan, or obtain AHJ closure of the sidewalk | Verified |
| 3306.4 | Construction railing height | Construction railings shall be not less than **1.05 m** in height and sufficient to direct pedestrians around construction areas | Table 3306.1 (unverified) requires construction railings | Commentary guard/1015 notes are not adopted | Conditional | Once the table requires railings, set the rail at **≥ 1.05 m** and use it to steer pedestrians off the works | Verified |
| 3306.5 | Site barrier height and length | Barriers shall be not less than **2.4 m** in height, on the walkway side nearest the construction, for the entire length of the construction site. Protect openings with doors that are normally kept closed | Table 3306.1 (unverified) requires a barrier | None stated | Conditional | Once the table requires a barrier, draw a **≥ 2.4 m** continuous screen on the construction side with self-closing site doors | Verified |
| 3306.6 | Prescriptive barrier assembly | Design barriers for **Chapter 16** loads, or build them with **50 mm by 100 mm** top and bottom plates; boards not less than **19 mm** or wood structural panels not less than **6.4 mm**; exterior-type adhesive on wood structural panels; **6.4 mm** or **23.8 mm** panels with studs not more than **600 mm** on center; **9.5 mm** or **12.5 mm** panels with studs not more than **1200 mm** on center and a **50 mm by 100 mm** mid-height stiffener where studs exceed **600 mm**; **15.9 mm** or thicker panels spanning not more than **2400 mm** | Barrier required and the prescriptive timber path is used | Engineered Chapter 16 path needs no these member sizes; Chapter 16 values are not imported | Conditional | Either engineer the hoarding to Chapter 16 or match this member schedule on the barrier detail | Verified |
| 3306.7 | Covered walkway height and load | Covered walkways shall have a clear height of not less than **2.4 m** from floor to canopy, adequate lighting at all times, and a design live load of not less than **7.2 kN/m²** for the entire structure | Table 3306.1 (unverified) requires a covered walkway | Exception: new light-frame construction not exceeding **two stories** above grade plane may use **3.6 kPa** or the imposed load, whichever is greater, or a seven-item timber recipe not published in this matrix (not typical for this high-rise) | Conditional | If a covered walkway is required, keep **2.4 m** clear height and **7.2 kN/m²** on the canopy; do not take the two-story **3.6 kPa** path for the tower | Verified |
| 3306.9 | Excavation street-line barrier | Every excavation **1.5 m or less** from the street lot line shall be enclosed with a barrier not less than **1.8 m** in height. More than **1.5 m** from the street lot line, erect a barrier where the building official requires. Resist Chapter 16 wind pressure | Excavation on the plot | Distance **> 1.5 m** is building-official discretion. Chapter 16 wind values are not imported | Conditional | If the basement cut is within **1.5 m** of the street lot line, enclose it with a **≥ 1.8 m** wind-rated barrier | Verified |

## 9. Adjoining property and public ways

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 3307.1 | Adjoining-property protection | Protect adjoining public and private property during construction, remodeling and demolition, including footings, foundations, party walls, chimneys, skylights and roofs. Control water runoff and erosion | Work that can affect adjoining property | None stated | Direct | Show neighbour-protection, runoff and erosion control on the construction method statement | Verified |
| 3307.1 | Excavation neighbour notice | The person causing an excavation shall give written notice to owners of adjoining buildings that the excavation will be made and that those buildings should be protected, delivered not less than **10 days** before the scheduled start | Excavation that can affect adjoining buildings | None stated | Conditional | Issue the **10-day** written notice before excavation start and keep the proof on the Golden Thread | Verified |
| 3307.2–3307.2.3 | Excavation retention system | Where a retention system supports an excavation to protect adjacent structures, a registered design professional shall design vertical and lateral support; the design shall require monitoring of the system and adjacent structures for horizontal and vertical movement; remove or decommission elements only where backfill or the new structure provides adequate replacement support | Retention system used to protect adjacent structures | None stated | Conditional | Assign shoring to the RDP, specify movement monitoring, and do not strike props until replacement support is in | Verified |
| 3308.1 | Temporary public-property storage | Temporary use of streets or public property for storing or handling construction or demolition materials or equipment, and public protection, shall comply with the applicable governing authority and this chapter | Storage or handling on streets or public property | AHJ street-occupation rules are not in this chapter | Conditional | Obtain the municipality street-occupation permit before placing skips or plant in the public way | Verified |
| 3308.1.1 | Intersection and hydrant clearances | Do not place or store construction materials and equipment so as to obstruct fire hydrants, standpipes, fire or police alarm boxes, catch basins or manholes, nor within **6.1 m** of a street intersection, nor so as to obstruct traffic-signal observation or public-transit loading platforms | Materials or equipment on or next to the public way | None stated | Direct | Keep a **6.1 m** clear cone at intersections and keep hydrants, standpipes, alarms and manholes unobstructed on the logistics plan | Verified |
| 3308.2 | Utility-fixture access | Do not place materials, fences, sheds or other obstructions so as to block free approach to a fire hydrant, fire department connection, utility pole, manhole, fire alarm box or catch basin, or so as to interfere with gutter flow. Protect those fixtures but do not hide them from sight | Work near utility or fire fixtures | None stated | Direct | Keep FDCs, hydrants and manholes visible and approachable on every construction stage plan | Verified |

## 10. Construction egress, extinguishers, standpipes and sprinklers

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 3309.1 | Portable fire extinguishers | Provide not fewer than **one** approved portable fire extinguisher per **Section 906**, sized for not less than ordinary hazard, at each stairway on all floor levels where combustible materials have accumulated, in every storage and construction shed, and additional extinguishers where special hazards exist (flammable and combustible liquids) | Structure under construction, alteration or demolition | Section 906 ratings are not imported | Direct | Place ordinary-hazard extinguishers at working-level stairs, in every shed, and at fuel/solvent stores | Verified |
| 3309.2 | Construction fire-hazard companion | Observe this code and **SBC 801** to safeguard against fire hazards attendant upon construction operations | Construction operations | Numeric 801 criteria are not in this chapter | External verification | Cross-reference SBC 801 on hot-work and combustible-storage controls; do not copy 801 values here | Verified |
| 3310.1 | Construction stairway | Where construction exceeds **12 m** in height above the lowest level of fire department vehicle access, provide a temporary or permanent stairway and extend it to within **one floor** of the highest point of construction having secured decking or flooring | Tower construction above **12 m** (this high-rise basis) | Commentary Section 1011 geometry is not adopted | Direct | Keep a usable stair within **one floor** of the working deck once the frame passes **12 m** above FD access | Verified |
| 3310.2 | Occupied means of egress | Maintain required means of egress at all times during construction, demolition, remodeling or alterations and additions | Occupied building or portion during the works | Exception: existing means of egress need not be maintained where approved temporary means of egress systems and facilities are provided | Conditional | Keep required exits open on occupied floors, or obtain approval of the temporary egress scheme before blocking them | Verified |
| 3311.1 | Construction standpipe | In buildings required to have standpipes by **Section 905.3.1**, provide not fewer than **one** standpipe for use during construction, installed before construction exceeds **12 m** above the lowest level of fire department vehicle access, with hose connections adjacent to 3310.1 stairways, extended to within **one floor** of the highest secured decking or flooring | Building that 905.3.1 will require standpipes (expected high-rise path) | 905.3.1 thresholds are not imported | Direct | Install the first construction standpipe before **12 m**, next to the construction stair, and raise it with the working deck | Verified |
| 3311.2 | Demolition standpipe | Maintain an existing standpipe operable for the fire department during demolition. Do not demolish it more than **one floor** below the floor being demolished | Building being demolished that contains a standpipe | None stated | Conditional | During demolition, keep the standpipe live to **one floor** below the working demolition floor | Verified |
| 3311.3 | Standpipe installation standard | Install standpipes in accordance with **Chapter 9** | Construction or demolition standpipes under 3311 | Exception: temporary or permanent standpipes, with or without a water supply, are permitted if they conform to **Section 905** as to capacity, outlets and materials. Those 905 figures are not imported | External verification | Specify Chapter 9 / Section 905 capacity, outlets and materials on the construction standpipe; do not invent pipe sizes here | Verified |
| 3312.1 | Sprinkler completion before occupancy | Where this code requires an automatic sprinkler system, do not occupy any portion until the installation has been tested and approved, except as provided in **Section 111.3** | Required sprinkler building (unconfirmed until Chapter 9 is locked) | Temporary occupancy only via 111.3; 111.3 terms are not imported | Conditional | Do not occupy floors until the required sprinkler is tested and approved, unless a 111.3 temporary occupancy is granted | Verified |
| 3312.2 | Sprinkler valve control | Only authorised personnel may operate sprinkler control valves, with notification of designated parties. Where valves are turned off and on to connect new segments, check them at the end of each work period to confirm protection is in service | Sprinkler being extended or isolated during construction | None stated | Conditional | Write a valve-isolation permit and an end-of-shift “system in service” check into the construction fire plan | Verified |

## 11. Water supply for fire protection

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 3313.1 | Construction fire-flow timing | Provide an approved temporary or permanent fire-protection water supply as soon as combustible building materials arrive on site, on commencement of vertical combustible construction, and on installation of a standpipe, per 3313.2 through 3313.5 | Combustible materials on site, vertical combustible construction, or standpipe installation | Exception: the fire code official may reduce fire-flow for isolated rural or small-community buildings where full fire-flow is impractical. Commentary Appendix B **3785 L/m** is not adopted | Direct | Make hydrant water available before combustibles, combustible vertical work, or the standpipe — do not wait for building completion | Verified |
| 3313.2 | Combustible-materials fire flow | When combustible building materials of the building under construction are delivered, provide a minimum fire flow of **1900 L/m** from a hydrant within **152 m** of those materials, measured along an approved fire apparatus access lane. Add hydrants if one cannot cover all such materials | Combustible building materials delivered to the site (including Type I/II cladding or stores) | None stated | Direct | Place hydrants so every combustible laydown is within **152 m** along an approved fire-access lane at **1900 L/m** | Verified |
| 3313.3.1–3313.3.3 | Type III–V vertical fire flow | Before vertical construction of Type III, IV or V buildings that use any combustible building materials, provide hydrants to deliver: fire separation **less than 9 m** from lot lines (adjacent property built or buildable) — **1900 L/m** or the entire completed-building fire flow, whichever is greater; **9 m up to 18 m** — **1900 L/m** or **50 percent** of that completed fire flow, whichever is greater; **18 m or greater** — **1900 L/m** | Type III, IV or V vertical construction with combustible materials | Completed-building fire-flow value is not in this chapter. Not the default Type I/II tower path | Conditional | Use this band only if the podium or a structure is Type III–V; otherwise keep 3313.4 | Verified |
| 3313.4 | Type I/II vertical fire flow | If combustible building materials are delivered, provide water supply per 3313.2. Additional water supply for fire flow is not required before commencing vertical construction of Type I and II buildings | Type I or II construction (expected tower path) | 3313.2 still applies the moment combustibles arrive | Direct | For a Type I/II tower, do not add extra fire flow solely to start vertical work; still meet 3313.2 when combustibles are on site | Verified |
| 3313.5 | Standpipe hydrant supply | Where a standpipe is required by 3311, provide a water supply of not less than **1900 L/m** from a hydrant within **30 m** of the fire department connection supplying the standpipe, regardless of combustibles, construction type or fire separation distance | Construction standpipe required by 3311 | None stated | Direct | Locate a **1900 L/m** hydrant within **30 m** of the construction FDC before the standpipe is relied upon | Verified |

## 12. Fire watch

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 3314.1 | Nonworking-hours fire watch | Provide a fire watch during nonworking hours for construction that exceeds **12 m** in height above the lowest adjacent grade at any point along the building perimeter, for new multistory construction with an aggregate area exceeding **4645 m²** per story, or as required by the fire code official | Construction exceeding **12 m** at the perimeter, or a new multistory floor exceeding **4645 m²** | Fire code official may require a watch at other sizes | Direct | Programme a night/weekend fire watch once the perimeter height exceeds **12 m**, and also if any story exceeds **4645 m²** | Verified |

## 13. Project-use controls

1. Use **Verified** rows for initial construction-logistics scoping after the row trigger is confirmed (occupied phasing, demolition, excavation, combustibles on site, construction type).
2. Treat every **Verify source** row as a design hold. Table 3306.1 cells are empty of adopted values; do not reconstruct protection type from IBC memory or from the chapter summary.
3. Do not import Chapter 9 / 905 / 906 ratings, Chapter 11 walkway geometry, Chapter 16 wind or live loads, Chapter 18 slope-footing rules, Section 111.3 temporary-occupancy terms, SBC 303 compaction, SBC 701 fixture counts, or SBC 801 Chapter 33 / Appendix B fire-flow figures into issued drawings from this matrix.
4. Do not adopt commentary **7200 Pa**, **6 m**, **3785 L/m**, Section 1011 stair geometry, or bibliography years as code cells.
5. Do not apply the 3306.7 two-story light-frame **3.6 kPa** / seven-item timber recipe to this high-rise tower.
6. Record occupied-phasing, hoarding type, hydrant locations and fire-watch decisions in the project Golden Thread; this matrix is not evidence of SCD NOC or stamped compliance.

## 14. Coverage summary

Internal inventory of the attached Chapter 33 extract (numbered code, exceptions, tables, footnotes; commentary excluded). Row-level records are not published.

- **Inventory scope:** numbered code, exceptions, tables, footnotes (commentary excluded)
- **Total independently checkable numeric records:** 60
- **Verified:** 54
- **Verify source:** 6

### Counts by top-level section

| Top-level section | Records |
|---|---:|
| 3301 | 0 |
| 3302 | 0 |
| 3303 | 0 |
| 3304 | 3 |
| 3305 | 0 |
| 3306 | 34 |
| 3307 | 1 |
| 3308 | 1 |
| 3309 | 1 |
| 3310 | 2 |
| 3311 | 4 |
| 3312 | 0 |
| 3313 | 12 |
| 3314 | 2 |

Appended tables: Table 3306.1 contributes **6** Verify-source records (apparent protection-type rows). Numbered 3306 clauses contribute the remaining **28** of the 3306 total.

Coverage cross-check against `SBC 201 Chapter 33 Safeguards During Construction (2024)_CS.md` was topics-only: occupied-building phasing; pedestrian walkways/railings/barriers/covered walkways; Table 3306.1 mashed HTML; excavation/adjoining notice; construction hydrants, standpipes and fire watch. No CS.md value was copied into a matrix cell.

## 15. Unresolved-source register

| Affected table / clause | Why unverified | Control note |
|---|---|---|
| Table 3306.1 (6 records) | Concatenated HTML (`HEIGHT OF BUILDING…DISTANCE…TYPE OF PROTECTION…`) with `rowspan="4"`. Tokens name **2.4 m**, **1500 mm**, one-fourth / one-half height, construction railings, barrier, barrier and covered walkway, and none. The last “exceeding one-half the height of construction” fragment lists both **Barrier** and **None** | No table-cell value is adopted. Do not repair pairing from IBC memory or CS.md printed bands. Numbered 3306.4 / 3306.5 / 3306.7 dimensions may be used only after the published table (or the AHJ) selects the protection type |
