# plot_style.py
import seaborn as sns
import matplotlib.ticker as ticker

PARCHMENT = {
    "axes.facecolor": "#F5EFE0",
    "figure.facecolor": "#F5EFE0",
    "axes.edgecolor": "#8B7355",
    "axes.labelcolor": "#4A3728",
    "xtick.color": "#4A3728",
    "ytick.color": "#4A3728",
    "text.color": "#4A3728",
    "grid.color": "#D4C5A9",
}

NAVY = "#1C2E4A"
RED  = "#C0392B"
FORREST_GREEN ="#3b6e4a"

def set_style(context="notebook"):
    sns.set_theme(style="ticks", context=context, rc=PARCHMENT)