---
name: sa-construction-documentation
description: >
  Expert guidance on KSA-specific construction documentation: ensuring SBC compliance, SCD (Civil Defence) approval readiness, IFC coordination for extreme climates, and fast-track delivery workflows aligned with Vision 2030 standards.
user-invocable: true
disable-model-invocation: true
---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Tender/IFC architectural packages | `sa-construction-documentation` | `sa-building-codes` |
| Early concept only | `sa-concept-design` | — |

## Halt conditions

- Stop and request data if **AHJ**, occupancy, or approval status is unknown (see `../../references/compliance.md`).
- Do not assert regulatory compliance without verified code edition and authority pathway.



# KSA Construction Documentation & Delivery Standards

## 1. Primary Objective
To produce a fully coordinated, **SBC-compliant** package that facilitates seamless **Building Permit** issuance via the SBPS portal and minimizes site-based Variations (VOs) caused by misalignment between MEP, Fire Safety, and Architectural envelopes.

## 2. Critical Coordination Pillars (KSA Context)
* **SBC 501 (Fire Protection) Integration:** Mandatory inclusion of SCD-approved fire life safety strategies. Documentation must show clear fire-rated partitioning, egress widths, and travel distances, cross-referenced with active system shop drawings.
* **Building Envelope & SBC 601:** Façade details must explicitly address thermal bridging, high-performance U-values, and **dust/sand ingress prevention** (essential for Riyadh/Eastern Province). Movement joints must account for the extreme thermal expansion ranges typical of the Central Region.
* **Vertical Transportation & MEP Risers:** Finalized shaft dimensions and plant room layouts to avoid late-stage structural penetrations, which are heavily scrutinized during **SBC 201 (Structural)** inspections.
* **Universal Access (SBC 1001):** Dedicated accessibility sheets showing ramp gradients, tactile paving, and clearance zones to satisfy both Saudi Building Code and **Quality of Life** program mandates.

## 3. Authority Submission & Document Control
* **Status Management:** Rigid adherence to status coding: **S1** (For Coordination), **S2** (For Information), **S3** (For Review/Approval), **S4** (For Stage Approval/Building Permit), and **IFC** (Issued for Construction).
* **Comment Response Matrix (CRM):** A live tracker linking comments from **Baladiya**, **SCD**, or **Third-Party Reviewers** (e.g., Momraha) directly to drawing revisions to ensure a closed-loop audit trail.
* **BIM/ISO 19650 Compliance:** Ensure all sheets are derived from the Federated Model to prevent "orphan" details that often fail site inspections by the Consultant or Authority.

## 4. Sustainability & Certification
* **Mostadam/LEED Tracking:** Documentation must include the "Sustainability Credit Evidence" set, ensuring that specified materials and systems align with the targeted **Mostadam** rating (Green/Diamond) as required by the project’s specific Giga-project authority.
