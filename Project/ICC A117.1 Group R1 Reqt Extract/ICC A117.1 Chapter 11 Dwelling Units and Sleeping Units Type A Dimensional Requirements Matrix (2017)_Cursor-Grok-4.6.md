# ICC A117.1 Chapter 11 Dwelling Units and Sleeping Units — Type A Dimensional Requirements Matrix (2017)

## 1. Document metadata and use limitation

- **Project basis:** Mixed-use tall building containing Group R-1 (hotel) with Group R-2 residential sharing podium, parking and routes. An occupied floor is stated to be more than 23 m above the relevant reference level. This matrix filters ICC A117.1 Chapter 11 for **Type A units** (Section 1103).
- **Unit type:** Type A (1103). Accessible (1102) and Type B (1104) interiors are omitted from this file. Type C (1105) is omitted.
- **Deliverable tier:** Project-use matrices in Sections 4–13 (design-check rows, not pasted inventory), plus project-use controls, a coverage summary and an unresolved-source register.
- **Code/source basis:** ICC A117.1 (2017), Chapter 11, source file `Reference\2017 ICC A117_1 Accessible and Usable Buildings and Facilities\source_reference\Chapter_11 — DWELLING UNITS AND SLEEPING UNITS.txt`. Companion numbers inlined from the attached 2017 Chapter 1–10 `source_reference` extracts where 1103 charges those sections.
- **Extraction audit:** Internal inventory: **236** independently checkable numeric records (**214** Verified, **22** Verify source). Unresolved OCR/flattened tables are listed in the register and are not design-release values.
- **Inspecting model:** Cursor Grok 4.6.
- **Prepared:** 2026-08-28.
- **Status:** Source-only architectural advisory matrix for design coordination. It is not a stamped compliance statement, accessibility consultant report, SCD NOC, SBPS approval, legal opinion, or permission to construct.
- **Scoping companion:** Counts and which units must be Type A are **SBC 201 Chapter 11**. This file is technical geometry only.
- **Edition gap:** SBC 201 Chapter 35 lists **ICC A117.1—09**. Charging SBC 1102.1 has no year. This extract is **2017**. 2017 new-building CFS, turning and door manoeuvre are larger than 2009. **Do not treat 2017 millimetres as the legal SBC minimum.**

### Scope and assumptions

1. Type A is Direct for the R-2 apartment typicals. Transient R-1 hotel rooms are not the Type A path; the gap register records that. Do not hide this matrix.
2. New construction is assumed. Existing-building dimensions are Conditional.
3. Type A uses **full 404 doors** and **304 turning** like Accessible units. Baths and kitchens are **adaptable** (removable cabinetry, grab-bar **blocking**, not grab bars in place).
4. Type A water-closet seat is **15–19 inches (380–485 mm)**, not the Accessible 17–19 in range.
5. FIGURE captions are dependencies. Flattened `<table>` blobs are not reconstructed as Verified cells.

## 2. Legends

### Applicability

| Status | Meaning |
|---|---|
| **Direct** | Expected to govern Type A unit interiors once geometry is confirmed (R-2 typical). |
| **Conditional** | Governs only if the stated feature, existing-building branch, in-unit ramp/lift/elevator, or communication overlay exists; or if Type A is applied to R-1. |
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
| A117.1 edition lock | Extracted edition is **2017**; SBC 201 Chapter 35 lists **A117.1—09** | 2017 new CFS **52 × 30 inches (1320 × 760 mm)** and turning **67 inches (1700 mm)** exceed 2009 | AHJ to lock 2009 vs 2017; do not treat this extract as the legal SBC minimum |
| Occupancy path | Mixed R-1 hotel + R-2 apartments | Type A is the R-2 adaptable typical, not the transient R-1 Accessible-guestroom path | Apply this matrix to R-2 Type A apartments; do not relabel hotel Accessible rooms as Type A |
| New vs existing | New construction assumed | 403.5 / 304.3 / 305.3 / 404.2.3 / 608.2.1.2 split new/existing | Hold Direct rows on the new-building option set |
| Grab bars | Type A is blocking, not bars in place | 1103.11.1 charges 604.5 / 607.4 / 608.3 reinforcement; vertical WC side-bar component is not required | Draw removable bases and blocking; do not install Accessible-unit grab bars as the Type A typical |
| Kitchenette vs full kitchen | Unconfirmed | 1103.12 work surface is not required without a cooktop/conventional range | Confirm whether Type A units have a range before locking the 30 in work surface |
| AHJ / NOC | Unconfirmed | Stamped compliance cannot be concluded from this extract | Engage the qualified local accessibility consultant before design freeze |

