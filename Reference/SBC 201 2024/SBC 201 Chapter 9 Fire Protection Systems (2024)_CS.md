# SBC 201 Chapter 9 Fire Protection Systems
**Architect critical summary for schematic design**
2024 | SBCNC

> Scope note: This chapter specifies **where** fire protection and life safety systems are required in **new** buildings and the design/installation/operation criteria for those systems. Periodic testing, inspection, and existing-building rules are **SBC 801**. Kitchen exhaust / Type I hoods and hazardous exhaust ducts are scoped here but detailed in **SBC 501** and SBC 801 §609. Detached one- and two-family dwellings and townhouses ≤ 3 stories with a separate means of egress are **not Group R** under these triggers — they go to **SBC 1101/1102**. Installation standards: **NFPA 13 / 13R / 13D** (sprinklers), **NFPA 14** (standpipes), **NFPA 72** (alarms). Code prevails over those standards where they differ (102.4).

## Regulatory Overview
Occupancy group, fire-area size, occupant load, and height relative to the level of exit discharge (LED) set automatic sprinklers (903.2), standpipes (905), and fire alarms (907); high-rise sprinklers and fire command centers are charged by Chapter 4 (403.3) and 911, not by a separate height table in this chapter. A system installed to take a code reduction is a **required** system (901.2) and must be monitored per NFPA 72.

## Critical main topics and subtopics

### 1. Fire areas that bound sprinkler and alarm thresholds (901.7, 706 / 707 / 711)
To stay under a 903.2 or 907.2 limit, divide the building into fire areas with **fire walls (706)**, **fire barriers (707)**, **horizontal assemblies (711)**, or a combination, rated not less than **Table 707.3.10**. Exterior walls also bound a fire area. Mixed-use separations under 508.4 are often **weaker** than fire-area ratings — two occupancies can sit in one fire area and both 903.2 tests still apply. Commentary to 907.2.1 treats the Table 707.3.10 rating for Group A fire areas as **2 hours**.

**SD takeaway:** Fire-area walls are a schematic compartmentation decision, not a late rating note — if you intend to avoid sprinklers, lock Table 707.3.10 barriers (and exits that do not share) before the plan is frozen.

### 2. Automatic sprinklers — occupancy fire-area triggers (903.2.1–903.2.10)
Approved automatic sprinklers in **new** buildings where **any** listed condition exists (903.2). Telecom equipment rooms with smoke detection and 1-hour barriers / 2-hour floors are the only general occupancy exception (903.2). Alternative 904 systems may replace sprinklers for the occupancy trigger but **do not** unlock sprinkler trade-offs (903.1.1).

When Group A is triggered, sprinkle the **story containing the A occupancy and all stories from that occupancy down to and including the LED** serving it.

