# ICC A117.1 Chapter 11 Dwelling Units and Sleeping Units — Type B Dimensional Requirements Matrix (2017)

## 1. Document metadata and use limitation

- **Project basis:** Mixed-use tall building containing Group R-1 (hotel) with Group R-2 residential sharing podium, parking and routes. An occupied floor is stated to be more than 23 m above the relevant reference level. This matrix filters ICC A117.1 Chapter 11 for **Type B units** (Section 1104).
- **Unit type:** Type B (1104). Accessible (1102) and Type A (1103) interiors are omitted from this file. Type C (1105) is omitted.
- **Deliverable tier:** Project-use matrices in Sections 4–13 (design-check rows, not pasted inventory), plus project-use controls, a coverage summary and an unresolved-source register.
- **Code/source basis:** ICC A117.1 (2017), Chapter 11, source file `Reference\2017 ICC A117_1 Accessible and Usable Buildings and Facilities\source_reference\Chapter_11 — DWELLING UNITS AND SLEEPING UNITS.txt`. Companion numbers inlined from the attached 2017 Chapter 1–10 `source_reference` extracts where 1104 charges those sections.
- **Extraction audit:** Internal inventory: **198** independently checkable numeric records (**186** Verified, **12** Verify source). Unresolved OCR/flattened tables are listed in the register and are not design-release values.
- **Inspecting model:** Cursor Grok 4.6.
- **Prepared:** 2026-08-28.
- **Status:** Source-only architectural advisory matrix for design coordination. It is not a stamped compliance statement, accessibility consultant report, SCD NOC, SBPS approval, legal opinion, or permission to construct.
- **Scoping companion:** Counts and which units must be Type B are **SBC 201 Chapter 11**. R-1 Type B applies only where units are intended to be occupied as a residence. This file does not import SBC quotas.
- **Edition gap:** SBC 201 Chapter 35 lists **ICC A117.1—09**. Charging SBC 1102.1 has no year. This extract is **2017**. Type B interiors already use reduced CFS and existing-style route exceptions; do not “upgrade” them to Accessible/Type A 2017 turning or 404 manoeuvring. **Do not treat 2017 millimetres as the legal SBC minimum.**

### Scope and assumptions

1. Type B is Direct for R-2 apartments. R-1 hotel Type B is Conditional unless units are occupied as a residence.
2. New construction is assumed for building-wide elements. Type B **interior** route exceptions in 1104.4.1 already print existing-style 180°/90°/passing numbers; those printed 1104 exceptions are Direct for Type B interiors.
3. **Do not** draw Type B interiors with Accessible/Type A 404 latch-side manoeuvre or 304 room-wide turning.
4. Type B CFS is **48 × 30 inches (1220 × 760 mm)** (1104.1.1), not 2017 new 52 in.
5. Interior user-passage clear opening is **31 3/4 inches (805 mm)**. Primary entrance still charges 404, with Type B front-approach **48 inches (1220 mm)** exceptions.
6. FIGURE captions are dependencies. Flattened `<table>` blobs are not reconstructed as Verified cells.

## 2. Legends

### Applicability

| Status | Meaning |
|---|---|
| **Direct** | Expected to govern Type B unit interiors once geometry is confirmed (R-2 typical). |
| **Conditional** | Governs only if the stated feature, R-1 residential occupancy, existing-building branch, in-unit ramp/lift/elevator, or communication overlay exists. |
| **Not typical** | Unrelated unit-type-only rule; omitted unless the gap register already opened that use. |
| **External verification** | A figure is missing, a flattened table is unread, or AHJ/edition must be confirmed first. |

### Source confidence

| Status | Meaning |
|---|---|
| **Verified** | Unambiguous mandatory source text or readable footnote after a table blob. |
| **Verify source** | OCR, flattened table, page-split, or footnote attachment is unresolved. Not a design-release value. |

## 3. Project decision and gap register