## 4. Unit accessible route, turning and walking surfaces

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | Type A status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1103.2 | Primary entrance location | Primary entrance on an accessible route from public and common areas; not to a bedroom unless it is the only entrance | Type A units | None stated | Direct | Place the Type A entry on the corridor accessible route | Verified |
| 1103.3.1 | Unit accessible-route extent | At least one accessible route shall connect all spaces and elements that are part of the unit and shall coincide with or be in the same area as the general circulation path | Type A interiors | Unfinished attics and unfinished basements | Direct | Connect entry, bedrooms, living, required bath and kitchen on one accessible route | Verified |
| 1103.3.2 / 304.3.1.1 | New circular turning space | All rooms served by the accessible route shall provide a circular turning space **67 inches (1700 mm)** minimum diameter | Rooms on the Type A accessible route | Not required in toilets/baths that are not the 1103.11.2 room; not required in closets or pantries **48 inches (1220 mm)** maximum depth; existing circular is **60 inches (1525 mm)** | Direct | Hold a 1700 mm turning circle in habitable rooms and the required bath | Verified |
| 1103.3.2 / 304.3.2.1 | New T-shaped turning option set | New T-turn is one of: **68 × 60 inches (1725 × 1525 mm)** with arms/base **36 inches (915 mm)** and **8-inch (205 mm)** chamfers; or **64 × 60 inches (1625 × 1525 mm)** with arms **38 inches (965 mm)** and base **42 inches (1065 mm)**; or **64 × 60 inches (1625 × 1525 mm)** with arms/base **40 inches (1015 mm)** | Rooms where a T-turn is used instead of a circle | Existing T-turn is a **60-inch (1525 mm)** square with arms/base **36 inches (915 mm)** | Direct | Pick one new T-option; do not mix the existing 1525 mm T on a new Direct plan | Verified |
| 304.3.1.1.1 | Turning-space knee/toe overlap | Circular-turn overlap **10 inches (255 mm)** maximum, not exceeding the knee/toe provided, only in Figure 304.3.1.1 | Turning under a fixture or counter | Figure-defined shaded zone | Direct | Limit vanity overlap into the 1700 mm circle to 255 mm | Verified |
| 1103.3.3 / 403.3 | Walking-surface slope | Running slope not steeper than 1:20; cross slope not steeper than 1:48 | Type A walking surfaces | Steeper surfaces become ramps (405) | Direct | Hold unit floors at 1:20 / 1:48 | Verified |
| 1103.4 / 403.5.1 | Interior accessible-route clear width | Interior **36 inches (915 mm)** minimum; exterior **48 inches (1220 mm)** minimum | Type A accessible routes | New pinch: **32 inches (815 mm)** for **24 inches (610 mm)** max, separated by **52 × 36 inches (1320 × 915 mm)**; existing pinch uses **48 inches (1220 mm)** separators; exterior seating **36 inches (915 mm)**; exterior ramp → 405.5 | Direct | Hold interior circulation at 915 mm; document any local pinch | Verified |
| 1103.4 / 403.5.2.1 | New 180-degree turn widths | Around an object **≥ 52 inches (1320 mm)**, new 90° options apply. Narrower object: **36 / 60 / 36 inches (915 / 1525 / 915 mm)**; or **42 / 48 / 42 inches (1065 / 1220 / 1065 mm)**; or **43 inches (1090 mm)** throughout | 180-degree turns | Existing 180° around object **< 48 inches (1220 mm)** is **42 / 48 / 42 inches (1065 / 1220 / 1065 mm)**, waived if the turn is **60 inches (1525 mm)** | Direct | Dimension 180° turns to one new option set | Verified |
| 1103.4 / 403.5.3.1 | New 90-degree turn widths | Both legs **40 inches (1015 mm)** held **28 inches (710 mm)** from the inner corner; or **8-inch (205 mm)** chamfers with both legs **36 inches (915 mm)**; or **42 / 38 inches (1065 / 965 mm)**; or **44 / 36 inches (1120 / 915 mm)** | 90-degree turns | Not required at 404.2.3 doors or 407–410 lifts; existing 90° is **36 inches (915 mm)** both legs | Direct | Pick one new 90° option at unit corners | Verified |
| 1103.4 / 403.5.4.1 | New passing space | Width **< 60 inches (1525 mm)**: passing at **200 feet (61 m)** max; **60 × 60 inches (1525 × 1525 mm)** or T-turn per 304.3.2.1 with arms/base **52 inches (1320 mm)** beyond the intersection | Long Type A routes under 1525 mm | Existing T-arm extension **48 inches (1220 mm)** | Conditional | Add a 1525 mm passing bay on any Type A corridor longer than 61 m under 1525 mm | Verified |
| 1103.4 / 303.2–303.4 | Change in level | Vertical **1/4 inch (6.4 mm)** max; **1/4–1/2 inch (6.4–13 mm)** beveled 1:2; above **1/2 inch (13 mm)** by ramp 405 or curb ramp 406 | Type A walking surfaces | None stated | Direct | Limit floor/balcony joints to 6.4 mm vertical or 13 mm at 1:2 | Verified |

