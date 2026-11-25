# Session 1 — Data processing in clinical trials

**Duration:** 120 minutes, including a ten-minute break. **Outcome:** explain how a development question becomes a study and recognize the teams needed to deliver it.

| Minutes | Content |
| --- | --- |
| 0–3 | Welcome and survey themes |
| 3–13 | Opening scenario: a perfect discovery |
| 13–30 | Clinical-trial foundations |
| 30–55 | Phases, success rates, why programs fail, and development decisions |
| 55–65 | Break |
| 65–85 | Industry journey: from paper to first patient |
| 85–105 | Public SLN360 case discussion |
| 105–120 | Recap, three checks, and take-home exercise |

**Welcome (0–3).** Share survey themes in one or two sentences and, briefly, your own route from statistics into clinical development and medical devices. Use an experience you can share publicly, not a confidential study detail.

## Slide 1 — A perfect discovery

**Slide text**

> Dr. Lin, a respected university researcher, finds that blocking protein X stops disease Y in mice. The study is published in a top journal. Headlines: "Cure found."

- Could we give this to patients next month?
- What is missing between this paper and a clinical trial?

**Instructor notes**

This scenario is invented. It is deliberately not SLN360 or any real program. Read the story aloud, then ask students to work in pairs for about three minutes and list everything that must happen before the first patient is dosed. Collect answers on the board without correcting them yet. Expect answers like "test in humans," "check safety," and "get approval"; push for the less obvious ones: "Who pays?", "Who makes the drug?", "Will it work in another lab?" Then reveal Slide 2 and sort their answers into its two columns.

## Slide 2 — Two directions: what's missing?

**Slide text**

| Science: "Is it real, and is it safe?" | Business and operations: "Who pays, and can it get there?" |
| --- | --- |
| Reproducibility: will another lab get the same result? | Funding: grant → patent → biotech → investors → pharma |
| Biology: does the mouse model reflect the human disease? | Market: unmet need, how many patients, competitors |
| Safety: what does it do to the rest of the body? What first dose? | Manufacturing: who makes a consistent clinical batch? |
| Evidence in people: what to measure, compared to what? | Permission to start: regulators, ethics review, sites |

**Instructor notes**

Place each student answer in a column; note anything neither column captures. Make the two columns meet: manufacturing and permission to start depend on the science column's safety and quality data. Each science gap also carries a data question: a small animal sample, an effect that may be inflated or may not replicate, a mouse outcome that is not a human endpoint. As one illustration of replication concerns, an industry team reported confirming only 6 of 53 "landmark" preclinical cancer findings ([Begley and Ellis, Nature, 2012](https://www.nature.com/articles/483531a)); present it as one team's experience in one field, not a universal rate. Close with: "The first half of today answers the science column; after the break we follow the business column." Keep pointing back to this slide.

## Slide 3 — The protocol is a shared plan

**Slide text**

- Who can enter the study, and why?
- What intervention and comparison will be used?
- What will be measured, when, and how?
- What safety and analysis decisions are planned?

**Instructor notes**