| Occupancy | Trigger (any one) | Exceptions / notes |
|-----------|-------------------|--------------------|
| **A-1** 903.2.1.1 | Fire area **> 1115 m²**; OL **≥ 300**; fire area **not on LED**; **multitheater complex** | Sprinkle story + stories to LED |
| **A-2** 903.2.1.2 | Fire area **> 465 m²**; OL **≥ 100**; fire area **not on LED** | Same coverage as A-1 |
| **A-3** 903.2.1.3 | Fire area **> 1115 m²**; OL **≥ 300**; fire area **not on LED** | **Detached mosque, Type I or II: sprinklers not required** |
| **A-4** 903.2.1.4 | Fire area **> 1115 m²**; OL **≥ 300**; fire area **not on LED** | Same coverage as A-1 |
| **A-5** 903.2.1.5 | Enclosed accessory use **> 100 m²** (per space, not aggregate) | Open seating itself not sprinkled |
| Grandstand/bleacher enclosed space 903.2.1.5.1 | Area **> 100 m²**, or **≤ 100 m²** and not built to 1030.1.1.1 | NFPA 13 |
| Roof assembly 903.2.1.6 | Occupied roof OL **> 100** (A-2) or **> 300** (other A) | Sprinkle floors between roof and LED; roof itself not required. **Open parking, Type I or II: exempt** |
| Multiple A fire areas 903.2.1.7 | A-1/A-2/A-3/A-4 share exit or exit access **and** combined OL **≥ 300** | Separate exits can keep fire-area strategy |
| **Ambulatory care (B)** 903.2.2 | **≥ 4** care recipients incapable of self-preservation, **or any** such recipient **not on LED** | Entire floor; if not on LED also floors below + to nearest LED. Open parking floors exempt |
| **E** 903.2.3 | Fire area **> 1115 m²**; fire area **not on LED**; OL **≥ 300** | Below-LED omit if every classroom has a ground-level exterior exit door |
| **F-1** 903.2.4 | Fire area **> 1115 m²**; fire area **> 3 stories** above grade plane; **combined** F-1 fire areas (all floors + mezzanines) **> 2230 m²** | Woodworking **> 230 m²** in the fire area (903.2.4.1); upholstered furniture/mattress manufacture fire area **> 230 m²** (903.2.4.3) |
| **H** 903.2.5.1 | **All** Group H | H-5 design Table 903.2.5.2; pyroxylin **> 45 kg** (903.2.5.3) |
| **I** 903.2.6 | **Throughout buildings** with a Group I fire area | I-1 Condition 1: 13R permitted. I-4 at LED with exterior door from every care room: omit. I-4 not on LED: NFPA 13 on care floor + floors to LED + floors below (open parking omit) |
| **M** 903.2.7 | Same three tests as F-1 (1115 / > 3 stories / 2230 combined) | High-piled/rack storage → **SBC 801**. Display/sale of upholstered furniture or mattresses fire area **> 465 m²** (903.2.7.2) |
| **R** 903.2.8 | **Throughout all buildings with a Group R fire area** — no area/OL/story minimum | **SBC 1101/1102 dwellings are not Group R.** R-3 and R-4 Condition 1: 13D permitted. R-4 Condition 2: 13R permitted. Care ≤ 5 persons in a single-family dwelling: 13D permitted |
| **S-1** 903.2.9 | Same three tests as F-1, **plus** commercial motor vehicle storage fire area **> 465 m²** | Repair garages: 2+ stories incl. basement with garage fire area **> 930 m²**; 1-story **> 1115 m²**; vehicles in basement; commercial MV repair **> 465 m²**. Tires **> 565 m³** volume → NFPA 13 throughout. Upholstered storage fire area **> 230 m²** (1-story self-storage with all units exterior-accessed exempt) |
| **S-2 parking** 903.2.10 | Enclosed garage fire area **> 1115 m²**; enclosed garage **beneath other groups** (not R-3); open garage fire area **> 4460 m²** | Commercial MV storage fire area **> 465 m²**. Mechanical-access enclosed garage: specially engineered sprinklers in that portion |

**SD takeaway:** Assume NFPA 13 throughout any building that contains **Group R or Group I**; for assembly, A-2 is the tight box (**465 m² / OL 100 / not on LED**), while A-1/A-3/A-4 use **1115 m² / OL 300 / not on LED** — a prayer hall off the LED sprinkles regardless of size unless it is a detached Type I/II mosque.

### 3. Automatic sprinklers — building geometry and special hazards (903.2.11, Table 903.2.11.6)
In all occupancies **except Group U**:

| Condition | Rule |
|-----------|------|
| Stories without openings, floor area **> 140 m²** 903.2.11.1 | Sprinkle that story unless exterior openings: below-grade stair/ramp each **15 m** of wall, or above-grade openings totalling **≥ 1.85 m²** each **15 m**, sill **≤ 1100 mm**, least dimension **≥ 750 mm**, spacing ≤ 15 m |
| Openings on one side only 903.2.11.1.2 | If opposite wall **> 23 m** from openings → sprinkle the story **or** provide openings on ≥ 2 sides |
| Basements 903.2.11.1.3 | Any portion **> 23 m** (travel) from required openings, or partitions that block hose streams → sprinkle **entire basement** (splitting into fire areas does not avoid this) |
| Rubbish/linen chutes 903.2.11.2 | Sprinklers at top, terminal room, alternate floors, and lowest intake; freeze-protect extensions |
| Height **≥ 16.5 m** 903.2.11.3 | Story with OL **≥ 30** whose finished floor is **≥ 16.5 m** above lowest fire-department vehicle access → sprinkle **throughout**. **Group F-2 exempt.** This is **not** the high-rise definition |
| Hazardous exhaust ducts 903.2.11.4 | Where **SBC 501** requires; ducts **< 250 mm** diameter exempt |
| Commercial cooking 903.2.11.5 | Sprinklers in hood/duct **only if** sprinklers are the 904 method; Type I hood suppression is otherwise 904.13 |
| Other occupancies Table 903.2.11.6 | Pointers include **403.3 high-rise**, 402 malls, 404 atriums, 405 underground, 407 I-2, 410 stages, 411 amusement, 507 unlimited-area, 509 incidental uses, 1030.6.2.3 smoke-protected seating |

