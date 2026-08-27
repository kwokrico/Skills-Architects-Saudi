---
name: sa-sbc-chapter-extract
description: >-
  Use when the user invokes this skill, asks for an SBC chapter dimensional
  requirements matrix, occupancy-filtered numeric extract, or data matrix from
  an attached SBC chapter, and when an inspecting-model name is to appear in
  the output filename suffix.
disable-model-invocation: true
---

# SA SBC Chapter Extract

Write a source-only dimensional requirements matrix from a **provided** SBC chapter for a **stated occupancy/typology**. Role: senior code consultant. Cite only the attached chapter. Do not invent clauses. Do not use the master-skill chat persona (no greeting, no first-person director voice). Keep SI units as published. Do not copy occupancy numbers from a prior run into a new chapter.

Document-shape example (project-use + coverage; not a hardcoded occupancy; do not copy Appendix A from older GPT/pre-skill files):
`Project/SBC Group R2 Reqt Extract/SBC 201 Chapter 10 Means of Egress Group R-2 High-Rise Dimensional Requirements Matrix (2024)_Cursor-Grok-4.6.md`

Row-shape gold is the 1003.2 before/after in this skill, not a pasted inventory.

## Required inputs

Halt and ask. Do not invent missing items.

| Input | Halt if missing | Notes |
|-------|-----------------|-------|
| Source | Yes | `@`-attached chapter extract or equivalent path. Never extract from an SBC number/chapter name alone. |
| Inspecting model | Yes | The model used for this run. Becomes the filename suffix. |
| Occupancy / typology | Yes | Filters the practical tier (e.g. Group R-2 high-rise). |
| AHJ / city, sprinkler, mixed use, storeys | No | If unknown, keep the matrix source-only and list gaps in the decision register. |

A chapter `*_CS.md` may be used only as a **coverage cross-check**. It is never the authority for values.

## Output path and filename

Create the occupancy folder if missing. Save **one** Markdown file **plus** a sibling Landscape A3 PDF:

```text
Project/SBC Group {Occupancy} Reqt Extract/{Code} Chapter {N} {Title} {Occupancy} {Typology} Dimensional Requirements Matrix ({year})_{Model}.md
Project/SBC Group {Occupancy} Reqt Extract/{Code} Chapter {N} {Title} {Occupancy} {Typology} Dimensional Requirements Matrix ({year})_{Model}.pdf
```

Derive fields from the **source file**, not memory:

1. Code designation (e.g. `SBC 201`).
2. Chapter number and short title from the extract heading.
3. Occupancy/typology from the user (e.g. `Group R-2 High-Rise`).
4. One parenthetical edition year if present in the source.
5. Model suffix: spaces → hyphens; keep dots and case (`GPT-5.6 Sol` → `_GPT-5.6-Sol.md`).

**Do not** write inside `source_reference/`. **Do not** leave temporary inventory `.json`, scratch reports, or print `.html` in the repo. Delete working inventories after the coverage block is written.

## Workflow

Copy this checklist and track it:

```
- [ ] Inputs complete (source, model, occupancy/typology)
- [ ] Chapter read fully; code vs commentary separated
- [ ] Numeric inventory complete (exceptions, tables, footnotes, list items)
- [ ] Project-use tier rewritten as design checks (not pasted inventory)
- [ ] Project-use self-check passed
- [ ] Coverage summary + unresolved register written; inventory discarded
- [ ] Completeness audit passed
- [ ] Landscape A3 PDF written beside the MD
- [ ] Temp files deleted; filename/model suffix match
```

### 1. Halt if inputs missing

Ask for the exact missing item. Do not start extraction from a code title, a CS.md, or a remembered edition.

### 2. Read the attached chapter fully

Mandatory: numbered code paragraphs, exceptions, tables, table footnotes/notes, page-split continuations after exceptions.

Not mandatory: commentary, figures-as-examples, commentary calculations, CS.md text, outbound SBC parts named but not quantified in this chapter.

### 3. Inventory every independently checkable numeric rule (internal only)

Include dimensions, clearances, widths, heights, distances, slopes, areas, capacity factors, occupant thresholds/counts, exit quantities, percentages, forces, illumination, durations, fire-resistance periods, and permitted story limits.

Inventory **every** numbered list item, exception item, table cell, and footnote that carries an independently checkable number.

**Internal inventory only:** one record per independently checkable rule. Split combined min/max/spacing rules **here**. Do not store list-item numbers (`1.`, `2.`) as values. Do **not** publish `CH10-0001`-style rows in the Markdown.

Do **not** paste this atomized inventory into project-use tables.

### 4. Write the Markdown file

**Project-use** (stated occupancy/typology):

