# SBC 201 Chapter 27 Electrical — Group R-2 High-Rise Dimensional Requirements Matrix (2024)

## 1. Document metadata and use limitation

- **Project basis:** Riyadh, Saudi Arabia; Group R-2 residential high-rise; an occupied floor is stated to be more than 23 m above the relevant reference level.
- **Deliverable tier:** Project-use matrices in Sections 1–8 (design-check rows, not pasted inventory), plus a coverage summary and unresolved-source register. The full row inventory is not published.
- **Code/source basis:** SBC 201 (2024), Chapter 27, source file `Reference\SBC 201 2024\source_reference\Chapter_27 — ELECTRICAL.txt`.
- **Extraction audit:** Skill extract. Project-use rows follow the chapter-extract row contract (noun-phrase checks, bold published tokens, building-language triggers, named exceptions, check-specific actions). Internal inventory: **17** independently checkable numeric records (**17** Verified, **0** Verify source). The attached extract has no appended tables. Clause 2702.2.13 contains OCR “below grand plant”; that laboratory-suite rule is omitted from project-use as Not typical and is not a design-release cell.
- **Model:** Cursor Grok 4.6.
- **Prepared:** 2026-08-27.
- **Status:** Source-only architectural advisory matrix for design coordination. It is not a stamped compliance statement, electrical design, SCD NOC, SBPS approval, legal opinion, or permission to construct.
- **Outbound-source rule:** No value in this matrix has been imported from SBC 401, SBC 801, SBC 901, the International Property Maintenance Code, SBC 501, SBC 1201, NFPA 70, NFPA 110, NFPA 111, NFPA 72, UL 2200, UL 1489, UL 2196, ASCE 24, Sections 403.4.8, 404.7, 405, 407.11, 408.4.2, 415.11.11, 422.6, 903.3.1.1, 909, 918, 1008.3, 1009.4.1, 1009.5, 1010.3.3, 1013.6.3, 3003.1, 3007.8, 3008.8, 3102.8.2, 5004.7, commentary examples, or the existing chapter summary. Where Chapter 27 sends the user elsewhere, this matrix records the dependency without supplying the outbound value.

### Scope and assumptions

1. Group R-2 and high-rise status are project statements, not independently verified classifications.
2. The exact Riyadh AHJ/permit pathway, project stage and SCD NOC status are unconfirmed; therefore this matrix does not conclude compliance.
3. Automatic sprinkler protection, mixed-use podium, storey count, indoor versus outdoor generator location, EVACS, smoke control and underground-building classification are unconfirmed. Show both sprinkler branches until locked. This chapter reduces 2702.1.2 fuel-line ratings only for **903.3.1.1**, not for 903.3.1.2.
4. Chapter 27 does not publish wiring methods, device ratings, generator kW, or 403.4.8 load lists. Those live in SBC 401 and the named outbound sections.
5. Occupancy-only rules for Group I-2, I-3, ambulatory care, hydrogen fuel-gas rooms, laboratory suites, membrane structures and semiconductor fabrication are omitted from the project-use tables.

## 2. Legends

### Applicability

| Status | Meaning |
|---|---|
| **Direct** | Expected to govern the stated R-2 tower basis, subject to confirmed geometry and design data. |
| **Conditional** | Governs only when the stated feature, use, occupant load, sprinkler branch or exception exists. |
| **Not typical** | Unrelated occupancy-only rule; omitted from this deliverable unless the gap register already opened that use. |
| **External verification** | Chapter 27 points to another section/code/standard, or the project/AHJ basis must be confirmed before use. |

### Source confidence

| Status | Meaning |
|---|---|
| **Verified** | Requirement and any stated numeric value were checked against unambiguous mandatory Chapter 27 source text. |
| **Verify source** | OCR, flattened table, page-split, or footnote attachment is unresolved. Not a design-release value. |

## 3. Project decision and gap register

