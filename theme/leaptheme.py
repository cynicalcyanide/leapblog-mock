"""House chart theme for The Leap Journal.

Usage, from any article's first code cell:

    import sys; sys.path.insert(0, "../../theme")
    import leaptheme

    ... build fig ...
    leaptheme.watermark(fig, article="Article Title", citation="Author (Year)")

Importing the module registers the "leap" Plotly template and makes it the
default: house colours, Latin Modern type, hover crosshairs and unified
value readout — authors write plain plotting code with no styling.
"""

import plotly.graph_objects as go
import plotly.io as pio

# Design tokens — keep in sync with theme/leap.scss
INK = "#1f2a24"
INK_SOFT = "#5b6b62"
PAPER = "#faf8f3"
RULE = "#e4e0d5"
COLORWAY = ["#2e5d43", "#a63d40", "#8a6d3b", "#3d5a80", "#5b6b62", "#c9a227"]
SERIF = "Latin Modern, Georgia, serif"
MONO = "IBM Plex Mono, Menlo, monospace"

_axis = dict(
    showspikes=True,
    spikemode="across",
    spikedash="dot",
    spikethickness=1,
    spikecolor=INK_SOFT,
    gridcolor=RULE,
    linecolor=INK,
    ticks="outside",
    tickcolor=INK,
    title_font=dict(family=SERIF, size=13),
)

pio.templates["leap"] = go.layout.Template(
    layout=dict(
        colorway=COLORWAY,
        font=dict(family=SERIF, size=14, color=INK),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="#ffffff",
        hovermode="x unified",
        hoverlabel=dict(font=dict(family=MONO, size=11)),
        xaxis=_axis,
        yaxis=_axis,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, font=dict(family=MONO, size=11)),
        margin=dict(l=10, r=10, t=40, b=70),
    )
)
pio.templates.default = "leap"


def watermark(fig, article, citation):
    """Stamp the journal watermark: a faint diagonal wordmark across the
    plot, and a caption line with the article name and citation below it."""
    fig.add_annotation(
        text="THE LEAP JOURNAL",
        xref="paper", yref="paper", x=0.5, y=0.5,
        showarrow=False, textangle=-20,
        font=dict(family=SERIF, size=42, color="rgba(31,42,36,0.06)"),
    )
    fig.add_annotation(
        text=f"THE LEAP JOURNAL · {article} · {citation}",
        xref="paper", yref="paper", x=0.5, y=-0.22,
        showarrow=False,
        font=dict(family=MONO, size=9, color="rgba(31,42,36,0.5)"),
    )
    return fig
