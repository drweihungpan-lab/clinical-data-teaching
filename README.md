# Clinical development for statistics master's students

A six-hour, knowledge-transfer course: three two-hour sessions, no required programming, and few exercises. Start with the [instructor guide](docs/teaching/instructor-guide.md).

| Session | Lesson | Central question |
| --- | --- | --- |
| 1 | [Data processing in clinical trials](docs/teaching/session-1.md) | How does a development question become a clinical study? |
| 2 | [Professional roles, clinical data, and AI](docs/teaching/session-2.md) | Who turns observations into trustworthy evidence? |
| 3 | [Diagnostics and the EU data context](docs/teaching/session-3.md) | What changes when the product measures rather than treats? |

Supporting material:

- [SLN360 public-study case card](docs/teaching/case-study.md) and [professional-role reference](docs/teaching/roles.md).
- [Synthetic CSV database and dictionary](data/synthetic/README.md); [TFL examples](tfl/README.md).
- [Pre-class survey](docs/teaching/pre-class-survey.md), [post-class survey](docs/teaching/post-class-survey.md), and [presentation topics and guidance](docs/teaching/presentations.md).
- [Instructor answers](docs/teaching/answers.md), [source register](docs/teaching/references.md), and [implementation decisions](docs/teaching/implementation-notes.md).

SLN360 is a real published example. The CSVs, their outputs, and the diagnostic product are invented teaching examples, not SLN360 patient data or results. No full CDISC submission package is claimed.

The Markdown lessons separate slide text from instructor notes. Present the short slide bullets; use the notes to explain them in your own words. Mermaid diagrams render on GitHub; CSVs open in a spreadsheet. The generated figure is also available as a standalone SVG.

Editable PowerPoint decks with presenter notes: [slides/README.md](slides/README.md).

Maintainer commands (students do not need these):

```sh
node scripts/generate-teaching-data.mjs
node scripts/validate-materials.mjs
```

For figure regeneration, see [the TFL guide](tfl/README.md). The committed assets are usable without installing anything.
