# EU frameworks for a fictional Lp(a) blood test and connected portal

Official sources checked: **2026-10-11**. This teaching note separates four questions: what the diagnostic claims, how health data may be processed, how information security is managed, and whether connected-product data-access rights apply. Examples and classroom tasks below are proposed teaching applications, not findings about an actual product.

Assume a fictional manufacturer offers a quantitative lipoprotein(a), or Lp(a), blood test for a stated cardiovascular purpose, plus a portal showing results. The scenario does not specify the specimen, target population, intended users, clinical claim, instrument connectivity, or portal functions sufficiently to determine every regulatory consequence. Those details are inputs to the exercise, not blanks to fill with assumptions.

## Device boundary and intended purpose

A test intended to examine human blood and provide medical information fits the IVDR's diagnostic-device concept; it is not a medicine merely because its results inform treatment. The manufacturer’s **intended purpose** includes its labelling, instructions, promotional statements and performance evaluation. Device classification depends on intended purpose and inherent risks under Article 47 and Annex VIII: this note assigns no IVD class. A portal requires a separate assessment of its intended functions; the presence of test results alone does not establish that it is device software. [IVDR, Articles 2(2), 2(12), 47 and Annex VIII](https://eur-lex.europa.eu/eli/reg/2017/746/oj/eng).

