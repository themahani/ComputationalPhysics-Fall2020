#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt


def euler(x, functions, length):
    """ euler method """
    n = 100000.0
    dt = length / n
    record = np.zeros(shape=(len(x), int(n)))
    # store initial conditions
    for enum in enumerate(x):
        record[enum[0], 0] = enum[1]

    # run numerical integration
    for time in range(int(n) - 1):
        for i in range(len(x)):
            x[i] += functions[i](x) * dt
            record[i, time + 1] = x[i]

    return record

def x_dot(x):
    return x[1]


def y_dot(x):
    return -x[0]


def main():
    """ main body """
    x = [0, 1]
    funcs = [x_dot, y_dot]
    record = euler(x, funcs, 10)
    time = np.linspace(0, 10, 100000, endpoint=False)

    plt.plot(time, record[0])
    plt.show()



if __name__ == "__main__":
    main()
