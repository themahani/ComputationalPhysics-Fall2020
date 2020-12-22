#!/usr/bin/env python

"""
Here, we draw the bifurcation portrait and find values of r where
bifurcations happen
"""

import numpy as np
from matplotlib import pyplot as plt


def f(x, r):
    """ function to find bifurcations for """
    return 4 * r * x * (1 - x)


def stable_point(r):
    """
    repeat the process n times to
    make sure we have reaches fixed points
    """
    n = 1500
    x = np.zeros(n)
    x[0] = np.random.uniform(0, 0.5)
    for i in range(n - 1):
        x[i + 1] = f(x[i], r)

    print(x[-200:])

    return x[-200:]


def main():
    """ main body """
    # constants
    n = 200
    # r axis
    r_axis = np.linspace(0.1, 1, n)

    # x axis
    x_fix = np.array([])

    # simulate for different r
    for enum in enumerate(r_axis):
        # x_fix[200 * enum[0]: 200 * (enum[0] + 1)] = stable_point(enum[1])
        x_fix = np.hstack((x_fix, stable_point(enum[1])))

    print(x_fix)

    # repeat each value of r, 200 times for the plot
    r_axis = np.repeat(r_axis, 200)

    # plot
    plt.plot(r_axis, x_fix, ls='', marker='o', ms=1)
    plt.xlabel('r')
    plt.ylabel('x_fix')
    plt.title('bifurcation plot')
    plt.savefig("bifurcation.jpg", dpi=200, bbox_inches='tight')
    plt.show()



if __name__ == "__main__":
    main()