**SD takeaway:** A four-storey office that never hits a Group B occupancy sprinkler row still sprinkles if an occupied floor with 30+ people sits **16.5 m** above FD access — check that elevation against the high-rise package (403) at the same time.

### 4. Which sprinkler standard (903.3.1)
Default is **NFPA 13** throughout (903.3.1.1). 13R and 13D do **not** unlock 13-based height/area/egress reductions unless the charging section names them.

| Standard | Where permitted | Schematic limits |
|----------|-----------------|------------------|
| **NFPA 13** 903.3.1.1 | Default “equipped throughout” | Exempt rooms only if detection provided (water-hazard, 2-hour generator/transformer, noncombustible contents, FSAE/OEE machine rooms, etc.). Group R bathrooms **≤ 5 m²** in the unit may omit heads if 15-min thermal barrier |
| **NFPA 13R** 903.3.1.2 | Group R, **all** of: ≤ **4 stories** above grade plane; highest floor **≤ 9 m** above lowest FD vehicle access; lowest floor **≤ 9 m** below that access | Pedestal stories counted from grade plane (510.2 / 510.4). Type V balconies/decks with a roof above must be sprinkled. Attics used for living/storage: sprinkle; podium Type III–V roof **> 16.5 m** above FD access needs attic sprinklers **or** noncombustible / FRT / noncombustible insulation |
| **NFPA 13D** 903.3.1.3 | One- and two-family; **R-3**; **R-4 Condition 1**; townhouses | Not a 13 substitute for mixed-use that independently needs 13 |

Quick-response or residential heads in I-2 care-recipient smoke compartments, ambulatory-care treatment-room compartments, I-1/R units, and NFPA 13 light hazard (903.3.2). Supervise waterflow and control valves at an approved station (901.6.1 / 903.4); 13D dwellings and limited-area systems (≤ 6 heads, 903.3.8) are the usual exceptions.

**SD takeaway:** A five-storey apartment that took the 504 sprinkler height increase is **NFPA 13**, not 13R — lock the standard when you lock storey count.

### 5. Commercial cooking — Type I hoods (903.2.11.5, 904.2.2, 904.13)
Each commercial kitchen exhaust hood/duct required by **SBC 801 §609** or **SBC 501 Chapter 5** to be a **Type I hood** (grease-laden vapour or smoke) shall have an approved automatic fire-extinguishing system (904.2.2). Install to this code, **NFPA 96**, listing, and manufacturer instructions; pre-engineered wet/dry chemical: **UL 300**. Factory-built recirculating systems: UL 710B + SBC 501 §304.1.

| Item | Rule |
|------|------|
| Manual pull | At or near a cooking-area exit, **3–6 m** from the exhaust system, **1050–1200 mm** AFF (904.13.1) |
| Fuel/electric shutoff | Automatic with system actuation (904.13.2) |
| Portable extinguishers | Class **K** within **9 m** travel of commercial cooking (906.1 Item 2) |
| Sprinklers under hoods | Not required where the 904 hood system protects kitchen equipment (903.3.3 exception) |

**SD takeaway:** Every grease-producing commercial kitchen is a Type I hood + listed suppression + K extinguisher — show the hood, 3–6 m pull, and make-up air at SD, not as a kitchen FF&E note.

### 6. Standpipes (905, NFPA 14)
Not required in **Group R-3** (905.3 exception). Combined sprinkler/standpipe risers are permitted.

| Trigger | System |
|---------|--------|
| **4 or more stories** above or below grade plane; **or** highest floor **> 9 m** above lowest FD vehicle access; **or** lowest floor **> 9 m** below highest FD vehicle access (905.3.1) | Class **III** throughout. Class **I** allowed if fully 13/13R sprinkled, or Group B/E, parking garages, sprinkled basements, or occupant hose will not be used |
| Nonsprinklered Group A, OL **> 1000** (905.3.2) | Class I automatic wet (open-air seating without enclosed spaces exempt) |
| Mall not otherwise 905.3.1 (905.3.3) | Class I hose on the sprinkler system, **945 L/min**, **≤ 345 kPa** residual loss; hose at mall/exit entries so tenant reach **≤ 60 m** |
| Stages **> 100 m²** (905.3.4) | Class III wet, 40 mm + 65 mm each side of stage (sprinkled: 40 mm only) |
| Underground buildings (905.3.5) | Class I automatic wet or manual wet |
| Roof helistop/heliport (905.3.6) | Class I or III to that roof (SBC 801 §2007.5) |
| Landscaped roofs (905.3.8) | Extend existing standpipe to that roof |