| Decision / gap | Current project basis | Why it controls Chapter 11 application | Required project action |
|---|---|---|---|
| A117.1 edition lock | Extracted edition is **2017**; SBC 201 Chapter 35 lists **A117.1—09** | Type B CFS and door width are in 1104; do not import Accessible 2017 52 in CFS or 67 in turning into Type B interiors | AHJ to lock 2009 vs 2017 for common/public routes; keep Type B interiors on 1104 |
| R-1 vs R-2 | Mixed hotel + apartments | R-2 Type B is Direct. R-1 Type B only if units are occupied as a residence (SBC scoping — quotas not imported) | Freeze hotel operating model before applying this matrix to guestrooms |
| New vs existing | New construction assumed | 1104.4.1 already prints existing-style pinch/180°/90°/passing as Type B exceptions; those are Direct for Type B interiors. Primary-door Table 404.2.3.2 new vs existing still splits | Do not mix Accessible new 403.5.3.1 90° options into Type B unit corridors |
| Manoeuvre inside the unit | Type B interiors are reduced | Interior user-passage doors are 1104.5.2 (**31 3/4 inches (805 mm)**), not full 404 manoeuvre | Do not draw 404 latch-side pads at bedroom/bath doors |
| Grab bars | Blocking only | 1104.11.1 reinforcement; bars not in place | Draw blocking; do not install Accessible-unit grab bars as the Type B typical |
| Option A vs Option B baths | Unconfirmed | Either all baths Option A, or one bath Option B | Pick one strategy per typical and dimension it |
| AHJ / NOC | Unconfirmed | Stamped compliance cannot be concluded from this extract | Engage the qualified local accessibility consultant before design freeze |

## 4. Unit accessible route and walking surfaces

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | Type B status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1104.2 | Primary entrance location | Primary entrance on an accessible route from public and common areas; not to a bedroom unless it is the only entrance | Type B units | None stated | Direct | Place the Type B entry on the corridor accessible route | Verified |
| 1104.3.1 | Unit accessible-route extent | At least one accessible route shall connect all spaces and elements that are part of the unit and shall coincide with or be in the same area as the general circulation path | Type B interiors | Unfinished attics/basements. One allowed miss: a raised or sunken portion of a living/dining/sleeping room, or a mezzanine without plumbing fixtures or enclosed habitable space | Direct | Connect entry, bedrooms, living, kitchen and accessible-level baths; document any single raised/sunken/mezzanine miss | Verified |
| 1104.3.2 / 1104.4 | Route components and slope | Walking surfaces with slope not steeper than 1:20, plus doors, ramps, elevators and platform lifts | Type B accessible routes | Steeper walking surfaces become ramps (405) | Direct | Hold unit floors at 1:20; treat steeper runs as ramps | Verified |
| 1104.4.1 / 403.5.1 | Interior clear width with Type B pinch | Clear width complies with 403.5, except Type B may reduce to **32 inches (815 mm)** min for **24 inches (610 mm)** max length if reduced segments are separated by **48 inches (1220 mm)** min length × **36 inches (915 mm)** min width | Type B interior accessible routes | This printed exception uses the existing-style **48-inch (1220 mm)** separator, not the new-building **52-inch (1320 mm)** separator | Direct | Hold Type B corridors at 915 mm; if a pinch is used, separate with 1220 × 915 mm | Verified |
| 1104.4.1 Exceptions 2–3 | Type B 180-degree turn | Around an object **< 48 inches (1220 mm)** wide: **42 inches (1065 mm)** approaching, **48 inches (1220 mm)** during, **42 inches (1065 mm)** leaving; or approach/leave **36 inches (915 mm)** if the turn is **60 inches (1525 mm)** min | 180-degree turns on the Type B route | These are the Type B printed exceptions (existing-style), Direct for Type B interiors | Direct | Dimension Type B 180° turns to 42/48/42 or 36/60/36; do not require Accessible new 43 in or 52 in object rules inside the unit | Verified |
| 1104.4.1 Exception 4 | Type B 90-degree turn | Clear widths approaching and leaving a 90-degree turn **36 inches (915 mm)** minimum | 90-degree turns on the Type B route | Do not apply Accessible new 403.5.3.1 40/38/44 in option set inside Type B units | Direct | Hold Type B 90° turns at 915 mm both legs | Verified |
| 1104.4.1 Exception 5 | Type B passing space | Where width **< 60 inches (1525 mm)**, passing at **200 feet (61 m)** max: **60 × 60 inches (1525 × 1525 mm)** or a T-turn per **304.3.2.2** with base/arms **48 inches (1220 mm)** min beyond the intersection | Long Type B routes under 1525 mm | 304.3.2.2 is the existing T-turn (**60-inch (1525 mm)** square, arms/base **36 inches (915 mm)**) | Conditional | Add a 1525 mm passing bay on any Type B corridor longer than 61 m under 1525 mm | Verified |
| 1104.4.2 / 303.2–303.4 | Change in level | Vertical **1/4 inch (6.4 mm)** max; **1/4–1/2 inch (6.4–13 mm)** beveled 1:2; above **1/2 inch (13 mm)** by ramp 405 or curb ramp 406 | Type B walking surfaces | Exterior impervious deck/patio/balcony may be **4 inches (100 mm)** max below the adjacent interior floor | Direct | Limit interior joints to 13 mm at 1:2; balcony drop ≤ 100 mm if impervious | Verified |

