---
name: sa-icc-chapter-extract
description: >-
  Use when the user invokes this skill, asks for an ICC A117.1 chapter
  dimensional requirements matrix, unit-type-filtered numeric extract
  (Accessible / Type A / Type B), or data matrix from an attached ICC
  A117.1 chapter, and when an inspecting-model name is to appear in the
  output filename suffix.
disable-model-invocation: true
---

# SA ICC A117.1 Chapter Extract

Write a source-only dimensional requirements matrix from a **provided** ICC A117.1 chapter for a **stated unit type**. Role: senior code consultant. Cite only the attached chapter. Do not invent clauses. Do not use the master-skill chat persona (no greeting, no first-person director voice). Keep dual units as published. Do not copy numbers from a prior run, from SBC 201, or from a CS.md into a new chapter.

This is **technical geometry**. Scoping (what, where, how many) is **SBC 201 Chapter 11**. Do not write a Critical Summary; that is a different skill.

Document-shape example (project-use + coverage; not a hardcoded unit type; do not copy Appendix A):
`Project/ICC A117.1 Group R2 Reqt Extract/ICC A117.1 Chapter 04 Accessible Routes Type A Dimensional Requirements Matrix (2017)_Cursor-Grok-4.6.md`

Row-shape gold is the 403.5.1 before/after in this skill, not a pasted inventory.

## Required inputs

Halt and ask. Do not invent missing items.

| Input | Halt if missing | Notes |
|-------|-----------------|-------|
| Source | Yes | `@`-attached chapter extract or equivalent path. Never extract from an A117.1 chapter name alone. |
| Inspecting model | Yes | The model used for this run. Becomes the filename suffix. |
| Occupancy / typology | Yes | Folder + metadata only (e.g. Group R-2 high-rise). Does not filter rows. |
| Unit type | Yes | **Accessible**, **Type A**, or **Type B**. Filters the practical tier. Type C only if the user names it. |
| AHJ / city, new vs existing, mixed use, storeys | No | If unknown, treat as **new construction**; existing-building limits are Conditional. List gaps in the decision register. |

A chapter `*_CS.md` may be used only as a **coverage cross-check**. It is never the authority for values.

## Output path and filename

Create the occupancy folder if missing. Save **one** Markdown file **plus** a sibling Landscape A3 PDF:

```text
Project/ICC A117.1 Group {Occupancy} Reqt Extract/ICC A117.1 Chapter {N} {Title} {UnitType} Dimensional Requirements Matrix ({year})_{Model}.md
Project/ICC A117.1 Group {Occupancy} Reqt Extract/ICC A117.1 Chapter {N} {Title} {UnitType} Dimensional Requirements Matrix ({year})_{Model}.pdf
```

Derive fields from the **source file**, not memory:

1. Code designation (`ICC A117.1`).
2. Chapter number and short title from the extract heading.
3. Unit type from the user (`Accessible`, `Type A`, `Type B`).
4. Occupancy token from the user for the folder (e.g. `R2`).
5. One parenthetical edition year if present in the source.
6. Model suffix: spaces → hyphens; keep dots and case (`GPT-5.6 Sol` → `_GPT-5.6-Sol.md`).

**Do not** write inside `source_reference/`. **Do not** leave temporary inventory `.json`, scratch reports, or print `.html` in the repo. Delete working inventories after the coverage block is written.

## Workflow

Copy this checklist and track it:

```
- [ ] Inputs complete (source, model, occupancy, unit type)
- [ ] Chapter read fully; code vs INSIGHTS/commentary/figures separated
- [ ] Numeric inventory complete (exceptions, tables, footnotes, list items, option sets)
- [ ] Project-use tier rewritten as design checks (not pasted inventory)
- [ ] Project-use self-check passed (dual units bold; new vs existing not mixed)
- [ ] Coverage summary + unresolved register written; inventory discarded
- [ ] Completeness audit passed
- [ ] Landscape A3 PDF written beside the MD
- [ ] Temp files deleted; filename/model suffix match
```

### 1. Halt if inputs missing

Ask for the exact missing item. Do not start extraction from a code title, a CS.md, or a remembered edition.

### 2. Read the attached chapter fully

Mandatory: numbered code paragraphs, exceptions, tables, table footnotes/notes, page-split continuations after exceptions.

Not mandatory: `INSIGHTS` heading tags, FIGURE captions-as-geometry, commentary, CS.md text, outbound SBC/ASME/BHMA values not quantified in this chapter.

### 3. Inventory every independently checkable numeric rule (internal only)

Include dimensions, clearances, widths, heights, distances, slopes, forces, areas, percentages, times, and new/existing option sets.

Inventory **every** numbered list item, exception item, table cell, and footnote that carries an independently checkable number.

