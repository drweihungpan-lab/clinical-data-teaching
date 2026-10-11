"""Plot the committed synthetic summary; not a student coding exercise."""
import csv
from io import StringIO
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["svg.hashsalt"] = "EDU-LPA-001"

root = Path(__file__).resolve().parent.parent
with (root / "tfl/lpa-figure-data.csv").open(newline="") as stream:
    records = list(csv.DictReader(stream))

fig, ax = plt.subplots(figsize=(8, 4.8), layout="constrained")
for arm, color in [("Placebo", "#666666"), ("Investigational A", "#006d77")]:
    rows = [row for row in records if row["ARM"] == arm]
    days = [int(row["DAY"]) for row in rows]
    means = [float(row["MEAN_LPA"]) for row in rows]
    ax.plot(days, means, marker="o", color=color, label=arm)
    for row, day, value in zip(rows, days, means):
        ax.annotate(f'n={row["N_OBSERVED"]}', (day, value),
                    xytext=(0, 9 if arm == "Placebo" else -16),
                    textcoords="offset points", ha="center", fontsize=9)
ax.set(title="Invented EDU-LPA-001: observed Lp(a) over time",
       xlabel="Study day", ylabel="Observed mean Lp(a), nmol/L")
ax.set_xticks([1, 15, 30, 90])
ax.set_ylim(0, 300)
ax.grid(axis="y", alpha=0.2)
ax.legend(loc="lower left")
fig.text(0.5, -0.025, "Synthetic teaching data — not SLN360 results. No imputation or inference.",
         ha="center", fontsize=9)
svg = StringIO()
fig.savefig(svg, format="svg", bbox_inches="tight", metadata={"Date": None})
(root / "tfl/lpa-over-time.svg").write_text(
    "\n".join(line.rstrip() for line in svg.getvalue().splitlines()) + "\n"
)
plt.close(fig)
print("Generated tfl/lpa-over-time.svg from committed synthetic summary.")
