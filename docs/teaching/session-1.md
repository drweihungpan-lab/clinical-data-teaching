# Session 1 — Clinical trials and the industry

**Duration:** 120 minutes, including a ten-minute break. **Outcome:** explain how a development question becomes a study and recognize the teams needed to deliver it.

| Minutes | Content |
| --- | --- |
| 0–5 | Welcome and survey themes |
| 5–30 | Clinical-trial foundations |
| 30–50 | Phases and development decisions |
| 50–60 | Break |
| 60–80 | Industry ecosystem |
| 80–105 | Public SLN360 case discussion |
| 105–120 | Recap, two checks, and topic choices |

## Slide 1 — What changes outside the statistics classroom?

**Slide text**

- A scientifically interesting question must become a feasible clinical study.
- Patient observations arrive through people, sites, laboratories, and systems.
- Evidence must support a decision and survive scrutiny.

**Instructor notes**

Ask what students imagine a statistician does in a drug company. Explain your own route from statistics into clinical development and medical devices. Emphasize that industry context adds collaborators, practical constraints, and accountability to their existing statistical knowledge. Use an experience you can share publicly, not a confidential study detail.

## Slide 2 — The protocol is a shared plan

**Slide text**

- Who can enter the study, and why?
- What intervention and comparison will be used?
- What will be measured, when, and how?
- What safety and analysis decisions are planned?

**Instructor notes**

