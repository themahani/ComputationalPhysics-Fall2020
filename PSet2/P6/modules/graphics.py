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
    ax.set_title("Ballistic Deposition")
    # Save to fig
    plt.savefig("canvas.jpg", dpi=500, bbox_inches='tight')


def draw_variance(x_axis, variance):
    """
    Plot the variance after finding the error bars :)
    """
    # Find the error bars. Take variance of the data as the error
    yerr = []
    means = []
    for _ in range(variance.shape[1]):
        yerr.append(error(variance[:, _]))
        means.append(np.mean(variance[:, _]))
    # Make subplot
    fig, ax = plt.subplots(1, 1)
    # Plot with error bars, errorbar color is default(blue)
    ax.errorbar(x_axis, means, yerr=yerr, ls='', marker='*',
                markersize=5, markerfacecolor='red', markeredgecolor='black',
                markeredgewidth=0.2, label='scatter data')
    # Find the curve fit and plot it
    popt, pcov = np.polyfit(np.log10(x_axis), np.log10(means), 1,
                            full=False, cov=True)

    # Make the fitted data
    # y_fit = np.zeros((x_axis.shape[0], ), dtype=float, order='F')
    # # y_fit = popt[1] * np.power(x_axis, popt[0])
    # for i in range(x_axis.shape[0]):
    #     y_fit[i] = popt[1] + (x_axis[i] * popt[0])
    # print("Values for y_fit: \n", y_fit)
    print("Values for popt:\n", popt)
    # ax.plot(x_axis, y_fit, color='green',
    #         label='Curve fit (a * x^beta)')
    # Log scale for x- and y-axis
    ax.set_xscale('log')
    ax.set_yscale('log')
    # axis labels
    ax.set_xlabel("Time (unit = number of particles depositted)")
    ax.set_ylabel("Roughness -- w(t)")
    # Show legend
    plt.legend()
    # Save to fig
    plt.savefig("plot_for_beta.jpg", dpi=500, bbox_inches='tight')
    # Calculate standard deviation for params (sqrt of the diagonal
    # of the covariance)
    stdev = np.sqrt(np.diag(pcov))

    return popt, stdev