**Internal inventory only:** one record per independently checkable rule. Split combined min/max/spacing rules **here**. Do not store list-item numbers (`1.`, `2.`) as values. Do **not** publish `CH04-0001`-style rows in the Markdown.

Do **not** paste this atomized inventory into project-use tables.

### 4. Write the Markdown file

**Project-use** (stated unit type):

- Metadata: occupancy, unit type, extracted edition, AHJ if known, inspecting model, source path, advisory limitation, **edition gap** (see ICC-only rules).
- Decision/gap register: A117.1 edition lock, unit type, new vs existing, AHJ/NOC.
- Focused matrices: one **design check** per row for topics that lock **this** unit type.
- Group related limits from the same clause (or consecutive subclauses checked as one drawing/detail) into a single row. Cite as `403.5.2–403.5.3` when grouped.
- Grouping predicate: if a designer would mark the same drawing/detail, one row; if they would check a different system, floor, or exception branch, split.
- **Option sets = one grouped check.** 90° turn options, 180° turn option sets, elevator Table 407.4.1 car options: one row; named alternatives in Exceptions / branch.
- Lead tables contain **Direct** and unit-type-relevant **Conditional** checks. **Not typical** rows stay out unless the gap register already opened that use (Type C, recreation, assembly). Unrelated unit-type rows are omitted — they are not parked in a published appendix.
- A cite appears in **one** project-use section. Do not repeat Table/section blocks across topics.

**Coverage (end of file — not a row inventory):**

```markdown
## {N}. Coverage summary
- Inventory scope: numbered code, exceptions, tables, footnotes (INSIGHTS, figures, commentary excluded)
- Total independently checkable numeric records
- Verified / Verify source counts
- Optional: counts by top-level section (one compact table, no row listing)

## {N+1}. Unresolved-source register
| Affected table / clause | Why unverified | Control note |
```

Each OCR/flattened-table hold point that appears in project-use as **Verify source** must appear in the register. No Appendix A. No per-section inventory tables.

### 5. OCR, units, figures, and outbound

- Damaged/flattened tables, concatenated `<table><td` blobs, or unreadable factors: **no value adopted** + **Verify source**. Canonical failure: reconstructing Table 404.2.3.2 manoeuvre cells from a flattened blob or from CS.md.
- Dual units as published: `36 inches (915 mm)` — keep **both**; **bold** both numbers. Do not SI-only the cell. Do not invent a conversion.
- Normalize OCR `\frac{1}{2}` to `1/2 inch (13 mm)` without changing the value.
- Keep published slope tokens intact (`1:20`, `1:12`, `1:48`).
- FIGURE captions (`FIGURE 403.5.1(A) CLEAR WIDTH…`) are dependencies, not values. If a dimension exists only in a missing figure: External verification + register.
- `INSIGHTS` in a heading is not code. Inventory the numbered paragraph and exceptions only.
- Where this chapter points elsewhere (A117.1 Ch 3, 5, 7; ASME A17.1; BHMA; SBC 201 Ch 10/11): record the dependency; **do not import unstated values**. Inverse outbound: do not import SBC 201 Chapter 11 counts (60% entrances, Type A quotas, parking %).

### 6. Audit before finish

- Every numeric code clause and appended table was inventoried internally; coverage counts and the unresolved register match that inventory.
- No commentary, CS.md, or INSIGHTS numbers in project-use requirement / value cells.
- Unit-type scopes are correct (do not apply Accessible/Type A manoeuvring to Type B interiors).
- New-building and existing-building limits are not mixed on the same Direct row.
- Filename, occupancy folder, unit type, and model suffix match the inputs.
- Markdown tables render (pipes escaped; consistent column counts).
- No temp inventory files remain.
- Project-use self-check (below) passed.
- No published Appendix A / `CHnn-0001` inventory.
- Edition gap row is present in the decision register.

### 7. Print Landscape A3 PDF

After the Markdown is finalized (coverage block included; no appendix), print a sibling PDF:

```text
python .cursor/skills/sa-sbc-chapter-extract/print_a3.py "{path-to-final.md}"
```

- ISO **A3 landscape** (420 × 297 mm). Reuse the SBC helper: markdown2 HTML, Playwright + installed Chrome (`channel="chrome"`). No Markdown Preview / Viewer / Print Friendly.
- Do **not** copy `print_a3.py` or its CSS into this skill folder.
- Do **not** use gstack `make-pdf` (letter/A4/legal only; no A3). Do **not** use Edge `--print-to-pdf` CLI.
- Do **not** print a file that still contains Appendix A.
- Delete any temp `.html` the helper leaves behind. Confirm the `.pdf` exists beside the `.md`.

