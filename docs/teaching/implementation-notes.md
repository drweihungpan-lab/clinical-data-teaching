# Implementation decisions and ticket traceability

This package implements the instructor's explicit request to build from the tickets. It changes the earlier planning-only boundary for this work; it does not automatically close human-in-the-loop issues or claim instructor approval of every new default.

| Planning ticket | Implemented assets |
| --- | --- |
| [Presentation timing and selection](https://github.com/drweihungpan-lab/clinical-data-teaching/issues/3) | Instructor guide; presentation topics, preparation, selection, feedback, final-session follow-up |
| [Lesson sequence and depth](https://github.com/drweihungpan-lab/clinical-data-teaching/issues/4) | Three lessons, role guide, answers, 120-minute schedules |
| [SLN360 and diagnostic case](https://github.com/drweihungpan-lab/clinical-data-teaching/issues/5) | Public case card; separate invented data study and diagnostic product |
| [Synthetic data and TFLs](https://github.com/drweihungpan-lab/clinical-data-teaching/issues/6) | CSV domains/dictionary, small analysis-ready layer, generated TFLs and figure |
| [AI and regulatory evidence](https://github.com/drweihungpan-lab/clinical-data-teaching/issues/7) | Primary-source research notes, source register, session 2/3 case explanations |
| [Surveys and checks](https://github.com/drweihungpan-lab/clinical-data-teaching/issues/8) | Anonymous pre/post course templates, checks and instructor answers |
| [Lesson format](https://github.com/drweihungpan-lab/clinical-data-teaching/issues/9) | Slide bullets separated from instructor notes throughout; working package for instructor review |

## Defaults chosen to make the package usable

- English; Markdown source and CSV data. No LMS, website, mandatory code lab, or slide conversion.
- Three 120-minute slots; presentations are 5–10 minutes each, with 30 minutes reserved in sessions 2 and 3. Each session includes a ten-minute break.
- Surveys before session 1 and at the end of session 3; anonymous, unpaired responses. Compare group patterns without claiming matched individual learning gains.
- Presentations are ungraded; selection is voluntary with instructor allocation if topics overlap. Session-3 topics are optional reflections with no extra meeting.
- The synthetic study has 24 participants, two invented arms, four visits, one missing Lp(a) result, and a few repeated adverse events. It is not SLN360 patient data.
- The diagnostic intended-use example is laboratory Lp(a) measurement with a result portal; no exact classification or conformity-assessment determination is made.

## Checks and remaining instructor choices

Generated data/output consistency and local document links can be checked using the scripts documented in the README. This is a document/data repo with no existing application typechecker or automated test suite. No new test seams were agreed; validation checks the teaching artifacts instead of introducing a software test framework.

The instructor should review case selection, factual framing, presentation/survey defaults, and delivery pacing. Public references are dated and checked for this implementation; recheck changing regulatory and program-status information before a later delivery. Review feedback can be captured on the existing tickets without duplicating the map's decision history.
