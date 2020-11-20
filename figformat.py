def figure_format(fig_width, fig_height=None):
    """
    Parameter
    ---------
    fig_width : float
        figure width in inches
        e.g. 3.4

    fig_height : float
        figure height in inches
        e.g. 3.4

    Returns
    -------
    A tuple with:
    - Float corresponding to figure width and height
    - A dictionary containing several parameters, such as fontsize
      , etc. If fig_width is not set, the default value is 3.4 inch,
      corresponding to the width of a column in a double colomn paper.
    """
    golden_ratio = 1.618  # Aesthetic ratio
    if fig_height is None:
        fig_height = fig_width / golden_ratio

    fig_size = [fig_width, fig_height]
    fontsize = 12
    linewidth = 1.0
    params = {
        "backend": "ps",
        "axes.labelsize": fontsize,
        "axes.titlesize": fontsize,
        "font.size": fontsize,
        "legend.frameon": False,
        "legend.fontsize": fontsize,
        "legend.loc": "best",
        "lines.linewidth": linewidth,
        "xtick.labelsize": fontsize,
        "ytick.labelsize": fontsize,
        "xtick.direction": "in",
        "ytick.direction": "in",
        "xtick.top": True,
        "ytick.right": True,
        "xtick.major.size": linewidth * 3,
        "xtick.major.top": True,
        "xtick.major.width": linewidth / golden_ratio,
        "xtick.minor.size": linewidth,
        "xtick.minor.top": True,
        "xtick.minor.width": linewidth / golden_ratio,
        "ytick.major.size": linewidth * 3,
        "ytick.major.width": linewidth / golden_ratio,
        "ytick.minor.size": linewidth,
        "ytick.minor.width": linewidth / golden_ratio,
        "figure.figsize": fig_size,
        "pgf.texsystem": "pdflatex",
        "font.family": "serif",
        "text.usetex": True,
        "pgf.rcfonts": False,
        "ps.usedistiller": "xpdf",
    }
    return (fig_width, fig_height, params)
