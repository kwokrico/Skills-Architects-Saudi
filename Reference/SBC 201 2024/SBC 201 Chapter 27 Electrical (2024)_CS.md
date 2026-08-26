# SBC 201 Chapter 27 Electrical
**Architect critical summary for schematic design**
2024 | SBCNC

> Scope note: This chapter **points** electrical design, construction and installation to **SBC 401**. Use/maintenance: **SBC 801**, IPMC and SBC 401. Alterations: **SBC 901** and SBC 401. The only building-code lock here is **where emergency and standby power are required** (2702). Wiring rules live in SBC 401 / **NFPA 70**.

## Regulatory Overview
Chapter 27 does not classify occupancy or construction type. It names the life-safety loads that need a generator or stored-energy source, and the 10 s / 60 s transfer split.

## Critical main topics and subtopics

### 1. Pointer and installation (2701.1, 2702.1)
Electrical work: this chapter **and SBC 401**. Emergency/standby systems: **SBC 801**, **NFPA 70** (or its equivalent in SBC 401), **NFPA 110** and **NFPA 111** (2702.1.3). Stationary generators: **UL 2200** (2702.1.1). Default load duration **2 hours** unless another section specifies otherwise (2702.1.5). Emergency power may substitute for standby (2702.1.7). Group I-2 in flood hazard areas: new essential electrical systems and generators per **ASCE 24** (2702.1.8).

| Kind | Transfer | Section |
|------|----------|---------|
| Emergency | Automatic secondary power **within 10 seconds** unless this code says otherwise | 2702.1.4 |
| Standby | Automatic secondary power **within 60 seconds** unless this code says otherwise | 2702.1.4 |

High-rise generator fuel lines inside the building: **2-hour** pipe-protection (UL 1489) or **2-hour** assembly, reduced to **1 hour** if the building is 903.3.1.1 sprinklered (2702.1.2). Critical circuits: UL 2196 cable **≥ 1 hour**, listed electrical circuit protective system **≥ 1 hour**, or **≥ 1-hour** construction (2702.3) — other sections may require 2 hours.

**SD takeaway:** Put SBC 401 / NFPA 70 on the electrical sheet; lock a 2-hour (1-hour if NFPA 13) protected fuel line if the generator sits inside a high-rise.

### 2. Where required — architect-relevant loads (2702.2)
Provided where 2702.2.1–2702.2.19 require it. Selected SD locks:

| Load | Power | Pointer | Section |
|------|-------|---------|---------|
| Elevators and platform lifts | Standby | **1009.4.1**, **1009.5**, **3003.1**, **3007.8**, **3008.8**. Commentary also: high-rise **403.4.8.3** | 2702.2.2 |
| High-rise buildings | Emergency **and** standby | **403.4.8** | 2702.2.11 |
| Underground buildings | Emergency **and** standby | **405** | 2702.2.19 |
| Means of egress illumination | Emergency, **≥ 90 minutes** | **1008.3** | 2702.2.14 |
| Exit signs | Emergency, **≥ 90 minutes** | **1013.6.3** | 2702.2.6 |
| Smoke control | Standby | **404.7**, **909.11**, **909.20.7.2**, **909.21.5** | 2702.2.17 |
| Emergency voice/alarm | Standby | NFPA 72 | 2702.2.4 |
| In-building 2-way ER communication | Standby, **100%** capacity **≥ 12 hours** | **918** and **SBC 801** | 2702.2.3 |
| I-2 essential electrical | — | **407.11** | 2702.2.8 |
| Ambulatory care essential electrical | — | **422.6** | 2702.2.1 |
| Special-purpose sliding/accordion/folding doors | Standby, **≥ 50** closing cycles | **1010.3.3** | 2702.2.18 |
| Membrane auxiliary inflation | Standby **≥ 4 hours** | **3102.8.2** | 2702.2.15 |

Other 2702.2 pointers (not expanded here): exhaust (SBC 501 / SBC 1201), gas detection (SBC 801), I-3 doors (408.4.2), hazardous materials (SBC 801), hydrogen rooms (SBC 801), laboratory suites (5004.7 / 428), semiconductor (415.11.11).

**SD takeaway:** High-rise, AMOE/FSAE/occupant-evac elevators, smoke control, and 90-minute egress lighting/exit signs are standby or emergency loads on the SD power diagram — size the plant room for them.

### Source
`Chapter_27 — ELECTRICAL.txt`. Companions named in this chapter: **SBC 401** / **NFPA 70**; **SBC 801**; **SBC 901**; **NFPA 110** / **111** / **72**; **UL 2200** / **1489** / **2196**; **ASCE 24**; SBC 201 **403.4.8**, **405**, **407.11**, **422.6**, **1008.3**, **1009.4–1009.5**, **1013.6.3**, **3003.1**, **3007.8**, **3008.8**, **909**, **918**.