| Decision / gap | Current project basis | Why it controls Chapter 27 application | Required project action |
|---|---|---|---|
| Indoor versus outdoor generator | Unconfirmed | 2702.1.2 applies only to fuel lines supplying a generator set **inside** a high-rise | Confirm plant location; apply the 2-hour / 1-hour fuel-line check only if the set is indoors |
| Sprinkler 903.3.1.1 versus 13R | Unconfirmed | The 2702.1.2 rating drop to **1 hour** is only where the building is sprinklered throughout per **903.3.1.1**. This chapter does not name 903.3.1.2 | Fire engineer to lock NFPA 13 versus 13R; do not take the 1-hour drop on a 13R-only basis from this chapter |
| Section 918 ER communication | Unconfirmed whether an in-building 2-way system is required | 2702.2.3 **100-percent** / **12-hour** standby applies only to systems required by 918 and SBC 801 | Radio/fire consultant to lock ERCCS; put the 12-hour load on standby only if that system exists |
| EVACS | Unconfirmed | 2702.2.4 requires standby in accordance with NFPA 72; this chapter publishes no 72 durations | Freeze EVACS on the fire-alarm drawings; do not import 24-hour / 15-minute commentary figures |
| Smoke control / smokeproof / atrium / hoistway | Unconfirmed | 2702.2.17 standby is triggered only where 404.7, 909.11, 909.20.7.2 or 909.21.5 systems exist | Confirm those systems on the fire strategy; put confirmed fans and detection on standby |
| Common kitchen / dryer exhaust | Unconfirmed | 2702.2.5 standby is for common exhaust in **multistory** structures per SBC 501 / 1201 | MEP to flag shared kitchen or dryer risers; put those fans on standby if they exist |
| Special-purpose sliding doors | Unconfirmed | 2702.2.18 **50** closing cycles applies only to 1010.3.3 doors | Door schedule to flag special-purpose horizontal sliding, accordion or folding egress doors |
| Underground building (405) | Unconfirmed deep basement | 2702.2.19 charges emergency and standby to Section 405 | Confirm whether any portion is an underground building; combine 405 loads with the high-rise schedule if it is |
| Mixed-use / podium program | Unconfirmed | Hazardous-materials, gas-detection and omitted occupancy clauses reopen only if those uses exist | Freeze occupancy by space; reopen omitted 2702.2 occupancies only if those uses are actually programmed |
| NOC / fire strategy / electrical PE | Unconfirmed | Transfer times, durations and load lists cannot evidence SCD NOC | Align the generator schedule with the stamped fire strategy and the electrical engineer of record |

## 4. Scope and installation

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 2701.1 | Electrical installation charging | Design, construction, erection and installation of electrical components, appliances, equipment and systems shall comply with this chapter and **SBC 401** | Electrical work on the building | Use and maintenance: **SBC 801**, the International Property Maintenance Code and **SBC 401**. Alteration, repair, relocation, replacement and addition: **SBC 901** and **SBC 401** | External verification | Name SBC 401, SBC 801 and SBC 901 on the electrical code sheet; do not import wiring, device or alteration values from those volumes | Verified |
| 2702.1 | Emergency/standby installation range | Emergency power systems and standby power systems shall comply with **2702.1.1 through 2702.1.8** | Required emergency or standby power | None stated | Direct | Route every emergency/standby source through the 2702.1 installation checks before freezing the plant | Verified |
| 2702.1.1 | Stationary generator listing | Stationary emergency and standby power generators required by this code shall be listed in accordance with **UL 2200** | Stationary generator used to meet this chapter | None stated | Conditional | Specify **UL 2200** listing on the generator equipment schedule | Verified |
| 2702.1.3 | Emergency/standby installation standards | Emergency and standby power required by this code or **SBC 801** shall be installed in accordance with **SBC 801**, **NFPA 70** (or its equivalent in **SBC 401**), **NFPA 110** and **NFPA 111** | Required emergency or standby system | None stated | External verification | Name those installation standards on the generator specification; do not import Article 700/701 or NFPA 110 class/type values from commentary or those standards | Verified |