EU device governance involves manufacturers, national competent authorities and, where required, notified bodies conducting conformity assessment. EMA is not the general EU device regulator. Its defined device roles include medicine-related consultations, such as companion diagnostics, and support for expert panels. A cardiovascular assay is not automatically a companion diagnostic. [EMA: medical devices and regulatory responsibilities](https://www.ema.europa.eu/en/human-regulatory-overview/medical-devices).

For teaching, have students draft a precise claim before selecting an endpoint. “Measures Lp(a)” and “predicts future cardiovascular events in a specified population” pose different evidence questions. Ask them to identify what additional facts would distinguish a result viewer from software that calculates a medically actionable interpretation.

## IVDR: three evidence questions and a continuing evaluation

Article 56 and Annex XIII require performance evaluation tied to intended purpose and sufficient clinical evidence. The manufacturer plans, assesses and documents the evidence, maintaining it through the device lifecycle, including post-market performance follow-up. [IVDR, Article 56 and Annex XIII](https://eur-lex.europa.eu/eli/reg/2017/746/oj/eng).

The evidence components answer distinct questions:

- **Scientific validity:** is the analyte associated with the claimed clinical condition or physiological state?
- **Analytical performance:** can this device correctly detect or measure the analyte?
- **Clinical performance:** do its results correlate with the relevant clinical condition or process in the intended population and for the intended user?

The performance evaluation plan sets the approach; the report brings together scientific-validity, analytical-performance and clinical-performance evidence and their assessment. Clinical performance studies are expected unless reliance on other clinical-performance sources is duly justified. MDCG 2022-2 explains these concepts and the continuing evaluation process; it is guidance rather than binding legislation. [MDCG 2022-2, sections 4 and 6–7](https://health.ec.europa.eu/system/files/2022-01/mdcg_2022-2_en.pdf).

Suggested statistical work: appraise whether published associations match the proposed claim; design repeatability, reproducibility, bias and interference studies; specify clinical comparators, endpoints, missing-data handling and uncertainty. For a hypothetical prediction claim, discuss calibration and external validation. For a threshold claim, discuss sensitivity, specificity and predictive values in the intended population. These are teaching choices to justify, not a universal mandatory checklist for every Lp(a) assay. A strong association in a paper does not establish the performance of the fictional measurement system.

## GDPR: health data, purpose and lawful processing

Identifiable test results and disease-risk information are health data and therefore special-category personal data. Processing needs both an Article 6 lawful basis and an applicable Article 9 exception. Explicit consent is one possible route; healthcare and scientific-research exceptions have their own legal conditions and safeguards. Article 9(2)(j) is not an unrestricted research exemption. [GDPR, Articles 4(15), 6, 9 and 89](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng). The Court confirms that an Article 9 exception does not remove the requirement to satisfy Article 6. [CJEU, C-667/21, paragraphs 71–79](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:62021CJ0667).

Consent must meet the GDPR’s requirements, including specificity, information, freely given agreement and withdrawal. A portal checkbox is not blanket permission for future research or marketing. Pseudonymisation separates identifying information and protects it with safeguards; a coded dataset that remains attributable using additional information is still personal data. [GDPR, Articles 4(5), 4(11), 7 and recital 26](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng).

Consent to participate in research and GDPR consent to process data are distinct questions. Other processing grounds may be available, subject to their conditions. [EDPB response on health research, paragraphs 4–10](https://www.edpb.europa.eu/sites/default/files/files/file1/edpb_replyec_questionnaireresearch_final.pdf).

Classroom application: separate result delivery, assay validation and later research as proposed purposes. Have students describe the required data and who determines each purpose. The statistician should ask for an approved data-access arrangement, minimise variables, keep linkage keys outside the analysis workspace and consider disclosure risk in outputs. The exercise should expose which decisions require the controller and privacy team rather than pretending that statistical usefulness supplies legal permission.

## ISO/IEC 27001: managing security within a defined scope

ISO/IEC 27001:2022 specifies requirements for an information security management system (ISMS), using risk management and continual improvement to protect confidentiality, integrity and availability. Certification is optional. [ISO’s official ISO/IEC 27001 overview](https://www.iso.org/standard/27001). ISO standards are voluntary, although other instruments can make their use consequential. [ISO public-policy guidance](https://policy.iso.org/home.html).

Scope matters: an ISMS may cover part of an organisation rather than every activity. Therefore, inspect the actual scope before assuming a certificate covers the portal, laboratory or analysis environment. [ISO/IEC JTC 1/SC 27 advisory note, page 2](https://committee.iso.org/files/live/sites/jtc1sc27/files/resources/ISO-IECJTC1-SC27-WG1_N3083_WG_1_CATF_Advisory_Note_1_-_Why_Is_ISOIEC_27001_Sufficient_for_the_disciplines_of_Information_Security_and_Cybersecurity.pdf).

Suggested exercise: map laboratory exports, portal storage and statistical workspaces onto an imagined ISMS scope. Ask who can change a result, recover a dataset or authorise an export. Statistical tie-ins include versioned datasets, reproducible transformations, access controls and checks against accidental alteration. Security evidence cannot substitute for assay-performance evidence or a processing basis.

## Data Act: conditional product-data rights and two dates

Regulation (EU) 2023/2854 generally applies from **12 September 2025**. Article 50 separately makes Article 3(1)’s design/access obligation applicable to connected products and services related to them placed on the market **after 12 September 2026**. That later date does not postpone the whole Act. Article 3(1) concerns accessible product/service data and relevant metadata, including machine-readable formats. [Data Act, Articles 3(1) and 50](https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng).

Article 1(5) preserves data-protection law: GDPR and relevant privacy law prevail in a conflict. The Act supplies no new permission to process personal data; recital 7 clarifies the limits on collection and disclosure, especially where the user is not the data subject. [Data Act, Article 1(5) and recital 7](https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng).

For Chapter II, establish a qualifying connected product, related service and covered data before asserting access or user-directed sharing rights. A related service has a functional connection to the product; an online portal is not automatically one. Raw and preprocessed data differ from inferred or derived information. [European Commission: Data Act explained, Chapter II](https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained).

Teaching inference: a communicating analyser could raise these questions, but the hypothetical blood test plus portal does not resolve them. Ask students to identify the product, service, user, data holder and patient. A laboratory user may differ from the patient whose data appear in an export. Proposed statistical tie-ins are documenting units, timestamps, provenance and transformations so an authorised recipient can interpret the data without confusing instrument readings with derived risk scores.

## Teacher-ready framework matrix

The responsibilities below are a teaching allocation; actual roles depend on the product and processing arrangements. Framework facts are sourced above.

| Framework | Core question | Responsibility to discuss | Statistician’s contribution |
| --- | --- | --- | --- |
| IVDR | Does evidence support the intended diagnostic purpose? | Manufacturer; study sponsor; relevant assessment bodies | Study design, uncertainty, evidence appraisal, monitoring |
| GDPR | May these health data be processed for this purpose? | Controller; processor within its role; privacy team | Necessary variables, safe linkage, disclosure-aware reporting |
| ISO/IEC 27001 | Are security risks managed within the stated ISMS scope? | Management and security owners | Dataset integrity, reproducibility, controlled access |
| Data Act | Do qualifying users have applicable product-data rights? | Relevant manufacturer, service provider and data holder | Interpretable exports, metadata, provenance |

Close the lesson by giving students one proposed change: the portal adds a risk score and a research export. Ask them to revisit the diagnostic claim, processing purpose, security scope and product/service relationship separately. Require a short evidence plan and a list of missing facts before any classification or scope conclusion.

Source-check method: official pages and PDFs were reviewed; where EUR-Lex direct retrieval returned a verification screen, article text was checked through indexed EUR-Lex extracts. Links identify the official instruments, not an exhaustive assessment of national requirements or product-specific obligations.
