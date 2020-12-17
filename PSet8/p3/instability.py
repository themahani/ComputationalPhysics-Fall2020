#!/usr/bin/env python

"""
Here we are to use an algorithm for the charging capacitor problem.
The algorithm is instable for this perticular problem, as we will examine.
"""

import numpy as np
import matplotlib.pyplot as plt


def num_solve(x_init, func, step, time):
    """ take the initial condition and the step and time, return evolution """
    # find count
    count = int(time / step)

    # initializations
    x = np.zeros(count)
    x[0] = x_init

    # first step is euler:
    x[1] = x[0] + step * func(x[0])

    # evolve
    for i in range(1, count - 1):
        x[i + 1] = x[i - 1] + 2 * step * func(x[i])

    return x, count


def x_dot(x):
    """ original equation for charging capacitor """
    return -x


def analytical_sol(x):
    """ function to draw analytical solution """
    return -1 / 300 * np.exp(-x)


def main():
    """ main body """
    # constants
    x_init = - 1 / 300
    end = 15
    step = 0.001

    # integrate numerically
    record, count = num_solve(x_init, x_dot, step, end)
    print(record)

    # time axis
    time = np.linspace(0, end, count)

    # plot both solutions in a graph
    plt.plot(time, record, 'r-.', label='numerical')
    plt.plot(time, analytical_sol(time), 'b--', label='analytical')
    plt.xlabel('tau')
    plt.ylabel('solutions')
    plt.legend()
    plt.savefig('instability.jpg', bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()