## 5. High-rise generator fuel lines

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 2702.1.2 | High-rise indoor generator fuel lines | Fuel lines supplying a generator set inside a high-rise, other than in the generator room, shall be protected by a **UL 1489** pipe-protection system rated **not less than 2 hours**, or by an assembly fire-resistance rated **not less than 2 hours**. Where the building is sprinklered throughout per **903.3.1.1**, that rating is reduced to **1 hour** | Generator set inside a high-rise building | Item 3: other approved methods. This chapter reduces the rating only for **903.3.1.1**, not for 903.3.1.2 | Conditional | Draw **2-hour** fuel-line wrap or rated chase from tank to indoor generator room, or **1-hour** if NFPA 13 throughout is documented | Verified |

## 6. Transfer, duration, UPS and substitution

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 2702.1.4 | Emergency and standby transfer time | Emergency power shall automatically provide secondary power within **10 seconds** after primary power is lost. Standby power shall automatically provide secondary power within **60 seconds** after primary power is lost, unless this code specifies otherwise | Required emergency or standby system | Other transfer times specified elsewhere in this code | Direct | Set ATS pickup to **10 seconds** on the emergency bus and **60 seconds** on the standby bus unless a more specific section overrides | Verified |
| 2702.1.5 | Default load duration | Emergency and standby power shall provide the required power for a minimum duration of **2 hours** without being refueled or recharged, unless specified otherwise in this code | Required emergency or standby system | This chapter states other durations for exit signs and egress illumination (**90 minutes**) and ER communication coverage (**12 hours**) | Direct | Size fuel or stored energy for **2 hours** as the default; override only where this chapter or another cited section states a different duration | Verified |
| 2702.1.6 | Uninterruptible power source | An uninterrupted source of power shall be provided for equipment when required by the manufacturer's instructions, the listing, this code or applicable referenced standards | Equipment whose listing, manufacturer, this code or a referenced standard requires no transfer-time gap | None stated | Conditional | Flag UPS-required fire-alarm, control and similar equipment on the electrical schedule; do not invent which devices need UPS from this chapter | Verified |
| 2702.1.7 | Emergency as standby substitute | An emergency power system is an acceptable alternative where standby power is required | Load that this chapter requires as standby | None stated | Direct | Place standby loads on the emergency bus when a single faster source serves both | Verified |

