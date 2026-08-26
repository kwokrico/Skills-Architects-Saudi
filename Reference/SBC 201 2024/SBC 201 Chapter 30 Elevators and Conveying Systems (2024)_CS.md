# SBC 201 Chapter 30 Elevators and Conveying Systems
**Architect critical summary for schematic design**
2024 | SBCNC

> Scope note: This chapter governs **building features** of elevators and conveying systems (hoistways, lobbies, machine rooms, emergency operation, FSAE, occupant-evac). It is **not** the equipment code — cars, machines, and devices are designed to **Table 3001.3** (ASME A17.1/CSA B44 and listed companions) and **ASCE 24** in flood hazard areas (3001.1–3001.3). Accessibility millimetres live in **ICC A117.1** via 1110.8; accessible means of egress in **Section 1009**; FSAE trigger and count in **403.6.1**; occupant-evac as a high-rise option in **403.6.2**. Shaft construction is **712/713**. Fire-service keys and occupant-evac plans: **SBC 801**.

## Regulatory Overview
This chapter does not classify occupancy or construction type; it attaches elevator building elements to shafts, high-rise packages, and egress already set elsewhere. Schematic locks are stretcher-car size, hoistway/lobby protection, machine-room rating, and whether 403.6.1 FSAE or 3008 occupant-evac applies — equipment detailing stays with Table 3001.3.

## Critical main topics and subtopics

### 1. Referenced standards (3001.3, Table 3001.3)
Equipment design, construction, installation, alteration, repair, and maintenance conform to Table 3001.3 and to **ASCE 24** in flood hazard areas. Where this chapter and a listed standard differ, the code prevails (commentary to 3001.3 → 102.4). Change of use (freight ↔ passenger, or freight class) → ASME A17.1/CSA B44 **Section 8.7** (3001.5).

| Type (Table 3001.3 as printed) | Standard |
|--------------------------------|----------|
| Elevators, escalators, dumbwaiters, moving walks, material lifts | ASME A17.1/CSA B44, ASME A17.7/CSA B44.7 |
| Platform lifts, stairway chairlifts, wheelchair lifts | ASME A18.1 |
| Conveyors and related equipment | ASME B20.1 |
| Belt manlifts | ASME A90.1 |
| Automotive lifts | ALI ALCTV |
| Industrial scissors lifts | ANSI MH29.1 |

No edition years appear in this chapter’s table. Flood: keep cars/equipment from descending below design flood elevation under 3003 recall (commentary to 3001.3).

**SD takeaway:** Spec the **ASME A17.1/CSA B44** (plus A17.7, A18.1, B20.1 as applicable) package on the elevator sheet; this chapter only sizes the building around it.

### 2. Hoistway enclosures and lobby protection (3002, 3006)
Hoistway = **shaft enclosure per 712 and 713** (3002.1). Opening protectives per Chapter 7; recall-floor car/hoistway doors may remain open during Phase I (3002.1.1). Not every hoistway is required to be enclosed — see ASME A17.1 2.1.1.3 for partial enclosures (commentary).

| Rule | Limit | Section |
|------|-------|---------|
| Cars per hoistway | **≤ 4**; if **≥ 4** cars serve the same portion → **≥ 2** hoistways | 3002.2 |
| Stretcher car (where elevators are already provided) | Buildings **≥ 4 stories above or below** grade plane: **≥ 1** car per floor served, **600 mm × 2100 mm** stretcher, **≥ 125 mm** corner radius, star of life **≥ 75 mm** on both sides of hoistway door frame | 3002.4 |
| Elevator + stair | Not in a common shaft (exception: open parking garages) | 3002.7 |
| Plumbing / mechanical in hoistway | Prohibited (exception: floor drains/sumps at base, **indirect** connection) | 3002.9 |
| Extra door at car access | Only if openable from the car without key, tool, special knowledge or effort | 3002.6 |
| Blind / exterior hoistway | Emergency door per ASME A17.1/CSA B44 | 3002.5 |
| Glass | 2409.2 | 3002.8 |
| Fire sign at call station | “IN CASE OF FIRE, ELEVATORS ARE OUT OF SERVICE. USE EXIT STAIRS” — **not** on 1009.4 AMOE or 3008 occupant-evac elevators | 3002.3 |