## 5. Doors and doorways

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | Type A status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1103.5 / 404.2.2 | Passage-door clear opening | **32 inches (815 mm)** minimum clear, door face to stop at 90°. Openings more than **24 inches (610 mm)** deep without a door: **36 inches (915 mm)**. No projections below **34 inches (865 mm)** AFF; **34–80 inches (865–2030 mm)** AFF projections **4 inches (100 mm)** max | Primary entrance and all user-passage doors | Closers/stops **78 inches (1980 mm)** min AFF; alterations latch-stop **5/8 inch (16 mm)** | Direct | Specify 815 mm clear; do not use Type B **31 3/4 inches (805 mm)** | Verified |
| 1103.5 Exception 1 | Exterior sliding threshold | Exterior sliding-door threshold **3/4 inch (19 mm)** maximum, beveled not greater than 1:2 | Type A exterior sliding doors | General 404.2.4 remains **1/2 inch (13 mm)** at other doors | Direct | Allow 19 mm at 1:2 only on exterior sliders | Verified |
| 1103.5 / Table 404.2.3.2 | Swinging-door manoeuvre table | Manoeuvre per Table 404.2.3.2 | Manual swinging user-passage doors | Flattened blob: **no cell adopted**. Readable footnotes: +**6 inches (150 mm)** closer+latch (fn 1) or closer (fn 2); +**12 inches (305 mm)** beyond latch if closer+latch (fn 3); hinge-side push beyond hinge (fn 4); existing front-push **48 inches (1220 mm)** (fn 5). 1103.5 does not require 404.2.3 on the room side of non-required baths, at closet/pantry ≤ **48 inches (1220 mm)** deep, or on undersized balcony exteriors; 404.2.5 series turning is not required | External verification | Hold manoeuvre off a readable table; apply footnotes now | Verify source |
| 1103.5 / Table 404.2.3.3–404.2.3.4 | Sliding and cased-opening manoeuvre | Tables 404.2.3.3 and 404.2.3.4 | Sliding/folding doors and cased openings **< 36 inches (915 mm)** | Flattened blobs: **no cell adopted**. Recess trigger 404.2.3.5: obstruction within **18 inches (455 mm)** of latch projecting **> 8 inches (205 mm)** | External verification | Confirm from readable tables; apply the 455/205 mm recess trigger | Verify source |
| 1103.5 / 404.2.4 | Door threshold (other than Ex. 1) | Thresholds **1/2 inch (13 mm)** maximum | Type A doorways other than exterior sliders | Existing/altered **3/4 inch (19 mm)** with 1:2 bevel above **1/4 inch (6.4 mm)** | Direct | Specify 13 mm max at swing doors | Verified |
| 1103.5 / 404.2.6 | Door hardware force and height | Push/pull **15 pounds (66.7 N)** max; rotational **28 inch-pounds (315 N·cm)** max. Hardware **34–48 inches (865–1220 mm)** AFF | Type A door hardware | Security-personnel-only doors | Direct | Schedule levers 865–1220 mm AFF | Verified |
| 1103.5 / 404.2.7–404.2.8 | Closer speed and opening force | Closer 90° to 12° in **5 seconds** min. Spring hinge 70° to closed in **1.5 seconds** min. Interior hinged/sliding/folding **5.0 pounds (22.2 N)** max | Doors with closers or interior swing/slide | Fire/panic opening-force path is AHJ-scoped | Direct | Set closers to 5 s; hold interior opening force at 22.2 N | Verified |
| 1103.5 / 404.2.9–404.2.10 | Push-side smooth surface and vision lite | Smooth push side within **10 inches (255 mm)** of the floor. Vision-panel bottom **43 inches (1090 mm)** max AFF | Swinging doors; doors with viewing panels | Sliding doors; vision lites with lowest part **> 66 inches (1675 mm)** AFF | Direct | Specify a 255 mm kick plate; hold vision panels at 1090 mm max | Verified |
| 1103.5 / 404.3.3 | Automatic-door clear width | **32 inches (815 mm)** clear in power-on and power-off | Power-operated Type A doors | BHMA A156 values not imported | Conditional | Keep 815 mm clear in both power states | Verified |