Define a clinical trial as a planned investigation involving people to address an intervention question. Contrast it with observing routine care without assigning an intervention. A protocol connects objectives, population, treatment, visits, and measurements. A statistical analysis plan makes the analysis approach more explicit. A beautifully fitted model cannot recover an outcome never collected. [FDA clinical-research overview](https://www.fda.gov/patients/drug-development-process/step-3-clinical-research)

## Slide 3 — Endpoints connect medicine to statistics

**Slide text**

- An endpoint defines what result matters and when it is assessed.
- A laboratory biomarker and a clinical event answer different questions.
- An analysis needs a population, comparison, and handling of incomplete observations.

**Instructor notes**

Use Lp(a) as the cardiovascular biomarker and cardiovascular events as a different outcome. Do not introduce derivation formulas. Ask: “If the biomarker improves, what else would you want to know?” Connect to duration of benefit, adverse effects, and the relationship between marker and patient outcomes. These are design and interpretation questions, not just significance tests.

## Slide 4 — Randomization, blinding, and safety

**Slide text**

- Randomization supports a fair treatment comparison.
- Blinding reduces the influence of knowing the assignment.
- Safety monitoring can affect whether and how a study continues.

**Instructor notes**

Randomization balances groups in expectation; it does not guarantee exact balance in a small sample. Blinding and allocation concealment address different sources of bias. Avoid claiming that every trial can be fully blinded. Safety is not established by a nonsignificant difference in a small adverse-event table. Explain how medical and statistical judgment meet when deciding whether to increase a dose or continue recruitment.

## Slide 5 — Phases are different evidence questions

**Slide text**

| Phase | Main question | Statistical/data emphasis |
| --- | --- | --- |
| I | Can early human exposure be studied safely, and what doses merit further work? | Close safety observation, dose/cohort context, descriptive signals |
| II | Is there enough evidence of activity and a suitable regimen to continue? | Endpoint/dose choices, uncertainty, feasibility |
| III | Is the benefit–risk evidence adequate for the proposed use? | Prespecified comparisons, larger evidence base, generalizability |
| IV | What is learned after authorization in practice? | Longer-term safety/effectiveness and broader use |

**Instructor notes**

Sample sizes grow in many programs but are not a rule defining the phases. As broad illustrations, FDA describes tens in early studies, hundreds in phase II, and hundreds to thousands in phase III. Disease, design, and purpose can change these patterns. Phase I is not always conducted in healthy volunteers. Do not transfer this phase structure mechanically to devices. [FDA definitions](https://www.fda.gov/drugs/investigational-new-drug-application-ind/drug-development-and-review-definitions)

## Slide 6 — Development is a sequence of decisions

**Slide text**

- Continue: evidence supports the next question.
- Change: revise dose, population, measurements, or approach.
- Stop: the evidence or feasibility no longer supports the program.

**Instructor notes**

Distinguish evidence from decision criteria. A small study may justify further investment without establishing approval-level evidence. Scientific, safety, operational, and business considerations can all affect development decisions; do not infer an undisclosed cause from a headline. Ask students to name what a phase I trial cannot answer reliably.

## Slide 7 — Who works in this ecosystem?

**Slide text**

| Organization | Contribution | Connection to data |
| --- | --- | --- |
| Pharma | Develops and maintains a broader product portfolio | Multiple programs, evidence packages, post-market data |
| Biotech | Often develops focused scientific programs | Concentrated assets, partnerships, resource trade-offs |
| CRO | Provides contracted study services | Operations, data management, programming, analysis |
| CMO/CDMO | Manufactures and/or develops manufacturing processes | Batch quality, product consistency, CMC evidence |

**Instructor notes**

This is an orientation model, not a definition based on company size or tool stack. Biopharmaceutical describes a scientific/product area rather than a mutually exclusive corporate type. A biologic program still needs clinical and manufacturing evidence. Explain CMC as chemistry, manufacturing, and controls in one sentence. A sponsor can transfer activities to service providers while retaining appropriate oversight. [ICH roles and oversight](https://admin.ich.org/sites/default/files/inline-files/ICH_E6%28R3%29_Step%204_Presentation_2025_0123.pdf)

## Slide 8 — Sites turn plans into observations

**Slide text**

- Investigator/site: patient care and study assessments.
- CRA: monitoring and site follow-up.
- Clinical operations: coordinating sites and vendors.
- Laboratories and systems: measurements and records.

**Instructor notes**

Keep this high-level. Follow one blood sample: scheduled visit → collection → lab → result → clinical database. A missing result could reflect a missed visit, a lost specimen, a processing issue, or a transfer issue. The reason matters, but a statistician should not invent it. Session 2 shows the relevant handoffs.

**Brief regulatory context within this block**

GCP connects ethical study conduct, participant protection, reliable results, and clear sponsor/site responsibilities. It matters to how data are collected, checked, and reported, not only to an inspection. [FDA E6(R3) overview](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/e6r3-good-clinical-practice-gcp)

FDA evaluates the submitted US drug-development evidence and makes approval decisions. For the EU centralized medicine route, EMA performs scientific assessment and recommends a decision; the European Commission grants authorization. EU clinical-trial authorization is a national-authority responsibility, not an EMA approval. RA helps teams navigate these interfaces. Keep this to two minutes rather than teaching submission procedures. [FDA review](https://www.fda.gov/drugs/information-consumers-and-patients-drugs/fdas-drug-review-process-ensuring-drugs-are-safe-and-effective), [EMA authorization overview](https://www.ema.europa.eu/en/about-us/what-we-do/authorisation-medicines)

## Slide 9 — SLN360: read the study, not only the headline

**Slide text**

- Use the [published case card](case-study.md).
- Identify the study question and actual design.
- Separate safety findings, biomarker response, and clinical benefit.

**Instructor notes**

Open the study and guide students through the card. Ask them to locate the primary outcome, treatment groups, and measurements. Briefly point to Table 1, Table 2, and Figure 2: participants, adverse events, and biomarker trajectories. Make the number of groups visible so nobody carries over the invented two-arm demonstration into the real study. No detailed cohort modeling or journal-figure redistribution is needed.

## Slide 10 — What would the next team need?

**Slide text**

- A result with its uncertainty and limitations.
- A reason to continue, revise, or stop.
- A clear account of what remains unknown.

**Instructor notes**

Ask students to imagine joining the development meeting. They should articulate the question a next study must answer, rather than simply say “the p-value is small.” Preview the four core data/statistical roles in session 2.

## Recap and student topics

Two oral checks: (1) Does biomarker improvement alone establish fewer cardiovascular events? (2) If a CRO performs study activities, does the sponsor's oversight disappear? Answers are in [the instructor key](answers.md).

Offer the three [session-1 presentation topics](presentations.md#after-session-1). Choose one speaker per topic before students leave.

## References for this session

Use [FDA phase definitions](https://www.fda.gov/drugs/investigational-new-drug-application-ind/drug-development-and-review-definitions), [FDA clinical-research overview](https://www.fda.gov/patients/drug-development-process/step-3-clinical-research), [ICH E6(R3) overview](https://admin.ich.org/sites/default/files/inline-files/ICH_E6%28R3%29_Step%204_Presentation_2025_0123.pdf), and the [SLN360 case reference](case-study.md). Sources checked for the 2026-10-11 implementation; the study findings are historical.
