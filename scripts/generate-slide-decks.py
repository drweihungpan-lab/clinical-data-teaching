"""Generate editable, speaker-noted PowerPoint decks for the three lessons."""
from pathlib import Path
import csv

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "slides/powerpoint"
OUT.mkdir(parents=True, exist_ok=True)
W, H = 13.333, 7.5
NAVY = "13263D"
INK = "1D3144"
MUTED = "617286"
TEAL = "147D78"
MINT = "DDEFEA"
CORAL = "E77961"
GOLD = "E7B861"
PAPER = "F6F4EF"
WHITE = "FFFFFF"
PALE = "E9EDF1"
FONT = "Aptos"

SOURCES = {
    "fda_phases": "https://www.fda.gov/drugs/investigational-new-drug-application-ind/drug-development-and-review-definitions",
    "fda_gcp": "https://www.fda.gov/regulatory-information/search-fda-guidance-documents/e6r3-good-clinical-practice-gcp",
    "ema": "https://www.ema.europa.eu/en/about-us/what-we-do/authorisation-medicines",
    "sln": "https://jamanetwork.com/journals/jama/fullarticle/2790912",
    "sdtm": "https://www.cdisc.org/standards/foundational/sdtm",
    "adam": "https://www.cdisc.org/standards/foundational/adam",
    "rentosertib": "https://www.nature.com/articles/s41591-025-03743-2",
    "dsp": "https://www.sumitomo-pharma.com/ir/library/presentation/assets/pdf/eir20220131.pdf",
    "ivdr": "https://eur-lex.europa.eu/eli/reg/2017/746/oj/eng",
    "gdpr": "https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng",
    "iso": "https://www.iso.org/standard/27001",
    "dataact": "https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng",
    "ema_device": "https://www.ema.europa.eu/en/human-regulatory-overview/medical-devices",
    "mdcg": "https://health.ec.europa.eu/system/files/2022-01/mdcg_2022-2_en.pdf",
    "replication": "https://www.nature.com/articles/483531a",
    "fda_preclinical": "https://www.fda.gov/patients/drug-development-process/step-2-preclinical-research",
    "ich_m3": "https://database.ich.org/sites/default/files/M3_R2__Guideline.pdf",
    "ind": "https://www.ecfr.gov/current/title-21/chapter-I/subchapter-D/part-312/subpart-B/section-312.40",
    "eu_ctr": "https://eur-lex.europa.eu/eli/reg/2014/536/oj/eng",
    "ich_e6": "https://admin.ich.org/sites/default/files/inline-files/ICH_E6%28R3%29_Step%204_Presentation_2025_0123.pdf",
}
SOURCE_LABELS = {
    "fda_phases": "FDA · drug development", "fda_gcp": "FDA · Good Clinical Practice",
    "ema": "EMA · medicine authorization", "sln": "Nissen et al. · JAMA 2022",
    "sdtm": "CDISC · SDTM", "adam": "CDISC · ADaM",
    "rentosertib": "Nature Medicine · rentosertib phase 2a",
    "dsp": "Sumitomo Pharma · public disclosure", "ivdr": "EU In Vitro Diagnostic Regulation",
    "gdpr": "EU General Data Protection Regulation", "iso": "ISO/IEC 27001",
    "dataact": "EU Data Act", "ema_device": "EMA · medical devices",
    "mdcg": "European Commission · MDCG guidance",
    "replication": "Begley & Ellis · Nature 2012",
    "fda_preclinical": "FDA · preclinical research", "ich_m3": "ICH M3(R2)",
    "ind": "21 CFR 312.40", "eu_ctr": "EU Clinical Trials Regulation 536/2014",
    "ich_e6": "ICH E6(R3)",
}

def rgb(hex_value):
    return RGBColor.from_string(hex_value)

def shape(slide, kind, x, y, w, h, fill, line=None, radius=False):
    obj = slide.shapes.add_shape(kind, Inches(x), Inches(y), Inches(w), Inches(h))
    obj.fill.solid()
    obj.fill.fore_color.rgb = rgb(fill)
    obj.line.fill.background() if line is None else None
    if line:
        obj.line.color.rgb = rgb(line)
        obj.line.width = Pt(1)
    return obj

def textbox(slide, text, x, y, w, h, size=18, color=INK, bold=False,
            font=FONT, align=PP_ALIGN.LEFT, valign=MSO_ANCHOR.TOP, margin=0.02):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(margin)
    tf.margin_top = tf.margin_bottom = Inches(margin)
    tf.vertical_anchor = valign
    p = tf.paragraphs[0]
    p.alignment = align
    p.space_after = Pt(0)
    run = p.add_run()
    run.text = text
    run.font.name = font
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = rgb(color)
    return box

def add_notes(slide, notes, source_links=()):
    content = notes.strip()
    if source_links:
        content += "\n\nSources (open in browser):\n" + "\n".join(source_links)
    slide.notes_slide.notes_text_frame.text = content or "Teaching slide."

def source_caption(source):
    labels = [SOURCE_LABELS[key] for key in source.split(",") if key in SOURCE_LABELS]
    return "Source: " + " · ".join(labels) if labels else source

def new_slide(prs, title, section, num, total, source=""):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    bg = slide.background.fill
    bg.solid()
    bg.fore_color.rgb = rgb(PAPER)
    shape(slide, MSO_SHAPE.RECTANGLE, 0, 0, W, 0.09, TEAL)
    textbox(slide, section.upper(), 0.62, 0.34, 10, 0.25, 9, TEAL, True)
    textbox(slide, title, 0.62, 0.73, 12.0, 0.62, 28, NAVY, True)
    shape(slide, MSO_SHAPE.RECTANGLE, 0.62, 1.47, 0.63, 0.045, CORAL)
    shape(slide, MSO_SHAPE.RECTANGLE, 0, 7.17, W, 0.33, NAVY)
    textbox(slide, "CLINICAL DEVELOPMENT  •  STATISTICS MASTER'S", 0.64, 7.22, 8.4, 0.15, 8, WHITE, True)
    textbox(slide, f"{num:02d} / {total:02d}", 11.55, 7.20, 1.10, 0.18, 9, WHITE, True, align=PP_ALIGN.RIGHT)
    if source:
        textbox(slide, source, 0.65, 6.91, 12.0, 0.18, 8, MUTED)
    return slide