## 6. Operable parts, reach and clear floor space

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | Type A status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1103.9 / 305.3.1 | New clear floor space | **52 × 30 inches (1320 × 760 mm)** minimum | Operable parts, fixtures and kitchen CFS (1103.12.2 → 305) | Existing **48 × 30 inches (1220 × 760 mm)** | Direct | Park 1320 × 760 mm CFS at controls, fixtures and appliances | Verified |
| 305.7.1–305.7.2 | Alcove CFS | Parallel alcove **60 inches (1525 mm)** min wide where depth **> 15 inches (380 mm)**. Forward alcove **36 inches (915 mm)** min wide where depth **> 24 inches (610 mm)** | CFS confined on three sides | None stated | Direct | Widen wardrobe/kitchen alcoves accordingly | Verified |
| 1103.9 / 306.2–306.3 | Knee and toe clearance | Toe to **9 inches (230 mm)** AFF, **25 inches (635 mm)** max / **17 inches (430 mm)** min depth, **30 inches (760 mm)** width. Knee **9–27 inches (230–685 mm)** AFF, **11 inches (280 mm)** min at 9 in and **8 inches (205 mm)** min at 27 in | Forward approach at lavatory, work surface and sink | Removable cabinetry permitted under Type A lavatory, work surface and sink if removable without replacing the fixture, floor finish continues, and surrounding walls are finished | Direct | Build removable bases to the 306 envelope so the CFS works after removal | Verified |
| 1103.9 / 308.2–308.3 | Reach ranges | Unobstructed high **48 inches (1220 mm)** / low **15 inches (380 mm)**. Obstructed forward: **48 inches (1220 mm)** at **≤ 20 inches (510 mm)** depth, **44 inches (1120 mm)** at **20–25 inches (510–635 mm)**. Obstructed side: obstruction **34 inches (865 mm)** max high × **24 inches (610 mm)** max deep; high side **48 inches (1220 mm)** at **10 inches (255 mm)** depth, **46 inches (1170 mm)** at **24 inches (610 mm)** | Lighting, panelboards, switches, receptacles, environmental, appliance, plumbing and security/intercom controls | Existing unaltered side reach **54 inches (1370 mm)** | Direct | Place Type A controls in the 380–1220 mm envelope, including plumbing/appliance controls | Verified |
| 1103.9 / 309.4 | Operable-part force | One hand; no tight grasp/pinch/wrist twist; **5.0 pounds (22.2 N)** maximum | Type A operable parts listed in 1103.9 | 309.1 exceptions (dedicated receptacles, one of two-plus kitchen counter receptacles, corner ≤ **9 square feet (0.835 m²)**, floor receptacles, HVAC, ceiling fans, redundant non-light controls, resets, panelboards vs 309.4) | Direct | Specify 22.2 N rocker devices; apply kitchen receptacle exceptions | Verified |

