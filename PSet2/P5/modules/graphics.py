"""
Here lie methods for ouputing as images--aka Graphics. R.I.P
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from .generate import error


def draw_canvas(canvas, max_height):
    """
    Draw the given table
    """
    fig, ax = plt.subplots(1, 1)
    ax.pcolor(canvas, cmap="RdBu")
    ax.set_ylim(0, np.max(max_height) + 10)
    # Save to fig
    plt.savefig("canvas.jpg", dpi=500, bbox_inches='tight')


def power_func(x, a, beta):
    return a * np.power(x, beta)


def find_opt(func, data):
    """
    Find the optimization params form data and function
    """
    x_dummy = np.linspace(0, len(data) * 2000, len(data))
    popt_params, pcov_params = curve_fit(func, x_dummy, data)
    return popt_params, pcov_params


def draw_variance(variance):
    """
    Plot the variance after finding the error bars :)
    """
    # Find the error bars. Take variance of the data as the error
    yerr = []
    means = []
    for _ in range(variance.shape[1]):
        yerr.append(error(variance[:, _]))
        means.append(np.mean(variance[:, _]))
    x_coord = np.linspace(0, variance.shape[1] * 2000, variance.shape[1])
    # Make subplot
    fig, ax = plt.subplots(1, 1)
    # Plot with error bars, errorbar color is default(blue)
    ax.errorbar(x_coord, means, yerr=yerr, ls='', marker='*',
                markersize=5, markerfacecolor='red', markeredgecolor='black',
                markeredgewidth=0.2, label='scatter data')
    # Find the curve fit and plot it
    popt, pcov = find_opt(power_func, means)
    y_fit = popt[0] * np.power(x_coord, popt[1])
    plt.plot(x_coord, y_fit, ls='-.', color='green',
             label='Curve fit (a * x^beta)')
    # Log scale for x- and y-axis
    plt.xscale('log')
    plt.yscale('log')
    # axis labels
    ax.set_xlabel("Time (unit = number of particles depositted)")
    # Show legend
    plt.legend()
    # Save to fig
    plt.savefig("plot_for_beta.jpg", dpi=500, bbox_inches='tight')
    # Calculate standard deviation for params (sqrt of the diagonal
    # of the covariance)
    stdev = np.sqrt(np.diag(pcov))

    return popt, stdev
