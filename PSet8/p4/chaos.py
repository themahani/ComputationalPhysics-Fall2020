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


def tidy_up(arr):
    new_arr = [arr[0]]
    old_value = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > old_value:
            new_arr.append(arr[i])
            old_value = arr[i]

    return new_arr


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
    r_axis= np.repeat(r_axis, 200)

    # plot
    plt.plot(r_axis, x_fix, ls='', marker='o', ms=1)
    plt.xlabel('r')
    plt.ylabel('x_fix')
    plt.title('bifurcation plot')
    plt.savefig("bifurcation.jpg", dpi=200, bbox_inches='tight')
    plt.show()


    # ===================================
    # ==== finding delta and alpha ======
    # ===================================
    index_arr = np.where(x_fix - 0.5 <= 0.01)[0]
    print(index_arr)

    x_cycle = x_fix[index_arr]
    r_cycle = r_axis[index_arr]
    r_cycle = tidy_up(r_cycle)

    print('\n\n\n')
    print('[Info]:main: finding delta: x_cycle =', x_cycle)
    print('[Info]:main: finding delta: r_cycle =', r_cycle)

    print("[Info]:main:finding delta: ", (r_cycle[3] - r_cycle[2]) / (r_cycle[4] - r_cycle[3]) )


if __name__ == "__main__":
    main()