def card(slide, x, y, w, h, title, body, accent=TEAL, label=None, body_size=16):
    shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h, WHITE)
    shape(slide, MSO_SHAPE.RECTANGLE, x, y + 0.12, 0.065, h - 0.24, accent)
    top = y + 0.22
    if label:
        textbox(slide, label.upper(), x + 0.24, top, w - 0.48, 0.22, 8, accent, True)
        top += 0.30
    textbox(slide, title, x + 0.24, top, w - 0.48, 0.42, 17, NAVY, True)
    textbox(slide, body, x + 0.24, top + 0.50, w - 0.48, h - (top - y) - 0.61, body_size, INK)

def bullet_list(slide, items, x=0.85, y=1.95, w=11.6, size=21, gap=0.86,
                color=INK, accent=TEAL):
    for i, item in enumerate(items):
        yy = y + i * gap
        shape(slide, MSO_SHAPE.OVAL, x, yy + 0.11, 0.17, 0.17, accent if i % 2 == 0 else CORAL)
        textbox(slide, item, x + 0.34, yy, w - 0.34, gap - 0.08, size, color)

def section_cover(prs, title, subtitle, session_no, duration, outcomes, case_line):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = rgb(NAVY)
    shape(slide, MSO_SHAPE.RECTANGLE, 0.7, 0.75, 0.12, 5.8, TEAL)
    shape(slide, MSO_SHAPE.OVAL, 10.0, -0.6, 4.6, 4.6, "1D394D")
    shape(slide, MSO_SHAPE.OVAL, 10.9, 4.2, 3.3, 3.3, "1A474B")
    textbox(slide, f"SESSION {session_no}   /   {duration}", 1.12, 0.88, 7.0, 0.3, 11, "76D0C2", True)
    textbox(slide, title, 1.10, 1.48, 10.9, 1.52, 36, WHITE, True)
    textbox(slide, subtitle, 1.13, 3.15, 10.0, 0.55, 19, "D8E4EA")
    shape(slide, MSO_SHAPE.RECTANGLE, 1.13, 4.05, 0.75, 0.055, CORAL)
    textbox(slide, "TODAY'S TAKEAWAY", 1.14, 4.35, 3.5, 0.25, 9, "76D0C2", True)
    textbox(slide, outcomes, 1.13, 4.72, 10.4, 0.66, 20, WHITE, True)
    textbox(slide, case_line, 1.14, 5.75, 10.8, 0.45, 12, "C8D5DC")
    textbox(slide, "DATA PROCESSING IN CLINICAL TRIALS  ·  MASTER'S LEVEL", 1.13, 7.0, 9.8, 0.2, 8, "C8D5DC", True)
    add_notes(slide, f"Open by stating the outcome: {outcomes}\n\nConnect to the course: {case_line}")

def agenda_slide(prs, title, items, section, number, total, notes=""):
    slide = new_slide(prs, title, section, number, total)
    left, top, usable, gap = 0.84, 1.93, 11.65, 0.59
    block = usable / len(items)
    for i, (time, label, desc) in enumerate(items):
        x = left + i * block
        shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, x, top, block - 0.12, 3.65, WHITE)
        shape(slide, MSO_SHAPE.RECTANGLE, x, top, block - 0.12, 0.09, TEAL if i != 1 else CORAL)
        textbox(slide, time, x + 0.18, top + 0.30, block - 0.42, 0.35, 13, TEAL, True)
        textbox(slide, label, x + 0.18, top + 0.85, block - 0.42, 0.72, 17 if len(items) <= 6 else 14, NAVY, True)
        textbox(slide, desc, x + 0.18, top + 1.78, block - 0.42, 1.5, 12, MUTED)
    add_notes(slide, notes or "Use this as a map, not a promise to spend equal time on every item.")
    return slide

def cards_slide(prs, title, cards, section, number, total, notes="", source="", cols=2):
    slide = new_slide(prs, title, section, number, total, source_caption(source))
    rows = (len(cards) + cols - 1) // cols
    gap_x, gap_y = 0.25, 0.24
    x0, y0, width, height = 0.72, 1.78, 11.9, 4.9
    cw = (width - gap_x * (cols - 1)) / cols
    ch = (height - gap_y * (rows - 1)) / rows
    colors = [TEAL, CORAL, GOLD, "4F78A3"]
    for i, entry in enumerate(cards):
        row, col = divmod(i, cols)
        x, y = x0 + col * (cw + gap_x), y0 + row * (ch + gap_y)
        card(slide, x, y, cw, ch, entry[0], entry[1], colors[i % len(colors)],
             label=entry[2] if len(entry) > 2 else None,
             body_size=14 if rows > 1 else 16)
    add_notes(slide, notes, [SOURCES[k] for k in source.split(",") if k in SOURCES])
    return slide

def scenario_slide(prs, title, story, questions, section, number, total, notes="", source=""):
    slide = new_slide(prs, title, section, number, total, source_caption(source))
    shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, 0.82, 1.85, 11.65, 2.35, WHITE)
    shape(slide, MSO_SHAPE.RECTANGLE, 0.82, 1.97, 0.08, 2.11, GOLD)
    textbox(slide, "AN INVENTED SCENARIO", 1.15, 2.05, 6.0, 0.25, 9, GOLD, True)
    textbox(slide, story, 1.15, 2.42, 11.0, 1.65, 22, NAVY)
    textbox(slide, "ASK THE ROOM", 0.85, 4.55, 6.0, 0.25, 9, CORAL, True)
    bullet_list(slide, questions, y=4.90, size=22, gap=0.72, color=NAVY, accent=CORAL)
    add_notes(slide, notes, [SOURCES[k] for k in source.split(",") if k in SOURCES])
    return slide