## 7. Required emergency and standby loads

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 2702.2 | Emergency and standby where-required | Emergency and standby power systems shall be provided where required by **2702.2.1 through 2702.2.19** | Building with any load listed in those subsections | Occupancy-only subsections not used on this R-2 tower are omitted from this table | Direct | Build the generator schedule from the rows below; do not add omitted occupancy loads unless the gap register reopens them | Verified |
| 2702.2.2 | Elevator and platform-lift standby | Standby power shall be provided for elevators and platform lifts as required in **1009.4.1**, **1009.5**, **3003.1**, **3007.8** and **3008.8** | Elevators, or platform lifts used as those sections require | Load lists, kW and extra fire-service or occupant-evac rules in those sections are not imported | External verification | Put elevators and any accessible-egress platform lift on the standby schedule; lock kW and extra elevator rules from Chapters 10 and 30 | Verified |
| 2702.2.3 | ER communication standby duration | Standby power for in-building 2-way emergency responder communication coverage systems required in **918** and **SBC 801** shall operate the system at **100-percent** system operation capacity for a duration of **not less than 12 hours** | In-building 2-way ER communication coverage system required by Section 918 and SBC 801 | None stated | Direct | Put the ERCCS on standby at **100-percent** capacity for **12 hours**; do not adopt commentary battery-split methods | Verified |
| 2702.2.4 | EVACS standby power | Standby power shall be provided for emergency voice/alarm communication systems in accordance with **NFPA 72** | EVACS provided on the building | NFPA 72 duration and alarm-operation times are not published in this chapter | Conditional | Put EVACS on the standby schedule; lock duration from NFPA 72, not from this matrix or commentary | Verified |
| 2702.2.5 | Multistory common exhaust standby | Standby power shall be provided for common domestic-kitchen exhaust in multistory structures as required in **SBC 501** Section 505.5, and for common clothes-dryer exhaust as required in **SBC 501** Section 504.11 and **SBC 1201** Section 614.11 | Common kitchen or dryer exhaust serving a multistory building | Exhaust criteria in SBC 501 and SBC 1201 are not imported | Conditional | If shared kitchen or dryer risers exist, put those fans on standby; lock duct and fan rules from SBC 501 and SBC 1201 | Verified |
| 2702.2.6 | Exit-sign emergency duration | Emergency power shall be provided for exit signs as required in **1013.6.3**. The system shall be capable of powering the required load for a duration of **not less than 90 minutes** | Exit signs required by Chapter 10 | This **90-minute** duration overrides the **2-hour** default of 2702.1.5 for this load | Direct | Put exit signs on the emergency bus with **90-minute** support; do not import sign luminance from 1013 | Verified |
| 2702.2.7 | Gas-detection emergency or standby | Emergency or standby power shall be provided for gas detection systems in accordance with **SBC 801** | Gas detection system required by SBC 801 | Which power type (emergency versus standby) is set in SBC 801, not here | Conditional | If gas detection is on the fire strategy, add it to the emergency or standby schedule per SBC 801; do not import 801 durations | Verified |
| 2702.2.10 | Hazardous-materials emergency or standby | Emergency or standby power shall be provided in occupancies with hazardous materials where required by **SBC 801** | Hazardous materials present and SBC 801 requires electrically operated protection | Outbound fail-safe alternatives, if any, are not imported | Conditional | If a podium or amenity exceeds MAQ, add the SBC 801-required loads to the generator schedule; do not import MAQ or ventilation figures | Verified |
| 2702.2.11 | High-rise emergency and standby | Emergency and standby power shall be provided in high-rise buildings as required in **403.4.8** | High-rise building | Standby versus emergency load lists and generator-room ratings in 403.4.8 are not imported | Direct | Split the generator schedule using the 403.4.8 load lists; do not copy those lists or 403 fuel-line/room ratings into this matrix | Verified |
| 2702.2.14 | Egress-illumination emergency duration | Emergency power shall be provided for means of egress illumination as required in **1008.3**. The system shall be capable of powering the required load for a duration of **not less than 90 minutes** | Means of egress illumination | This **90-minute** duration overrides the **2-hour** default of 2702.1.5 for this load | Direct | Put egress lighting on the emergency bus with **90-minute** support; do not import illumination levels from 1008 | Verified |
| 2702.2.17 | Smoke-control standby power | Standby power shall be provided for smoke control systems as required in **404.7**, **909.11**, **909.20.7.2** and **909.21.5** | Atrium smoke control, smoke-control system, mechanical smokeproof enclosure, or elevator hoistway pressurization as those sections require | Duration and fan quantities in those sections are not imported | Conditional | Put confirmed smoke-control, smokeproof and hoistway-pressurization equipment on standby; lock fan details from Chapters 4 and 9 | Verified |
| 2702.2.18 | Special-purpose door standby cycles | Standby power shall be provided for special-purpose horizontal sliding, accordion or folding doors as required in **1010.3.3**. The standby power supply shall have a capacity to operate **not fewer than 50** closing cycles of the door | Special-purpose horizontal sliding, accordion or folding door under 1010.3.3 | None stated | Conditional | If such a door is on the egress schedule, specify standby capable of **50** closing cycles | Verified |
| 2702.2.19 | Underground-building emergency and standby | Emergency and standby power shall be provided in underground buildings as required in **405** | Building or portion classified as an underground building under Section 405 | 405 load lists are not imported | Conditional | If 405 applies to a deep basement, combine those loads with the high-rise 403.4.8 schedule; do not copy 405 lists here | Verified |

