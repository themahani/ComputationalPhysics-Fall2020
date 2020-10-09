"""
Here lie methods for ouputing as images--aka Graphics. R.I.P
"""

import matplotlib.pyplot as plt
from numpy import max, mean, linspace
from .generate import error


def draw_canvas(canvas, max_height):
    """
    Draw the given table
    """
    fig, ax = plt.subplots(1, 1)
    ax.pcolor(canvas, cmap="Blues")
    ax.set_ylim(0, max(max_height) + 10)
    plt.show()


def draw_variance(variance):
    """
    Plot the variance after finding the error bars :)
    """
    # Find the error bars. Take variance of the data as the error
    yerr = []
    means = []
    for _ in range(variance.shape[1]):
        yerr.append(error(variance[:, _]))
        means.append(mean(variance[:, _]))
    x_coord = linspace(0, variance.shape[1] * 2000, variance.shape[1])
    # Make subplot
    fig, ax = plt.subplots(1, 1)
    # Plot with error bars, errorbar color is default(blue)
    ax.errorbar(x_coord, means, yerr=yerr, ls='--', marker='*',
                markersize=5, markerfacecolor='red', markeredgecolor='black',
                markeredgewidth=0.2)
    # Log scale for x- and y-axis
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
