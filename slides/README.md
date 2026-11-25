# PowerPoint slide decks

Three editable widescreen PowerPoint decks are available below. Each deck contains slide content plus presenter notes. They were designed for projection and a short knowledge-transfer lecture; the linked Markdown lessons remain the fuller instructor script.

- [Session 1 — Data processing in clinical trials](powerpoint/session-1-clinical-trials.pptx)
- [Session 2 — Professional roles, clinical data, and AI](powerpoint/session-2-roles-data-ai.pptx)
- [Session 3 — Diagnostics and the EU data context](powerpoint/session-3-diagnostics-eu-data.pptx)

To regenerate them from the repository root with Python 3.12 or later:

```sh
python3 -m venv .venv-slides
.venv-slides/bin/python -m pip install -r requirements-slides.txt
.venv-slides/bin/python scripts/generate-slide-decks.py
```

The script reads the committed synthetic TFL summaries and figure data. The generated PowerPoint files work without running the script. All synthetic study values are invented and visibly identified as teaching examples; the SLN360 slide cites only published public findings.