## 5. Doors and doorways

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | Type B status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1104.5.1 / 404.2.2 | Primary-entrance clear opening | Primary entrance complies with 404: clear opening **32 inches (815 mm)** min, door face to stop at 90° | Type B primary entrance door | Interior user-passage doors use 1104.5.2, not this row | Direct | Specify 815 mm clear at the unit entry only | Verified |
| 1104.5.1 Exceptions 2–4 | Type B primary-door front manoeuvre | Front-approach push on swinging doors, front approach on sliding/folding doors, and front approach at doorways without doors: perpendicular dimension **48 inches (1220 mm)** minimum | Type B primary entrance | Storm/screen doors exempt from 404.2.5. Remainder of 404 manoeuvre at the primary door still charges Table 404.2.3.2 (flattened: **no other cell adopted**). Readable 404.2.3.2 footnotes 1–4 still apply at the primary door | Direct | Hold 1220 mm perpendicular on the push/front side of the Type B entry; do not import reconstructed table cells for other approaches | Verify source |
| 1104.5.2.1 | Interior user-passage clear opening | Doorways intended for user passage: clear opening **31 3/4 inches (805 mm)** minimum, measured door face to stop at 90° | Interior Type B user-passage doors | Shower door assemblies exempt. This is **not** 404 manoeuvre and **not** 32 in (815 mm) | Direct | Specify 805 mm clear at bedrooms, baths and kitchens; do not draw 404 latch-side pads | Verified |
| 1104.5.2.1.1 | Double-leaf inactive hardware | If operable parts on an inactive leaf are **> 48 inches (1220 mm)** or **< 15 inches (380 mm)** AFF, the active leaf shall provide the 1104.5.2.1 clearance | Type B double-leaf user-passage doors | None stated | Conditional | Keep inactive-leaf hardware in 380–1220 mm or size the active leaf to 805 mm clear | Verified |
| 1104.5.2.2 / 303 | Interior thresholds | Thresholds comply with 303: **1/4 inch (6.4 mm)** vertical; **1/2 inch (13 mm)** at 1:2 | Type B user-passage doorways | Exterior sliding doors **3/4 inch (19 mm)** max, beveled not steeper than 1:2 | Direct | Specify 13 mm max interior thresholds; 19 mm at 1:2 on exterior sliders | Verified |
| 1104.5.2.3 / 404.3.3 | Automatic user-passage doors | Automatic doors comply with 404.3: **32 inches (815 mm)** clear in power-on and power-off | Power-operated interior Type B doors | BHMA A156 values not imported | Conditional | If an automatic interior door is used, keep 815 mm clear in both power states | Verified |
| 1104.5.1 / 404.2.6 | Primary-door hardware | Push/pull **15 pounds (66.7 N)** max; rotational **28 inch-pounds (315 N·cm)** max; hardware **34–48 inches (865–1220 mm)** AFF | Type B primary entrance | Interior 1104.5.2 doors are not charged with full 404 hardware | Direct | Schedule entry levers 865–1220 mm AFF | Verified |