def two_column_slide(prs, title, columns, section, number, total, notes="", source="", footer=""):
    slide = new_slide(prs, title, section, number, total, source_caption(source))
    x0, top, gap = 0.72, 1.78, 0.30
    col_w = (11.9 - gap) / 2
    for i, (heading, question, items) in enumerate(columns):
        x = x0 + i * (col_w + gap)
        accent = TEAL if i == 0 else CORAL
        shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, x, top, col_w, 4.55, WHITE)
        shape(slide, MSO_SHAPE.RECTANGLE, x, top, col_w, 0.09, accent)
        textbox(slide, heading.upper(), x + 0.28, top + 0.26, col_w - 0.56, 0.28, 11, accent, True)
        textbox(slide, question, x + 0.28, top + 0.58, col_w - 0.56, 0.42, 19, NAVY, True)
        for j, (label, detail) in enumerate(items):
            yy = top + 1.22 + j * 0.80
            shape(slide, MSO_SHAPE.OVAL, x + 0.30, yy + 0.08, 0.15, 0.15, accent)
            textbox(slide, label, x + 0.58, yy, col_w - 0.86, 0.30, 15, NAVY, True)
            textbox(slide, detail, x + 0.58, yy + 0.31, col_w - 0.86, 0.42, 12, MUTED)
    if footer:
        textbox(slide, footer, 0.9, 6.45, 11.5, 0.35, 14, TEAL, True, align=PP_ALIGN.CENTER)
    add_notes(slide, notes, [SOURCES[k] for k in source.split(",") if k in SOURCES])
    return slide

def flow_slide(prs, title, stages, section, number, total, notes="", source="",
               tagline="A HANDOFF IS A CONVERSATION ABOUT PURPOSE, QUALITY, AND WHAT THE NEXT TEAM NEEDS."):
    slide = new_slide(prs, title, section, number, total, source_caption(source))
    count = len(stages)
    x0, top, gap = 0.65, 2.55, 0.14
    box_w = (12.0 - gap * (count - 1)) / count
    for i, (label, detail) in enumerate(stages):
        x = x0 + i * (box_w + gap)
        shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, x, top, box_w, 1.8,
              MINT if i % 2 == 0 else WHITE)
        textbox(slide, f"{i + 1:02d}", x + 0.16, top + 0.16, 0.45, 0.25, 10, TEAL, True)
        textbox(slide, label, x + 0.16, top + 0.55, box_w - 0.32, 0.52, 14, NAVY, True, align=PP_ALIGN.CENTER)
        textbox(slide, detail, x + 0.14, top + 1.14, box_w - 0.28, 0.50, 10, MUTED, align=PP_ALIGN.CENTER)
        if i < count - 1:
            textbox(slide, "›", x + box_w - 0.03, top + 0.72, gap + 0.08, 0.35, 20, CORAL, True, align=PP_ALIGN.CENTER)
    textbox(slide, tagline, 1.0, 5.15, 11.3, 0.55, 17, TEAL, True, align=PP_ALIGN.CENTER)
    add_notes(slide, notes, [SOURCES[k] for k in source.split(",") if k in SOURCES])
    return slide

def table_slide(prs, title, headers, rows, section, number, total, notes="", source="", widths=None):
    slide = new_slide(prs, title, section, number, total, source_caption(source))
    x, y, w, h = 0.75, 1.88, 11.83, 4.85
    table = slide.shapes.add_table(len(rows) + 1, len(headers), Inches(x), Inches(y), Inches(w), Inches(h)).table
    if widths:
        for col, value in zip(table.columns, widths):
            col.width = Inches(value)
    for ri in range(len(rows) + 1):
        for ci in range(len(headers)):
            cell = table.cell(ri, ci)
            cell.fill.solid()
            cell.fill.fore_color.rgb = rgb(NAVY if ri == 0 else (WHITE if ri % 2 else "E9EFED"))
            cell.margin_left = cell.margin_right = Inches(0.13)
            cell.margin_top = cell.margin_bottom = Inches(0.06)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.text = headers[ci] if ri == 0 else str(rows[ri - 1][ci])
            for p in cell.text_frame.paragraphs:
                p.font.name = FONT
                p.font.size = Pt(12 if len(headers) > 3 else 14)
                p.font.bold = ri == 0
                p.font.color.rgb = rgb(WHITE if ri == 0 else INK)
    add_notes(slide, notes, [SOURCES[k] for k in source.split(",") if k in SOURCES])
    return slide

def image_slide(prs, title, image, section, number, total, notes="", source=""):
    slide = new_slide(prs, title, section, number, total, source_caption(source))
    slide.shapes.add_picture(str(image), Inches(1.15), Inches(1.78), width=Inches(11.0))
    add_notes(slide, notes, [SOURCES[k] for k in source.split(",") if k in SOURCES])
    return slide

def bullets_slide(prs, title, items, section, number, total, notes="", source="", callout=None):
    slide = new_slide(prs, title, section, number, total, source_caption(source))
    count = len(items)
    bullet_list(slide, items, y=1.93, size=20 if count <= 4 else 18,
                gap=min(0.95, 4.55 / count))
    if callout:
        shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, 0.82, 5.95, 11.65, 0.61, MINT)
        textbox(slide, callout, 1.0, 6.10, 11.25, 0.32, 13, TEAL, True)
    add_notes(slide, notes, [SOURCES[k] for k in source.split(",") if k in SOURCES])
    return slide

def make_prs():
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(W), Inches(H)
    prs.core_properties.author = "Clinical Data Teaching"
    prs.core_properties.subject = "Six-hour course for statistics master's students"
    prs.core_properties.keywords = "clinical trials, biostatistics, data science, synthetic teaching data"
    return prs

