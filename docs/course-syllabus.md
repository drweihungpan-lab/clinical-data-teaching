# Course Syllabus: Data Processing in Clinical Trials & the Bio-Pharma Ecosystem

## Course Overview

**Total duration:** 6 hours  
**Format:** 3 sessions, 2 hours per session  
**Target audience:** Master's students with a statistics background and no assumed clinical-trial experience

**Teaching style:** Knowledge transfer, high-level examples, brief interpretation checks; no required coding

**Teaching package:** [Instructor guide](teaching/instructor-guide.md), [three lessons](../README.md), synthetic CSVs, TFL examples, surveys, and presentation guidance

## Course Objective

This intensive course bridges the gap between academic statistics and the global biopharmaceutical industry. Students will develop a practical understanding of:

- The drug and medical device development lifecycle
- The corporate ecosystem surrounding clinical development, including Pharma, Biotech, CROs, and CMOs
- Regulatory landscapes and data standards used in clinical research
- The evolving roles of Biostatisticians and Data Scientists in the era of artificial intelligence and digital health

## Learning Outcomes

By the end of the course, students should be able to:

1. Describe the objectives, data, and statistical characteristics of clinical trial Phases I–IV.
2. Explain how Pharma, Biotech, CRO, and CMO organizations contribute to the biopharma value chain.
3. Compare the responsibilities, outputs, and handoffs of Biostatisticians, Data Scientists, Statistical Programmers, and Data Managers, with brief awareness of Data Governance, QA, RA, and clinical teams.
4. Explain how real-world data can inform trial feasibility and distinguish an AI-assisted drug-development milestone from a setback using public evidence.
5. Explain the purpose of SDTM, analysis-ready data, and TFLs without building them.
6. Recognize the different evidence, privacy, information-security, and data-access questions raised by an EU diagnostic product, with high-level IVDR, GDPR, ISMS, and EU Data Act context.

## Shared Examples and Participation

- The published **SLN360 phase 1 study** is the real drug-development example. Its Lp(a) biomarker findings are discussed at a high level; no confidential information or actual patient-level records are used.
- A separate invented **EDU-LPA-001** dataset demonstrates the shape and purpose of SDTM-style domains, analysis-ready data, and TFLs. Its design and results are not those of SLN360.
- A separate fictional **CardioLab Connect** Lp(a) blood-test product and portal anchor session 3. It is not a Silence Therapeutics product or a SLN360 companion diagnostic.
- Each session includes a ten-minute break. Sessions 2 and 3 start with three student presentations of 5–10 minutes, one per open topic from the preceding session, within the two-hour slot.
- Three open topics are offered after every session; the final set is optional follow-up reflection with no extra meeting. Surveys bracket the complete course; presentations and knowledge checks are ungraded.

## Session Schedule

### Session 1: Drug Development Lifecycle & the Corporate Ecosystem

**Duration:** 2 hours

#### Opening Scenario: A Perfect Discovery

- Start from an invented researcher's published mouse study and ask what is missing before a clinical trial.
- Sort the gaps into two directions: science (reproducibility, biology, safety, human evidence) and business/operations (funding, market, manufacturing, permission to start).

#### The Clinical Trial Pipeline

- Introduce protocol, endpoints, randomization, blinding, and safety monitoring before discussing phases.
- Deconstruct Phases I–IV by examining their objectives, typical sample sizes, endpoints, and data collection requirements.
- Trace the progression from early safety and dose-finding studies through confirmatory trials and post-market surveillance.
- Discuss how the purpose and structure of clinical data change across the development lifecycle.
- Use the published SLN360 study to explain evidence that supports continuing, changing, or stopping development, without detailed dose-cohort analyses.

#### Mapping the Global Industry Ecosystem

Taught as the invented researcher's journey from paper to first patient: university grant and patent, spin-out biotech and venture funding, a light market check, preclinical safety studies and a clinical batch, permission to start (FDA IND; EU clinical-trial application), and a pharma partner for later phases.