- Metadata: occupancy, typology, AHJ if known, inspecting model, source path, advisory limitation.
- Decision/gap register for unconfirmed sprinkler, EVACS, storeys, mixed use, NOC/fire strategy.
- Focused matrices: one **design check** per row for topics that lock **this** occupancy.
- Group related limits from the same clause (or consecutive subclauses checked as one drawing/detail) into a single row. Cite as `1003.3.2–1003.3.3` when grouped.
- Grouping predicate: if a designer would mark the same drawing/detail, one row; if they would check a different system, floor, or exception branch, split.
- Lead tables contain **Direct** and occupancy-relevant **Conditional** checks. **Not typical** rows stay out of the deliverable unless the gap register already flags that feature (amenity assembly, podium mix). Unrelated occupancy table rows (dormitories, bowling, exhibit galleries) are omitted — they are not parked in a published appendix.
- A cite appears in **one** project-use section. Do not repeat Table/section blocks across topics.

**Coverage (end of file — not a row inventory):**

```markdown
## {N}. Coverage summary
- Inventory scope: numbered code, exceptions, tables, footnotes (commentary excluded)
- Total independently checkable numeric records
- Verified / Verify source counts
- Optional: counts by top-level section (one compact table, no row listing)

## {N+1}. Unresolved-source register
| Affected table / clause | Why unverified | Control note |
```

Each OCR/flattened-table hold point that appears in project-use as **Verify source** must appear in the register. No Appendix A. No per-section inventory tables.

### 5. OCR and outbound rules

- Damaged/flattened tables, degree symbols in place of units, concatenated cells, or unreadable factors: **no value adopted** + **Verify source**. Canonical failure: treating Table 1017.2 `60° / 75°` as metres from memory.
- Show sprinkler/mixed-use **branches** instead of assuming NFPA 13, 13R, or a podium program.
- Distinguish unit-level checks from story-level checks when the chapter does.
- Where the chapter points to another section/code (Chapter 9, 11, 403, SBC 501, ICC A117.1, SCD): record the dependency; **do not import unstated values**.
- Keep published slope/percent tokens intact (`8.3-percent` stays `8.3-percent`; do not drop leading digits).

### 6. Audit before finish

- Every numeric code clause and appended table was inventoried internally; coverage counts and the unresolved register match that inventory.
- No commentary numbers in project-use requirement / value cells.
- Occupancy scopes are correct (do not apply another group’s trigger to the stated occupancy).
- Filename, occupancy folder, and model suffix match the inputs.
- Markdown tables render (pipes escaped; consistent column counts).
- No temp inventory files remain.
- Project-use self-check (below) passed.
- No published Appendix A / `CHnn-0001` inventory.

### 7. Print Landscape A3 PDF

After the Markdown is finalized (coverage block included; no appendix), print a sibling PDF:

```text
python .cursor/skills/sa-sbc-chapter-extract/print_a3.py "{path-to-final.md}"
```

- ISO **A3 landscape** (420 × 297 mm). `print_a3.py` converts MD with markdown2, opens HTML in installed Chrome (`channel="chrome"`), and Playwright issues Chrome’s print-to-PDF. Paragraph style: Segoe UI 9pt body, navy `#1f4e79` headings with h2 rule, navy table headers / zebra rows, running header + advisory footer. No Markdown Preview / Viewer / Print Friendly.
- Do **not** use gstack `make-pdf` (letter/A4/legal only; no A3). Do **not** use Edge `--print-to-pdf` CLI.
- Do **not** print a file that still contains Appendix A.
- Delete any temp `.html` the helper leaves behind. Confirm the `.pdf` exists beside the `.md`.

## Project-use row contract

Each project-use cell **is** the following. Match this shape, not a pasted inventory record.

| Column | The cell IS |
|--------|-------------|
| **Cite** | Section or table. Range OK when grouped (`1003.3.2–1003.3.3`). |
| **Component / check** | 2–8 word noun phrase a designer would search (`General egress ceiling height`). Not a truncated sentence. Not a list marker. |
| **Exact source requirement / value** | One synthesized rule. **Bold** every published SI number/limit in place. No `(SI: …)` trailer. No first-line clause dump. Units as published. |
| **Trigger / condition** | Building-language condition (`All egress components`, `R-2 room/space with one exit access doorway`). Never `Per Section {n}.` |
| **Exceptions / branch** | Named exception, occupancy/sprinkler branch, or `None stated`. Never `See clause text.` Never copy the requirement cell. |
| **{Occupancy} status** | Direct / Conditional / Not typical / External verification per the legend. |
| **Design action** | One check-specific instruction for drawings or schedules. |
| **Source confidence** | Verified or Verify source. |

Required shape (same cite):

```markdown
| 1003.2 | General egress ceiling height | Means of egress ceiling height **not less than 2300 mm** above finished floor | All egress components | Dwelling/sleeping-unit ceilings, stair headroom, door height, ramp headroom and other listed cases are separately controlled | Direct | Coordinate reflected ceilings, services and signage to preserve the applicable clear height | Verified |
```

Reject this shape:

```markdown
| 1003.2 | The means of egress shall have a ceiling | The means of egress shall have a ceiling height of not less than 2300 mm above the finished floor. **(SI: 2300 mm)** | Per Section 1003.2. | See clause text. | Direct | Coordinate the stated dimension/capacity on life-safety drawings. | Verified |
```

