---
name: sa-unauthorised-building-works
description: >
  Technical and regulatory workflow for managing unauthorized site changes and deviations from SBC-approved drawings. Focuses on risk mitigation, Saudi Civil Defence (SCD) alignment, and the 'as-built' regularization process within the SBPS portal.
user-invocable: true
disable-model-invocation: true
---

## When to Use This Skill

| Question type | This skill | Use instead |
|---------------|------------|-------------|
| Unauthorized works, rectification, enforcement risk | `sa-unauthorised-building-works` | `sa-building-codes` |
| Routine permitted minor works | `sa-minor-works` | — |

## Halt conditions

- Stop and request data if **AHJ**, occupancy, or approval status is unknown (see `../../references/compliance.md`).
- Do not assert regulatory compliance without verified code edition and authority pathway.



# KSA Site Deviations & Regularization Protocol (SBC Compliance)

## 1. Executive Summary
In the high-pressure environment of Saudi giga-projects and fast-track Riyadh/Jeddah developments, site-led changes frequently outpace official design revisions. Unmanaged deviations risk **SBC non-compliance**, rejection of **Civil Defence NOCs**, and the withholding of the **Certificate of Occupancy**. This protocol establishes a pathway to identify, risk-assess, and regularize deviations without derailing the handover programme.

## 2. Regulatory & Authority Context (SBC/SCD)
* **SBC 201/501 Integrity:** Any change affecting fire-rated assemblies, means of egress, or structural loads must be re-validated.
* **SBPS Portal Updates:** Major deviations may require a "Revision to Approved Plans" submission via the Saudi Building Permit System before final inspection.
* **Civil Defence (SCD):** Any modification to smoke management, sprinkler coverage, or travel distances is a "red line" item that can halt project handover.

## 3. High-Risk Deviation Categories (Priority Review)
* **Fire & Life Safety (SBC 501):** Unprotected MEP penetrations in rated shafts, modified door hardware on egress routes, or changes to stairwell pressurization logic.
* **Building Envelope:** Substitution of facade materials lacking **UL/Intertek/SASO** certification or modifications to thermal breaks (SBC 601).
* **Accessibility (SBC 1001):** Minor site level changes that invalidate ramp gradients or tactile paving layouts required for MoMRA/Baladiya compliance.

## 4. Regularization Workflow
1.  **Technical Impact Assessment:** Compare deviation against the Approved Construction Documents and relevant SBC clauses.
2.  **Liability Check:** Determine if the change requires a revised **Engineer’s Calculation/Statement** for the Supervision Consultant's records.
3.  **The "As-Built" Delta:** Categorize as:
    * *Type A (Minor):* Record in As-Builts only.
    * *Type B (Major):* Requires formal Design Change Notice (DCN) and potential Authority re-submission.
4.  **Evidence Collection:** High-resolution photos, Material Approval Requests (MARs), and shop drawing redlines.

## 5. Required Information for Review
To provide a professional recommendation, please provide:
* **The "Delta":** Marked-up plans comparing 'Approved' vs. 'As-Built' condition.
* **Compliance Status:** Does the change violate a specific **SBC 501** or **SBC 201** requirement?
* **Stakeholder Origin:** Was this a Contractor V.E. proposal or a Client-directed site instruction?
* **Inspection Timeline:** Date of the next scheduled Baladiya or SCD site walk-through.

