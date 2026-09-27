"""Render original descriptive charts from visual-data.csv; no effect estimates."""

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


directory = Path(__file__).resolve().parent
with (directory / "visual-data.csv").open(newline="") as source:
    records = list(csv.DictReader(source))

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.labelsize": 9,
    "axes.titlesize": 10,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "axes.spines.top": False,
    "axes.spines.right": False,
})


def value(figure, series, measure):
    return next(float(row["value"]) for row in records
                if row["figure"] == figure and row["series"] == series
                and row["measure"] == measure)


fig, ax = plt.subplots(figsize=(6.25, 2.2))
stages = ["Entered 30-day conditions", "Speaking analysis", "Survey analysis"]
for series, offset, colour, hatch in [
    ("Video Call", -0.18, "0.25", None),
    ("Regular lessons", 0.18, "0.86", "///"),
]:
    counts = [value("video-sample", series, stage) for stage in stages]
    positions = [i + offset for i in range(len(stages))]
    ax.barh(positions, counts, height=0.3, color=colour, edgecolor="0.2",
            hatch=hatch, linewidth=0.5, label=series)
    for y, count in zip(positions, counts):
        label = str(int(count))
        if y > 0.5:
            label += f" ({count / 329:.1%})"
        ax.text(count + 5, y, label, va="center", fontsize=8.5)
ax.set_yticks(range(len(stages)), stages)
ax.invert_yaxis()
ax.set_xlim(0, 400)
ax.set_xticks([0, 100, 200, 300])
ax.set_xlabel("Learners (percentage of each condition's initial n = 329)")
ax.spines["left"].set_visible(False)
ax.tick_params(axis="y", length=0)
ax.legend(loc="lower left", bbox_to_anchor=(0, 1.02), ncols=2, frameon=False)
fig.subplots_adjust(left=0.31, right=0.99, bottom=0.23, top=0.83)
fig.savefig(directory / "video-sample.pdf")
plt.close(fig)

fig, axes = plt.subplots(1, 3, figsize=(6.25, 1.9))
panels = [
    ("Episodes", 1, [0, 7500, 15000], ["0", "7,500", "15,000"], ["300", "15,000+"], 18500),
    ("Courses", 1, [0, 10, 20, 30], ["0", "10", "20", "30"], ["2", "25+"], 32),
    ("Daily sessions", 1000000, [0, 2.5, 5], ["0", "2.5", "5"], ["0.5", "5"], 6),
]
for ax, (measure, divisor, ticks, ticklabels, labels, limit) in zip(axes, panels):
    counts = [value("duoradio", series, measure) / divisor
              for series in ["Before scaling", "After scaling"]]
    for y, count, label, colour, hatch in zip(
            [1, 0], counts, labels, ["0.86", "0.25"], ["///", None]):
        ax.barh(y, count, height=0.36, color=colour, edgecolor="0.2",
                hatch=hatch, linewidth=0.5)
        ax.text(count + limit * 0.025, y, label, va="center", fontsize=9)
    ax.set_title(measure.title(), loc="left", fontweight="bold", pad=12)
    ax.set_xlim(0, limit)
    ax.set_ylim(-0.6, 1.6)
    ax.set_yticks([])
    ax.set_xticks(ticks, ticklabels)
    ax.tick_params(axis="x", labelsize=8)
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("Millions per Day" if divisor > 1 else "Count")
fig.legend(handles=[
    Patch(facecolor="0.86", edgecolor="0.2", hatch="///", label="Before Scaling"),
    Patch(facecolor="0.25", edgecolor="0.2", label="After Scaling"),
], loc="upper center", ncols=2, frameon=False, bbox_to_anchor=(0.5, 1.02))
fig.subplots_adjust(left=0.025, right=0.98, bottom=0.24, top=0.70, wspace=0.42)
fig.savefig(directory / "duoradio-scale.pdf")
plt.close(fig)
