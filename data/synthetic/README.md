# Synthetic clinical-data database

**Invented teaching study: EDU-LPA-001. Not SLN360 data or results.** Open the CSV files in a spreadsheet. Students need only recognize the structure and purpose of the files; there is no coding assignment.

The study has 24 participants, 12 assigned to Placebo and 12 to Investigational A, with baseline/day-15/day-30/day-90 visits. Every participant receives one invented 1 mL administration at baseline. One scheduled laboratory sample, EDU-LPA-007 at day 30, is unavailable. All values, dates, event terms, and intervention details are invented.

| File | Rows | Purpose |
| --- | --- | --- |
| [dm.csv](dm.csv) | 24 | Participant characteristics and arm |
| [ex.csv](ex.csv) | 24 | Minimal exposure context: assigned intervention administered |
| [ae.csv](ae.csv) | 7 | Adverse-event records; a participant can have multiple records |
| [vs.csv](vs.csv) | 192 | Two vital-sign measurements at each visit |
| [lb.csv](lb.csv) | 96 | Scheduled Lp(a) observations, including one not-done record |
| [adsl-teaching.csv](adsl-teaching.csv) | 24 | Small participant-level analysis-ready illustration |
| [adlb-teaching.csv](adlb-teaching.csv) | 96 | Small longitudinal analysis-ready illustration |

The first five files use SDTM-style names but intentionally omit many standard variables, domains, controlled terminology, metadata, and submission artifacts. The two analysis-ready files are simplified teaching illustrations, not a full ADaM implementation. CSV is an accessibility choice, not a regulatory submission format claim. No standards certification or production validation is implied.

## Two-minute demonstration

1. Open DM: each row is a participant. Follow `USUBJID` into AE and LB.
2. Open AE: distinguish records from affected participants. EDU-LPA-003 has two headache records.
3. Open LB: find EDU-LPA-007 at day 30. The result is blank and the not-done reason is recorded; it is not zero.
4. Show the analysis-ready file and the [TFL examples](../../tfl/examples.md). Explain purpose and ownership, not individual derivation steps.

See the [dictionary](data-dictionary.md) for fields. For maintainer use only, `node scripts/generate-teaching-data.mjs` regenerates the CSVs and Markdown summaries deterministically. The figure has a separate plotting command in [the TFL guide](../../tfl/README.md). Artifact checks use `node scripts/validate-materials.mjs`.