## 8. Critical circuits and maintenance

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | R-2 tower status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 2702.3 | Critical-circuit fire protection | Required critical circuits shall be protected by **UL 2196** cables with a fire-resistance rating of **not less than 1 hour**, an electrical circuit protective system rated **not less than 1 hour**, or construction rated **not less than 1 hour** | Required critical circuits | Three listed methods. Electrical circuit protective systems shall be installed in accordance with their listing | Direct | Protect generator, fire-pump and similar critical feeders with **1-hour** listed cable, wrap or rated construction on the riser drawings | Verified |
| 2702.4 | Emergency/standby maintenance | Emergency and standby power systems shall be maintained and tested in accordance with **SBC 801** | Installed emergency or standby system | None stated | External verification | Put SBC 801 testing on the O&M specification; do not import test intervals from this chapter | Verified |

## 9. Project-use controls

1. Use **Verified** rows for initial scoping after the row trigger and branch are confirmed.
2. There is no **Verify source** row in this deliverable. Do not treat the 2702.2.13 OCR token as a laboratory-suite design value, and do not fill omitted occupancy rows from memory.
3. Do not import SBC 401 wiring methods, NFPA 70 transfer commentary, NFPA 72 24-hour / 15-minute figures, 403.4.8 load lists or generator-room ratings, 405 load lists, or ASCE 24 flood elevations into issued drawings from this matrix.
4. Do not take the 2702.1.2 **1-hour** fuel-line reduction unless **903.3.1.1** throughout is documented. Do not apply a 903.3.1.2 reduction from Chapter 4 to this chapter’s fuel-line row.
5. Default duration is **2 hours** (2702.1.5). Override to **90 minutes** for exit signs and egress illumination, and to **12 hours** at **100-percent** capacity for ER communication coverage, only for those loads.
6. Record generator location, sprinkler standard, ERCCS, EVACS, smoke-control and 405 decisions in the project Golden Thread; this matrix is not evidence of SCD NOC or stamped electrical compliance.

## 10. Coverage summary

Internal inventory of the attached Chapter 27 extract (numbered code, exceptions, tables, footnotes; commentary excluded). Row-level records are not published.

- **Inventory scope:** numbered code, exceptions, tables, footnotes (commentary excluded)
- **Total independently checkable numeric records:** 17
- **Verified:** 17
- **Verify source:** 0

### Counts by top-level section

| Top-level section | Records |
|---|---:|
| 2701 | 0 |
| 2702 | 17 |

No appended tables in the attached extract.

Coverage cross-check against `SBC 201 Chapter 27 Electrical (2024)_CS.md` was topics-only: charging to SBC 401; emergency versus standby transfer; default **2-hour** duration; high-rise indoor fuel-line protection; 2702.2 load pointers including 403.4.8 and 405; **90-minute** exit-sign and egress-illumination durations; ERCCS **12 hours**; **1-hour** critical-circuit protection; occupancy-only clauses omitted from project-use. No CS.md value was copied into a matrix cell.

## 11. Unresolved-source register

No project-use **Verify source** hold point. 2702.2.3 is page-split; the continuation (**100-percent** / **12 hours**) is unambiguous and was adopted as Verified. 2702.2.13 OCR “below grand plant” was not adopted; that laboratory-suite clause is Not typical for this occupancy and is omitted from the tables above.

| Affected table / clause | Why unverified | Control note |
|---|---|---|
| — | None in project-use | Do not reconstruct omitted occupancy numbers or outbound SBC 401 / 403.4.8 / NFPA 72 values here |