## 6. Clear floor space and operable parts

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | Type B status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1104.1.1 | Type B clear floor space | Clear floor spaces **48 inches (1220 mm)** min length × **30 inches (760 mm)** min width | Type B fixtures, appliances, laundry and controls that require a CFS | Do **not** use 2017 new 305.3.1 **52 inches (1320 mm)** inside Type B units | Direct | Park 1220 × 760 mm CFS at Type B fixtures and appliances | Verified |
| 1104.1.2 | Mailbox side reach | Mailboxes serving Type B units may use unobstructed side reach **54 inches (1370 mm)** maximum AFF | Mailboxes serving Type B units | This is a Type B permission, not a 308.3.1 existing-element rule | Conditional | If unit mailboxes are provided, 1370 mm side reach is permitted | Verified |
| 1104.9 / 309.3 / 308 | Control height | Lighting, switches, receptacles, environmental controls, panelboards and security/intercom controls: height in a 308 reach range, with CFS per 1104.1.1. Unobstructed high **48 inches (1220 mm)** / low **15 inches (380 mm)** | Type B lighting, receptacles, environmental, panelboards, security/intercom | Plumbing fixture and appliance controls are **not** charged (Ex. 7–8). Dedicated receptacles; one of two-plus kitchen counter receptacles; corner counter ≤ **9 square feet (0.835 m²)**; floor receptacles; HVAC diffusers; ceiling-fan controls; appliance resets; redundant non-light controls. Kitchen/bath controls may sit over cabinets **36 inches (915 mm)** max high × **25 1/2 inches (650 mm)** max deep | Direct | Place switches and receptacles at 380–1220 mm; allow the 915 × 650 mm over-cabinet exception in kitchens/baths; do not force 309 on plumbing/appliance controls | Verified |
| 1104.11.2.2 / 306 | Knee and toe at fixtures | Fixture CFS may include 306 knee/toe: toe to **9 inches (230 mm)** AFF, **25 inches (635 mm)** max / **17 inches (430 mm)** min; knee **9–27 inches (230–685 mm)** AFF | Forward-approach Type B fixtures | Option A lavatory typical is parallel approach (no 306 required unless the 606 forward option is used) | Conditional | Apply 306 only where a forward Type B approach is used | Verified |