## 7. Toilet and bathing facilities (adaptable)

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | Type A status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1103.11 / 1103.11.2 | Required Type A bath set | At least one toilet/bathing facility complies with 1103.11.2. At least one lavatory, one water closet and either a bathtub or shower in a single area so travel between fixtures does not go through other parts of the unit. All baths comply with 1103.11.1 blocking | Type A units | None stated | Direct | Put WC, lav and tub or shower in one adaptable bathroom | Verified |
| 1103.11.1 | Grab-bar and seat blocking | Reinforcement for future 604.5 WC bars, 607.4 tub bars, and 608.3 / 608.2.1.3 / 608.2.2.3 / 608.2.3.2 shower bars and seats | All Type A baths | Non-required fixtures may use 1104.11.1 blocking. Not required in a lav+WC-only room that is not the only lav/WC on the accessible level. Vertical WC side-bar component of 604.5 is **not** required. Lavatory-overlap exception: rear-wall blocking for a **24-inch (610 mm)** min bar centered on the WC | Direct | Back WC/tub/shower walls for future bars; omit the vertical side-bar blocking | Verified |
| 1103.11.2.1 | Bath door swing | Door shall not swing into any fixture CFS or clearance | The 1103.11.2 bathroom | CFS provided in the room beyond the door-swing arc | Direct | Swing the door out or past a 1320 × 760 mm CFS | Verified |
| 1103.11.2.2 / 606.3 | Lavatory with removable cabinetry | Lavatory complies with 606: forward 305.3 CFS, 306 knee/toe, front **34 inches (865 mm)** max AFF, faucets 309, insulated pipes | Type A required lavatory | Cabinetry permitted if removable without replacing the lavatory, floor finish continues under, and surrounding walls are finished | Direct | Draw a removable-base 865 mm lavatory; show the 306 envelope after removal | Verified |
| 1103.11.2.3 | Mirror height | Bottom of reflecting surface **40 inches (1015 mm)** maximum AFF | Mirrors above the 1103.11.2.2 lavatory | None stated | Direct | Hold the Type A bath mirror at 1015 mm max | Verified |
| 1103.11.2.4.1–1103.11.2.4.5 | Water-closet location, clearance, seat | Centerline **16 inches (405 mm)** min to **18 inches (455 mm)** max from the sidewall. Clearance **60 inches (1525 mm)** min wide × **56 inches (1420 mm)** min deep. Seat **15 inches (380 mm)** min to **19 inches (485 mm)** max AFF | Type A required water closet | Overlap of WC, grab bars, dispensers, hooks, shelves, accessible routes, other fixture CFS and the turning space is permitted. Lavatory **24 inches (610 mm)** max deep on the rear wall, **18 inches (455 mm)** min from WC centerline to lavatory side edge, if WC clearance depth is **66 inches (1675 mm)** min | Direct | Set WC at 405–455 mm in a 1525 × 1420 mm zone; seat 380–485 mm (not Accessible 430–485 mm) | Verified |
| 1103.11.2.4.6 | Flush control | Hand-operated or automatic; hand-operated 309; on the open side of the water closet | Type A required WC | None stated | Direct | Place the flush on the open side in the 308/309 envelope | Verified |
| 1103.11.2.5.1 / 607.2 | Bathtub clearance with removable cabinetry | Tub complies with 607: clearance the length of the tub × **30 inches (760 mm)** min depth; +**12 inches (305 mm)** beyond a permanent head-end seat. Seat per 610. Controls, **59-inch (1500 mm)** hand shower, **120°F (49°C)** water | Type A required bathtub | Countertops/cabinetry at one end of the clearance if removable, floor finish continues, and surrounding walls are finished. Grab bars are **blocking** (1103.11.1), not 607.4 bars in place | Direct | Hold a 760 mm tub clear; show removable end cabinetry; back for 607.4 bars | Verified |
| 1103.11.2.5.2 / 608.2 | Shower with removable cabinetry | Shower complies with 608 (transfer **36 × 36 inches (915 × 915 mm)** with new **52 × 36 inches (1320 × 915 mm)** clear; standard roll-in **60 × 30 inches (1525 × 760 mm)** with **60 × 30 inches (1525 × 760 mm)** clear; alternate roll-in **60 × 36 inches (1525 × 915 mm)**). Hand shower required (608.5 Accessible/Type A). Threshold **1/2 inch (13 mm)** | Type A required shower | At 608.2.2 standard roll-in, lavatory/counter/cabinetry permitted at one end of the clearance if removable, floor finish continues, and walls are finished. Grab bars/seats are blocking | Direct | Prefer a 1525 × 760 mm roll-in; show removable end cabinetry; back for 608.3 bars and 610 seat | Verified |
| 604.5.1–604.5.2 | Future WC grab-bar geometry (blocking) | Side horizontal **42 inches (1065 mm)** min, **12 inches (305 mm)** max from rear wall, extending **54 inches (1370 mm)** min; vertical **18 inches (455 mm)** min at **39–41 inches (990–1040 mm)** AFF and from rear wall — vertical component **not required** to be blocked (1103.11.1 Ex. 3). Rear **36 inches (915 mm)** min, **6 inches (150 mm)** max from side wall, extending **42 inches (1065 mm)** min | Type A WC blocking | Rear **24 inches (610 mm)** min centered where lavatory overlap exception applies | Direct | Block for the 1065 mm side horizontal and 915 mm rear bar; skip vertical side-bar blocking | Verified |
| 609.2–609.3 / 609.8 | Grab-bar product (when installed) | Circular OD **1 1/4–2 inches (32–51 mm)**; wall clearance **1 1/2 inches (38 mm)**; **250 pounds (1112 N)** | Future bars | Adult 609.4 height unverified in the Chapter 6 extract | External verification | Size blocking for 32–51 mm bars at 38 mm off the wall and 1112 N; confirm 609.4 AFF later | Verify source |

