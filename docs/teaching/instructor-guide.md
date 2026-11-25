# Instructor guide

## Purpose and learning outcomes

Students know statistical inference and regression. They may not know what a trial protocol is, where clinical data come from, or how industry teams work together. By the end they should be able to:

1. Explain the purpose of trial phases, protocol, endpoints, randomization, blinding, and safety monitoring.
2. Distinguish the main responsibilities and handoffs of biostatisticians, data scientists, statistical programmers, and data managers, with supporting awareness of governance, QA, RA, and clinical teams.
3. Explain the purpose of SDTM, analysis-ready data, and TFLs without constructing them.
4. Interpret an early-development result and say what it does not establish.
5. Compare a documented AI milestone with a documented setback, without treating either as proof about all AI-developed drugs.
6. Recognize how evidence, privacy, security, and data access interact in an EU diagnostic-product context.

The clinical-data backbone is clinical question → trial design → collected observations → standardized data → analysis-ready data → TFLs → development decision. Statistics informs both the question and the interpretation; it is not a last step appended to data collection.

## Before teaching

- Read the [SLN360 card](case-study.md), [source register](references.md), and the two research notes linked there. Recheck sources before a later delivery: the course uses dated published findings, not a claim about the latest pipeline status.
- Send the [pre-class survey](pre-class-survey.md) before session 1. It takes about three minutes; use it to adjust vocabulary and examples, not to grade students.
- Open the three lessons, [roles](roles.md), [data dictionary](../../data/synthetic/data-dictionary.md), and [TFL collection](../../tfl/README.md). Download CSVs for offline use.
- Have the published study page ready, including its Table 1, Table 2, and Figure 2. Link to published assets; do not assume you may redistribute journal figures.
- After session 1, assign the [ClinicalTrials.gov take-home exercise](presentations.md#after-session-1-take-home-exercise--why-did-these-trials-stop) to every student and pick two presenters at the start of session 2. After session 2, use the [presentation guidance](presentations.md): choose one speaker per topic and record the choices before leaving.

## Delivery and pacing

Each slot is 120 minutes, including a ten-minute break. Session 2 reserves 25 minutes for two take-home-exercise presentations plus class discussion; session 3 reserves the maximum 30 minutes for three 5–10-minute presentations. Shorter presentations release time for explanation, not extra required content.

| Session | Blocks in minutes | Total |
| --- | --- | --- |
| 1 | Welcome 3; opening scenario 10; trial foundations 17; phases, success rates, and development decisions 25; break 10; industry journey 20; SLN360 discussion 20; recap and topic choices 15 | 120 |
| 2 | Two exercise presentations and discussion 25; roles and workflow 20; data/TFL demonstration 25; break 10; RWD and AI cases 30; recap and topic choices 10 | 120 |
| 3 | Presentations 30; diagnostic-product contrast 20; break 10; four-framework map 25; cross-team scenario 15; synthesis, survey, and optional topics 20 | 120 |

Feedback is brief and embedded in transitions: offer one strength and one evidence/interpretation correction. Do not add a separate 15-minute feedback block. If a presentation runs toward ten minutes, shorten examples, not the break or the final recap.

Each lesson has a few check questions; ask them aloud or by a show of hands. The missing-lab demonstration is instructor-led. The final integrative prompt is a five-minute discussion, not a large assignment. [Answers](answers.md) are instructor-only until after the discussion.

## What to emphasize and what to skip

Emphasize the reason for each stage, accountable roles, how teams communicate, and what decisions evidence supports. Give the four core statistical/data roles most of the attention. QA, RA, governance, and the legal/security frameworks are brief context.

Do not teach variable-level SDTM mapping, ADaM derivations, audit preparation, ISO certification, coding, or formal legal interpretation. The dataset generator and derivation notes exist so teaching examples are coherent; they are not required student reading.

Use your own experience to explain work patterns, but distinguish personal experience from the published SLN360 study and avoid adding nonpublic study details. Actual drug-development results, fictional examples, and AI cases occupy separate sections.

## Practical defaults and instructor review

The requested implementation proceeds with these reversible defaults: English material; anonymous surveys bracketing the full course; ungraded presentations with feedback; topics chosen voluntarily with the instructor resolving clashes; final-session topics are optional take-home reflection with no fourth meeting. Session spacing is not assumed. If students have no preparation interval, let them present a short interpretation of the supplied source instead of a new literature search.

Review the selected AI cases, fictional diagnostic intended use, timing, and survey/presentation defaults before delivering the course. These are material choices implemented for review, not claims that every open planning issue has been human-approved and closed.