## 7. Toilet and bathing facilities (blocking; Option A or B)

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | Type B status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1104.11 | Bath applicability | Toilet and bathing fixtures comply with 1104.11 | Fixtures on accessible levels of the Type B unit | Fixtures on levels not required to be accessible | Direct | Apply this section to the accessible-level bath(s) | Verified |
| 1104.11.3 | Option A or Option B | Either **all** toilet/bathing areas comply with Option A (1104.11.3.1), or **one** toilet/bathing area complies with Option B (1104.11.3.2) | Type B accessible-level baths | Pick one strategy; do not mix unlabelled | Direct | Freeze Option A (every bath) or Option B (one room) on the typical | Verified |
| 1104.11.1 | Grab-bar and seat blocking | Reinforcement for future 604.5 WC bars, 607.4 tub bars, and 608.3 / 608.2.1.3 / 608.2.2.3 / 608.2.3.2 shower bars and seats, where walls permit those installations | Water closets, tubs and showers on accessible levels | Powder room that is not the only lav/WC on the accessible level. Vertical WC side-bar component of 604.5 not required. Rear **24 inches (610 mm)** min centered if 604.5.2 will not fit. Side **24 inches (610 mm)** min, **12 inches (305 mm)** max from rear wall, if a **42-inch (1065 mm)** side bar will not fit. Swing-up bars per 1104.11.1.1 permitted in lieu. Shower seat blocking not required in compartments larger than **36 × 36 inches (915 × 915 mm)** | Direct | Back WC/tub/shower walls for future bars; omit vertical side-bar blocking | Verified |
| 1104.11.1.1 | Swing-up grab-bar blocking | **18 inches (455 mm)** min from WC centerline to any side wall or obstruction (on the side opposite a side approach). Bar centered **15 3/4 inches (400 mm)** from WC centerline, **28 inches (710 mm)** min length from the wall, down position **33–36 inches (840–915 mm)** AFF. Force per 609.8 **250 pounds (1112 N)** | Where swing-up blocking is used instead of a 42 in side bar | If the WC has a wall to the rear and one side, centerline **16–18 inches (405–455 mm)** from the sidewall | Conditional | If swing-up blocking is used, hold 455 mm to the obstruction and 840–915 mm down height | Verified |
| 1104.11.2.1 | Bath door swing | Door shall not swing into any fixture CFS or clearance | Option A or B bathrooms | CFS beyond the door arc, excluding knee/toe under elements | Direct | Swing the door out or past a 1220 × 760 mm CFS | Verified |
| 1104.11.3.1.1 | Option A lavatory | Parallel-approach CFS centered on the lavatory | Option A lavatories | Not more than one lavatory per combined toilet/bathing area. Powder-room lav+WC exemption. Forward 606.3/606.4 lavatory with 1104.1.1 CFS and removable cabinetry permitted | Direct | Center a 1220 × 760 mm parallel CFS on the Option A lavatory | Verified |
| 1104.11.3.1.2.1–1104.11.3.1.2.2.4 | Option A water closet | Centerline **16–18 inches (405–455 mm)** from one side of the required clearance. Clearance **48 inches (1220 mm)** min wide × **56 inches (1420 mm)** min deep; **66 inches (1675 mm)** min deep where a forward approach is provided. Vanity/obstruction **24 inches (610 mm)** max deep may overlap if remaining WC width is **33 inches (840 mm)** min | Option A water closets | Clearance complying with Type A 1103.11.2.4.2–1103.11.2.4.4 (**60 × 56 inches (1525 × 1420 mm)**, 24 in lavatory overlap at 66 in depth) is permitted | Direct | Set WC at 405–455 mm in a 1220 × 1420 mm zone (1675 mm if forward approach) | Verified |
| 1104.11.3.1.3.1 | Option A parallel bathtub | Clearance **60 inches (1525 mm)** min length × **30 inches (760 mm)** min width in front. 606 lavatory permitted in the clearance. 1104.11.3.1 lavatory at one end permitted if a **48 × 30 inches (1220 × 760 mm)** clearance remains in front of the tub | Option A parallel-approach tub | None stated | Direct | Hold 1525 × 760 mm in front of a parallel Option A tub | Verified |
| 1104.11.3.1.3.2 | Option A forward bathtub | Clearance **60 inches (1525 mm)** min length × **48 inches (1220 mm)** min width in front. A water closet and lavatory permitted in the clearance at one end | Option A forward-approach tub | None stated | Direct | Hold 1525 × 1220 mm in front of a forward Option A tub | Verified |
| 1104.11.3.1.3.3 | Option A/B shower (only bathing fixture) | If the shower is the only bathing facility: **36 × 36 inches (915 × 915 mm)** min. Clearance **48 inches (1220 mm)** min perpendicular from the control wall × **30 inches (760 mm)** min from the shower face | Transfer shower as the only bath | **30 × 44 inches (760 × 1120 mm)** permitted. Removable shower door assembly permitted | Direct | If a shower-only Type B bath, hold 915 × 915 mm with a 1220 × 760 mm clear | Verified |
| 1104.11.3.2.1.1 | Option B lavatory height | Front of the lavatory **34 inches (865 mm)** max AFF to the higher of rim or counter, plus Option A lavatory CFS | Option B lavatory | Option B fixtures must be in a single toilet/bathing area | Direct | Specify an 865 mm max lavatory with a centered parallel CFS | Verified |
| 1104.11.3.2.3.1 | Option B bathtub | Clearance **48 inches (1220 mm)** min perpendicular from the control end × **30 inches (760 mm)** min width in front | Option B bathtub | Shower may be used instead (1104.11.3.1.3.3) | Direct | Hold 1220 × 760 mm in front of the Option B tub, measured from the control end | Verified |

