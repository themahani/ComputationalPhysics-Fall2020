"""
Here lie methods for ouputing as images--aka Graphics. R.I.P
"""

import matplotlib.pyplot as plt
import numpy as np
from .generate import error


def draw_canvas(canvas, max_height):
    """
    Draw the given table
    """
    fig, ax = plt.subplots(1, 1)
    ax.pcolor(canvas, cmap="RdBu")
    ax.set_ylim(0, np.max(max_height) + 10)
    ax.set_title("Ballistic Deposition")
    # Save to fig
    plt.savefig("canvas.jpg", dpi=500, bbox_inches='tight')


def plot_dist(dist, x_axis):
    # Find means and error bars
    yerr = []
    means = []
    for _ in range(dist.shape[1]):
        yerr.append(error(dist[:, _]))
        means.append(np.mean(dist[:, _]))
    # Make subplot
    fig, ax = plt.subplots(1, 1)
    # Plot with error bars, errorbar color is default(blue)
    ax.errorbar(x_axis, means, yerr=yerr, ls='', marker='*',
                markersize=5, markerfacecolor='red', markeredgecolor='black',
                markeredgewidth=0.2, label='scatter data')
    # Axis Labels
    ax.set_xlabel("Time t")
    ax.set_ylabel("Distance of the right most from the left most")
    # Show legend
    plt.legend()
    # Save to fig
    plt.savefig("dist_plot.jpg", dpi=500, bbox_inches='tight')