## 8. Kitchens

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | Type A status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1103.12.1.1–1103.12.1.2 | Kitchen work-aisle clearance | **40 inches (1015 mm)** min between opposing bases/counters/appliances/walls. U-shape (three contiguous sides): **60 inches (1525 mm)** min | Type A kitchens | U-shape with an island may use the 1015 mm aisle | Direct | Hold 1015 mm (1525 mm if U-shaped) | Verified |
| 1103.12.3–1103.12.3.2 | Work surface | At least one section **30 inches (760 mm)** min length. Forward CFS + 306 knee/toe. Height **34 inches (865 mm)** max AFF | Type A kitchens with a cooktop or conventional range | Not required without cooktop/conventional range. Removable cabinetry permitted (remove without replacing the work surface; floor and walls finished). Adjustable/relocatable **29–36 inches (735–915 mm)** AFF without cutting the counter | Direct | Provide a 760 mm × 865 mm max work surface with removable base and 306 clearance | Verified |
| 1103.12.4.1–1103.12.4.4 | Sink | Forward CFS + 306. Front **34 inches (865 mm)** max AFF to the higher of rim or counter. Faucets 309. Pipes insulated | Type A kitchen sink | Knee/toe at only one bowl of a multi-bowl sink; removable cabinetry permitted; parallel centered CFS permitted where no cooktop/range and at wet bars. Adjustable **29–36 inches (735–915 mm)** if rough-in allows **29 inches (735 mm)** connections | Direct | Specify an 865 mm max sink with removable base (or parallel CFS if no range) | Verified |
| 1103.12.5.1–1103.12.5.5 | Appliance CFS and approach | CFS parallel or forward at each appliance. Dishwasher door shall not obstruct its CFS or an adjacent sink. Cooktop forward needs 306 and insulated underside; parallel CFS centered. Oven door shall not obstruct its CFS; side-hinged ovens get a countertop on the latch side; bottom-hinged on one side. Controls shall not require reaching across burners. Appliance controls comply with 1103.9 | Kitchen appliances where provided | Appliance doors/latches exempt from 309.4; open bottom-hinged doors exempt from 309.3 | Direct | Park a 1320 × 760 mm CFS at each appliance; keep oven swing clear | Verified |
| 1103.12.5.6 | Refrigerator/freezer | At least **50 percent** of freezer shelves including the freezer bottom **54 inches (1370 mm)** max AFF at maximum shelf positions. Parallel CFS; centerline offset **24 inches (610 mm)** max from the appliance centerline | Combination refrigerator/freezer | None stated | Direct | Specify ≥ 50% of the freezer at or below 1370 mm with CFS offset ≤ 610 mm | Verified |