## 8. Kitchens

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | Type B status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1104.12.1.1–1104.12.1.2 | Kitchen work-aisle clearance | **40 inches (1015 mm)** min between opposing bases/counters/appliances/walls. U-shape: **60 inches (1525 mm)** min | Type B kitchens | U-shape with an island may use the 1015 mm aisle | Direct | Hold 1015 mm (1525 mm if U-shaped) | Verified |
| 1104.12.2.1 | Sink CFS | Parallel-approach CFS centered on the sink bowl, sized per 1104.1.1 (**48 × 30 inches (1220 × 760 mm)**) | Type B kitchen sink | Forward sink per 1103.12.4.1 permitted | Direct | Center a 1220 × 760 mm parallel CFS on the sink; do not require Type A knee space unless the forward option is used | Verified |
| 1104.12.2.2–1104.12.2.4 | Appliance CFS | Parallel or forward CFS at dishwasher, cooktop and oven. Dishwasher/oven doors shall not obstruct their CFS. Cooktop forward needs 306 and insulated underside; parallel CFS centered | Kitchen appliances where provided | None stated | Direct | Park a 1220 × 760 mm CFS at each appliance; keep door swings clear | Verified |
| 1104.12.2.5.2–1104.12.2.5.3 | Refrigerator CFS offset | Forward approach: CFS centerline offset **15 inches (380 mm)** max from the appliance centerline. Parallel approach: offset **24 inches (610 mm)** max | Refrigerator/freezer | None stated | Direct | Align the 1220 × 760 mm CFS within 380 mm (forward) or 610 mm (parallel) of the fridge centerline | Verified |
| 1104.12.2.6 | Trash-compactor CFS | Parallel or forward CFS | Trash compactor where provided | None stated | Conditional | If a compactor is provided, park a 1220 × 760 mm CFS | Verified |

## 9. Laundry equipment

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | Type B status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1104.10.1 | Laundry clear floor space | CFS at each washer and dryer (1104.1.1 **48 × 30 inches (1220 × 760 mm)**). Parallel approach at top-load. Forward or parallel at front-load | In-unit laundry | 611 height/operable-part millimetres are **not** charged by 1104.10 | Conditional | If in-unit laundry exists, provide a 1220 × 760 mm CFS (parallel at top-load) | Verified |

## 10. In-unit ramps, elevators and platform lifts

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | Type B status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1104.6 / 405.2–405.8 | Ramp geometry | Slope steeper than 1:20 and not steeper than 1:12. Cross slope 1:48. Width **36 inches (915 mm)** min. Rise **30 inches (760 mm)** max per run. Landings **60 inches (1525 mm)** min; direction-change **60 × 60 inches (1525 × 1525 mm)**. Handrails where rise **> 6 inches (150 mm)** | Ramps inside the Type B unit | Table 405.2 flattened: **no cell adopted** | Conditional | If a unit ramp exists, hold 1:12, 915 mm and 1525 mm landings | Verified |
| 1104.7 Exception | Private-residence elevator car | Private residence elevators: clear floor **48 inches (1220 mm)** min length × **36 inches (760 mm)** min width | Private residence elevator serving the Type B unit | Full 407/408/409 otherwise. Table 407.4.1 flattened: **no destination-car cell adopted**. Note: the printed width millimetre is **(760 mm)** beside **36 inches** | Direct | If a private elevator is used, hold 1220 × 760 mm clear inside the car | Verified |
| 1104.8 Exception | Platform-lift size | Lifts with a single door or opposite-end doors: **36 inches (915 mm)** min width × **48 inches (1220 mm)** min length | Platform lifts inside the Type B unit | Full 410 otherwise (new opposite-end **36 × 52 inches (915 × 1320 mm)**) | Conditional | If a Type B lift exception is used, hold 915 × 1220 mm | Verified |

