# Tables, figures, and listings

Start with [the generated example collection](examples.md). **Everything in that collection is invented EDU-LPA-001 teaching data, not published SLN360 results.**

| Output | Teaching purpose | Source |
| --- | --- | --- |
| Participant-characteristics table | Recognize population and baseline summaries | DM and participant-level analysis illustration |
| Adverse-event table | Distinguish event records from affected participants and show denominators | AE plus exposure/participant context |
| Lp(a) figure | Recognize a trajectory and the changing observed denominator | Longitudinal analysis illustration |
| Patient listing | Inspect records and see how missingness is communicated | Selected longitudinal records |

The separate [public SLN360 case card](../docs/teaching/case-study.md) links to the study's published Table 1, Table 2, and Figure 2. Use those as real reporting examples by opening the article. The repo does not copy its figures, use its patient data, or present our invented outputs as reproductions of that trial.

## Regeneration for maintainers

```sh
node scripts/generate-teaching-data.mjs
python3 scripts/plot-teaching-figure.py
node scripts/validate-materials.mjs
```

The plot command requires Matplotlib (`python3 -m pip install matplotlib` in a virtual environment is one option). It reads the generated figure CSV and writes [lpa-over-time.svg](lpa-over-time.svg). All assets are committed for immediate use, so students and instructors do not need Python or Matplotlib to view them.

Interpretation boundaries: no imputation, no modeled treatment contrast, no confidence intervals, and no inference that the invented effects represent SLN360. The safety terms are plain-language observations, not MedDRA-coded summaries. Formal clinical-report production would require additional specifications, metadata, validation, and review.