## 9. Laundry equipment

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | Type A status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1103.10 / 611.2–611.4 | Laundry CFS, reach, height | Parallel CFS; top-load centered; front-load offset **24 inches (610 mm)** max. Operable parts 308/309; 308.3.2 obstruction **36 inches (915 mm)** max. Top-load door **36 inches (915 mm)** max AFF; front-load opening **15–36 inches (380–915 mm)** AFF | Washers and dryers in the Type A unit | None stated | Conditional | If in-unit laundry exists, provide a 1320 × 760 mm CFS and 380–915 mm openings | Verified |

## 10. Windows and storage

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | Type A status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1103.13.1–1103.13.2 | Operable windows | Natural-ventilation windows: 309.2 CFS and 309.3 reach. Emergency-escape windows: 309.2 CFS. (Type A does not charge 506.2 opening-force newtons) | Operable windows in Type A units | Kitchen and bathroom windows | Direct | Provide a 1320 × 760 mm CFS at the ventilation/escape window and keep locks in the 308 envelope | Verified |
| 1103.14 / 905.2–905.4 | Storage | At least one of each type: CFS, 308 reach, 309 operable parts | Storage other than kitchen cabinets | Kitchen cabinets exempt | Direct | Put one rod/shelf of each type in the 380–1220 mm range with a CFS | Verified |

## 11. In-unit ramps, elevators and platform lifts

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | Type A status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1103.6 / 405.2–405.8 | Ramp geometry | Slope steeper than 1:20 and not steeper than 1:12. Cross slope 1:48. Width **36 inches (915 mm)** min. Rise **30 inches (760 mm)** max per run. Landings **60 inches (1525 mm)** min; direction-change **60 × 60 inches (1525 × 1525 mm)**. Handrails where rise **> 6 inches (150 mm)** | Ramps inside the Type A unit | Table 405.2 flattened: **no cell adopted** | Conditional | If a unit ramp exists, hold 1:12, 915 mm and 1525 mm landings | Verified |
| 1103.7 / Table 407.4.1 | Destination-elevator car size | Elevators within the unit comply with 407, 408 or 409 | Elevators inside the Type A unit | Flattened Table 407.4.1: **no cell adopted**. Fn 1 **7/8 inch (16 mm)**; fn 2 **36-inch (915 mm)** door with **60-inch (1525 mm)** turning diameter | External verification | Confirm car size from a readable table | Verify source |
| 1103.7 / 408.4.1 / 409.4.1.1 | LULA and new private elevator | LULA: width **42 inches (1065 mm)** min, area **15.75 square feet (1.46 m²)**. New private-residence elevator: **36 × 52 inches (915 × 1320 mm)** | LULA or private elevator in the unit | Existing LULA and 409.4.1.2 **36 × 48 inches (915 × 1220 mm)** | Conditional | If provided, hold the new-building car size | Verified |
| 1103.8 / 410.5.1.1 | New platform-lift size | Opposite-end new: **36 × 52 inches (915 × 1320 mm)**. Adjacent-side new: **42 × 60 inches (1065 × 1525 mm)**. End door **32 inches (815 mm)** min; side door **42 inches (1065 mm)** min; open **20 seconds** min | Platform lifts inside the Type A unit | Incline **36 × 48 inches (915 × 1220 mm)**; existing opposite-end **36 × 48 inches (915 × 1220 mm)** | Conditional | If a lift is used, hold 915 × 1320 mm new opposite-end | Verified |