## 11. Communication-feature overlay

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | Type B status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1106.2–1106.4 / 702.1 | Visible/audible notification | Unit smoke audible per NFPA 72. Building alarm wiring extended into the unit. Visibles, where provided, comply with 702 (dwelling visibles may use 1106.2–1106.4.4) | Type B units also scoped for communication features | NFPA 72 spacing not in Chapter 7 extract | Conditional | Extend alarm wiring and provide 702/1106 visibles; this does not replace 1104 geometry | Verified |
| 1106.5.1–1106.5.2 | Doorbell and visitor ID | Hard-wired doorbell; public-side button; audible in the unit; sleeping-area visible-signal deactivation. Visual ID without opening the door; peepholes **180-degree** min | Comms-unit primary entrance | None stated | Conditional | Specify a hard-wired doorbell and 180° viewer | Verified |
| 1106.6–1106.7 | Remote entry voice/TTY | Public interface supports voice and TTY; unit interface has a telephone jack supporting voice and TTY | Remote visitor communication | None stated | Conditional | If a lobby video-phone exists, provide a TTY-capable jack | Verified |

## 12. Project-use controls

- Use **Verified** rows as design-release geometry for Type B apartment typicals.
- Do not use **Verify source** rows (flattened Table 404.2.3.2 cells beyond the printed 1104.5.1 48 in exceptions; Tables 405.2 and 407.4.1) until a readable source is confirmed.
- Do not draw Accessible/Type A 404 latch-side manoeuvre, 32 in interior doors, 52 in CFS, or 67 in room-wide turning inside Type B units.
- Grab bars are **blocking**, not in place.
- R-1 hotel application remains Conditional until residential occupancy is confirmed.

## 13. Coverage summary

- Inventory scope: numbered Chapter 11 code (1104, 1106 overlay), exceptions, charged companion paragraphs/footnotes from Chapters 3–6 and 9. INSIGHTS, figures and commentary excluded. Type C omitted. Accessible/Type A-only 804 kitchens, 611 height, 1102.15 beds and full 404 interior manoeuvre omitted as not charged.
- Total independently checkable numeric records: **198**
- Verified: **186**
- Verify source: **12**

| Top-level section | Numeric records |
|---|---|
| 1104 local + 1106 overlay | 78 |
| 303 / 306 / 308 / 309.3 | 22 |
| 403.5 / 404 primary (paragraphs + footnotes; tables held) | 38 |
| 405 / 407–410 ramps and vertical | 24 |
| 604.5 / 606–609 blocking geometry | 36 |

## 14. Unresolved-source register

| Affected table / clause | Why unverified | Control note |
|---|---|---|
| Table 404.2.3.2 (primary door, non-front approaches) | Flattened swinging-door blob | 1104.5.1 Exceptions 2–4 lock front perpendicular at **48 inches (1220 mm)**; do not adopt other reconstructed cells |
| Table 405.2 | Flattened existing-ramp blob | New ramps use paragraph 1:12 |
| Table 407.4.1 | Flattened destination-elevator blob | Type B private-residence exception **48 × 36 inches (1220 × 760 mm)** is Verified from 1104.7 |
| 609.4 | Adult grab-bar height paragraph missing/garbled | Blocking length/location from 604.5 / 1104.11.1 is Verified; confirm AFF from a readable 609.4 when bars are installed |
| 702 / NFPA 72 | No millimetre spacing in Chapter 7 | Visible layout remains NFPA 72 |
| ASME A17.1 / BHMA A156 | Named only | Do not import unstated values |
| 1104.7 Exception SI | Source prints **36 inches (760 mm)** for private-elevator width | Keep the published pair; do not “correct” to 915 mm |
