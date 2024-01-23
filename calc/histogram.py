# histogram.py

from os import makedirs, path
import matplotlib.pyplot as plot
from matplotlib.ticker import StrMethodFormatter


def generate_histogram(dataframe, marks_column):
    graph = dataframe.hist(column=marks_column, bins=25, grid=False, figsize=(
        12, 8), color="#128c8a", zorder=2, rwidth=0.9)
    graph = graph[0]

    for x in graph:

        # Despine
        x.spines['right'].set_visible(False)
        x.spines['top'].set_visible(False)
        x.spines['left'].set_visible(False)

        # Switch off ticks
        x.tick_params(axis="both", which="both", bottom="off", top="off",
                      labelbottom="on", left="off", right="off", labelleft="on")

        # Draw horizontal axis lines
        vals = x.get_yticks()
        for tick in vals:
            x.axhline(y=tick, linestyle='dashed',
                      alpha=0.4, color='#ffe5b4', zorder=1)

        # Remove title
        x.set_title("Histogram analaysis")

        # Set x-axis label
        x.set_xlabel(f"Total Marks ({marks_column})",
                     labelpad=20, weight='bold', size=12)

        # Set y-axis label
        x.set_ylabel("Number of students", labelpad=20, weight='bold', size=12)

        # Format y-axis label
        x.yaxis.set_major_formatter(StrMethodFormatter('{x:,g}'))

    makedirs("_plots", exist_ok=True)
    plot.savefig(path.join("_plots", "histogram.png"))
