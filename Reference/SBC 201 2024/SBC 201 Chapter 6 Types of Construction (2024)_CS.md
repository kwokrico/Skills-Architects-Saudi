# SBC 201 Chapter 6 Types of Construction
**Architect critical summary for schematic design**
2024 | SBCNC

> Scope note: This chapter assigns every building to Type I–V (with A/B or IV-A/B/C/HT) and sets minimum fire-resistance of building elements in Table 601. It is not the height/area chapter (Ch. 5) and not the fire-separation-distance chapter (Table 705.5). Exterior walls take the **higher** of Table 601 and Table 705.5. Multiple construction types in one structure are allowed only where the code says so (notably Section 510 podiums) or where a fire wall creates two buildings.

## Regulatory Overview
Types I and II are noncombustible building elements (combustibles only as Section 603 allows); Type III has noncombustible exterior walls and any code-permitted interior; Type IV is mass timber or noncombustible; Type V may be combustible or mixed. The A vs B (and IV-A/B/C vs HT) suffix is fire-resistance and encapsulation, not sprinkler protection.

## Critical main topics and subtopics

### 1. Construction-type menu (601.1, 602.1–602.5)
| Type | Materials | Subtypes |
|------|-----------|----------|
| I, II | Noncombustible elements (FRTW and listed combustibles per 603) | IA, IB, IIA, IIB |
| III | Noncombustible exterior walls; interior any permitted material; FRTW framing/sheathing in exterior walls rated **≤ 2 h** | IIIA, IIIB |
| IV | Mass timber or noncombustible; light-frame wood **excluded** from IV-A/B/C | IV-A, IV-B, IV-C, IV-HT |
| V | Combustible or noncombustible or both | VA, VB |

A building that only partly meets a higher type is classified as the type it fully meets (602.1.1). The permit documents should state the chosen type.

Commentary primary-frame ratings from Table 601: **IA 3 h**, **IB 2 h**, **IIA 1 h**, **IIB 0 h**. Type III load-bearing exterior walls: **2 h** (Table 601). HT in the table means no hourly rating — use Sections 602.4.4 and 2304.11 sizes instead.

**SD takeaway:** Write the construction type on the SD code sheet; height/area tables will not run without it, and you cannot mix types later except via fire wall or Section 510.

### 2. Table 601 vs Table 705.5 (601, 602.1, Notes e–f)
| Element | Rating source |
|---------|----------------|
| Primary structural frame | Table 601; members in/on exterior walls also vs Table 705.5 and exterior bearing-wall rating (highest of three — Note f / 704.10) |
| Exterior **bearing** walls | **Higher** of Table 601 and Table 705.5 (FSD) |
| Exterior **nonbearing** walls | Table 705.5 only |
| Interior nonbearing walls | Table 601 typically 0 h; other sections (corridors, dwelling separations, incidental uses) may add a rating |
| Floor / roof + secondary members | Table 601 + Section 711 |

Table 601 ratings do **not** by themselves require opening protectives; dampers/doors follow Chapter 7 when the wall is also a fire barrier, shaft, corridor, etc.

**SD takeaway:** Set lot-line fire separation distance with the construction type — a Type IIB wall at tight FSD is governed by Table 705.5, not by the 0-hour Table 601 cell.

### 3. Roof-rating reliefs (Table 601 Notes a–c)
| Note | Relief | Limits |
|------|--------|--------|
| a | Primary frame and interior bearing walls **−1 h** if supporting **roof only** | Types IA, IB; also IV-A/B/C primary frame |
| b | Roof construction may be **unprotected** if **all** parts are **> 6 m** above any floor below | Types IA, IB, IIA, IIIA, VA; **not** Groups F-1, H, M, S-1. A mezzanine that drops clearance below 6 m kills the relief for the whole member |
| c | Heavy timber may substitute for roof rating **≤ 1 h** | Types IB, IIA, IIB, IIIA, VA — **not** IA |

Columns must keep their rating for the full height (no cutoff at 6 m).

**SD takeaway:** High-volume roofs (> 6 m to the floor) can drop roof fireproofing in several types — but a mezzanine under part of the roof forfeits that for the entire member.

### 4. Type IV mass timber (602.4–602.4.2)
IV-A: mass timber fully covered with noncombustible protection (interior contribution **≥ 80 min**, and ≥ two-thirds of the required rating). Floors: **≥ 25 mm** noncombustible topping. IV-B: limited exposed timber — ceilings up to **20%** of floor area, walls up to **40%**, or a mixed formula; standalone columns/beams may be exposed. IV-C: more exposure; still protect concealed spaces, shafts, and exterior face. IV-HT: traditional heavy timber + limited 1-hour light-frame partitions.

High-rise mass timber: occupied floor **> 23 m** above FD access, up to **12 stories or 54 m** — interior exit and elevator hoistway enclosures may be protected mass timber; **above 12 stories or 54 m** those enclosures shall be **noncombustible** for the full building height.

Concealed spaces in IV-A/B/C: combustibles limited to MEP/fire protection permitted in plenums under **SBC 501** Section 602, plus Section 718.

**SD takeaway:** Exposed CLT is an IV-B/C choice with percentage caps; stair/elevator shafts in tall timber become noncombustible above 12 stories or 54 m — plan that core material at SD.

### 5. Combustibles in Types I and II (603)
FRTW is allowed in limited locations (e.g. unprotected roofs per Note b; nonbearing exterior walls where no rating is required). FRTW is not itself a fire-resistance rating. Other combustibles only as listed in 603.1.

**SD takeaway:** Do not assume wood blocking, roof decks, or partitions are free in Type I/II — they need a 603.1 line item or they force a type change.

### Source
`Chapter_06 — TYPES OF CONSTRUCTION.txt`. Companions named in this chapter: Table **705.5** (Ch. 7); Section **510** (podium mixed types); Section **2304.11** / Ch. 23 (mass timber sizes); **SBC 501** (plenums in IV concealed spaces); NFPA 285 (IV-A exterior wall covering commentary).
