---
name: sa-critical-summary
description: >-
  Use when the user invokes this skill, asks for a Critical Summary, CS.md,
  or schematic-design constraints extracted from a named Saudi source: SBC
  volume or chapter, ICC A117.1 or other referenced standard, SCD circular,
  Baladiya/MoMRAH circular, Mostadam manual, or giga-project design guideline.
disable-model-invocation: true
---

# SA Critical Summary

Write a highly practical, scannable Architect Critical Summary from a **provided** KSA source. Role: senior code consultant highlighting the absolute critical items an architect needs before schematic design. Skip legal preamble, boilerplate, and administrative filler. Get straight to the design constraints. Do not invent clauses. Do not use the master-skill chat persona (no greeting, no first-person director voice). Keep SI units as published.

## Workflow

1. **Halt if no source.** Do not summarize from memory or an SBC / circular name alone. Ask for the PDF, extract, topic folder, or `@`-attached path.
2. **Choose mode from the attachment, not the code title.**
   - **Volume mode (default):** user `@`s a topic folder, several chapters, or the code as a whole → one CS for the volume. Read architect-relevant chapters only (occupancy, height/area, construction type, fire/smoke, egress, accessibility, interior environment, energy, elevators, special occupancy). Skip admin filler and materials chapters (masonry, aluminum, gypsum, etc.) unless they lock architecture.
   - **Chapter mode:** user `@`s a single chapter file, or asks to summarize one chapter → one CS for that chapter. Read that file fully.
3. **Cite only what is in the provided source.** If a chapter cites a companion edition (e.g. ICC A117.1 year), report that year. Do not “correct” it from memory.
4. **Derive the CS filename** (rules below). Never put "Architect Critical Summary" in the filename.
5. **Write the CS file** in the topic parent folder (`Reference/{Title}/`) — **not** inside `source_reference/`.
6. **Source files stay in `source_reference/`.** If extracts are already there, leave them. If a new PDF arrives, place it there with its existing filename. Prefer English CC/CR extracts; do not invent from an Arabic AR edition.

---

## File naming and folder layout (mandatory)

### Mode → filename

- Volume SBC: `SBC 201 (2024)_CS.md`
- Chapter SBC: `SBC 201 Chapter 10 Means of Egress (2024)_CS.md`
- ICC volume: `ICC A117.1 (2017)_CS.md`
- ICC chapter: `ICC A117.1 Chapter 04 Accessible Routes (2017)_CS.md`
- SCD / municipality circular: keep circular number + short title + year if present, then `_CS.md`

**Do NOT** use "Architect Critical Summary" in the filename.

**Examples:**
| Source | Mode | Critical Summary filename |
|--------|------|---------------------------|
| `Reference/SBC 201 2024/` (folder or several chapters) | volume | `SBC 201 (2024)_CS.md` |
| `Chapter_10 — MEANS OF EGRESS.txt` | chapter | `SBC 201 Chapter 10 Means of Egress (2024)_CS.md` |
| `Reference/2017 ICC A117_1 Accessible and Usable Buildings and Facilities/` | volume | `ICC A117.1 (2017)_CS.md` |
| SCD circular PDF with number, title, and year | volume (single instrument) | `{Circular No. + short title} (YYYY)_CS.md` |

**Derive the CS title from the source by:**
1. Using the document’s short title (SBC number, ICC designation, circular title).
2. Stripping boilerplate suffixes: `CC`, `CR`, `AR`, `Code & Commentaries`, `Code Requirements`, language tags.
3. Keeping one parenthetical edition year if present in the source.
4. In chapter mode, inserting `Chapter {N} {Short name}` after the code designation.
5. Appending `_CS.md`.

### Folder layout

```text
Reference/SBC 201 2024/
 ├── SBC 201 (2024)_CS.md
 ├── SBC 201 Chapter 10 Means of Egress (2024)_CS.md   # chapter mode only
 └── source_reference/
      ├── 00_front_matter.txt
      └── Chapter_*.txt
```

Never rename files already in `source_reference/`.

---

## Markdown structure

Use this skeleton:

```markdown
# {Short title}
**Architect critical summary for schematic design**
{edition / year} | {issuing authority}

> Scope note: {what this instrument is / is not — including which companion SBC/AHJ governs the rest}

## Regulatory Overview
{exactly 2 sentences: occupancy / construction class / when another SBC part or AHJ takes over}

## Critical main topics and subtopics

### 1. {topic} ({section refs})
{tables of hard rules}
**SD takeaway:** {one schematic design lock}

### Source
{source filename(s) + companions}
```

### Heading and body rules

- **Title (`#`)**: short document title (same short title as the filename, without `_CS`).
- **Subtitle line**: always `**Architect critical summary for schematic design**` (in the body, never in the filename).
- **Metadata line**: edition year, then issuing authority (SBCNC, SCD, MoMRAH / Baladiya, ICC, or special AHJ such as NEOM / RSG / DGDA when that is the source).
- **Scope note**: one blockquote stating what the instrument governs and what it is **not**, plus which companion SBC/AHJ governs the rest.
- **`## Regulatory Overview`**: exactly 2 sentences.
- **`## Critical main topics and subtopics`**: numbered `###` topics with section refs. Prefer tables of hard rules. End each topic with `**SD takeaway:**` (one design lock for schematic design).
- **`### Source`**: original source filename(s) plus companions. Typical maps (only if the provided source points there): fire → SBC 501 + SCD; accessibility scoping → SBC 1001 + ICC A117.1; energy → SBC 601 + Mostadam; dwellings exception → SBC 1101/1102. Do not dump the full code.

Scale depth to the source: a short circular may be a few tables; a full SBC volume needs numbered topics for architect-relevant chapters only. Every topic still gets an SD takeaway.

---

## Common mistakes

| Mistake | Do this instead |
|---------|-----------------|
| CS saved inside `source_reference/` | Save `_CS.md` as a sibling of `source_reference/`, in the topic parent folder |
| Filename contains "Architect Critical Summary" | `{Short title} (year)_CS.md` only |
| Source files renamed to match the CS | Keep existing extract/PDF filenames |
| Summarizing without a provided file | Halt and ask for the source |
| Legal preamble, commencement history, or admin filler | Design constraints, numbers, and section refs only |
| Topic with no SD takeaway | One `**SD takeaway:**` per `###` topic |
| Invented clauses or remembered code text | Read the provided file; cite only what is in it |
| Regulatory Overview longer than 2 sentences | Two sentences, then move on to topics |
| Treating a full SBC volume as one unread PDF | Volume mode: read architect-relevant chapters; skip materials/admin unless they lock design |
| Chapter CS when the user attached the folder (or volume CS when they attached one chapter) | Mode follows the attachment |
| HK Caps, PNAPs, or FSD circulars | SBC / SCD / Baladiya / Mostadam / ICC / giga-project sources |
| Converting SI to imperial | Keep SI as published |
| “Correcting” an ICC edition year the source cites | Report the year in the provided file |
| Omitting companion SBC/AHJ in `### Source` | Name the companions the source points to |
