# AI in early drug discovery and development: two teaching cases

Checked: 2026-10-11. Audience: statistics master's students; suggested use: a 15–20 minute high-level lesson. These are historical milestones verified against primary sources, not a claim about either programme's latest development or regulatory status. “Success” below means reaching a meaningful evidence milestone, not demonstrating an approved, effective medicine.

The learning objective is to distinguish three questions: did AI contribute to discovering a candidate, what does a clinical study establish about that candidate, and what does a sponsor's continuation decision reveal? Each question has a different unit of analysis and requires different evidence.

## Case card 1 — Rentosertib: a randomized clinical evidence milestone

**Candidate and AI role.** Insilico Medicine's rentosertib, formerly ISM001-055, targets TNIK for idiopathic pulmonary fibrosis (IPF). The discovery paper describes PandaOmics ranking target hypotheses from omics, biological networks and literature, followed by Chemistry42 generating molecular leads. Researchers synthesized, tested and optimized compounds; AI supported both target prioritization and molecular design. The authors report roughly 18 months from target discovery to preclinical candidate nomination. This is a defined discovery interval, not time to approval. The preceding preclinical/phase 1 paper appeared online on 8 March 2024. [Ren et al., Nature Biotechnology](https://www.nature.com/articles/s41587-024-02143-0).

**Verified clinical milestone.** The China phase 2a trial ran from 19 July 2023 to 11 June 2024; its peer-reviewed report appeared online on 3 June 2025. Seventy-one patients were randomized, double-blind, to 12 weeks of placebo or three regimens: 30 mg once daily, 30 mg twice daily, or 60 mg once daily. The primary endpoint was having at least one treatment-emergent adverse event: 70.6% on placebo versus 72.2–83.3% on active treatment. Secondary forced vital capacity (FVC) mean change was +98.4 ml at 60 mg once daily (95% CI 10.9–185.9), versus −20.3 ml on placebo (−116.1–75.6). Liver toxicity and diarrhea caused treatment discontinuations. [Xu et al., Nature Medicine](https://www.nature.com/articles/s41591-025-03743-2).

**Teaching takeaway.** An AI-assisted discovery programme reached a randomized patient trial with an encouraging lung-function signal. That supports further investigation. It does not by itself establish durable clinical benefit, comprehensive safety, regulatory approval, or superiority of AI over another discovery process.

## Case card 2 — DSP-1181: clinical entry followed by discontinuation

**Candidate and AI role.** Sumitomo Dainippon Pharma and Exscientia jointly developed DSP-1181, a serotonin 5-HT1A receptor agonist intended initially for obsessive-compulsive disorder (OCD). Their 30 January 2020 announcement said phase 1 had begun in Japan. It explicitly combined Sumitomo's monoamine GPCR discovery expertise with Exscientia's Centaur Chemist AI platform. The companies reported completing exploratory research in less than 12 months, compared with a claimed conventional average of 4.5 years. Treat that comparison as a sponsor-reported benchmark, not a controlled estimate of AI's causal effect. [Joint company announcement](https://www.sumitomo-pharma.com/news/20200130.html).

**Verified timeline and setback.** The June 2021 factbook still listed DSP-1181 in Japanese phase 1, with pipeline status dated 12 May 2021. [Sumitomo factbook, pp. 11 and 13](https://www.sumitomo-pharma.com/ir/library/factbook/assets/pdf/fb202106.pdf). The company's conference-call presentation dated 31 January 2022 then recorded discontinued development in Japan. Its stated reason was: “As a result of Phase 1 study, not reach expected criteria.” The slide describes changes since 27 October 2021; it establishes disclosure by January 2022, not the exact internal decision date. [Q3 FY2021 presentation, slide 15](https://www.sumitomo-pharma.com/ir/library/presentation/assets/pdf/eir20220131.pdf).

**Teaching takeaway.** The sponsor documented a development stop linked to phase 1 results, but the cited disclosure does not identify the unmet criteria or provide quantitative trial results. Do not assign the stop to efficacy, safety, pharmacokinetics or commercial strategy without further documentation. In particular, it does not establish failed efficacy in OCD patients. The supported wording is “discontinued after phase 1 did not meet unspecified expected criteria.”

## Comparison for discussion

| Question | Rentosertib | DSP-1181 |
| --- | --- | --- |
| Documented AI contribution | Target prioritization and molecule design | Compound discovery with pharmaceutical expertise |
| Selected milestone | Published randomized phase 2a findings | Official discontinuation after phase 1 |
| Main evidence form | Peer-reviewed patient trial | Sponsor development disclosure |
| Appropriate classroom conclusion | Encouraging evidence merits further testing | Fast discovery did not ensure continued development |
| Unsupported leap | AI has proved clinical superiority | AI caused an efficacy failure |

Sources for the factual comparison are linked in the cards. These are deliberately contrasting examples, not a representative sample. One milestone and one discontinued programme cannot estimate a success rate: “one of two” has no meaningful denominator for the AI drug-discovery industry. The diseases, mechanisms, study stages and disclosure depth also differ, preventing a direct efficacy comparison.

## Statistical caveats and questions

**Separate the treatment effect from the discovery-method effect.** Randomizing patients to a molecule or placebo can support a causal treatment comparison under the trial's assumptions. It does not randomize discovery projects to AI or conventional research. To assess whether AI improves discovery, ask for prospectively defined, comparable projects, resource use, elapsed time, and all outcomes, including abandoned candidates. Specify where the clock starts and stops before comparing speed claims.

**Read uncertainty at the right level.** The arithmetic difference between the quoted FVC means is 118.7 ml; this calculation is not a separately reported treatment-effect estimate. A confidence interval for change within an arm answers a different question from a confidence interval for the between-arm contrast. Ask students what additional analysis they would need before making a comparative claim. Also separate statistical evidence from the magnitude and durability of benefit meaningful to patients.

**Ask about missing outcomes and safety precision.** The rentosertib paper reports 22 missing week-12 spirometry measurements and multiple imputation assuming missing at random; it made no statistical adverse-event comparisons. Insilico sponsored the study, and several authors were employees. [Trial methods and disclosures](https://www.nature.com/articles/s41591-025-03743-2). For discussion, ask whether unobserved outcomes could depend on tolerability or worsening health, and what sensitivity analysis would probe that possibility. Similar observed adverse-event percentages do not establish safety equivalence; small, short studies provide limited information about rare or delayed harms.

**Keep decision labels distinct from measured endpoints.** A programme-level stop is a decision, not an effect size or hypothesis-test result. Without the relevant criterion, population, endpoint and uncertainty, students cannot reconstruct the DSP-1181 decision statistically. Conversely, a decision to continue a programme would not itself prove benefit. This is an exercise in recognizing the boundary of public evidence, rather than filling gaps with a plausible story.

## Suggested instructor explanation

“AI can propose which biological target to pursue and which molecules to synthesize. Experimental work then checks those proposals, and human studies address new questions. Rentosertib illustrates progress to randomized evidence; DSP-1181 illustrates that reaching humans quickly does not guarantee a programme continues. Keep discovery productivity, candidate performance and development decisions separate when interpreting a headline.”

Give students two minutes to rewrite “AI invented a successful drug” and “AI's drug failed” into claims that these sources actually support. Then ask which evidence would change their conclusions: a larger prespecified efficacy trial, longer safety follow-up, a comparable discovery cohort, or disclosure of the stopping criterion. Close by having them name the estimand for each question. The aim is to practice calibrated inference while preserving both the technological contribution and the remaining uncertainty.