**3006.2 — not an automatic lobby at three stories.** Hoistway **door openings** shall be protected per 3006.3 where **all** of the following hold: the hoistway connects **more than three stories**; it is required to be a shaft per **712.1.1**; **and** any of:

| Trigger | Section |
|---------|---------|
| Building **not** sprinklered throughout (903.3.1.1 or 903.3.1.2) | 3006.2 item 1 |
| Group **I-1 Condition 2**, **I-2**, or **I-3** | 3006.2 items 2–4 |
| High-rise **and** hoistway height **> 23 m** (lowest to highest floor served) | 3006.2 item 5 |
| Rated corridor required by 1020.2 | 3006.2.1 |

Exceptions to 3006.2: open parking garages (406.5); **level(s) of exit discharge** if that level is 903.3.1.1 sprinklered; openings to the **exterior**.

**3006.3 methods** (when 3006.2 applies) — pick one:

| Method | What to draw |
|--------|----------------|
| 1 Enclosed lobby | **708** fire partitions; lobby doors as corridor doors (716.2.2.1); ducts as corridors (717.5.4.1) |
| 2 Enclosed lobby (sprinklered) | **710** smoke partitions + listed door/duct rules |
| 3 Additional doors at hoistway | 3002.6 + smoke/draft (716.2.2.1.1) tested **UL 1784** without artificial bottom seal |
| 4 Pressurization | **909.21** |

FSAE and occupant-evac **enclosed** lobbies (3007.6 / 3008.6) override these options when those systems are used (3006.1 items 4–5). Underground buildings: enclosed lobbies per **405.4.3**. Area of refuge in a lobby: **1009.6**. Lobby needs **≥ 1** means of egress (Chapter 10); egress through a lobby is permitted per 1016.2 item 1 (3006.4).

**SD takeaway:** Do not assume a lobby at three stories — 3006.2 is **> 3 stories + shaft + (unsprinklered / I-1 Cond. 2 / I-2 / I-3 / high-rise hoistway > 23 m)** or a rated corridor; FSAE/OEE always get their own enclosed lobby.

### 3. Emergency operations (3003)
3003 does **not** require standby power; it governs how it operates **where required or furnished** (403.4.8.2 high-rise, 1009.4 AMOE, 3007.8 FSAE, 3008.8 occupant-evac).

| Rule | Requirement | Section |
|------|-------------|---------|
| Manual transfer | Standby power **manually transferable** to all elevators in each bank | 3003.1.1 |
| One elevator | Auto-transfer **within 60 s** of normal-power failure | 3003.1.2 |
| Two or more (common operating system) | All auto-transfer in 60 s if source can run all; else sequential return to designated landing, then **≥ 1** remains on standby | 3003.1.3 |
| Machine-room HVAC | On the same standby source as the elevators | 3003.1.4 |
| Fire-fighter operation | Phase I recall + Phase II in-car per ASME A17.1/CSA B44 | 3003.2 |
| Keys | Standardized fire-service elevator key per **SBC 801** | 3003.3 |

Commentary: 3008 needs **all** occupant-evac cars on standby — sequential 3003.1.3 transfer is not a substitute. ASME A17.1 may omit Phase I/II for rise **≤ 2000 mm** with no floor penetration / unrated hoistway, and LU/LA unless those features are installed.

**SD takeaway:** Size standby so FSAE and occupant-evac cars stay up; 3003 sequencing is only for ordinary banks, not 3008.

### 4. Machine rooms, control rooms, machinery and control spaces (3005)
Approved access to machine rooms, control rooms, control spaces, and machinery spaces (3005.1). Independent ventilation or air-conditioning to the equipment temperature range (3005.2). If the hoistway is pressurized, rooms/spaces with openings into it pressurize on heat/smoke detection in those rooms (3005.3). No plumbing in elevator equipment rooms (3005.6).

**Enclosure (3005.4)** — fire barriers (707) and/or horizontal assemblies (711) at **not less than the hoistway rating**; openings rated not less than hoistway doors.

| Exception (not FSAE, not occupant-evac) | Rating |
|-----------------------------------------|--------|
| Rooms/spaces **do not abut** and have **no openings** to the hoistway they serve | Reduce to **1 hour** |
| Same, and building **≤ 4 stories** above grade plane | Rating **not required** |