def synthetic_figure():
    path = ROOT / "slides/powerpoint/.lpa-synthetic-preview.png"
    with (ROOT / "tfl/lpa-figure-data.csv").open(newline="") as stream:
        records = list(csv.DictReader(stream))
    fig, ax = plt.subplots(figsize=(10.0, 4.15), layout="constrained")
    for arm, color in [("Placebo", "#617286"), ("Investigational A", "#147D78")]:
        rows = [row for row in records if row["ARM"] == arm]
        days = [int(row["DAY"]) for row in rows]
        means = [float(row["MEAN_LPA"]) for row in rows]
        ax.plot(days, means, marker="o", linewidth=2.5, markersize=7, color=color, label=arm)
        for row, day, value in zip(rows, days, means):
            ax.annotate(f'n={row["N_OBSERVED"]}', (day, value), xytext=(0, 9),
                        textcoords="offset points", ha="center", fontsize=8)
    ax.set(title="Observed Lp(a) in fictional EDU-LPA-001", xlabel="Study day",
           ylabel="Observed mean Lp(a), nmol/L")
    ax.set_xticks([1, 15, 30, 90])
    ax.set_ylim(0, 320)
    ax.grid(axis="y", alpha=0.2)
    ax.legend(frameon=False, loc="lower left")
    fig.savefig(path, dpi=190, facecolor="white")
    plt.close(fig)
    return path