Class I hose locations (905.4): every required interior exit stair (each story, main floor landing unless FD official approves otherwise); each side of a horizontal exit; exit-passageway entries; mall public entrances; roof if slope < 4:12. Additional outlets if remote point **> 45 m** (nonsprinklered) or **> 60 m** (sprinklered) from a hose connection.

**SD takeaway:** Four storeys **or** > 9 m to the highest floor locks a standpipe riser in every required exit stair at SD — do not wait for the fire-protection engineer to add shafts.

### 7. Fire alarm and detection (907.2, NFPA 72)
Required systems monitored per 907.6.6 / 901.6.3 (smoke alarms and I-3 detectors excepted). Sprinkler waterflow may replace **manual boxes** in many groups if occupant notification still activates; it does not delete the alarm system.

| Occupancy | Alarm trigger | Extra |
|-----------|---------------|--------|
| **A** 907.2.1 | Assembly OL **≥ 300**, **or** Group A OL **> 100** above/below lowest LED. Unseparated A spaces (707.3.10) count as one occupancy | OL **≥ 1000**: emergency voice/alarm (EVAC) 907.2.1.1 |
| **B** 907.2.2 | Combined B OL all floors **≥ 500**; B OL **> 100** above/below lowest LED; **or** fire area contains ambulatory care | Ambulatory care: supervised smoke detection in the facility + public corridors/elevator lobbies (907.2.2.1) |
| **E** 907.2.3 | Manual system with **EVAC** | OL **≤ 50**: no manual system. OL **≤ 100**: EVAC not required if approved occupant notification. Corridor/shop detection or full 13 + EVAC on waterflow can omit corridor boxes |
| **F** 907.2.4 | **Both** ≥ 2 stories **and** combined OL **≥ 500** above/below lowest LED | |
| **H** 907.2.5 | H-5 and organic-coating manufacture | Emergency alarms 908 / 415.5 |
| **I** 907.2.6 | Manual system in all I; smoke detection per 907.2.6.1–.3 | I-1: corridors, waiting open to corridors, habitable rooms except sleeping units and kitchens. Private-mode signalling permitted with SBC 801 fire plan |
| **M** 907.2.7 | Combined M OL **≥ 500**, **or** M OL **> 100** above/below lowest LED | Malls per 402 exempt from this manual system |
| **R-1** 907.2.8 | Manual system + corridor smoke detection serving sleeping units | Exempt if ≤ 2 stories, 1-hour partitions, each unit exits directly to public way/yard |
| **R-2** 907.2.9 | Manual system if any unit is **≥ 3 stories** above lowest LED, **or > 1 story** below highest LED, **or > 16** dwelling/sleeping units | College/university R-2: extra corridor/common-space detection; unit smoke alarms interconnected to building alarm (907.2.9.3) |
| **S** 907.2.10 | Public- and self-storage **≥ 3 stories**: interior corridors and common areas | Visible appliances not required inside storage units |
| **High-rise** 907.2.13 | Automatic smoke detection + FD communication + EVAC | Detectors in unsprinklered equipment rooms; **always** in elevator machine/control rooms and elevator lobbies. Occupied floor **> 36 m** above FD access: **multi-channel** EVAC (907.2.13.3) |
| Smoke alarms 907.2.11 | UL 217 + NFPA 72 in R-1 sleeping units; in R-2/R-3/R-4/I-1: each sleeping room, outside each sleeping area, and each story of the unit | Interconnected in the unit; hard-wired with battery backup in new work. Not SBC 1101/1102 dwellings |

Visible alarm sleeping-accommodation counts: Table 907.5.2.3.2 (e.g. 6–25 units → 2; 501–1000 → 5% of total).

**SD takeaway:** Assembly OL 300 (or 100 off the LED) and R-2 with > 16 units or three storeys above LED lock a building fire-alarm/EVAC backbone — and high-rise always adds lobby/elevator-machine detection plus a fire command centre (911).

### 8. Smoke control (909) versus smoke and heat removal (910)
**909** applies only where **other** sections require smoke control (atrium 404.5, underground 405.5, mall atrium > 2 stories 402.7.2, I-3 windowless 408.9, smokeproof enclosures 403.5.4 / 1023.11 / 909.20). Purpose: **tenable environment for evacuation/relocation**, not contents protection or fire-fighter overhaul. **910 vents are not a 909 substitute.** Mechanical smoke control is not an SBC 501 Chapter 5 exhaust system. Duration: **≥ 20 minutes or 1.5 × calculated egress time**, whichever is less (909.4). Special inspection Chapter 17.