**Shunt trip (3005.5):** where those spaces or the hoistway are sprinklered, disconnect main-line power per NFPA 72 **21.4** before water; not self-resetting; sprinklers **outside** those spaces shall not trip the elevator. **Do not** install shunt trip on FSAE (3007.4) or occupant-evac (3008.4).

**SD takeaway:** Match machine-room rating to the hoistway unless the room is detached (1 h, or unrated if ≤ 4 stories); keep sprinklers **out** of FSAE/OEE machine spaces so shunt trip is never needed.

### 5. Fire service access elevators (3007; trigger 403.6.1)
Charging 3007.1: FSAE are provided **where required by 403.6.1**, and **every floor at and above** the lowest level of fire-department vehicle access shall be served, installed per this chapter and ASME A17.1/CSA B44.

Exceptions: elevators that only serve an open/enclosed parking garage and the building lobby; the **top floor** if it is equipment-only.

**Verify vs 403.6.1:** this chapter does **not** independently set the count or the height. Commentary to 3007.1 states a **minimum of two** FSAE in buildings with an **occupied floor more than 36 m** above the lowest level of fire-department vehicle access **in accordance with 403.6.1**. Commentary also: every floor served by **at least two** FSAE; FSAE may be passenger or service and may be the 1110.4 accessible-egress car. Confirm the 36 m / two-car numbers on the **403.6.1** sheet — do not treat commentary as a substitute for that section.

| Package item | Rule | Section |
|--------------|------|---------|
| Sprinklers | Building throughout 903.3.1.1; **no** sprinklers in FSAE machine rooms, machinery spaces, control rooms/spaces, or hoistways | 3007.2, 3007.2.1 |
| Water at lobby | Approved method to keep sprinkler water **outside** the hoistway | 3007.3 |
| Shunt trip | **Not** installed | 3007.4 |
| Hoistway | Shaft 713; structural integrity **403.2.2.1–403.2.2.4**; hoistway lighting **≥ 11 lux** (top of car) when firefighters’ emergency operation is active | 3007.5–3007.5.2 |
| Lobby | Enclosed 3007.6.1–3007.6.5; second entrance on a floor may use 3006.3 | 3007.6 |
| Stair/ramp | **Direct** access from lobby to interior exit stair/ramp (or equivalent protected path + smoke/draft door) | 3007.6.1 |
| Lobby enclosure | **1-hour smoke barrier** (not required at levels of exit discharge) | 3007.6.2 |
| Lobby doors | **¾-hour** fire door + smoke/draft, UL 1784 **without** artificial bottom seal (not hoistway/control-room doors) | 3007.6.3 |
| Lobby size | **≥ 14 m²**, min dimension **2.4 m** — same size even if several FSAE share the lobby | 3007.6.4 |
| Symbol | Standardized “fire hat” **≥ 75 mm**, **1.9–2 m** AFF, both sides of frame facing the FSAE lobby | 3007.6.5 |
| Monitoring | Continuous at fire command center, NFPA 72 interface | 3007.7 |
| Power | Normal + **Type 60/Class 72** (extract as printed) to equipment, hoistway lighting, machine-room HVAC, car lighting; 2-hour protection of critical wiring (UL 2196, listed system, or 2-hour construction) | 3007.8, 3007.8.1 |
| Standpipe | Class I hose connection (905) in the interior exit stair/ramp with **direct** lobby access; that enclosure reaches the floor **without** passing through the FSAE lobby | 3007.9, 3007.9.1 |

**SD takeaway:** If 403.6.1 applies (commentary: occupied floor **> 36 m** above FD access → **≥ 2** FSAE), lock a **14 m² / 2.4 m** smoke-barrier lobby with a direct stair and Class I standpipe on **every** occupied floor from FD access up.

### 6. Occupant evacuation elevators (3008)
Optional system for occupant **self-evacuation before Phase I recall** (3008.1). Commentary: 403.6.2 permits designating passenger elevators; 3008 may be used in buildings that are not high-rise if the full package is met. Operation: ASME A17.1/CSA B44 **2.27.11** + the building fire-safety plan (3008.1.4). Plan per **SBC 801 Section 404** (3008.1.3).