Banned Design action strings (rewrite the row):

- `Coordinate the stated dimension/capacity on life-safety drawings.`
- `Apply only if the stated feature, load, sprinkler branch or exception exists.`

### Self-check before writing Sections 4–N

Rewrite any row before continuing if:

- Component / check reads like a sentence start (`The means of…`, `Where a…`, `A stair with…`)
- Value cell contains `(SI:`
- Trigger is `Per Section` (alone or as the whole cell)
- Exceptions is `See clause text.` or a paste of the requirement cell
- Design action matches a banned canned phrase

## Applicability and confidence

| Occupancy status | Meaning |
|------------------|---------|
| **Direct** | Expected to govern the stated occupancy/typology once geometry is confirmed. |
| **Conditional** | Governs only if the stated feature, load, sprinkler branch, or exception exists on this project. |
| **Not typical** | Unrelated occupancy-only rule; omit from the deliverable unless the gap register already opened that use. |
| **External verification** | This chapter sends the user elsewhere, or OCR/AHJ must be confirmed first. |

| Confidence | Meaning |
|------------|---------|
| **Verified** | Unambiguous mandatory source text/table cell. |
| **Verify source** | OCR, flattened table, page-split, or footnote attachment is unresolved. Not a design-release value. |

## Document skeleton

```markdown
# {Code} Chapter {N} {Title} — {Occupancy} {Typology} Dimensional Requirements Matrix ({year})

## 1. Document metadata and use limitation
- Project basis, source path, inspecting model, advisory (not stamped / SCD NOC / SBPS)
- Assumptions and unknown branches (sprinkler, mixed use, storeys)

## 2. Legends
Applicability + source confidence tables

## 3. Project decision and gap register
Unknowns that change which table row applies

## 4–N. Focused project-use matrices
One table per design topic that locks the stated occupancy

## N+1. Project-use controls
How to use Verified vs Verify source rows

## N+2. Coverage summary
Counts only — no inventory rows

## N+3. Unresolved-source register
OCR / flattened-table hold points
```

Project-use row:

```markdown
| Cite | Component / check | Exact source requirement / value | Trigger / condition | Exceptions / branch | {Occupancy} status | Design action | Source confidence |
```

## Hard rules

- Advisory only — not stamped compliance, SCD NOC, SBPS approval, or permission to construct.
- Do not convert SI to imperial unless the source publishes both.
- Do not treat CS.md, commentary examples, or outbound SBC parts as source values.
- Do not hardcode Group R-2, high-rise, Riyadh, or Chapter 10 numbers into a different extract.

## Common mistakes

| Mistake | Do this instead |
|---------|-----------------|
| Extract from an SBC chapter name with no file | Halt and ask for the extract |
| CS.md or commentary used as the value source | Read the chapter code/tables only |
| Repair OCR (`60°` → 60 m) from memory | Verify source; leave value empty |
| Commentary example promoted to a requirement | Keep commentary out of the matrix |
| List marker `1.` stored as a numeric value | Extract only the requirement’s quantities |
| One occupancy’s trigger applied to another | Keep the chapter’s occupancy scope |
| Unit-level one-door rule used as story exit count | Separate unit vs story checks |
| Assumed NFPA 13 vs 13R | Show both branches until the project locks one |
| Outbound Chapter 9 / 403 / A117.1 values filled in | Name the dependency; do not import numbers |
| Matrix saved in `source_reference/` | Save under `Project/SBC Group {Occupancy} Reqt Extract/` |
| Model omitted from filename | `{…}_{Model}.md` with the inspecting-model suffix |
| Temp `.json` inventory left in the repo | Delete after the coverage block is written |
| Claimed completeness with unread tables | Coverage counts + unresolved register match the internal inventory |
| Published Appendix A / `CHnn-0001` rows | Coverage summary + unresolved register only |
| Truncated clause as Component/check (`The means of egress shall have a ceiling`) | 2–8 word noun phrase (`General egress ceiling height`) |
| Verbatim clause + `(SI: 2300 mm)` trailer | Synthesized rule with **bold** numbers in place |
| Trigger cell is `Per Section 1003.2.` | Building-language condition (`All egress components`) |
| Exceptions is `See clause text.` or a copy of the requirement | Named exception, branch, or `None stated` |
| Canned Design action on every row | Check-specific drawing/schedule instruction |
| Inventory rows pasted into Sections 4–N | Rewrite as grouped design checks; atomize only in the internal inventory |
| Unrelated occupancy dump in lead tables (dormitories, exhibit galleries) | Omit unless the gap register opened that use |
| Same table block repeated in two project-use sections | One cite, one section |
| Slope token `8.3-percent` stored as `3-percent` | Keep the published token intact |
| Portrait A4/letter PDF, gstack make-pdf, or Edge `--print-to-pdf` | `print_a3.py` — markdown2 HTML, Playwright + installed Chrome, Landscape A3 |