## 12. Communication-feature overlay

| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | Type A status | Design action | Source confidence |
|---|---|---|---|---|---|---|---|
| 1106.2–1106.4 / 702.1 | Visible/audible notification | Unit smoke audible per NFPA 72. Building alarm wiring extended into the unit. Visibles, where provided, comply with 702 (dwelling visibles may use 1106.2–1106.4.4). Same appliances may serve both; not used for other purposes | Type A units also scoped for communication features | NFPA 72 spacing not in Chapter 7 extract | Conditional | Extend alarm wiring and provide 702/1106 visibles; this does not replace 1103 geometry | Verified |
| 1106.5.1–1106.5.2 | Doorbell and visitor ID | Hard-wired doorbell; public-side button; audible in the unit; sleeping-area visible-signal deactivation. Visual ID without opening the door; peepholes **180-degree** min | Comms-unit primary entrance | None stated | Conditional | Specify a hard-wired doorbell and 180° viewer | Verified |
| 1106.6–1106.7 | Remote entry voice/TTY | Public interface supports voice and TTY; unit interface has a telephone jack supporting voice and TTY | Remote visitor communication | None stated | Conditional | If a lobby video-phone exists, provide a TTY-capable jack | Verified |

## 13. Project-use controls

- Use **Verified** rows as design-release geometry for Type A apartment typicals.
- Do not use **Verify source** rows (flattened door/elevator/ramp/dispenser tables; 609.4 height) until a readable source is confirmed.
- Do not mix new **67 inches (1700 mm)** turning or **52 inches (1320 mm)** CFS with existing values on the same Direct typical.
- Do not install Accessible-unit grab bars in place as the Type A typical; draw removable bases and blocking.
- Do not apply this matrix to transient R-1 Accessible guestrooms.

## 14. Coverage summary

- Inventory scope: numbered Chapter 11 code (1103, 1106 overlay, charged 1104.11.1 exceptions), exceptions, charged companion paragraphs/footnotes from Chapters 3–9. INSIGHTS, figures and commentary excluded. Type C omitted. Public compartments, children’s toilets, urinals, drinking fountains and Chapter 10 omitted.
- Total independently checkable numeric records: **236**
- Verified: **214**
- Verify source: **22**

| Top-level section | Numeric records |
|---|---|
| 1103 local + 1106 overlay | 42 |
| 303–309 building blocks | 52 |
| 403–404 routes/doors (paragraphs + footnotes; tables held) | 46 |
| 405 / 407–410 ramps and vertical | 26 |
| 506 / 606–611 / 905 | 70 |

## 15. Unresolved-source register

| Affected table / clause | Why unverified | Control note |
|---|---|---|
| Table 404.2.3.2 | Flattened swinging-door manoeuvre blob | Do not adopt reconstructed cells; footnotes 1–5 remain Verified |
| Table 404.2.3.3 | Flattened sliding/folding blob | Confirm from a readable table |
| Table 404.2.3.4 | Flattened doorway-without-door blob | Confirm from a readable table |
| Table 405.2 | Flattened existing-ramp blob | New ramps use paragraph 1:12 |
| Table 407.4.1 | Flattened elevator-car blob | Footnotes 1–2 remain Verified |
| Table 603.6 | Flattened dispenser/dryer blob (only if a dispenser is specified) | Confirm from a readable table |
| 609.4 | Adult grab-bar height paragraph missing/garbled | Confirm AFF from a readable 609.4; do not back-fill |
| Figure 304.3.1.1 | Shaded overlap zone | Treat as a figure dependency |
| 702 / NFPA 72 | No millimetre spacing in Chapter 7 | Visible layout remains NFPA 72 |
| ASME A17.1 / BHMA A156 | Named only | Do not import unstated values |