def session1():
    prs = make_prs()
    T = 18
    section_cover(prs, "Clinical trials &\nthe industry", "From a mouse-study discovery to evidence and a development decision",
                  1, "2 HOURS", "Understand the trial before analyzing its data.",
                  "Opening: an invented discovery. Real anchor: the published SLN360 phase 1 study. Synthetic records are a separate teaching example.")
    agenda_slide(prs, "A map for the next two hours", [
        ("00–13", "Opening", "A perfect discovery · two directions"),
        ("13–30", "Trial basics", "Protocol · endpoint · bias"),
        ("30–50", "Phases", "Different evidence questions"),
        ("50–60", "Break", "Ten minutes"),
        ("60–80", "Industry journey", "Paper → company → first patient"),
        ("80–105", "SLN360", "Read the actual study design"),
        ("105–120", "Synthesis", "Checks and open topics"),
    ], "Session 1", 2, T, "All blocks, including the break, fit inside 120 minutes. Welcome takes the first three minutes: survey themes and your own route into clinical development.")
    scenario_slide(prs, "A perfect discovery",
        "Dr. Lin, a respected university researcher, finds that blocking protein X stops disease Y in mice. "
        "The study is published in a top journal. Headlines: “Cure found.”",
        ["Could we give this to patients next month?",
         "What is missing between this paper and a clinical trial?"],
        "Opening scenario", 3, T,
        "This scenario is invented; it is not SLN360 or any real program. Read it aloud, then give pairs about three minutes "
        "to list everything that must happen before the first patient is dosed. Collect answers without correcting them. "
        "Push for the less obvious ones: Who pays? Who makes the drug? Will it work in another lab? Then reveal the next slide.")
    two_column_slide(prs, "Two directions: what's missing?", [
        ("Science", "Is it real, and is it safe?", [
            ("Reproducibility", "Will another lab get the same result?"),
            ("Biology", "Does the mouse model reflect the human disease?"),
            ("Safety", "What does it do to the rest of the body? What first dose?"),
            ("Evidence in people", "What to measure, and compared to what?"),
        ]),
        ("Business & operations", "Who pays, and can it get there?", [
            ("Funding", "Grant → patent → biotech → investors → pharma"),
            ("Market", "Unmet need, how many patients, competitors"),
            ("Manufacturing", "Who makes a consistent clinical batch?"),
            ("Permission to start", "Regulators, ethics review, sites"),
        ]),
    ], "Opening scenario", 4, T,
        "Sort each student answer into a column. Make the columns meet: manufacturing and permission to start depend on the "
        "science column's safety and quality data. Data questions sit under each science gap: small animal samples, effects that "
        "may be inflated or may not replicate, a mouse outcome that is not a human endpoint. One industry team reported confirming "
        "only 6 of 53 landmark preclinical cancer findings (Begley & Ellis 2012); present that as one team's experience, not a "
        "universal rate. Close: the first half answers the science column; after the break we follow the business column.",
        "replication", footer="FIRST HALF: THE SCIENCE COLUMN  ·  AFTER THE BREAK: THE BUSINESS COLUMN")
    cards_slide(prs, "A protocol is a shared plan", [
        ("WHO?", "Which people can answer the question?", "Population"),
        ("WHAT?", "Which intervention and comparison?", "Treatment"),
        ("WHEN?", "What is measured, and at which visits?", "Endpoints"),
        ("HOW?", "How will safety and evidence be assessed?", "Analysis"),
    ], "Trial foundations", 5, T, "A protocol links objectives, population, treatment, visits, and measurements. The statistical analysis plan makes analysis methods explicit. A model cannot recover an outcome the study never collected.", "fda_phases", cols=2)
    flow_slide(prs, "The endpoint connects medicine to statistics", [
        ("Clinical question", "What matters to patients?"),
        ("Biomarker", "Biological change"),
        ("Clinical outcome", "How patients feel, function, survive"),
        ("Decision", "What evidence is enough?"),
    ], "Trial foundations", 6, T,
       "An Lp(a) change is a biomarker result; a cardiovascular event is a different kind of outcome. Ask: if the marker changes, what else would you want to know? Discuss duration, safety, and the marker-to-outcome relationship. Point back to Dr. Lin: a mouse result is not a human endpoint.")
    cards_slide(prs, "Three ideas that make comparisons credible", [
        ("Randomization", "Balances measured and unmeasured factors in expectation; small trials can still look imbalanced.", "Fair comparison"),
        ("Blinding", "Reduces effects of knowing an assignment. It is not always feasible for every person or intervention.", "Bias control"),
        ("Safety review", "Participant welfare can change dose escalation or study continuation.", "Oversight"),
    ], "Trial foundations", 7, T, "These methods support interpretable comparisons; none replaces clinical judgment or careful measurement.")
    table_slide(prs, "Phases ask different questions", ["Phase", "Main question", "Evidence emphasis"], [
        ["I", "Can early human exposure be studied safely?", "Close safety, dose and descriptive signals"],
        ["II", "Is there enough activity to choose what comes next?", "Dose, endpoints, uncertainty, feasibility"],
        ["III", "Is the benefit–risk case adequate for the proposed use?", "Planned comparisons; broader evidence"],
        ["IV", "What is learned in wider use?", "Longer-term safety/effectiveness"],
    ], "Drug development", 8, T,
       "These are common purposes, not rigid recipes. Sample sizes are not definitions. Phase I can include patients; never transfer the drug phase model mechanically to devices.", "fda_phases", widths=[1.0, 4.3, 6.4])
    cards_slide(prs, "Development is a sequence of decisions", [
        ("CONTINUE", "Evidence supports asking the next question.", "Next study"),
        ("CHANGE", "Revise dose, population, measure, or plan.", "Adapt the program"),
        ("STOP", "Evidence, safety, or feasibility no longer supports continuation.", "End the program"),
    ], "Drug development", 9, T, "A decision is not itself an effect estimate. A small early study may justify more research without establishing clinical benefit.", cols=3)
    flow_slide(prs, "From paper to company", [
        ("University lab", "Grants fund the discovery"),
        ("Patent", "Tech-transfer office files"),
        ("Spin-out biotech", "Licenses the patent"),
        ("Investors", "Venture funding rounds"),
        ("Market check", "Need · patients · competitors"),
    ], "Industry journey · Dr. Lin", 10, T,
       "Publishing before filing a patent can damage patentability: Europe generally requires absolute novelty, while the US offers a limited grace period for an inventor's own disclosure. A practical hook, not legal training. "
       "Investors ask two things: is the science real (the left column) and could a product matter commercially. Keep the market check to two minutes: who needs it, how many people, what already exists. No pricing or reimbursement today. "
       "A biotech often has one focused program and limited cash, so every study is also a funding milestone. This is one common route; programs can also stay academic longer, license directly to pharma, or be funded by foundations or governments.",
       tagline="A BIOTECH TURNS A PAPER INTO A PROGRAM, AND EVERY STUDY BECOMES A FUNDING MILESTONE.")
    cards_slide(prs, "Getting ready for the first human", [
        ("Pick a candidate", "One specific molecule, not just “blocking protein X.”", "Drug"),
        ("Pharmacology & PK", "Does it reach the target in animals, and how long does it stay?", "Animal data"),
        ("GLP safety studies", "Toxicology, typically in two species for a small molecule; often run by a CRO.", "CRO"),
        ("Clinical batch", "Quality-controlled supply and CMC evidence; often made by a CDMO.", "CDMO"),
        ("Documents", "Investigator's brochure, first protocol, consent, starting-dose rationale.", "Paperwork"),
    ], "Industry journey · Dr. Lin", 11, T,
       "This is preclinical development. For a typical small molecule, repeated-dose toxicity studies in two species, one a non-rodent, generally support early trials (ICH M3(R2)); biologics follow a product-specific approach. "
       "CMC means chemistry, manufacturing, and controls: evidence that each batch is what it claims to be. The first human dose is chosen from animal safety and exposure data with a margin of caution. "
       "A small biotech rarely owns animal facilities or manufacturing plants, which is why CROs and CDMOs exist.",
       "fda_preclinical,ich_m3", cols=3)
    cards_slide(prs, "Permission to start", [
        ("United States", "IND to FDA. The trial may begin 30 days after FDA receives it, unless FDA places a clinical hold.", "FDA"),
        ("European Union", "One clinical-trial application through CTIS; the member states concerned, including ethics review, assess it.", "EU CTR"),
        ("Before dosing", "Ethics/IRB approval, selected sites, contracts, and trial registration.", "Sites"),
    ], "Industry journey · Dr. Lin", 12, T,
       "Regulatory affairs coordinates these submissions; a pre-IND meeting lets a sponsor ask FDA questions before filing. EU trial authorization is a member-state decision, not an EMA approval. "
       "Stress the distinction: permission to start a trial is not approval to market a medicine. Marketing approval comes only after the phases. Do not teach submission procedures.",
       "ind,eu_ctr", cols=3)
    table_slide(prs, "Who carries it further?", ["Organization", "Where it appeared in Dr. Lin's journey", "Connection to data"], [
        ["Biotech", "Turned a paper into a program", "Concentrated assets, partnerships, trade-offs"],
        ["CRO", "Ran safety studies; later runs trials", "Operations, data management, programming"],
        ["CMO / CDMO", "Made the clinical batch", "Batch quality, consistency, CMC evidence"],
        ["Pharma", "Partners, licenses, or acquires, often after early human data", "Larger trials, portfolio, post-market data"],
    ], "Industry journey · Dr. Lin", 13, T,
       "A pharma partner brings money, development experience, and scale for later phases. Link back to the decisions slide: each phase result is also a business decision point. "
       "Company types overlap; this is an orientation model, not a rule based on size or software. Delegation does not erase sponsor oversight.",
       "ich_e6", widths=[2.2, 5.0, 4.6])
    flow_slide(prs, "A measurement crosses several hands", [
        ("Protocol", "Visit and procedure"), ("Site", "Collect specimen"),
        ("Laboratory", "Measure and report"), ("Data team", "Review and resolve"),
        ("Analysis", "Use for a planned question"),
    ], "Industry journey · first patient", 14, T, "Once the trial starts, sites turn plans into observations. A missing result could mean a missed visit, lost specimen, processing problem, or transfer issue. The source and reason matter; the statistician should not invent a value.", "fda_gcp")
    cards_slide(prs, "SLN360: read the study, not just the headline", [
        ("32", "Participants with elevated Lp(a), no known clinical cardiovascular disease.", "Population"),
        ("5 groups", "Placebo plus four single ascending active-dose cohorts.", "Actual design"),
        ("Primary", "Safety and tolerability; Lp(a) change was a secondary outcome.", "Question"),
        ("150 days", "Maximum follow-up for the biomarker measurement.", "Window"),
    ], "Published case · SLN360", 15, T,
       "This is the 2022 published phase 1 APOLLO study. Do not describe it as a generic two-arm confirmatory trial. Open the paper's participant table, adverse-event table, and Lp(a) figure. Never imply the invented EDU-LPA data are actual trial records.", "sln", cols=2)
    slide = table_slide(prs, "What changed in the published Lp(a) result?", ["Group", "Max median change from baseline"], [
        ["Placebo", "−10%"], ["SLN360 30 mg", "−46%"], ["SLN360 100 mg", "−86%"],
        ["SLN360 300 mg", "−96%"], ["SLN360 600 mg", "−98%"],
    ], "Published case · SLN360", 16, T,
       "Reported maximum median percentage change over follow-up in a 32-person phase 1 study. This dose-related biomarker result supports further study; it does not establish fewer cardiovascular events, approval, comprehensive safety, or clinical benefit. These are not treatment-effect estimates with uncertainty intervals.", "sln", widths=[4.3, 7.5])
    bullets_slide(prs, "Read the evidence at the right level", [
        "A published mouse study is a starting point, not permission to treat people.",
        "A biomarker response is not the same endpoint as a cardiovascular event.",
        "A small phase 1 study cannot characterize rare or delayed harms reliably.",
        "Published results are real; the teaching database is invented.",
        "A development decision uses evidence plus safety, feasibility, funding, and judgment.",
    ], "Session 1 · recap", 17, T, "Three oral checks: biomarker vs events; CRO vs sponsor oversight; Dr. Lin's paper vs first human trial (name one science gap and one business gap). Then invite students to pick one of the three presentation topics.", "sln")
    cards_slide(prs, "Three open topics for next session", [
        ("01 · PHASES", "Why does an early result lead to another question rather than settle development?", "Volunteer"),
        ("02 · SLN360", "What do the study question and biomarker result show—and leave open?", "Volunteer"),
        ("03 · SPONSOR + CRO", "How can activities be shared while oversight remains?", "Volunteer"),
    ], "Session 1 · student topics", 18, T, "Choose one volunteer per topic before leaving. Each presentation is 5–10 minutes at the next session. Suggested primary sources appear in presenter notes.", cols=3)
    prs.save(OUT / "session-1-clinical-trials.pptx")