| Item | Rule | Section |
|------|------|---------|
| Number | Egress analysis: full-building time **< 1 hour**, **or** five consecutive highest-OL floors **< 15 minutes**; **≥ 1** per bank; **≥ 2** where more than one car opens into the lobby | 3008.1.1 |
| Extra high-rise stair | Additional exit stair required by **403.5.2** is **not** required if 3008 occupant-evac is provided | 3008.1.2 |
| Sprinklers / water / shunt | Same pattern as FSAE: 903.3.1.1 throughout; **no** sprinklers in OEE machine/hoistway spaces; keep lobby sprinkler water out of hoistway; **no** shunt trip | 3008.2–3008.4 |
| Hoistway | Shaft 713; structural integrity 403.2.2.1–403.2.2.4 | 3008.5, 3008.5.1 |
| Lobby | Enclosed 3008.6; not required at levels of exit discharge | 3008.6.2 |
| Stair | Direct access to interior exit stair/ramp (protected-path exception; parking-only elevators exempt) | 3008.6.1 |
| Lobby doors | **¾-hour** + smoke/draft, UL 1784 without bottom seal; **vision panel**; auto-close on EVAC signal | 3008.6.3–3008.6.3.2 |
| Lobby size | **25%** of floor OL at **0.27 m²**/person **plus** one **0.75 m × 1.2 m** wheelchair space per **50** persons of floor OL (or fraction) | 3008.6.4 |
| Signage / comms | Approved self-evac sign at each call station; two-way comms to FCC per **1009.8.1–1009.8.2** | 3008.6.5, 3008.6.6 |
| Monitoring / recall | FCC (or FD-approved point) displays car location, direction, occupancy, power, alarm status; manual Phase I from that location | 3008.7, 3008.7.1 |
| Power | Normal + **Type 60/Class 2/Level 1** standby to equipment, machine HVAC, car lighting; load from 3008.1.1 count; 2-hour wiring protection | 3008.8–3008.8.2 |
| EVAC | Building EVAC (907.5.2.2); **≥ 1** audible **and** **≥ 1** visible appliance in each OEE lobby | 3008.9, 3008.9.1 |
| Hazardous materials | No areas exceeding MAQ per control area (414.2) — commentary: no Group H | 3008.10 |

OEE and FSAE may share a lobby; apply the more restrictive of 3007 and 3008 (commentary to 3007.6 / 3008.6). Charging lobby area is **0.27 m²**/person; do not substitute the 0.3 m figure-table OCR.

**SD takeaway:** Occupant-evac is a **choice** that can drop the 403.5.2 extra stair — only if you lock large 25%-OL lobbies, EVAC, and standby on the analyzed car count, not on a single shuttle.

### 7. Accessible elevators (3001.2, 3001.4)
Passenger elevators required to be accessible **or** to serve as part of an accessible means of egress shall comply with **Sections 1009 and 1110.8** (3001.4). Commentary: 1110.8 makes elevators on an accessible route accessible; 1009 may require an elevator as AMOE; **ICC A117.1** supplies car/door/control/signal criteria (destination-oriented, LU/LA, private-residence, and standard passenger). **No A117.1 year** is stated in this chapter. Which elevator type may be used is limited by ASME A17.1/CSA B44 (e.g. private-residence elevators only to/in a private dwelling).

**3001.2** emergency two-way communication: visible **text** and **audible** modes; live interactive back-and-forth with emergency personnel; operational whenever the elevator is operational; occupant selects text or audible.

**SD takeaway:** Accessible passenger cars follow **1110.8 + 1009 + ICC A117.1** (year not in this chapter — use Chapter 11 / Chapter 35); LU/LA and private-residence types only where ASME A17.1 allows.

### Source
`Chapter_30 — ELEVATORS AND CONVEYING SYSTEMS.txt`

Companions named in this chapter: **ASME A17.1/CSA B44** (and A17.7/CSA B44.7, A18.1, A90.1, B20.1, ALI ALCTV, ANSI MH29.1, ASCE 24); **ICC A117.1** (no year here); **SBC 801** (keys 3003.3; fire-safety plan 3008.1.3); **NFPA 72** (shunt 21.4; FSAE monitoring); **NFPA 13** (escalator draft-curtain method in commentary); **UL 1784**, **UL 2196**; SBC 201 **712/713**, **707/708/710/711**, **716/717**, **903**, **905**, **907**, **909.21**, **1009**, **1016.2**, **1020.2**, **1110.8**, **2409.2**, **403.2.2**, **403.5.2**, **403.6.1**, **403.6.2**, **405.4.3**, **414.2**.
