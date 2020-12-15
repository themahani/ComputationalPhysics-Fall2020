#!/usr/bin/env python

""" implement the euler method for numerical integration """

import numpy as np
import matplotlib.pyplot as plt


def x_dot(x):
    return - 1 / 0.003 * x[0] + 1 / 300.0


def euler(x, functions, length):
    """ euler method """
    dt = 0.000001
    n = int(length / dt)
    record = np.zeros(shape=(len(x), int(n)))
    # store initial conditions
    for enum in enumerate(x):
        record[enum[0], 0] = enum[1]

    # run numerical integration
    for time in range(int(n) - 1):
        for i in range(len(x)):
            x[i] += functions[i](x) * dt
            record[i, time + 1] = x[i]

    return record, n


def solution(x):
    return 10 * (1 - np.exp(- x / 0.003))


def main():
    x = [0]
    dots = [x_dot]

    end = 0.0005
    x_record, count = euler(x, dots, end)
    time = np.linspace(0, end, count, endpoint=False)

    plt.plot(time, x_record[0], ls='-.', label='simulation')
    plt.plot(time, solution(time), ls='--', label='analytic sol.')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
