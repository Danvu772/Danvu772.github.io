# matplotlib-theme.py
# Void Protocol — matplotlib rcParams
# Drop this in your notebook with: exec(open('path/to/matplotlib-theme.py').read())
# Or import it: from assets.matplotlib_theme import *

import matplotlib.pyplot as plt
import matplotlib as mpl

# ============================================================
# VOID PROTOCOL COLOR PALETTE
# ============================================================
VP_BG         = "#050508"
VP_BG_SURFACE = "#0a0d12"
VP_BG_AXES    = "#0a0d12"
VP_BORDER     = "#1a1f2e"
VP_TEXT       = "#7a8694"
VP_TEXT_BRIGHT= "#e2e8f0"
VP_TEXT_MUTED = "#4a5260"
VP_ACCENT     = "#06b6d4"   # ice cyan — primary line/accent
VP_GREEN      = "#4ade80"
VP_RED        = "#f87171"
VP_YELLOW     = "#fbbf24"
VP_ORANGE     = "#fb923c"
VP_PURPLE     = "#a78bfa"
VP_PINK       = "#f472b6"

# Color cycle for multi-line plots
VOID_CYCLE = [
    VP_ACCENT,   # cyan — default first line
    VP_GREEN,    # green
    VP_PURPLE,   # purple
    VP_ORANGE,   # orange
    VP_PINK,     # pink
    VP_YELLOW,   # yellow
    VP_RED,      # red
    "#67e8f9",   # light cyan
    "#86efac",   # light green
    "#c4b5fd",   # light purple
]

def apply_void_theme(mode="dark"):
    """
    Apply Void Protocol theme to matplotlib.

    Args:
        mode: "dark"  — full dark bg (for website/HTML)
              "print" — white bg, adapted colors (for PDF submission)
    """

    if mode == "dark":
        bg          = VP_BG
        bg_axes     = VP_BG_AXES
        text_color  = VP_TEXT
        text_bright = VP_TEXT_BRIGHT
        grid_color  = VP_BORDER
        spine_color = VP_BORDER
        cycle       = VOID_CYCLE
        accent      = VP_ACCENT

    elif mode == "print":
        bg          = "#ffffff"
        bg_axes     = "#f8fafc"
        text_color  = "#334155"
        text_bright = "#0f172a"
        grid_color  = "#e2e8f0"
        spine_color = "#cbd5e1"
        accent      = "#0891b2"
        cycle       = [
            "#0891b2",  # teal
            "#16a34a",  # green
            "#7c3aed",  # purple
            "#ea580c",  # orange
            "#be185d",  # pink
            "#ca8a04",  # yellow
            "#dc2626",  # red
        ]

    params = {
        # Figure
        "figure.facecolor":         bg,
        "figure.edgecolor":         bg,
        "figure.dpi":               120,
        "figure.figsize":           (8, 4.5),

        # Axes
        "axes.facecolor":           bg_axes,
        "axes.edgecolor":           spine_color,
        "axes.labelcolor":          text_color,
        "axes.titlecolor":          text_bright,
        "axes.titlesize":           13,
        "axes.titleweight":         "600",
        "axes.labelsize":           11,
        "axes.prop_cycle":          mpl.cycler(color=cycle),
        "axes.spines.top":          False,
        "axes.spines.right":        False,
        "axes.linewidth":           0.8,
        "axes.grid":                True,
        "axes.axisbelow":           True,

        # Grid
        "grid.color":               grid_color,
        "grid.linewidth":           0.6,
        "grid.alpha":               1.0,
        "grid.linestyle":           "--",

        # Ticks
        "xtick.color":              text_color,
        "ytick.color":              text_color,
        "xtick.labelsize":          10,
        "ytick.labelsize":          10,
        "xtick.major.width":        0.8,
        "ytick.major.width":        0.8,
        "xtick.direction":          "out",
        "ytick.direction":          "out",

        # Lines
        "lines.linewidth":          1.8,
        "lines.solid_capstyle":     "round",
        "patch.linewidth":          0.8,
        "patch.edgecolor":          bg_axes,

        # Legend
        "legend.facecolor":         bg_axes,
        "legend.edgecolor":         spine_color,
        "legend.labelcolor":        text_color,
        "legend.fontsize":          10,
        "legend.framealpha":        1.0,
        "legend.borderpad":         0.6,

        # Fonts — match JetBrains Mono where possible
        "font.family":              "monospace",
        "font.size":                11,
        "text.color":               text_color,

        # Scatter
        "scatter.edgecolors":       "none",

        # Histogram
        "hist.bins":                "auto",

        # Savefig
        "savefig.facecolor":        bg,
        "savefig.edgecolor":        bg,
        "savefig.dpi":              150,
        "savefig.bbox":             "tight",
        "savefig.pad_inches":       0.1,

        # Image
        "image.cmap":               "viridis",
    }

    mpl.rcParams.update(params)
    print(f"[void-protocol] matplotlib theme applied — mode={mode}")


# ============================================================
# CONVENIENCE: QUICK PALETTE ACCESS
# ============================================================
class VoidColors:
    """Quick access to Void Protocol colors for manual use."""
    cyan    = VP_ACCENT
    green   = VP_GREEN
    red     = VP_RED
    yellow  = VP_YELLOW
    orange  = VP_ORANGE
    purple  = VP_PURPLE
    pink    = VP_PINK
    text    = VP_TEXT_BRIGHT
    muted   = VP_TEXT_MUTED
    bg      = VP_BG
    surface = VP_BG_SURFACE
    cycle   = VOID_CYCLE


# Apply dark mode by default on import
apply_void_theme("dark")
vc = VoidColors()