## ICC-only rules

### Edition gap (mandatory metadata, not a value source)

Attached extracts are typically **2017**. SBC 201 Chapter 35 lists **ICC A117.1—09**. Charging 1102.1 has no year.

Every extract must:

- State the extracted edition from the source heading.
- Put a gap-register row: AHJ must lock 2009 vs 2017; 2017 new-building CFS, turning, and door manoeuvre are larger; **do not treat 2017 as the legal SBC minimum**.
- **Do not** back-fill 2009 millimetres from memory or from SBC commentary.

### Unit-type filter

- **Common / public accessible routes, doors, ramps, lifts (Ch 3–10):** Direct for Accessible, Type A, and Type B unless the clause is explicitly a dwelling-unit interior rule.
- **Dwelling interiors:** follow A117.1 Chapter 11 technical sets. Accessible = 1102 (full 404 + 304 turning). Type A = 1103 (full 404; adaptable baths/kitchens). Type B = 1104 (reduced doors **31 3/4 inches (805 mm)**, existing-style 180°/90°/passing, grab-bar **blocking** not grab bars in place). Do not draw Type B interiors with Accessible/Type A manoeuvring.
- **Type C (1105):** omit unless requested.
- **Communication features (1106):** Conditional overlay, not a substitute for mobility type.

### New vs existing

2017 constantly splits (403.5, 304.3, 305.3, 404.2.3 footnotes). For new construction: new-building option set is Direct; existing-building dimensions are Conditional. Never mix **67 inches (1700 mm)** new turning with **60 inches (1525 mm)** existing on the same Direct row.

## Project-use row contract

Each project-use cell **is** the following. Match this shape, not a pasted inventory record.

| Column | The cell IS |
|--------|-------------|
| **Cite** | Section or table. Range OK when grouped (`403.5.2–403.5.3`). |
| **Component / check** | 2–8 word noun phrase a designer would search (`Interior accessible-route clear width`). Not a truncated sentence. Not a list marker. |
| **Exact source requirement / value** | One synthesized rule. **Bold** every published inch **and** millimetre number in place. No `(SI: …)` trailer. No first-line clause dump. Dual units as published. |
| **Trigger / condition** | Building-language condition (`Interior accessible routes`). Never `Per Section {n}.` |
| **Exceptions / branch** | Named exception, new/existing branch, option set, or `None stated`. Never `See clause text.` Never copy the requirement cell. |
| **{UnitType} status** | Direct / Conditional / Not typical / External verification per the legend. |
| **Design action** | One check-specific instruction for drawings or schedules. |
| **Source confidence** | Verified or Verify source. |

Required shape (same cite):

```markdown
| 403.5.1 | Interior accessible-route clear width | Interior accessible route clear width **36 inches (915 mm)** minimum | Interior accessible routes | New pinch: **32 inches (815 mm)** for **24 inches (610 mm)** max, separated by **52 × 36 inches (1320 × 915 mm)**; existing pinch uses **48 inches (1220 mm)** separators; exterior seating **36 inches (915 mm)**; exterior ramp → 405.5 | Direct | Hold interior corridor clear width at 915 mm; document any local pinch | Verified |
```

Reject this shape:

```markdown
| 403.5.1 | The clear width of an interior accessible route shall be | The clear width of an interior accessible route shall be 36 inches (915 mm) minimum. **(SI: 915 mm)** | Per Section 403.5.1. | See clause text. | Direct | Coordinate the stated dimension/capacity on accessibility drawings. | Verified |
```

Banned Design action strings (rewrite the row):

- `Coordinate the stated dimension/capacity on life-safety drawings.`
- `Coordinate the stated dimension/capacity on accessibility drawings.`
- `Apply only if the stated feature, load, sprinkler branch or exception exists.`

### Self-check before writing Sections 4–N

Rewrite any row before continuing if:

- Component / check reads like a sentence start (`The clear width…`, `Where an…`, `Accessible routes shall…`)
- Value cell contains `(SI:` or drops the published inch token
- Trigger is `Per Section` (alone or as the whole cell)
- Exceptions is `See clause text.` or a paste of the requirement cell
- Design action matches a banned canned phrase
- New-building and existing-building limits are merged as if they were one Direct value

## Applicability and confidence

| Unit-type status | Meaning |
|------------------|---------|
| **Direct** | Expected to govern the stated unit type (and common/public routes) once geometry is confirmed. |
| **Conditional** | Governs only if the stated feature, existing-building branch, or exception exists on this project. |
| **Not typical** | Unrelated unit-type-only rule; omit unless the gap register already opened that use. |
| **External verification** | This chapter sends the user elsewhere, a figure is missing, or OCR/AHJ must be confirmed first. |

