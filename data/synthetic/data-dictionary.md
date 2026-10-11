# Teaching-data dictionary

All records are invented. Empty CSV fields mean unavailable/not applicable, not zero. Dates are ISO `YYYY-MM-DD`; units are intentionally explicit. `STUDYID` identifies EDU-LPA-001, while `USUBJID` identifies a participant such as EDU-LPA-007. Names resemble SDTM/ADaM conventions for recognition, without claiming full conformance.

## Shared identifiers and visit fields

| Fields | Meaning |
| --- | --- |
| STUDYID | Invented study identifier |
| DOMAIN | Short domain name in the SDTM-style files |
| USUBJID | Participant identifier shared across files |
| SUBJID | Within-study numeric identifier, retained as a string |
| AESEQ / LBSEQ / VSSEQ / EXSEQ | Record sequence within participant and domain |
| VISIT / AVISIT | Baseline, day 15, day 30, or day 90 label |
| LBDY / VSDY / AESTDY / ADY | Study day; baseline/administration is day 1 |
| LBDTC / VSDTC / AESTDTC / AEENDTC / EXSTDTC | Observation, event, or administration date |

## DM and EX

| Fields | Meaning |
| --- | --- |
| AGE / AGEU | Age and years |
| SEX | Synthetic recorded sex, F or M; only these invented categories appear |
| ARM | Assigned teaching arm: Placebo or Investigational A |
| RFSTDTC / RFENDTC | Day-1 start and day-90 end in this simplified example |
| EXTRT | Administered teaching intervention |
| EXDOSE / EXDOSU | One mL in each arm; invented administration volume, not an SLN360 dose |

## AE, VS, and LB

| Fields | Meaning |
| --- | --- |
| AETERM | Plain-language recorded event; not licensed coded terminology |
| AESEV / AESER | Severity and seriousness; all MILD / N in this example |
| VSTESTCD / VSTEST | SYSBP / systolic blood pressure; PULSE / pulse rate |
| VSORRES / VSORRESU | Recorded vital-sign value and unit (mmHg or beats/min) |
| LBTESTCD / LBTEST | LPA / Lipoprotein(a) |
| LBORRES / LBORRESU | Recorded result and nmol/L unit |
| LBSTRESN / LBSTRESU | Numeric result in the same unit; no conversion is needed in this example |
| LBSTAT / LBREASND | NOT DONE / SPECIMEN NOT AVAILABLE for the one unavailable observation; blank otherwise |

## Simplified analysis-ready fields: instructor/maintainer context

| Fields | Meaning |
| --- | --- |
| TRT01A | Actual teaching arm; all participants received their assignment |
| SAFFL | Y for all 24 participants, identifying the example safety population |
| LPA_BASE / BASE | Observed baseline Lp(a) value |
| PARAMCD | LPA parameter code |
| AVAL | Numeric observed Lp(a), blank for the unavailable observation |
| CHG / PCHG | Difference / percentage difference from baseline, rounded to one decimal; blank when the observation is unavailable |
| OBSFL | Y if observed, N if not done |

The lecture does not teach these derivations. They make the output provenance inspectable for the instructor. Baseline is the day-1 result; changes are relative to that result, not to another participant. No imputation is performed. Participant-level safety denominators are all exposed participants; longitudinal means use observed participants at the visit.

## TFL CSV fields

- `baseline-summary.csv`: arm, participant count, age mean/sample SD, female count, and median baseline Lp(a).
- `safety-summary.csv`: arm, term, denominator, distinct participant count/percentage, and event-record count.
- `lpa-figure-data.csv`: arm, day/visit, observed participant count, observed mean Lp(a).
- `patient-listing.csv`: selected participant, arm, visit, value and explicit observed/not-done status.

No statistical tests, modeled effects, or uncertainty intervals are estimated in these illustrative TFLs.