- **Pharma:** Understand the operating model, product portfolio, development strategy, and data assets of large pharmaceutical companies.
- **Biotech:** Explore science-driven development, funding models, partnerships, and the role of focused data assets.
- **Biopharmaceuticals:** Situate biologics and advanced therapies within the broader industry landscape.
- **CROs (Contract Research Organizations):** Examine their role in clinical trial execution, statistical programming, data management, and operational delivery.
- **CMOs (Contract Manufacturing Organizations):** Introduce the connection between clinical development data and chemistry, manufacturing, and controls (CMC).

### Session 2: The Data Profession Landscape: Biostatistics, Data Science & AI

**Duration:** 2 hours

#### Professional Roles and Handoffs

| Role | Typical focus | Representative methods and outputs | Common tools and data contexts |
| --- | --- | --- | --- |
| **Biostatistician** | Trial design and planned inference | Design rationale, analysis plans, interpretation | Collaborates with clinicians, Data Managers, and Statistical Programmers |
| **Data Scientist** | Exploration and RWD informing design | Exploratory findings, predictive approaches, recruitment-feasibility estimates | Collaborates with clinical, statistical, governance, and engineering teams |
| **Statistical Programmer** | Reproducible implementation and output checks | Standardized/analysis datasets and TFLs | Implements agreed specifications with statistical and data-management teams |
| **Data Manager** | Usable collected observations | Collection specifications, queries, reconciled database | Works with sites, CRAs, laboratories, statisticians, and programmers |

Discuss overlap rather than defining professions by software. Introduce Data Governance, QA, RA, investigators, CRAs, and Clinical Operations briefly through handoffs. Use one instructor-led missing-lab-result scenario.

#### Conceptual Clinical-Data Workflow

- Clinical question → design → collected observations → SDTM-style domains → analysis-ready data → TFLs → development decision.
- Show a few DM, AE, VS, and LB records, a small analysis-ready illustration, and representative TFLs.
- Explain purpose and ownership, not mapping rules, variable derivations, or code.

#### AI in Early Drug Discovery and Development

- Explain target prioritization and molecule design at a high level.
- Compare rentosertib's published development milestone with DSP-1181's documented discontinuation, distinguishing clinical evidence from sponsor claims and undisclosed stopping criteria.
- Separate evidence about a drug's effect from evidence that AI improves the discovery process. Do not treat these two selected programs as an industry-wide success-rate sample.

### Session 3: Frontier Sectors & Regulatory Frameworks

**Duration:** 2 hours

#### Diagnostic Products and Digital Health

- Contrast changing biology with measuring it; connect intended use to evidence questions using the separate fictional Lp(a) test and portal.
- Introduce scientific validity, analytical performance, and clinical performance under the IVDR at a high level.
- Discuss remote participation, software, and sensor-data opportunities briefly as context. Do not transfer drug phases or another jurisdiction's device classes directly to the IVD case.

#### Regulatory Frameworks and Compliance

- Use a simple connecting diagram: **IVDR** (evidence for intended purpose), **GDPR** (appropriate processing of personal data), **ISMS / ISO/IEC 27001** (information-security management), and **EU Data Act** (applicable connected-product data access).
- Keep these frameworks and the QA/RA distinction as supporting context for statistics students; no detailed legal articles, audit procedures, or certification training.
- Retain concise FDA/EMA medicine-development, CDISC, and GCP context where it supports the workflow. EMA is not the general EU device regulator.
- Discuss data integrity, provenance, controlled access, and appropriate collaboration; do not assume every framework applies identically to every portal or assay.

## Prerequisites

Students should have:

- A basic understanding of statistical inference.
- Familiarity with regression models.
- An interest in healthcare, clinical research, or the pharmaceutical and medical device industries.

Prior experience with SAS, R, Python, clinical trials, or regulatory submissions is helpful but not required.

## Key Terms

**Biopharma**, **Biotech**, **CRO**, **CMO/CDMO**, **protocol**, **endpoint**, **TFL**, **CDISC**, **SDTM**, **ADaM**, **GCP**, **RWD/RWE**, **QA**, **RA**, **IVDR**, **GDPR**, **ISMS**, **ISO/IEC 27001**, **EU Data Act**, **FDA**, and **EMA**.

For the current source register and detailed references, see [teaching references](teaching/references.md).
