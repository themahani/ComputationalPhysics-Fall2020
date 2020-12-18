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


def stable_point(x, r):
    """
    repeat the process n times to
    make sure we have reaches fixed points
    """
    n = 1000
    for _ in range(n):
        x = f(x, r)

    return x.copy()


def main():
    """ main body """
    # constants
    n = 1001
    x_0 = np.array([[0.1, 0.3, 0.6, 0.7]]).T
    # r axis
    r_axis = np.linspace(0.1, 1, n)
    # x axis
    x_fix = np.zeros((len(x_0), n))
    # simulate for different r
    for enum in enumerate(r_axis):
        x_fix[:, enum[0]] = stable_point(x_0, enum[1]).T

    print(x_fix)

    plt.plot(r_axis, x_fix[0, :], ls='', marker='o', ms=1)
    plt.plot(r_axis, x_fix[1, :], ls='', marker='o', ms=1)
    plt.plot(r_axis, x_fix[2, :], ls='', marker='o', ms=1)
    plt.plot(r_axis, x_fix[3, :], ls='', marker='o', ms=1)
    plt.xlabel('r')
    plt.ylabel('x_fix')
    plt.title('bifurcation plot')
    plt.show()



if __name__ == "__main__":
    main()