def session2(figure):
    prs = make_prs()
    section_cover(prs, "Roles, clinical data\n& AI", "Who turns observations into evidence—and what can we conclude?",
                  2, "2 HOURS", "Recognize responsibilities, outputs, and handoffs across the data workflow.",
                  "Start with three student presentations. The real clinical example is SLN360; the dataset is invented.")
    agenda_slide(prs, "A map for the next two hours", [
        ("00–30", "Presentations", "Three topics · 5–10 min each"),
        ("30–50", "Core roles", "Outputs and handoffs"),
        ("50–70", "Data → TFL", "Conceptual walkthrough"),
        ("70–80", "Break", "Ten minutes"),
        ("80–110", "RWD + AI", "Feasibility; two evidence cases"),
        ("110–120", "Synthesis", "Checks and topic choices"),
    ], "Session 2", 2, 15, "Presentations are capped at ten minutes each; feedback is brief and embedded.")
    cards_slide(prs, "Four core roles · one evidence chain", [
        ("Biostatistician", "Shapes design and planned inference.", "Question + analysis"),
        ("Data scientist", "Explores patterns; uses RWD to inform design.", "Exploration + feasibility"),
        ("Data manager", "Makes collected observations complete and usable.", "Collection + queries"),
        ("Statistical programmer", "Implements and checks agreed specifications.", "Datasets + TFLs"),
    ], "Professional roles", 3, 15, "These are typical responsibilities. Titles and task allocation vary; tool choice does not define a profession.", cols=2)
    cards_slide(prs, "Design and inference meet exploration", [
        ("Biostatistics", "Start with the clinical question; plan endpoints, comparisons, analysis populations, and interpretation.", "Prespecified"),
        ("Data science", "Explore linked, observational, or multimodal data; estimate feasibility or develop hypotheses.", "Exploratory"),
        ("Shared work", "Either role can contribute to either task; agree the evidence standard and intended decision.", "Collaboration"),
    ], "Professional roles", 4, 15, "Avoid the shorthand 'SAS versus Python.' The role describes the problem and responsibility, not the programming language.", cols=3)
    flow_slide(prs, "The data journey", [
        ("Question", "What must be learned?"), ("Design", "Protocol + collection"),
        ("Observations", "What happened?"), ("SDTM", "Standardized records"),
        ("Analysis data", "Planned inputs"), ("TFLs", "Communicate results"),
        ("Decision", "What next?"),
    ], "Clinical-data workflow", 5, 15, "This is the purpose chain. The lecture does not teach data mapping or variable derivation.", "sdtm,adam")
    cards_slide(prs, "What do the domains help us recognize?", [
        ("DM", "Who took part?", "Participants"), ("AE", "What events were recorded?", "Safety"),
        ("VS", "What vital signs were measured?", "Observations"),
        ("LB", "What lab results were collected?", "Laboratory"),
    ], "Conceptual data example", 6, 15, "Open two or three CSV rows. Follow USUBJID across domains. These are simplified SDTM-style teaching files, not standards-conformant submission datasets.", cols=4)
    cards_slide(prs, "One data point · four different jobs", [
        ("Site / lab", "Was the sample collected and processed?", "Find the source"),
        ("Data manager", "Is the observation present and reconciled?", "Coordinate query"),
        ("Programmer", "How is status represented in the agreed output?", "Implement rule"),
        ("Biostatistician", "Could missingness affect the analysis or conclusion?", "Assess impact"),
    ], "Instructor-led scenario", 7, 15, "Use the unavailable synthetic day-30 result for EDU-LPA-007. A blank is not zero. Leave the record missing if no valid measurement can be recovered. Clinical operations/CRA support site follow-up; QA and RA are not automatically called for every query.", cols=2)
    slide = image_slide(prs, "An invented teaching figure · not SLN360", figure, "Synthetic TFL · EDU-LPA-001", 8, 15,
        "The fictional two-arm study has 24 participants. Values are invented and not calibrated to SLN360. The observed day-30 active-arm denominator is 11 after one unavailable lab result. This descriptive mean uses available observations: no imputation, confidence intervals, or causal treatment-effect claim. Ask students what the changing denominator tells them.")
    cards_slide(prs, "A table, a figure, and a listing answer different needs", [
        ("Baseline table", "Who is represented? Read the columns and summaries.", "Describe"),
        ("Safety table", "How many participants had an event? How many event records?", "Count carefully"),
        ("Biomarker figure", "What pattern appears over time—and with what denominator?", "See trajectory"),
        ("Patient listing", "Which individual record needs review? Is the value missing?", "Inspect detail"),
    ], "TFLs", 9, 15, "Use tfl/examples.md. The event table distinguishes participants from records. The listing is selected illustration, not full study output.", cols=2)
    flow_slide(prs, "RWD can inform recruitment feasibility", [
        ("Eligibility", "State the clinical criteria"),
        ("Data source", "Check coding + coverage"),
        ("Potentially eligible", "Estimate who might qualify"),
        ("Recruitability", "Validate with sites + patients"),
    ], "Real-world data", 10, 15, "A database count is not a recruitable population. Missing measurements, geography, consent, criteria, and competing studies all matter. The numbers in this classroom example are hypothetical.")
    cards_slide(prs, "AI in early drug development", [
        ("Target", "Prioritize biological hypotheses.", "Discovery"),
        ("Molecule", "Propose candidates for synthesis and testing.", "Design"),
        ("Evidence", "Experimental and clinical work test different questions.", "Validation"),
    ], "AI · framing", 11, 15, "AI can contribute proposals; experiments and clinical trials test them. Do not assume AI accelerated any particular program unless the evidence supports that specific claim.")
    cards_slide(prs, "Milestone · rentosertib", [
        ("AI contribution", "Reported target prioritization and molecular design.", "Discovery"),
        ("Human evidence", "Published randomized phase 2a study; 71 participants.", "Clinical"),
        ("Interpretation", "A patient-trial milestone and encouraging signal; further evidence needed.", "What it means"),
    ], "AI · case 1", 12, 15,
       "A treatment trial can address the candidate-versus-placebo question. It does not randomize discovery method, so it cannot establish that AI is superior to conventional discovery. Small, short studies leave efficacy and safety questions.", "rentosertib", cols=3)
    cards_slide(prs, "Setback · DSP-1181", [
        ("AI collaboration", "A discovery collaboration reported entry into phase I.", "Milestone"),
        ("Development stop", "The sponsor later disclosed discontinuation after phase I.", "Setback"),
        ("Evidence boundary", "Public disclosure did not specify which expected criteria were unmet.", "Do not infer cause"),
    ], "AI · case 2", 13, 15,
       "Do not claim efficacy failure, toxicity, or that AI caused the stop. The public disclosure supports a narrower statement. One selected milestone and one selected stop cannot estimate an industry success rate.", "dsp", cols=3)
    cards_slide(prs, "Three claims · three different evidence needs", [
        ("Did the molecule affect patients?", "Randomized clinical comparison, outcome, uncertainty, and follow-up.", "Candidate evidence"),
        ("Did AI improve discovery?", "Comparable projects, measured from a defined starting point, including abandoned programs.", "Method evidence"),
        ("Why did the sponsor stop?", "The stated decision criterion and public evidence about that criterion.", "Decision evidence"),
    ], "Session 2 · interpretation", 14, 15, "Two selectively chosen cases do not provide a denominator. Ask: what exactly succeeded or failed, according to which source?", cols=3)
    cards_slide(prs, "Three open topics for next session", [
        ("01 · MISSING LAB", "Which teams find the source and assess analysis impact?", "Volunteer"),
        ("02 · AI CLAIM", "Rewrite a public claim so it matches the evidence.", "Volunteer"),
        ("03 · RWD", "What separates eligible counts from recruitment feasibility?", "Volunteer"),
    ], "Session 2 · student topics", 15, 15, "One 5–10-minute speaker per topic. The final session offers optional follow-up topics, not a fourth meeting.", cols=3)
    prs.save(OUT / "session-2-roles-data-ai.pptx")