Define a clinical trial as a planned investigation involving people to address an intervention question. Contrast it with observing routine care without assigning an intervention. A protocol connects objectives, population, treatment, visits, and measurements. A statistical analysis plan makes the analysis approach more explicit. A beautifully fitted model cannot recover an outcome never collected. [FDA clinical-research overview](https://www.fda.gov/patients/drug-development-process/step-3-clinical-research)

## Slide 4 — Endpoints connect medicine to statistics

**Slide text**

- An endpoint defines what result matters and when it is assessed.
- A laboratory biomarker and a clinical event answer different questions.
- An analysis needs a population, comparison, and handling of incomplete observations.

**Instructor notes**

Use Lp(a) as the cardiovascular biomarker and cardiovascular events as a different outcome. Do not introduce derivation formulas. Ask: “If the biomarker improves, what else would you want to know?” Connect to duration of benefit, adverse effects, and the relationship between marker and patient outcomes. These are design and interpretation questions, not just significance tests. Point back to Slide 2: Dr. Lin's mouse result is a mouse outcome, not a human endpoint.

## Slide 5 — Randomization, blinding, and safety

**Slide text**

- Randomization supports a fair treatment comparison.
- Blinding reduces the influence of knowing the assignment.
- Safety monitoring can affect whether and how a study continues.

**Instructor notes**

Randomization balances groups in expectation; it does not guarantee exact balance in a small sample. Blinding and allocation concealment address different sources of bias. Avoid claiming that every trial can be fully blinded. Safety is not established by a nonsignificant difference in a small adverse-event table. Explain how medical and statistical judgment meet when deciding whether to increase a dose or continue recruitment.

## Slide 6 — Phases are different evidence questions

**Slide text**

| Phase | Main question | Typical size | Statistical/data emphasis |
| --- | --- | --- | --- |
| I | Can early human exposure be studied safely, and what doses merit further work? | 20–100 participants | Close safety observation, dose/cohort context, descriptive signals |
| II | Is there enough evidence of activity and a suitable regimen to continue? | Up to several hundred | Endpoint/dose choices, uncertainty, feasibility |
| III | Is the benefit–risk evidence adequate for the proposed use? | 300–3,000 | Prespecified comparisons, larger evidence base, generalizability |
| IV | What is learned after authorization in practice? | Several thousand | Longer-term safety/effectiveness and broader use |

**Instructor notes**

Typical sizes are FDA's broad illustrations ([FDA clinical research](https://www.fda.gov/patients/drug-development-process/step-3-clinical-research)). Sample sizes grow in many programs but are not a rule defining the phases. The actual size comes from the question, endpoint, expected effect, and power calculation: rare-disease trials can be far smaller and cardiovascular outcome trials far larger. Disease, design, and purpose can change these patterns. Phase I is not always conducted in healthy volunteers. Do not transfer this phase structure mechanically to devices. [FDA definitions](https://www.fda.gov/drugs/investigational-new-drug-application-ind/drug-development-and-review-definitions)

## Slide 7 — How often does a candidate make it?

**Slide text**

| Transition (2011–2020) | Success rate |
| --- | --- |
| Phase I → Phase II | 52.0% |
| Phase II → Phase III | 28.9% (the biggest hurdle) |
| Phase III → submission | 57.8% |
| Submission → FDA approval | 90.6% |

**Overall, Phase I → approval: 7.9%, about 1 in 13 candidates** (shown as its own row below the four transitions).

- Why do the other 12 stop? Write down two reasons before the next slide.

**Instructor notes**

Rates are from the BIO/Informa/QLS analysis of 12,728 phase transitions in 2011–2020 ([BIO 2021](https://go.bio.org/rs/490-EHZ-999/images/ClinicalDevelopmentSuccessRates2011_2020.pdf)). Ask students to multiply the four transition rates: 0.520 × 0.289 × 0.578 × 0.906 ≈ 0.079. Compounding is the point. Then ask the statistics questions: what is the denominator (program–indication transitions, not molecules or trials), and which programs are in the database? Rates vary widely by disease area. In the same analysis, hematology reached 23.9% overall and oncology 5.3%, and programs that preselected patients with a biomarker reached 15.9%. Other analyses using different methods and periods report different overall numbers, so present this as one well-documented estimate rather than a fixed law. FDA's own patient page, for example, gives about 70% moving past phase 1 and about 33% past phase 2. Asking why the sources differ (period, denominator, which programs are counted) is a good statistics question.

Give pairs about two minutes to write two reasons a program might stop. Collect a few and sort them aloud into the two columns from Slide 2, science and business/operations. That sorting sets up the next two slides. Do not reveal the answers yet.

## Slide 8 — Why programs fail: the drug and the science

**Slide text**

| Reason | Share of clinical failures | What it looks like |
| --- | --- | --- |
| Lack of efficacy | 40–50% | The target or animal model did not translate to people; no meaningful benefit over control |
| Unmanageable toxicity | about 30% | Off-target or organ harm; the benefit no longer outweighs the risk |
| Poor drug-like properties | 10–15% | Too little exposure, fast clearance, does not reach the tissue; wrong dose chosen |

**Instructor notes**

Shares are as summarized for 2010–2017 clinical trials by [Sun et al., 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9293739/). The remaining about 10% they attribute to lack of commercial need and poor strategic planning, which the next slide covers. Compare with the students' list. Lack of efficacy is the left column of Slide 2 coming due: a mouse result that did not hold in humans. This is why phase II, the first real test of efficacy in patients, is the biggest hurdle. Toxicity often appears early, but rare or delayed harms may only surface in large or long trials.

## Slide 9 — Why programs and trials fail: operations

**Slide text**

| Reason | What it looks like |
| --- | --- |
| Money and strategy | Funding runs out, a portfolio is reprioritized, a competitor gets there first |
| Statistical design | Underpowered sample size, an endpoint that does not capture benefit, wrong population, unrealistic assumptions |
| Recruitment and retention | Too few eligible patients, criteria too strict, participants drop out |
| Sites and execution | Slow start-up, protocol deviations, missing or poor-quality data |
| Supply | The clinical batch is delayed or fails quality checks |

**Instructor notes**

These reasons can stop a trial even when the drug might work, so a "failure" is not always evidence against the drug. One analysis of 905 terminated trials on ClinicalTrials.gov found that 68% stopped for reasons other than the trial's accumulated data, and insufficient accrual was the leading reason among those (57%, 350 of 619) ([Williams et al., 2015](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0127242)). Point out that the denominator here is terminated trials, not drug programs, so it cannot be added to the shares on Slide 8. That difference is itself a statistics lesson.

Emphasize the statistician's part. Sample size and power, endpoint choice, eligibility criteria, and realistic recruitment assumptions are design decisions made before the first patient enrolls. Session 2 shows how real-world data can test recruitment feasibility.

## Slide 10 — Development is a sequence of decisions

**Slide text**

- Continue: evidence supports the next question.
- Change: revise dose, population, measurements, or approach.
- Stop: the evidence or feasibility no longer supports the program.

**Instructor notes**

Distinguish evidence from decision criteria. A small study may justify further investment without establishing approval-level evidence. Scientific, safety, operational, and business considerations can all affect development decisions; do not infer an undisclosed cause from a headline. Ask students to name what a phase I trial cannot answer reliably.

## Industry journey: from paper to first patient (65–85)

Return to Dr. Lin and follow the business-and-operations column of Slide 2. Each step introduces one kind of organization, so the ecosystem is learned as a journey, not a list. Budget about four minutes per slide. The path below is one common route, not the only one: some programs stay in academia longer, some are licensed directly to pharma, and some are funded by foundations or governments.

## Slide 11 — From paper to company

**Slide text**

- University lab: grants fund the discovery; the tech-transfer office files a patent.
- Spin-out **biotech**: founded around the licensed patent, funded by venture investors.
- Light market check: unmet need, number of patients, existing competitors.

**Instructor notes**

Publishing before filing a patent can damage patentability. Europe generally requires absolute novelty; the US offers a limited grace period for an inventor's own disclosure. Mention this as a practical hook, not legal training. Investors ask whether the science is real (the left column) and whether a product could matter commercially. Keep the market discussion to two minutes: who needs this, how many people, and what already exists. Pricing and reimbursement are out of scope today. A biotech often has one focused program and limited cash, so every study is also a funding milestone.

## Slide 12 — Getting ready for the first human

**Slide text**

- Choose one specific drug candidate, not just "blocking protein X."
- Animal pharmacology and pharmacokinetics: does it reach the target, and how long does it stay?
- Formal (GLP) safety studies, often run by a **CRO**.
- A quality-controlled clinical batch, often made by a **CDMO**: the CMC evidence.
- Documents: investigator's brochure, first protocol, consent form, starting-dose rationale.

**Instructor notes**

This is preclinical development. For a typical small molecule, repeated-dose toxicity studies in two species, one of them a non-rodent, generally support early clinical trials ([ICH M3(R2)](https://database.ich.org/sites/default/files/M3_R2__Guideline.pdf)); biologics follow a different, product-specific approach. Explain CMC as chemistry, manufacturing, and controls in one sentence: evidence that each batch is what it claims to be. The first human dose is chosen from animal safety and exposure data with a margin of caution. A small biotech rarely owns animal facilities or manufacturing plants, which is why CROs and CDMOs exist. [FDA preclinical research](https://www.fda.gov/patients/drug-development-process/step-2-preclinical-research)

## Slide 13 — The regulator's role at each stage (FDA as example)

**Slide text**

| Stage | What FDA does | Type of control |
| --- | --- | --- |
| Entering humans (IND) | Reviews preclinical, manufacturing, and the first protocol within 30 days | **Entry gate**: silence after 30 days means go |
| During every trial | Receives expedited safety reports (7 or 15 days) and annual reports | **Ongoing watch**: can place a clinical hold at any time |
| Phase 1 → 2 → 3 | Receives each new protocol; it may start once submitted and IRB-approved | **Veto, not approval**: stops only for safety or a clearly deficient design |
| End-of-phase 2 meeting | Advises on phase 3 design, endpoints, number of trials | **Advice**: not binding, but ignoring it is risky |
| Submission (NDA/BLA) | Full review: re-analyzes data, inspects sites and factories | **Approval gate**: approval or a Complete Response Letter |

- The regulator protects participants throughout; it does not guarantee the program will succeed.

**Instructor notes**

Many students assume the regulator approves each phase. In the US the default is "go unless FDA says stop": a new protocol under an existing IND may begin once submitted to FDA and approved by an IRB ([21 CFR 312.30](https://www.ecfr.gov/current/title-21/section-312.30)). FDA can place a clinical hold for safety and, for phase 2/3, when the protocol is clearly deficient in design to meet its stated objectives ([21 CFR 312.42](https://www.ecfr.gov/current/title-21/section-312.42)). The IND enters effect 30 days after receipt unless FDA places a hold ([21 CFR 312.40](https://www.ecfr.gov/current/title-21/section-312.40)). Expedited safety reports follow [21 CFR 312.32](https://www.ecfr.gov/current/title-21/section-312.32). Day-to-day monitoring is the sponsor's job; FDA inspects selected sites, mostly around submission.

Link to the success-rate slide: why are about 9% of submissions never approved, even after a "successful" trial? Meeting the SAP shows the trial hit its own prespecified target; FDA judges the whole benefit–risk case. FDA re-analyzes the submitted data (robustness to missing data, single-site effects, multiplicity), may not accept the endpoint, population, or dose, may need more than one adequate trial, needs an adequate safety database, and inspects sites and factories. If not approvable, FDA sends a Complete Response Letter listing what must be fixed. One line for students: "The SAP is the exam the sponsor wrote for itself; the regulator grades the whole case." Regulatory affairs (RA) coordinates these interactions. Do not teach submission procedures.

## Slide 14 — US and EU: who decides what?

**Slide text**

| Question | United States | European Union |
| --- | --- | --- |
| Who authorizes a clinical trial? | FDA, through the IND | Each member state concerned (competent authority and ethics committee), via one application in CTIS, not EMA |
| Does each new trial need authorization? | No: new protocols run under the existing IND unless FDA objects | Yes: every trial needs its own explicit authorization |
| Scientific advice during development | FDA meetings (pre-IND, end-of-phase 2) | EMA scientific advice, or national agencies; not binding |
| Who approves the medicine? | FDA approves the NDA/BLA | Centralized route: EMA's CHMP gives an opinion; the European Commission grants the authorization |
| If not approvable | Complete Response Letter | Negative CHMP opinion, or the sponsor withdraws |

**Instructor notes**

The EU is closer to the "gate at every trial" picture many students expect: under the [Clinical Trials Regulation](https://eur-lex.europa.eu/eli/reg/2014/536/oj/eng), each trial is authorized before it starts. The application has a scientific part assessed jointly by the member states concerned, led by a reporting member state, and a national part (such as informed consent, site suitability, and recruitment) assessed by each member state, including ethics review. EMA does not authorize clinical trials. For marketing, EMA's committee assesses the evidence and the European Commission decides ([EMA authorization overview](https://www.ema.europa.eu/en/about-us/what-we-do/authorisation-medicines)); national and decentralized routes also exist. Stress the distinction: permission to *start a trial* is not approval to *market a medicine*. Keep this to a comparison; do not teach procedures or timelines.

## Slide 15 — Who carries it further?

**Slide text**

| Organization | Where it appeared in Dr. Lin's journey | Connection to data |
| --- | --- | --- |
| Biotech | Turned a paper into a program | Concentrated assets, partnerships, resource trade-offs |
| CRO | Ran safety studies; later runs trials | Operations, data management, programming, analysis |
| CMO/CDMO | Made the clinical batch | Batch quality, product consistency, CMC evidence |
| Pharma | Partners, licenses, or acquires, often after early human data | Multiple programs, larger trials, post-market data |

**Instructor notes**

A pharma partner brings money, development experience, and scale for later phases. Link back to Slide 10: each phase result is also a business decision point. This is an orientation model, not a definition based on company size or tool stack. Biopharmaceutical describes a scientific/product area rather than a mutually exclusive corporate type. A sponsor can transfer activities to service providers while retaining appropriate oversight. [ICH roles and oversight](https://admin.ich.org/sites/default/files/inline-files/ICH_E6%28R3%29_Step%204_Presentation_2025_0123.pdf)

## Slide 16 — Sites turn plans into observations

**Slide text**

- Investigator/site: patient care and study assessments.
- CRA: monitoring and site follow-up.
- Clinical operations: coordinating sites and vendors.
- Laboratories and systems: measurements and records.

**Instructor notes**

Keep this high-level. Follow one blood sample: scheduled visit → collection → lab → result → clinical database. A missing result could reflect a missed visit, a lost specimen, a processing issue, or a transfer issue. The reason matters, but a statistician should not invent it. Session 2 shows the relevant handoffs.

**Brief regulatory context within this block**

GCP connects ethical study conduct, participant protection, reliable results, and clear sponsor/site responsibilities. It matters to how data are collected, checked, and reported, not only to an inspection. [FDA E6(R3) overview](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/e6r3-good-clinical-practice-gcp)

Slides 13–14 already covered the regulator's role and the US/EU differences; skip this unless students ask. [FDA review](https://www.fda.gov/drugs/information-consumers-and-patients-drugs/fdas-drug-review-process-ensuring-drugs-are-safe-and-effective), [EMA authorization overview](https://www.ema.europa.eu/en/about-us/what-we-do/authorisation-medicines)

## Slide 17 — SLN360: read the study, not only the headline

**Slide text**

- Use the [published case card](case-study.md).
- Identify the study question and actual design.
- Separate safety findings, biomarker response, and clinical benefit.

**Instructor notes**

Open the study and guide students through the card. Ask them to locate the primary outcome, treatment groups, and measurements. Briefly point to Table 1, Table 2, and Figure 2: participants, adverse events, and biomarker trajectories. Make the number of groups visible so nobody carries over the invented two-arm demonstration into the real study. No detailed cohort modeling or journal-figure redistribution is needed.

## Slide 18 — What would the next team need?

**Slide text**

- A result with its uncertainty and limitations.
- A reason to continue, revise, or stop.
- A clear account of what remains unknown.

**Instructor notes**

Ask students to imagine joining the development meeting. They should articulate the question a next study must answer, rather than simply say “the p-value is small.” Preview the four core data/statistical roles in session 2.

## Recap and take-home exercise

Three oral checks: (1) Does biomarker improvement alone establish fewer cardiovascular events? (2) If a CRO performs study activities, does the sponsor's oversight disappear? (3) Dr. Lin's mouse paper is in a top journal. Does that mean the first human trial can start? Name one science gap and one business gap. Answers are in [the instructor key](answers.md).

Assign the [take-home exercise](presentations.md#after-session-1-take-home-exercise--why-did-these-trials-stop): every student searches ClinicalTrials.gov for terminated trials in one condition, sorts the "Why Stopped" reasons into science, operations, or unclear, and prepares at most five slides. Tell students you will pick two presenters at the start of session 2, so everyone should come prepared. It extends Slides 8–9 with real registry data.

## References for this session

Use [BIO/Informa/QLS success rates 2011–2020](https://go.bio.org/rs/490-EHZ-999/images/ClinicalDevelopmentSuccessRates2011_2020.pdf), [Sun et al., 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9293739/), [Williams et al., 2015](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0127242), [FDA preclinical research](https://www.fda.gov/patients/drug-development-process/step-2-preclinical-research), [ICH M3(R2)](https://database.ich.org/sites/default/files/M3_R2__Guideline.pdf), [21 CFR 312.40](https://www.ecfr.gov/current/title-21/section-312.40), the [EU Clinical Trials Regulation](https://eur-lex.europa.eu/eli/reg/2014/536/oj/eng), [FDA phase definitions](https://www.fda.gov/drugs/investigational-new-drug-application-ind/drug-development-and-review-definitions), [FDA clinical-research overview](https://www.fda.gov/patients/drug-development-process/step-3-clinical-research), [ICH E6(R3) overview](https://admin.ich.org/sites/default/files/inline-files/ICH_E6%28R3%29_Step%204_Presentation_2025_0123.pdf), and the [SLN360 case reference](case-study.md). Sources checked for the 2026-10-11 implementation; opening and industry-journey sources checked 2026-11-25. The study findings are historical.
