# Session 2 — Professional roles, clinical data, and AI

**Duration:** 120 minutes, including presentations and a ten-minute break. **Outcome:** explain the four core roles and how data and evidence move through development.

| Minutes | Content |
| --- | --- |
| 0–25 | Two take-home presentations and class discussion: why did these trials stop? |
| 25–45 | Core roles and shared workflow |
| 45–70 | Conceptual SDTM/analysis/TFL demonstration |
| 70–80 | Break |
| 80–110 | RWD feasibility and two AI cases |
| 110–120 | Recap, checks, and next topic choices |

**Opening presentations (0–25).** Pick two students to present the [session-1 take-home exercise](presentations.md#after-session-1-take-home-exercise--why-did-these-trials-stop), at most five slides and about eight minutes each. Use the remaining time for a short class discussion: did operations reasons outnumber science reasons, what share was unclear, and what denominator did each person use? Bridge to today: the "Why Stopped" field is a real example of messy, partly missing data, which is what the data roles in this session handle.

## Slide 1 — Four roles, one evidence chain

**Slide text**

- The biostatistician shapes the question and planned inference.
- The data scientist explores additional data and hypotheses.
- The data manager makes collected observations usable.
- The statistical programmer makes the analysis reproducible.

**Instructor notes**

Use the [role reference](roles.md) as a handout. State that these are typical responsibilities, not impermeable boundaries. Software preferences differ by team; neither SAS nor Python defines a profession. Students should recognize the task and output before they recognize the tool.

## Slide 2 — Biostatistician

**Slide text**

- Responsibility: align design and analysis with the clinical question.
- Outputs: design rationale, analysis plan, interpretation.
- Collaborators: clinicians, data management, programmers, RA.

**Instructor notes**

Explain why endpoint timing, population, comparator, and missing-data considerations should enter before data collection. Point back to the public study's clinical question. Describe a statistician's contribution without claiming knowledge of specific SLN360 job assignments. The point is translating a medical question into evidence, not teaching the sample-size formula.

## Slide 3 — Data scientist

**Slide text**

- Responsibility: explore patterns and evaluate useful predictive/integrative approaches.
- Outputs: exploration, models, RWD feasibility estimates.
- Collaborators: clinical experts, statisticians, governance and engineers.

**Instructor notes**

Use a hospital dataset to ask whether enough potentially eligible patients exist for a proposed trial. A coding-based count is only a first estimate: eligibility details, geography, consent, and competing studies influence recruitability. A model predicting risk does not by itself estimate a treatment effect. RWD can inform design without automatically replacing a randomized comparison.

## Slide 4 — Statistical programmer

**Slide text**

- Responsibility: implement and check agreed data/analysis specifications.
- Outputs: standardized data, analysis-ready data, TFLs.
- Collaborators: biostatistician, data manager, standards specialists.

**Instructor notes**

Explain traceability: another person should be able to understand where an output came from and reproduce it. This is domain-aware work, not simply pressing “run.” Distinguish programmed output checks from QA's broader process responsibilities. Do not teach derivation code.

## Slide 5 — Data manager

**Slide text**

- Responsibility: support complete, consistent, usable observations.
- Outputs: collection specifications, queries, reconciled database.
- Collaborators: sites, CRAs, laboratories, statisticians and programmers.

**Instructor notes**

Give examples: a date before enrollment, incompatible units, or a missing scheduled lab. A database can be syntactically tidy while clinically questionable. The data manager coordinates resolution with the people who generated the observations; unresolvable missing values remain missing.

## Slide 6 — Handoffs and supporting roles

**Slide text**

- Show the [shared workflow](roles.md#shared-workflow).
- Governance: appropriate access and use.
- QA: reliable processes; RA: regulatory strategy and evidence expectations.

**Instructor notes**

Run the [missing-lab demonstration](roles.md#a-missing-laboratory-result-instructor-demonstration) in two or three minutes. Ask one question: “Who investigates the source, and who assesses the analysis impact?” Give the answer immediately after a few responses. Keep this a demonstration rather than a lengthy exercise or audit scenario.

## Slide 7 — Four forms of the same evidence journey

**Slide text**

| Stage | Purpose |
| --- | --- |
| Collected observations | What happened and what was measured |
| SDTM-style domains | Organize standardized clinical records |
| Analysis-ready data | Represent the planned analysis clearly |
| TFLs | Communicate results for review and decisions |

**Instructor notes**

Open [the synthetic-data guide](../../data/synthetic/README.md). Display two or three rows only: DM for participants, AE for events, VS for vital signs, LB for lab results. Follow the participant identifier across domains. Then show the small analysis layer and one TFL without teaching column derivations. CDISC describes SDTM and ADaM as different standards with different purposes. Our educational CSVs are simplified examples, not certified standard datasets. [CDISC SDTM](https://www.cdisc.org/standards/foundational/sdtm), [CDISC ADaM](https://www.cdisc.org/standards/foundational/adam)

## Slide 8 — Read a table, a figure, and a listing

**Slide text**

- Table: summarize a population or events.
- Figure: make a pattern over time visible.
- Listing: retain individual detail for review.

**Instructor notes**

Use the [TFL collection](../../tfl/README.md). Ask students to find the denominator in the safety table and the number observed at each figure visit. Explain why counting event records is different from counting participants with events. A listing is not a replacement for a summary. Label the invented study clearly before opening its outputs; do not call the invented arms SLN360 doses.

## Slide 9 — RWD informs trial feasibility

**Slide text**

- Start with an eligibility question.
- Check definitions, missingness, and coverage.
- Distinguish potentially eligible from actually recruitable.

**Instructor notes**

Invent a simple scenario verbally: a hospital code identifies 500 candidates, but only some have a recent Lp(a) measurement and satisfy the study criteria. Do not present invented numbers as research results. Ask what the data scientist can estimate and what requires clinical/site input. Mention access and permitted-use review before linking data. The lesson is appropriate use, not building a recruitment model.

## Slide 10 — AI can help discovery; human evidence remains necessary

**Slide text**

- Target hypotheses and molecule proposals are inputs to experiments.
- Experimental and clinical studies address different questions.
- Discovery speed and patient benefit require different evidence.

**Instructor notes**

Use the two [source-checked case cards](../research/ai-drug-development.md). SLN360 remains our trial-workflow example; we are not claiming it was discovered by AI. In the next slides, compare evidence levels and limitations rather than algorithms or marketing language.

## Slide 11 — Milestone: rentosertib

**Slide text**

- AI supported target prioritization and molecular design.
- The program reached a published randomized phase 2a study.
- Encouraging results are a reason to investigate further, not proof of approval.

**Instructor notes**

Keep clinical details in the optional research note. Explain that a randomized drug comparison does not randomize the discovery process: it cannot establish that AI discovers better drugs than conventional research. Small, short studies leave efficacy durability and safety questions. [Discovery paper](https://www.nature.com/articles/s41587-024-02143-0), [phase 2a report](https://www.nature.com/articles/s41591-025-03743-2)

## Slide 12 — Setback: DSP-1181

**Slide text**

- An AI-assisted discovery collaboration reached phase I.
- The sponsor subsequently disclosed discontinuation.
- The public disclosure does not identify which expected criteria were unmet.

**Instructor notes**

Teach the boundary of public evidence. Do not state that the candidate failed to improve OCD symptoms, that toxicity caused the stop, or that AI caused failure. The selected historical disclosure supports a narrower statement about development stopping after phase I results. [Initial announcement](https://www.sumitomo-pharma.com/news/20200130.html), [January 2022 presentation, slide 15](https://www.sumitomo-pharma.com/ir/library/presentation/assets/pdf/eir20220131.pdf)

## Recap and student topics

Two oral checks: (1) Can the data manager replace a missing measurement with zero? (2) Does one progressing and one discontinued AI program establish an industry-wide success rate? See [answers](answers.md).

Assign the three [session-2 topics](presentations.md#after-session-2). If presentations were shorter than 30 minutes, use the recovered time for role questions or reading outputs rather than additional technical material.

## References for this session

Use the linked [CDISC SDTM](https://www.cdisc.org/standards/foundational/sdtm) and [ADaM](https://www.cdisc.org/standards/foundational/adam) pages, the [public-study card](case-study.md), and the primary sources in [the AI research note](../research/ai-drug-development.md). Professional-role examples are an illustrative teaching model, not claims about named employees.