| Confidence | Meaning |
|------------|---------|
| **Verified** | Unambiguous mandatory source text/table cell. |
| **Verify source** | OCR, flattened table, page-split, or footnote attachment is unresolved. Not a design-release value. |

## Document skeleton

```markdown
# ICC A117.1 Chapter {N} {Title} — {UnitType} Dimensional Requirements Matrix ({year})

## 1. Document metadata and use limitation
- Project basis, unit type, extracted edition, source path, inspecting model
- Advisory (not stamped / SCD NOC / SBPS); technical standard only; scoping is SBC 201 Chapter 11
- Edition gap: SBC 201 Chapter 35 lists ICC A117.1—09; do not treat this extract as the legal SBC minimum

## 2. Legends
Applicability + source confidence tables

## 3. Project decision and gap register
Edition lock, unit type, new vs existing, AHJ

## 4–N. Focused project-use matrices
One table per design topic that locks the stated unit type

## N+1. Project-use controls
How to use Verified vs Verify source rows

## N+2. Coverage summary
Counts only — no inventory rows

## N+3. Unresolved-source register
OCR / flattened-table / figure hold points
```

Project-use row:

```markdown
| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | {UnitType} status | Design action | Source confidence |
```

## Hard rules

- Advisory only — not stamped compliance, SCD NOC, SBPS approval, or permission to construct.
- Do not drop inches when the source publishes inch-pound and SI.
- Do not treat CS.md, INSIGHTS, FIGURE titles, or outbound SBC/ASME/BHMA parts as source values.
- Do not hardcode Type A, Group R-2, or Chapter 4 numbers into a different extract.
- Do not treat the 2017 extract as automatically the legal SBC minimum.

## Common mistakes

| Mistake | Do this instead |
|---------|-----------------|
| Extract from an A117.1 chapter name with no file | Halt and ask for the extract |
| CS.md or commentary used as the value source | Read the chapter code/tables only |
| Reconstruct Table 404.2.3.2 from a flattened `<table>` blob or from CS.md | Verify source; leave manoeuvre cells empty; footnotes after the blob may still be Verified |
| Treat 2017 millimetres as the SBC legal minimum | Extract the attached edition; gap-register the 2009 vs 2017 lock; do not back-fill 2009 from memory |
| Draw Type B interiors with full 404 / 304 | Type B interiors follow 1104; common/public routes still use this chapter |
| SI-only cell (`915 mm`) dropping `36 inches` | Keep the published pair; bold both numbers |
| Invent geometry from `FIGURE 403.5.1(A)…` | Record the figure as a dependency; External verification if the number is only in the figure |
| Treat `INSIGHTS` heading text as a requirement | Inventory the numbered paragraph and exceptions only |
| Mix new 67 in (1700 mm) turning with existing 60 in (1525 mm) on one Direct row | New = Direct; existing = Conditional unless the user stated alteration |
| Import SBC 201 Ch 11 counts (60% doors, Type A quotas, parking %) | Name the scoping companion; do not import numbers |
| Import ASME/BHMA values this chapter only names | Name the companion; do not import unstated values |
| Repair OCR from memory | Verify source; leave value empty |
| List marker `1.` stored as a numeric value | Extract only the requirement’s quantities |
| Option-set items pasted as four inventory rows | One grouped design check; alternatives in Exceptions / branch |
| Matrix saved in `source_reference/` | Save under `Project/ICC A117.1 Group {Occupancy} Reqt Extract/` |
| Model omitted from filename | `{…}_{Model}.md` with the inspecting-model suffix |
| Temp `.json` inventory left in the repo | Delete after the coverage block is written |
| Claimed completeness with unread tables | Coverage counts + unresolved register match the internal inventory |
| Published Appendix A / `CHnn-0001` rows | Coverage summary + unresolved register only |
| Truncated clause as Component/check | 2–8 word noun phrase |
| Verbatim clause + `(SI: 915 mm)` trailer | Synthesized rule with **bold** inch and mm in place |
| Trigger cell is `Per Section 403.5.1.` | Building-language condition |
| Exceptions is `See clause text.` or a copy of the requirement | Named exception, new/existing branch, option set, or `None stated` |
| Canned Design action on every row | Check-specific drawing/schedule instruction |
| Inventory rows pasted into Sections 4–N | Rewrite as grouped design checks; atomize only in the internal inventory |
| Same table block repeated in two project-use sections | One cite, one section |
| Slope token `1:20` stored as `20` or `5%` | Keep the published token intact |
| Portrait A4/letter PDF, gstack make-pdf, copied print script, or Edge `--print-to-pdf` | Existing `sa-sbc-chapter-extract/print_a3.py` — Landscape A3 |