Smokeproof enclosure (909.20) where 1023.12 requires it:

| Alternative | Schematic lock |
|-------------|----------------|
| Vestibule access 909.20.1 | Width ≥ corridor (min **1.1 m**); length in egress direction **≥ 1.8 m** |
| Natural vent 909.20.3.3 | Vestibule opening **≥ 1.5 m²** to a court/yard/public way **≥ 6 m** wide |
| Mechanical vestibule 909.20.4 | ≥ 1 air change/min supply; exhaust **≥ 150%** of supply; ceiling smoke trap **≥ 500 mm** above door; shaft **≥ 25 Pa** vs vestibule |
| Stair pressurization (fully 13 sprinkled, no vestibule) 909.20.5 | **25–85 Pa** shaft vs building, all doors closed |
| Standby power | 909.20.7.2 / 2702 |

**910** is post-control **fire-fighter smoke/heat removal**, not occupant tenability:

| Where | System |
|-------|--------|
| F-1 or S-1 with **> 4650 m²** undivided area (910.2.1) | Vents 910.3 **or** mechanical removal 910.4; if the story is not a roof, mechanical only. S-1 aircraft repair hangars exempt |
| High-piled storage per SBC 801 Table 3206.2 (910.2.2) | Unsprinklered: vents only. Sprinklered: vents or mechanical |

Omit 910 for frozen-food warehouses (Class I/II, sprinkled), ESFR, and listed CMSA sprinklers (RTI ≤ 50, ≤ 12-head design) (910.2 exceptions).

**SD takeaway:** An atrium, underground occupied floor, or high-rise smokeproof stair is a **909** shaft/fan/vestibule problem at SD; a big F-1/S-1 shed is a **910** roof-vent or mechanical-removal problem — do not swap them.

### 9. Fire command centre, FDC, and pump/riser rooms (911, 912, 902, 913)
Fire command centre required in **high-rise** buildings, where other sections require it (including smoke-protected seating panel 909.16), and in **F-1 and S-1** with footprint **> 46450 m²** (911.1). Location/access: fire code official. **1-hour** fire barrier/horizontal assembly. Size: **≥ 0.015%** of total building area **or 20 m²**, whichever greater; minimum dimension **0.7√area or 3 m**, whichever greater. F-1/S-1 > 46500 m² footprint: **9 m²**, min dimension **2.4 m** if the fire code official approves. Identify the door **FIRE COMMAND CENTER**. Features per NFPA 72 (EVAC, FD comms, alarm/sprinkler/elevator/smoke-control/stair-unlock/power panels).

| Support room | Schematic lock |
|--------------|----------------|
| Pump / sprinkler riser room 902.1 | Manufacturer working clearances; door large enough to remove the largest piece; ready access (lock OK if key always available); door letters **≥ 50 mm**, stroke **≥ 10 mm**; room **≥ 4°C**; permanent lighting |
| Fire pump room 913.2.1 | **2-hour** fire barriers and/or horizontal assemblies |
| FDC 912 | Street side or FD access road, fully visible; location approved by fire code official; **900 mm** clear; no landscape/obstruction; threads compatible with the department (901.4) |
| Emergency responder radio 918.1 | All **new** buildings per SBC 801 §510 |

High-rise and 909-integrated systems: integrated testing **NFPA 4** before occupancy and ≤ 10-year intervals (901.6.2).

**SD takeaway:** High-rise (and huge F-1/S-1 footprints) lock a **≥ 20 m²** (typically) 1-hour fire command room on the FD-approved arrival face, plus a 2-hour pump room, visible FDC, and radio-coverage strategy — none of these are “MEP later.”

### Source
`Chapter_09 — FIRE PROTECTION SYSTEMS.txt`

Companions named in this chapter: **SBC 801** (maintenance, existing buildings, high-piled storage, cooking §609, construction Ch. 33, emergency responder radio §510); **SBC 501** (Type I/II hoods Ch. 5, hazardous exhaust §510); **SBC 1101/1102** (dwellings excluded from Group R triggers); **SBC 701** (indirect waste / backflow at test connections); **NFPA 13, 13R, 13D, 14, 72, 4, 20, 25, 92, 96**. High-rise sprinklers and associated systems: **Section 403** (Table 903.2.11.6). Fire-area ratings: **Table 707.3.10** in Chapter 7.