def session3():
    prs = make_prs()
    section_cover(prs, "Diagnostics &\nthe EU data context", "When the product measures rather than treats: evidence, privacy, security, access",
                  3, "2 HOURS", "Name the right evidence question and the collaborators it requires.",
                  "The fictional CardioLab Connect diagnostic product is separate from the real SLN360 study.")
    agenda_slide(prs, "A map for the final two hours", [
        ("00–30", "Presentations", "Three topics · 5–10 min each"),
        ("30–50", "Product claim", "Drug vs diagnostic"),
        ("50–60", "Break", "Ten minutes"),
        ("60–85", "Four frameworks", "Evidence · data · security · access"),
        ("85–100", "Scenario", "Who needs to work together?"),
        ("100–120", "Synthesis", "Survey + reflection"),
    ], "Session 3", 2, 14)
    cards_slide(prs, "Two products · two kinds of question", [
        ("Drug · SLN360", "Does the intervention change a planned clinical or biological outcome?", "Treatment"),
        ("Diagnostic · fictional", "Does the assay measure accurately and support its intended use?", "Measurement"),
    ], "Product context", 3, 14, "The fictional diagnostic product is not part of SLN360 or Silence Therapeutics. Evidence standards follow the product purpose and claim.", cols=2)
    flow_slide(prs, "Start with intended use", [
        ("What is measured?", "Analyte + specimen"),
        ("In whom?", "Population + setting"),
        ("For what purpose?", "Specific clinical claim"),
        ("Who acts?", "User + decision"),
    ], "Diagnostic evidence", 4, 14, "A numeric Lp(a) result and an individualized future-risk score imply different claims. We cannot assign a device class or software status from a vague product label.", "ivdr")
    cards_slide(prs, "IVDR evidence: three questions", [
        ("Scientific validity", "Is the analyte associated with the claimed condition or state?", "Association"),
        ("Analytical performance", "Does the test measure the analyte appropriately?", "Measurement"),
        ("Clinical performance", "Do results support the intended purpose in the intended context?", "Use"),
    ], "EU diagnostic context", 5, 14, "A published biomarker association does not establish the performance of a new test. Evidence is tied to intended purpose; this overview does not classify the fictional device.", "ivdr,mdcg", cols=3)
    cards_slide(prs, "Four frameworks · four practical questions", [
        ("IVDR", "Does evidence support the diagnostic intended purpose?", "Performance evidence"),
        ("GDPR", "Is this personal health data used appropriately for this purpose?", "Data processing"),
        ("ISMS", "How are information-security risks managed within scope?", "Security"),
        ("EU Data Act", "Do applicable connected-product data-access rights arise?", "Data access"),
    ], "EU context · high level", 6, 14, "Brief context for statisticians, not detailed legal training. ISO/IEC 27001 is a reference for an ISMS; certification is not clinical-performance evidence.", "ivdr,gdpr,iso,dataact", cols=2)
    cards_slide(prs, "Health data: purpose before export", [
        ("Define the purpose", "A useful dataset is not permission for every new use.", "Governance"),
        ("Check the data", "Coded or pseudonymized information can remain personal data.", "Privacy"),
        ("Minimize access", "Request only what the approved analysis needs.", "Statistician's role"),
        ("Protect integrity", "Track versions, changes, provenance, and authorized access.", "ISMS connection"),
    ], "Privacy + security", 7, 14, "Involve the controller/privacy and security owners. A portal checkbox is not blanket consent for future research. Applicable conditions depend on context.", "gdpr,iso")
    flow_slide(prs, "Trace an authorized result", [
        ("Assay", "What was measured?"),
        ("Record", "Units + timestamp"),
        ("Portal", "Who can see it?"),
        ("Export", "What data + metadata?"),
        ("Analysis", "What claim can it support?"),
    ], "Data Act + statistical work", 8, 14,
       "Data Act questions depend on identifying a qualifying connected product, related service, user, data holder, and covered data. GDPR remains relevant. An online portal does not automatically settle applicability.", "dataact,gdpr")
    cards_slide(prs, "Who needs to join the conversation?", [
        ("Biostatistician", "Study design, endpoints, uncertainty, interpretation.", "Evidence"),
        ("Data scientist", "Exploration and feasibility questions.", "Analysis"),
        ("Data governance / privacy", "Purpose, access, definitions, safeguards.", "Use"),
        ("QA + RA", "Reliable processes and evidence/regulatory interfaces.", "Support"),
    ], "Cross-team roles", 9, 14, "Keep QA and RA high level. They support but do not replace statistical judgment; legal/security determinations involve their accountable specialists.", cols=2)
    cards_slide(prs, "Instructor-led scenario · proposed research export", [
        ("Question", "A data scientist proposes using hospital Lp(a) results to estimate trial feasibility.", "RWD"),
        ("Statistics", "The biostatistician asks how eligibility and missing measurements are defined.", "Design"),
        ("Governance", "The data controller/privacy and security teams check access and purpose.", "Appropriate use"),
        ("Evidence", "The assay team clarifies what its measurement claim supports.", "Interpret carefully"),
    ], "Instructor-led scenario", 10, 14, "Ask what facts are missing before proposing an analysis. Do not treat this fictional scenario as a legal determination or device classification.", cols=2)
    cards_slide(prs, "Remote and wearable data · keep the claims grounded", [
        ("Collection changes", "Remote participation adds logistics and source questions.", "Operations"),
        ("Streams are messy", "Timing, missingness, device versions, and adherence matter.", "Data quality"),
        ("Endpoints need evidence", "A stream is not automatically a validated endpoint.", "Interpretation"),
    ], "Digital health · brief context", 11, 14, "Use this slide to retain syllabus context. Drug phases, laboratory diagnostics, wearables, and software do not share one automatic pathway.", cols=3)
    cards_slide(prs, "Four questions to take back to your team", [
        ("Claim", "What exactly is the product intended to measure or support?", "Evidence"),
        ("Data", "What was collected, by whom, and with what uncertainty?", "Provenance"),
        ("Access", "Who is authorized to see and use it?", "Governance"),
        ("Conclusion", "What can the results support—and what remains unknown?", "Judgment"),
    ], "Session 3 · synthesis", 12, 14, "Invite brief answers, then administer the post-class survey. Final open topics are optional reflections; there is no fourth session.", cols=2)
    cards_slide(prs, "Closing checks", [
        ("Coded data", "Does coded test-result data necessarily mean anonymous?", "No"),
        ("Security", "Does ISO/IEC 27001 establish clinical performance?", "No"),
        ("Biomarker", "Does biomarker change alone prove clinical benefit?", "No"),
    ], "Session 3 · discussion", 13, 14, "Let students explain one reason for each answer. The goal is to identify the right question and collaborator, not memorize article numbers.", cols=3)
    cards_slide(prs, "Optional follow-up · no fourth class", [
        ("Diagnostic claim", "How does measurement differ from individual risk prediction?", "Read"),
        ("Data reuse", "Why is a useful dataset not automatically available for a new purpose?", "Reflect"),
        ("Careers", "Which core role would you like to explore next?", "Explore"),
    ], "Course close", 14, 14, "Offer these as optional reading/reflection, not a new graded assignment.", cols=3)
    prs.save(OUT / "session-3-diagnostics-eu-data.pptx")

if __name__ == "__main__":
    figure = synthetic_figure()
    session1()
    session2(figure)
    session3()
    figure.unlink(missing_ok=True)
    for item in sorted(OUT.glob("*.pptx")):
        print(f"Generated {item.relative_to(ROOT)} ({item.stat().st_size:,} bytes)")
